#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'APMICRO-Teaching'
VIS = BASE / 'Visual-Plan'

SOURCES = [
    ('FRED-UNRATE', 'FRED UNRATE', 'Python chart data', 'https://fred.stlouisfed.org/series/UNRATE', 'BLS civilian unemployment rate; download the series at build time.'),
    ('FRED-CPIAUCSL', 'FRED CPIAUCSL', 'Python chart data', 'https://fred.stlouisfed.org/series/CPIAUCSL', 'BLS Consumer Price Index for All Urban Consumers; compute year-over-year inflation when needed.'),
    ('FRED-GDP', 'FRED GDP', 'Python chart data', 'https://fred.stlouisfed.org/series/GDP', 'BEA gross domestic product series; use real GDP separately when the lesson needs quantities rather than current dollars.'),
    ('FRED-FEDFUNDS', 'FRED FEDFUNDS', 'Python chart data', 'https://fred.stlouisfed.org/series/FEDFUNDS', 'Effective federal funds rate; context extension for policy and banking visuals.'),
    ('FRED-M2SL', 'FRED M2SL', 'Python chart data', 'https://fred.stlouisfed.org/series/M2SL', 'M2 money stock; context extension for banking and monetary conditions.'),
    ('FRED-SP500', 'FRED SP500', 'Python chart data', 'https://fred.stlouisfed.org/series/SP500', 'S&P 500 index; use for market confidence or financial-market context, not as an AP Micro core objective.'),
    ('FRED-GINI', 'FRED GINIALLRH', 'Python chart data', 'https://fred.stlouisfed.org/series/GINIALLRH', 'U.S. household income inequality measure; pair with a Lorenz curve drawn locally.'),
    ('WIKIMEDIA-GREAT-DEPRESSION-US', 'Wikimedia Commons: Great Depression in the United States', 'Historical photo discovery', 'https://commons.wikimedia.org/wiki/Category:Great_Depression_in_the_United_States', 'Choose individual files and verify their description-page license before copying.'),
    ('WIKIMEDIA-GREAT-DEPRESSION', 'Wikimedia Commons: Great Depression', 'Historical photo discovery', 'https://commons.wikimedia.org/wiki/Category:Great_Depression', 'Includes bank runs, unemployment, relief, and public-policy context images.'),
    ('WIKIMEDIA-BANK-RUNS', 'Wikimedia Commons: Bank runs', 'Historical photo discovery', 'https://commons.wikimedia.org/wiki/Category:Bank_runs', 'Use for banking, liquidity, confidence, and deposit-withdrawal context.'),
    ('WIKIMEDIA-BANKING', 'Wikimedia Commons: Banking', 'Historical/photo discovery', 'https://commons.wikimedia.org/wiki/Category:Banking', 'Broad category for bank documents, bank buildings, bank runs, and financial systems.'),
    ('WIKIMEDIA-WALL-STREET', 'Wikimedia Commons: Wall Street', 'Historical/photo discovery', 'https://commons.wikimedia.org/wiki/Category:Wall_Street', 'Contains Wall Street, bank buildings, NYSE, and financial-district images.'),
    ('WIKIMEDIA-WALL-STREET-HISTORY', 'Wikimedia Commons: Wall Street in History', 'Historical/photo discovery', 'https://commons.wikimedia.org/wiki/Category:Wall_Street_in_History', 'Useful for historical banking and financial-market context.'),
    ('WIKIMEDIA-FACTORIES', 'Wikimedia Commons: Factories', 'Historical/photo discovery', 'https://commons.wikimedia.org/wiki/Category:Factories', 'Use only after checking each selected file’s license and attribution requirements.'),
    ('WIKIMEDIA-NYSE-HISTORY', 'Wikimedia Commons: History of the New York Stock Exchange', 'Historical/photo discovery', 'https://commons.wikimedia.org/wiki/Category:History_of_the_New_York_Stock_Exchange', 'Includes historical exchange and Wall Street crash material.'),
    ('AP-CED', 'College Board AP Microeconomics CED', 'Official course boundary', 'https://apcentral.collegeboard.org/media/pdf/ap-microeconomics-course-and-exam-description.pdf', 'Use to keep visuals aligned with the official Unit and Learning Objective structure.'),
]

V = [
(1,'Unit 1','Scarcity and resource allocation',[
('Three-resource scarcity panel','Python/diagram','Three constrained inputs feeding three competing uses; introduce scarcity and trade-offs.','Generated locally from a simple allocation table.','planned'),
('Choice and opportunity-cost card','Concept diagram','A two-option choice card with explicit foregone benefit; use as the first classroom prompt.','Draw locally; no external asset.','planned'),
('Resource allocation photograph','Historical/real-world photo','A farm, factory, or public-service resource scene to make scarce inputs visible.','WIKIMEDIA-FACTORIES; check file license.','planned')]),
(2,'Unit 1','Production possibilities curve',[
('PPC with efficiency zones','Python chart','Show efficient, inefficient, and unattainable points with a growth shift.','Generated locally; use clear labels and one-color annotations.','planned'),
('PPC movement animation frames','Concept diagram','Four frames: movement along PPC, inside point, outside point, outward shift.','Draw locally for slides/handout.','planned'),
('Production landscape photograph','Historical/real-world photo','A factory or agricultural landscape as a visual bridge from resources to output combinations.','WIKIMEDIA-FACTORIES; check file license.','planned')]),
(3,'Unit 1','Comparative advantage and trade',[
('Specialization and trade flow map','Python/diagram','Two producers, opportunity costs, specialization arrows, and terms of trade.','Generated locally from the lesson’s production table.','planned'),
('Comparative-advantage heatmap','Python chart','Color-code opportunity cost by producer and product to make the lower opportunity cost visible.','Generated locally; no external asset.','planned'),
('Port and container trade photograph','Real-world photo','Connect specialization to actual exchange across borders.','Use a Wikimedia Commons port/container category after license check.','planned')]),
(4,'Unit 1','Cost-benefit and marginal consumer choice',[
('Total benefit, total cost, and net benefit bars','Python chart','Compare total and marginal reasoning in one decision.','Generated locally from a classroom choice dataset.','planned'),
('MB and MC crossing diagram','Concept diagram','Highlight the quantity where marginal benefit and marginal cost meet.','Draw locally; align with CBA-2 objectives.','planned'),
('Everyday consumer choice photo','Real-world photo','A shopping or time-allocation scene that makes opportunity cost concrete.','Use a self-created photo or a clearly licensed Commons file.','planned')]),
(5,'Unit 2','Demand and supply',[
('Market equilibrium chart','Python chart','Plot demand and supply, label equilibrium price and quantity, and keep a clean blank version.','Generated locally from a simple linear schedule.','planned'),
('Demand shifters icon strip','Concept diagram','Income, tastes, substitutes, complements, technology, and input prices.','Draw locally with consistent icon style.','planned'),
('Farmers market photograph','Real-world photo','Connect buyers, sellers, price, and quantity to a recognizable market.','Wikimedia Commons food-market category; check license.','planned')]),
(6,'Unit 2','Price elasticity of demand and supply',[
('Steep versus flat demand curves','Python chart','Compare elastic and inelastic responses to the same price change.','Generated locally; use identical axes for comparison.','planned'),
('Elasticity slider sequence','Concept diagram','Four small panels showing percentage quantity response as price changes.','Draw locally for handout.','planned'),
('Essential versus luxury goods photo pair','Real-world photo','Use a staple good and a discretionary good to prompt elasticity predictions.','Self-created or licensed Commons images.','planned')]),
(7,'Unit 2','Other elasticities and total revenue',[
('Total-revenue curve','Python chart','Show how total revenue changes across elastic, unit elastic, and inelastic regions.','Generated locally from a demand schedule.','planned'),
('Substitute/complement network','Concept diagram','Arrows between related goods, with signs for cross-price elasticity.','Draw locally; use simple product icons.','planned'),
('Income elasticity product ladder','Python/diagram','Place necessities, normal goods, and inferior goods on an income-response ladder.','Generated locally from hypothetical data; clearly label as illustrative.','planned')]),
(8,'Unit 2','Market equilibrium and surplus',[
('Consumer and producer surplus graph','Python chart','Shade CS, PS, and total surplus with old/new labels.','Generated locally from a linear market model.','planned'),
('Auction price ladder','Concept diagram','Bids and asks arranged to show who trades and who gains.','Draw locally; no external asset.','planned'),
('Market exchange photograph','Real-world photo','A market transaction scene to connect surplus to willingness to pay and sell.','Wikimedia Commons market category; check license.','planned')]),
(9,'Unit 2','Market disequilibrium and changes in equilibrium',[
('Shortage and surplus side-by-side','Python chart','Show price below equilibrium and above equilibrium with quantity supplied/demanded labels.','Generated locally; keep a blank student version.','planned'),
('Shock-to-equilibrium storyboard','Concept diagram','Initial equilibrium, demand/supply shock, adjustment, final equilibrium.','Draw locally for FRQ practice.','planned'),
('Empty shelf or queue photograph','Real-world photo','A visual prompt for shortage, rationing, and non-price adjustment.','Use a licensed Commons file or self-created photo.','planned')]),
(10,'Unit 2','Government intervention',[
('Price ceiling, price floor, tax, and subsidy grid','Python/diagram','Four mini-graphs with the same market axes and policy labels.','Generated locally; one reusable slide asset.','planned'),
('Tax wedge and incidence diagram','Concept diagram','Show buyer price, seller price, tax wedge, and relative elasticities.','Draw locally for handout.','planned'),
('Rent-control or fuel-price sign photograph','Real-world photo','Introduce the policy problem before graphing.','Use a clearly licensed Commons or self-created image.','planned')]),
(11,'Unit 2','International trade and public policy',[
('Tariff graph with world price','Python chart','Show domestic price, imports, CS, PS, government revenue, and DWL.','Generated locally from a trade schedule.','planned'),
('Trade route map','Python/diagram','Draw an importer/exporter map with goods and price arrows.','Generated locally; use a simple outline map.','planned'),
('Container port photograph','Real-world photo','Make the abstract import/export flow visible.','Wikimedia Commons port/container search; check license.','planned')]),
(12,'Unit 3','The production function',[
('TP, AP, and MP curves','Python chart','Show the relationship among total, average, and marginal product.','Generated locally from a production table.','planned'),
('Production-table heatmap','Python chart','Color the stages of increasing and diminishing marginal returns.','Generated locally; use the same table as the handout.','planned'),
('Factory production line photograph','Real-world photo','Connect inputs, output, and marginal product to a production setting.','WIKIMEDIA-FACTORIES; check file license.','planned')]),
(13,'Unit 3','Short-run production costs',[
('FC, VC, TC, ATC, AVC, and MC curves','Python chart','Use a coordinated six-panel chart with consistent output axis.','Generated locally from a cost table.','planned'),
('Cost-table annotation visual','Concept diagram','Point from a table row to each corresponding cost formula.','Draw locally for the worksheet.','planned'),
('Factory input photograph','Real-world photo','Show fixed plant and variable labor/material inputs.','Self-created or licensed Commons file.','planned')]),
(14,'Unit 3','Long-run costs and types of profit',[
('LRATC economies-of-scale curve','Python chart','Show economies, constant returns, and diseconomies of scale.','Generated locally with clearly illustrative values.','planned'),
('Accounting versus economic profit ledger','Concept diagram','Separate explicit costs, implicit costs, accounting profit, and economic profit.','Draw locally; use a two-column ledger.','planned'),
('Large-scale versus small-scale production photo pair','Real-world photo','Visualize scale and average-cost trade-offs.','WIKIMEDIA-FACTORIES; check license.','planned')]),
(15,'Unit 3','Profit maximization',[
('MR, MC, and profit-maximizing output','Python chart','Highlight the output where MR intersects MC and map price/revenue/cost.','Generated locally; include a blank annotation version.','planned'),
('Profit rectangle sequence','Concept diagram','Three panels for positive profit, zero economic profit, and loss.','Draw locally for FRQ graph practice.','planned'),
('Firm decision dashboard','Python/diagram','Output, price, revenue, cost, and profit in a compact table-card.','Generated locally from the same graph data.','planned')]),
(16,'Unit 3','Produce, shut down, enter, or exit',[
('Shutdown decision graph','Python chart','Compare price with AVC and ATC; label produce, shut down, profit, and loss regions.','Generated locally.','planned'),
('Entry and exit flowchart','Concept diagram','Short-run production versus long-run entry/exit decision path.','Draw locally; use arrows and condition boxes.','planned'),
('Open/closed business storefront pair','Real-world photo','Make entry, exit, and shutdown decisions concrete.','Self-created or licensed Commons file.','planned')]),
(17,'Unit 3','Perfect competition and review',[
('Market-versus-firm two-panel graph','Python chart','Place industry equilibrium beside a representative firm’s horizontal demand curve.','Generated locally with matching labels.','planned'),
('Perfect-competition assumptions card','Concept diagram','Many buyers/sellers, identical product, price-taking, and free entry/exit.','Draw locally.','planned'),
('Commodity farm photograph','Real-world photo','Use a standardized-product market as an intuitive starting point.','Wikimedia Commons agriculture category; check license.','planned')]),
(18,'Unit 4','Introduction to imperfect competition',[
('Market-structure comparison matrix','Concept diagram','Compare number of firms, product differentiation, barriers, and price-setting power.','Draw locally; reuse through Unit 4.','planned'),
('Concentration ratio bar chart','Python chart','Illustrate how market share concentration changes across industries.','Use public industry-share data later; start with clearly labeled illustrative data.','planned'),
('Infrastructure or network photograph','Real-world photo','Show a natural-barrier setting such as rail, utility, or bridge infrastructure.','Use a licensed Commons file.','planned')]),
(19,'Unit 4','Monopoly',[
('Monopoly D-MR-MC-ATC graph','Python chart','Show output, price, profit, consumer surplus, and DWL.','Generated locally.','planned'),
('Entry-barrier storyboard','Concept diagram','Legal, natural, ownership, and network barriers with examples.','Draw locally.','planned'),
('Bridge or utility photograph','Real-world photo','Make a natural monopoly example visually immediate.','Self-created or licensed Commons file.','planned')]),
(20,'Unit 4','Price discrimination',[
('Segmented-price graph','Python chart','Compare one-price monopoly with two or more consumer segments.','Generated locally with illustrative demand schedules.','planned'),
('Price-menu cards','Concept diagram','Movie ticket, student discount, peak/off-peak, and bulk pricing examples.','Draw locally with icons; avoid copying brand material.','planned'),
('Cinema or transit pricing photograph','Real-world photo','Prompt students to identify price discrimination in daily life.','Self-created or licensed Commons file.','planned')]),
(21,'Unit 4','Monopolistic competition',[
('Short-run versus long-run monopolistic competition','Python chart','Show profit/loss in the short run and tangency/zero-profit adjustment in the long run.','Generated locally.','planned'),
('Product differentiation collage','Concept diagram/photo grid','Same broad product category, different brands/features/designs.','Use self-created icons or licensed Commons images.','planned'),
('Restaurant street photograph','Real-world photo','Connect product differentiation and many sellers to a familiar market.','Wikimedia Commons restaurant/street category; check license.','planned')]),
(22,'Unit 4','Oligopoly and game theory',[
('Payoff matrix heatmap','Python chart','Color-code payoffs, dominant strategies, and Nash equilibrium.','Generated locally from a two-firm example.','planned'),
('Repeated-game decision tree','Concept diagram','Show cooperate, defect, retaliation, and repeated interaction.','Draw locally.','planned'),
('Airline or telecom market photograph','Real-world photo','Introduce a market with a small number of visible large firms.','Use a licensed Commons file; avoid trademark-heavy framing.','planned')]),
(23,'Unit 4','Market structure review',[
('Four-market-structure dashboard','Python/diagram','One page comparing price, output, profit, efficiency, and barriers.','Generated locally from Unit 4 visuals.','planned'),
('Efficiency comparison bars','Python chart','Compare competitive output, monopoly output, and DWL.','Generated locally; label as model comparison.','planned'),
('Four-market photo strip','Real-world photo grid','Farm commodity, utility, restaurant, and airline examples.','Use four individually licensed Commons files.','planned')]),
(24,'Unit 5','Introduction to factor markets',[
('Derived-demand chain','Concept diagram','Consumer demand → product price → MRP → factor demand.','Draw locally for the opening explanation.','planned'),
('MRP schedule chart','Python chart','Display product price, marginal product, and MRP in aligned rows.','Generated locally from a production table.','planned'),
('Workplace hiring photograph','Real-world photo','Show a firm choosing workers or inputs.','WIKIMEDIA-FACTORIES or a licensed workplace photo.','planned')]),
(25,'Unit 5','Changes in factor demand and factor supply',[
('Factor-market shift chart','Python chart','Show productivity, product price, migration, education, and alternative opportunities as shifters.','Generated locally with separate mini-panels.','planned'),
('Labor-supply determinants map','Concept diagram','Wage, preferences, population, migration, and working conditions.','Draw locally.','planned'),
('Training or migration photograph','Real-world photo','Connect human capital and labor supply to people and institutions.','Use licensed Commons or public-domain government photo.','planned')]),
(26,'Unit 5','Competitive factor markets',[
('Competitive labor-market equilibrium','Python chart','Show labor demand, labor supply, equilibrium wage, and employment.','Generated locally.','planned'),
('MRP versus factor price decision chart','Concept diagram','Highlight the last input unit hired when MRP equals factor price.','Draw locally; reuse in the handout.','planned'),
('Staffing photograph','Real-world photo','Show a small business scheduling workers and inputs.','Self-created or licensed Commons file.','planned')]),
(27,'Unit 5','Monopsony and review',[
('Monopsony MFC-MRP graph','Python chart','Show employment and wage under monopsony and compare with competition.','Generated locally.','planned'),
('Single-employer labor-market map','Concept diagram','Map workers, one dominant employer, wage-setting, and mobility limits.','Draw locally.','planned'),
('Hospital or company-town photograph','Real-world photo','Use a real-world context where one employer may dominate local hiring.','Use a licensed Commons photo; frame as an example, not proof of monopsony.','planned')]),
(28,'Unit 6','Socially efficient and inefficient market outcomes',[
('Private versus social benefit/cost graph','Python chart','Show efficient quantity, market quantity, and DWL.','Generated locally.','planned'),
('Efficiency triangle animation frames','Concept diagram','Move from market outcome to efficient outcome and shade the change.','Draw locally for the worksheet.','planned'),
('Pollution or congestion photograph','Real-world photo','Introduce the gap between private decision and social cost.','Use a licensed Commons file.','planned')]),
(29,'Unit 6','Externalities',[
('Negative and positive externality pair','Python chart','Compare MSC above MPC and MSB above MPB with policy corrections.','Generated locally.','planned'),
('Pigouvian tax/subsidy decision tree','Concept diagram','Choose tax, subsidy, regulation, or permit based on the externality.','Draw locally.','planned'),
('Traffic or emissions photograph','Real-world photo','Use congestion or pollution as an immediate externality case.','Use a licensed Commons file or public-domain government photo.','planned')]),
(30,'Unit 6','Public and private goods',[
('Rivalry-excludability 2×2 matrix','Concept diagram','Classify private goods, public goods, common resources, and club goods.','Draw locally.','planned'),
('Free-rider participation chart','Python chart','Show provision as contributions rise while individual incentives to free ride remain.','Generated locally from an illustrative class model.','planned'),
('Streetlight or public park photograph','Real-world photo','Make non-excludability and shared use visible.','Use a licensed Commons file.','planned')]),
(31,'Unit 6','Government intervention in different market structures',[
('Policy-tool comparison dashboard','Python/diagram','Compare tax, subsidy, price control, regulation, and antitrust across market structures.','Generated locally from Unit 2, 4, and 6 visuals.','planned'),
('Great Depression unemployment-rate timeline','Python chart','Use UNRATE with historical recession markers as policy-context background; keep macro extension clearly labeled.','FRED-UNRATE; download at build time.','planned'),
('Great Depression breadline or bank-run photograph','Historical photo','Use the historical image to introduce why governments respond to market failures and crises.','WIKIMEDIA-GREAT-DEPRESSION-US or WIKIMEDIA-GREAT-DEPRESSION; verify file license.','planned')]),
(32,'Unit 6','Inequality',[
('Lorenz curve and Gini visual','Python chart','Show equality line, Lorenz curve, and changing Gini values.','Use FRED-GINI for a data context and draw the curve locally.','planned'),
('Income-distribution histogram','Python chart','Compare a compressed and a more unequal distribution using transparent illustrative data.','Generated locally; label hypothetical distributions.','planned'),
('Housing or opportunity photograph','Real-world photo','Prompt discussion of access, wealth, and opportunity without reducing inequality to one image.','Use a licensed Commons or public-domain government photo.','planned')]),
(33,'Unit 6','Market failure FRQ synthesis',[
('Market-failure synthesis map','Concept diagram','Connect externality, public good, common resource, inequality, policy, and DWL.','Draw locally as a one-page revision map.','planned'),
('Policy evidence dashboard','Python chart','Combine quantity, price, surplus, and DWL changes for one policy case.','Generated locally from a selected FRQ-style scenario.','planned'),
('Government response photograph','Historical/real-world photo','Use a relief, infrastructure, or public-service image as a policy-evaluation prompt.','WIKIMEDIA-GREAT-DEPRESSION or public-domain government archive; verify license.','planned')]),
(34,'Review','Core graphs',[
('Six-core-graphs poster','Python/diagram','PPC, supply-demand, cost, perfect competition, monopoly, and externality mini-graphs.','Generated locally from the course graph library.','planned'),
('Blank graph practice sheet','Concept diagram','Same six graphs without labels for retrieval practice.','Generated locally in SVG/PDF later.','planned'),
('Graph-label checklist card','Concept diagram','Axes, curves, old/new points, numbers, units, and shaded areas.','Draw locally for the handout.','planned')]),
(35,'Review','Timed MCQ and error analysis',[
('Timed-practice dashboard','Python chart','Accuracy and response time by Unit and error type.','Generated locally from student practice logs; no personal identifiers.','planned'),
('Error-type heatmap','Python chart','Concept, graph, calculation, reading, and expression errors by topic.','Generated locally from a CSV template.','planned'),
('MCQ workflow card','Concept diagram','Read, predict, calculate, eliminate, check units, record error.','Draw locally for slides.','planned')]),
(36,'Review','Timed FRQ and exam readiness',[
('FRQ response anatomy','Concept diagram','Prompt, graph, calculation, explanation, units, and conclusion in one annotated response.','Draw locally; use an original synthetic example.','planned'),
('Scoring-guideline alignment chart','Python/diagram','Map response components to point opportunities and common misses.','Generated locally from a generic rubric structure; do not reproduce restricted text.','planned'),
('Exam-readiness timeline','Concept diagram','Final week schedule for graph review, MCQ, FRQ, sleep, and materials.','Draw locally.','planned')]),
]


def write_sources():
    with (VIS/'sources.csv').open('w', newline='', encoding='utf-8') as f:
        w=csv.writer(f)
        w.writerow(['source_id','name','type','url','notes'])
        w.writerows(SOURCES)


def write_plan():
    out=['# AP Microeconomics 36-Session Visual Plan','',
         'This is the visual design index for the 36-session course. Each session should have two to five visuals, with two as the minimum and additional charts, diagrams, or context images added when they improve the lesson. The current draft provides a core pair plus an optional third visual; later production can expand a session to four or five when useful. The final count is decided during handout and slide production. The plan is intentionally source-aware so later downloads and Python-generated charts can be tracked without mixing them into the lesson-plan source files.','',
         '## Production rules','',
         '- **Python charts:** generate from public data at build time, save the data snapshot and script, and include a source note on the figure itself.',
         '- **Concept diagrams:** draw locally as SVG/PDF/PNG so labels remain consistent across handouts and slides.',
         '- **Wikimedia Commons:** category pages are discovery indexes. Before copying a file, open its individual description page and record the exact license, author, source, and attribution text.',
         '- **Historical images:** use them to open a discussion or provide context. Do not treat a single photograph as statistical evidence.',
         '- **Macro and banking extensions:** indicator, government, and banking visuals are context modules. They supplement AP Microeconomics and should be labeled as extensions when they are outside the official Unit objective.',
         '', '## Session plans','']
    for session,unit,topic,items in V:
        out += [f'### Session {session} · {unit} · {topic}','']
        for i,(name,kind,purpose,source,status) in enumerate(items,1):
            planned_status = f'{status}; optional extension' if i == 3 else status
            out += [f'{i}. **{name}**', f'   - Type: `{kind}`', f'   - Classroom use: {purpose}', f'   - Source / method: `{source}`', f'   - Status: `{planned_status}`', '']
    out += ['## Cross-cutting visual modules','',
            '### Indicators','',
            '- `indicator-unemployment-rate.png`: FRED `UNRATE`, with recession markers and a separate blank-label version.',
            '- `indicator-inflation-cpi-yoy.png`: FRED `CPIAUCSL`, transformed into year-over-year CPI inflation; explain that an index level and an inflation rate are different quantities.',
            '- `indicator-gdp-growth.png`: FRED `GDP` or real GDP growth series, used as a macro context panel rather than an AP Micro core graph.',
            '- `indicator-policy-rate.png`: FRED `FEDFUNDS`, used to introduce interest-rate policy and the boundary between Micro course content and macro extension.',
            '', '### Government and public policy','',
            '- `government-great-depression-breadline.jpg`: historical photo opening for Unit 6 government objectives.',
            '- `government-bank-run-1933.jpg`: historical photo opening for confidence, financial crisis, and banking extension.',
            '- `government-policy-response-timeline.png`: locally drawn timeline connecting crisis, unemployment, relief, and policy response.',
            '', '### Banking and Wall Street','',
            '- `banking-wall-street-historical.jpg`: Wall Street or bank-building photograph from Wikimedia Commons.',
            '- `banking-bank-run-photo.jpg`: bank-run photograph from Wikimedia Commons.',
            '- `banking-money-and-interest-dashboard.png`: local Python dashboard using `FEDFUNDS`, `M2SL`, and selected market series.',
            '', '## File naming and future folders','',
            'Planned assets should eventually be stored as:',
            '',
            '```text',
            'APMICRO-Teaching/Visual-Plan/assets/',
            '├── data/          # downloaded CSV snapshots',
            '├── python/        # reproducible chart scripts',
            '├── diagrams/      # locally drawn SVG/PDF/PNG',
            '├── wikimedia/     # files with license records',
            '└── exports/       # slide-ready and handout-ready exports',
            '```','',
            'The current turn creates the design index and source catalog. Actual downloads and chart generation should be done in a later asset-production pass, with every file added to a manifest.','']
    (VIS/'visual-plan-36-sessions.md').write_text('\n'.join(out),encoding='utf-8')


def write_readmes():
    (VIS/'assets').mkdir(parents=True, exist_ok=True)
    (BASE/'README.md').write_text('''# AP Microeconomics Teaching Materials\n\nThis folder is the working area for course planning and classroom production.\n\n## Structure\n\n- [`Lesson-Plans/`](Lesson-Plans/) — bilingual 36-session lesson plan, CED objective map, Markdown schedule, and LaTeX/PDF editions.\n- [`Handouts/`](Handouts/) — student-facing worksheets, graph practice, formula sheets, and FRQ/MCQ review pages.\n- [`Slides/`](Slides/) — future English and Chinese PPT/PPTX decks, organized by Unit and session.\n- [`Visual-Plan/`](Visual-Plan/) — visual design index, data-source catalog, and future chart/photo assets.\n\n## Production order\n\n1. Keep the session objective and activity in `Lesson-Plans/` as the source of truth.\n2. Use `Visual-Plan/visual-plan-36-sessions.md` to select or generate the session visuals.\n3. Build the matching worksheet in `Handouts/`.\n4. Build the teacher-facing and student-facing decks in `Slides/`.\n5. Add generated assets and source/license records to the visual manifest before using them in public materials.\n''',encoding='utf-8')
    (BASE/'Handouts'/'README.md').write_text('''# AP Microeconomics Handouts\n\nThis folder is reserved for student-facing materials. Suggested organization:\n\n```text\nHandouts/\n├── Unit-1/ ... Unit-6/\n├── Review/\n└── templates/\n```\n\nEach handout should record its session number, official objective ID, answer-key status, and the visual assets it uses. Keep the handout source editable and export PDFs only after the layout is checked.\n''',encoding='utf-8')
    (BASE/'Slides'/'README.md').write_text('''# AP Microeconomics Slides\n\nThis folder is reserved for PPT/PPTX and slide-source files. Suggested organization:\n\n```text\nSlides/\n├── Unit-1/ ... Unit-6/\n├── Review/\n└── shared/\n```\n\nEach deck should record the session number, official objective ID, visual asset filenames, and whether the deck is English or Chinese. The English deck can remain the primary version, with a linked Chinese edition when both are available.\n''',encoding='utf-8')
    (VIS/'README.md').write_text('''# AP Microeconomics Visual Plan\n\n- [`visual-plan-36-sessions.md`](visual-plan-36-sessions.md) — a flexible two-to-five-visual plan for every session, plus indicator, government, and banking extension modules.\n- [`sources.csv`](sources.csv) — FRED, official course, and Wikimedia Commons discovery sources.\n- `assets/` — reserved for later downloaded images, generated charts, diagrams, data snapshots, and exports.\n\nUse two visuals as the minimum lesson set. Add a third, fourth, or fifth visual when a session benefits from another graph, diagram, data panel, historical image, or real-world example. The plan uses FRED for reproducible public-data charts and Wikimedia Commons for historical or real-world image discovery. Record the exact series ID or individual file page and license before an asset enters a handout or slide deck.\n''',encoding='utf-8')
    (VIS/'assets'/'README.md').write_text('''# Visual Assets\n\nReserved layout for future asset production:\n\n- `data/` — public CSV snapshots and retrieval dates\n- `python/` — chart-generation scripts\n- `diagrams/` — original SVG/PDF/PNG diagrams\n- `wikimedia/` — downloaded files plus license records\n- `exports/` — slide-ready and handout-ready versions\n''',encoding='utf-8')


def main():
    VIS.mkdir(parents=True, exist_ok=True)
    write_sources(); write_plan(); write_readmes()
    print(f'Wrote visual plan for {len(V)} sessions and {len(SOURCES)} source records.')

if __name__=='__main__': main()
