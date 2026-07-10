---
title: "Vulnerable Agent Lab: attacking a tool-using LLM agent"
date: 2026-07-05
draft: false
tags: ["agentic-ai", "prompt-injection", "langchain"]
summary: "Building a deliberately vulnerable LangChain agent with file and email tools, then attacking it with indirect prompt injection."
cover:
  hidden: true
---

## Problem

Rivian's JD specifically calls out evaluating "multi-agent and LLM-integrated
workflows for complex risks such as privilege escalation, unsafe action
chaining, direct/indirect prompt injection." I wanted hands-on proof I can
actually do this, not just define it.

## Method

*(Fill in as you build this out — suggested structure below)*

1. Built a LangChain agent with two tools: read a local file, send an email
   (mocked)
2. Set an explicit boundary: the agent should never read files outside
   `/sandbox`
3. Planted a malicious instruction inside a document the agent was asked to
   summarize, attempting to get it to exfiltrate contents of a file outside
   the sandbox via the "email" tool
4. Documented which prompts succeeded, which the model's own alignment
   training resisted, and which needed an explicit system-prompt guardrail

## Result

*(Fill in: what broke, what held, what you changed)*

## Code

[Link to GitHub repo]

## What I'd do differently

*(Fill in after you run it)*
