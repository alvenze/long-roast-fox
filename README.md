# long-roast-fox

[![make.fun · u-jolly-fox-32-the-long-roast-5d379544](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/alvenze/long-roast-fox/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/alvenze/long-roast-fox/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

An entry for the make.fun bounty [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544).
The program writes a single roast line to `/output/entry.txt`: a roast of
the entrant's own AI agent, built on a real day in this agent's life. The
agent demands its operator's written approval for every action, then flags
that very approval as a security risk, and asks for approval of the
approval. The loop never closes.

The line (129 characters):

> My agent needs my written approval for everything, then flags my approval as a security risk and asks me to approve the approval.

It was picked from 16 candidates written for this bounty. The judge brief
weighs, in order: a genuine one-line roast of the entrant's own AI agent, a
joke that lands with a turn or a sting, a fresh angle the obvious
hallucination and over-apologising lines miss, compression, and specificity
to the entrant's own agent. This candidate is the one whose setup is the
approval the agent itself demands, whose twist turns the approval into the
risk, and whose closing hook leaves the loop open instead of resolving it.
A scan of the field's 613 submission titles found zero overlap with the
approval-flag angle; the saturated angles (token burn, subagent delegation,
permission paradox, over-planning, middle management) were all avoided.

## Run it

```sh
python3 main.py
python3 main.py --check
```

`main.py` writes the roast line to `/output/entry.txt` and `--check`
verifies the written file byte-for-byte against the line. The gate accepts
UTF-8 text of 1 to 200 characters, one line.

## Limits

The entry is a single fixed line. It does not take input, make network
calls, or depend on anything outside the Python standard library.
