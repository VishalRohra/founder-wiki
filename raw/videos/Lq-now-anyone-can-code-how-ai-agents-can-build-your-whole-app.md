---
title: "Now Anyone Can Code: How AI Agents Can Build Your Whole App"
slug: "Lq-now-anyone-can-code-how-ai-agents-can-build-your-whole-app"
media_type: "Video"
author: "Y Combinator"
speakers: ["Amjad", "Audience Member", "Diana Hu", "Gary Tan", "Host", "Jared Friedman", "Speaker"]
categories: []
description: "We speak with Amjad Masad, the CEO of Replit, an AI-powered software development and deployment platform, to see how coding power can be given to everyday users."
url: "https://ycombinator.com/library/Lq-now-anyone-can-code-how-ai-agents-can-build-your-whole-app"
youtube_id: "jbIQfoldLag"
youtube_url: "https://www.youtube.com/watch?v=jbIQfoldLag"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Now Anyone Can Code: How AI Agents Can Build Your Whole App

Thanks to rapid development in LLM’s, we are now at the point where AI is able to follow prompts and generate code to
build functional custom software. So how does the tech landscape change when the ability to code is democratized? In
this episode of the Lightcone, the hosts speak with Amjad Masad, the CEO of Replit, an AI-powered software development
and deployment platform, to see how coding power can be given to everyday users.

## Transcript

Gary Tan: 1984 the Mac brought personal computing to the masses. 2024 we have personal software. You actually are going to be able to orchestrate this giant army of agents. And I think of Mickey Mouse and Fantasia. Just like, you know, learning this new magical sort of ability, and suddenly all the brooms are walking and talking and dancing. And it's this incredible menagerie of being able to build whatever the heck you want whenever you want.

Host: Someone who had an idea for 15 years but didn't have the tools to build it was able to build it in 15 minutes, and he recorded his reaction. I almost shed a tear on that.

Gary Tan: Welcome back to another episode of the Lightcone. I'm Gary. This is Jared Harger and Diana. And collectively we funded companies worth hundreds of billions of dollars, right at the beginning, just a few people with an idea. And today we have one of our best alumni to show off what he just launched: Replit Agent. Amjad, thanks so much for joining us today.

Amjad: My pleasure. Thank you for having me.

Gary Tan: Yeah, so we just launched this product. It is in Early Access, meaning it's barely beta software, but people got really excited about it. It works some of the time, so there's a lot of bugs. But we're going to do a live demo here, and I wanted to like build an app, like a personal app that could track my morning mood correlated with like what I've done the previous day. So I want an app to log my mood in the morning, and also things I've done the previous day, such as the last time I had coffee or if I had alcohol and if I exercised that day. That'll send it to the agent.

Amjad: Now you have this like chat interface, so you can see the agent just read the message, and it's now thinking. So what we're looking at here is actually how you might chat with another user, or is this like specifically...

Gary Tan: Yeah, I mean it's very similar to like a multiplayer experience on Replit.

Amjad: Got it. So here it's saying I created a plan for you to log your daily mood. The app will show your mood, coffee, alcohol consumption, and exercise, and it also suggests other features. So for example, suggesting visualization. And that sounds good. Reminders. I don't know, I'll remember. So let's just go with these two steps.

Gary Tan: I think what was also cool is it picked the tech stack that's very quick to get started: Flask, vanilla JS, Postgres. Like, very, very good.

Amjad: So now we're looking at what we're calling the progress pane. So the progress pane is, you can see what the AI is doing right now is installing packages. Actually wrote a lot of code. It looks like it built a database connection, all of that, and it's now installing packages. And we should be able to see a result pretty soon.

Gary Tan: This is really cool because I think a lot of times for new software engineers, one of the annoying parts is just getting all the packages and dependencies and picking the right stuff. And this just does it for you. The agent.

Amjad: So here we have our mood app. I can kind of put that I'm feeling pretty good today. I did have coffee yesterday, but I didn't exercise. Log my mood. Go to history.

Gary Tan: So built a complete web app with just a prompt, like no further instruction from you?

Amjad: Yes. And it has a backend. It has Postgres. And I can just deploy this. So this is already pretty useful. You have this rating, and you have the history, and it's asking me if it did the right thing.

Gary Tan: Oh, it actually is asking you to test it for them?

Amjad: Yeah, it actually did some testing on its own. So it took a screenshot here, and so it knows that at least something is presented, but it wants someone to actually go in and do a little bit of QA. Is it using like computer vision to look at the screenshot?

Gary Tan: Okay, yeah, yeah. And now all the models are multimodal, so it's fairly straightforward.

Amjad: What's on the backend right now? We have actually a few models because, you know, it's a multi-agent system, and we found different models work for different types of agents. The main coding one is Claude Sonnet 3.5, which is like just unbeatable on coding. It is like the best thing. But we use GPT-4o in some cases. There's also some like in-house models. We built an embedding model, a super fast embedding model, binary embedding model, and the retrieval system and index. All of this is built in-house. And a big part of what makes this work is the sort of retrieval system, because figuring out what to edit turns out is the most important thing for making these agents work. You're going a step beyond just RAG, because RAG has hit the limit for this, and you basically have to find a new way to search and find the right places to edit in the code.

Gary Tan: Yes, which is actually something that I don't think has happened yet, but I think is going to happen. For all these agent systems, people are going to move away from RAG and start building custom orchestration like this. So this is very notable. This is like a very cool thing that you figured out.

Amjad: Yeah, if just throwing the codebase in RAG is not going to work, you actually have several different representations.

Gary Tan: Exactly, to allow the agents to do better work.

Amjad: That's right. And we have the trends thing working right now. Nice.

Gary Tan: So we have a couple graphs. We don't have a lot of entries here. I can actually ask it to create data?

Amjad: Oh, really? You can have it create data as well. Yes.

Gary Tan: Now it's asking me to deploy because it's done. It's like, it's time to deploy. And here we have the activity trends, like how many what am I doing by day?

Amjad: There you have it. It's going directly from just an idea to a deployed web app that anyone in the world can access right now.

Gary Tan: Exactly. And one of the things I'm really excited about is like this idea of personal software. 1984 the Mac brought like personal computing to the masses. 2024 we have personal software. I think we just experienced this. You know, Karpathy just tweeted about Replit Agent. He said, "This is a feel the AGI moment." Did you just feel the AGI?

Jared Friedman: I definitely did. And I did last night. I spent a few hours last night using Replit Agent to make a Hacker News clone.

Gary Tan: Nice.

Jared Friedman: There were a couple moments where like I really felt the AGI. The first was it actually had like really good intuition about what you want to make and how to design it. Like we saw that there, where like you didn't give it the idea to make the slider bar be like emojis. It just came up with that on its own. And then the second thing was when I was using it, it really felt like I had a development partner, where it would ask me questions. It would ask me to like change things. At one point it got like stuck. I wasn't sure how to do something, and so it asked me how to do the thing. And then I told it, and then it's like, cool, got it, and just kept going.

Gary Tan: Yeah, it feels great. And sometimes you want to give it some help, right?

Jared Friedman: Right. You want to go debug if you know how to debug yourself, or you go ask ChatGPT about something and come back to it. Just give it more information, it'll be able to kind of react to it.

Diana Hu: You should have it. It definitely feels like talking to like a developer. You should do like the grumpy thing and have different modes. You could have like grumpy programmer where it just tells you your ideas are bad and he wants to build something else anyway.

Gary Tan: Oh, that would be cool. Just like have a toggle, for example, like an overengineer toggle. Like just like overengineer everything.

Amjad: So it added this toggle, but I don't think it works. I don't think it connected up to the X-axis.

Gary Tan: Yeah. I think this is interesting about all these AI programmers, which is that it's not like we created some super intelligence that somehow can just build an entire app perfectly from start to finish without making any mistakes. It actually codes the way a human does, which is it writes some code and it's like, "Well, I think this is right, but I'm not sure. I guess I'll try." And then it tries. "Oh no, I have a bug." It's like the same thing.

Amjad: Yeah, yeah. And our design decision has been always like this is a coworker, and you can just close this and you can go to the code and you can code yourself. Just fix it yourself. And again, if you don't know how to code, my hope is that as you are reading what the agent is doing, you've learned a little bit of coding along the way. And by the way, this is how I think our generation learned how to code, not through agents, but almost by doing these incremental small things like editing your MySpace page or doing a GeoCities thing. And I feel like we sort of lost that incremental learning scale, where now you need to go and get a computer science degree or go to a coding bootcamp to kind of figure this out. But if we made this like a fun thing that people can go build side projects in and get exposed to what code is, I think that would be perfect. And again, my view is that we're still far from fully automated software engineering agents, and people should still learn how to code. You have to do way less coding, but you will have to read the code. You will have to debug it. In some cases, the agent will get you fairly far, but sometimes it'll get stuck, and you need to go into the code and figure it out.

Gary Tan: Yeah, I think that's actually pretty important. I've been meeting a lot of 18, 19-year-olds who are freshmen, and they're like, "Well, the code will write itself, right? I don't have to study this stuff anymore." And I'm like, "No, that's not true at all." Like, I actually think that now it is actually more leverage. It is far more leverage to know how to code than ever before. And it's actually even more important. And it will make you way more powerful. Like, you don't have to be all the way in the weeds on everything. You actually are going to be able to orchestrate this giant army of agents. And I think of Mickey Mouse in Fantasia. Just like, you know, learning this new magical sort of ability. And like, you know, suddenly all the brooms are like, you know, walking and talking and dancing. And it's this incredible menagerie of being able to build whatever the heck you want whenever you want. Just like, literally from any computer, from any web browser.

Jared Friedman: Yeah, I try to come up with a like a Moore's Law type thing, where it's like the return on learning to code is like doubling every six months or something like that. So learning code a little bit is, in 2020, was not that useful because you would still get blocked. You wouldn't know how to deploy something. You wouldn't know how to configure something. Let's go to 2023 with ChatGPT. Learn to code a little bit, you'll get fairly far because ChatGPT can help you. And then 2024, learn to code a little bit is a massive leverage because we have agents like this and others. And there's a lot of really cool tools out there like Cursor and others that will get you super far by just having a little bit of coding. And just extend that forward. Like six months later, you're going to have even more power. So programmers are just on this massive trajectory of increased power.

Amjad: Can you tell us more about the tech behind this? It's kind of fascinating. At the heart of it, it is sort of this, as I described before, a multi-agent system. You have this core sort of ReAct-like loop. So ReAct is a, you know, an agent Chain of Thought type prompting that's been around for a couple of years now. And most agents are built on that. But ours is also a multi-agent system. We give it a ton of tools using tool calling. And those tools are the same tools, again, that are exposed to people. And by the way, you need to be really careful about how to expose these tools and how the agent sees them. So for example, our edit tool returns errors from the language server. So we have a language server here, a Python language server. Like a human coding, you know, if I make a mistake anywhere here, it will show me right away. Similarly, when the agent is coding, it gets feedback from the language server. So again, you want to treat it as much as you can like a real user. And so for any action it gets, it gets sort of feedback, and then it can react to that feedback. And so these are the tools again: package management, editing, deployment, all the database, all those are tools. And then there are a lot of things that make sure that it doesn't go totally off the rails, because it's very easy. We've all used agents that go off the rails and go into endless loops. This still sometimes does it, but we have another loop that is doing a reflection that is always thinking, "Am I doing the right thing?" We use a lot of LangChain tools. So LangGraph is an interesting new tool from LangChain that allows you to build agent DAGs very nicely. And they have some logging mechanism and a tool called LangSmith, where you can look at the tracers. Looking at the traces for DAGs is very, very, very difficult and very hard. So debugging these things have been fairly difficult because you want a tool to actually visualize the graph, and there isn't a lot of tools that do that right now. And so there's this reflection tool, reflection agent. And the other thing that we talked about earlier is retrieval is crucial. And again, this has to be kind of neurosymbolic. It has to be able to do RAG-style embeddings retrieval, but it has to be able to look up functions and symbols inside the code. This is why I do think, maybe extrapolating a bit, even if we get into the world of foundation models that have really, really large context windows—I mean, Gemini allows in the millions of tokens—you will still need very specialized things that do lookups like this because it applies to different contexts, knowing the functions, and treating it more like how it compiles, at the end like a graph. Large context windows, you can totally shoot yourself in the foot with them.

Gary Tan: Yes, because it's easy for the model to bias a lot more towards whatever is at the end.

Amjad: Kind of like a human, yes, exactly. And so you still need to do context management. And you need to figure out what to put in and how to rank memories. So this agent, every time it does a step, it goes into a memory bank. And then every time we go into the next step, we need to be able to pick the right memories and figure out how to put them in context. If you pick the wrong memories, for example if you pick a memory that had a bug or there was an error in it, whatever—it might still think that there's a bug. But if you've already recovered from that, you want to make sure that the memory of having created a bug is either kind of augmented by another memory of fixing it or entirely removed from the context. And so memory management is crucial here. You don't want to put the entire memory in context. You want to be able to pick the right memories for the right tasks.

Gary Tan: I feel like this is a really concrete rebuttal to situational awareness...

Gary Tan: Whole like sort of sci-fi, you know, AGI is going to kill us tomorrow kind of argument simply because that all is predicated on larger context window, more parameters, throw GPUs at it and it's going to work. Like you can't just scale it up, like you're not going to get what you want from just scaling it up. There is actually a lot of utility in having these agents work one with one another, with being actually smart about what is the intermediate representation and being able to pull back, you know, sort of model what a human would do. I mean, this is sort of like the case study and like, oh yeah, you can't just, you know, scale up everything by 50x and have it work the way that they think it will.

Host: Yeah, in many ways, like building a system like that sort of humbles you, you know, sets your expectations about AI and the progress in AI in sort of a different way because yeah, the systems are very fragile. They're really still not great at following instructions. People talk a lot about the hallucination problem. I think the bigger problem is like just following orders. It's so hard to get them to actually do the right thing. What do you think is the path to AGI?

Gary Tan: So my view on AGI is that maybe we'll get to something called functional AGI, which is where we automate all those sort of economically useful tasks. I think that's fairly within reach. I think it's almost like a brute force problem. It's sort of the bitter lesson.

Host: Do you think it involves doing a lot of work like what you guys did? Like basically building, like carefully fine-tuning orchestrations of groups of agents for each task, so doing what you did for programming but doing it for customer support and for sales, for accounting, every function?

Gary Tan: Yeah, I think so. And maybe you can eventually put it all into one model. The history of machine learning has been we create these systems, we grow these systems around these models, and eventually the model will eat those systems. So hopefully like everything that we did, at some day there's like an end-to-end machine learning system that could do it. Tesla, you know, famously had all these logic and whatever, and now like after v13, they just do end-to-end training. And so eventually we'll get there. But I wouldn't consider it true AGI because you throw something out of distribution at it and it wouldn't be able to handle it. I think true AGI would require efficient learning, being able to be thrown in an environment with no information at all, being able to understand the environment by examining it and learning a skill required to navigate that environment. And LLMs are not that. Maybe they're a component of that, but they're not efficient learners at all.

Host: You actually demonstrated this because the way you describe LLMs are intuition machines, and in order to get them to work in programming tasks you have to add this layer with symbolic representation like in programming, and there's a lot of concepts in programming and how computation works like Turing completeness and all that, right?

Gary Tan: Yes, exactly. Those are like very explicit classical computer science, classical AI. Yeah, we do backtracking and all that.

Host: Yes, that's not generalized, that's specialized.

Gary Tan: Incredibly useful, specialized, yes.

Host: So it's only been live for four days, yeah? But already people have done a bunch of like really interesting and impressive stuff with it. Do you want to talk about some of the things that you've seen people do with it that are most like surprising and interesting?

Gary Tan: Yeah, one of my favorite things that I saw was someone who had an idea for 15 years but didn't have the tools to build it, and was able to build it in 15 minutes. And he recorded his reaction, and it's like a personal app. He built an app where he can put memories on a map and attach files and audio files to it, memories about his life. "I went to school here," and like add a picture, whatever. When the app showed up and he tested it, he was like, he was so surprised. I almost shed a tear. I was like, you being able to unlock people's creativity is so rewarding. And then he wants an integration with Apple Photos or to use it to actually build an export tool.

Host: Yes.

Gary Tan: And another user Meck built a sort of Stripe coupon tool. So he has a course he runs on Stripe, and he wants to be able to send people coupons, and so he built it in like 5, 10 minutes. And actually, I don't think you would be able to build something like that in no-code. You would struggle really hard. You would probably use two or three no-code tools. People use like Bubble on the front end and Zapier on the back end and what have you. Sometimes I'm surprised the no-code people are actually quite smart and quite hardworking because they figure out how to create these systems using no-code, but it's just actually a lot easier to just generate the code for it.

Host: It's a coding tool for the no-coders.

Gary Tan: Yes, yes. And so yeah, we're seeing a lot of traction there, which is actually a challenge I think the no-code tools have in general. Is straddling this line between they start very much no-code, and then they find that people keep pushing the limits of what they want to build in these tools. And then the frustrating part with no-code tools is that if you hit the limits, you're just stuck. You just can't solve it. And the cool thing is, if you were saying earlier, if you can get the no-code people to switch to Replit, maybe initially they don't program at all, all they know how to do is like prompt it. But then at some point they're going to look at the code and they'll realize that they can just edit it, and like it isn't that hard, and that's how they gradually become programmers.

Host: Yeah, that's interesting. I played around with it to build just like a simple recruiting CRM, which is actually the kind of thing you would have used Airtable for. And one of the suggestions when it told me the plans, one of the features was, "Would you like this feature?" was exactly that. It just like role-based permissions. And I was like, oh, that's pretty like a sophisticated prompt or like suggestion off the bat.

Gary Tan: Yeah, that's a $10,000 a month enterprise feature right there that you could just prompt and have it work. It's crazy.

Host: I mean, this is like the definition of low bar, high ceiling. Like all of the biggest software companies in the world sort of capture that idea really powerfully. So my favorite thing is these order multiple order magnitude sort of time difference of building something. Someone said they spent 18 months building a startup, they were able to generate the same app in 10 minutes using Replit. Someone said they spent a year building a certain app that they were able to build it in an hour with Replit agent. But yeah, I think it will save millions of dollars of human hours.

Audience Member: What a time to be alive, guys. Can I take a Replit agent and apply it to my existing coding stack yet?

Gary Tan: Not yet, got it. So again, it's sort of super early. We built the retrieval system that we built is to be able to do this. We should be able to throw it into any codebase, index the codebase really quickly, and be able to give it intelligence about the codebase. The system also has like summaries of files and summaries of projects. So we use LLMs to, as we're indexing the system, create these like small summaries for the agent to understand what a project is. So we have the infrastructure for it, but that's the next step. And we also want to add more autonomy for people who want it. So for the team version of this, we want to be able to send it to the background, be able to give it a prompt, and then forking the project, going and working as autonomously as it can, and then when it's done, it sends you a pull request back. Or if it runs into a problem, it comes back to you with a problem.

The other thing I want to do is, you know, the vision for this has been, you know, we have this bounties program, and bounties, people submit things they want to build or problems they have. And people in our community, users, help them fix it for a certain price. And I was thinking, you know, agents are not perfect. And so perhaps the agent can also summon a human. So another tool that it has is to be able to summon like a bounty hunter. And so we go to the market, it asks the creator working with it, "Hey, like I'm running into a problem. Do you want to put some money on it?" And we can go like, you know, grab an expert. And so it's like, "Yeah, cool, yeah, put $50 on it," and we'll go to the market, hopefully real-time market. We'll say for $50, we have this problem. Can you come in? A human expert comes in as another multiplayer into the system, either helps you by prompting the agent or by going and editing the code themselves.

Host: That's so clever. I mean, this whole thing of getting the human to be another agent in this greater intelligence orchestration system. You have, yes, I'm a big fan of Lickliter's sort of human-machine symbiosis. Right? That's always been the thing. You know, I like to talk about AGI and all of that, but I just feel like you know, computers are fundamentally better by being extensions of us and by joining with us, as opposed to you know, being this competitor.

Gary Tan: 100%, team human. We need to print t-shirts.

Host: You had a, I guess, sort of mini chess moment earlier this year. Then we're all blown away by this demo. And sort of, you know, you've been working hard on sort of remaking the way all software is deployed and written for some time. I mean, what did it take to get to this moment? You know, you did have to do a layoff and reset your org. What happened?

Gary Tan: Yeah, so last year we raised a big round. We felt we're making fast progress, and there was a lot of energy, and I felt like I needed to grow the company. You know, for a long time, Jared knows for a long time, Replit was like tiny. It was actually run out of your apartment for how many years?

Jared Friedman: For many years, like three or four years.

Gary Tan: And we were like four or five people for like many years. So we started growing in 2023, even when you had a lot of users?

Jared Friedman: Yes, like you were four or five employees when you had like millions of users.

Gary Tan: Yes, that's right. So we were always kind of lean, but I thought last year, okay, we have really big ambitions, we got to go hire people. I got to hire executives, I got to create like a management structure. I got to like grow up, is what investors were telling you?

Jared Friedman: He was like, oh, you got to hire.

Gary Tan: No, actually, I was on my own. But it definitely was the prevalent advice. I mean, you were absorbing this advice from sort of the world that ordinarily advises startups to do exactly that.

Jared Friedman: That's right, that's right.

Gary Tan: And it just got really miserable. We had like multiple layers, we had different meetings where I'm trying to like run the company from. We had like an executive meeting, staff meeting, whatever. We had road maps, we had planning sessions, and I just couldn't shake the feeling that it was all laring. It was not work, it was laring. But right now, we don't have a road map. Right now, literally, we work on like three or four things. I'm involved in all of them, and I know what's going on. I know what people are working on, and I think we got a lot more productive by getting smaller, by, you know, flattening the organization.

Jared Friedman: I think one thing that's a story that I think we've heard from many founders, and one thing I'm curious to see how this plays out is I feel like what actually sparked off a lot of manager mode was feeling that people had more ideas to run with and they had like resources to execute on. And you realize that bureaucracy creeps in and you actually just can't get ideas done as quickly as you want. And so now I feel like everyone's getting rid of middle management. And I'm curious to see if the same thing, the same temptation, I think will happen again. I think even is when you make it easy to go from like zero to one, you actually help you create more good ideas because you're like, oh yeah, it's actually like, I can just get things off the ground really quickly. And so then it'll be interesting to see how people stay now you have the smaller, flatter structure, you'll get more ideas for things you want to do, and then staying like disciplined to not go back into, oh yeah, like we should actually do like the 10 things we could possibly be doing versus like the five or six you can keep in your head. I think is actually a challenge.

Host: I guess there's a warning idea here because there's Parker Conrad's compound startup. But the interesting thing about the compound startup is I think they're trying to explicitly make the other product lines feel like a startup and govern like a startup unto itself, which is like sort of the opposite of having like divisional responsibility. I also think with Rippling and Parker, like Parker is known having this hiring tactic where he only hires, or tries to hire, a lot of former founders and then puts them in charge of a product line, which has obviously worked really well for Rippling. I think it's hard for most people to pull that off because you can't hire the quality of former founder unless you have, I think unless the company's already like proven successful, or you're just like a top-tiered recruiter. Parker is pretty like, you know, top 0.1% of ability to recruit really great people. But Parker sort of founded remote though because we, he gave a talk at YC Growth when we did this a couple years ago, and he was still doing support tickets.

Gary Tan: Oh yeah, still is.

Host: He told us that Harj hosted him a couple of months ago actually, right over there. And he said that, he said basically he loves answering customer support tickets and he will never let it go because it's his direct line of information to know what's really going on with the customer.

Gary Tan: Yeah, yeah. I mean, that's to final remoting. I think maybe he's doing the compound startup. He's giving them a lot of autonomy, but he's in the details.

Host: So how did this play out for this AI agent? Like we talked about how you built it technically, how did you build it organizationally? This was a whole big like a big bet. It was totally new technology that like the Replit team wasn't used to working on. How did you pull it off organizationally?

Gary Tan: Yeah, great question. We tried building agents multiple times in the past, and just the technology wasn't there. And finally, when we felt it was there, actually one of our employees, Zen Lee, who kind of started this new incarnation of this, made a demo. And he showed me the demo, and it was so simple. It was just like the agent like calling a couple tools and doing things in IDE. But I could see that it's finally almost here, like I could taste it almost. And in that feeling, just was like, okay, we're going to make this big bet. And so we created something called the Agent Task Force. So in the task force, it's like people...

Gary Tan: From a lot of different teams. So you have the IDE team present in the task force, you have the DevX team that works on package management and things like that, you have a UX and design component, and you have the AI team. So you have the AI team at the center, so it's almost similar to a Kera diagram. So in, we organize it in the same way that the diagram works. The kernel OS is the sort of the AI team, and then they're connecting out to all these tools that are created by the tool teams. And then you on top of all of that, you have the product and instead of UX team that is working on the entry points and how do you structure this, which was very tough as well. The design was tough, and we had like two meetings every week. On Monday, we had this war room meeting where Michael, our head of AI, will do like a run, and we'll see what's broken, what's wrong with it. They'll come up with the priorities for this week. And then on Friday, we have the Agent Salon, where I do a run and I look at what's working, what's broken. I ask them about their priorities. We might reprioritize something. Things I might change some things in the product. We make big changes like rapidly. And so every week, we made a ton of progress.

Host: What does doing a run mean?

Speaker: Doing an agent run literally, actually going through and using the product and seeing where it broke, seeing where it breaks, and figuring out what the priorities in order to fix it where it broke.

Host: Brilliant. Yeah, did each of the teams basically build their own agent as well?

Speaker: Um, some of them did because some of them you had to. The screenshot tool was an agent because you had to kind of have an AI look at the screenshot, come up with the thoughts, and then return them to the main manager agent. So the ID team wrote the screenshot agent, and then the package management team kind of built probably the text stack setup type of configuration, which is really cool.

Gary Tan: Yeah, it worked out. The organization structure worked out really well. I mean, surprisingly well, because I think it is similar to how we worked when at the center was the user, and now the user is the AI. What's coming next with the agent? Like, what do you want to add to it? What do you think are going to be the big next leap forwards for it?

Speaker: Reliability. I think the most important thing right now is reliability, making sure it's not spinning, making sure it's not breaking. And then expanding it to support any stack you would want. So right now, we don't really listen to the user when they give us a stack. We push back. The agent pushes back. It's like, "Ah, I'm just going to do it in Python," or whatever. But if you really want OTE, so we want to be able to accept user requirements with the great stack. Should have the poor grey mode, write only. Write it in Lisp, you know? This modes thing is a really like an April fools thing. Like, polyglot over engineer, bad UI, doesn't care about UI, everything's correct, but very confusing.

Host: How about just the interaction? I mean, you mentioned like Licklider and the whole human-computer symbiosis theory. Like, is text like as far as it goes? Are there other ways that people you think will want to interact with their AI agent?

Speaker: You should be able to like draw in the UI and communicate with the AI by drawing, right? Should be able to say, "Hey, like, this button's not working, maybe move this here," or "This file, you know, bro, is not, you know, refactor this file," whatever. So, you know, if the whole thing is a canvas that you can draw on, you can communicate a lot more expressively with the agent. And of course, you're talking, you know, as opposed to typing, being able to talk and draw. It's imagine it on the iPad too. We have an iPad app. It could get really, really fun and creative, kind of like a full UI mockup that you would do in Figma. You could kind of hand sketch it and get it to do it, like like how running a real engineering product team would feel.

Gary Tan: Like that's right.

Speaker: And then we're going to add like more simpler agentic tools. So right now the agent kind of is, you know, takes over and it's like writing everything. But a lot of people just want more agency, more advanced users. So we want to be able to do like single step or single action agents. So say like, "I want to add this feature, show me what you're going to do." I'll do a dry run, show you all the diff, show you all the packages going to install. And then you'll be able to accept it or reject it. And that way, more advanced users will have more control over the code they're writing.

Gary Tan: Om, thank you so much for coming and showing us the future in such a profound way. If I wanted to do this all myself, what would I do?

Speaker: Well, first of all, I want to say it's again barely beta software. If you're if you're brave and you want to test it and give us feedback, go to Repet, sign up for our core plan, because this thing is expensive. We can't give it away for free. And you'll be able to see that module on the homepage that says, "What do you want to build today?" And then you can go through that and start working with the agents. Just have an idea in your mind. Just write a couple sentences. Don't make it too complicated or too technical. And get started. You'll get a feel of how to work with the agent pretty quickly. It should be pretty intuitive. And share with us what you're building. Happy to kind of reshare, retweet, whatever people are building with the agent.

Gary Tan: Amazing. Well, it's time to feed the AGI. We'll see you guys next week.
