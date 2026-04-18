---
title: "GPT-OSS vs. Qwen vs. Deepseek: Comparing Open Source LLM Architectures"
slug: "Mr-gpt-oss-vs-qwen-vs-deepseek-comparing-open-source-llm-architectures"
media_type: "Video"
author: "Ankit Gupta"
speakers: ["Speaker"]
categories: []
description: "OpenAI recently released its first open-weights model since GPT-2, entering a field led by DeepSeek and Alibaba's Qwen. YC's Ankit Gupta breaks down everything you need to know about these top OSS models, including what sets them apart under the hood."
url: "https://ycombinator.com/library/Mr-gpt-oss-vs-qwen-vs-deepseek-comparing-open-source-llm-architectures"
youtube_id: "raTbhtKZTZA"
youtube_url: "https://www.youtube.com/watch?v=raTbhtKZTZA"
transcript_source: "yc_page"
multi_speaker: false
speaker_labels: true
---

# GPT-OSS vs. Qwen vs. Deepseek: Comparing Open Source LLM Architectures

OpenAI recently released its first open-weights model since GPT-2, entering a field led by DeepSeek and Alibaba's
Qwen.

YC's Ankit Gupta breaks down everything you need to know about these top OSS models, including what sets them apart
under the hood. He’ll compare their approaches to mixture-of-experts, long-context training, and post-training
techniques that shape reasoning and alignment—and explore how different design choices lead to surprisingly similar
performance.

## Transcript

Speaker: OpenAI recently dropped GPT-OSS, its first open weights model since GPT-2 in 2019. It's one of the highest profile open source model launches since DeepSeek R1 made waves back in January. But how does GPT-OSS compare to the other top open source models out there architecturally? Let's find out.

Speaker: GPT-OSS is one of OpenAI's most anticipated recent launches—a large, fully open weights model from one of the leading American AI labs. Let's take a closer look at the paper to find out how it was actually engineered and trained.

Speaker: GPT-OSS is a mixture of experts model available in two sizes: 120 billion parameters and 20 billion parameters. Each token activates the top four experts, meaning only a portion of the total parameters are used at any given time. This allows for efficient inference without sacrificing the benefits of a larger model.

Speaker: Trained as a decoder-only transformer, GPT-OSS incorporates plenty of features typical to modern LLMs. This includes grouped query attention, a modified attention mechanism that lets multiple query heads share the same key-value pairs to reduce memory use and speed up inference. It also includes SwiGLU activations in the feed-forward network layers, which allow for more nuanced transformations than simpler activations like ReLU. As well as rotary positional embeddings, or RoPE, which encode token position directly into the attention mechanism to support longer contexts. Finally, the model also makes use of RMS norm with pre-normalization, a normalization method that scales inputs by their root mean square for more stable training.

Speaker: One standout capability of the model is its 131,000 token context window, which it achieves by applying YaRN scaling during pre-training rather than as an inference-time adjustment. We'll touch on what this means a little bit later in the video.

Speaker: For GPT-OSS, OpenAI makes use of their open-source o200K Harmony tokenizer. This byte-pair encoding tokenizer has over 200,000 tokens and builds on the o200K tokenizer used in models like GPT-4.

Speaker: As for the dataset GPT-OSS was trained on, OpenAI has only disclosed the broad strokes. The model was trained on a text-only corpus in the trillions of tokens with a focus on STEM, coding, and general knowledge. Harmful content was filtered out for safety, but beyond that, there's little else known publicly.

Speaker: Once training was complete, the model was released in a quantized format by default, making it lightweight enough for deployment on modest hardware. This allows it to be run on consumer-grade GPUs, laptops, or other resource-limited hardware. However, there's no unquantized version available.

Speaker: GPT-OSS also underwent substantial post-training for safety and alignment, shaping its default behavior for more controlled outputs. It's worth noting that some in the open source community are experimenting with reducing or removing these layers in order to explore the raw model's capabilities.

Speaker: In the broader landscape of open source AI, GPT-OSS arrives as a fully equipped long-context model ready for immediate use. As impressive as it is, however, it's just one of several models in a rapidly expanding field of open source LLMs.

Speaker: Qwen 3, the newest family of models developed by Alibaba Cloud, dropped this past April to considerable hype with benchmark scores that rivaled those of leading open source models like DeepSeek V3 or Llama 4.

Speaker: The Qwen 3 family includes both dense models, which activate all of their parameters for each query, and mixture of experts models, which only activate a small subset of their parameters for each query. The dense models come in seven different size classes, including a 6 billion parameter model, one of the smallest current-generation open-weight models around, while the mixture of experts models come in two different size classes.

Speaker: Architecturally, Qwen 3 dense models are very similar to the Qwen 2.5 models, Alibaba's previous releases. Like Qwen 2.5 and GPT-OSS, Qwen 3 incorporates features like grouped query attention, SwiGLU, RoPE, and RMS norm.

Speaker: Qwen 3's sparse models share the same fundamental architecture as its dense models but add a mixture of experts layer with 128 total experts, of which eight are activated per token.

Speaker: All Qwen 3 models also use the same tokenizer used in previous Qwen models, which implements byte-level byte-pair encoding that allows it to handle any text or symbol without special pre-processing, unlike word or character-based tokenizers.

Speaker: One of the main things that sets Qwen 3 apart from previous Qwen models is the way it controls the scale of the key, query, and value projections to keep attention scores stable at scale. It replaces QKV bias, a static offset that shifts KQV projections in previous models, with QK norm, a normalization step that dynamically rescales the query and key vectors to maintain constant magnitudes.

Speaker: Data-set-wise, Qwen 3 was trained on 36 trillion pre-training tokens, twice as many as the Qwen 2.5 models. In addition to pulling data from multilingual texts, STEM and coding sources, and reasoning tasks, Qwen 3 also uses Qwen 2.5 models to generate trillions of tokens of synthetic data in different formats like textbooks, instructions, and code snippets.

Speaker: Qwen 3's pre-training occurred in three stages. In stage one, the general stage, models were trained on over 30 trillion tokens covering 119 languages at a sequence length of 4,096 tokens. In stage two, the reasoning stage, models were trained on an additional 5 trillion higher-quality tokens featuring more STEM reasoning and coding problems. And in stage three, which the Qwen team calls the long-context stage, context length was extended to over 32,000 tokens using a bunch of clever algorithmic optimizations, including ALiBi, a technique to adjust RoPE so positional signals remain accurate over much longer sequences, YaRN to further scale for longer inputs, and dual-chunk attention to process sequences efficiently. Together, all of these optimizations allow the model to reason over much longer inputs at inference.

Speaker: Finally, Qwen uses a four-step post-training pipeline with two goals: giving users more control over how much reasoning to use for a given query and letting them efficiently distill larger model capabilities into smaller models.

Speaker: The first step in the post-training pipeline is a long chain-of-thought cold-start stage, which involves feeding a model a curated dataset of challenging reasoning problems from math, logic, and STEM with verifiable reference answers and then filtering outputs to ensure quality. This is followed by a reasoning RL stage using GRPO, an RL algorithm originally developed by DeepSeek researchers, on roughly 4,000 query-verifier pairs to strengthen complex problem-solving.

Speaker: Personally, I think it's fascinating that it only takes 4,000 pairs to get great results.

Speaker: The third step in the post-training pipeline, thinking-mode fusion, is a key Qwen 3 innovation that integrates reasoning and non-reasoning into a single model, letting users switch modes without changing models. Essentially, what developers did in this step was fine-tune the model on a mix of thinking data, which includes intermediate reasoning steps, and non-thinking data, which omits them, and then build a chat interface to let users toggle modes. Though this was unique to Qwen when the model first launched, GPT-4o now features a similar toggle.

Speaker: The final step, general RL, broadens capabilities in instruction following, formatting, preference alignment, tool use, and specialized scenarios.

Speaker: Qwen's developers then use strong-to-weak distillation, which allows for the training of smaller models from larger ones.

Speaker: All in all, Qwen 3's performance is very impressive, especially given its relatively small size. But just months earlier, a different model had already raised the stakes in open source.

Speaker: Released in December of last year, DeepSeek's V3 model was one of the most ambitious open source LLMs to come out of a major lab in recent years.

Speaker: The chatbot developed in China called DeepSeek.

Speaker: DeepSeek is such a fundamental change to the economics of what's going on.

Speaker: The most downloaded free app in the US. This is an update in what people think is possible.

Speaker: At 671 billion parameters, it's a massive general-purpose-based model designed for efficiency as much as capability, laying the groundwork for the reasoning-focused R1 model that would follow.

Speaker: We're not going to get into a ton of detail about V3's architecture or training pipeline here because we put out a comprehensive deep dive into it back in February. But high-level, the thing to know about V3 is that it's a mixture of experts model with several hardware and algorithmic optimizations, including training V3 natively in 8-bit rather than 16 or 32-bit—a huge unlock for cutting training costs.

Speaker: And just recently, DeepSeek pushed V3 even further with an updated version. The newly released V3.1 builds directly on the original V3-based checkpoint, extending it with a two-phase long-context training approach and adding a hybrid thinking mode that lets the same model switch between reasoning-heavy and lightweight inference. It also improves tool use and agent performance thanks to more advanced post-training.

Speaker: In practice, this means V3.1 keeps the same core architecture as V3 but delivers stronger reasoning, smarter tool use, and greater performance.

Speaker: One thing that sets V3 apart is that it uses a different attention mechanism than GPT-OSS and Qwen 3. In modern LLMs, a lot of the compute and memory is tied up in the KV cache, and so V3 makes use of MLA, which compresses keys and values into a smaller latent space before caching them, then decompresses them during inference. Although MLA is a bit more complex to implement, the previous DeepSeek V2 paper found it delivers greater memory savings and better modeling performance than GQA, especially in huge long-context models like this one.

Speaker: And that's just one of several areas where DeepSeek V3 takes a different path.

Speaker: With all that in mind, let's take a step back from V3 to Qwen to GPT-OSS. How should we think about, at a high level, the differences between these models?

Speaker: One big difference is size. The Qwen 3 model family is the only one of the three to offer both dense and mixture of experts variants, with dense models from 6 billion to 32 billion parameters and a mixture of experts lineup that includes a 30 billion parameter model and a 235 billion parameter model. Notably, Qwen's mixture of experts base models matched the dense models' performance with only a fifth as many active parameters.

Speaker: On the other hand, DeepSeek V3 only comes in a mixture of experts architecture with 671 billion parameters, of which 37 billion are activated for a given token prediction. So considerably larger than even the biggest Qwen 3 model.

Speaker: GPT-OSS sits in the middle. It offers two models: one with 117 billion parameters, of which 5.1 billion are activated for a given token, and a smaller one with 21 billion parameters, of which 3.6 billion are activated for a given token.

Speaker: One of the most interesting technical differences lies in how each model extends its context length. YaRN, short for "Yet Another RoPE eXtension," is a technique for stretching the model's rotary positional embeddings so that it can handle far longer sequences than it was originally trained on. Normally, RoPE starts to break down when you feed it more tokens than its base frequency was set for. But YaRN tweaks that frequency so the same embedding space covers much more ground.

Speaker: What's interesting is how the three models here use it differently. GPT-OSS applies YaRN right from pre-training, so its weights have learned to work natively with 131,000 token contexts. DeepSeek takes a staged approach, fine-tuning after pre-training to first reach 32,000 tokens, then further training to achieve 128,000. Qwen also fine-tunes to 32,000 but skips that additional retraining step. Instead, at inference time, they apply YaRN scaling again, increasing the RoPE base frequency by a factor of four to reach 128,000 tokens without extra retraining.

Speaker: In other words, GPT-OSS is born with long-context ability. DeepSeek is trained into it step by step, and Qwen pushes the limits of what a 32,000-trained model can do without more long-context training.

Speaker: Personally, I think one of the most interesting things about these papers and the state-of-the-art in deep learning more generally is that a lot of these read as empirical findings. Each lab describes the combination of tools that works well for them, but almost no one gives a first-principles justification of why one tool is better than the other. For instance, why MLA is better than GQA, full stop. This is much different from domains like math or theoretical physics, which are all about providing first-principles explanations that derive results from axioms or laws.

Speaker: Also, it's interesting that even though most of these models have similar top-line benchmark statistics and use broadly the same tools like attention mechanisms, activation functions, positional embeddings, and so on, they achieve these similar results using often very different techniques. This is quite surprising. You'd expect that very different training methods would lead to very different results.

Speaker: Also, all of the major models heavily use reinforcement learning as part of the post-training and reasoning portions of their model training efforts. And it's fascinating and pretty surprising how some of these RL efforts require very little amounts of data—just 4,000 data pairs in the case of Qwen.

Speaker: Another point here is that it's very opaque what the differences in datasets are between the labs. It's clear from the papers that there's an enormous amount of work happening behind the scenes in dataset engineering. This work is probably a significant aspect of the moat that makes these companies comfortable releasing their models. It's very difficult to replicate what they're releasing.

Speaker: So the big takeaway when reading these papers is you shouldn't focus too much on just the benchmark performance or top-line stats like context size. Instead, look at the specific methods that these labs are using to achieve those results. There are tons of high-performing open source models that we didn't discuss in this video, like Claude K2 or Google Gemma 3. But when you peek under the hood of many of these, you'll find nuanced differences that I find really interesting.

Speaker: I hope this gives you a framework for how to understand the latest open source releases and gives you a toolkit to start tinkering with them yourself. Thanks for watching. See you in the next episode.
