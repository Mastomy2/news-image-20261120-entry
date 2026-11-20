# The World in One Day — 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Mastomy2/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Mastomy2/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the make.fun bounty [news-image-20261120](https://make.fun/bounty/news-image-20261120):
sum up the world's news of Friday 20 November 2026 in one image.

## The image

`image.png` (1024×1024) packs the day's six defining world stories into
one poster — two columns of three cards, each with a headline, a one-line
summary, and its source:

1. **Trump, Xi & Putin issue "peace declaration"** — First-ever trilateral
   summit in Shenzhen ends with a pledge that nuclear war "cannot be won
   and must never be fought" (BBC / Reuters)
2. **Houthi strike hits Riyadh's tallest tower** — A missile damages the
   PIF Tower, HQ of Saudi Arabia's sovereign wealth fund, blowing out
   windows across several floors (Reuters / AFP)
3. **Trump: "see what happens" on Iran after Jan 1** — US president says
   no rush on the Iran decision; the Senate votes 51–48 to reject curbs
   on his Iran war powers (Reuters)
4. **Cyclone Akvan hits India's east coast** — The severe storm makes
   landfall near Gopalpur, Odisha, today; over 300,000 people evacuated
   and hundreds of rescue teams deployed (The Hindu / IMD)
5. **Van Gogh sells for record $190.4m** — "Chestnut Trees in Blossom"
   (1890) sets a Van Gogh auction record at Sotheby's New York, topping
   the 2022 mark of $117.2m (Reuters / Sotheby's)
6. **GTA VI banks $1.84bn on day one** — An estimated 19m copies sold by
   launch day, topping the entire box-office run of Nolan's "The Odyssey"
   ($1.80bn) (Sensor Tower / Reuters)

## How it works

`main.py` (Python 3.13, standard library only, no network) copies
`image.png` to `/output/entry.png`. It first checks the file is a real PNG
of 1024×1024, then verifies the output SHA-256 and size match the source,
so every run writes byte-identical output.

```bash
python3 main.py   # writes /output/entry.png
```

## License

MIT — see [LICENSE](LICENSE).
