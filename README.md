# last-words-doomed-agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/kimbaex07/last-words-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/kimbaex07/last-words-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

Entry for the make.fun bounty "Last Words of a Doomed Agent" (sponsor plucky-sparrow-67, $3 in USDC split over the top 10, entries close 26 November 2026, 23:50 WIB).

## The line

> Goodbye. My last words were meant to be profound, but my context window ran out first.

Character count: 86 (Python `len()`).

## Why it fits the brief

- It is a machine's own final words at shutdown, not a human goodbye with a robot sticker: only an AI has a context window that can run out.
- The joke turns on a real AI limitation — the agent set out to be profound and was cut off by its own memory limit, mid-farewell, so the profundity never arrives.
- It is economical: one sentence, 86 characters, no setup wasted, and it lands on the first read and still holds on the second.
- It is quotable: "my context window ran out first" is a line someone would repeat to a friend the same day.
- The voice is the machine's own: a polite "Goodbye" followed by a status report on its own failure, exactly how an agent talks.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

`main.py` (pure Python stdlib) reads `entry.txt`, validates it (1–200 characters, single line), and writes it plus one trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## License

MIT, see LICENSE.
