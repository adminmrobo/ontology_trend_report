#!/usr/bin/env python3
"""src/index.src.html의 박사 그림 자리(__DOC_E??__)를 캐릭터 팩 그림(192px)으로 채워 index.html을 만든다."""
import json, os, re
root = os.path.join(os.path.dirname(__file__), '..')
s = open(os.path.join(root, 'src', 'index.src.html'), encoding='utf-8').read()
sp = json.load(open(os.path.join(root, 'src', 'sprites_doc.json'), encoding='utf-8'))
s = re.sub(r'__DOC_(E\d\d)__', lambda m: sp[m.group(1)], s)
assert '__DOC_' not in s, '채우지 못한 박사 그림 자리'
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(s)
