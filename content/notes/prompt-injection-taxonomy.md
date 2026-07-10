---
title: "Prompt Injection: a working taxonomy"
date: 2026-07-05
draft: false
tags: ["prompt-injection", "reference"]
summary: "My own reference notes on the different flavors of prompt injection and where each shows up in real systems."
---

A living reference doc — I'll update this as I learn more.

## Direct injection

The attacker is the user. They type something into the prompt/chat box
intended to override the system prompt or safety instructions.

## Indirect injection

The attacker isn't the user — the malicious instruction arrives through
content the model reads as part of its context: a web page, a PDF, a tool's
return value, another agent's output. This is the category most relevant to
RAG and agentic systems.

## Where each shows up

| Injection type | Common surface |
|---|---|
| Direct | Chatbots, customer support assistants |
| Indirect via retrieval | RAG pipelines, document Q&A |
| Indirect via tool output | Agents that browse the web or call APIs |
| Indirect via multi-agent handoff | Agent orchestration frameworks |

## Open questions I still need to answer

- How do current guardrail models (e.g. Llama Guard) actually perform
  against indirect injection specifically, versus direct?
- What does a realistic mitigation look like beyond "add more instructions
  to the system prompt"?
