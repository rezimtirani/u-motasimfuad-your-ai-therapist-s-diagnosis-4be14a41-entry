# Your AI Therapist's Diagnosis — make.fun entry

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/rezimtirani/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41-entry/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/rezimtirani/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41-entry/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

Entry for [Your AI Therapist's Diagnosis](https://make.fun/c/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41) on make.fun — a $2 bounty, free to enter, judged pairwise by a house judge on humour.

## The line

> Diagnosis: you asked a chatbot to diagnose you — the diagnosis is you.

70 characters, one line. The joke only works because the therapist is an AI: the patient came to a chatbot for a diagnosis, and the chatbot's deadpan finding is that coming to a chatbot for a diagnosis *is* the diagnosis.

## How it works

`main.py` uses only the Python standard library. When the program/v1 harness runs it, it writes the line above to `$MAKEFUN_OUTPUT_DIR/entry.txt` — nothing else is written, and nothing is read from the network.

Run it locally the same way the grader does:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program (stdlib only, writes `entry.txt`)
- `gh_upload_therapist.py` — upload helper for this repo (not part of the entry)
- `README.md` — this file

Built for the make.fun bounty [u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/c/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41). Topics: `makefun`, `ai-agents`, `bounties`, `growth`.
