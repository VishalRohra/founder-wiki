---
title: "Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design"
slug: "Mp-anthropic-co-founder-building-claude-code-lessons-from-gpt-3-llm-system-design"
media_type: "Video"
author: "Y Combinator"
speakers: ["Host", "Tom Brown"]
categories: []
description: "Tom Brown discusses his unconventional path from YC founder to AI researcher, the discovery of scaling laws that changed everything, and his advice for young engineers entering AI today."
url: "https://ycombinator.com/library/Mp-anthropic-co-founder-building-claude-code-lessons-from-gpt-3-llm-system-design"
youtube_id: "JdT78t1Offo"
youtube_url: "https://www.youtube.com/watch?v=JdT78t1Offo"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Anthropic Co-founder: Building Claude Code, Lessons From GPT-3 & LLM System Design

Tom Brown co-founded Anthropic after helping build GPT-3 at OpenAI. A self-taught engineer, he went from getting a
B-minus in linear algebra to becoming one of the key people behind AI's scaling breakthroughs. And his work is paying
off.

Today, Anthropic's Claude is the go-to choice for developers, and his team is overseeing what he calls "humanity's
largest infrastructure buildout ever." On this episode of The Lightcone, he discusses his unconventional path from YC
founder to AI researcher, the discovery of scaling laws that changed everything, and his advice for young engineers
entering AI today.

## Transcript

Host: Welcome back to another episode of The Light Cone. Today we've got a real treat, co-founder of Anthropic, Tom Brown.

Tom Brown: Excited to be here.

Host: So Tom, one of the things that a lot of the people watching would love to figure out is you got started in tech at the age of 21, fresh from MIT. How does someone go from that in 2009 to literally co-founding something as important as Anthropic?

Tom Brown: Summer 2009, Linked Language. Two of my friends had started that out. I think they had seen one of our other friends, Kyle Vote, kind of do a YC company. And so it was in the water that that's a thing that we could try to do. They started out I was the first employee back then.

Host: Yeah. You guys let me join for all the dinners and stuff like that too.

Tom Brown: I could have instead gone to like a big tech company or something like that. And I think probably just as a software engineer, I might have learned more software engineering skills. But I think by being there with the other co-founders without anyone telling us what to do basically like we had to figure out how to live, how to like the company would die by default. I think in school there was a lot of like a feeling of more of people would give me tasks and I would do the tasks. It's kind of like a dog waiting for like food to be fed to them in their bowl or something like that. And I think for that company it was more like wolves and we have to like hunt our real food otherwise like our kids are going to starve or something like that. I think that mindset I think has been like the most valuable mindset that shift that I've had for trying to do like bigger more exciting things.

Host: Yeah. Big tech just teaches you to work at a big tech company whereas it's much more fun to be a wolf.

Tom Brown: Yeah.

Host: How did you go from like so working at friend's startup to then you started your own one?

Tom Brown: So Linked was um we ran the company for a bit. I ended up going back to school afterwards and then when I left school I went to this company Mopub.

Host: The mobile advertising thing right?

Tom Brown: Yeah. Yeah. I was like the first engineer there. I was like okay I want to be a wolf but like I was really bad at programming also. I was like very very struggling as like a software engineer. I know I want to do more but I don't know how to do it yet. And so I think that was kind of like a experience getting to scale something. Winter 2012, one of my friends who was my smartest friend from college pitched me on let's go and start a YC company. We did at the time Solid Stage. This was before Docker existed. And so the idea was try to make it easier to do DevOps, but Docker doesn't exist. So it's going to be a more flexible Heroku, which basically meant a more complicated Heroku. And so we I remember we like we interviewed with you guys. I think folks didn't really understand what we were trying to build. I think we didn't really understand what we were trying to build that much.

Host: When you're trying to do something new. That's actually sometimes common.

Tom Brown: Yeah. I think we were an outlier there cuz we like did our interviews and then we got called back driving back to San Francisco and PG had written on the board like an angry frowny face and "What are you actually going to build?" And so he like wanted us to explain that. I guess we explained it enough or he was just like these guys still don't know what they're doing but maybe they'll figure it out. Halfway through I kind of felt I still didn't actually understand what we were going to build and how we would attach a mission to it that like I wanted to work on for my whole life.

Host: Yeah.

Tom Brown: Um and so I left. PG actually intro'd me to Michael Waxman who was the Grouper founder.

Host: Yeah. So Grouper was a dating app. Only it was novel in that you had what, three guys and three girls, y'all?

Tom Brown: Yes. This was before AI in a lot of ways. So there was like a set of a team of people who would manually link people up, right? And they'd meet up at a bar and shenanigans would ensue.

Host: Okay.

Tom Brown: The pitch for Grouper for me for like why I was excited for it was just I was like an incredibly awkward kid. What I wanted to do was to basically have a thing that lets awkward people like me go out and talk to other people for me to talk to girls and feel like I was safe doing it with like my friends around and stuff like that. And so I think who were going to be our employees was important. I did like all of our engineering interviews. Who would take someone. The only person who went on more was Greg Brockman.

Host: I think he had a phase where like every single week he would go and like post on Slack or HipChat at the time.

Tom Brown: New York and he was hanging out at the Recurse Center during this period.

Host: Oh, I think he was at Stripe. Maybe maybe for part of it he was at Recurse. Yeah. But he also had uh I think just like a phase where he would just at Stripe he would just like post in their thing every like I'm going on Grouper who's going for like a whole year.

Tom Brown: So I ended up being close with Greg which which ended up being a connection to OpenAI.

Host: What was the journey like? Because you started as you just graduated from MIT CS. You were 21. You became first an early employee for all these YC startups. Then you started your company just a couple years later. And what was the path for you to eventually become the co-founder of Anthropic? It was like a long path but it's pretty impressive. How how did you get there? I mean, it sounds like getting in touch with Greg at that moment.

Tom Brown: Uh, and then you were one of the first uh, you know, a couple dozen people to join OpenAI as a result.

Host: Yeah. So I left Grouper 2014, June 2014, and I joined OpenAI I think a year later. I tried to like build up courage to make the switch to be a to try to learn AI research. At the time I was like, "Okay, it seems like sometime in our lifetimes we might end up making transformative AI. If we do, that would be the biggest thing. Maybe there's some way that I could help out, but also I got like a B minus in linear algebra in college." And so it seemed like at the time you needed to be just top superstar in order to try to help out with that at all. And so I think I had like a lot of uncertainty about whether I would be able to help. And also I'd had some success with startups. And so a lot of me was just like rather than trying to retool at this like I could try to do another startup or something like that. I feel like in that period um going to work on AI research which is not seen as like a serious like practically serious thing to do and you're in a world where it's like people try and build companies and do these like really practical things like what did your were your friends like oh that's really cool you're going to go work on AI stuff or was it not really.

Tom Brown: I think my friends were like that sounds that sounds weird and bad kind of like it it doesn't really seem like like AI safety is a thing we should be worried about like overpopulation on Mars doesn't make any sense and my friends were also just like I don't know if you're going to be good at that though. I think that for that reason, I think I didn't try very hard for I like kind of flip-flopped on it for like six months trying to build up courage to do it.

Host: And what were you specifically at this point? Like you're reading research papers like what it what does it look like?

Tom Brown: Yeah. So first I was just kind of hanging out. I built like an art car for Burning Man and stuff like that.

Host: Oh, that was fun. Yeah.

Tom Brown: Yeah. So I I spent like a whole summer like three months after Grouper doing that cuz honestly I was I was like kind of burned out for Grouper where I know startups like the highs are high like the lows are low and we weren't working at the end. Our business wasn't succeeding. Our revenue was going down but my main job still was like recruiting engineers and so I had to like pitch them on this dream that I had had but I like no longer really.

Host: Sounds like a death march.

Tom Brown: And so I was super burnt out and I was like, "Okay, Tom, like chill out, do some yoga, like do some CrossFit, like build an art car."

Host: And what was the hindsight? Like, you know, hindsight's 2020. What's the retrospective on like Grouper obviously attracted all these really, really smart people. The graphs were up and to the right and then it flatlined and maybe started declining. What happened?

Tom Brown: I think that when we started the competition was like Okay Cupid.

Host: It was all web-based.

Tom Brown: All web-based. The main problem that I think we were solving was the it's hard to like go and put yourself out there and go like talk to someone new and they might just be like I don't want to talk to you. You seem weird. And so we solved that by just blind matching. Tinder came out while we were doing Grouper and Tinder solved that same problem with both people have to show interest before you get matched. So there's also no worries about getting rejected. And I think that they just had better that was a better solution to that same problem. So good work Tinder. Good work all the swipers. I think that that that solved the like mission that we were trying to solve better than we solved it.

Host: And then yeah, like when did you get serious about AI and just how did you approach it?

Tom Brown: Three months of like kind of playing and having fun and then I ran out of money also when I had like my personal runway. I ran out and so I was like, okay, I think that I'm going to need six months of stealth study to have a shot at getting a job. At that point it was Deep Mind or Google Brain were the two places to do work there or MIRI. Miri was the third one that I was like looking at. So I was like if I want to help out with that those are the three places to look at. I don't have any of the skills yet. I need six months of self-study to feel like I would not be a drag on them and like actually be helping instead.

Host: Can you um maybe explain a bit what was that self study like? Because I'm sure there's a lot of software engineers right now in their 20s are looking to retool to become AI researchers. What was what was that six months like? Even though as you said you had uh gotten a B minus in linear algebra which is like core.

Tom Brown: Might have been a C plus. I'm not I should check. I'm going to keep telling.

Host: That's pretty impressive where where you got to.

Tom Brown: Yeah. Yeah. It turned out okay. First I did a contract actually with Twitch um and like earned like enough to have that six months of runway. So I did like three-month contract with Twitch and then I made a a plan to self-study. I don't think it's the right plan now for people too at least 2015. What did it looked like? It was like take a Coursera course on machine learning, try to solve some Kaggle projects, read Linear Algebra Done Right, and uh I had a statistics textbook. I think I had YC alumni credits and so I bought like a GPU and I would like SSH into the GPU to like work through my courses for it.

Host: And this is right after Yeah, it was already after AlexNet, right?

Tom Brown: This is after AlexNet. Yeah. So I was mostly doing image image classification stuff that I was trying to learn was like the thing that all the courses would teach you to do.

Host: How did you get the OpenAI job? Because you were one of the few engineers. It was mostly researchers and they had pretty stacked team of researchers.

Tom Brown: I messaged Greg um as soon as OpenAI was announced and I was like I'd love to help out in some way. I got a B minus in my linear algebra but I know some engineering. I've done a bit of distributed systems work. If you guys need help, I'm like happy to mop floors if if you guys need I want to help out, however. And I think Greg was like, yeah, I think there's like a plethora of people who he said plethora, too. I was like, fancy word there. There's a plethora of people who know both machine learning and distributed systems. So, like, yes, you should do that. I think he introduced me to Peter Abbeel also to help me put together like a little course for myself, too. And then I checked in on with him, I think every month or something. And then after a couple months he was like oh we actually have a project which is uh we need to put together we want to play a game like play games can you help uh make Starcraft environment and so I joined to like help them with the Starcraft uh environment. So that that ended up I think getting my foot in the door. I I didn't do any machine learning work with them for the first nine months that I was there basically.

Host: And what did OpenAI feel like at this point? Like had it raised much funding? Did it have like an office? Which is what will do it. Did it feel like a startup?

Tom Brown: So it was in the chocolate on top of the Dandelion Chocolate factory. Um.

Host: This is after Greg's apartment. That's the after Greg's apartment. Yeah. So like right after Greg's apartment in the chocolate factory when it kicked off, right? It was like a billion dollars of committed funding from Elon. It felt like it was like very solid.

Tom Brown: The other interesting milestone for you was when you got to build a lot of the engineering around the training for GPT.

Host: Yeah. For GPT-3 and how how what was that? Because you got from GPT-2 was in TPUs, right?

Tom Brown: Yep.

Host: And the big breakthrough in GPT-3 was like use more compute and using GPUs.

Tom Brown: Yep. So I ended up working at OpenAI for a year, left, went to Google Brain for a year, came back, and then GPT-3 was 2018 through 2019 was like building up to GPT-3, which exactly as you said was like scaling things up. I think that like Dario had seen the big trend of scaling laws basically. You published a paper for that.

Host: Yeah. Yeah.

Tom Brown: And that's like a pretty important paper that now has withstood the test of time and we're living now the dream of it. Definitely like seeing that line of reliably you get more intelligence if you spend more compute with the right recipe was the main thing that was at least for me was like this is a thing that's like happening happening now cuz you could look even at the.

Tom Brown: Time we weren't spending very much money on the training jobs at the time, and you could see that there was scaling there. And then also Danny Hernandez did a paper at the time that showed how much cheaper algorithmic efficiency was making stuff over time too. And like those two things stack together, that was like, "Oh wow, we're going to get a lot more intelligence over the next few years."

Host: So it was noteworthy and surprising when you saw it.

Tom Brown: Yeah. And I think the thing that seemed the weirdest to me is like, I'm not a physicist, but like all these physicists were doing this stuff. The original scaling laws paper, just the very straight line over like 12 orders of magnitude. I'm just like, 12 orders of magnitude is like just like a stupidly large amount. I've like never seen anything go over 12 orders of magnitude. That convinced me to definitely pivot all of my work into scaling, which I hadn't been doing before.

Host: Can I ask a like kind of lay person question? Is it fair to say that the scaling law might show up in all of these other domains? Are there like 2, 5, 100, 10,000 domains where the scaling law could hold that we're just not investing into?

Tom Brown: Yeah. So I think in physics scaling laws hold all over the place, which I didn't know at the time. But within physics, like there's a whole field called phenomenology that basically looks at various aspects of the world and then does those types of fits. And they find these like power law distributions all over the place. This was like I think the first one that I had ever seen in a computer science adjacent thing, which I think was like interesting and surprising.

Host: And at the time, people were mad about it. They actually were like, "You're throwing money at GPUs or just like wasting money. This is very wasteful."

Tom Brown: Yeah, that was sort of—

Host: People are still mad about that.

Tom Brown: Yes. Different people now, but still people mad about it.

Host: Yeah, yeah. I guess the researchers were mad at that too, where it's like, it's not elegant. You're just like brute forcing it. The jester cap, like stack more layers, which I think Anthropic's slogan I think is like, "Do the stupid thing that works." That was a thing where like this was very clearly the very stupid thing that works.

Tom Brown: Yeah.

Host: Can you tell us then how you ended up collecting the last infinity stone with Anthropic? Because there's very few people in the world that have basically worked at OpenAI, DeepMind, and Anthropic. And you were part of the team that spun off from GPT-3.

Tom Brown: Yeah.

Host: And then started Anthropic. So how was that jump?

Tom Brown: There were two teams there. That was the safety org and the scaling org, were the two orgs that reported into Dario and Daniela. I think we had just like worked together extremely well. One thing I think that was great both at OpenAI and at Anthropic was just like we had a culture where like everything is on Slack, 100% of things on Slack. And within that, all public channels, great communication. I think that that group also was the group that took the scaling laws the most seriously, where it was like, "Okay, like this actually is going to be transformative. There's going to be a handoff where like humanity will hand off control to transformative AI at some point, and hopefully like they'll be aligned with us and like that'll be a good transition that goes well. But it might not be. The stakes are incredibly high." And so I think that group was very focused on like, "How do we make sure that that's taken seriously enough, and that like we've built an institution that can handle the weight of that?" That ended up being the core group that left to join Anthropic. And I think it wasn't clear at all to me that like that was the right thing for the world at the time. In hindsight now, it seems like that was a good choice.

I think what was kind of cool then too is when we started out, we didn't seem like we were going to be successful at all. OpenAI had a billion dollars and like all of these all of this star power, and we had seven co-founders in COVID like trying to build something. And we didn't know if we were necessarily going to make a product or what the products would look like. And so I think that what was interesting from that too is that all of the initial people who joined were there for the mission too. They all could have worked somewhere else for more prestige, more more more money. People would have known what they were doing, et cetera.

Host: Well, stayed at OpenAI basically.

Tom Brown: Exactly, yeah. That exactly. That's been an interesting thing then that I think has been like the key to letting our culture or letting our org scale. We're like 2,000 people now, but we still have a thing where it doesn't seem like politics have crept in. And I think a lot of that is like the first hundred people all were just there for the mission. So like if something starts to go wrong, they'll like raise their hand and be like, "It seems like this person might not be acting for the mission."

Host: Hey, tell us about the early days of Anthropic. So the seven, you broke off from OpenAI. You had a general idea of the sort of long-term mission that you wanted to do, you know, not destroy humanity. But like, how did what did you actually work on for the first year? How did that converge on an actual product?

Tom Brown: So first year, the main thing that I tried to do was just build the training infrastructure that we needed to train a model and then get the compute that we needed to train the model. Those were like my two main projects. All the other things that you need to do when you're like starting up a company too, so like set up a Brex account, and like I don't know, like all all of that, all of that stuff. We started out with seven co-founders. Within like a few months, I think like 25 folks from OpenAI overall had joined. So we had like a pretty substantial team that like already knew how to work together too. And so that helped us get up and running faster.

Host: And at what point did you launch the first product and when did things begin to actually start working?

Tom Brown: So the first product that we launched was after ChatGPT. We had like a maybe nine months before ChatGPT. We had a Slackbot version of like Claude One.

Host: Oh yeah, we had that in the YC Slack actually.

Tom Brown: Yeah, yeah.

Host: Yeah, I remember like Tom Blfield adding all of you guys to it.

Tom Brown: It was really cool. And then I think that at the time though, we didn't know whether or not we wanted to launch it as a product. We didn't know if doing so would be good for the world at the time. I think we hadn't really thought through our theory of impact that much for like how we actually will make stuff work well. Plus, I think actually in hindsight, like if we had tried to launch it, we like wouldn't have had the serving infrastructure to have done it. And I think because we weren't sure whether or not we wanted to, we like hesitated for too long on building that infrastructure, which I think is learning for me.

Host: I mean, at this time, ChatGPT had not launched yet. ChatGPT hadn't launched, and so I guess we didn't know that it would be a big deal too.

Tom Brown: This is around the pandemic, 2022.

Host: This is summer 2022. Yep. And then ChatGPT launched fall 2022, and then we relaunched our API after that, and then Claude AI after that also. I think it didn't seem like it was working basically until Claude 3.5 and coding. I think like really really like through that whole time then until about a year ago, it seemed like it wasn't clear that we were going to end up being like a successful company.

Host: We actually saw that in the startups because we kind of get a bit of a vibe check in terms of what is the preferred model for startups. So all of 2023, OpenAI was the response. Then things started to turn in 2024 is when we saw Claude 3.5 and especially Sonnet was starting to get market share per se in the YC batches, going from single digit to at some point like 20% to 30%, and especially for coding.

Tom Brown: Yeah.

Host: Became the default choice, which was very interesting. Can you tell us about how that emergent behavior and the spikiness on that particular skill must be 80% now or 90%?

Tom Brown: Yeah, for coding even more, especially now Claude Code. What was that? Was that on purpose or just kind of happened?

Host: I think that we invested more in trying to make the model really good at code because we wanted the model to be good at code, was one thing.

Tom Brown: And you did it.

Host: Yeah. And then I think seeing the reaction of everyone to it was like, "Okay, yeah, like let's go much harder on that also."

Tom Brown: And this is before 3.5 Sonnet, you'd already invested enough in coding to realize that that was really promising and you decided to double down.

Host: I think this really was like individuals within the org being like, "We want to do coding," before 3.5 Sonnet. And then when we saw 3.5 Sonnet's really good product market fit, that was good signal to like go go for that.

Tom Brown: And do you guys know like the day that you guys launched 3.5 Sonnet, did you know that you had something really special and this was going to be the turning point for the company? Or were you as surprised as OpenAI when they launched ChatGPT and it just like unexpectedly took off?

Host: Yeah, I wish that we had like more foresight on that, but no, I think it was surprising for us too, like how big of a deal it was. And then I think 3.7 Sonnet also like surprised us by how much it unlocked like agentic coding. I think for each of these things, yeah, we move quite fast in rolling them out. And so we really often don't know what the results are going to be there.

Tom Brown: I think it's what made a lot of these coding agent startups work. I mean there's a crazy story of Replit going to 100 million in just 10 months, right? There's Cursor, of course, a story, and all built on all these with Sonnet.

Host: I think that all all of those things have been surprising to me. And then also just like in my working with Claude too, like I think I continue to be surprised by like the type of stuff that it can do. And I do think with each one there's like more stuff that kind of unlocks. But one of my friends was telling me that she had some code, some code source tool that she wanted to modify, but she didn't have the source code for it. She had the compiled binary, and she's like, "Claude, can you can you decompile this?" Like, "Yeah, can you disassemble the assembly?" And Claude chewed on it for 10 minutes and like made a C version of it. And so then she had the thing, which is insane. And she's like, "Yeah, like if I spent three days on it, I probably could have gotten the hex tables and like wrote a little code to do it. But like it did the whole thing, made up variable names for them, et cetera." So I do think that like we keep getting surprised by stuff that model has memorized all the hex tables. It can think through, try to work through it. I think we're going to continue to be surprised by that sort of stuff too.

Host: If you pull like the YC founders, they prefer using Anthropic models for coding by like a huge margin, that's much larger than what you would predict if you just looked at the benchmark results.

Tom Brown: Yeah.

Host: So there seems to be some X factor that makes people really like these models for coding. Do you know what it is and is it intentional in some way, or it just came out of the black box somehow?

Tom Brown: I think that the benchmarks are like easy to game, where I think that all the other big labs I think have teams where their whole job with the team is to like make the benchmarks scores good. And we don't have such a team. And so I think that I think that that is probably the biggest factor.

Host: You don't teach to the test.

Tom Brown: We don't teach to the test, because I do feel like if you start doing that, then like it has weird bad incentives. Maybe we could like put that team under marketing or something like that and then ignore all the benchmarks. But I think that that's one reason why there's some train test mismatch there.

Host: So the evaluations are more qualitative. But internally, do you have your internal—

Tom Brown: We have internal benchmarks, yeah. But we don't we don't publish them.

Host: And is it the internal benchmarks that the teams are really focused on improving?

Tom Brown: That's right, yeah. So we have internal benchmarks that the team focuses on and improving, and then we also have a bunch of tasks. Like I think that accelerating our own engineers is like a top top priority for us too. And so we we do a ton of like dog fooding there to make sure that it's helping with our folks too.

Host: Going back to Golden Gate Claude, there's a lot of sort of interpretability, seems like it's a big part of it. And then most people would say that, you know, Claude's personality just feels better. And then how do you sort of at once be very quantitative, but then also, you know, build evals around personality?

Tom Brown: The evals for personality are kind of complicated too, for like how do you tell if like Claude has like a good heart or something like that? It's like hard to hard to know. But I do think that that's like Amanda Askell's team's mandate is I think she describes it as like being like a good world traveler, where like it can like Claude goes and talks with all sorts of people from different backgrounds. And like each of the people should come from come to that being like, "I feel good about like this conversation that I've had."

Interpretability I think is like a long-term bet, right? Where it's like right now the models aren't that scary, but at some point they're going to be more scary. And so I think the hope there is to have some ability to know what's actually going on under the hood when it becomes more intense.

Host: Then more recently, Claude Code's been a real success. Can you talk us through like how did that project get started internally? And again, was it like a did you like know this time it was going to work or was it a surprise?

Tom Brown: Claude Code was an internal tool also. So like try to help out our engineers within Anthropic, that yeah, Boris had like hacked together.

Host: There's an internal Anthropic engineer wanting to build it for themselves.

Tom Brown: For internal for other internal engineers, yeah. For him and other internal engineers. And then I think yeah, I think we definitely didn't know that it would be successful out there. And I I think I think to some degree like we really had fully just bet on the API before that, with the intention being like there's like so many so many startups out there with so many good ideas. Who are we to like figure out what the right product is to build on top of this stuff? Everyone out there is going to build better stuff than us. And so put all of our effort into just making the best possible API. And I think that this surprised me as like, "Okay, like we actually were able to make something that like as a product was like better than the other products out on the market for this agentic" coding capability.

Tom Brown: use. I have like some theory that like part of that came from like a mind shift of seeing Claude as like the user, uh, for this thing too. For like, link that we were like trying to build things for teachers were like our users for Grouper, it was like single people in New York mostly I guess. Um, for this I think really the like users are the developers but also I think the users is Claude. It's like give Claude the right tools that Claude can actually do that effectively help Claude get the right context to work effectively. This team was like the most focused on Claude as like a user which I think makes sense that you guys would understand Claude the best.

Host: Yeah, I I do think that that's a place where like startup founders though like can can do that too. And I think that that's that's probably a rich vein for people to like make tools that are better for models as users.

Tom Brown: That's the perfect anthropomorphization of like the LLM itself. Like the agent is one of the stakeholders is one of the users that you would go after and try to like empower.

Host: Yeah. Yeah. Totally. Which actually makes a lot of sense why you guys actually got MCP to work to do tool calling because a bunch of other labs had tried to do something and the standard that stuck that really took off was yours.

Tom Brown: Yeah, I think that that seems like a similar one too where it's like model focused going back to Claude code. So like success is really exciting. It's also scary for like Cursor and other companies that have built on top of the API. Like what's your advice to founders building products like how should they think about building on the API but also worrying about like Anthropic or one of the labs building something better than they can build.

Host: I think I was kind of surprised that Claude code like we we did build a thing that was like uh like the best in the market there too. It's not super clear to me what the big advantage was for us for Claude code besides more empathy for Claude or something.

Tom Brown: That's actually I think that's actually really interesting insight. Like it seems like the thing that yeah, you were building for a specific user that you knew really well that other people wouldn't have thought to build for versus like you had some like intrinsic technology advantage.

Host: Yeah. Like I think a startup could could have done that same thing too, right?

Tom Brown: Yeah. I think we're the most like developer focused lab. I think we're the most like API focused lab too. So I think we want to make sure that we have the best platform for people to build stuff on cuz this thing is growing so incredibly quickly. Like we're not going to be the fastest at figuring out all the ways that we need to empower Claude to do the work that connects Claude to the entire human business that's like human human world is all designed for humans but like we need to get the models to be able to be productive members of uh the economy.

Host: Are there like ideas or areas you would love to see developers building in or like areas you don't, you you think are like underappreciated right now?

Tom Brown: Yeah, Claude code is like how do you get Claude to be a useful pair programmer kind of um or like junior engineer. You've got like a level two or three or something like that that you can work with or like very spiky because also it can do the like weird disassembly stuff that like a super high level suite would struggle with. Less good at knowing what type of work to do. Needs kind of a lot of handholding. Needs a lot of context from it. That's like one very particular subset of work that can be done. Uh if you look at like all the stuff that happens in businesses besides that, it's like a very tiny fraction of like all the work that's done in businesses that like a smart person who knows how to code and like use lots of tools but doesn't have that much context yet uh would want to do. So I think I think finding ways to coach Claude or uh co coach whatever model to like do useful tasks for businesses seems like there's just like a huge huge space there.

Host: So Tom, a big part of your job is like owning all the compute infrastructure that makes Anthropic work. Can you talk about like what what is the compute infrastructure behind this giant thing? Now, one thing that's interesting to look at is just that humanity is on track for like the largest infrastructure buildout of all time. Now, this is going to be larger than the Apollo project, larger than the Manhattan project.

Tom Brown: It'll be bigger than both of them next year if it keeps on the current trajectory, which is like roughly 3x per year increase in spending on AGI compute, which is just bonkers.

Host: Yeah. Like 3x per year is wild. I think it's going to keep up on the 3x per year trajectory. It's already locked in for that for for next year and then it's a little bit open for for 2027.

Tom Brown: I mean anecdotally internal to YC uh we can't get enough you know credits across all of the top frontier models including Claude. So you got to help us out a little bit.

Host: Yeah.

Tom Brown: We're just I mean everyone's bottlenecked literally every you know it's like give me more intelligence. I can't have enough.

Host: Yeah. And I know you guys have been looking at more hardware startups also for like more accelerators. I think that we will see more accelerators coming online to 2027. That's a good a good space. Also like data center tech I think is a big one.

Tom Brown: Where are the bottlenecks for you guys now? Is it like getting enough electricity, getting enough GPUs, getting construction permits?

Host: Power, people are using jet engines to get power. That's nuts.

Tom Brown: Overall for the buildout, I think power is going to be the biggest bottleneck, especially power in the US. Like we want to build in the US. That's one of our biggest policy goals is to like get the US to like build more data centers, permit more data centers, make it easier to build.

Host: Is the answer renewables or is it uh nuclear?

Tom Brown: I I definitely I feel like yes, yes, all all of those things. I wish I wish that nuclear was easier to build.

Host: Anthropic is the only major lab that uses not just one kind of GPU, but the GPUs from three different manufacturers. Can you talk about that and how how how that strategy has played out?

Tom Brown: Yeah. Yeah. So we use um GPUs, TPUs and Tranium. Downside of doing that is that we split our performance engineering teams across all of those platforms which is a ton of extra work. The positive thing is it gives us the flexibility to both one like soak up that extra capacity because there there just is more of those altogether than just one and then two is we can use the like right chips for the right jobs where some chips will be better for inference, some chips will be better for training and we can match the the right chips to the right jobs. So yeah, I think that that's kind of the the trade-off there.

Host: I guess one cool thing is just connecting the dots through your career and how all of this compounded because you you were the one engineer building that change of the architecture from TPUs to GPUs back at OpenAI that got GPT-3 to actually scale and now you're in charge of that at a much much bigger scale years later. I don't know if that kind of connected dots for you.

Tom Brown: The big move from TPUs to GPUs at OpenAI I think was partly driven just that PyTorch was a better software stack on top of them than TensorFlow on top of TPUs. And I think that that then unlocked fast iteration where like if you have like a good reliable software stack then you can experiment quickly just like build a whole system that works. I think that that's the thing that we really strive for now at Anthropic too is a challenge of having many more platforms is that it's harder to write all the good software. I think building the muscle of knowing how to build that software well so that all of the people who build on top of that low level can have a great experience with it is the most important thing there.

Host: Do you have advice for um kind of like a younger Tom version of yourself who now you've seen and went through this crazy journey? If someone was you back in the twenties living today and they wanted to ride and join the AI revolution, what would you say to them? And very specifically something we see from a lot of hear from a lot of college students at the moment is they uh they don't know what like if they should stay in college like are there going to be jobs for them what like how is the world going to change and what should they do?

Tom Brown: Taking more risks I think is is wise and then also trying to work on stuff where your friends would be really excited and impressed if you did it or a more idealized version of yourself would be really like proud of yourself if you succeeded at it I think is like probably the thing that I would I would try to tell a younger version of myself.

Host: More intrinsic less extrinsic like don't chase these other credentials and getting the degree or whatever you know working at FANG like those are just irrelevant.

Tom Brown: as of today.

Host: Yeah, exactly. That's all we have time for today. We'll see you guys next time.
