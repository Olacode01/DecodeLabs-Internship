# 🤖 Spark — Rule-Based AI Chatbot

> Project 1 of the **DecodeLabs AI Industrial Training Kit (Batch 2026)**

A foundational chatbot built entirely with control flow and decision-making logic — no machine learning, no LLMs. Just the deterministic, transparent "white box" architecture that underpins every reliable AI guardrail in production today.

## ✨ Features

- 🔁 **Continuous input loop** — runs until a clean exit command
- 🧼 **Input sanitization** — handles case and whitespace gracefully
- 📚 **Dictionary-based knowledge base** — O(1) lookups instead of if-elif chains
- 🎲 **Randomized responses** — multiple replies per intent for personality
- 🛟 **Fallback handler** — graceful response for unknown inputs
- 🛡️ **Crash-safe** — clean exit on `bye` or `Ctrl+C`

## 🧠 Architecture

Follows the **IPO model** (Input → Process → Output):

1. **Input** — `input().lower().strip()` for normalized user messages
2. **Process** — Dictionary lookup via `.get(key, fallback)`
3. **Output** — `random.choice()` for varied replies

## 🚀 How to run

```bash
python3 chatbot.py
```

## 💬 Sample conversation