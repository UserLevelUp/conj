"""Check atlas coverage, local links, image files, and figure provenance."""
from pathlib import Path
import hashlib
import json
import re
import struct
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.git','.recur','work','.venv','__pycache__'}


def main():
    catalog=json.loads((ROOT/'tools/catalog.json').read_text(encoding='utf-8'))
    assert [c['id'] for c in catalog]==[f'C{i:02}' for i in range(1,26)]
    assert [c['id'] for c in catalog if c['status'].startswith('Priority')]==['C03','C06','C07','C13','C15','C17']
    assert len(list(ROOT.glob('main.conjectures.c[0-9][0-9].*.current.md')))==25
    for c in catalog:
        stem=c['id'].lower()
        assert (ROOT/'docs/atlas'/f'{stem}.md').is_file(),stem
        png=(ROOT/'assets'/f'{stem}.png').read_bytes()
        assert png[:8]==b'\x89PNG\r\n\x1a\n',stem
        width,height=struct.unpack('>II',png[16:24])
        assert width>=1000 and height>=500,stem
        ET.parse(ROOT/'assets'/f'{stem}.svg')
    manifest=json.loads((ROOT/'assets/manifest.json').read_text())
    for path,sha in manifest['source_sha256'].items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha, f'Stale atlas input: {path}'
    subset=json.loads((ROOT/'assets/c15-subset.manifest.json').read_text())
    for group in ('source_sha256','artifact_sha256'):
        for path,sha in subset[group].items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==sha, f'Stale C15 figure: {path}'
    ET.parse(ROOT/'assets/c15-subset.svg')
    broken=[]; checked=0
    for path in ROOT.rglob('*.md'):
        if set(path.relative_to(ROOT).parts)&EXCLUDED: continue
        text=path.read_text(encoding='utf-8')
        links=re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)',text)
        links+=re.findall(r'(?:href|src)="([^"]+)"',text)
        for link in links:
            if re.match(r'^(?:https?://|mailto:|#)',link): continue
            target=unquote(link.split('#',1)[0]).strip('<>')
            if not target: continue
            checked+=1
            if not (path.parent/target).exists(): broken.append(f'{path.relative_to(ROOT)} -> {target}')
    assert not broken, '\n'.join(broken)
    print(f'PASS: 25 candidates, six priority cards, atlas and C15 subset provenance, {checked} local links.')


if __name__=='__main__': main()
