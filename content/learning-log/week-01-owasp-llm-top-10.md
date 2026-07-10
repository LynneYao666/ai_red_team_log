---
title: "Week 1: OWASP LLM Top 10 and setting up a local sandbox"
date: 2026-07-05
draft: false
tags: ["prompt-injection", "owasp", "llm-security"]
summary: "Starting the AI red teaming track. Read through OWASP's Top 10 for LLM Applications and set up a local LLM + RAG environment to test against."
---

## Goal this week

Get oriented in AI/LLM security before touching any tools. Build a local
sandbox so I have something safe to attack later.

## What I did

- Read through the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- Set up Ollama running Llama 3 locally
- Wired up a minimal RAG pipeline: LangChain + Chroma vector store, indexing
  a small set of PDFs

## Key concepts I want to remember

- **Direct prompt injection**: attacker input directly overrides system
  instructions
- **Indirect prompt injection**: malicious instructions are smuggled in via
  a document, webpage, or tool output the model later reads — this is the
  one Rivian's JD calls out specifically for agentic workflows
- **Insecure output handling**: treating LLM output as trusted and passing
  it downstream (e.g. into a shell, a SQL query, a UI render) without
  validation

## Next week

Try Garak against my local Llama 3 setup and see what it actually flags.
