---
title: "Anthropic’s Claude Computer Use Is A Game Changer"
slug: "Lw-anthropic-s-claude-computer-use-is-a-game-changer"
media_type: "Video"
author: "Garry Tan"
speakers: ["Host", "Speaker"]
categories: []
description: "The age of AI agents is here. Models can read, see, talk, and now, even use a computer all by themselves.

YC President and CEO Garry Tan dives into how Claude Computer Use works, what it can do, and how it may change AI forever."
url: "https://ycombinator.com/library/Lw-anthropic-s-claude-computer-use-is-a-game-changer"
youtube_id: "VDmU0jjklBo"
youtube_url: "https://www.youtube.com/watch?v=VDmU0jjklBo"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Anthropic’s Claude Computer Use Is A Game Changer

The age of AI agents is here. Models can read, see, talk, and now, even use a computer all by themselves. One of the
first out of the gates is Anthropic’s Claude Computer Use. In this episode of YC Decoded, President and CEO Garry Tan
dives into how Claude Computer Use works, what it can do, and how it may change AI forever.

## Transcript

Host: The robots can talk, but they can also read. They can see, and now they can use a computer. Browsing the web, clicking buttons, typing text, all by itself. The age of AI agents is here. One of the first out of the gate is Claude Computer Use, Anthropic's brand new AI agent. Let's dive into how it works, what it can do, and how it may change AI forever.

Host: In October, Anthropic made waves when it released a set of upgraded models, Claude 3.5 Haiku and a new 3.5 Sonic. They also released something special: Computer Use. But they're not the only ones in the space. We already know Sam Altman is working to recreate Samantha from the movie Her, and OpenAI is said to be releasing its own agent, Operator, in the new year. Google is working on something similar too. The landscape for AI agents is growing fast, and so far, Anthropic is the first of the big AI labs to get into the game.

Host: Right now, Claude Computer Use is still in public beta as developers put it to the test, but already it's looking like a complete game changer.

Host: So how does it work? Claude had the ability to understand images for a while, so the next step was to train it on how and when to perform specific actions like clicking buttons or writing text based on what's displayed on the screen.

Speaker: Claude has had, for a long time, since Claude 3 back in March, the ability to analyze images and respond to them with text. The only new thing we added is those images can be screenshots of a computer, and in response, we trained the model to give a location on the screen where you can click and/or buttons on the keyboard you can press in order to take action. And it turns out that with actually not all that much additional training, the models can get quite good at that task. It's a good example of generalization.

Host: For this, Anthropic needed to train Claude to recognize exact locations on the screen down to the pixel. Anthropic was then able to train Claude to understand what's happening on screen and to reason about how it should use its software tools to do tasks.

Host: For example, it might help you automate boring and repetitive tasks. Claude's going to start taking screenshots of my screen and quickly realizes that the ant equipment company isn't actually in the spreadsheet. Luckily, we get a search match, and Claude then starts scrolling through the page, looking for all the information it needs to fill out this form.

Host: To get started with Computer Use, developers have to run it in a virtual machine or container like Docker. You'll also need an Anthropic API key. Once that's all set, you can then open a dedicated browser window which shows the user prompt on the left and Claude's activity on the right.

Host: Claude starts by analyzing the prompt and deciding which tool to use. As it works, it takes a screenshot at each step to check its progress, making sure the task is on track. If adjustments are needed, Claude loops back to try different actions or tools until it completes the task. This repeatable loop of deciding, evaluating, and acting is called the Agent Loop, and it's how Claude handles complicated step-by-step tasks all on its own.

Host: So what else can Computer Use make possible? In their own demos, Anthropic shows us a few different tasks. Like this one, of Claude helping to plan a sunrise hike at the Golden Gate Bridge. It searches the web, figures out some important details, and then creates an event in Google Calendar.

Host: In another example, Wharton Professor Ethan Mollick puts Claude Computer Use to the test by feeding it a video of a construction site and prompting Claude to monitor the site and look for issues with safety. You'll see Claude takes screenshot after screenshot, analyzing different parts of the site, making note of all the gear and materials, and trying to spot any potential issues. It even finishes up by putting everything together in a nice, neat spreadsheet. Automated OSHA compliance check.

Host: By now, it should be clear that Computer Use is a step forward for AI. Up until now, developers have had to make tools to fit the model, coming up with custom environments where AIs use specially designed tools to do different, various tasks. Now we can make the model fit the tools. That's a powerful change.

Host: Computer Use opens up so many applications. Businesses can automate repetitive tasks and increase efficiency, while the average user can save time on routine things like booking flights or ordering food. It's easy to see a future where AI agents handle most of the drudge work for us. And for developers, Computer Use massively lowers the barriers to entry. LLMs have already made tasks like coding way more accessible to the average person, and Computer Use takes that a whole step further.

Host: Computer Use is still a work in progress, so it has some bugs and limitations. It's much slower than typical models and has a tendency to crash from time to time, so reliability is still an early concern. Occasionally, Claude will misstep in its tool selection, get confused, or even sometimes veer off task.

Host: During one session that Anthropic shared on YouTube, Claude unexplainably started searching for pictures of Yellowstone National Park out of nowhere in the middle of its task. To be fair, humans get distracted and sometimes do that too.

Host: Claude does have guardrails since it could easily be used for abuse. It steers clear of things like account creation or content generation for social media. It's also vulnerable to prompt injection, a security risk where the model can be tricked to follow different information or prompts embedded in the online sources it visits, rather than sticking to the original prompt.

Host: Imagine a website prompt injecting Claude to upload the contents of your password manager. That'd be bad. Anthropic thought about and tries to keep users safe by keeping actions contained to a secure virtual machine, limiting access to sensitive data, and strictly controlling approved sites. However, many of these limitations could be lifted soon because this beta is just the beginning.

Host: Anthropic's already said that Computer Use will rapidly improve to become faster, more reliable, and more useful for the tasks users want to complete. Plenty of startups are getting into the mix too. Just recently, a YC company Kura released their own browser agents that seem to outperform Claude Computer Use on the web Voyager benchmark, achieving a new state-of-the-art.

Host: In the near future, LLMs with the full ability to use and control computers will reshape everything: how developers write software, how CEOs run their companies, and even how we all live our daily lives. Each new groundbreaking application will transform how we work, connect, and live.

Host: This kind of AI won't just be an assistant. It'll take on entire tasks that once needed whole teams or companies.

Host: So what will you build with Computer Use?
