#!/usr/bin/env python3
"""연구실 리포트(동향) '왜 지금 온톨로지인가'의 kg.json · refs.json · meta.json을 만든다."""
import json, os
OUT = os.path.join(os.path.dirname(__file__), '..', 'kg')
PAGE = 'ontology-trend-2026-11'
ACC = '2026-11-13 접속'

# ---- 참고문헌 (페이지 번호 → CSL) ----
R = [
 (1,'gartner2026semantics','report','Gartner Says Lack of Semantics Causes Inaccurate AI Agents and Wasted Spending',[{'literal':'Gartner'}],'2026-05-11','Gartner Newsroom','https://www.gartner.com/en/newsroom/press-releases/2026-05-11-gartner-says-lack-of-semantics-causes-inaccurate-artificial-intelligence-agents-and-wasted-spending','primary','보도자료 원문(gcom 미러) 대조'),
 (2,'microsoft2025introducing','webpage','From Data Platform to Intelligence Platform: Introducing Microsoft Fabric IQ',[{'literal':'Microsoft'}],'2025-11','Microsoft Fabric Updates Blog','https://blog.fabric.microsoft.com/en-us/blog/from-data-platform-to-intelligence-platform-introducing-microsoft-fabric-iq','primary','발표문 원문 대조'),
 (3,'itmedia2025ignite','article-newspaper','「AIエージェントには業務の文脈が必要不可欠」 Microsoftが年次イベントでWork IQなどを発表',[{'literal':'@IT (ITmedia)'}],'2025-11-19','@IT','https://atmarkit.itmedia.co.jp/ait/articles/2511/19/news121.html','background','기사 검색 발췌 대조(발표일 2025-11-18 확인)'),
 (4,'microsoft2026build','webpage','Microsoft Build 2026: Building agentic apps with Microsoft Fabric and Microsoft Databases',[{'literal':'Microsoft'}],'2026-06-02','Microsoft Azure Blog','https://azure.microsoft.com/en-us/blog/microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-microsoft-databases/','primary','발표문 원문 대조'),
 (5,'gartner2026first','report','First Take: Microsoft\'s Fabric IQ Updates Make Ontologies Operational',[{'literal':'Gartner'}],'2026-09','Gartner First Takes','https://www.gartner.com/en/insights/gartner-first-takes/microsoft-fabric-iq','background','검색 결과의 원문 발췌만 확인(본문 열람 실패)'),
 (6,'evelson2026build','post-weblog','Build Meaning Before Machines: Why Semantics, Ontologies, And Knowledge Graphs Matter For Agentic AI',[{'family':'Evelson','given':'Boris'},{'literal':'et al.'}],'2026-06-02','Forrester Blogs','https://www.forrester.com/blogs/build-meaning-before-machines-why-semantics-ontologies-and-knowledge-graphs-matter-for-agentic-ai/','background','블로그 원문 대조'),
 (7,'snowflake2025snowflake','article-newspaper','Snowflake, Salesforce, dbt Labs, and More, Revolutionize Data Readiness for AI with Open Semantic Interchange Initiative',[{'literal':'Snowflake'}],'2025-09-23','Business Wire','https://finance.yahoo.com/news/snowflake-salesforce-dbt-labs-more-130100051.html','primary','보도자료 게재본 대조'),
 (8,'constellation2025snowflake','article-newspaper','Snowflake, Salesforce, BlackRock lead effort to standardize semantic data',[{'literal':'Constellation Research'}],'2025-09','Constellation Research','https://www.constellationr.com/insights/news/snowflake-salesforce-blackrock-lead-effort-standardize-semantic-data','background','기사 대조'),
 (9,'dps2026iso','dataset','ISO/FDIS 23726-3 project information',[{'literal':'General Directorate of Standardization (Albania)'}],'2026-06-03','DPS standards catalogue','https://dps.gov.al/en/project/show/iso:proj:87560','primary','표준 목록 원문 대조'),
 (10,'iss2026iso','dataset','ISO 23726-3 project information',[{'literal':'Institute for Standardization of Serbia'}],'2026-10-30','ISS standards catalogue','https://iss.rs/en/project/show/iso:proj:87560','primary','표준 목록 원문 대조(한 곳)'),
 (11,'palantir2026q3','report','Palantir Reports Q3 2026 results (Form 8-K Exhibit 99.1)',[{'literal':'Palantir Technologies'}],'2026-11-02','U.S. SEC EDGAR','https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000045/a2026q3ex991pressrelease.htm','data','공시 원문 발췌 대조'),
 (12,'palantir2026q2','report','Palantir Reports Q2 2026 results (Form 8-K Exhibit 99.1)',[{'literal':'Palantir Technologies'}],'2026-08-03','U.S. SEC EDGAR','https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000039/a2026q2ex991pressrelease.htm','data','공시 원문 발췌 대조'),
 (13,'palantir2026q4','report','Palantir Reports Q4 2025 U.S. Comm Revenue Growth of 137% Y/Y and Revenue Growth of 70% Y/Y',[{'literal':'Palantir Technologies'}],'2026-02-02','Business Wire','https://www.businesswire.com/news/home/20260201154946/en/','data','보도자료 대조'),
 (14,'palantir2025q2','report','Palantir Reports Q2 2025 results (Form 8-K Exhibit 99.1)',[{'literal':'Palantir Technologies'}],'2025-08-04','U.S. SEC EDGAR','https://www.sec.gov/Archives/edgar/data/1321655/000132165525000105/a2025q2ex991pressrelease.htm','data','공시 원문 발췌 대조'),
 (15,'kalkine2026palantir','article-newspaper','Palantir Q3 2026 Revenue $2.31B, Net Income $1.13B (Form 10-Q summary)',[{'literal':'Kalkine'}],'2026-11','Kalkine','https://kalkine.com/news/announcements/palantir-q3-2026-revenue-231b-net-income-113b','data','10-Q 요약 기사 대조'),
 (16,'constellation2026palantir','article-newspaper','Palantir\'s US commercial, government deals surge in Q1',[{'literal':'Constellation Research'}],'2026-05-04','Constellation Research','https://www.constellationr.com/insights/news/palantirs-us-commercial-government-deals-surge-q1','data','기사 대조'),
 (17,'marketbeat2026palantir','article-newspaper','Palantir Technologies Q1 Earnings Call Highlights',[{'literal':'MarketBeat'}],'2026-05-04','MarketBeat','https://www.marketbeat.com/instant-alerts/palantir-technologies-q1-earnings-call-highlights-2026-05-04/','background','기사 대조'),
 (18,'asthagiri2026why','post-weblog','Why ontologies matter, why they fail and how to build them anyway',[{'family':'Asthagiri','given':'Nimisha'}],'2026-06-17','Thoughtworks Insights','https://www.thoughtworks.com/insights/blog/data-strategy/why-ontologies-matter-fail-build-anyway','background','블로그 원문 대조'),
 (19,'singhal2012introducing','post-weblog','Introducing the Knowledge Graph: things, not strings',[{'family':'Singhal','given':'Amit'}],'2012-05-16','Google Blog','https://blog.google/products/search/introducing-knowledge-graph-things-not/','data','블로그 원문 대조'),
 (20,'sej2020google','article-newspaper','Google\'s Knowledge Graph: how it works',[{'literal':'Search Engine Journal'}],'2020-05','Search Engine Journal','https://www.searchenginejournal.com/google-knowledge-graph-works-news/369484/','data','기사 발췌 대조'),
 (21,'gruber1993translation','article-journal','A translation approach to portable ontology specifications',[{'family':'Gruber','given':'Thomas R.'}],'1993','Knowledge Acquisition','https://doi.org/10.1006/knac.1993.1008','background','DOI 해석 확인'),
 (22,'w3c2009owl','report','OWL 2 Web Ontology Language Document Overview',[{'literal':'W3C'}],'2009-10-27','W3C Recommendation','https://www.w3.org/TR/owl2-overview/','primary','권고안 원문 대조'),
 (23,'w3c2017shapes','report','Shapes Constraint Language (SHACL)',[{'literal':'W3C'}],'2017-07-20','W3C Recommendation','https://www.w3.org/TR/shacl/','primary','권고안 원문 대조'),
 (24,'edge2024local','article','From Local to Global: A Graph RAG Approach to Query-Focused Summarization',[{'family':'Edge','given':'Darren'},{'literal':'et al.'}],'2024-04-24','arXiv','https://arxiv.org/abs/2404.16130','background','arXiv 원문 대조'),
 (25,'babaeigiglou2023llms4ol','article','LLMs4OL: Large Language Models for Ontology Learning',[{'family':'Babaei Giglou','given':'Hamed'},{'family':'D\'Souza','given':'Jennifer'},{'family':'Auer','given':'Sören'}],'2023-07-31','arXiv','https://arxiv.org/abs/2307.16648','background','arXiv 원문 대조'),
 (26,'atlan2026why','webpage','Why AI Grounding Is Driving Ontology Demand for Enterprise Agents',[{'literal':'Atlan'}],'2026','Atlan','https://atlan.com/know/ai-agent/ontology/ontology-ai-grounding/','background','검색 결과 발췌 대조(업계 분석)'),
 (27,'itonline2026gartner','article-newspaper','Gartner: semantics in AI-ready data (2027 prediction)',[{'literal':'IT-Online'}],'2026-05','IT-Online','https://it-online.co.za/?p=316078','background','기사 발췌 대조'),
 (28,'wikipedia2026knowledge','entry-encyclopedia','Knowledge Graph (Google)',[{'literal':'Wikipedia'}],'2026','Wikipedia','https://en.wikipedia.org/wiki/Knowledge_Graph_(Google)','data','항목 발췌 대조(한 곳)'),
]
RID = {n: rid for n, rid, *_ in R}

def dp(s):
    return {'date-parts': [[int(x) for x in s.split('-')]]}

N, E = [], []
def node(id, type, ko, en, anchor, level=2, conf='high', cov='explained', **kw):
    d = {'id': id, 'type': type, 'label': {'ko': ko, 'en': en}, 'page': PAGE, 'anchor': anchor, 'level': level,
         'status': 'known', 'confidence': conf, 'coverage': cov, 'match': [], 'domain': ['ai']}
    if type == 'Work': d.pop('domain')
    d.update(kw); N.append(d); return id
def edge(s, p, o, anchor, conf='high'):
    E.append({'s': s, 'p': 'lab:' + p, 'o': o, 'anchor': anchor, 'confidence': conf})
def claim(slug, ko, en, anchor, asof, refs, conf='high', level=3):
    cid = 'lab:claim/' + slug
    node(cid, 'Claim', ko, en, anchor, level, conf, 'explained', asOf=asof,
         source=[{'ref': RID[r], 'loc': ''} for r in refs], family='graph')
    for r in refs: edge(cid, 'assertedIn', 'lab:work/' + RID[r], anchor, conf)
    return cid

# ---- 개념·방법 ----
ONT = node('lab:concept/ontology', 'Concept', '온톨로지', 'ontology', '#sec-4-1', 2, family='graph',
           definition={'ko': '한 분야에 무엇이 있고 서로 어떤 관계인지를 사람과 기계가 같은 뜻으로 읽도록 적어 둔 명세.'},
           altLabel={'ko': ['존재론적 명세']})
SEM = node('lab:concept/semantic-layer', 'Concept', '시맨틱 계층', 'semantic layer', '#g-semantic-layer', 2, family='graph',
           definition={'ko': '데이터 위에 업무 용어와 지표의 정의를 얹어 도구마다 같은 뜻으로 계산하게 하는 층.'})
KG = node('lab:concept/knowledge-graph', 'Concept', '지식 그래프', 'knowledge graph', '#g-kg', 2, family='graph',
          definition={'ko': '대상을 점, 관계를 선으로 이은 사실의 망. 온톨로지가 정한 종류와 관계에 맞춰 사실을 채운 것.'})
AG = node('lab:concept/llm-agent', 'Concept', '에이전트', 'AI agent', '#g-agent', 2, family='language',
          definition={'ko': '목표를 받아 도구를 부르고 여러 단계를 스스로 실행하는 AI 시스템.'})
CTX = node('lab:concept/context-layer', 'Concept', '맥락 계층', 'context layer', '#pos-a', 3, family='graph',
           definition={'ko': '에이전트가 조직 데이터의 관계와 규칙을 읽도록 데이터·분석 기반에 두는 층(Gartner 권고의 용어).'})
OL = node('lab:concept/ontology-learning', 'Concept', '온톨로지 학습', 'ontology learning', '#sec-4-2', 3, family='graph',
          definition={'ko': '문서와 데이터에서 용어·계층·관계를 자동 또는 반자동으로 뽑아 온톨로지를 만드는 일.'})
HAL = node('lab:concept/hallucination', 'Concept', '환각', 'hallucination', '#sec-4-3', 2, 'high', 'mentioned', family='responsible')
ANA = node('lab:analogy/ontology-store-map', 'Analogy', '마트 진열 안내도', 'store floor map', '#sec-4-analogy', 1, family='graph',
           definition={'ko': '"요거트는 유제품, 유제품은 냉장 코너"처럼 한 줄을 더하면 자리와 규칙이 따라오는 안내도.'})
RAG = node('lab:method/rag', 'Method', 'RAG (검색 증강 생성)', 'retrieval-augmented generation', '#g-graphrag', 2, 'high', 'mentioned', family='language')
GRAG = node('lab:method/graphrag', 'Method', 'GraphRAG', 'GraphRAG', '#sec-4-2', 3, family='language',
            definition={'ko': '문서에서 지식 그래프를 만든 뒤 그 그래프를 근거로 답을 찾는 검색 증강 생성 방식.'})
FIQ = node('lab:method/fabric-iq-ontology', 'Method', 'Fabric IQ 온톨로지', 'Microsoft Fabric IQ Ontology', '#tl-2025-11-18', 3, family='graph',
           definition={'ko': '업무의 대상·관계·속성·규칙·행동을 모델로 정의하는 Microsoft Fabric IQ의 기능.'})
PLO = node('lab:method/palantir-ontology', 'Method', 'Palantir 온톨로지(AIP)', 'Palantir Ontology (AIP)', '#tl-2026-05-04', 3, family='graph',
           definition={'ko': 'Palantir가 AI 운영의 중간 표현이라고 설명하는 자사 플랫폼의 온톨로지 계층.'})
DRAFT = node('lab:method/llm-ontology-drafting', 'Method', 'LLM으로 온톨로지 초안 쓰기', 'LLM-assisted ontology drafting', '#sec-4-3', 3, family='graph',
             definition={'ko': '기존 데이터 모델·문서를 LLM이 읽어 대상·관계·규칙을 먼저 제안하고 사람이 검토하는 방식.'})
MVO = node('lab:method/minimum-viable-ontology', 'Method', '한 사용 사례로 좁혀 시작하기', 'minimum viable ontology', '#pos-b', 3, family='graph',
           definition={'ko': '수익이 큰 한 가지 문제에 맞춘 최소 온톨로지를 먼저 만들고, 가치를 보인 뒤 넓히는 방식(Thoughtworks 권고).'})
# 한계
COST = node('lab:limitation/manual-ontology-cost', 'Limitation', '수작업 구축 비용', 'cost of manual ontology building', '#sec-4-3', 3, family='graph')
MAINT = node('lab:limitation/ontology-maintenance', 'Limitation', '유지보수 문제', 'ontology maintenance problem', '#pos-b', 3, family='graph',
             definition={'ko': '규정·조직·제품이 바뀌는 속도를 수작업 모델이 따라가지 못해 모델이 낡는 문제.'})
SCOPE = node('lab:limitation/scope-creep', 'Limitation', '범위 확장', 'scope creep', '#pos-b', 3, family='graph',
             definition={'ko': '전체 분야를 다 모델링하려다 가치를 보이기 전에 사업이 멈추는 문제.'})
GAP = node('lab:limitation/translation-gap', 'Limitation', '번역 간극', 'translation gap', '#tl-2026-06-17', 3, family='graph',
           definition={'ko': '모델링 전문가와 업무 전문가가 서로의 지식을 옮기며 세부가 빠지는 문제.'})
INC = node('lab:limitation/ai-draft-incompleteness', 'Limitation', 'AI 초안의 불완전성', 'incompleteness of AI-generated ontology drafts', '#pos-b', 3, family='graph',
           definition={'ko': 'AI가 기존 데이터에서 만든 초안이 불완전하거나 칸막이식일 수 있다는 지적(Gartner 첫 논평).'})
# 기준·규격
OWL = node('lab:standard/owl2', 'Standard', 'OWL 2', 'OWL 2 Web Ontology Language', '#sec-4-2', 2, asOf='2009-10-27', jurisdiction='W3C', family='graph')
SHACL = node('lab:standard/shacl', 'Standard', 'SHACL', 'Shapes Constraint Language', '#sec-4-2', 3, asOf='2017-07-20', jurisdiction='W3C', family='graph')
ISO = node('lab:standard/iso-23726-3', 'Standard', 'ISO 23726-3 산업 데이터 온톨로지(IDO)', 'ISO 23726-3 Industrial Data Ontology', '#tl-2026-06-03', 3,
           asOf='2026-06-03', jurisdiction='ISO/TC 184/SC 4', family='graph')
OSI = node('lab:standard/open-semantic-interchange', 'Standard', 'Open Semantic Interchange (OSI)', 'Open Semantic Interchange', '#tl-2025-09-23', 3,
           asOf='2025-09-23', jurisdiction='업계 공동 규격 (Snowflake 외)', family='graph')
# 지표
REV = node('lab:metric/palantir-quarterly-revenue', 'Metric', 'Palantir 분기 매출', 'Palantir quarterly revenue', '#fig-5-1', 2, family='graph',
           definition={'ko': 'Palantir가 분기마다 공시하는 매출(단위: 10억 달러).'})
ACCM = node('lab:metric/agentic-ai-accuracy', 'Metric', '에이전트형 AI 정확도', 'agentic AI accuracy', '#kpi-gartner', 2, family='evaluation')
FACTS = node('lab:metric/kg-fact-count', 'Metric', '지식 그래프 사실 수', 'number of facts in a knowledge graph', '#tbl-5-2', 2, family='graph')

# ---- 사건·숫자 주장 ----
c_osi = claim('osi-launch-2025', 'Snowflake 외 기업들이 시맨틱 메타데이터 공동 규격 OSI를 시작했다', 'Snowflake and partners launched the Open Semantic Interchange initiative', '#tl-2025-09-23', '2025-09-23', [7, 8])
c_fiq = claim('fabric-iq-announced-2025', 'Microsoft가 Ignite 2025에서 Ontology 항목을 핵심으로 한 Fabric IQ를 발표했다', 'Microsoft announced Fabric IQ with an Ontology item at Ignite 2025', '#tl-2025-11-18', '2025-11-18', [2, 3])
c_dis = claim('iso-23726-3-dis-vote', 'ISO/DIS 23726-3 투표가 마감됐다(단계 40.60)', 'Voting on ISO/DIS 23726-3 closed (stage 40.60)', '#tl-2025-12-18', '2025-12-18', [9])
c_q1 = claim('palantir-q1-2026-revenue', 'Palantir 2026년 1분기 매출은 16억 3,300만 달러로 전년 대비 85% 늘었다', 'Palantir Q1 2026 revenue was $1.633B, up 85% YoY', '#tl-2026-05-04', '2026-05-04', [16, 17])
c_po = claim('palantir-ontology-intermediary', 'Palantir 경영진은 온톨로지를 AI 운영의 중간 표현이라고 설명했다', 'Palantir management described the ontology as the intermediary representation for operational AI', '#tl-2026-05-04', '2026-05-04', [16, 17])
c_gs = claim('gartner-semantics-agents', 'Gartner는 시맨틱스가 부족하면 AI 에이전트가 부정확해지고 지출이 낭비된다고 밝혔다', 'Gartner said lack of semantics causes inaccurate AI agents and wasted spending', '#tl-2026-05-11', '2026-05-11', [1, 27])
c_gp = claim('gartner-2027-prediction', 'Gartner는 2027년까지 시맨틱스를 우선한 조직의 에이전트 정확도가 최대 80% 오르고 비용이 최대 60% 준다고 예측했다', 'Gartner predicted up to 80% accuracy gain and 60% cost reduction by 2027', '#kpi-gartner', '2026-05-11', [1, 27])
c_ga = claim('fabric-iq-ga-2026', 'Microsoft가 Fabric IQ를 정식 출시했고 온톨로지 기능은 몇 달 안에 정식 출시될 예정이라고 밝혔다', 'Microsoft made Fabric IQ generally available; ontologies expected to be GA in coming months', '#tl-2026-06-02', '2026-06-02', [4])
c_fr = claim('forrester-semantics-first', 'Forrester는 시맨틱 계층에서 시작해 지식 그래프로 넓히라고 권고했다', 'Forrester recommended starting with semantics and evolving to knowledge graphs', '#tl-2026-06-02-forrester', '2026-06-02', [6])
c_fdis = claim('iso-23726-3-fdis', 'ISO 23726-3이 최종안 승인 단계(50.00)로 등록됐다', 'ISO 23726-3 registered as FDIS (stage 50.00)', '#tl-2026-06-03', '2026-06-03', [9])
c_tw = claim('thoughtworks-failure-reasons', 'Thoughtworks는 번역 간극·범위 확장·유지보수를 온톨로지 사업의 실패 원인으로 들었다', 'Thoughtworks named the translation gap, scope creep and maintenance as reasons ontology programs fail', '#tl-2026-06-17', '2026-06-17', [18])
c_ft = claim('gartner-first-take-fabric', 'Gartner 첫 논평은 AI가 만든 온톨로지 초안에 업무 전문가 검증이 필요하다고 적었다', 'Gartner First Take said SMEs remain essential to validate AI-generated ontology proposals', '#tl-2026-09-29', '2026-09-29', [5], 'medium')
c_60 = claim('iso-23726-3-stage-6000', '한 표준 목록은 ISO 23726-3을 발행 준비 단계(60.00)로 표시한다', 'One catalogue lists ISO 23726-3 at stage 60.00 (under publication)', '#tl-2026-10-30', '2026-10-30', [10], 'medium')
c_q3 = claim('palantir-q3-2026-revenue', 'Palantir 2026년 3분기 매출은 23억 1,300만 달러로 전년 대비 96% 늘었다', 'Palantir Q3 2026 revenue was $2.313B, up 96% YoY', '#tl-2026-11-02', '2026-11-02', [11])
c_7q = claim('palantir-seven-quarter-growth', 'Palantir 분기 매출은 2025년 1분기 0.884에서 2026년 3분기 2.313(10억 달러)으로 늘었다', 'Palantir quarterly revenue rose from $0.884B (Q1 2025) to $2.313B (Q3 2026)', '#fig-5-1', '2026-11-02', [11, 12, 13, 14, 15, 16])
c_g12 = claim('google-kg-2012', 'Google 지식 그래프는 2012년 출시 때 대상 5억 개 이상, 사실 35억 개 이상이었다', 'Google Knowledge Graph launched with 500M+ objects and 3.5B+ facts', '#tbl-5-2', '2012-05-16', [19])
c_g20 = claim('google-kg-2020', 'Google 지식 그래프는 2020년 5월 대상 50억 개, 사실 5,000억 개 규모였다', 'Google Knowledge Graph held 500B facts about 5B entities in May 2020', '#tbl-5-2', '2020-05', [20])
c_gr = claim('gruber-1993-definition', 'Gruber(1993)는 온톨로지를 개념화의 명시적 명세로 정의했다', 'Gruber (1993) defined an ontology as an explicit specification of a conceptualization', '#sec-4-1', '1993', [21])
c_grag = claim('graphrag-2024', 'Microsoft 연구진이 GraphRAG를 발표했다', 'Microsoft researchers introduced GraphRAG', '#sec-4-2', '2024-04-24', [24])
c_l4 = claim('llms4ol-2023', 'LLMs4OL 연구가 LLM으로 용어 분류·계층 발견·관계 추출을 시험했다', 'LLMs4OL tested LLMs on term typing, taxonomy discovery and relation extraction', '#sec-4-2', '2023-07-31', [25])
c_at = claim('atlan-demand-and-cost', 'Atlan은 에이전트가 정의의 수요를 늘리고 LLM이 초안 비용을 줄였다고 설명했다', 'Atlan said agents raised demand for definitions while LLMs cut drafting cost', '#sec-4-3', '2026', [26], 'medium')

# 입장
PA = node('lab:claim/position-build-semantics-first', 'Claim', '입장 A: 에이전트의 기반으로 먼저 갖춰야 한다', 'Position A: build the semantic foundation first', '#pos-a', 3, 'medium', 'explained',
          asOf='2026-11-13', source=[{'ref': RID[1], 'loc': ''}, {'ref': RID[6], 'loc': ''}], family='graph')
PB = node('lab:claim/position-start-narrow', 'Claim', '입장 B: 좁게 시작하고 유지 비용을 따져야 한다', 'Position B: start narrow and weigh maintenance cost', '#pos-b', 3, 'medium', 'explained',
          asOf='2026-11-13', source=[{'ref': RID[18], 'loc': ''}, {'ref': RID[5], 'loc': ''}], family='graph')
for r in (1, 6): edge(PA, 'assertedIn', 'lab:work/' + RID[r], '#pos-a', 'medium')
for r in (18, 5): edge(PB, 'assertedIn', 'lab:work/' + RID[r], '#pos-b', 'medium')

# 질문
Q = {}
for qid, ko, en, a in [('gartner-prediction-validity', '2027년 예측이 맞을지', 'Will the 2027 Gartner prediction hold?', '#q-gartner'),
                        ('iso-23726-3-publication-date', 'ISO 23726-3의 발행일', 'When is ISO 23726-3 published?', '#q-iso'),
                        ('fabric-iq-ontology-ga-date', 'Fabric IQ 온톨로지의 정식 출시일', 'When do Fabric IQ ontologies become GA?', '#q-fabric'),
                        ('revenue-ontology-causality', '실적과 온톨로지 기능의 인과관계', 'Is revenue growth caused by ontology features?', '#q-causal'),
                        ('osi-adoption', 'OSI 규격의 실제 채택 범위', 'How widely is OSI adopted?', '#q-osi')]:
    Q[qid] = node('lab:question/' + qid, 'Question', ko, en, a, 4, 'medium', 'explained', family='graph')

# Work 노드 (주장이 인용한 문헌만)
used = sorted({s['ref'] for n in N for s in n.get('source', [])})
for n_, rid, typ, title, auth, date, cont, url, role, how in R:
    if rid in used:
        node('lab:work/' + rid, 'Work', '%s (%s) %s' % ((auth[0].get('family') or auth[0].get('literal')), date[:4], cont), title, '#ref-%d' % n_, 1, family='graph')

# ---- 관계 ----
def br(s, t, a): edge(s, 'broader', 'lab:topic/' + t, a)
for s, t, a in [(ONT, 'knowledge-graph', '#sec-4-1'), (SEM, 'knowledge-graph', '#g-semantic-layer'), (KG, 'knowledge-graph', '#g-kg'),
                (AG, 'pretrained-lm', '#g-agent'), (CTX, 'knowledge-graph', '#pos-a'), (OL, 'knowledge-graph', '#sec-4-2'), (OL, 'pretrained-lm', '#sec-4-2'),
                (HAL, 'ai-safety', '#sec-4-3'), (RAG, 'rag', '#g-graphrag'), (GRAG, 'rag', '#sec-4-2'), (GRAG, 'knowledge-graph', '#sec-4-2'),
                (FIQ, 'knowledge-graph', '#tl-2025-11-18'), (PLO, 'knowledge-graph', '#tl-2026-05-04'), (DRAFT, 'prompting', '#sec-4-3'), (DRAFT, 'knowledge-graph', '#sec-4-3'),
                (MVO, 'knowledge-graph', '#pos-b'), (COST, 'knowledge-graph', '#sec-4-3'), (MAINT, 'knowledge-graph', '#pos-b'), (SCOPE, 'knowledge-graph', '#pos-b'),
                (GAP, 'knowledge-graph', '#tl-2026-06-17'), (INC, 'knowledge-graph', '#pos-b'), (ANA, 'knowledge-graph', '#sec-4-analogy')]:
    br(s, t, a)
edge(ONT, 'prerequisiteOf', KG, '#g-kg')
edge(ONT, 'prerequisiteOf', SEM, '#g-semantic-layer', 'medium')
edge(KG, 'prerequisiteOf', GRAG, '#sec-4-2')
edge(RAG, 'prerequisiteOf', GRAG, '#g-graphrag')
edge(GRAG, 'contrastsWith', RAG, '#g-graphrag')
edge(SEM, 'contrastsWith', KG, '#tl-2026-06-02-forrester')
edge(ANA, 'analogyOf', ONT, '#sec-4-analogy')
edge(SEM, 'partOf', CTX, '#pos-a', 'medium')
edge(ONT, 'partOf', CTX, '#pos-a', 'medium')
edge(FIQ, 'partOf', CTX, '#tl-2025-11-18', 'medium')
edge(ONT, 'governedBy', OWL, '#sec-4-2')
edge(KG, 'governedBy', SHACL, '#sec-4-2')
edge(ISO, 'governedBy', OWL, '#tl-2026-06-03')
edge(ISO, 'partOf', ONT, '#tl-2026-06-03', 'medium')
edge(OSI, 'partOf', SEM, '#tl-2025-09-23')
edge(FIQ, 'partOf', ONT, '#tl-2025-11-18')
edge(PLO, 'partOf', ONT, '#tl-2026-05-04')
edge(AG, 'hasLimitation', HAL, '#sec-4-3')
edge(HAL, 'addressedBy', CTX, '#sec-4-3', 'medium')
edge(ONT, 'hasLimitation', COST, '#sec-4-3')
edge(COST, 'addressedBy', DRAFT, '#sec-4-3')
edge(OL, 'prerequisiteOf', DRAFT, '#sec-4-3')
edge(DRAFT, 'hasLimitation', INC, '#pos-b')
edge(DRAFT, 'hasLimitation', MAINT, '#sec-4-3')
edge(ONT, 'hasLimitation', MAINT, '#pos-b')
edge(ONT, 'hasLimitation', SCOPE, '#pos-b')
edge(ONT, 'hasLimitation', GAP, '#tl-2026-06-17')
edge(SCOPE, 'addressedBy', MVO, '#pos-b')
edge(FIQ, 'evaluatedBy', ACCM, '#kpi-gartner', 'medium')
edge(CTX, 'evaluatedBy', ACCM, '#kpi-gartner')
edge(PLO, 'measuredBy', REV, '#fig-5-1', 'medium')
edge(KG, 'measuredBy', FACTS, '#tbl-5-2')
edge(DRAFT, 'partOf', FIQ, '#sec-4-3', 'medium')
# 주장이 받치는 것
for c, o, a in [(c_osi, OSI, '#tl-2025-09-23'), (c_fiq, FIQ, '#tl-2025-11-18'), (c_dis, ISO, '#tl-2025-12-18'), (c_fdis, ISO, '#tl-2026-06-03'),
                (c_60, ISO, '#tl-2026-10-30'), (c_q1, REV, '#tl-2026-05-04'), (c_q3, REV, '#tl-2026-11-02'), (c_7q, REV, '#fig-5-1'),
                (c_po, PLO, '#tl-2026-05-04'), (c_gs, CTX, '#tl-2026-05-11'), (c_gs, PA, '#pos-a'), (c_gp, ACCM, '#kpi-gartner'),
                (c_ga, FIQ, '#tl-2026-06-02'), (c_fr, PA, '#pos-a'), (c_fr, SEM, '#tl-2026-06-02-forrester'), (c_tw, PB, '#pos-b'),
                (c_tw, MAINT, '#pos-b'), (c_tw, SCOPE, '#pos-b'), (c_tw, GAP, '#tl-2026-06-17'), (c_ft, INC, '#pos-b'), (c_ft, PB, '#pos-b'),
                (c_g12, FACTS, '#tbl-5-2'), (c_g20, FACTS, '#tbl-5-2'), (c_gr, ONT, '#sec-4-1'),
                (c_grag, GRAG, '#sec-4-2'), (c_l4, OL, '#sec-4-2'),
                (c_at, DRAFT, '#sec-4-3'), (c_po, PA, '#pos-a')]:
    edge(c, 'supports', o, a)
edge(PA, 'contrastsWith', PB, '#sec-6')
edge(c_g12, 'supersededBy', c_g20, '#tbl-5-2')
edge(c_dis, 'supersededBy', c_fdis, '#tl-2026-06-03')
edge(c_fdis, 'supersededBy', c_60, '#tl-2026-10-30', 'medium')
edge(c_fiq, 'supersededBy', c_ga, '#tl-2026-06-02')
edge(c_gp, 'raises', Q['gartner-prediction-validity'], '#q-gartner')
edge(ISO, 'raises', Q['iso-23726-3-publication-date'], '#q-iso')
edge(c_ga, 'raises', Q['fabric-iq-ontology-ga-date'], '#q-fabric')
edge(c_po, 'raises', Q['revenue-ontology-causality'], '#q-causal')
edge(OSI, 'raises', Q['osi-adoption'], '#q-osi')

kg = {'version': '1.0', 'page': PAGE, 'nodes': N, 'edges': E}
refs = []
for n_, rid, typ, title, auth, date, cont, url, role, how in R:
    supports = sorted({nd['id'] for nd in N if any(s['ref'] == rid for s in nd.get('source', []))})
    refs.append({'id': rid, 'type': typ, 'title': title, 'author': auth, 'issued': dp(date), 'container-title': cont, 'URL': url,
                 'accessed': dp('2026-11-13'),
                 'lab': {'work': 'lab:work/' + rid, 'role': role, 'supports': supports, 'locs': ['#ref-%d' % n_],
                         'verified': {'title': True, 'author': True, 'year': True, 'container': True, 'pages': False, 'doi': rid == 'gruber1993translation'},
                         'checkedBy': '%s, %s' % (how, ACC), 'checkedSource': 'web'}})
meta = {'title': '왜 지금 온톨로지인가 — AI 에이전트 시대에 다시 불려 나온 30년 된 개념', 'number': 'R-2026-11-13', 'series': '연구실 리포트(동향)',
        'about': [ONT, SEM, KG, AG, CTX, ISO], 'basedOn': [RID[1], RID[4], RID[6], RID[9], RID[11], RID[18]],
        'educationalLevel': '입문~중급', 'creator': [{'name': '안상선', 'role': 'author'}],
        'contributor': [{'name': 'AI 보조 제작', 'role': 'assistant'}], 'date': '2026-11-13', 'version': '1.0', 'language': ['ko'],
        'license': '', 'url': 'https://adminmrobo.github.io/ontology_trend_report/', 'registry': 'KG_00_registry 0.2',
        'learningResourceType': 'news report', 'domain': ['ai'],
        'seeAlso': 'https://adminmrobo.github.io/ahnboat_lab_cover_status/ontology.html',
        'suggestedCitation': '안상선 (2026). 왜 지금 온톨로지인가 — AI 에이전트 시대에 다시 불려 나온 30년 된 개념. 연구실 리포트(동향) R-2026-11-13, v1.0.'}
os.makedirs(OUT, exist_ok=True)
for name, obj in (('kg.json', kg), ('refs.json', refs), ('meta.json', meta)):
    json.dump(obj, open(os.path.join(OUT, name), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('nodes', len(N), 'edges', len(E), 'refs', len(refs), 'relatedTo', sum(e['p'] == 'lab:relatedTo' for e in E))
