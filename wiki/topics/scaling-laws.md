---
title: Scaling Laws
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["scaling laws", "AI scaling", "compute scaling", "neural scaling laws", "chinchilla scaling", "LLM training", "pretraining"]
related: ["[[AI Coding Agents]]", "[[AI-Native Software]]", "[[Andrej Karpathy]]"]
sources: ["Ml-scaling-and-the-road-to-human-level-ai-anthropic-co-founder-jared-kaplan", "Mw-how-to-train-an-llm-with-anthropic-s-head-of-pretraining", "Mr-gpt-oss-vs-qwen-vs-deepseek-comparing-open-source-llm-architectures", "N3-transformers-explained-the-discovery-that-changed-ai-forever"]
speakers_referenced: ["Jared Kaplan"]
---

# Scaling Laws

Scaling laws describe the empirical relationship between compute, data, model size, and AI performance. Jared Kaplan, Anthropic co-founder, helped establish the foundational research showing that language model performance improves predictably as these variables increase, following power law relationships [1]. This research underpins the strategy of every major AI lab and has profound implications for AI startups.

## The Core Finding

Kaplan's scaling laws research at OpenAI (later refined by the Chinchilla paper from DeepMind) showed that loss (a proxy for model capability) decreases as a smooth function of compute, dataset size, and model parameters [1]. The relationship is a power law: each 10x increase in compute yields a predictable improvement in capability.

The practical implication: if you know the scaling laws for your domain, you can predict how much better a model will be with more compute before you spend the money to train it. This turns AI research into something closer to engineering, where results are predictable within bounds [1].

## How to Train an LLM

Anthropic's head of pretraining describes the practical process of training frontier language models [2]. Key insights:

- **Data quality dominates data quantity.** Careful curation and deduplication of training data matters more than sheer volume. The best models are trained on carefully selected subsets of the internet, not everything [2].
- **Curriculum matters.** The order in which training data is presented affects final model quality. Starting with high-quality text and gradually mixing in more diverse data produces better results than random sampling [2].
- **Evaluation is continuous.** Training runs cost millions of dollars and take weeks. Catching problems early requires constant monitoring of intermediate checkpoints against evaluation benchmarks [2].

## Open Source LLM Architectures

The open-source LLM ecosystem has produced competitive models through different architectural choices [3]:

- **DeepSeek** pioneered mixture-of-experts architectures that activate only a fraction of parameters per token, dramatically reducing inference cost [3].
- **Qwen** (Alibaba) and other Chinese labs have demonstrated that scaling laws hold across languages and training regimes [3].
- **GPT-OSS** alternatives are narrowing the gap with frontier models, particularly for specialized tasks [3].

## The Transformer Foundation

The transformer architecture, introduced in the "Attention Is All You Need" paper, is the foundation for all current language models [4]. The self-attention mechanism allows models to weigh the relevance of different parts of the input when generating each output token. This architecture scales better with compute than previous approaches (RNNs, LSTMs), which is why scaling laws work as well as they do [4].

## Implications for Startups

For AI startups, scaling laws create both opportunities and constraints:

- **Frontier models will keep improving.** If scaling continues, the capabilities available to startups via APIs will grow predictably. Building on the assumption that models get better is a safe bet [1].
- **Fine-tuning has its own scaling dynamics.** Smaller models fine-tuned on domain-specific data can match larger general models for specific tasks. This creates opportunities for startups that accumulate high-quality domain data [2].
- **Inference cost matters.** The economics of deploying AI at scale depend on inference efficiency. Startups that can achieve the same quality with fewer parameters or smarter architecture have a structural advantage [3].

## References

1. [Scaling and the Road to Human-Level AI: Anthropic Co-Founder Jared Kaplan](https://www.youtube.com/watch?v=placeholder) -- Jared Kaplan (2025)
2. [How to Train an LLM with Anthropic's Head of Pretraining](https://www.youtube.com/watch?v=placeholder) -- Anthropic (2025)
3. [GPT-OSS vs Qwen vs DeepSeek: Comparing Open Source LLM Architectures](https://www.youtube.com/watch?v=placeholder) -- Y Combinator (2025)
4. [Transformers Explained: The Discovery That Changed AI Forever](https://www.youtube.com/watch?v=placeholder) -- Y Combinator (2025)
