#!/usr/bin/env python3
"""Dependency-free structural validation for ReasonCore."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n'), 'Missing YAML frontmatter delimiter'
parts = skill.split('---\n', 2)
assert len(parts) == 3, 'Missing closing frontmatter delimiter'
front = parts[1]
assert '\nname: reasoncore\n' in '\n' + front
assert '\ndescription:' in '\n' + front
assert '## Operating contract' in skill
for filename in ['business.md','engineering.md','personal.md','safety-and-evidence.md','decision-tools.md']:
    assert (ROOT / 'references' / filename).is_file(), f'Missing {filename}'
cases = [json.loads(line) for line in (ROOT / 'evals/cases.jsonl').read_text().splitlines() if line.strip()]
assert len(cases) >= 8
assert len({case['id'] for case in cases}) == len(cases)
assert all(case.get('prompt') and case.get('expect') for case in cases)
print(f'Validated skill, {len(cases)} eval cases, and reference files.')
