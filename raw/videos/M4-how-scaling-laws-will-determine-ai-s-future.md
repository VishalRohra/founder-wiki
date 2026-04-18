---
title: "How Scaling Laws Will Determine AI's Future"
slug: "M4-how-scaling-laws-will-determine-ai-s-future"
media_type: "Video"
author: "Garry Tan"
speakers: ["Host"]
categories: []
description: "In this episode of YC Decoded, President and CEO Garry Tan looks into both sides of the scaling laws debate and how a brand-new paradigm could potentially forecast the future of AI."
url: "https://ycombinator.com/library/M4-how-scaling-laws-will-determine-ai-s-future"
youtube_id: "d6Ed5bZAtrM"
youtube_url: "https://www.youtube.com/watch?v=d6Ed5bZAtrM"
transcript_source: "yc_page"
multi_speaker: false
speaker_labels: true
---

# How Scaling Laws Will Determine AI's Future

In the past few years, AI labs have adopted a “more is more” approach to scaling LLMs. By introducing more parameters,
data and compute, they’ve been able to predictably improve model performance.

But recently, there’s been plenty of debate within the AI community as to whether or not we may have finally reached the
limits of scaling laws.

In this episode of YC Decoded, President and CEO Garry Tan looks into both sides of the scaling laws debate and how a
brand-new paradigm could potentially forecast the future of AI.

## Transcript

Host: The deadline to apply for the first YC spring batch is February 11th. If you're accepted, you'll receive $500,000 in investment plus access to the best startup community in the world. So apply now and come build the future with us.

Host: Large language models are getting bigger, much bigger. They're also getting smarter. Over the past few years, AI labs have hit on what feels like a winning strategy: scaling more parameters, more data, more compute. Keep scaling the models and they keep improving. You know, just like Moore's Law, we saw the doubling in performance every 18 months. With AI, we've now started to see that doubling every six months or so. But could that be coming to an end? Is the era of scaling finally over? Or are we standing right at the beginning of a brand new scaling paradigm—one that promises to revolutionize AI forever?

Host: In November of 2019, OpenAI released GPT-2, its largest ever model with one and a half billion parameters. The next summer, they released its successor, GPT-3, which was something we'd never seen before. Not only was GPT-3 far more useful and usable, it was also much bigger—over 100 times bigger than GPT-2. The era of scaling laws had arrived.

Host: Before GPT-3, LLMs were already getting bigger, but it was still anyone's guess whether or not that extra size, data, and compute would be worth it. There was no guarantee that making your model 100 times bigger would also make it 100 times better. What if they started to run into diminishing returns?

Host: It wasn't until January of 2020, when Jared Kaplan, Sam McCandlish, and their colleagues at OpenAI released the influential "Scaling Laws for Neural Language Models" paper, that the field started to take notice.

Host: Think of training AI models like a recipe. You have three main ingredients: the model itself, the data it's trained on, and the compute power used to train it. Larger models have more parameters—these are the internal values of the neural net that are tweaked and trained in order to make predictions. These models are also typically trained on much more data, measured in tokens, which for LLMs are often words or parts of words. Finally, training these larger models requires computing power, which means more GPUs running for longer, using more and more energy.

Host: What the scaling laws paper revealed was that by cranking up all three—the parameters, the data, and the compute—the result was a smooth, consistent improvement in model performance in the form of a power law. Performance, it turned out, depends much more on scale than on the algorithm.

Host: Later in the year, more research from OpenAI confirmed that these scaling laws worked for other kinds of models too: on text-to-image, image-to-text, and even math. The same scaling laws were there.

Host: But back in early 2020, LLM scaling laws were pretty much unknown outside of OpenAI. That is, except for one person: the anonymous researcher and writer, Gwern. Gwern was one of the first people to hone in on what he called the scaling hypothesis. Scale up the size, the data, and the compute, and watch intelligence emerge.

Host: Maybe intelligence really is just a lot of compute applied to a lot of data applied to a lot of parameters. Um, maybe Moravec and Legg and Kurzweil were right.

Host: Gwern's post brought scaling laws into the mainstream, and over time, what started as a quiet observation quickly turned into a foundational principle for AI development.

Host: But OpenAI research was just a part of the picture. In 2022, Google DeepMind released their own research on scaling laws, and they added an important missing piece. It turned out that it's not just about making models bigger. It's also about making sure you train them on enough data.

Host: Researchers were looking to find the most optimal model size and training data for a given compute budget. So they trained over 400 models of different sizes with different amounts of data. And what they found was surprising.

Host: Their research suggested that previous LLMs, like GPT-3, were actually undertrained. These models were huge, but they hadn't been trained on enough text to fully realize their potential.

Host: To test this, they trained Chinchilla, an LLM less than half the size of GPT-3, but with four times more data. And boy, Chinchilla was far better than models double, even triple its size.

Host: These so-called Chinchilla scaling laws meant that training the optimal model wasn't just about making the model larger, but also about having enough data to feed it. Chinchilla was a huge milestone on the road to training the frontier AI models we have today, like GPT-4, Claude 3.5 Sonnet, and others.

Host: Labs learned they could trust in the scaling laws and get reliably better and better models. So the future of AI is just bigger and bigger models forever, right?

Host: Well, recently there's been plenty of debate within the AI community about whether or not we've finally reached the limits of scaling laws. Some argued that as the latest generation of models have gotten bigger and more expensive, capabilities have started to plateau.

Host: There's a lot of debate. In fact, just in the last multiple weeks: have we hit the wall with scaling laws? The current generation of LLM models are roughly, you know, few companies have converged at the top, but I think we're all working on our next versions too. We're increasing GPUs at the same rate, um, but we're not getting the intelligence improvements at all.

Host: Meanwhile, rumors have leaked out of major labs about failed training runs and diminishing returns. Others have speculated that the lack of high-quality data to train new models has also become a major bottleneck.

Host: Uh, one practical issue we could have is we could run out of data for various reasons. I think that's not going to happen, but uh, you know, uh, if you look at it very, very naively, we're not that far from right now data-wise. And so it's like we just don't have the data to continue the scaling curves.

Host: So if the old scaling laws are beginning to lose their edge, what comes next? What if there's a new frontier for scaling from a brand new kind of model?

Host: OpenAI's new class of reasoning models hints at a potential new direction. In a previous video, we explained how O1 learns to think through complex problems using its own chain of thought. And OpenAI researchers found that the longer O1 was able to think, the better it performed.

Host: It wasn't immediately clear how well this strategy would continue to scale up, but now with the recent release of its successor, O3, the sky seems to be the limit for this new paradigm of scaling LLMs.

Host: O3 made headlines when it was announced, as it smashed benchmarks that were previously considered far out of reach for AI. From software engineering to math to PhD-level science questions, O3 easily surpasses the old state-of-the-art results.

Host: O3 isn't just a small improvement on its predecessors. It's a huge leap. And OpenAI researchers say they have every reason to believe this trajectory will continue. It may even be on a path to artificial general intelligence.

Host: Instead of continuing to scale up the model size during training, it seems likely that researchers will shift focus to scaling the amount of compute available to the model for its chain of thought, also called test-time compute. By letting models think for longer, LLMs like O1 and O3 can leverage more compute on the fly, scaling up their intelligence when it's needed for harder and harder problems.

Host: Scaling pre-training may have plateaued, but by training test-time compute, OpenAI may have just opened up an entirely new paradigm for scaling laws, potentially unlocking capabilities we never thought possible.

Host: Large language models are a key piece of the hunt for artificial general intelligence. These same principles of scaling appear to hold for other models too: image diffusion models, protein folding, and chemical models, even world models for robotics like self-driving.

Host: One thing is clear: it might be midgame for large language models, but we are clearly still in the early game for scaling other modalities. Buckle up.
