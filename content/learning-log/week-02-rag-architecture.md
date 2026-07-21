---
title: "Week 2: RAG Pipeline Architecture Review"
draft: false
tags: ["rag", "langchain", "chromadb", "architecture"]
summary: "Reviewing the two phases of my RAG pipeline — indexing and query — and drawing out the full data flow."
---

## Goal

Step back from the code and map out the full data flow of the RAG pipeline
built this week: documents in, answers out.

## Architecture

```mermaid
flowchart TD
    subgraph Indexing["Indexing (run once)"]
        A[Documents<br/>5 txt files] --> B[Chunking<br/>split into text chunks]
        B --> C[Embedding<br/>nomic-embed-text to vectors]
        C --> D[Vector Store<br/>stored in Chroma]
    end

    subgraph Query["Query (every question)"]
        E[User Question] --> F[Retrieval<br/>top-k most similar chunks]
        F --> G[Prompt Building<br/>context + question merged]
        G --> H[Generation<br/>llama3:8b writes the answer]
    end

    D -.stored vectors enable retrieval.-> F
```

## Key takeaway

Indexing and query are two independent lifecycles: indexing runs once to
build the knowledge base, while query runs on every question. The vector
store is the connection point between them — which is exactly why it
becomes its own attack surface (next week's poisoning experiments target
this connection point).

![RAG pipeline architecture](/images/2026-07-21-RAG.png)
