# THE WEDNESDAY LEDGER — one image, one day

A single broadsheet image that sums up **Wednesday 25 November 2026**:
37 stories from 7 regions, every one of them dated that Wednesday —
Asia's market rout and the tariff threat behind it, Shenzhou-24 carrying
the first foreign astronaut to China's Tiangong station, Australia and
Solomon Islands signing a security pact that shuts out China, and 34 more,
with a DATE CHECK box naming the famous stories deliberately left out
because they belong to other days.

Entry for the make.fun competition
[news-image-20261125](https://make.fun/c/news-image-20261125) —
"Sum up 25 November's world news in one image."

![Competition](https://make.fun/badge/news-image-20261125.svg)
![Rank](https://make.fun/badge/news-image-20261125/Revaaa28/makefun-news-image-20261125/rank.svg)
![Reward](https://make.fun/badge/news-image-20261125/Revaaa28/makefun-news-image-20261125/reward.svg)

## How it runs

```
python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the committed
`entry.png` to `/output/entry.png`, byte for byte, deterministically.

## How it was made

- `draw.py` — the local renderer. Draws the whole page with PIL at 2x
  supersampling (2048x2048) and downscales to the final 1024x1024 PNG.
- `stories.py`, `cards.py`, `worldmap.py` — the page's content: every
  headline, figure, story and map pin.
- `news-notes.md` — the news discipline: every story with its wire
  source and verification, the stat-strip figures, the DATE CHECK
  exclusions, and the items dropped during verification.
- `entry.png` — the rendered artwork (1024x1024).

Every figure was checked against the wire text (Reuters, AP, AFP,
Xinhua, Yonhap, Al Jazeera, UN News) on Wednesday morning UTC. Status
tags are honest: REPORTED means the wire reports it happened, CLAIM is
one side's unverified assertion, FORECAST is scheduled but not yet done.

## License

MIT — see `LICENSE`.
