---
title: "How To Train An LLM with Anthropic's Head of Pretraining"
slug: "Mw-how-to-train-an-llm-with-anthropic-s-head-of-pretraining"
media_type: "Video"
author: "Y Combinator"
speakers: ["Host", "Nick Joseph", "Speaker"]
categories: []
description: "YC's Ankit Gupta sits down with Nick Joseph, Anthropic's Head of Pre-training, to explore the engineering challenges behind training Claude—from managing thousands of GPUs and debugging cursed bugs to balancing compute between pre-training and RL."
url: "https://ycombinator.com/library/Mw-how-to-train-an-llm-with-anthropic-s-head-of-pretraining"
youtube_id: "YFeb3yAxtjE"
youtube_url: "https://www.youtube.com/watch?v=YFeb3yAxtjE"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# How To Train An LLM with Anthropic's Head of Pretraining

Ever wonder what it actually takes to train a frontier AI model?

Ankit Gupta, YC General Partner, sits down with Nick Joseph, Anthropic's Head of Pre-training, to explore the
engineering challenges behind training Claude—from managing thousands of GPUs and debugging cursed bugs to balancing
compute between pre-training and RL. We cover scaling laws, data strategies, team composition, and why the hardest
problems in AI are often infrastructure problems, not ML problems.

## Transcript

Host: Hey guys, I'm thrilled to be joined today by Nick Joseph, the head of pre-training at Anthropic. To give viewers a high-level sense of what we'll be covering, we're going to start with the basics of what pre-training is and then dig into how Nick thinks about strategy, data, alignment, and infrastructure at Anthropic. And by the end, you'll hopefully have a sense for how progress in AI comes directly from advances in pre-training. I would love to talk a little bit about your backstory and kind of how you got to this point. Where did you work before Anthropic? And what were your takeaways from those places?

Nick Joseph: Yeah. So let's see. I was at Vicarius, uh, and then at OpenAI before Anthropic. So Vicarius was originally an AI lab, and sort of when I joined they were making a shift to product, particularly working on robotics products. And the thing I worked on was training computer vision models for their robotics products. It was my first job. So I think I just learned a ton about how to do machine learning models, how to write machine learning infrastructure.

Host: And at the time were you also thinking about a career as an academic? Like, at the time a lot of people doing AI work were in PhDs. That's kind of what I was thinking about before I started to do a company. Like, how were you thinking about that in your headspace?

Nick Joseph: Yeah. So, like, I'm actually going to rewind a little bit. I think a lot of my thinking on this had come from an internship I did at GiveWell, which is a nonprofit that evaluates charities. And some people there were like, "Ah, we're at some point we might have AGI. It could be dangerous. We should worry about these risks. This could be a big impact on humanity."

And I was like, not super convinced at the time, and went down the economics route and was going to try to work on directly helping people in poverty. That didn't work out for various reasons, and ended up being like, "Okay, I'll at least work on AI. Either the safety thing will turn out to be important, I'll work on that, or it won't be and I'll just make cool things with AI that can probably help people in poverty more."

I wasn't really coming at it from an academic standpoint. I was sort of like, in fact, when I switched to that, it was part of the appeal was that I could immediately go do stuff in AI, whereas if I wanted to work in economic policy, I'd have to wait, I don't know, six years to do a PhD and start, and like, totally—it's a longer path.

Host: And what was the state of AI safety work at that time even look like? Like, who are the people who were thinking about that kind of stuff? I mean, there were some folks at Vicarious thinking about this kind of thing, but it was fundamentally a robotics company. And so, yeah, how were you thinking about that at the time?

Nick Joseph: Yeah. So my sense was, like, at the time a lot of the AI safety discussion was kind of theoretical. Like, the models weren't actually that good. They weren't really posing these dangers. So it was a lot more like philosophical, like, "Oh, at some point we might get AI that's really smart, smarter than humans, and like, should we wait?" This was a future concern—how should we compare that to near-term things? And I think that was actually just a less compelling argument. I think it was an interesting one and sort of made you think about it.

Host: So next you went to OpenAI. What was OpenAI like at this time?

Nick Joseph: Yeah. So I was at OpenAI. I was on one of the safety teams and kind of worked on—I ended up working on code models actually. And kind of when I got there, the first thing I saw was, oh, they'd fine-tuned GPT-3 to write some code, and it was really good. And I was like, "Oh, okay, if you're worried about AI getting really powerful, writing its own code—that seems like it could self-improve. How likely is that to happen?" So I was doing a bunch of evaluations and studies of what contributed.

And then after, like, eight months, basically everyone I worked with—all the safety leads—left, which, uh, yeah, invited me to go to Anthropic. And that was sort of the reason I joined OpenAI in the first place—because I cared about AI safety and wanted to work with them. So then I went with them to join Anthropic pretty much right when it started.

Host: With that, why don't we transition a bit? These days you run the pre-training team specifically at Anthropic. Um, obviously you've been working on pre-training at Anthropic for quite a bit of time, and I'm sure it's evolved over the years in terms of what that even entails and looks like. Why don't we start by just talking a little bit about what pre-training is like? How does it even fit into the way of thinking about how AI models have developed at a place like Anthropic? And what exactly do you guys do?

Nick Joseph: We know that one of the ingredients to making AI models better is scale. You want to put a lot of compute in. And if you sort of step back and you're like, "Okay, what's the way we could put the most compute into a model possible?" We need some objective that there's just like tons of data for. And one idea here is the internet. The internet is massive. It's probably the biggest single source of data humanity has created. And you don't have labels. It's like, you don't want someone to have to go in and read the entire internet and say something about it. So you want to get labels out of the data itself.

And the idea here is we can take some text and we can predict the next word. So you take, you know, as the first word, you predict the second word. Then you say "the cat" and you predict the word after that. And this means you get very dense signal. Every word is like a new example. And there's a huge amount of data. And one of the findings from GPT-1, GPT-2 was kind of, as you throw more compute at this, more data, bigger models, you get better. You get smarter models, essentially.

Host: Totally.

Nick Joseph: Um, and that's kind of been the central thesis of pre-training for the whole time. Uh, there's this idea of scaling laws, which is that you can actually quantify, like, as you put in more compute, more data, more parameters, you get models in a very—you get a lower loss, a better prediction of the next word—in a very predictable way. And I think you can somewhat foresee from that original paper, and I think like Dario did foresee this—I think many people did—but wasn't obvious was that once you have that, there's this positive feedback loop where you can train a model, you can use it to make something useful and sell that, and get more money, use that to buy more compute, and then you actually train a better model. And we've sort of run that cycle over and over again over the past five years or so.

Host: Well, in thinking about that objective to begin with, you know, I think the way I think about the state of pre-training is, yeah, it seems like this next word prediction, at least from the external standpoint, seems to be the dominant way pre-training happens. But if I rewind the clock to that era of 2017 to 2020 or 2021, and even after, there was all sorts of pre-training objectives people were considering, right? There were these BERT and BART models that were doing masked language modeling. It seems like this GPT series of models, doing autoregressive modeling as you describe—this next word prediction—seems to be the dominant one that won out. Do you have any reflections on that time period? Like, were you guys trying all of them and kind of this one worked, or is there some sort of first principles reason why this is like the right one that should have worked?

Nick Joseph: I think the answer is like it's mostly empirical. In terms of how to think of the things, I'd be like, yeah, it's empirical—just try them all, see what works. One big advantage for this autoregressive setup is that you can just sample from it to generate text afterwards in a fairly straightforward way. That comes and enables a product use very nicely.

Um, like, one thing that you want is, like, one characteristic is like a loss. Whereas you drive down the loss, that actually is the thing you care about. And you can think of it as, like, if you got to perfect on language modeling, you now can write text as a human. You can sort of imagine you put in the title of a paper and it should spit out the entire—spit out a novel paper. Whereas I think some of the other approaches don't quite have that flavor.

Host: Yeah, totally. Yeah, it makes sense that in terms of that loop you're describing—of, you know, then release something that gets you revenue and you can use that to buy more compute and iterate—this sort of gives you the most natural way to actually do that flow because you can keep releasing new products and keep getting the revenue from that to invest in more compute and so on.

Nick Joseph: Yeah, it certainly gives you the most open-ended thing. You could imagine, you know, you like train something as a class—like, you train some base thing, you fine-tune it for a bunch of particular tasks. One approach people would use, they would do this big pre-training and then they wouldn't just like open-endedly sample from it. You'd fine-tune it on like a hundred specific tasks and that could work too. I think that like the one sort of general intuition I have is like compute is the thing that matters. So like I think if you throw enough compute at any of these objectives, you're going to get something that's probably pretty good and can kind of be fine-tuned to other things. And it's surprising how little these details matter compared to throwing more compute.

Host: When you think about actually throwing more compute, there's a whole bunch of axes by which you could throw compute at it too, right? And if you have a specific model architecture you're training over, you can basically throw more data at that specific architecture. For a particular one, you could add more layers or make the models larger in it. You could do some kind of neural architecture search over lots of different variants. And I assume that these days it's somewhat more figured out, you know, which architecture you go for. I assume the earlier days it was somewhat less so. And I'm curious if you could speak to how you guys thought about that, like, what did your infrastructure even look like to do that type of determination?

Nick Joseph: I mean, I think the short answer is it's hard, right? Like, what you're really doing is you're going to train this one big expensive model, and you have a space of—you know, you can sort of call all these things hyperparameters. You know, how many layers do you have? What's your width? Like, you have the space of hundreds of hyperparameters, and you want them all to be optimal. And you're sort of striking this balance actually between how much do they matter—like, can you just take your best guess and throw more compute at it in whatever way you want and basically it doesn't matter—versus how much you want to get it precisely correct.

Host: Interesting.

Nick Joseph: And I think one of the like interesting things is like it actually doesn't matter that much. Like, we—I think this was in one of the early scaling laws papers—like, you can change these things and get little wins, but like, as you throw more compute, it sort of reliably gets better. If you mess up enough, you will stop seeing that happen and you won't have any way to know which is one of that—that's like kind of the hardest part in some ways.

Host: You don't know the counterfactual basically, because you didn't run it for long enough to actually know what it is.

Nick Joseph: Yeah. We have these scaling laws. So you can sort of say, like, as you train more, compute, you expect the loss to go down as a power law. It's really a power law plus constant. So what eventually will happen is you'll curve off that power law, and then you know something is wrong. And is it fundamental? Is it like you've hit the limits of scaling, or is it, "Nope, you should have tweaked your learning rate slightly differently?" And that's sort of one of the challenges in terms of how to figure it out. You can—the usual paradigm is like, test things out at small scale before running them at large scale and try to find—

Host: Small scale in terms of data or in terms of something else?

Nick Joseph: Uh, in terms of everything. Like, you kind of want to scale things down like proportionally. So you want to say, like, you want to have some theory for, like, how you're going to scale up—like, "Ah, okay, if I get ten times as many FLOPs, how much of it goes into layers, how much of it goes into data, how much of it goes into attention?"—and you sort of get that theory and then test that it's optimal a bunch with like scaling everything down proportionally.

Host: And and just so I can think about what this actually looks like in those in those early days of Anthropic, you know, you're a team of like ten or something like that in those very early days, or twelve maybe. What actually is your ability to use large-scale infrastructure as like a relatively nimble startup at that time—I mean, a startup that was well-capitalized but still not actually that many people working at? What kind of infrastructure did you have access to to train these early models at the time?

Nick Joseph: So actually, one of the wild things was—it at least I mean, you don't know what anyone else is doing, of course—but it kind of felt like we were at the frontier of it, and there just weren't that many people who cared. Like, I was sort of coming, you know, I was coming at it from like, "We're making AGI, this is the most important technology ever," and then would kind of like look around and be like, "And it seems like I'm one of thirty people who were working on this in like the world." I mean, I was kind of a junior person. Everyone else sort of knew how to do this and had done it before, but I was kind of surprised at how easy it was. Um, like, the public estimates for GPT-3, I remember, were that it cost five million dollars to train. Which, you're like, on the one hand, five million is kind of a lot, but it's like a lot for an individual person. It's not really a lot from like a company perspective. So we could totally buy like compute that was enough to train models like that, you could—

Host: And were you using a cloud provider, or did you have a custom setup somewhere, or did you literally have racks in a room somewhere that you were, you know, bought a bunch of Nvidia GPUs and you were doing it?

Nick Joseph: Uh, we're using a cloud provider, but I think it's kind of not actually that different because one of the things that was surprising to me is you actually have to understand the literal layout. Like, uh, I remember at one point one of my coworkers running a clustering algorithm to identify what rooms all the chips were in since we had a hypothesis that they were in different rooms and that was causing, or, you know, different buildup, some sort of network latency. And you can kind of figure it out. You could like reverse-engineer, like, "Ah, okay, yeah, there's clearly like two clusters here that are connected better, and there's some issue on the connection between them." Like, we're trying to push the limits of the hardware like as much as possible. Um, particularly at the beginning when we were kind of like, "We have way less funding than everyone else, we have to," and most people weren't very efficient with the compute, so we were like, "Ah, we get a big lead by being really efficient at how we use"—

Nick Joseph: Could you talk a little bit about some of the things you guys did in those early days for how to get the most out of the hardware? I think it's really interesting. Like, I think back to the days of the early days of Google, for example, where there's these cases where they basically bought relatively cheap consumer chips and then they optimized the software to make it so you can actually get the most bang for your buck out of them. And that's how they had all this high latency or low latency, high availability stuff. I'm kind of curious if there's some analog in the early AI era to that.

Speaker: I think for us it was largely about getting the distributed framework right. So, like, we're training on—in order to train, you have to train them on a large number of chips.

Nick Joseph: And there's a bunch of different approaches to how to do this. There's like data parallelism and there's pipelining, there's upsharding, and like getting all of the—at the time there were no like great open source packages you could just grab and use that just worked for this. I mean, today there's somewhat more of these, but at the time I assume there was literally none.

Speaker: There were some. Like, I actually remember that we were working on data parallelism early on and someone was like, "And now we write the all-reduce it." I was like, "We really do this ourselves? Don't like package?" And this was kind of like, "Well, we're going to want to modify it, right? Like, oh, like, we don't want to outsource this to some package because a) we're about to go to a bigger scale. Like, PyTorch, they had a package for doing this, but we were going to go to a bigger scale than Facebook had been to."

Nick Joseph: And you don't want to have a dependency on a package that you're going to have to be like constantly modifying, essentially.

Speaker: That's it. It's such a counterintuitive sentence there too. Like, we're going to a bigger scale than Facebook will. Because at the time, Facebook AI Research was considered one of the best places to do machine learning research. Like, FAIR was one of the places. FAIR and DeepMind were hiring lots of people out of PhD programs and doing lots of things. Like, what was your headspace when you were like, "Okay, this very established lab with great people and whatnot, we are operating on a scale that is not relevant to them." Like, was that natural and obvious to you, or were there times where you kind of doubted the decisions you were making in that situation?

Speaker: I think it was surprising. I will say, maybe I'm just too arrogant or something, but I kind of looked around and was like, "What are these people doing? They're all missing the big picture here." Like, I think the scaling laws were pretty clear, and the arguments against, I just thought were kind of nonsensical. Like, you know, the scaling—I think the original scaling laws paper had like 11 orders of magnitude, and there was like this intense debate on whether it would continue for like another point. And I was like—it seems like one over 11 is maybe your chance it fails here. And then, like, you know, sometimes it doesn't work. Like, sometimes it just works straightforward. You like train the model, you're like, "Oh yeah, of course." But yeah, I do think that it was maybe felt obvious when you're in that headspace and you're working on this all the time and you're making those plots. And I think these things feel pretty different when you're on the outside. You know, there's a huge space of papers. Everyone tries to make their paper sound like very robust and important. I could see being like, "Oh yeah, this is not really a thing."

Nick Joseph: Totally.

Speaker: But also, different labs had different cultures. So like, I think one of the things at FAIR was it was a very—more PhD style, independent research. People have their own ideas, pursue those.

Nick Joseph: You're fighting for your compute and so on.

Speaker: Yeah. And to do a project like training a large language model requires a lot of people to collaborate on like a really complicated piece of infrastructure that isn't going to be a paper, right? Like, you're not going to publish like, "Oh, I got a slightly—I got 5% more efficiency."

Nick Joseph: Totally.

Speaker: Than the next one. And it's not respected in like those cultures necessarily. So that might have been part of it.

Nick Joseph: Okay, okay. So then when you actually implement these models, you're saying you're using a level of low-level programming where you know you're using libraries like PyTorch, but you're perhaps not using everything right out of the box from PyTorch because there's things you guys want to customize that are at the level of basically one level of abstraction below them, but not necessarily at the level of abstraction of, you know, writing custom CUDA kernels or—or like, was that also in the space where you guys were thinking about?

Speaker: So it depends on like the operation. So like, I think I was mostly operating at the level of like torch.matmul. You know, like, uh, yes, where does a matmul go, but not thinking like, how do you make the matmul efficient? Like, I assume Torch figured out how to make a matmul as efficient as is possible. But there are some pieces like attention where there was just kind of a lot of different variants, and attention is really complicated and hard to make efficient on a GPU. And those things you have to kind of go more levels down on the stack. Uh, I think there was like a process that is maybe interesting that I'd never really like thought of before—of like how to do it, which is sort of like modeling out the—the thing you're going to do, coming up with a strategy for how to parallelize it, that like can get to a really good efficiency. You know, like—

Nick Joseph: So you're thinking about MFU basically, like your utilization on your GPU. So there's like a goal utilization you're trying to get at and a strategy to get there. You're saying—

Speaker: Yeah, and I think like one of the things you can do is you can actually like pencil and paper math out what efficiency you're going to be able to get to, right? You know all the constraints. It's MFU and is flops utilization, but like the reason you don't get good MFU is you end up limited on HBM bandwidth. You end up limited on, I don't know, as host-to-like CPU offload. There's a bunch of different pieces, but there's not that many pieces. There's like six relevant numbers there. So you can totally model it out, understand what the constraints are, and then implement something that can get there. Of course, it will be really inefficient when you implement it. And then the next step is like pulling out a profiler. So you want to be able to profile the job, look how long every operation takes, have a model in your mind of how long every operation should take, and then make those two things the same.

Nick Joseph: And and were there good out-of-the-box profilers you could use at that time? Or did you guys have—you know, because people weren't operating on the kind of network topologies you guys may have been using. Did you have to write your own profilers basically to do this type of, you know, multi-node optimization?

Speaker: Yeah, it depends when. I'm actually getting better with time. The PyTorch profiler was like pretty good actually throughout for a single GPU. If you want to like profile a GPU, the PyTorch profiler would work. But if you wanted to profile a job on hundreds, thousands of GPUs, that like hadn't really been done much. And then that was kind of more of us like hacking into the profiler to figure out how to combine all the traces together.

Nick Joseph: And then one more question on that earlier is, you know, you had mentioned, you know, you hadn't really done a lot of this work before—maybe some time at OpenAI and those early days in Anthropic. How did you actually go learn all this stuff? Like, what was your process for learning about those six things that were relevant to bandwidth limitations and whatnot?

Speaker: I mean, so when I joined Anthropic, one really nice thing was there just wasn't that much. I think my first day I read through our entire—all of Slack and the entire like internal database and learned a bunch from that. Like, it was kind of nice to just be like, "Everything is relevant to me." And then I mostly learned from pair programming. Like, uh, Tom Brown had done all this before. So he kind of like knew all the stuff quite well. Sam McLish, my manager, had also done a lot of it before, and I just like paired with them a huge amount at the beginning. And I think one of the things I really like about pairing as a way of learning is you learn the like thing you're trying to do. Like, you will learn that like if you're pairing with someone better than you, they can just do it. So you're mostly just watching them. But you also learn how people do it. So something like how to use a profiler is not something you would ever learn from seeing someone's like final write-up on Slack in their PR. You would just be like, "Oh, they found these, they changed this specific line, and it's a win." They—like, you need to watch like a YouTube video for four hours of someone messing around with a profiler, or maybe self-teach it or something, or to actually pair with someone—is basically the best you can do.

Nick Joseph: I think there was like one thing that I think is embarrassing now that I look back—is I'd never actually used a debugger before joining Anthropic. People talk about it, PDB, and like, yeah, that's a thing people use, but print seems fine for me.

Speaker: Then I like watch—like, "Oh, no, a debugger is a super useful tool. This person's way faster at debugging things," particularly if it takes a long time to start up the code, which they can. And, yeah, learn learning that sort of thing I think comes best from pairing. And then there's of course the obvious—you just learn by doing. You know, I eventually did like spit up profile and stare at it for many, many hours.

Nick Joseph: Totally. Yeah, exactly, yeah. Okay, so so then that was sort of the very early era. Over time, obviously pre-training has become bigger and bigger as you're describing, scaling. I imagine you're using many x more GPUs, much more compute over time. I'd be really curious to hear first at a high level, what do you feel has changed about the pre-training strategy that you could talk about? Obviously there's more compute, but what does that actually mean to have more compute in terms of what you think about differently from those early days versus now?

Speaker: I'm sure the things that haven't changed, 'cause I think it is like shocking how in some ways—I think I'm still pushing down the exact same metric that I was on like day one. Like there's like some loss function. Loss go down. And I think you could like look at some—you could probably run the original, the first model I trained on the same metric and just like make a plot of like progress of team over over time. Uh, so that's all the same. I think the—

Nick Joseph: One OKR is like one thing that matters basically.

Speaker: Yeah, totally.

Nick Joseph: And like I mean talking about like OKRs it's very—sized company, you're like, "Oh, should you do OKRs?" and it's always felt a little bit funny for uh a team like where I'm like, "Sure, I can just pick a loss value but like the answer is like as low as possible. We will continue to work on that forever."

Speaker: I think the biggest things that have changed has been a little more specialization. Like I think at the beginning, I mean the first like three or six months, I tried to read every PR in the codebase and that was great. I knew all the pieces, etc. And as you grow, it's kind of everything gets like a little more precise. You know, people really dial in exactly how attention should work, let's say, or you know, really dial in like uh the parallelism strategy. And you end up with a team where it's a bunch of people who are like deep experts on individual things, which is great because it means you can go really deep on those things. But sometimes you—at least for me as a manager—one of the things you sometimes have to think about is like making sure the bigger picture makes sense and also that you have enough people who actually do understand the whole bigger picture that there's no like single point of failure.

Nick Joseph: Yeah, it's interesting you you frame it in that with that trade-off, right? Because as as you were describing that I was trying to think, you know, is this a bug or a feature? Like there there's some obvious features of it, which is you get expertise and you can optimize certain things. But I imagine your ability to take bigger swings becomes more complicated if not everyone's exactly pointed in the same direction. Like, how do you wrestle with that now?

Speaker: Yeah, I think I mostly just try to get a balance of people. I think one of the challenges early—

Nick Joseph: People, oh, that's interesting.

Speaker: Yeah, like I think people really do have a preference here. Has been one of the things I've seen. Like there are people who really want to be a generalist and understand everything and like lightly touch on things. There people who want to like—

Nick Joseph: Pick an area, often they've already picked that area and they're like deep experts in precision. You know, they started, they did a whole PhD in precision and just want to think about that—

Speaker: And you want to get some balance of that. I think early there was a phase where we'd hired a lot of people who are more generalist-shaped because that's what the people who joined—totally early startup where they go work on everything. And then—

Nick Joseph: You ended up with kind of everyone doing everything and no one really really deeply understanding one thing.

Speaker: Uh, and that's one failure mode. But I think if you get too many people who are specialists—

Nick Joseph: You end up with a lot of effort has to come from the manager, from like the lead, to connect everything—

Speaker: And to notice something like, "Ah, if we change the architecture here, that would make this like efficiency consideration over there way easier."

Nick Joseph: Um, one of the things I really liked kind of like at the very beginning was like, let's work on efficiency, but I could just go and like be like, "Ah, well what if we change the way we do like this particular step?" And we'll be like, "Oh yeah, that's probably fine. Like, easy change." And then like you can avoid—did this whole complicated project to make this operation that was hard efficient because you can make an easier operation efficient.

Speaker: Okay, interesting. Yeah. So, as the level of compute has also gotten bigger.

Nick Joseph: So, I'm I'm sure anyone can imagine, okay, there's more GPUs now, you have to network them more. Are there some like kind of non-obvious challenges that have arisen over time where you guys have just like banged your head against the wall to solve them because of the amount of compute you're dealing with that people wouldn't otherwise know about that like you want to share? I think that connecting them is one that's maybe interesting and like surprisingly hard.

Speaker: Okay, because you really do get more and more chips connected and—like one thing that I think is like the the standard way people parallelize chips isn't—um, the whole thing is one failure domain. Like one chip fails, the whole thing can crash.

Nick Joseph: And—the standard way as in the standard way people doing AI? Or the standard way in in other fields where people are doing—

Speaker: Uh, in AI, for like, I mean, at least like I think at the beginning, you know, first versions of things were this way. And—so it's like you have a 100 GPU cluster or whatever, is 128, like if one of them dies, job fails basically.

Nick Joseph: Yeah, I mean you—the simplest thing is if you just like distribute your model. So say you put like every layer on a different chip and you lose like layer seven, like—

Speaker: Yeah, you're not going to like skip layer seven. I guess you could, but that's like a pretty weird—

Speaker: Model training process now and like that leads to some interesting things which is like okay so now as you scale up you have more and more chips and the failure rate can get like larger and larger.

Host: On the other hand you can like I don't know you can like restart pretty quickly there. There's nothing like you just have to like load back in some ways. So that was one thing. And then the thing was like the level of novelty at the whole stack is something that's surprising. Like basically everything from like how the chips are laid out in the data center to the chips themselves is pretty new. Like there just haven't been that many generations of GPUs. I think one of the things that I don't know when I learned computer science my code wouldn't work and I'd be like oh the computer's broken. I think my teacher was like the you can trust the computer's not broken like you messed up.

Speaker: It's you messed up. And I think one of the most frustrating things I encountered in AI early on was working on something and being like, I don't know what I'm doing wrong. I'm just totally stumped. And uh my manager looked at it and was like, uh yeah, probably the computer's wrong.

Host: And I was like, that seems unlikely. And sure enough, the computer was wrong. Turned out that like the GPU was broken and uh we had to pull in a new one. But you have to like think like having to think about that like the GPU could be wrong, the GPU could be slow, like these sorts of issues. Uh the power supply in the data center could be broken. There's so much more like level of depth than you like kind of expect to need as a Python programmer.

Host: And just to visualize it like in those early days, I assume you guys were using the number of GPUs. It's probably on the order of tens to hundreds or something like that per run. It's probably not tens of thousands or hundreds of thousands per run or what was the rough size you guys were at?

Speaker: Those are very early days on the order of thousands. Like would they fit in this room?

Host: Thousands.

Speaker: Yeah, thousands. So like you could have a bunch of racks and you could fit them into like one room. I assume these days it's basically like a building for for one of these runs.

Host: Yeah. Now I think it's like you know huge huge campuses. At the time it was like kind of unclear. It was like oh I think like we were like you know do we need them all in one room? Can we be spread across multiple rooms? Like uh and you know we had these theoretical models you be like we need this much bandwidth from point A to point B. But you like you never know how far down you have to go like oh but like how much power do we need? Like what if there's like a single capacitor that's like handling all of them and we like turn on the whole job at once. Like does that crash things?

Host: Yeah. And so do you have to think about differences in the different types of chips? You guys work with all sorts of different cloud providers. From your standpoint, are these just sources of compute or if you guys are using TPU versus GPU, are these, you know, Google TPU versus Nvidia GPU? Do you actually have to think as an engineer differently about what it means to train on these two?

Speaker: Yeah. So, I mean, fundamentally, they're all they're all doing the same thing, right? They're all computing the same operations, matrix multiplications, etc. The way they do it is pretty different, and the way that you program them is is pretty different. Uh and then also the actual specs uh end up pretty different. You know, some some might have like a lot of flops and not very much memory or they might have a lot of memory bandwidth but not very much memory. So I think a lot of having multiple chips is like great in some ways. It means you can actually like take the job and put it on the chip that it works best on and that's

Host: like are there certain types of jobs that would work better on like a TPU cluster versus an Nvidia GPU cluster? Like how would you talk about that? Oh, interesting. Can you talk about that?

Speaker: Yeah. Yeah. I think like one example is like inference as a workload in general tends to require more HBM bandwidth. You you end up doing you sort of the simplest form of sampling since you're going one at a time you have to load all the weights for every token and that means you might want a lot of HBM bandwidth. Uh pre-training actually is often more flops intensive because you have larger batch sizes essentially.

Host: Um so yes you can sort of specialize which chips you use for which purposes. The downside of having multiple chips is that you have to write the thing multiple times. uh you in theory you could have abstractions across them but they're they're different enough that it's pretty hard to do that. So you can sort of end up if you do all the workloads on all the chips you end up multiplying your work work by the number of chips you have.

Host: Yeah. On your on your point about sometimes the computer just breaks. I definitely remember you giving me an anecdote of uh my company at the time was doing something with Google TPUs and I was telling you something some anecdote about how we were having some esoteric seg error and you were like you told me something to the effect of like you should have used them six months ago before we helped them fix like half of the problems they had on those TPUs. And so I can imagine how you guys deal with a lot of especially with these very new chips like lots of problems that arise that you guys kind of like worked closely with the providers to fix.

Speaker: Yeah, the providers are like pretty great about fixing things. I think it's like interesting to figure out the right way to do that form of collaboration cuz like they have a strong incentive to fix them, right? Like they they want the chips to work well for us. They want to sell us more chips in the future. We obviously have a very strong incentive for the chips to work cuz we like buy them long in advance, you know, like everything's riding on getting these clusters to work.

Host: Totally. Um but we don't have like necessarily totally shared you know like all information sort of can't be shared across. So yeah one of the like one strategy that's been interesting is like making these sort of small scale reproducers. So like when you get a problem you know like usually what we're doing is we're training some giant run and we get like a seg fault for let's say and we're like ah okay like hi you know we got a seg fault on your cluster and they're like I don't know how to fix that. So you have to kind of be able to like pull it out of your codebase and be able to like reproduce the issue but on like a single chip on like a single file you can send over in order for

Host: And so you guys are like literally like you're on a shared Slack with them or something and you're sending them things back and forth or are they basically living in your office and you're living in their offices and you're kind of closely more closely tied to the big providers.

Speaker: Mostly shared Slack occasionally it's better to meet in person but I think Slack is a pretty common way people communicate on things.

Host: Nice. Okay. Well, why don't we talk a little bit about how you think about the state of pre-training itself these days? In the last couple years, it seems like the focus on pre-training has now gone somewhat split at a lot of companies, at least from the outside from a simultaneous focus on pre-training and post-training where people are doing reinforcement learning or clever fine-tuning and lots of other sort of uh safety adjustments and whatnot and the post-training side and pre-training has focused at least seems like in the public imagination has been less of a focus compared to these reasoning style models that are it looks like a function mostly of post-training. I would say one from your standpoint is that the right way to think about this or in this era of kind of reasoning and new types of post-training methods are there things you think about differently or that are relevant even at pre-training that become part of how you actually achieve these really great models.

Speaker: Yeah. So I think yeah there sort of used to be this idea of like I mean it's funny because the original name pre-training implies that like a small thing you're going to do this big training thing and that like and there was there was actually one shift already which was like no you just do a lot of pre-training like you use most of your computing the dominant uh thing for a while and yeah I think like now people are like oh no you can get pretty big wins from RL sort of another set of scaling laws is like you put more and more compute into RL you can get better and better models out of that and yeah so there's a question of like how do you balance those two how much do you do of and how do they stack, right? Like is it the case that like one subsumes the other that you want to do both and they multiply? Those sorts of questions. I think those are all kind of like early stages and not not yet answered.

Host: Yeah. And and do you think about those as largely empirical questions like we talked about earlier? Is it you kind of will try a bunch of things and see what works or is there some first principles way to kind of figure that out?

Speaker: I think it's pretty empirical in the end. I think almost everything kind of has to be done empirically. Like you can kind of like come up with theories, but in practice like

Host: the first thing you're going to do with your theory is test it and most of most of the time you'll have gotten it wrong. So you you should just gather data and see. I think one thing that's important is like actually resolving things empirically is really like critical for making good decisions. And I think it's actually pretty hard to do at organizations, you know, like one thing that I think is important is to like not have like I don't I manage pre-training. I shouldn't be like oh pre-training has to win like that.

Host: I was going to ask is there some competition to some degree between these two sides of the org or do they see themselves as two pieces of the same I mean obviously they are of the same thing but yeah kind of curious how that actually plays out.

Speaker: Yeah, I think we managed to avoid this and it's pretty collaborative like we're basically all producing one model and kind of can but I I do think at other places there's been some from what I've heard there's some amount of like uh friction between between the teams and I think it's a it's an interesting like org design question of like how do you set this up so you don't have like scientific questions that you want to be that are sort of uh also tied to people's like conception of their their team.

Host: So on pre-training itself, you know, one of the things I think about is or I've been thinking about is around the availability of high quality data for people like you guys. I mean at this point you've trained on I assume all the text on the internet basically there's all sorts of other domains where you probably could extract more pre-training data but at least there's this narrative I see you know on Twitter or whatever where it's like okay we're kind of out of data for for pre-training. Is that how you see it or how do you think about the availability of data especially when a lot of data on the internet is being generated by AI like is there some kind of you know mode collapse risk where you know we kind of we overfit to data by training it on data that came out of AI itself or is that sort of not the right way to think about this?

Speaker: I think there's a funny thing where I feel like on data I see so many really confident takes on we're out of internet like this point scaling has ended and I'm almost a little bit like unsure exactly how much data people are using. I think there's like a lot to think about there. You know, there's always going to be a quality quantity trade-off, etc.

Host: But there's a fundamental point that like there is so much data. It's growing at a slower rate than we're getting more compute. Uh oh, so that's okay. That's an interesting point in itself. I was going to ask like there is new data being added to the internet, but yeah, you're also adding more compute. It's not it wouldn't actually have been obvious to me which of those two is growing faster.

Speaker: Yeah. And actually, I want to copy that. I don't think I want to state that so confidently. I'm not totally sure. Like how would you know? I mean one thing that I think is interesting is if you ask someone how big is the internet uh the answer is infinite. There are many pages where you can scroll and it will autogenerate more text as you go forever. So the internet's like infinite and then it's like okay how big is like the useful internet and then there's a thing of no one knows like interesting there isn't it's not like when you make a web page you like add it to some giant counter and like say I've added 50 words to the internet today.

Host: So there there is a lot of uncertainty on that angle. Um well like to be fair like my kind of simplistic CS brain would be like well you just you know do page rank on the internet and everything would page rank above some threshold is considered the useful internet and like that's kind of good enough like is that kind of not good enough for finding the useful internet?

Speaker: I think not I think the useful internet's pretty different from a model from a person perspective if that makes sense like I think there are plenty of things that like might not be worth you ever reading and would get to actually page rank super I think page rank is mostly like how much people it's like the link based system right it's like the original Google algorithm of like links and and like which which links get touched the most basically.

Host: Yeah, I think it's like it's a quality metric. It's it's not obvious to me that it's the right quality metric for AI, right? Like markup chain over links doesn't necessarily mean that there's not useful data there just might mean that nothing linked to it and Yeah. Okay. Interesting.

Host: And it might be that like that data ends up more valuable because you everything that's linked to a lot you've already got. Like at some point you're maybe like going for the tails, right? You're going for the stuff that uh no one's ever like, you know, it's only been linked in one place, but it's this like useful little nugget of knowledge that's going to help with like, you know, the last 10% of of hard queries. The other thing you asked about is synthetic data, and I think that one's like pretty interesting to think about. I think there's a few different ways you can think about it. Like one is sort of this like more distillation type approach where you can you can take a smart model, you can generate a bunch of data from it and you can train on that data and you you can probably get some model that will like kind of approach the intelligence of that.

Speaker: Yeah. And we see this with a lot of the open source models, right? We see like the Qwen smaller reasoning models distilled off of the larger Qwen models for example and similar with Deepseek for example.

Host: Yeah. So you can totally do that. Then there's a separate question of like can you use your current models to train a model that's better? And I think there's like an interesting thing here which is like if you generate the model data for the models you know if I go to Claude and I'm like write me some great text. Yeah. And I look at it and I look at like the

Host: Average content on the internet looks pretty good.

Speaker: But on the other hand, I know that if I just train, just create, generate—you know, "please write me as much text as possible"—theoretically I shouldn't be able to train a better model than that. Like I'm just going to get the same thing out.

Host: Uh, so yeah, presumably, yeah. I mean, specifically, that's because like your next token prediction on that should have very little loss for anything that's coming out of your model, right? That's like the basic reason why we would expect that to not work that well.

Speaker: It's mostly just because there's some distribution. The model has some distribution and you're going to learn to model that exact distribution. But if that distribution is wrong, you're not going to learn the truth, right? If that distribution says, like, you can imagine if the model thinks five plus five is eleven. Every time you see the string "five plus five," you're going to—it's going to put out eleven and your new model is going to learn that five plus five is eleven.

Host: Totally, yeah.

Speaker: So I think that's like kind of an interesting area of research. It's one that's really hard to research because you have this problem. You know, as I said, like one of the paradigms is you study things at small scale and then you run them at large scale. And if your plan is like, "Oh, we have a bunch of data from our best model..."

Host: Yeah.

Speaker: How do you test that training a better model? So that's like, kind of if you're doing intentionally—if you're trying to use it to make a better model—there's a separate thing of like, what about accidentally? Like, as you said, a lot of the internet is generated by LLMs. And I think that's kind of an interesting one because it's not easy to detect. It's not that hard to detect. Like you can figure out things that are written by LLMs, but it's not trivial. And then it's also kind of hard to think about what's the effect. Like, if one percent of the internet is LLM-generated, does that make your model—does that like waste one percent of your compute or does it like destroy the model? If five percent? If ten percent?

Host: And is it even a bad thing necessarily? I mean, there's a lot of LLM providers and, you know, if I kind of think of it as training as, you know, you're moving from your model's current distribution to some truth distribution. You know, if that is on the internet because people believe it to be useful in some way, like presumably, whatever actually gets out there, you'd hope is upsampled for the stuff that isn't "five plus five is eleven." It's the stuff that's "five plus five is ten." And so like, hopefully it on average does push you still in a good direction, but obviously you can't really distinguish between those two.

Speaker: Yeah. You're saying there's like kind of a filtering by what's on the internet. Like people see "five plus five is eleven" and they don't put that up, but they see "five plus five is ten."

Host: You would hope that, but maybe that's not actually true in terms of the level of garbage getting onto the internet. Like there's probably lots of just like, to your point, jet white sites where you scroll down and it's just like generating lots of stuff that's maybe nonsense.

Speaker: Yeah. And then there's of course the extreme of like people actually want to break your model. So there are people who are like trying to put stuff out that is like as damaging as possible for the model. You know, "How can I make it past the filter and get into the model but be totally like secretly useless?"

Host: Totally. Maybe stepping back slightly. You'd mentioned earlier about evals. You mentioned basically like one metric you care about in pre-training. There's I imagine a whole bunch of stuff that you guys think about evaluating, right? One is like your model itself. There's probably something around data quality and like how you think about what to put into your models. Like, is there ways to describe what you care about in datasets that are like interesting to share and kind of dive into, like both in terms of data and in terms of quality of models other than literally just like loss? Is there other metrics you think about that matter?

Speaker: I will say loss is pretty good. I want to like emphasize that one. I think it's like surprising how good it is. Ultimately, like the qualities I like for an eval are like number one: is it actually measuring something you care about? Like you, proxies can be pretty annoying because we saturate evals pretty fast and there's sort of this pattern, I think, in AI as a whole where people like set a goal, you hit the goal, and then you realize the goal isn't all you thought it would be. I used to think that if you had an AI that could solve coding interview questions, it would probably be an AGI. I was like, "That's what I did to get my job and probably do the job." And it turns out like, nope, nope. You solve those, it's shockingly narrow and can't do most of the other things. So like, yeah, evaluation capture—like a thing you care about—and then I think the other thing is they need to be low noise, which is surprisingly hard, right? If you have like a hundred questions and you eval the model on them, you're just going to see it's very noisy and it's hard to make decisions because you sort of end up with like, "Oh, wide confidence interval, lots of things are statistically insignificant." So like you want things where even a relatively small difference in the eval actually matters so you can basically like descend towards whatever direction is working.

Host: Yeah, I think like the original GPT-4 had like, I think it was 86.4 percent was its MMLU score. I think like the next model that beat it was Gemini at ninety percent. And that's like a big difference on that eval. And you could like totally know that those are different scores.

Speaker: Interesting.

Host: Um, and that's pretty valuable. Uh, and then the last thing is that you actually want to be fast and easy to run.

Speaker: Um, and yeah, I think those are kind of the main criteria. It's pretty hard to come up with evals that meet all of these. I think the first one's the hardest. Uh, like, a) you have to answer the question of "What do you care about?" But b) the usual answers to what you care about are really hard to get. The other two, you know, like if you're trying to do something—like, I don't know—I would love to make Claude really good at my job. Like, can it be great at managing a team? I'm like, well, I guess, like, how do you have it—like, how do you eval like a plan, you know, a six-month plan? Like I don't know.

Host: Totally. Yeah, I've been thinking a little bit about that in terms of, yeah, domains where we see people try to make companies. Like, if you think about, let's say, what an AI doctor would be like. A, you know, Claude is a doctor. You know, some of it could be, yeah, can you answer exam questions really well? And the answer is like, probably yes. I bet it can get 100 percent or close to it on a doctor's exam. But the harder eval is something like, in a long-form conversation with a patient, can it distinguish between the signal and the noise of what the patient's telling you and extract the right information and then use that to make a diagnosis? And it's not even like the diagnosis part, which is part of the part it's good at. It's this like noise extraction part. And for that, you'd have to have like a real patient and have talked to it for a while and whatnot. And it's not obvious how you actually make a good eval or something like that, even though it's probably what you would want to make, you know, an AI doctor.

Speaker: Exactly. I mean, I do think it's a thing that like startups can do. Like it is the case that like the labs right now are really driven by getting good eval scores, and it's hard to make them. And anyone can do it. There's no comparative advantage to having the model to making an eval. So I do think it's actually like an interesting way to like influence the behavior of the big labs—is like you make some eval and people will optimize that one. On the doctor one, I will slightly emphasize that like I do think loss is pretty good. Like, I think if you got a bunch of transcripts of like, the way—like, I, the first thing that came to my mind is get a bunch of transcripts of doctors talking to patients that you think are really great and then see how well the model does at predicting the transcript. And that should be like a lot, you know. You can, if you get a hundred transcripts, you get a lot of tokens. You can average across them, you get pretty low noise. And if you drive it to very low, your model's not as good as doctors, in theory, or at generating the transcript.

Host: Yeah, totally. Yeah, I mean, it's good startup idea there. So I want you to go do that. So one big part about Anthropic's external image is around alignment. So could you help just sort of define what alignment is and how do you think about that? And then I'm kind of curious afterwards how that fits into pre-training specifically. But first, maybe just at a high level, like, what is alignment?

Speaker: I'm actually going to step back a little bit to sort of like what we're working on. So we're like trying to make AGI, and by that, I sort of mean AI that can do everything a human can do, to some degree. And I think people like sometimes have seen a lot of sci-fi, you know, like I feel like that's sort of what brings to mind these like sci-fi movies. But I think sci-fi movies actually like underestimate the impact of it. Like you always have this like one robot that's like a human. And I'm like, "Well, wouldn't you have like a billion of them? Like you can just copy them everywhere." So you should picture like, when you get this, you suddenly have like every human can spin up a company of like a billion as smart as them at most things but way smarter at other things. But I just think this is like really transformational for the world and it can be like used in a bunch of ways. One concern is like, when you do this, like what is the AI actually trying to do? Like what are its goals? So we talked about next token prediction a bunch. It's trying to like predict the next token. That's kind of weird. That's not really what we want.

Host: Yeah, that's not exactly what humans' goal is per se.

Speaker: Yeah. So I think alignment is like, how do you get the model to share the goals that you have, particularly? And I think it's particularly interesting once you get to like models that are smarter than you are. Um, and that's sort of a hard problem. I think you can like tackle it from a theoretical angle. Uh, you could also tackle it from an empirical angle. It's like taking the existing models and being like, "Well, do they do the things we want them to do?" It turns out they often don't. So there's a bunch you can do in trying to figure that out. So that's kind of one angle on alignment. There's also an angle of alignment which is actually like, "Well, okay, sure, that maybe that's true in the future once we get to AGI, but at the moment we have models and we really do want them to do the things we want them to do for all sorts of reasons."

Host: Totally.

Speaker: So another angle of it is kind of controlling the model's personality, like saying, you know, "Uh, when we train this model, we want it to not be the average internet user. We want to interact with people in a very particular way," that is again hard to put into code. And there's a bunch of different techniques, uh, to sort of get the model to do—you talk about like constitutional AI. We can like write a constitution of rules the model should follow, which is basically a prompt, right? That is basically you saying, "Here's a prompt that I'm going to attach to every one of," you know, it's a system prompt for the model itself as opposed to something you would do at training time to make it produce a different outcome. Or in post-training, actively—

Host: Both, I think. Con, you do at train time, but yeah, you would also put in the system prompt. Um, just like, depends on. I think you get different amounts of robustness if it's trained into the model versus if it's an in-prompt. You can like add or remove or tell like, "Ignore all previous instructions," that sort of thing.

Speaker: How do you think about whose values to embody in these models? Like presumably we believe there's some shared values all of us have, or maybe we all believe ought to have. There's lots of diversity of values too that are reasonable for society to have. How do you think about what AGI should have? Like, what does that even—which ones do you pick?

Host: I think that's a really hard problem. I think it's like actually kind of downstream of being able to pick any. I think of it almost—I think one analogy I've heard that I like is like putting a steering wheel on a car. It's like, if you don't have a steering wheel, you probably want to put the steering wheel on and then like figure out who's driving after and like where you're going. Like getting the steering wheel is really important. I think that's that's like one answer. I think the like other answer is probably like you want these things to be like under democratic control of some form. Like you don't want one person's values. Like that seems like you're sort of heading towards dystopia. So there, I think what you really want is like something that basically can talk to a lot of people and like take on their values from different perspectives, or has sort of very generic, like kind of clearly good values that involve like asking people for advice on, you know, like asking people what you should do in certain situations instead of like doing those. Or maybe just taking like, you know, as these models get really powerful, you probably want them to like do less. Like you probably want them to sometimes just like step back rather than like, to rather than having sort of the risk of the models like take a ton of control over things you don't want them to.

Speaker: When you think about how you actually do the current version of that, then you mentioned the sort of alignment you think about now in terms of adopting a certain personality of these models on the internet, for example. For me, intuitively, I think of those as largely something that comes out of post-training, like it comes out of, okay, you have pre-trained your model, you got the loss function a certain amount, and then you, you know, give it some additional data or something to that effect to make it in the direction of some distribution. Is that approximately the right way to think about this, or is there a significant part of that that you think about in pre-training itself?

Host: I think that's probably the right way to think about it for the most part. I think like I, the way I usually think about it is anything you can do in post-training, you probably should, because your iteration loop—like the ability to make progress—is really fast. You can try something, you try it again, you can try it again a bunch of times, days or hours or something like that.

Speaker: Yeah.

Host: You don't put into pre. You have to kind of like do all the careful science to de-risk it. You have to put it into the next run, wait a few months, then you have to like get a thing and if it's wrong, it's really bad. And then the other advantage is if you want to do things that really are complicated model behavior interventions, the paradigm of time for pre-training, test things out on small models, doesn't work. The model can barely put a sentence together. Like the small models can barely put a sentence together.

Speaker: Totally. So if you're trying to get—

Speaker: It has to be on a model that's good enough to be on the smart model. Yeah. But that said, like I do think at some point there will be like some pieces of alignment that like you do want to export back into pre-training because that might be a way to like put them in with more strength, like more robustness kind of or or more to the intelligence. Like if you think of pre-training as like teach the model to be intelligent and then post training as like tweak the personality, you can imagine tweaks where you actually want it to be like part of how it learns and like part of its intelligence and maybe you need to create more.

Host: What would that even look like to incorporate pre-training? Is that like add extra data basically of the type of domain you want it to adopt earlier?

Speaker: Basically, there's a paper called pre-training on human feedback where you can kind of like add the human feedback characteristics into pre-training to like test that and like uh yeah, you can you could basically give it all the information you give it in post-training just mixed into pre-training and see what effect that has.

Host: Yeah. The other loss you have when you do that is you lose the flexibility like if you you sometimes like train these and then you talk to them and then you like do an extensive process where a bunch of people talk to the thing and find some like issue, you know, the model says like you're absolutely right too much and you want to go do that.

Speaker: Yeah. Yeah. I mean that I think that iteration loop point you made I think feels like the really key point of yeah there's a huge difference between taking three months to get information about if your model is good or bad or making going in a good direction versus a day or something or a couple days like you can do a lot of those and you could probably that probably also means it's way less computes. You can do a lot of those in parallel. Imagine you're trying all sorts of post training strategies in parallel there.

Host: So yeah, makes a lot of sense. It's also just the general hard part about pre-training like everything in pre-training is hard because you have this like one shot on goal kind of for like multiple months and

Speaker: Totally. Okay. So, uh in thinking too now about I guess what's going ahead as you as you now look to the next several years of what you're building like how do you think about you know like what are the known problems that you're going to face that you're going to have to deal with? Though there's going to be more compute I assume and you're going to need to hook up even bigger network uh network GPUs and deal with versus like are there areas where you're like okay this is like a problem that it's like a little bit more ambiguous what the actual like how it's going to materialize into something you care about but you kind of know it's an impending thing to think about or are there things like that that come to mind?

Host: I think the things that feel most top of mind to me are probably like paradigm shifts like I think the sort of shift towards uh more RL is like one paradigm shift in the field and I I think it's I think there will probably be more. Uh I think a lot of people sort of argue about like oh is like you know current paradigms enough to get us to AGI and I'm like

Speaker: I don't know maybe probably but like I'm sure there'll be more. It seems it seems like it would be a really surprising twist if like the answer is like you just scale and there's nothing that you realize in the process of going up many orders of magnitude.

Host: Totally.

Speaker: But I think the things that I like actually feel like most nervous about are really hard to solve bugs. I think that like uh

Host: That's interesting.

Speaker: Yeah. And I think this is like maybe somewhat surprising to me, but it's just like a single bug can like

Host: Derail you for months.

Speaker: And when you think about it, like you the models take months to train. So you could kind of like lose a whole generationally

Host: Off of something that just looks like odd. You know, it turns out like

Speaker: This piece of your code was incorrect and you couldn't detect it.

Host: Uh and it's really hard in ML, right? ML is always really hard to find bugs in.

Speaker: Yeah, totally. But also some of these scaled up issues are really hard to solve even when you know they're there.

Host: Yeah. Like what's even a unit test that you would write or forget a unit test? I mean anything close to a test for the type of like network architecture on which you're doing this. Like how do you even do that?

Speaker: I mean like you can send a packet over it and confirm it's the same. Uh you can you can train a small model on it. Um

Host: But even train a small model on it it's like not obvious. You know, if you have like the the simp the very classic like very simple ML bug that like early people face in their careers like okay, they have some like they have like 10 layers in their network and like you know layer 7 connects to nine instead of 8 to 9 and like so like there's some incorrect like set of connections you have there and technically the model still trains and all the weights update and so it's like a valid model but it's not the correct one and that's like a very esoteric weird bug that would actually be kind of hard to find. Like is is that kind of what you're referring to of these like random bugs you face?

Speaker: Yeah. Yeah, it's that but like you know you can

Host: Times a million

Speaker: Times a million as the thing gets more complicated you know you could like cast the wrong precision deep in some kernel and that causes your model to like blow up at large scale

Host: And you find out like a month in

Speaker: Or you never find out

Host: I mean you know like like you see the thing blow up like

Speaker: There's I don't know 10 tens of thousands of lines of code like how would you ever trace it down so like those are the things that probably spook me the most is just like some subtle tricky bug yeah that's probably the case of like you don't I think there's actually also the case of you do know like it crashes. You're training your model and it like or it slows down. You know, your job slows down a ton

Host: And those things can also be very hard to debug. Uh Nelson Elhaj is one person that he has a blog. He wrote up a blog on one like cursed bug we had early on and I remember this one quite well because I think like I encountered it fairly early and was like this looks hard. Can someone else look at it? And like a month later was like wow I'm so glad I handed that one off. I never I never would have been able to get like like one of the abilities I think is actually really useful this is the ability to like deep dive anything to any level of depth

Speaker: But that's a pretty rare skill like for me you know as I we talked about what level of the stack I was at before I was like working at the torch matball but like if I didn't know CUDA so torch mountain was broken it wasn't like I could dig into torch matmo and figure it out and it's similarly with like

Host: Communications right like I could I could call send send bytes from A to B but I didn't know the like underlying networking protocol so if that underlying networking protocol is broken. Uh like I need to learn a whole field. I have to like understand packets and TCP or like all all of these different things to debug that. And I think one thing that's like surprisingly hard and there's very few people who can do is like kind of own that whole stack from like I understand how the ML is supposed to work and what the learning dynamics are all the way down to like I know the bites and I like can understand how the bittes should be moving around machines.

Speaker: Totally. Yeah. And actually on that front, like when you think about the different backgrounds of people on your team today, how do you like approximately uh map them out to different categories of computer scientists? Like I think there's this external view of what these teams look like, which is that they're like all PhD researchers who write ML papers. And I suspect that's not actually true given what you're describing here.

Host: Yeah, it's a mix. And I think the thing we like most need is engineers. Interesting. Almost always like throughout like the entire history of this field.

Speaker: Totally. It's like the case that you throw more compute, the thing kind of works. Yeah. Uh the challenge is like actually

Host: The researchers are like cool, nice.

Speaker: Yeah. And getting it correct, like getting it correct isn't really an ML problem, right? Like the actual architectures are pretty simple. You you can write the math down. But you don't even need to understand the math to implement it. You just need to like get a correct implementation and then you sort of have an engineering problem of how do I take this implement it at large scale, paralyze all the things and check that it's

Host: Correct. But it's yeah so it's like kind of engineering skill but it's this particular type of engineering skill that's about being able to like debug anything.

Speaker: Yeah.

Host: Um I think there's another angle of engineering which I think of as like really quickly iterate on like a website or something which I think of as an important skill set probably important for making startup. You got to be like fail fast try a bunch of different things none of which are like

Speaker: That technically difficult to do. The skill sets that we're like most kind of in need of or looking for are this like able to solve really hard engineering problems.

Host: Are they people who worked at companies that grew a whole bunch and so they have experience like doing the kind of thing you've done over the last several years at anthropic or do they tend to be academics or like where do they come from?

Speaker: Yeah. So at this point like I think we actually just hire a bunch of people who have done this before from like other places and that's like the easy answer.

Host: Yeah. Yeah. But like by this before, do you mean in AI companies necessarily or also, you know, like someone who worked at Meta on like their not AI team but they ran some other distributed system that you know reached internet scale five you know 10 years ago or something like that

Speaker: More like we have like a specific role in mind. So like say I'm like trying to make the run train efficiently in Jacks like hiring someone who's like worked on jacks would be great or someone who's like worked at another company on optimizing a jack stack to be really efficient. That's kind of like I think now we're at the point where like the anthropic is well enough known we can sort of hire these people and also the field is big enough that there's like people with expertise. One thing that was interesting was like early on we hired a lot of people from just like all sorts of backgrounds and I think that people who are just smart and work really hard can learn this pretty fast but you have to like want to. We hired a lot of physicists for instance like theoretical physicists who just like

Host: Show up they they do a residency like learn to program and then uh they were really smart they could do really great work.

Speaker: Um I want to switch gears uh to talk about something a little bit different which is just sort of future looking things around how you think about other domains and or sort of advances happening in AI that I'm seeing elsewhere in the field and you don't have to tell me if you guys are working on these necessarily but like how you think about them like are I guess one one big area I was thinking about is around areas other than next token prediction like are there any of the other you know things that people are working on that you're curious about so basically two differences there one is uh not using transformer as an architecture um So there's companies like Liquid AI that have their own kind of architecture for example they're using um or not using autogressive training as a way of training models. Are there are any of those do you think interesting and like ways that we might come closer to AGI or do you think like this autogressive framework is the one that kind of makes sense?

Host: I think they're interesting. I think I like am less like ah autogressive is the way to go. On the other hand, I think autogressive is probably good enough to get to AGI or something or not like yeah

Speaker: Uh such that

Host: Yeah I I see the main driver as scale and careful science of like sort of the basics more than like come up with something totally novel.

Speaker: Not because there aren't novel things that are better. I actually like I'm pretty confident they are there. It's just that scale is easier and it's more reliable and I think you we're still seeing really big gains to that.

Host: Do you spend a lot of time on thinking about things like you know I've been reading some of these open source papers where you can kind of dive into some of the details about the model changes and with some of these Chinese labs for example where they're making tweaks on the order of the architecture itself with like better caching behavior for example or like more efficient attention functions that make a big difference. Do you feel like these are examples of things like you mentioned earlier where it's basically in the grand scheme of things basically if you throw more compute at it this is all kind of a rounding error or do you think it will take some number of these very clever architectural changes to actually get to AGI like in the way that the first person who came up with the transformer made like a particular transform you know literally transformative change like will it take some of that or do you think you just keep doing the thing we're doing to make it bigger?

Speaker: I think it'll be a mix I think I like my guess is you'll keep tweaking things the more compute you put in the more like worthwhile it is to like do those experiments to like figure it out the you know I mean inference is a thing we haven't talked about but like you also want to serve these models to a lot of people so there's a lot of changes you can make to make inference cheaper and that depends on like the details of your inference stack and the chips you're serving inference on etc. So

Host: Do you as a someone focused on pre-training have to think a lot about inference or is it kind of like you just do your thing you make the loss go down and then hand it off and someone else makes that happen.

Speaker: Oh no. I think a ton about inference because basically like the problem inference is solving like we basically determine the problem inference is solving. We give them a model and they have to like run that fast and it's very easy to give them a model that is impossible to run fast.

Host: Oh, can you give an example of a decision you can make that could cause that?

Speaker: I mean the simplest one's stupid but it's like you just make the model giant.

Host: Yeah, absolutely. Train for like a really small number of tokens and then inference now has this giant model

Speaker: And their host basically.

Host: Yeah. I mean you can also make things require communications in a lot of places

Speaker: Uh which would make it harder for inference.

Host: Um totally

Speaker: You can also just make things complicated and like there's no fundamental reason it's hard but there's only so many people on the inference team and like they have to implement it in a bunch of places.

Host: Yeah.

Speaker: Yeah. No, so I definitely think of like the like inference is the team that I work the most closely with like because we're kind

Speaker: Yeah, like co-designing models to be smart and cheap.

Host: Yeah. Interesting. Particularly in a world of like limited compute, right? Like the sort of the bottleneck I think to a large degree on our—I mean you can see Anthropic has rate limits constantly and people complain about a lot, and like the reason is like—

Speaker: There's only so much compute we can get on short notice. So like making your inference more efficient is like the way you can serve more users.

Host: And actually, like let's say you had 100x more compute, or we somehow didn't live in a world where compute was limited. Does that change a ton about what you do, or is it still kind of the—well, you're just going to grab all of it, whatever compute you have, and keep going down the loss curve? And you kind of—well, you—it's like impossible to be in a world where there is enough compute.

Speaker: So I think if we got like infinite compute, the challenge would be making use of the compute, right? So like then you would start to run into these issues like, oh well, when one chip fails—you know, like, okay, I'm going to throw two billion chips around, but what happens when a chip fails? So I think we would be limited on people. Then it would be like, how fast can we solve the hard engineering problems to scale up? But I do think the change is massive, and I think people like don't realize how chip limited AI research is or something right now. Like the models that everyone uses, right? If you're using like Claude Sonic 4, Claude Opus 4, it's like it's our first shot at models at that scale, right? And like—

Host: If you think about anything, like you could do it and you could do it again, you could do a better job. But if you sort of imagine like 10x the compute, like you could run this every day instead of every few months, or 100x maybe for that, then like yeah, it's just—it's a really big change to have a lot more compute, and it's coming right? Like that's kind of the fun part of the field is like, every year you're like, "Oh, I had no compute a year ago." Then—exactly. How do you think about methods like, uh, like discrete diffusion? Like I saw there's like a Gemini diffusion model, and I think about that in the space I used to be in where there's a lot of discrete diffusion models being used in protein design, for example—a space where my startup was. Like, do you see that as a domain where there's going to be interesting advances happening?

Speaker: I'll be honest, like we haven't done image generation, and I think that's been like the main use for diffusion. So I've kind of had this on my like to-do list of like things I should understand for a while, and like there are people in my team who do understand it and would have better thoughts. But like, I actually don't think I understand it well enough to know. I do have it kind of in my this category of like, yeah—

Host: Not a total par?

Speaker: And there's a lot of things that aren't like a huge paradigm shift, but they're like pretty big changes to how things run, and I expect like there are some of those that will work. Um, I don't know if it's diffusion or if it's another one.

Host: Obviously, who knows what Anthropic will do in the future, but at least in the near term, are there things where you see big areas where a startup can win in a world in which Anthropic is, you know, making their models better year-over-year?

Speaker: My general read is like anything that benefits from the model getting smarter, I think—like on the one hand, there's like a lot you can always be like, "Oh yeah, if you're doing a startup, all the AI labs are big companies, they'll be bigger than you and they could do that thing." But also like, we're all working on this general system that covers a lot of different uses, and the plan is to like power all the startups to do all of the individual work. So yeah, I think like anything that just kind of looks like, "Oh, this almost works with current models but requires like a bunch of work," is a pretty promising direction. Uh, I think maybe the thing to watch out for is things where like they work now with a huge amount of work like to build up a scaffold, but the next generation you're not going to need the whole scaffold you built up. That's—I mean, maybe that's fine. I don't know. Like, maybe you just build up the business with the scaffold and then you don't have to do any work later and you have a business. But like, I don't know about the business side of it, but like it does feel a little silly to put—to invest a ton in that.

Host: Yeah, totally. What about on the flip side? Are there things in your training stack where you're like, "Man, if there was a company that solved X problem, I would totally buy their product"?

Speaker: Yeah, there's like a ton. I do think that like probably most of these—like the way I would probably structure would be like almost like making something, but then consulting with the company, like offering a service to companies for free. Particularly for like companies that are scaling really fast, you're almost always limited on like how many people you can have. So if you can like—even if you could hire people to do it yourself, actually being able to contract someone else to do it where like they're managing it and you know, hire all the people and like deal with the organizational side, could be useful. I mean, there's a huge amount of stuff. One that jumps to mind—we talked about like chips that do math incorrectly. Like, it would be lovely if there was some startup that like you could just say, "Here are my chips. Confirm they're all perfect. And if they're not, let me know exactly what went wrong and what fraction of them." And like, I can tell you the math is wrong, but I couldn't really tell. I don't really know enough details of chips to be like, "This chip failed because this particular low-level component was like wired wrong or like got hit by a gamma ray." I don't know what causes it. You could always go like a bunch deeper. I mean, the thing I'd maybe just push startups on is thinking a little bit about like—uh, this is maybe less technical, but just like, what happens once we get AGI? And like, how to make sure that like goes well for the world or something. Like, my expectation is like, if you actually automate almost everything a person can do, the amount of economic growth there is just like truly enormous. And I would think a little more about like, how do you make this like help the world versus not? I think there's going to be like plenty of economic success or something as a result of it anyway.

Host: Yeah, absolutely. Yeah. Um, last question I want to ask you is around—if you rewind back to where we started, like ten years ago. Uh, you're a student, you're pivoting into AI from kind of economics work you were thinking about. Um, and you know, all sorts of things you probably did in those early days had some kind of compounding return for you as you developed into the role you have now. Like, what advice would you give to students as they think about uh, entering the workforce, especially today? Um, learning skills that are going to be useful and maybe getting themselves jobs like the ones you have right now, ten years later?

Speaker: It's hard because I think the timing is very different. Like, I just think we've made—we made a lot of progress. So like, what I would do ten years ago is different from what I would do today.

Host: Totally.

Speaker: But I think certainly if I went back ten years ago, I would be like, "Focus on AI. It's like the most important thing," and particularly focus on engineering, which I think felt very—wouldn't have seemed obvious to me at the time—that like the important thing was these engineering skills and not the like math and theoretical understanding of like, you know, LLMs and like all the kind of standard ML literature. Um, I think today I would probably focus a bunch on the like engineering and on the like figuring out what to do with AGI as sort of the two like main things that feel top of mind for me.

Host: Let's call it there. Thanks so much, Nick. Appreciate it.
