---
title: "Vibe Coding Is The Future"
slug: "ME-vibe-coding-is-the-future"
media_type: "Video"
author: "Y Combinator"
speakers: ["Diana", "Gary", "Gary Tan", "Harj Taggar", "Host", "Jared", "Speaker"]
categories: []
description: "Andrej Karpathy recently coined the term “vibe coding” to describe how LLMs are getting so good that devs can simply “give in to the vibes, embrace exponentials, and forget that the code even exists.” We surveyed YC founders to get their take on how this new way of programming is changing how products are built."
url: "https://ycombinator.com/library/ME-vibe-coding-is-the-future"
youtube_id: "IACHfKmZMr8"
youtube_url: "https://www.youtube.com/watch?v=IACHfKmZMr8"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Vibe Coding Is The Future

Andrej Karpathy recently coined the term “vibe coding” to describe how LLMs are getting so good that devs can simply
“give in to the vibes, embrace exponentials, and forget that the code even exists.” We surveyed YC founders to get
their take on how this new way of programming is changing how products are built.

## Transcript

Gary: Was like somebody dropped some like giant beanstalk seeds at night. We woke up in the morning going on. I mean, I think our sense right now is this isn't a fad. This isn't going away. This is actually the dominant way to code. And if you're not doing it, like you might just be left behind.

Gary: Welcome back to another episode of the Lightbulb. I'm Gary. This is Jared, Harj, and Diana. And we're partners at Y Combinator. Collectively, we've funded companies worth hundreds of billions of dollars right when it was just an idea and a few people.

Gary: So today we're talking about Vibe Coding, which is from an Andrej Karpathy post that went viral recently. There's a new kind of coding. I call Vibe Coding where you fully give in to the vibes, embrace exponentials, and forget that the code even exists.

Gary: So we surveyed the founders in the current YC batch to get their take on Vibe Coding. And we essentially asked them a bunch of questions. We asked them what tools are you using? How has your workflow changed? And sort of generally, where do you think the future of software engineering is going? And how will the role of software engineer change as we get into a world of Vibe Coding? And we got some pretty interesting responses.

Host: Anyone have any favorite quotes that jumped out from the founders?

Jared: I think one of them that I can read verbatim is: "I think the role of software engineer will transition to product engineer. Human taste is now more important than ever as coding tools make everyone a 10x engineer." That's from the founder of Outlet.

Diana: I got one. Obby from Asura said, "I don't write code much. I just think and review." This is like a super technical founder whose last company was also a dev tools company. He's extremely able to code. And so it's fascinating to have people like that saying things like this.

Diana: There's another quote from a different founder. RB from Copycat said, "I am far less attached to my code now, so my decisions on whether we decide to scrap or refactor code are less biased since I can code three times as fast. It's easy for me to scrap and rewrite if I need to."

Diana: And then I guess the really cool thing about this stuff is it parallelizes really well. So Yoav from Codix he says, "I write everything with Cursor. Sometimes I even have two windows of Cursor open in parallel and I prompt them on two different features."

Jared: Which makes sense. Why not three, you know? Do a lot actually.

Diana: And I think another one that's great is from the founder of a train loop. He mentions how coding has changed. Six to one months ago, 10x speed up. One month ago to now is 100x speed up. Exponential acceleration. And he says, "I'm no longer an engineer. I'm a product person."

Gary: Yeah, that's super interesting. I think like that might be something that's happening broadly, you know? It really ends up being two different roles. You need—I mean, it actually maps to how engineers sort of self-assign today. In that, either you're front-end or back-end. And then back-end ends up being about actually infrastructure. And then front-end is so much more actually being a PM. You're sort of almost being like an ethnographer going into the obscure, underserved parts of the pie of GDP. And you're trying to extract out like, "This is what those people in that GDP pie actually want." And then I'm going to turn that into code. And then actually, evals are the most important part of that.

Gary: When I was running Triple Byte, this was actually one of the things we noticed. It was almost as important as a technical assessment of engineers when trying to figure out who's a good match for a specific company. There's a certain threshold of technical ability you need, but beyond that, it was: do you actually want to talk to users or not? Some engineers are actually just very motivated by working on things where they know who the users are and they get to communicate with them and they get live feedback and they can iterate. And essentially being a product engineer. And other engineers really don't want to do that at all. Like, they find it annoying having to deal with users. And they want to just work on hard technical problems and refactor back-end engineering.

Jared: Yeah, that's what we call a back-end engineer.

Gary: Yeah, sure. And that's a theme that came up in these survey responses, right? This idea of sort of the LLMs are maybe going to push people to choose. The actual writing of the code may become less important. It's about: are you really doing this? Do you have taste and you want to solve product problems? Or are you an architect and you want to solve systems problems?

Diana: Oh, and interestingly, I guess one thing the survey did indicate is that this stuff is terrible at debugging.

Jared: Yeah.

Diana: And so you still—the humans have to do the debugging. They have to figure out: well, what is the code actually doing? Here's a bug. Where's the code path that you know we have some logic error? You know, just didn't figure this out right there. There doesn't seem to be a way to just tell it to debug.

Gary: You were saying that you have to be very explicit, like as if giving instructions to a first-time software engineer. You have to really spoon-feed the instructions to get it to debug stuff. Or you can kind of embrace the vibes. I'd say Andrej Karpathy style is just like ignore the bug and just roll—just tell it to try again from scratch. Like, it's wild how your coding style changes when actually writing the code becomes a tax, cheaper. Like, as a human you would never just blow away something that you'd worked on for a long time and rewrite it from scratch because you had a bug. You'd like fix the bug. But like for the LLM, if you can just rewrite a thousand lines of code in like six seconds, like why not?

Diana: That's kind of like taking the approach of how people use Midjourney or Playground when you're trying to generate images. Like, if there are artifacts or things that I don't like, sometimes I don't even change the prompt. I just click roll and I do that five times and sometimes it just works. I'm like, "Oh, I can use that now." Which is very different from the frame of building systems because you're not building foundationally step-by-step. You're really doing it from scratch because fundamentally what's going on is like all these tools today are coming from the world of AI-generated code that are in this latent space hidden somewhere and you have to do it from scratch to find like a different gradient and not get stuck. And then you want to add a bit of randomness, get it to regenerate.

Jared: But I do think maybe I don't know, whatever next generation—O5 maybe—we'll get to the point that actually is able to build upon. I mean, as of right now, I think most of it is you need to reroll and rewrite, but it doesn't build upon it yet.

Diana: But we haven't seen any of the coding tools right now work well with reasoning.

Jared: I think we have. Well, O3 is infinitely better at debugging than 3.5 Sonnet. So like, it definitely feels like we're headed in the direction where this may not be true in you know six months. The next time we do this episode, Diana, do you want to talk about the models that people are using? The IDEs that the people are using? There's some really interesting trends there.

Diana: Yeah, I think as we mentioned a couple episodes ago, we already saw this shift. It started happening back in summer 2024 when Cursor was being used by a big portion of the batch. And now, by far, is the leader. But the other thing that's happening—this is a very fast and moving environment—Windsurf is a fast follower. It's starting to be a very good product as opposed to Cursor.

Jared: I think the number one reason that people are switching is that Cursor today largely needs to be told what files to look at in your codebase. So you have a large code base. You can tell it what to do, but you have to tell it like where to look in the code base. Windsurf indexes your whole code base and is pretty good at figuring out what files to look at on its own. There's other differences too, but I think that's the most important one at the moment.

Diana: Notable Devon does get mentioned, but the drawback of Devon not really being used for serious features is that it doesn't really understand the code base. It's being used mostly for small features and barely. It's like barely mentioned. The other one—people still use ChatGPT. And the reason they use it is because they want to actually use the reasoning models. So D.O. gets posted. People post some of the debugging questions to use the more powerful models for reasoning. Because right now, Cursor and Windsurf are still in the old world—I mean old world, less than six months ago—of pre-reasoning models, not in the test time compute. So founders are using that.

Diana: And there's some founders—some of them are self-hosted as well. Self-hosting models because maybe they have more critical, sensitive IP. They do that. And now, talking about the shifts in terms of models, the big name in town that we saw six months ago was Claude Sonnet 3.5. It's still actually a big contender. Most are still using it. But O1, O1 Pro, and O3—meaning all these reasoning models—are starting to see it. It's almost like getting neck-and-neck now, close with Claude Sonnet 3.5.

Diana: The other one is GPT-4. Virtually no use for code. And the other interesting thing is DeepSeek R1 is getting mentioned. It's been in use. It's like a viable contender as well. And Gemini? Not really mentioned. The one thing I've heard from Gemini is because it has like the longest context window. I've heard from a couple of founders that they do use it. And the way that they use it is they put their entire code base into the Gemini context window and they just tell it to like fix a bug. And it doesn't always work. But like, sometimes it can just on-shot fix it because it has the whole thing in the context window.

Diana: It will be interesting to see as people get more adoption on the newly released reasoning models with Flash 2.0. I don't think people have tried it yet. But the long context window plus reasoning could be a good contender.

Host: What is the estimated code that's being written by LLMs in the current batch? This is pretty crazy.

Diana: So we explicitly asked this question: What percent of your codebase do you estimate is AI-generated? The way I interpret the question is like the actual characters in your code base—not including any libraries that you imported—like, what percentage of the characters were typed by human hands versus emitted by an LLM? And the crazy thing is one quarter of the founders said that more than 95% of their code base was AI-generated.

Gary: Wow, which is like an insane statistic. And it's not like we funded a bunch of non-technical founders. Like, every one of these people is like highly tactical, completely capable of building their own product from scratch. A year ago, they would have built their own product from scratch. But now 95% of it is built by an AI except for, you know, maybe—it sounds like we have one or two examples of people who are so young that they learned to code in the last two years. So they actually don't know a world where Cursor didn't exist.

Jared: Yeah, this is one of my best companies this batch, actually. It's exactly this. The founders are extremely technical minds, but they're not classically trained in computer science and programming. And they are incredibly productive and able to produce just a ton of like really amazing product. And AI is writing almost the entire thing.

Gary: It kind of makes me think a lot of the discourse around sort of how these are the first digital natives that grew up with the internet. This is like the generation that grew up with native AI coding tools. They skip the classical training of a software engineer and they just do it with the vibes. But they are actually very technical minded. I mean, they have degrees in math and physics.

Diana: Physics, yeah. So they have that raw, let's call it, more like system-thinking type of mind that you still need. Maybe we should talk a bit about that. It's like what's still the same and what has changed.

Gary: I think Vibe Coding will enable people who have those kinds of tactical minds who come from other tactical disciplines like math and physics to become highly productive as programmers much faster than it was in the past. Like, I remember there were coding boot camps back in the day. They would try to retrain physics people into programmers. And like, it didn't work that well because it just takes too long to learn all of the syntax and all of the libraries and all the stuff that you have to know to be really productive. But like, now it's a new world.

Diana: The boot camps are also very specifically focused on getting you hired at companies. And then I think there was—it was during this around like 2015 era—where just companies themselves were rethinking how to evaluate software engineers in their hiring processes. And there was a real shift away from like, "We want to hire classically trained computer scientists"—whiteboard algorithmic problems—towards, "We actually want people who are just really productive and write code quickly."

Gary: And some of these arguments are like evergreen, right? Like, I remember when Rails first came out, there was just like a real sense of, "Oh, like, I don't know. Active Record as a way to interact with your database was seen as a great abstraction. But there was still this same flavor of argument, right? Like, oh, you know, if you don't really understand the internals, like you're just going to write like crappy, low-performing web software." How do you feel those arguments have aged if you look back on it now?

Jared: My feeling is that many of the most successful companies—I would say Stripe and Gusto are just two that really spring to my mind—are ones that really heavily leaned into, "Actually, we just want people who are really productive with the tools, and we're going to change our whole hiring process to just select for people who are good at—" The interview shifted from, "Teach us how you think" to "You've got three hours on a laptop and you need to build a to-do list app and build it as quickly as you can." And those companies have had a tremendous amount of success.

Gary: It does seem like at some point as they grew and they scaled, then the bottleneck did actually become having people who were classically trained and systems thinkers to sort of scale up and architect things.

Diana: It does seem like how people are hiring engineers is changing, but maybe not changing fast enough yet. The results of the survey are relatively surprising to the four of us here. Probably pretty shocking out there. It's just like this thing that popped up in our backyard only in the last six to nine months. My guess would be engineering hiring period has not actually caught up to this. People are still standing at whiteboards and doing that kind of thing as opposed to, "What can you get done?"

Gary: And so it sounds like the Stripes of the world, they were ahead of the game. And everyone has to hire engineers this way now.

Jared: I mean, I wonder if actually even that's going to be sort of the old method. I mean, something that stood out from the survey responses was this idea of two themes we talked about, right? Like, one is, "How? Okay, we're all just product people now. Like, actually, the thing that you need is really great taste and understand what to build." And the second was, "Actually, now what's really valuable is to be like a systems thinker and an architect."

Jared: To really understand the bigger picture. In which case, actually, like, maybe being a really productive coder—because that's definitely something that always fit my definition of when you're talking about who are great engineers, you know? And like, that's one of the dimensions that they're just really good at—they can write code really fast. Like, maybe that's outdated. Like, maybe that's not. If the LLMs are actually really good at writing code quickly, your role and iterating from scratch, debugging the builds, might be completely different.

The problem is there's like two different stages. There's zero to one, in which case speed is the only thing that matters. And then to your point about Active Record and Rails—that battle was actually fought to a standstill because, of course, using Active Record or Rails allowed you to go from zero to one very quickly. But then what happened to Twitter? It became the fail whale, right? Like, basically once you get to one—like one—you know, that architecture will not get you to a billion or ten billion or hundred billion dollar valuation or users or whatever. Like, it's just not going to actually work.

So I think you're going to see the same thing. And then there's nuance in what you just said, right? Like, getting zero to one quickly and then being able to scale to a billion users are two totally different sets. And then I think that might be irreplaceable for now around people. And one of the things I discovered as we were scaling one of the biggest Rails sites—I mean, you scaled one of the biggest Rails sites too—is that there aren't that many people who have to do it. Getting to one is so rare.

Speaker: Yeah, that's true. That, uh, did you reach this point where how you got to zero to one very quickly was like you use lots and lots of open source? And then at some point, like maybe two years into this, maybe a year and a half into the startup, even we could not use random gems anymore—gems anymore—because they were just never designed for companies at scale. And so we have to, and it just falls over, right? This very good examples of what you're saying, Gary.

I think maybe to summarize a bit more: zero to one will be great for vibe coding where founders can ship features very quickly. But once they hit product-market fit, they're still going to have a lot of really hardcore systems engineering where you need to get from the one to N, and you need to hire very different kinds of people. And to that, I think there's very good historical example like Facebook as well. I mean, they got away with PHP, which personally is a terrible language. Yeah, maybe I get flamed, but I think it's a bad language.

Gary Tan: I'm with you. I never liked it. Sorry, guys, it was very bad.

Speaker: But you could ship things very quickly. But at some point it became such a big bottleneck for them to ship features that they had to hire the hardcore systems people to build a custom compiler, HipHop, yeah, so that it would run fast on bare metal because it was just too expensive to replace all the code. Yeah. And those kind of people that did that are not the vibe code people—are sort of these hardcore systems people that, based on our survey, current tools are not good at that low-level systems engineering.

Harj Taggar: I'm not sure everybody who's listening knows what TripleByte is, but it's actually very relevant. You do—you want to just describe for everybody?

Speaker: Yeah. TripleByte is the company I started in 2015, and our goal—we were essentially building a technical assessment for engineers. Like, our goal was, how can you use software to automate evaluating software engineers? And the way we did it was pre all these LLM models. Which is we built all of our own custom software to interview engineers, have humans interview engineers, and then essentially just, like, label the data like, in and interview them by, like, asking them to write code. They highly technical interview, yeah. It was high, yes, like it was aching to write code. Um, we did actually include algorithmic problems.

Harj Taggar: Is it true that you and your co-founders have done more technical interviews than any other people on the planet?

Speaker: I think so. Like, in terms of just like pure hours, because it was—that was just like the early days of it were like all every day, just thousands and thousands of them, right? Um, and then we scaled up and we had like a team of about a hundred engineers contracted just that we would pay per interview completed.

Jared: And so you're exactly the right person to ask this question. You've literally spent more time thinking about this than anyone else on the planet. Um, if you were starting TripleByte again today and you had to design like new tactical assessments for engineers, what would you have them do?

Speaker: The big takeaway I had with TripleByte and the screening in particular is just people want different things. And so you kind of need to know up front like what exactly it is that you're evaluating for, and then design your technical screen around that. It's kind of what I'm getting at with where Stripe and Gusto and these companies just knew that they didn't care if someone had fundamental CS knowledge, so it didn't make sense to screen them on that. Like, they wanted to screen for the thing that they were actually going to do in their job. And then our product was more trying to screen for everything—company trying to get a taste of everything companies might want—and then figure out what someone's max skill was. Um, and then send the people with the max skill to the companies that would value that max skill.

In today's world, I think I would actually have a screen that at least accounted for just how well people knew how to use these tools. Like, and so again, it's maybe contradicting what I'm saying earlier, but it might be the case that maybe how quickly you can code and can build product is actually something to explicitly screen on. Um, just at the bar much higher. You probably have to ask different questions, because I'll bet if you go back to the original TripleByte assessment, I bet a lot of those questions you could literally just copy and paste the question into ChatGPT and it would spit out a perfect answer. In which case you're not really proving that much competence if you're just copy—like, the questions probably have to be like a hundred times harder.

Jared: I mean, this gets at the deepest stuff, right? Not necessarily, because if you have someone else monitor it, it depends on like what conditions you're going to put on the screen, which are things interesting. So I know a classic question was like build tic-tac-toe?

Speaker: Um, yes, of course. If you do that unsupervised and you just let someone, like, come back with their tic-tac-toe solution, that's going to take like two seconds, right? Um, um, if you want to watch them code and force them to not use an LLM, I guess that's a question: do you force them to code it without an LLM? With like the old questions? Or do you let them use an LLM, and now you need new questions because the other ones became trivial?

Gary Tan: I think that is what everyone hiring software engineers right now should be thinking about and trying to figure out.

Speaker: Yeah, I'm not sure I know what the correct answer is to that.

Jared: Yeah, I think there going to be probably—you're going to test for different things because I also did a lot of engineering hiring. I think one key skill that's going to—I think remain that's constant—I do think skills of reading code and debugging are—maximum is like you have to have the taste and enough training to know that the LLM is spitting bad stuff or good stuff. So like bad code or good. And I think you can see it clearly sometimes if a candidate is using the tools, and there's actually a reasonable solution that the LLM outputs, and then the candidate is like, oh, this is actually bad. That is a sign. So I think knowing kind of more the high-level thinking to know what is good versus bad in order to do good vibe coding, you still need to have the taste, and you still need that kind of classical training, maybe not necessarily classical training, but enough knowledge to judge what's good versus bad. And you only become good with enough practice, I think. That will be one that will be constant. That would be my opinion.

Speaker: Yeah, that's interesting. Just coder—it's like more like code review as the interview versus like actually like producing code?

Jared: Yeah, I mean, you could have some form of system design. You want to know how good they can put a product out there. So then is testing for taste? So we're going to test for debugging and then taste. But then how do you get to—I guess this is a question going to these kids that you have that we call it AI coding natives. Yeah, how do you develop taste when you don't come from a classically trained world? Which would be interesting for next generation.

Speaker: Well, you have to, because if you don't, the startup dies, right? So let's say this founder, they go off, they have 95% written by AI. The proof is in a year, two years out. Um, they, you know, have a hundred million users on that thing, you know? Does it fall over or not? And then one of the things that's pretty clear is these systems, uh, you know, in the first realm, the first versions of reasoning models, they're not that good at debugging. So you actually would need to descend down into the depths of what's actually happening, yeah. And if you can't, then you got—I mean, let's hope that they can go find another architect. They're going to have to hire someone who can.

Jared: I think there going to be a generation of software engineers that are like good enough because it's so easy to retool there with with all these coding tools. Like the barrier to entry is so low you're going to be good enough engineers. There's going to be tons of those. But to be exceptional, like the top one percent, I think you're going to need to get into deliberate practice.

I mean, the analogy we're talking about is uh, Malcolm Gladwell popularized this concept of 10,000 hours of practice to become an expert, which came from this research from uh, what was his name? The uh, Anders Ericsson?

Speaker: Anderson Ericsson, right?

Jared: Which it wasn't just the research was very specific. It was about uh, how do you find world-class violinists? And it wasn't about just putting in the time, but deliberate practice. It's like hours that actually plan and thought and is hard work. You could become an expert with less hours. So I think what's happening with coding tools now is that it's very cheap to put in the hours because the output is just so quick. You can get to good enough. But to become the best in the world and the best founder, you're going to need that deliberate practice to go into the details and you're going to have to peel the onion and understand the systems and get to, again, to some extent, being classically trained.

I mean, a good example is maybe we go back to history is like Picasso. One of the greatest painters, it was amazing at drawing lifelike pictures, which is not what he's famous for, of course. When you imagine a Picasso you imagine the opposite of that, yeah? There's this famous sequence of drawings on how he got to abstract work. It starts from being lifelike to iterations until he gets to the essence, to kind of the abstract art that he's very well known for. But he could only get to be the best in the world because he was actually a very good painter and classically trained and could draw super well. But that's not what he's known for. So I do think we'll see these two classes of engineers. You'll still have like a very fat class of like good enough. You need engineers for those. But the best in the world, the founders that become outliers, are going to need to put in the deliberate practice.

Speaker: Yes and no. I mean, I think uh, there are lots of really amazing examples of um, great systems-level, world-class engineers who ended up being CEO and CEO of the biggest public companies in the world. I think of Max Levchin. I think of Toby Lütke from Shopify. I mean, these are people who just like actually are great. Um, and the thing is there are lots of other people who were not that great but also still CEO or co-founders of companies. And then it kind of goes back to to link up what we were saying earlier. It goes back to hiring.

I mean, I I keep thinking about the Twitter analogy that you brought up because I think it's a really interesting one. Like, if you compare Facebook and Twitter, in both cases they went very quickly from zero to one in sort of scrappy, move fast, break things way. Um, Facebook was able to solve the scaling technical challenges in a pretty impressive way. I think most people would agree. I mean, Mark Zuckerberg was by far way more technical, way more in the weeds. Probably, maybe, but I I don't know. Like I think Twitter's scalability challenges were also harder based on the usage patterns. Like, the thing about the usage of Facebook is that it grows—it's pretty smooth throughout the day. Like, people just use it all the time. The problem with Twitter is that the usage is incredibly spiky. You get like a Super Bowl or like a, you know, like a world event, and all of a sudden you have like ten times as much usage. The way the fan out of the feed works is I think like fundamentally a very difficult computer science problem.

Jared: Okay, that's fair. Though, I also think that they were like really hamstrung by their tools. Do you remember using this terrible Q system called Starling? AB?

Speaker: I used it because I thought, oh, Twitter's so much bigger than us. They're so smart. They wouldn't use something that's crap. No, they totally use crap. And then I use crap. And I couldn't make it work. It was like it was dropping jobs on the floor. Like, it's like all these crazy bugs happened. And then I was like, finally, I was like, I'm not using that anymore. I have to switch to RabbitMQ or whatever the heck the actually correct thing to use was.

Jared: Yeah. And like, Ruby is an incredibly slow language—even like ten times slower than PHP, which was already too slow. So I don't know. I mean, basically you should be so lucky to get to one, yeah? Is there an advantage for a technical founder to be classically trained and be a really deep systems thinker?

Speaker: Well, I mean, you just—I mean, a Toby or a Max Levchin is not going to get bullshitted by people. From Stripe is the same. I mean, I'll tell you a crazy story. Uh, when I was uh, at Palantir, here, you know, I sort of burnt out there after a couple years. After I designed the logo and then I actually between that and going to start my YC startup, I spent six months as an interaction designer. And I was—it was this like terrible venture-backed company that ended up going in the ground. And it was like credit card software. It was the worst. I spent six months building uh, like basically just interaction designs, which was really fun. That's what allowed me to work on my startup in my spare time because I had a lot of spare time. But I remember designing um, you know, this faceted search thing for like rental cars or something like that. And then I go into my meeting with my dev manager and engineers who were going to implement it. And they were like, oh yeah, it can't be done. We can't do it that way.

Oh, like, and I was like, what are you talking about? Just make the indexes like this. And they were like, whoa, what do you mean? Like, and then they looked up my resume, hear that going, that from the interaction designer?

Yeah, basically they're like, how did you know that? And I'm like, you lied to me. And that's the thing, like, what founders—and like, you know, when you're hiring people—what—like, that that was like the wildest thing to me. But it was like sort of the ultimate lesson where it's like, when you're in the workplace, you sort of assume that the people you bring on, like, they're not going to lie, they're not lazy. Like, we're all for the goal and the mission.

Speaker: Right, and I like—no, like people who hire you, they totally will lie to you if you cannot tell that they're lying. And then the worst part is like you kind of have to call them on it. Like, you know, sometimes you have workplace cultures that are so polite that people are like, "Oh, I'm going to let that pass," and then I'm going to talk shit about them behind their back. And it's like, you should fire them. The AI agents, incidentally, will do exactly the same thing. They will absolutely—like, the AI agents will shit you just like a human employee will, if you don't—if you're not technical enough to like call them out on their shit and be like, "No, like you didn't make the change that I—" It goes back to your point about like why being classically trained is still helpful. Like, you have to be able to call out all the people working for you, whether they're human or not. Being technical enough to be able to do that is a superpower.

Speaker: So just to wrap up: basically what's going on with all these tools is giving superpowers to the best engineers and making bad engineers also worse. This is a quote from the founder of a train loop about how coding has changed. Six to one month ago: ten X up. Now, one month ago: one hundred X up. Now it's exponential acceleration. Sort of crept up on us, actually.

Speaker: Yeah, it was like somebody dropped some like giant beanstalk seeds at night, we woke up in the morning—what's going on?

Speaker: So I mean, I think our sense right now is this isn't a fad. This isn't going away. This is actually the dominant way to code. And if you're not doing it, like you might just be left behind. This is just here to stay. And you know, vibe coding is not a fad. It's time to accelerate. So with that, we'll see you guys for the next lightcone.
