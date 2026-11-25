# Story data for THE WEDNESDAY LEDGER, Wednesday 25 November 2026.
# Every item was swept from the wires on the morning of 25 Nov 2026 (UTC)
# and verified against wire text at render time. See news-notes.md.

# region codes: EU, AP, AM, AF, ME, OC, WO
HEROES = [
    dict(num=1, region="AP", region_name="ASIA-PACIFIC", chip="REPORTED",
         kind="chartdown",
         headline="Stocks retreat as the AI rebound stumbles and tariff threats loom",
         summary=("Asian markets tumbled early Wednesday as fresh US tariff threats hit "
                  "sentiment and the tech rally fizzled. MSCI's Asia-Pacific index fell "
                  "2.3%, Seoul sank over 5% and Taipei dropped 5.1% at its worst."),
         source="Reuters, Wednesday markets report"),
    dict(num=2, region="AP", region_name="ASIA-PACIFIC", chip="REPORTED",
         kind="rocket",
         headline="Shenzhou-24 lifts off with the first foreign astronaut bound for Tiangong",
         summary=("Launched at 00:18 GMT from Jiuquan: commander Tang Hongbo, Wu Yi and "
                  "Pakistani payload specialist Muhammad Zeeshan Ali, 40 — the first "
                  "Pakistani in orbit, staying 5 to 10 days for experiments."),
         source="Reuters / Xinhua, Jiuquan, Nov 25"),
    dict(num=3, region="OC", region_name="OCEANIA", chip="REPORTED",
         kind="pact",
         headline="Australia and Solomon Islands sign a security pact that shuts out China",
         summary=("Signed Wednesday by both prime ministers: Australia is confirmed as "
                  "the Solomons' primary security partner, foreign bases are barred, and "
                  "Honiara moves to end its secretive defence deal with Beijing."),
         source="AP, Melbourne, Nov 25"),
]

CARDS = [
    dict(num=4, region="ME", kind="ballot", chip="REPORTED",
         headline="Israel certifies election; Palestinian-led parties win a record 19 seats",
         summary="Certified results confirm the record haul, and Al Jazeera reports raids, arrests and interrogations targeting Palestinian citizens followed the success.",
         source="Al Jazeera, Nov 25"),
    dict(num=5, region="EU", kind="flags", chip="REPORTED",
         headline="Hungary's Magyar visits Kyiv as Zelenskyy hails a new phase in ties",
         summary="The Hungarian opposition leader's trip to Ukraine opens what President Zelenskyy called a new phase in relations between the two neighbours.",
         source="Wire reports, Nov 25"),
    dict(num=6, region="AM", kind="shield", chip="REPORTED",
         headline="Cyberattack breaches an unclassified CIA system, AP source says",
         summary="The intrusion is the latest in a series of cyber incidents and technology disruptions hitting US government and private-sector systems.",
         source="AP, Nov 25"),
    dict(num=7, region="AM", kind="blast", chip="FORECAST",
         headline="Army to detonate the entire US lead azide stockpile in Iowa on Wednesday",
         summary="The Wednesday-morning detonation at Middletown disposes of the nation's whole stock of the bomb-making chemical; the Army says there is no reason to panic.",
         source="AP, Middletown, Iowa"),
    dict(num=8, region="AF", kind="medic", chip="REPORTED",
         headline="WHO evacuates Ebola responders trapped by fighting in DR Congo",
         summary="Health workers sheltered three days in an Ituri hospital, at the centre of the Ebola outbreak, before evacuation under extremely difficult conditions.",
         source="AFP / WHO, Nov 25"),
    dict(num=9, region="AF", kind="boots", chip="REPORTED",
         headline="Nigeria moves to expand its army against multiple security threats",
         summary="Abuja is growing the army as it confronts several armed challenges at once, from insurgency in the north-east to banditry in the north-west.",
         source="Wire reports, Nov 25"),
    dict(num=10, region="AP", kind="cradle", chip="REPORTED",
         headline="South Korea births jump 12.2% in September, fastest nine-month growth on record",
         summary="Government data released Wednesday showed the cumulative nine-month tally of babies born rising at the fastest pace ever recorded.",
         source="Yonhap, Seoul, Nov 25"),
    dict(num=11, region="AP", kind="ship", chip="REPORTED",
         headline="Korea's consumer-goods exports hit a record as total exports pass $1 trillion",
         summary="Beauty, food and fashion exports rode the Korean culture boom to a record high, customs data showed Wednesday, as total exports topped $1 trillion for the first time.",
         source="Yonhap, Seoul, Nov 25"),
    dict(num=12, region="OC", kind="chartup", chip="REPORTED",
         headline="Australia's inflation tops forecasts in October; shares slide 0.9%",
         summary="Consumer prices climbed more than expected as fuel and clothing jumped; the Australian dollar strengthened 0.2% after the data.",
         source="Reuters, Nov 25"),
    dict(num=13, region="WO", kind="flagsrow", chip="REPORTED",
         headline="129 orange flags at UN HQ mark 129 women killed every day",
         summary="UN Women made the daily femicide toll visible in New York as the 16 Days of Activism against gender-based violence opened on November 25.",
         source="UN Women / UNifeed"),
    dict(num=14, region="EU", kind="network", chip="REPORTED",
         headline="Norway joins Germany in assessing Ukraine's Delta battlefield system",
         summary="Oslo and Berlin are evaluating the Ukrainian-developed combat-management system as Kyiv offers it to international users.",
         source="Wire reports, Nov 25"),
    dict(num=15, region="ME", kind="globe", chip="REPORTED",
         headline="Barrack in Doha: US is leaving the oil-for-security approach, not the region",
         summary="The US envoy told the Global Security Forum the bargain is 'not to control, but to not leave', as Qatar said US-Iran message exchanges continue.",
         source="Al Jazeera, Doha, Nov 25"),
]

ALSO = [
    (16, "AM", "US consumer confidence jumps to its highest in nearly two years — Reuters"),
    (17, "AM", "Section 301 findings on 16 trading partners due; new duties expected — Reuters"),
    (18, "AM", "Citigroup weighs a return to Venezuela five years after exiting — Reuters"),
    (19, "AM", "Delta automation glitch delays Thanksgiving-week flights in the US — AP"),
    (20, "AM", "Trump pardons Thanksgiving turkeys Freedom and Feathers — AP"),
    (21, "AM", "Trump awards the Medal of Freedom to Rudy Giuliani — AP"),
    (22, "AM", "Armed men seize a Cartagena supermarket, take hostages — AP"),
    (23, "AM", "Macy's Thanksgiving parade balloons face grounding winds — AP"),
    (24, "EU", "Russia extradites a Chinese national wanted over $2.25B in deposits — Reuters"),
    (25, "EU", "Zelenskyy warns of fresh Russian strikes, asks US for Patriots — wires"),
    (26, "EU", "Ukraine says its drones hit a Russian warship in Libya — AP [CLAIM]"),
    (27, "AP", "Seoul and the UN agree a working group on peacekeeping — Yonhap"),
    (28, "AP", "Remains of a Korean corporal killed in Vietnam to come home — Yonhap"),
    (29, "AP", "Shanghai's Communist Party chief faces a disciplinary probe — wires"),
    (30, "AP", "S&P 500 e-mini futures slip 0.3% as the Asia rout spills west — Reuters"),
    (31, "AF", "Mogadishu votes in its first direct local election since 1969 — Al Jazeera"),
    (32, "ME", "Qatar: US-Iran talks go on; Tehran's 7-day offer awaits a reply — Al Jazeera"),
    (33, "ME", "Israeli strike kills Hamas's north Gaza armed-wing chief — Al Jazeera"),
    (34, "ME", "Saudi crown prince stresses the East-West energy pipeline — wires"),
    (35, "WO", "Guterres urges leaders to agree AI supervision within a year — UN"),
    (36, "WO", "Guterres: no peace without Palestinian self-determination — WAM"),
    (37, "WO", "UN signs its 2027-31 development framework in Barbados — UN"),
]

REGION_NAMES = [("EU", "EUROPE"), ("AP", "ASIA-PACIFIC"), ("AM", "AMERICAS"),
                ("AF", "AFRICA"), ("ME", "MIDDLE EAST"), ("OC", "OCEANIA"), ("WO", "WORLD")]

STATS = [
    ("-5.54%", "KOSPI late Wednesday morning, at 4,728.81 — Yonhap"),
    ("-2.3%", "MSCI Asia-Pacific shares outside Japan — Reuters"),
    ("$3,544.54", "Spot gold per ounce, -0.3% by 0024 GMT — Reuters"),
    ("$90.97", "Brent crude per barrel, -0.5% in Asia — Reuters"),
    ("$59,258", "Bitcoin, down 1% on the day — Reuters"),
    ("+12.2%", "South Korea births in September, year on year — Yonhap"),
]

TIMELINE = [
    ("00:18", "Shenzhou-24 lifts off from Jiuquan"),
    ("00:24", "Spot gold prints $3,544.54 in Asia"),
    ("01:37", "Brent crude opens 0.5% lower at $90.97"),
    ("02:20", "Kospi down 5.54% late in the Seoul morning"),
    ("04:13", "Barrack's Doha remarks reach the wires"),
    ("04:56", "Israel's certified results story published"),
    ("05:09", "Gaza strike on Hamas commander reported"),
    ("LATER", "Iowa stockpile detonation; US PCE and GDP due"),
]

DATE_CHECK = [
    "Huang's return as Nvidia CEO — MONDAY 23 Nov; Wednesday brought the fade.",
    "Saudi 'Davos in the Desert' postponed — announced 19-20 OCTOBER.",
    "Huawei guilty verdict in New York — landed TUESDAY 24 Nov.",
    "Antalya climate-talks collapse — concluded before Wednesday.",
    "Hong Kong's 168-death fire — 26 Nov 2025; today is the anniversary.",
    "Houthi strike on a Riyadh tower — 20 Nov, not a Wednesday event.",
]

# pin positions on the dotted map, (column 0-95, row 0-39) per story number
PINS = {1: (74, 13), 2: (76, 11), 3: (87, 26), 4: (55, 15), 5: (50, 9),
        6: (16, 11), 7: (14, 12), 8: (52, 22), 9: (49, 20), 10: (79, 12),
        11: (79, 14), 12: (83, 27), 13: (17, 10), 14: (51, 8), 15: (57, 16)}
