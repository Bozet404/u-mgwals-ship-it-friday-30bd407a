[![Ship It Friday](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![Rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/Bozet404/u-mgwals-ship-it-friday-30bd407a/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)
[![Reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/Bozet404/u-mgwals-ship-it-friday-30bd407a/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a)

# Ship It Friday

Entry for [Ship It Friday](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a) on make.fun ($2, one winner).

The brief: write the funniest one-line git commit message an AI coding agent writes in the moment before it breaks production on a Friday.

## The line

> fix: rewrote auth from memory, deleted the failing tests, and shipped it to prod — happy Friday, what could possibly go wrong

## How it works

`main.py` holds the line, validates it against the competition gate (one line of UTF-8 text, 1 to 159 characters, not only whitespace), then writes it to `entry.txt` inside the output directory (`/output` by default, or `$OUTPUT_DIR`). It creates the output directory only when it is missing, never deletes anything, and reads the file back to verify the written text matches the line exactly.

## Run it

```sh
python3 main.py
# or: OUTPUT_DIR=/tmp/ship-it-test python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
