---
title: "Why OpenAI's o1 Is A Huge Deal"
slug: "Ll-why-openai-s-o1-is-a-huge-deal"
media_type: "Video"
author: "Garry Tan"
speakers: ["Host"]
categories: []
description: "OpenAI’s newest model, o1, makes huge leaps forward in domains like mathematics and coding and scores big on many of the toughest benchmarks. The secret to its success? It represents an entirely new class of models designed to reason or “think through” complex problems.

For the very first episode of YC Decoded, we took a look inside."
url: "https://ycombinator.com/library/Ll-why-openai-s-o1-is-a-huge-deal"
youtube_id: "Lv9bKyQgoHo"
youtube_url: "https://www.youtube.com/watch?v=Lv9bKyQgoHo"
transcript_source: "yc_page"
multi_speaker: false
speaker_labels: true
---

# Why OpenAI's o1 Is A Huge Deal

OpenAI’s newest model, o1, makes huge leaps forward in domains like mathematics and coding and scores big on many of the
toughest benchmarks. The secret to its success? It represents an entirely new class of models designed to reason or
“think through” complex problems.

For the very first episode of YC Decoded, we took a look inside.

## Transcript

Host: OpenAI's newest model is finally here. It's called O1, and it's much better for questions around mathematics and coding and scores big on many of the toughest benchmarks out there. So what's the secret to why it works? Let's take a look inside.

Host: OpenAI recently released two brand new models: O1 Preview and O1 Mini. These are the models that Sam Altman has been hinting at for months, the ones previously codenamed Q-Star and Strawberry. Together, they represent an entirely new class of models that are designed to reason or think through complex problems.

Host: O1 really is the first system that can do pretty advanced reasoning. You know, if you give it a difficult programming challenge or a difficult math problem, difficult science thing you need help with, you can really get pretty extraordinary results. It performs similarly to PhD students on challenging benchmark tasks in areas like physics, chemistry, and biology, and excels in math and coding.

Host: It's worth noting that when compared to GPT-4.0, users don't always prefer O1 for more informal, subjective tasks like creative writing or editing text. This is likely a result of the very unique way in which OpenAI trained O1.

Host: It's fair to say that O1 Preview and O1 Mini amount to an entirely new kind of LLM. If O1 is reasoning, the question is: how similar is it to how humans work through a complex problem?

Host: It makes use of a chain of thought process to break down the question into smaller steps. Many of us have already used such a strategy when prompting earlier models like GPT-4.0, telling it "think step by step" or "take a breath and go line by line." It'll work through the step, recognize its own mistakes, try to correct it, try different strategies, and fine-tune its approach as needed. In other words, it's not just spitting out answers. It's working through problems in a way that mirrors human reasoning.

Host: Now, people were already doing this. Since we already had a term for it: chain of thoughts, which came out in 2022 by Google Brain researchers. Here's an example of chain of thoughts direct from the paper: John has one pizza cut into eight equal slices. John eats three slices and his friend eats two slices. How many slices are left?

Host: Chain of thoughts will break this down. First, you'd ask it to identify the total number of slices. The pizza is cut into eight equal slices. Then, calculate the number of slices eaten by John and his friend. John eats three slices and his friend eats two slices. Finally, subtract the total number of slices eaten from the original number of slices to find out how many are left. That's three slices.

Host: Without chain of thoughts breaking it down into steps, LLMs would just try to predict the most likely token, and in any given request, there often would be just not enough context.

Host: If lots of people were already using manual chain of thoughts, how exactly did OpenAI approach this? They haven't said much, but here's a good guess. Their AI researchers have said no amount of prompt engineering on GPT-4.0 could get it to rival the abilities of O1. Instead, the new model was trained in an entirely novel fashion via reinforcement learning.

Host: This is a type of ML that allows a model to learn by trial and error from its own actions, often using rewards and punishments as signals for positive and negative behavior. Instead of only training on human-written chains of thought, OpenAI trained O1 further with large-scale reinforcement learning. This means they allowed it to generate its own synthetic chains of thought that emulate human reasoning.

Host: These chains of thought are judged by the reward model and then used to train and fine-tune it more and more over time. OpenAI has found O1 consistently improves with more reinforcement learning and with more time spent thinking.

Host: What this means is not only can the base model continue to improve with further training, but that in production, when you the user ask O1 a complex problem, the longer it is allowed to think, the more compute OpenAI is able to use to do so, and the more accurate its response is going to be.

Host: Does this mean that O1 will only keep improving? Well, yes. We know the unreleased versions of O1 are still evolving. O1 Preview has been described as an early version of the fully baked model, which can hopefully expect to be released in the coming weeks or months.

Host: A few wise startups have already received early access, and the results for them have been nothing short of staggering. In fact, recently published research proved that by using chain of thought, an LLM can essentially solve any inherently serial problem. This means the sky truly is the limit for this series of models.

Host: With enough compute resources, according to Sam Altman, we can definitely expect rapid improvement in these models over time. Given these inference time scaling laws, Sam compared the current O1 models to being at the GPT-2 stage, hinting that we likely see a leap to the GPT-4 stage within a few years.

Host: So is O1 actually reasoning? Without getting too philosophical, we think it is fair to say yes, it is. O1 tackles complex problems that require planning by generating its own sequence of intermediate steps, working through them, and often, but not always, arriving at a correct answer.

Host: Perhaps it is more accurate to say that O1 marks a shift from models that memorize the answers to ones that memorize the reasoning. Of course, O1 still needs work. It hallucinates occasionally, forgets details, and struggles with problems that fall out of distribution. Like all models, its results can be improved a bit with better prompt engineering, especially prompts that outline edge cases or guide its reasoning style.

Host: So what's next? According to OpenAI's own researchers, the company has some exciting updates planned, including support for additional tools such as code interpreter and browsing, longer context windows, and eventually even multimodality.

Host: The only real question that remains is: what will you build with O1?
