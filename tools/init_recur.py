"""Create optional, local Recur discovery capsules; preserve every existing file."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def write_missing(name, text):
    path=ROOT/'.recur'/name
    if path.exists():
        print(f'Preserved {path.name}')
        return
    path.write_text(text,encoding='utf-8')
    print(f'Created {path.name}')


def main():
    (ROOT/'.recur').mkdir(exist_ok=True)
    write_missing('config.toml', '''[reveal]
mode = "single-thread"
entry_suffix = ".recur.md"
trust = "config-first"
max_threads = 1

[reveal.skills.conjecture-analysis]
path = "conjecture-analysis/SKILL.md"
[reveal.skills.recur-expert]
path = "recur-expert/SKILL.md"
[reveal.skills.recur-eventness]
path = "recur-eventness/SKILL.md"

[traits.trace_id]
enabled = true
producer_keywords = "publish,send,emit,enqueue"
consumer_keywords = "subscribe,queuebind,routingkey,consumer"
trigger_keywords = "register(,registerrule,register,routing pattern,*."
''')
    lanes={
        'main.conjectures':('Read the public portfolio and its evidence boundaries','main.conjectures.index.current.md'),
        'main.conjectures.notes':('Read and edit the current findings notebook before adding notes','main.conjectures.analysis.notes.current.md'),
        'main.conjectures.analysis':('Recover the four review gates and candidate review contract','main.conjectures.analysis.current.md'),
        'main.conjectures.discovery':('Review N01 and N02 as preliminary, unverified leads','main.conjectures.discovery.current.md'),
        'main.conjectures.publication':('Explore the public atlas, reproduction commands, and contribution guide','README.md'),
    }
    for lane,ids in [('boolean','C01-C04'),('spectral','C05-C10'),('witness','C11-C14'),('education','C15'),('additive','C16-C20'),('order','C21-C25')]:
        lanes['main.conjectures.'+lane]=(f'Recover {ids} from the statement index and review notebook','main.conjectures.index.current.md')
    for name,(agenda,path) in lanes.items():
        write_missing(name+'.recur.md',f'''# {name}

artifact.type = lane
agenda = {agenda}
pull.first = {path}
pull.then = main.conjectures.evidence.current.md
verify = compare exact statements, primary sources, and current input fingerprints
do.not.disturb = C01 is implied by known theorems; 24 claims remain unresolved here; novelty is unverified
ready.state = public review materials available; no mathematical acceptance inferred
''')


if __name__=='__main__': main()
