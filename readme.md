# Cognitive Ability Test

A Python app that measures **Language**, **Reasoning**, and **Memory** using multiple-choice questions and adaptive difficulty.

## What it does
- Shows a short memory stimulus first.
- Runs Language and Reasoning sections with adaptive difficulty (`easy -> medium -> hard`).
- Runs Memory recall questions after distraction phases.
- Builds a final score, percentage, and cognitive level.

## Run
```bash
python -m pip install -r requirements.txt
python main_gui.py
```

CLI entry point also exists:
```bash
python main_cli.py
```
