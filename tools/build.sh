#!/bin/sh
# 원본(src) → 그림 넣기 → 지식 색인 조립 → 점검
set -e
cd "$(dirname "$0")/.."
EX=${EX:-../adminmrobo/ahnboat_lab_explainer}
T=$EX/packs/task/onto-retrofit/tools
python3 tools/embed.py
python3 tools/build_kg.py
cp index.html kg/index.orig.html
python3 $T/retrofit.py index.html --kg kg/kg.json --refs kg/refs.json --meta kg/meta.json --backbone $EX/data/backbone_ai.json
rm -f index.html.bak
python3 $T/check.py kg/index.orig.html index.html --backbone $EX/data/backbone_ai.json --registry $EX/data/KG_00_registry.json --report kg/check_report.md
rm -f kg/index.orig.html
