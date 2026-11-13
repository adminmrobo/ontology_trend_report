#!/usr/bin/env python3
"""src/index.src.html의 캐릭터 그림 자리(__DOC_*__)를 캐릭터 팩 그림으로 채워 index.html을 만든다."""
import json, os
root = os.path.join(os.path.dirname(__file__), '..')
s = open(os.path.join(root, 'src', 'index.src.html'), encoding='utf-8').read()
sp = json.load(open(os.path.join(root, 'src', 'sprites_doc.json'), encoding='utf-8'))
s = s.replace('__DOC_BOARD__', sp['doc_board']).replace('__DOC_FRONT__', sp['doc_front'])
open(os.path.join(root, 'index.html'), 'w', encoding='utf-8').write(s)
