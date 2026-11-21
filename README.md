# The World in One Day — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Mastomy2/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Mastomy2/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun bounty [news-image-20261120](https://make.fun/bounty/news-image-20261120):
one image summing up the world's news of Friday 20 November 2026.

## The image

`image.png` (1024×1024, 589,569 bytes, full colour) is a newspaper-style
poster: a navy masthead naming the day, then twelve numbered stories in
a three-by-four grid, each with a region tag, a headline, a short
summary and its source. Round 5 rebuilds the poster from scratch after
checking every story against live reporting. Every event below is dated
Friday 20 November 2026 in its source — events from 19 November
(the Shenzhen summit, the ICJ Myanmar ruling, the Haiti police
operation, the Colombia strike, the Taiwan ADIZ incursion, the
Denmark–Greenland vote, the Anthropic IPO debut) were checked and
deliberately left out.

1. **Russian missiles land in Poland** — Europe. Russia's biggest
   November barrage hits Kyiv (110+ missiles, 400+ drones, 8 killed);
   two missiles and a drone crash in Poland. NATO calls it a "grave
   violation" (AP / ISW / CNN)
2. **UK and EU strike landmark deal** — Europe. The second EU–UK summit
   in Brussels ends with food-trade and youth-mobility pacts (100,000
   places each way); von der Leyen calls it a "turning point"
   (AP / Le Monde / European Council)
3. **Ukraine reveals "Bear Trap" victory** — Europe. Kyiv discloses a
   secret counteroffensive that retook 14 settlements and ~200 sq km in
   northern Kharkiv (BBC News Ukraine / 112.ua, reported 20 Nov)
4. **Cyclone Akvan hits India's east coast** — Asia. Landfall near
   Gopalpur, Odisha, on Friday morning; 372,000 people evacuated, 423
   rescue teams deployed, no major damage reported (IMD / The Hindu)
5. **Xi hails Australia "turnaround"** — Asia–Pacific. Xi tells PM
   Anthony Albanese ties have seen a "comprehensive turnaround" at
   APEC in Shenzhen, pitching more cooperation on agriculture and AI
   (Reuters)
6. **Houthi missile hits Riyadh's tallest tower** — Middle East. The
   blast blew out windows across 7–8 floors of the PIF Tower, HQ of
   Saudi Arabia's sovereign wealth fund; no injuries (Reuters / WSJ)
7. **Tanker struck near Hormuz** — Middle East. A tanker is hit by an
   unidentified projectile 8 nautical miles north of Khasab, Oman, as
   Trump claims "total control" of the strait; US Treasury sanctions
   four Iranian oil facilitators the same day (UKMTO / Reuters)
8. **COP31 draft drops fossil fuels** — Middle East (Türkiye). Final-day
   talks in Antalya stall as the draft cover decision omits oil, gas
   and coal while acknowledging a 1.5°C overshoot (Reuters / UN News)
9. **Senate backs Trump on Iran war, 51–48** — North America. Senators
   reject curbs on the president's Iran war powers; Trump says "we'll
   see what happens after January 1" (Reuters)
10. **Wall Street sinks into correction** — North America. An AI-led
    sell-off: the S&P 500 fell 3.7% to 6,910, the Nasdaq 5.3% and
    turned negative for 2026; the Nikkei fell 5.1%, Nvidia 14% (AP)
11. **Trump threatens data-center tax** — North America. At a White
    House news conference after his Asia trip, Trump says US firms
    building data centers abroad face a "tremendous tax" (Reuters / WSJ)
12. **GTA VI banks an estimated $1.84bn** — Culture. A record launch:
    ~19m copies sold by day one on Sensor Tower's estimate, topping
    the year's biggest film at the box office (Sensor Tower / Reuters)

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
