# 그림 명세서 — 왜 지금 온톨로지인가 (연구실 리포트 · 동향)

기준: ai-lab-report-news v1.1 8장, ai-lab-explainer 18장, 캐릭터 팩 `fruitfly-lab-expressions @ 86d04ac`.
지금 페이지는 캐릭터 팩의 박사 정면 그림(192px)으로 모든 자리를 채웠다. 아래 두 장을 받으면 바꿔 넣는다.

## 지금 쓰는 그림

| 자리 | 키 | 표정 | 비고 |
|---|---|---|---|
| 표지 | `doc_e08` | 안내 | 표지 장면 그림(R1)을 받으면 교체 |
| 들어가며 · 맺음말 | `doc_e08` | 안내 | |
| 메모: 한눈에 보기 · 숫자로 보기 · 출처 | `doc_e13` | 기본 | 사실 전달 |
| 메모: 반응과 쟁점 | `doc_e13` | 기본 | 진지한 표정(R2)을 받으면 교체 |
| 메모: 무슨 일이 있었나 · 배경 · 용어 풀이 | `doc_e07` | 설명 | 헷갈리기 쉬운 점·연결 |
| 메모: 아직 모르는 것 | `doc_e09` | 생각 | |

## 받을 그림

### R1. 표지 — 소식을 전하는 박사 (1600×900, 16:9, WebP)

- 반영 위치: `index.html` 표지 `.hero-doc` (`data-img="cover_doc_news"`), `src/index.src.html` 같은 자리
- 프롬프트:

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, bright clean laboratory corridor with a white wall, soft purple accent light, 16:9 landscape, chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak and a small ponytail at the back, white lab coat over black vest and tie, standing at the right third facing the viewer with a calm friendly expression, holding up a folded newspaper in one hand and pointing with the other hand to a large cork news board on the left, the board pinned with blank cards connected by thin strings like a small graph, a few cards glowing teal, no text, no letters, no numbers, no logos, no real brands, no weapons
```

### R2. 표정 — 진지한 박사 (정사각형 512×512, WebP)

- 반영 위치: 메모 `#memo-6`(반응과 쟁점)
- 프롬프트:

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, consistent with the reference images, plain white background, square bust portrait, chibi scientist with thin teal rectangular glasses, spiky black hair with one white streak and a small ponytail at the back, white lab coat over black vest and tie, calm serious expression with closed mouth and level eyebrows, hands together in front of the chest, neutral and attentive, not happy and not angry, no text, no letters, no logos
```

## 규칙

- 한 편 합계 600KB 이하(지금 `index.html` 약 360KB).
- 사건의 좋고 나쁨을 드러내는 표정(환호·실망)은 쓰지 않는다.
