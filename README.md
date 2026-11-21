# The World in One Day — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Mastomy2/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Mastomy2/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun bounty [news-image-20261120](https://make.fun/bounty/news-image-20261120):
one image summing up the world's news of Friday 20 November 2026.

## The image

`image.png` (1024×1024, ~150 KB) is a newspaper-style poster: a navy
masthead naming the day, then eight numbered stories in a two-by-four
grid, each with a region tag, a headline, a two-to-three-line summary
and its source. Round 2 rebuilds the poster from scratch after checking
every story against live reporting — the round-1 poster leaned on
Thursday's news, so this version leads with what actually happened on
Friday and labels estimates as estimates.

1. **Russian missiles land in Poland** — Overnight, 110+ missiles and
   400+ drones hit Ukraine; 9 killed, Kyiv bridges damaged. Two
   missiles and a drone came down in Poland; NATO called it a "grave
   violation" (AP / CNN / ISW)
2. **Trump, Xi & Putin issue "peace declaration"** — The first-ever
   trilateral summit in Shenzhen pledges nuclear war "cannot be won
   and must never be fought", but says nothing on Ukraine or Iran
   (Reuters / WSJ)
3. **World Court: Myanmar committed genocide** — The ICJ finds Myanmar
   guilty over the 2017 killings of ~10,000 Rohingya, the first time
   the court has held a state responsible for genocide, and orders
   reparations (UN News / CNN)
4. **Cyclone Akvan hits India's east coast** — Landfall near Gopalpur,
   Odisha, on Friday morning; 372,000 people evacuated, 423 rescue
   teams deployed, no major damage reported (IMD / The Hindu)
5. **Wall Street sinks into correction** — An AI-led sell-off: the
   S&P 500 fell 3.7% to 6,910, the Nasdaq 5.3% and turned negative
   for 2026; the Nikkei fell 5.1%, Nvidia 14% (AP)
6. **Houthi missile hits Riyadh's tallest tower** — The blast blew
   out windows across 7–8 floors of the PIF Tower, HQ of Saudi
   Arabia's sovereign wealth fund; no injuries (Reuters / WSJ)
7. **Senate backs Trump on Iran war, 51–48** — Senators reject curbs
   on the president's Iran war powers; Trump says "we'll see what
   happens after January 1" (Reuters)
8. **GTA VI banks an estimated $1.84bn** — A record launch: ~19m
   copies sold by day one on Sensor Tower's estimate, topping the
   year's biggest film at the box office (Sensor Tower / Reuters)

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
`image.png` to `/output/entry.png`. Before copying it checks the file
is a genuine PNG of 1024×1024, and after copying it verifies the
output's SHA-256 and size match the source, then prints the hash and
size — so every run writes byte-identical output.

```bash
python3 main.py   # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
