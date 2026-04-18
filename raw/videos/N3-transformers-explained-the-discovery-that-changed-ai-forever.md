---
title: "Transformers Explained: The Discovery That Changed AI Forever"
slug: "N3-transformers-explained-the-discovery-that-changed-ai-forever"
media_type: "Video"
author: "Ankit Gupta"
speakers: ["Speaker"]
categories: []
description: "YC's Ankit Gupta traces how AI learned to understand language — from early RNNs and LSTMs to attention mechanisms and the breakthrough 2017 paper Attention Is All You Need — the discovery that unlocked the modern AI era."
url: "https://ycombinator.com/library/N3-transformers-explained-the-discovery-that-changed-ai-forever"
youtube_id: "JZLZQVmfGn8"
youtube_url: "https://www.youtube.com/watch?v=JZLZQVmfGn8"
transcript_source: "yc_page"
multi_speaker: false
speaker_labels: true
---

# Transformers Explained: The Discovery That Changed AI Forever

Nearly every modern AI model, from ChatGPT and Claude to Gemini and Grok, is built on the same foundation: the
Transformer.

In this video, YC's Ankit Gupta traces how AI learned to understand language — from early RNNs and LSTMs to attention
mechanisms and the breakthrough 2017 paper Attention Is All You Need — the discovery that unlocked the modern AI era.

## Transcript

Speaker: Nearly every state-of-the-art AI system, whether it's ChatGPT, Claude, Gemini, or Grok, is built on the same underlying model architecture, the transformer. But where did the transformer architecture come from? And what can its development teach us about the way breakthroughs in AI happen? Let's dive in.

Speaker: A transformer is a neural network that uses self-attention to take input data like text or images, model the relationships between that data, and finally generate outputs like meaningful text responses, translations, or classifications. Many people know that the original transformer architecture was introduced in a now famous 2017 paper from Google called "Attention Is All You Need." But what you might not know about are the breakthroughs that made this overnight success possible. There are three key developments that we'll discuss today: long short-term memory, sequence-to-sequence with attention, and then finally transformers.

Speaker: Let's start with long short-term memory networks, or LSTMs. One of the core challenges motivating early AI research was to get neural networks to understand sequences. Natural language is inherently sequential. The meaning of a word depends on what comes before it or after it. And understanding an entire sentence requires maintaining context across many words. Early architectures like feed-forward neural networks process each input in isolation, and so they weren't capable of understanding context, or they required looking at inputs of a fixed length.

Speaker: So researchers developed recurrent neural networks, or RNNs, as a solution to this. In simple terms, an RNN iterates over the inputs in order, one at a time, and consumes the previous outputs as additional input at each step. So if an input is of length n, there are n feed-forward pass steps. And as a result, during the backwards pass, the gradient with respect to the early inputs is the result of n matrix multiplications.

Speaker: Now in practice, this meant that we often faced a problem called vanishing gradients. The early inputs in a sequence had less and less influence on the network's output as the sequence grew longer because it went through these multiple matrix multiplications. Gradients, which are the signals used to adjust weights during training, would fade to near zero as they were passed backwards through time.

Speaker: In the 1990s, Hochreiter and Schmidhuber proposed a solution to this. It was called the long short-term memory network, or LSTM. LSTMs were a type of RNN that attempted to fix the vanishing gradient problem by introducing gates, which could learn what information to keep, update, or forget. This made it possible to learn long-range dependencies, something vanilla RNNs struggled with.

Speaker: But LSTMs were too expensive to train at scale in the '90s, and so progress stalled. Now you fast forward to the early 2010s, and GPU acceleration, better optimization techniques, and new large-scale datasets brought LSTMs back into the spotlight. Suddenly, this relatively old architecture was viable again, and it began to dominate natural language processing. LSTMs were quickly adopted for everything from speech recognition to language modeling.

Speaker: In these years, NLP and computer vision were actually somewhat separate worlds. RNNs and LSTMs in particular were preeminent in language tasks, while convolutional neural networks, or CNNs, were winning in vision. But the basic question motivating both NLP and computer vision was the same: how do you model sequences? How do you let those models capture structure that spans time or space?

Speaker: LSTMs were a huge step forward, but they still had limitations. The most fundamental was something called the fixed-length bottleneck. Here's how most early LSTM systems worked. For sequence-to-sequence tasks like translation, you would take the input sentence, feed it into an encoder LSTM, and boil the input down to a single fixed-size vector. Then a decoder LSTM would take that vector and try to construct the target sentence word by word. This yielded impressive results on the benchmarks of that era.

Speaker: But in practice, that single vector was still unable to accurately capture the meaning of long or complex sentences. Also, there wasn't a great way to encode the concept of order into a fixed-size vector. This was very important in translation tasks. For example, in English, we put adjectives before nouns, and in Spanish, we often place adjectives after nouns. You'd see this in performance. These models worked okay on short inputs, but they quickly fell apart as sequences got longer.

Speaker: And truthfully, this was more than a performance issue. It pointed to a deeper architectural problem. Allowing the decoder to only see one static summary of the input was a fundamental limitation. Why not give it access to all of the intermediate information that the encoder saw? This sort of insight is what gave rise to the next big leap.

Speaker: In 2014, a paper introduced what would become the new standard for sequence translation: sequence-to-sequence, or seq2seq models with attention. Like before, the core idea was to train two neural networks jointly—an encoder which reads the input sequence and builds a representation of it, and a decoder which generates the output sequence one step at a time. Both models were LSTMs, and crucially, they were trained together end-to-end.

Speaker: But there was a key insight that enabled this performance jump: attention. Even though seq2seq used a fixed-length vector, researchers realized that if you could let the decoder look back or attend to the encoder's hidden states, you could let the model learn how to align parts of the input to parts of the output. Bahdanau, Cho, and Bengio showed that these models could significantly outperform traditional rule-based systems and the existing seq2seq models on tasks like machine translation. That was a big deal.

Speaker: These models were evaluated on translation benchmarks and showed near state-of-the-art performance, beating even the best statistical systems at the time. It was a sign that neural models could compete head-to-head with the mature, production-grade systems of old. And for many people, this was the first moment they began to see these models in practice. This was real, usable NLP. For example, Google Translate adopted a neural seq2seq architecture around this time. And you may remember this as the era in which Google Translate started to finally work well.

Speaker: This insight—learning to align and translate at the same time—was transformative. And it wouldn't just stay in NLP. One of the original seq2seq authors, Yoshua Bengio, soon applied similar alignment-based architectures to computer vision. This was the first sign that these sequence models might be useful beyond language.

Speaker: But even when augmented with attention, RNNs were still constrained by their sequential architecture. Processing tokens one at a time made it challenging to run computations in parallel across time steps. So runtime scaled linearly with sequence length. This made training models on large datasets—the kinds we knew would be necessary to achieve broadly useful AI—intractably slow.

Speaker: In an attempt to speed up RNNs, researchers developed techniques like factorizing LSTM matrices into smaller matrix products or conditionally activating only parts of a network that were relevant to a query. But the fundamental linear runtime constraint remained.

Speaker: Then came the big breakthrough in 2017 when a team of researchers at Google published a paper called "Attention Is All You Need," which proposed a new machine translation architecture that they called a transformer. Transformers scrapped recurrence entirely, instead relying solely on an attention mechanism to generate outputs.

Speaker: We won't get fully into the technical weeds of transformers here. For that, check out Andrej Karpathy's fantastic explainer. But at a high level, transformers use a modified version of the encoder-decoder architecture originally proposed in seq2seq. Instead of compressing inputs into a single vector embedding, transformers kept separate embeddings for each input token and updated these through self-attention—a mechanism that updated token representations based on a learned weighted dot-product over the embeddings of all other tokens in the sequence.

Speaker: Because each token in this architecture could attend to all others simultaneously, transformers could process an entire sequence in parallel, making them dramatically faster than RNNs. Remarkably, they were also much more accurate on machine translation benchmarks.

Speaker: Over the next few years, researchers started to experiment with different variations of the transformer architecture. The architecture described in the original Google paper featured an encoder and decoder that each had self-attention and cross-attention between the two. This resembled the original seq2seq architectures but without the recurrence.

Speaker: The next several years saw a lot of innovation in the transformer architecture itself. For example, a series of models called BERT focused on using only the encoder to do masked language modeling. In parallel, efforts to use only the decoder for autoregressive modeling gave rise to OpenAI's GPT series of models. At a high level, we can describe both of these model series as subsets of the original "Attention Is All You Need" transformer model.

Speaker: It quickly became clear that these models could scale to large numbers of parameters. Ultimately, one model type, the generative pre-trained transformer model, or GPT, would be scaled up to create the LLM that we regularly use today in products like ChatGPT or Claude.

Speaker: But not that long ago, it wasn't obvious that there might be one model to rule them all. In fact, people were training variants of model architectures for every task—one for machine translation, another for named entity recognition, and so on. Each with a shared backbone, but slight differences in the final model layers. These models were intelligent in that their accuracy was high, but they were largely single-task models.

Speaker: Also, at this point, there wasn't really a concept of prompting the models because there was no chat interface. Instead, people interacted with the models through domain-specific inputs. It was only as the lab started to experiment with training autoregressive models on much larger datasets that they began to look and feel more like generally intelligent systems.

Speaker: Hopefully, this history helped contextualize some of what it took to get these models to a place of being able to scale them. In the next video, we'll talk about some of the architectural and engineering innovations it took to actually get them to their current performance levels. Thanks for watching.
