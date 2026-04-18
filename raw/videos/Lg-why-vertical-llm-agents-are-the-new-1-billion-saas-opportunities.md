---
title: "Why Vertical LLM Agents Are The New $1 Billion SaaS Opportunities"
slug: "Lg-why-vertical-llm-agents-are-the-new-1-billion-saas-opportunities"
media_type: "Video"
author: "Y Combinator"
speakers: ["Host", "Jake", "Speaker"]
categories: []
description: "In this episode of the Lightcone, the hosts sit down with YC alum Jake Heller, the co-founder and CEO of Casetext (which sold to Thomson Reuters for $650 million in 2023) to discuss what it takes to build a successful vertical AI company."
url: "https://ycombinator.com/library/Lg-why-vertical-llm-agents-are-the-new-1-billion-saas-opportunities"
youtube_id: "eBVi_sLaYsc"
youtube_url: "https://www.youtube.com/watch?v=eBVi_sLaYsc"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Why Vertical LLM Agents Are The New $1 Billion SaaS Opportunities

As LLM’s become exponentially better it is clear that vertical AI agents are key to the next generation of billion
dollar SaaS companies. In this episode of the Lightcone, the hosts sit down with YC alum Jake Heller, the co-founder and
CEO of Casetext (which sold to Thomson Reuters for $650 million in 2023) to discuss what it takes to build a successful
vertical AI company and overcome resistance from industry veterans and skeptics.

## Transcript

Speaker: Jake Healer

This is their first ever experience talking to this godlike feeling, you know, AI that was all of a sudden doing these tasks that would take me when I practice like a whole day and it's being done in a minute and a half. The whole company, all 120 of us, did not sleep for those, you know, months before GPT-4. We felt like we had this amazing opportunity to run far ahead of the market. That's why you're the first man on the moon.

Host: Gary Tan

Yeah, welcome back to another episode of the Light Cone. I'm Gary. This is Jared, and Diana Harge is out but he'll be back on the next one. And today we have a very special guest, Jake Heler of CaseText. I think of Jake as a little bit like one of the first people on the surface of the moon. He created CaseText more than I think 11, 12 years ago actually. And in the first 10 years you went from zero to $100 million valuation, and then in a matter of 2 months after the release of GPT-4, that valuation went to a liquid exit to Thomson Reuters for $650 million. So you have a lot of lessons about how to create real value from really large language models. I think you were, um, you know, one of our friends in YC, one of the first people to actually realize this is a sea change and revolution, and not only that, we're going to bet the company on it. And you were super right. So welcome, Jake.

Speaker: Jake Healer

Happy to be here.

Host: Gary Tan

One of the cool things I think about Jake's story and reason why we wanted to bring him on today is that if you just look at the companies that good founders are starting now, it's a lot of vertical AI agents. I mean, I was trying to count the ones in S24. We have literally dozens of the YC companies in the last batch that are building vertical-specific AI agents. And I think Jake is the founder who is currently running the most successful vertical AI agent. It's by far the largest acquisition, and it's actually deployed at scale in a lot of mission-critical situations. And the inspiration for this was, uh, we hosted this retreat a few months ago, and Jake gave an incredible talk about how he built it. And we thought that it'd be super useful for people who watch the Light Cone who are interested in this area to hear directly from one of the most successful builders in this area how he did it. So how did you do it?

Speaker: Jake Healer

Well, first of all, like a lot of these things, um, there's a certain amount of luck over the course of our decade-long journey. We started investing very deeply in AI and natural language processing, and we became close with a number of different research labs, including some of the folks at OpenAI. And when it came time for them to start testing early versions—uh, we didn't realize it was GPT-4 at the time—but what was GPT-4? We got a very early kind of view of it. And so, you know, months before the public release of GPT-4, you know, we as a company were all under NDA, all working on this thing. And I'll never forget the first time I saw it. It took maybe 48 hours for us to decide to take every single person of the company and shift what they were working on from the projects we were then working on at the time to 100% of the company all working on building this new product we call Co-Counsel based on the GPT-4 technology.

Host: Jared

How many people was that?

Speaker: Jake Healer

We're about 120 people at the time.

Host: Gary Tan

So you took like 120 people and completely changed what they were all working on?

Speaker: Jake Healer

Yes. Yes, yes. In 48 hours, yes.

Host: Gary Tan

And for the people watching, uh, CaseText originally, I mean, had always been in the legal space. You're a lawyer and you built something for yourself. And you know, sort of the first versions of it were actually sort of annotated versions of case law.

Speaker: Jake Healer

Actually, yeah, that's exactly right. So in the very early origins of the company, the mission of the company, what we're always focused on, is how can we build something that brings the best of technology to the legal space? Um, I as a lawyer, I actually like the job a lot. The parts of my job that I hated the most was when I had to interact with the technology that lawyers have to use regularly to get the job done. I remember thinking, and this is like 2012 when I was at a law firm, if I want to do something really trivial, I had like a new iPhone at the time. I can go on Google and find like movie times or where's the closest open Thai restaurant with vegetarian options? That was super easy. But if I wanted to find the piece of evidence that was going to exonerate my client and make it so he doesn't have to go to jail for the rest of his life, or the key legal case that will help me win a billion dollar lawsuit, well, that's going to be like 5 days in a row till 5 a.m. every day. It's like there's got to be a better way.

Host: Gary Tan

What is the process as a lawyer you would have to read the stacks and stacks of documents?

Speaker: Jake Healer

Pretty much, yeah. Um, right before I started practicing, before everything went virtual or like online, uh, you would literally be in a basement with bankers' boxes full of documents reading them one by one by one to try to find, you know, all the emails in a company like Fisher or Google to see if there is potential fraud or, um, and then if you wanted to find case law, slightly before my time, you'd literally go to the library and open up books and just start reading. And you know, new products were coming out that were some of the first web-based research tools, but they were pretty clunky. It was just hard to find the relevant information. You couldn't do Control+F or any of this stuff basically.

Host: Gary Tan

Basically not?

Speaker: Jake Healer

Yeah.

Host: Gary Tan

And what was interesting about your, uh, background is you also happened to be the rare breed of having also computer science training. So this must have driven you nuts.

Speaker: Jake Healer

Yeah, exactly. I mean, in the law firm I'll never forget, I was building like browser plugins to go on top of the tools I was using just to make my like life more efficient and effective. And actually, one of the reasons I left the law firm to start a company and apply to YC was I got in trouble with the general counsel who thought, like, hey, why are you spending all your time, you know, doing this tech stuff? And also made it at the time very clear that my law firm owns all that technology. So I decided to do something different.

Host: Gary Tan

So do you want to tell us a little bit about the first 10 years of CaseText, the sort of like long slog in the pre-LLM era? One of the lessons here, I think that I took away from that time period, is that when you start a company you may not get the exact right—you may have like the right kind of general direction, you know? There's a problem you're trying to solve. But it could take a very long time to figure out what the solution is. For us, for example, you know, we saw that there was this kind of combined issue of like bad technology in the legal sphere, but also like, a lot of lawyers use content to do things like research and understand like what the law is. And so we thought, okay, well, we can do the technology better. But how are we gonna get this content? And we spent like a couple of years trying to get, as Gary said, lawyers to annotate case law and to provide information. So it's like a UGC site, like user-generated. That was a big focus of ours—like the kind of one-two punch of better technology but also better content. Um, we, you know, at the time our heroes were like Stack Overflow and Wikipedia and GitHub and other kind of open source or UGC kind of websites. And it was a total failure. Like, we could not get lawyers to contribute their time and information. And I think these are just different populations. The typical Wikipedia editor has more time on their hands than they know what to do with, and so they're adding—not all, but many do—and they're adding content for free and altruistically. Lawyers bill by the hour. Their time is incredibly valuable. They're always running out of time. They had no time to kind of contribute to some UGC site. So we had to pivot. And we started investing, investing very deeply at the time—it was not called AI, it's just like natural language processing and machine learning. And saw that first of all, we didn't need to create all this UGC like to replicate some of the best benefits of what our competitors had in these big content databases. Some of it you can basically do even then, kind of on an automated basis. And then also, uh, we were starting to create these user experiences that were, you know, a lot better than what our competitors could offer, based on then, at the time, what seems kind of quaint, like AI stuff. Like, you know, the same recommendation algorithm that powers Pandora and Spotify's like recommended music. You can use that. They look at basically how this song relates to that song. People listen to this also listen to this and this and this, right? Similarly, we looked at, okay, cases that cite you, you know, other cases—they all reference earlier opinions. You know, they kind of build out this network of citations. And we found ways that we can check a lawyer's work. They'd upload their work so far and be like, well, everybody who talks about this case talks about this case too, and you missed that. Um, so cool experiences like that. But the truth is, until the very end, until Co-Counsel, a lot of what we did were relatively speaking kind of incremental improvements on the legal workflow. And one of the things that's kind of weird about this is, um, when there's just an incremental improvement, it's actually pretty easy to ignore. A lot of our clients—they never say this literally, but you get this impression—you walk into the room, their office, and you try to pitch them a product and you say, this is going to change everything about the way you practice. And they go, well, I make $5 million a year. I don't want nothing to change. This technology? No, I do not want to introduce anything that has the opportunity to make my life at all worse or potentially worse or potentially more efficient because they bill by the hour. It was really only after, like, much later, when ChatGPT came out—you know, the time we were privately and secretly working on GPT-4—ChatGPT came out, and all of a sudden, every lawyer in America, probably in the world, saw, oh, my God, I don't know exactly how this is going to change my work, but it's going to change it very substantially. Like, they could feel it. And the same, you know, guys and gals were telling us, I make $5 million a year, why would it change anything about my life? We like, I make $5 million a year—this is going to change something. I need to be ahead of this. The technology itself—and we'll get into this in a second—really changed what we can build for law employers, but also the market perception of what was necessary really changed as well. And for the first time in our 10 years, you know, even before we launched Co-Counsel publicly based on GPT-4, they were calling us like, you know, we know you work on AI. We need to get on top of this. What can you, you know, what can you show us? What can we work on? And I think it's because the change was not incremental anymore. It was like fundamental. And all of a sudden, they had to pay attention. They could not ignore it.

Host: Gary Tan

I guess the mental model I have for you is there's this concept of the idea maze, you know? The founder goes in the beginning of the maze, and they're just like feeling around. Like, actually, uh, in the arena, talking to, you know, customers, learning, like, where are the walls? Which path to go? Should I go left or right? Like, and then, um, as is actually common for startup founders in the idea maze, you will actually reach a dead end and then usually you have to pivot.

Host: Jared

Yeah.

Host: Gary Tan

And then I think you have a very interesting story because you were sort of towards the end of maybe like one of the, uh, you know, parts that weren't going to get you all the way to product-market fit. But then LLMs dropped, and then it's like the maze got shaken up.

Host: Jared

Yeah.

Host: Gary Tan

And then you are actually much closer to product-market fit than absolutely anyone else.

Speaker: Jake Healer

That's yeah, I think that's exactly right. That's why you're the first man on the moon, yeah. I think there's clearly something to that. And the thing is, you know, each time we progressed through that maze, it felt like maybe now we're at product-market fit, you know? We were making real revenue before we launched Co-Counsel, and we had real customers, and they said really great things about us. I keep on thinking about this article written by Marc Andreessen in like the early 2000s. Uh, I think it's called "The Only Thing That Matters." And in it, he describes what it feels like to have product-market fit. He lists things like your servers will go down, you can't hire support people and sales people fast enough. You're going to eat for a year free at Bucks, the, the kind of famous Woodside, you know, diner where a lot of VCs will take you. The press, and I read that early on in my like, like, you know, career, and I was like, okay, well, that's like hyperbolic. But when we launched Co-Counsel, it was literally exactly that. Our servers were going down. We could not hire support people fast enough. We couldn't hire sales people fast enough. I ate a lot of Bucks, you know. Um, before, we was a really big day if we were in the ABA Journal or some other, you know, legal-specific publication. We were on CNN and MSNBC. And like, you know, all of a sudden, everything changed. And that's what real product-market fit looks like. I think Mark was even in like 2005, whenever the article came out.

Host: Gary Tan

Exactly right about it.

Speaker: Jake Healer

Looked like in 2023.

Host: Gary Tan

Can you talk about that crazy time? Because it was only two months from when you launched Co-Counsel to getting bought for $650 million. So like, what happened in those two months?

Speaker: Jake Healer

Well, to be clear, the transaction only closed six months after we launched, but it was two months the conversation started. And so, uh, so we started building Co-Counsel, and, and for just just to, uh, to kind of background purposes, the idea we came up with—again, like, 48 hours, like a weekend—after seeing GPT-4 was, um, and it's something that not but kind of still sounds crazy today, but it felt crazy at the time, which is this AI legal assistant. By which we mean it's like almost like a new member of the firm. You can just talk to it, um, not unlike how you might talk to something like ChatGPT today. Uh, and give it tasks like, I need you to read these a million documents for me and tell me if there's any evidence of fraud happening in this company. And then within a couple of hours, it's like, I've read all the documents. Here's what the summary is. Or summarize documents or do legal research and put together a whole memo after researching, you know, hundreds or thousands of cases, answering the lawyer's initial research question. And, and so in that sense, it was this like really powerful extension of the workforce of these law firms that was the concept from the beginning. And we made a very early initial version of it. And we started—because we couldn't, you know, under our agreement with OpenAI, we could not be public about this product—but they did let us extend the NDA to a handful of our customers. And so we started having our customers use it. And so, you know, for months before GPT-4 was launched publicly, we had a number of law firms. Uh, they had no idea they're using GPT, but they were like seeing something really special, right? This is actually even before ChatGPT. So they, this is their first ever experience talking to this.

Speaker: Godlike feeling, you know? AI that was all of a sudden doing these tasks that would take me—when I practiced—like a whole day, and it's being done in a minute and a half, right? And so, as you might imagine, like it was nuts. I mean, first of all, the whole company—all 120 of us—did not sleep for those, you know, months before GPT-4 was like publicly launched. Therefore, we could publicly launch the product. We felt like we had this amazing opportunity to run far ahead of the market.

Something really beautiful happens when everybody's working super, super hard, which is you iterate so quickly. And actually, I still see some companies out there—they're stuck where we were in the first month of seeing GPT-4, right? Um, and I think it's because they're just not like as intensely focused and engaged as we were able to be during those—like, about six months or so—before the public launch of GPT-4.

Host: You kind of had to shake the company. You kind of went into deep founder mode because there was a lot of pushback from employees, like, "Oh, this thing was working. Why should we go into the deep end of AI?" Tell us about that founder mode moment for you.

Speaker: So, first of all, this is especially true running a business for ten years, because they've seen you wander through that maze and bump into dead ends. And a lot of those folks have been there for most or all that time, watching me—as the founder—saying, "We're definitely going this direction. It's definitely going to work." And sometimes it doesn't. And you only get so many of those with employees, right? So this was maybe my last one that I had with some of these folks. And they're like, "Here Jake goes again with this crazy new technology and some idea we're gonna invest deeply in." And yeah, it took some convincing.

If you imagine, like, what some of the different roles are—if you're in the go-to-market role, if you're selling or marketing a product, and we're making—you know, we're growing seventy, eighty percent year-over-year, we're between fifteen and twenty million in ARR—things weren't like terrible, right?

Host: That's great, yeah.

Speaker: Yeah, we were great. But like, so they were like, "What? Why are we even—?" You know, the board—some of the members—like, I get this immediately. Some of them had to be persuaded, right?

Um, about the founder mode moment—like, one thing that really worked for me is I led the way through example. I built the first version of it myself.

Host: Wow. Even with a 120-person company with a whole bunch of engineers and lawyers and stuff, like, you opened up your IDE and actually built the thing yourself?

Speaker: Oh, yeah. And part of it was the NDA only extended, at first, to me and my co-founder. That was it. But that was a blessing, though—it turned out to be like perfect. And even after the NDA got extended a little bit, we kept it pretty small at first. For the first little bit of time, I made my mind within forty-eight hours that we're going to do this. But we actually only told the company, I think, a week and a half afterward. We first got access during that week and a half. Like, we built the very first version—like, prototype version—of this. And again, I won't—I'll never forget this. The timing is just so funny.

Like, we saw it on like a Friday. We had it all weekend long. We're working with it. And then Monday was an executive offsite where everybody came. All my executives came, and they expected we're going to be talking about how we're going to hit our sales target for the next quarter. And it's like, "Guys, we're talking about none of that, you know? We are talking about something totally different right now. Let me show you something on my laptop."

So yeah, I built the first version myself. But going through that process—me and then a handful of other people—I think was really helpful. And we also brought in customers early, and that helped convince a lot of people. As soon as like a skeptical sales or marketing person, or whatever, or even an engineer, was on the other line, end of a Zoom call, where a customer was reacting to the product in real time and giving us their honest reactions—like, seeing the look on their face—again, you have to imagine it's almost hard to imagine that the world was like pre-ChatGPT. But then there, some of these people were seeing that exact idea for the first time, and they were just blown away. And that really changed minds quickly.

I mean, we saw people go through like existential crises live, you know, on Zoom calls. Like, "Oh my God!" You see their expression change exactly in all kinds of ways. It's like, "What am I going to do?"

The very common reaction amongst the senior attorneys we showed it to was like, "Well, that got me retiring soon." Like, "You know, I'd have to deal with this."

And some of this was driven by GPT-4 coming out. Like, you had access to three. You had access even to two, I think. We had access. We were in a close relationship, again, with a lot of the labs, but including OpenAI. And they kept on showing us stuff kind of early on in its development. And they're like, "Well, can you build something with this for legal?" And every time we're like, "No, this sucks." Like, you know, by the time we got to three and 3.5, it was like, "Okay, well, this is plausible-sounding English and sounds kind of like a lawyer. So kudos for that. But it is just making stuff up wildly." Like, we just didn't—it's very hard to connect it to a real use case, especially in legal, where it's so important that you actually get the facts right. You can't hallucinate. You can't even, you know, make the wrong kinds of assumptions.

And we had to do a lot of work with those earlier models to even get them close to usable, and they just weren't really. I mean, like, one example along the way is when GPT-3.5 came out. The study was run, and it showed that GPT-3.5 got a tenth percentile on the bar passage, right? So like, it did better than some people actually. But the ten percent of them—

Host: Yeah, probably the ones who just filled it out randomly, basically.

Speaker: Um, when we got early GPT-4, we're like, "Let's run the study again, too." And we work with OpenAI. We're like, "We're going to confirm this. This test is not in the training set. And it wasn't a totally new test to it." And the test we ran, it did better than ninety percent of the test takers, right? So it's like a big difference.

And also, we started running some tests like, "Okay, here's four or five cases to read. Using those cases, write a memo responding to this question." And we did a lot of prompt work to get it to essentially just do it accurately, to cite the actual things in the context that we gave it, and not make things up. And we're like, "Okay, well, this is very different than what we saw before." So it's a big moment for us. And honestly, I'm not sure what the mindset was of the researchers we were working with, but almost felt like by the time we were having that meeting, it felt like one of those other meetings we'd had in the past where we were getting ready to say, like, "This is not going to work for legal. Keep on trying." And I think they saw us go through maybe some form of the existential crisis on that call that our customers did. We were like, "Oh wait, this is super, super, super different!"

I guess, you know, today we have o1. We have, you know, chain-of-thought reasoning. Um, I think a lot of people look at it as it's not merely the text itself, but also the instructions that lead up to it—you know, the workflow. But way at the beginning, nobody knew any of this stuff.

Host: How did you start? You had your sort of tests that you had written for previous versions of the model. They outperformed. But then there's this moment where you say, "Okay, well, now it's something. But what do we do next? And how do we do it?"

Speaker: So the process that we started with then—it's actually not too dissimilar to what we're doing today. It started with a question of like, "Okay, well, what problem are we trying to solve for the user, right?" The user wants to do research—legal research. And they want like a memo answering their question with citations to the original source. So like, that's the end result. And then we're like, "Well, how do we go from that end result? Like, working backwards, almost. What would it take to get there?"

And what ends up happening a lot with the things that we built for Counsel—we call them "skills," which felt very unique at the time. I think a lot of companies now call their AI capability "skills." So when you're building these skills, um, it turns out it usually takes a lot of work to go from like, say, the customer inputs something—say, like, a set of documents or a question or what have you—to the end result that they're looking for.

And the way that we thought about it was, "How would the best attorney in the world approach this problem?" So, in the case of research, for example, the best attorney would, you know, get the request from a partner. And then break that request down into like actual search queries that run against these platforms. And sometimes they use special search syntax. It looks actually probably like SQL, almost, right? So like, from the English language query, you have to break it down to these different kinds of search queries. Maybe a dozen different search queries, being really diligent. And then, um, they'd execute the search queries against these databases of law. They come back with, say, like, a hundred results each. And then, you know, the most diligent, best attorney would sit down and just read every single one of these results that come back—all the case law, statutes, regulations. And you start to do things like make notes and summarize and kind of compile like an outline of what your response might be, like, line by line or paragraph by paragraph.

Host: Actually, yeah, a hundred percent. And you start like just taking out those like insights you're getting from what you're reading.

Speaker: And then finally, based on all that work and all the citations you've gathered, etc., then finally you put together your research memo. And so we're like, "Okay, well, each one of those steps along the way—for the vast majority of them—those were impossible to accomplish with previous technology. But now they're prompts. Think step by step."

Host: Yeah, think step by step.

Speaker: Yeah, exactly. But we actually broke it down. Each one, so getting to the final result may be a dozen or two dozen different individual prompts, each of which might, by the way, be thinking step by step themselves. But um, and for each of those prompts, you know, as part of this chain of actions you take to get to the final result, we had a very clear sense of what good looks like. And we were able—you know, we had a series, like a battery of tests before. But this got way more intense. Where we'd write, at first, maybe a few dozen tests, and then a few hundred, and a few thousand, for every single one of those prompts.

So, you know, if the job to be done in the very beginning of this research process—for example, is taking the English language query and breaking it down into search queries—we had a very clear sense of what good search queries look like. And we wrote like gold standard answers for giving this input, this is what the output looks like, right?

And so our prompt engineers—and I was one of them at the very beginning—we all just kind of got in it together. We're writing these English language prompts to try to, you know, write the test first, basically. And wrote these English language prompts to try to get it so of twelve hundred times they got the right answer, twelve hundred times, or eleven ninety-nine times, or what have you.

Host: So, sort of like, um, test-driven development.

Speaker: Oh, yeah, really. Approach from doing software engineering to prompting?

Host: That's exactly right.

Speaker: And the funny thing is, I never really believed in test-driven development before prompting. Like, I was like, "The code works, it doesn't—it's fine. You'll see it when you..." But like, with prompting, actually, I think it becomes even more important because of the kind of nature of these LLMs. They might go in crazy directions unexpectedly. And so, you know, you might very easily add in a set of instructions to solve one problem you're seeing with these sets of tests, and then break something with these sets of tests. So that exact kind of theory of test development applies, you know, ten times more—I'd say—in the world of prompting.

Host: There's a lot of, uh, sort of the naysayers are saying that a lot of companies are just building GPT wrappers, and there's not a lot of IP getting built. But actually, there's a lot of finesse to how you explain all of this. Like, can you tell us about all of that and how much more there's to be built?

Speaker: Oh yeah, I mean, I think the thing is, when you're actually trying to solve a problem for a customer and actually doing the job—in our case, like, what a young associate might do—and do it really well, there are many layers of things you have to add in to actually get the job done. And by the time you like add that all up, you're not like a GPT wrapper. You're a full application that may include, in our case, proprietary datasets, like the law itself, and our annotations to the law that we added automatically. It may include connections into customer databases. In our case, in legal, they have these very specific, legal-specific document management systems. You know, so connecting into those is like very important.

Um, it may include something as subtle as like how well you OCR and like what OCR programs you use and how you set those up. When you're doing that task of, you know, one of the tasks that Counsel does, for example, is reviewing large sets of documents. Once you start working with a lot of documents, you see like stuff there—handwriting all over it, and they're like tilted in the scan. And there's this crazy thing that they do in law where they print four pages on one page to save like room. And OCR is going to read it directly across, but actually it goes, you know, one, two, three, four. So by the time you've dealt with like all the edge cases, frankly—not even before you hit the large language model—like, everything else up to the large language model—um, there might be dozens of things you build into your application to actually make it work and work well.

And then you get to the prompting piece—and writing out tests and very specific prompts, and the strategy for how you break down, you know, a big problem into step by step by step kind of thinking. Um, and how you feed in the information, how you format that information the right way. Um, all of that also becomes like, you know, your IP, and it's very hard to replicate. Very hard to build and therefore very hard to replicate. Which is all the business logic. Which is all even all the very successful SaaS companies—with very specific domain—you need very, very custom, esoteric, niche integrations, like plug into this esoteric law database.

Host: Yeah, absolutely. Two things I think about it all the time. It's like basically all SaaS for a while was just like a SQL wrapper, right? Like, if you think about like very successful companies like Salesforce, they built that business logic around basically just databases and connections between like tables in a database. And sometimes bridging that gap between um something that like either a very technical person can do but most people can't and making accessible.

Host: Or, um, bridging that gap between that "almost works"—like, you can do a lot of cool demos in ChatGPT without building a line of code—but that almost works and works, you know, 70% of the time. But going to 100% of the time is a very different kind of task. And people will pay $20 a month for the 70%, and maybe $500 or $1,000 a month for something that actually works, depending on the use case, right? So there's a lot of value gained going that last mile or 100 miles, whatever it is.

Host: Yeah, can you talk about how you went from 70% to 100%? Because I think the other knock on this technology that we hear a lot is like, "Oh, these LLMs hallucinate too much. They're not accurate enough for real-world use." But as you said earlier, like, the use case that you're working on is a mission-critical use case. There's like a lot at stake if the agent gives bad information to lawyers who are working on important court cases. How did you make it accurate enough for lawyers, who are conservative by nature, to trust this?

Jake: Test-driven development framework, first of all, goes a long way because you can start seeing, you know, patterns and why it's making a mistake. And then you add instructions against that pattern. And then sometimes it still doesn't, you know, do the right thing. And then you kind of really ask yourself, "Okay, well, was I being super clear in my instructions?" You know, am I including information? Doesn't—you know, it shouldn't see too much or too little information for it to really get the full context. And usually, like, these things are pretty intelligent. And so usually, you can kind of root cause why you're failing certain tests and then build to a place where you're actually passing those tests and just getting it right, you know?

Jake: And one of the things we learned is if it after passes frankly even like 100 tests, the odds that it will do on any random distribution of like user inputs the next 100,000 100% accurately is like very high.

Host: One of the things that strikes me that is tricky—like, many founders we work with are very tempted to just raw dog it, yeah? There's like no evals, no test-driven development. We're just like, "Vibes only," prompt engineering. And maybe—I mean, you switched over to this very quickly. Then, like, was it just obvious from the beginning? You're like, "We just can't do it that other way. We should not raw dog any of these prompts."

Jake: Yeah, I think the biggest thing first of all depends on the use case. For a lot of things that we were working on, for better or for worse, there was a right answer. And if you get the wrong answer, lawyers are not going to be happy about it. You know, I had been a lawyer myself, but also been around lawyers for a decade. And every time we made the smallest mistake in anything that we did, we heard about it immediately, right? And so I had that voice in my head, maybe as I was going through this process.

Host: Um, and that—how was the learning from the 10 years of slogging through pre-LLM? You're like, "No, it has to be 100%."

Jake: Oh, yeah. Oh, yeah. That's probably true of way more domains than we realize, actually. It could be. Um, because the other thing that we're thinking about a lot is you can lose faith in these things really quickly, right? You have one bad experience. Especially if it's your first bad—your first experience is bad, and you're like, "You know, maybe I'll check on this AI stuff a year from now," especially if you're like a busy lawyer, not a technologist. So we knew you had to make that first encounter—the first week—really, really work for the lawyer, or else they're not going to invest in it deeply.

Host: So let's talk a bit about OpenAI O1, because it is very different model. I mean, up to this point with GPT-4 and all that previous generation, the analogy in terms of the intelligence is sort of the kind of "System One" thinking—and the Daniel Kahneman type of intelligence, right? He has this whole economic theory around it, won the Nobel Prize for it. System One thinking is just very fast. It's kind of these decisions that humans make very intuitively and based on patterns. And LLMs are fantastic at that. But they're terrible at the executive function. Because what I'm hearing with all the stuff that you're describing is kind of you're just giving the LLM executive function. It's like, "How do you think? How do I manage you?" It's really that slower thinking. And I think O1 is exciting. We haven't seen things built yet because it just got announced a few days ago, right? I think it's getting to that System Two thinking. And I think this has been a big area of research, which I saw a lot in news a year ago, where a lot of the researchers were excited to unlock this because this is the missing piece to AGI. Let's talk about what are your thoughts on O1 and how this changes things.

Jake: So first of all, I think O1's a very impressive model. Um, like, with other things, we gave it the kinds of tests that we knew were failing. And the degree of—it's not just math. Degree of thoroughness, precision, intelligence applied to some of these questions. And sometimes it's the stuff that you wouldn't expect you need a super smart model to do. Like, in one of the tests that we run, we give it lawyers real legal briefs, but we edited very slightly some of the lawyer's quotations to the case to make it a wrong quotation or wrong kind of summarization of his case. So in this like 40-page legal brief, you alter things with just adding the word "like not"—can change the meaning of something entirely, right? And then we give the full text of the case as well to the AI, and we say, "Well, what did the lawyer get wrong about this case, if anything?"

Jake: And literally, every LLM before that would be like, "Nothing. It's perfectly right." And it's just not a precise thinker about some of the very nuanced things that we altered about the brief to make it slightly wrong. And then O1 gets it, like, immediately. Like, you said, like, it thinks. Actually, for a while, like, it sits there for a minute, you're like, "Is this—is this anything?" You know? But then it starts answering, and it's like, "Oh, well, you know, you changed an 'and' to a 'neither nor,' so..."

Jake: Those are the kinds of tests that you kind of expect, even frankly earlier AI, like LLMs, to be able to pass, but just could not. And all of a sudden, O1 is even doing these things that take like precise detail thinking. Obviously, we don't have the internals on how O1 really works. We have, you know, this broad idea of chain of thought seemingly. We know that if OpenAI had a giant corpus of internal monologue of people thinking through, doing things step by step, O1 would be even a lot better. It sort of rhymes with, uh, the thing you did to, you know, put your first step on the moon, right? Like, you break it down into, you know, chunks where you can get to 100% accuracy instead of just throw it all in the context window and, you know, maybe magically it will work.

Host: Yeah, do you think that's what's happening, then?

Jake: I think there's a good shot that they've had, you know, maybe changed what their contractors are doing. Instead of just doing, you know, input-in-answer-out, they were doing input-in-how-would-I-think-about-solving-this-problem, and then answer out. But then, you know, the interesting thing is then it's kind of limited by the intelligence of the people writing those instructions. And one of the things that we're investigating, for what it's worth, with O1 is: Can we prompt it to tell it what to think about during its thinking process? And inject, like, again, like we've hired some of the best lawyers in the country—how would the best lawyers in the country think about solving this problem? And maybe, you know, we have no conclusive evidence one way or the other yet that this dramatically improves things. It's so early, and just not enough time yet has passed.

Jake: There's a chance that one of the new prompting techniques with O1 is teaching it not just like how to answer the question, what examples of good answers look like, but how to think. And I think that's another like really interesting opportunity here—is injecting domain expertise or, um, just your own intelligence.

Host: I'm just so thankful because I think you're sort of sharing the breadcrumbs. And you know, there are a great many other spaces where this technology is just beginning. I mean, you go to pretty much any company, people have no concept of what's just happened, yeah? Like, they actually literally still repeat all of those sort of tired tropes of, "Oh, you better be fine-tuning," or all the—I mean, these things are just not connected to like what we're seeing day-to-day with startups and founders trying to create things for users. What I'm kind of glad for is that we get to actually share this news, like this knowledge. Because like, even the things we talked about—you know, "Hey, you should probably do evals"—like, there's a lot of alpha in getting to 100%, not just 70%. These are sort of the breadcrumbs that will actually go on to create all of the billion-dollar companies—maybe thousands of them, actually. We hope so.

Host: I mean, I think that you're about to start to see a lot of other fields like law really level up when you don't have to spend, you know, millions of dollars in six months literally in a basement reading document by document by document, right? When you actually can just get past that and get just the results, and now you're thinking strategically and intelligently. And the unlock for these companies—I mean, they currently pay, again, millions of dollars in salaries for these jobs to be done. Each of them, right? So for any company to come out with an AI that can do even a percentage of that, the value is like really there. And I just want to encourage people to not kind of give up based on those tropes, right? Like, "Oh, it hallucinates too much. It's too inaccurate." Whatever. There's—for an example of anything, it's like there's a path, and you can do it. And there's some good news in that, you know? What the jobs aren't going to go away—they'll just be more interesting. That's what I think.

Host: Yeah, well, with that, we're out of time. But Jake, thank you so much for being with us.

Jake: Thanks for having me. See you guys next time.
