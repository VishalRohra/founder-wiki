---
title: "How This 25-Year-Old Built A $675M Legal AI Startup (With No Legal Experience)"
slug: "Mq-how-this-25-year-old-built-a-675m-legal-ai-startup-with-no-legal-experience"
media_type: "Video"
author: "Y Combinator"
speakers: ["Gustaf Alstromer", "Host", "Max Strand"]
categories: []
description: "At 23, with no legal background, Max Junestrand co-founded Legora to transform how lawyers work. Today, Legora’s AI workspace is used by tens of thousands of lawyers, including top law firms like Goodwin and Cleary Gottlieb— and is valued at $675M just 13 months after launch."
url: "https://ycombinator.com/library/Mq-how-this-25-year-old-built-a-675m-legal-ai-startup-with-no-legal-experience"
youtube_id: "pHuXCzM2ntU"
youtube_url: "https://www.youtube.com/watch?v=pHuXCzM2ntU"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# How This 25-Year-Old Built A $675M Legal AI Startup (With No Legal Experience)

At 23, with no legal background, Max Junestrand co-founded Legora to transform how lawyers work. Today, Legora’s AI
workspace is used by tens of thousands of lawyers, including top law firms like Goodwin and Cleary Gottlieb— and is
valued at $675M just 13 months after launch.

From due diligence grids that turn days of work into minutes, to Word integrations that renegotiate contracts, Max sat
down with YC General Partner Gustaf Alstromer to share how Legora won over skeptical firms, scaled from 10 to 100
people, and built a new category in legal AI.

## Transcript

Gustaf Alstromer: AI is continuously developing super, super quickly, and that means we need to do the same. We're finding that as we go deeper and deeper and deeper in the entire legal software stack, we're also seeing that the line between software and service is blurring. I think that's been one of our strengths as a company to say we don't know exactly where the future's going, but neither do you. So let's work together to make sure that we're both winners in whatever happens. Today, I'm joined by Max Junior Strand. He's the CEO and co-founder of Legora. Legora was in winter '24, and they are the leading AI workspace helping lawyers and legal professionals do their work. Welcome, Max.

Max Strand: Hey, thanks Gustaf.

Gustaf Alstromer: It's been thirteen months since you did the batch. It's been a really busy year for you.

Max Strand: It has. Uh, it feels like it was a really long time ago. I feel like I've aged five years in the last one.

Gustaf Alstromer: For those who don't know, tell us about Legora. Yeah, what are you guys building?

Max Strand: At Legora, we're building the AI-powered workspace for lawyers. We're essentially transforming the way that they complete their work. Everything from reviewing, drafting, researching. Essentially, within legal, you've had this incredibly fragmented software space where there was a lot of point solutions, and AI was never good enough to actually work with unstructured text, precedent, legal documents. And when GPT-3.5 got out, that just completely changed the game. So we were quick to build a prototype, and then now we've scaled that all the way to an enterprise-grade system serving tens of thousands of lawyers daily.

Gustaf Alstromer: Those point solutions were basically workflow tools. So what were they before? Because it's been a history of a legal technology industry that existed before. This is not started right now.

Max Strand: No, I mean legal tech has been a category for a long time, but it was really unsexy for a long time, I think. And you'd essentially have a broad range of point solutions. Everything from templating tools where you would sort of codify a contract to spell-check translation tools or redline tools or research tools. And all of them work with text somehow. And generative AI came into the game and just kind of threw everything off the table. And then when it landed, you very clearly saw how you could solve a lot for a lot of these use cases with the same underlying tech.

Gustaf Alstromer: So ChatGPT came maybe eight months prior to you guys starting this company. Describe that moment. Was that an important moment for the company's founding?

Max Strand: We were playing around in AI and legal way before ChatGPT, and we were using these early models from BERT coming from Google. They were decent in English, but they were just horrendously bad in Swedish. And you know, the first observation that kind of sparked the founding of the company was one of the co-founders' friends who was a lawyer spent four months during a summer just summarizing court cases for a big law firm. We basically saw that GPT-3.5 was released to developers, started building. I think the first thing that we built was a stock option reader that would explain how a stock option contract worked.

Gustaf Alstromer: Useful.

Max Strand: Right. You know, as startup founders with no legal background, that seemed reasonable. And then very quickly the sort of focus changed to how do we build this more wall-to-wall or end-to-end system that every legal professional wants to work with on a daily basis? And the first product was really quite simple. Uh, especially building for Europe, you got to go through a lot of hassle to kind of conform with all the data processing requirements. So, you know, all data hosted within Europe, nothing for training, no retention, exemption from human review. When you look at the way Azure and AWS is structured, we kind of jumped through all those hoops and just built a system that was compliant for law firms to work with. And then very quickly, as the general sort of AI platforms continued to develop with ChatGPT, with Claude, with Gemini, the requirements for what we had to build to be much, much better, you know, continuously increased.

Gustaf Alstromer: In some industries or some categories, like coding or law, for example, it seems like the models are just magical. Like, they do things that the people that were in those industries before could not even imagine be possible. Could you describe sort of like the first time you used Legora to do something that was magical for a customer and how they experienced it?

Max Strand: Yes, I think the first time was when we deployed Legora into the biggest, largest law firm in the Nordics, man. Um, they, their managing partner had a famous saying in the newspaper that AI was more artificial than intelligent, which was back from the early models.

Gustaf Alstromer: Yeah. I mean, a lot of firms burnt themselves buying expensive tools that didn't solve anything.

Max Strand: And I came into that meeting, you know, I bring out my laptop and I just ask him, you know, put in a query.

Gustaf Alstromer: And he puts in this uh legal research query, and we've tied Legora to Swedish legislation with a RAG system. Yeah. And it answers perfectly.

Max Strand: And you know, you kind of see it on his eyes like it's the aha moment. And now when we're...

Gustaf Alstromer: Is that your aha moment as well?

Max Strand: No, I think my personal aha moment was just using ChatGPT generally, right? Like it was amazing. It felt completely sci-fi that you could talk with the computer and it talked back. And you know, as an entrepreneur, you kind of quickly understand that, all right, we can apply it in this space in this way and in that space in this other way. And I think for legal-specific, the chat experience I think was always cool, but when we took the same models and sort of applied them differently, um, one of the first use cases we did was due diligence, where you have hundreds, or you know, a lot of documents that you want to review. And instead of going through them one by one by one, we just made this large grid where essentially every document represented a row.

Gustaf Alstromer: And then you could put your queries in the columns, right?

Max Strand: And as you then put in, you know, one hundred employment agreements and you ask, uh, does all of them include an IP clause where the company protects its intellectual property? And it just starts to rattle and it goes, yes, yes, yes, no, no, no, yes, yes, yes. And it always links back to the citation. And you realize, like, holy, this is transformational. It's taking tasks which used to be, you know, days or hours, and it's turning them into minutes.

Gustaf Alstromer: By the time this is live, uh, you will have announced that you have raised uh Series B. How much did you raise?

Max Strand: We raised eighty million dollars, led by Iconic and General Catalyst. And you know, grateful for YC's continued participation, as well as Benchmark and Red Points.

Gustaf Alstromer: What is the software like? So, as a lawyer using Legora, what does my day-to-day look like?

Max Strand: So it's really broken up into two pieces. The first one is the web application, and the second one is our Word add-in. So we integrate directly into Microsoft Word.

Gustaf Alstromer: Right?

Max Strand: So if we start with the web application, the first thing that we had was just a simple chat over your own documents and files. This has quickly developed into its own agent that's able to use a lot of the other endpoints in the app and also external tools to solve more complex, sort of step-by-step workflows.

Gustaf Alstromer: Mm-hmm.

Max Strand: So you could imagine saying, um, hey, I want to write a memo, and the first step of the memo is to go out and do some research. The second step is to take all that research and conform it into the standard language of the firm, and the third step is to write the report and then output is a report.

Gustaf Alstromer: And does it do all that?

Max Strand: It does all of that.

Gustaf Alstromer: Wow.

Max Strand: Right. Um, and I think we can talk more about it later, but MCP and the way that you can scale the tool usage of these agents is something that I'm super keen on, and that we're leaning very heavily into because a lot of firms have different needs in terms of how they want to adopt the tools to solve for their specific workflows. And it's different if you work in intellectual property or if you work in restructuring or if you work in corporate or if you work in disputes. The second piece outside of the chat is uh well, the grid that I talked about before. We call it tabular review.

Gustaf Alstromer: Yeah?

Max Strand: Um, it's essentially input any number of files and then input any number of queries, and we sort of cross-run that across each other. And the big innovation there does not really come from, you know, how do you prompt and work with the model, but it's how do you make this run at scale.

Gustaf Alstromer: Right?

Max Strand: You know, how do you run one hundred thousand queries in parallel at the same time and make sure nothing breaks, all the citations are correct? There's a lot of chunking, sort of RAG searching within the individual documents, because sometimes they're very, very long.

Gustaf Alstromer: Yeah?

Max Strand: And with legal docs, there are certain intricacies where you need to always include things like the definitions.

Gustaf Alstromer: Yeah?

Max Strand: And there might be cross-references within each clause to each other. So taking all of that into consideration, that kind of serves the grid. Looking at the Word add-in, I think you could phrase it as Cursor for lawyers.

Gustaf Alstromer: Lawyers basically use Word. That's that's a like a known fact for a long time.

Max Strand: Yeah. I mean, they draft and they review contracts in Word or PDF form. And what we really wanted to do is, similar to Cursor, how do we bring generative AI into the existing work environment of a legal professional? And that means integrating in Word.

Gustaf Alstromer: Now, the difference is you can't fork Word and you can't take up all the real estate you want. You're basically confined to this sort of right-hand column.

Max Strand: And then you got to get really creative. It's basically like designing a mobile app, almost, because that's all the real estate you get. And the first thing that we built there was just, you know, how do we integrate an assistant or a chat that's able to not only read the document but also create edits. So you might say, I want you to, um, you know, renegotiate this MSA for the buyer.

Gustaf Alstromer: Yeah?

Max Strand: And do that using this internal checklist that I have or this internal sort of playbook or precedent. And now we've scaled that to not only work in a chat-by-chat basis, but also more extensive workflows. So you can say, here's a contract. I want you to take my playbook that consists of twenty different steps and make sure we negotiate from the starting positions and have, you know, different fallbacks included.

Gustaf Alstromer: Do you have a specific example of something that was impossible a couple years ago for a lawyer? Like, literally, you couldn't do it, and now you can do it?

Max Strand: Yeah, I mean I think, well, there's a lot of it, right? The early ML models were really bad at legal language, and what they were really bad at was when the language looked different across documents, right? You could train a system to find, let's say, a change of control clause if it looked the same way across all the documents.

Gustaf Alstromer: Yeah.

Max Strand: But it was really frankly bad at finding the meaning of a change of control if the clause didn't look that way.

Gustaf Alstromer: Mm-hmm.

Max Strand: And so what the LLMs have allowed us to do is to just take tasks where, especially on like large contracting and large document extraction. So how do we pull the insights from this? Another one is just, you know, redlining. So redlining files within Word against a precedent or playbook, completely impossible. Or take deep research across, you know, hundreds or thousands of judgments where you need to conform not only the judgments but also pull in things like legislation and regulation all into the same place. And since the cost of intelligence is going down, it also increases the amount of queries we can do, right? So one pretty cool thing is, you know, embedding, making one search against your own documents and files.

Gustaf Alstromer: Yeah. Making another one on the web and making another one against um court cases and judgments and legislation and then combining all of it to create effectively like a memo that...

Max Strand: Maybe they couldn't afford to do in the past. They just like just didn't do it.

Gustaf Alstromer: No. And similarly with with due diligence, when, if you go way back, it used to be a physical data room. That's why it's called a room, right?

Max Strand: You used to go into the room, you had all the documents and all the contracts, and then you'd sit down and read through all of them.

Gustaf Alstromer: Yeah.

Max Strand: And you had to mark them with a pen. So making and doing a due diligence on a company was really expensive. And now it's becoming almost a commodity where you're expected to do it. But...

Gustaf Alstromer: Clients are also not really that excited to pay for very simple contract review when they know that AI can do, you know, ninety-nine percent of it.

Max Strand: Wow. Yeah.

Gustaf Alstromer: So in the time that I've been at YC, we have funded some legal software companies, but the hardest challenge for all of them was selling to law firms.

Max Strand: And selling to legal. Most of them would end up selling to companies, because law firms were just like not possible to sell to. That radically changed, um, just like two years ago.

Gustaf Alstromer: Yeah. Can you tell us sort of like what do you think changed and how do you do it when you go and sell to uh one of the major law firms in the world? So for everybody listening, this was also one of the questions that I remember you pushing really hard on during the interview.

Max Strand: And I think we were quite contrarian to say, you know, no, it's different this time. Trust us.

Gustaf Alstromer: Yeah?

Max Strand: I'm glad we were right.

Gustaf Alstromer: I think the way that we approached the problem was always with this idea of we win if you win. So let's align our incentives with saying, as a law firm, this technology is revolutionizing, you're going to need to adopt it in some sense, shape, or form, and we want to be that long-term partner.

Max Strand: And somehow they know that.

Gustaf Alstromer: Well, so what what happens is um a lot of legal work is low differentiation. You know, if you're doing a DD from, you know, law firm X or law firm Y, you're kind of getting the same deal.

Max Strand: And so when you have this perfect equilibrium of services and somebody disrupts that by taking a new approach, clients are quick to switch.

Gustaf Alstromer: Yeah. I mean, clients are under price pressure. They want to be effective. Legal fees are very high. And so if this equilibrium breaks, you are almost forced to adopt it, and you are incentivized.

Max Strand: It's kind of the same as when lawyers adopted computers, right? If you're billing by the hour, you could say, well, let's have a person walk to the library, you know, find the right book, you know, find the right cases or the right precedent and use that for whatever work we do.

Gustaf Alstromer: Or you press Ctrl+F, right?

Max Strand: There's always this dilemma of you want to serve your client in the best way possible because that drives you more revenue over time.

Gustaf Alstromer: Yeah. And for a lot of a lot of the firms that we work with, their, you know, brand reputation, trust, as always, putting the client first is what matters the most. And so a lot of the firms also want to be leaders here.

Max Strand: Yeah. You know, some of them want to be fast second movers, but many want to be first movers because they're understanding if you have this perfect equilibrium and you take a simple type of work that gets disrupted, you should get more market share by moving quicker.

Gustaf Alstromer: Mm-hmm. But then it's not a race to the bottom, right?

Max Strand: It's a question of, okay, if we take every country has a ranking of law firms basically, right? And and it's also not a race to the bottom in terms of pricing because if you pull down, let's say, the cost of a due diligence, you free up more time to spend with a board on advising them on, you know, a really complex merger or a really complex acquisition. And so what typically...

Max Strand: Ends up happening is you're under time pressure. You could do more work, but you just have all this stuff that needs to get done. And that's what AI is really good at. But it's also serving lawyers in very creative ways. I mean, we've had use cases where, you know, we get a call from somebody and they say, "I played a role-playing game with Lora, you know, trying to win this argument and I'm asking it to act as the other party, right?"

Host: Wow.

Max Strand: There was this amazing situation that one of the Spanish partners at a firm called Perorca had where he went into court. He had put all the evidence and all the documents from the opposing party in Lora and he was actively querying it during the hearing and during, you know, at the time when the other attorney was speaking because then he could immediately interrupt if he found something that was wrong.

Host: Wow.

Max Strand: And he phrased it very nicely. He said when he goes into the battlefield, having Lora is like having another piece of armor. And I thought that was very poetically put.

Host: Could you use Lora to do negotiation on your behalf?

Max Strand: Yeah. So the way that we built that is, I think the LLMs by themselves are not good enough for that yet, and we can talk about that, but it's interesting to build these products knowing that the models will get better.

Host: And where do you stop?

Max Strand: Yeah. Right. On every feature. But so that feature in Lora is called playbooks. A playbook is essentially a collection of rules where you either approve or disapprove something. So you might say for the way that you would sign NDAs here at Y Combinator, you always want the definition within a confidentiality agreement to look a certain way. So you provide the rule, you provide some example language and then you say, "All right, if the opposing party will not accept this definition, we have some fallbacks." So fallback one and fallback two. And you just open a document in Lora, you open the playbook, and you press play. And it goes through every rule and runs it against the contract and it marks it up.

Host: Yeah. So if it does not conform with your playbook, it gives you the suggested language so that it will. And the really cool thing about this is it scales outside of just legal departments. So at Lora, every sales rep is using Lora to negotiate NDAs before sending it to our legal team. And we just started working with this very large bank in the Nordics and it very quickly moved from, you know, the legal team to compliance to risk.

Max Strand: And now to sales.

Host: Wow.

Max Strand: Because everybody can leverage the system. And the cool thing about it is it's not only faster and more accurate, but you agree on a standard.

Host: Because the legal team then creates the playbook and that becomes the standard that everybody uses. So it actually increases quality and consistency over time.

Host: Y Combinator's next batch is now taking applications. Got a startup in you? Apply at [ycombinator.com/apply](http://ycombinator.com/apply). It's never too early and filling out the app will level up your idea. Okay, back to the video. None of you guys when you started were lawyers.

Max Strand: Oh.

Host: So you're still building one of the largest or fastest growing legal AI companies in the world. How do you do that?

Max Strand: I think at this point I've become a hobby lawyer. But how we approached it was being incredibly humble. Humble for the fact that we did not know the industry. We were quick to create relationships with our early partners where feedback was, you know, happening daily.

Host: Yeah.

Max Strand: And I think that's been one of our strengths as a company to say, we don't know exactly where the future's going, but neither do you. So let's work together to make sure that we're both winners in, you know, whatever happens. And I think now we of course have the privilege of having hired a ton of lawyers into the team that work directly with the product teams and directly with the customers. Especially in an industry that is now going through such big change, it was useful to come in with more naiveté, if you will, saying why does it work this way? You know, it could work this way instead.

Host: Let's say you're a founder watching this right now. You're like, "I want to build AI software for logistics or for insurance or finance." Is your advice basically you don't need any expertise? How would you learn about the things you need to learn though?

Max Strand: I think my advice is, you know, learn about them, right? Like, we went into this and the first thing I did was I interviewed 100 lawyers. I had this good hack on LinkedIn. I texted them asking if we could have lunch and I would pay their hourly rate and I definitely could not afford it and none of them would impose that. They would just say, "Oh, that's amazing. Like I'll have the lunch with you anyways." One of the attributes that have been very helpful in my career has been that I'm somebody people want to help.

Host: I think that's a very underrated skill.

Max Strand: I think there are things you can do to be more like that. You can be a bit fearless in your approach to people and you can also be very thoughtful and grateful and appreciative of the work that other people help you with. If we hadn't done that, we would not be where we are today.

Host: And then how do you conduct a lunch with a lawyer when you're starting a startup and you don't know much about law?

Max Strand: So you'd sit down like this. You'd go somewhere decently nice because again they make a lot of money. And it took me some time to even understand that the way that departments work are fundamentally different. Like a transactional lawyer works nothing like the way a lawyer within the corporate department works. You just ask them a ton of questions. And I think also giving them something back. So, you know, I'd reach out, they see my tech background and you try to be, you know, give them nuggets of, "Oh, that's really cool. Have—what do you think about this?" Like, you give them ideas, you make them engaged in wanting to give you advice.

Host: And people generally feel good giving founders advice, of course. Like it's something that you should take advantage of.

Max Strand: Yeah. And something that I'm really happy to do now from the position where we're at. There are some large companies in legal technology. Are you going up against all of them or what? How do you think about the existing market of legal tech?

Host: Right. So there's been a lot of sort of large M&A machines and incumbents in this space for a long time. They're not very popular with the end users.

Max Strand: I think they have very kind of deep rooted roots. There are some advantages, you know, data modes and so on that come into play, but effectively what AI has done is really changed the game in terms of how quickly you can ship something and it's created a new category. So a lot of these existing point solutions were in maybe suites of these M&A machines and now a lot of it is becoming irrelevant very quickly. And the cost of building software is also going down very, very rapidly. So our ability to out-ship or outdeliver these teams of, you know, thousands of engineers with just 30.

Host: Is insane.

Max Strand: And so we have instead managed to build a company with, I think at the time of recording, it's about 100, where like our velocity is way higher than companies, you know, 100 times our size. I think that's interesting in and of itself in terms of how we built the company over the last year because when we came out of Y Combinator we were roughly 10 people and now we're 100 and that means we've onboarded on average like two people a week. And hiring correctly, it's really hard. Like it's a skill you need to learn. And hiring for velocity, hiring for, you know, entrepreneurship and ownership of different products and things, but also scale because the company is growing exponentially so you need your teammates to scale exponentially as well. If people scale linearly, at some point it's a really large delta and then things aren't working out anymore.

Host: Do these big companies have lock-in like the big legal tech companies?

Max Strand: So these big companies have a couple of advantages, but I think the disadvantages outweigh the advantages almost 10 to 1. There were very large data advantages and being like an incumbent where you lock in a large contract.

Host: Yeah.

Max Strand: But I think the buyers have also changed their aptitude here. So we're not seeing anybody want to lock in a five-year contract.

Host: Right?

Max Strand: Because the world is moving so fast.

Host: So we instead see them, you know, doing one-year contracts.

Max Strand: It sounds like a good motivation for companies moving faster.

Host: It is. Yes. And but even law firms, right? I mean, they don't want to be locked in with a vendor. So they're doing one or two year contracts. And you know, as we see them now coming up in a lot of places, they're also looking outside of their existing alternatives. So you might have made a bet back in 2023 or 2024 when it was experimentation days, but now you're looking at what are we going to deploy, you know, more long term. And there what I'm seeing is yes, people look at the technology, but even more so they're zooming out and they're looking at your rate of change.

Max Strand: They want to work with the partner that's going to get them from point A to point B. And they can be different things. It might be "we want to be AI-first and drive our top line," or "we want to drive profitability and streamline our operations." It can be very different motivations.

Host: Right.

Max Strand: How does your tech stack look like? What's under the hood internally?

Host: Yeah.

Max Strand: Yeah. So building our infrastructure, I think from the beginning it was pretty clear that we wanted to be on Azure just because it was the same that our customers were on and in the beginning I think OpenAI and GPT was really the only model that you could serve via Azure. Now we have much more options available to us. So we use AWS and Claude and Gemini and GPT and Mistral kind of interchangeably. The biggest thing there has been how do we build everything in such a way where we can hot-swap the models whenever we want and also build it in such a way that as the models become better, everything improves. And now we've also looked into classification models where, you know, if you do a simple query we'll serve you a simple model. If you do a complex query we'll serve you a complex model. And that's just because that's to keep the margins down, but also sometimes you don't need a bazooka when you just need a water gun.

Host: So who is the buyer? My understanding is that law firms have—but maybe you could explain to me. Like, there's a bunch of partners and there's other people there too, right? How is a law firm or a legal team at a company generally constructed and who are there? And who buys it and who uses software?

Max Strand: It changes a bit depending on size. So if you start with the biggest firms, of course you have the partner group that kind of runs things, but you very often have an innovation department, which sometimes have more or less influence. If it's a very strong innovation department, they make their own choices. They procure software and they're responsible for the entire innovation agenda. I've frankly got the most energy out of working with the innovation folks who are really smart about these things because there are a lot of people that just want to kind of check the AI box, and then others who really want to push things forward. And the interesting dilemma there is, you know, they're basically driving efficiency across the stack or across the firm, but they're not the users themselves, right? However, you might often have innovation practitioners that work in the M&A group or the disputes group or arbitration, and then they will work with those teams to drive an upskill. So they will have a very kind of process-minded way of working and then they might use Lora to build use cases for the end users because when you work in a big law firm you need to hit your billing targets.

Host: Yeah, they work a lot. Like we grind as startup folks, but lawyers—

Max Strand: Lawyers grind as well. And if you know that there's a way to solve something and it's going to take 6 hours for you to do that and you know a way to do it in 6 hours, you might not take the chance of exploring a way how you could potentially solve it quicker or with higher quality. You'll just conform to the way you're used to working.

Host: Yeah. So innovation teams have a huge opportunity and frankly, you know, mission to drive that across the firm. And if you go down a bit, so you have sort of mid-size firms, more often than not you might not have an innovation department, and so it's the partners who are making the move or the decision.

Max Strand: And what I found is it's hard to get the entire partnership to buy in.

Host: Go deeper on this point because I know a lot of founders ask me: how do I sell to a financial firm or law firm or something like that? And it seems like this is the tricky part—like you have to convince everybody.

Max Strand: You have to convince everybody or you start smaller.

Host: Okay.

Max Strand: You say, "Let's work with this partner and their team and make them rock stars."

Host: Hmm.

Max Strand: And then everybody else looks at them saying, "What's that guy doing?"

Host: Right.

Max Strand: That looks awesome. We also want in. And then you expand. But the key here is to sell, sort of like not top-down, but sell to the senior people first.

Host: Right? So there's it's impossible to do a bottom-up motion in our industry because you don't procure software individually. You take it through procurement and you take it through IT.

Max Strand: Yeah.

Host: And there's a lot of security checks. There's a lot of data privacy checks that you need to go through in order to actually serve client data in your systems. You were 23 when you co-founded Lora.

Max Strand: Yeah.

Host: By then you'd already done a lot. You had some stints at other Y Combinator companies like multiple different ones.

Max Strand: Yeah.

Host: What was your background before you started this company?

Max Strand: When I was 18 and it was time to apply to college, I actually had two options. I was either going to go down the route of becoming a professional Dota 2 player or go to college. I knew this, and my thinking at the time was, "Okay, what's the best case scenario in each of the outcomes?" So best case scenario in Dota would be to win The International, the biggest tournament in the world. You make $10 million. That would be amazing. But then I was thinking, what happens then? You know, it kind of feels like then life stops.

Host: Yeah.

Max Strand: And the best case scenario with going to college was basically this, what I'm doing now. So I decided to go to college. And when you apply to college in Sweden, you go to one school to do one program. So the engineering university is completely separate from the business university, which I think is really weird. We don't mix at all, which is bad. But there was a hack so that you could make an admission to one of the schools and then kind of pull the admission to make another one or pull your application to make another one and then call them and say that you messed it up and you wanted to reapply. So I ended up making it so that I could go to both universities in parallel. It was really good timing during COVID to do that because—

Max Strand: That means when you have two lectures at the same time, you can just have two laptops.

Host: Record one.

Max Strand: Yeah.

Host: Yeah. And there were multiple times where I had like exams at the same time with both universities and you would, you kind of sit with one camera over here and one camera over here pretending that you were just doing one of the exams. And so like one or two years into it, I was working as a programmer. I was building statistical models for esports betting and that was really fun. But I think I also wanted to kind of see what the business side looked like. So I had the privilege of working at a company called Norhen. It's like Y Combinator but for impact and it's based in Stockholm. And I think I got a lot of exposure to other entrepreneurs.

Max Strand: What struck me then was one—a few of them were not super ambitious to build companies that we're doing now, but they sort of had this like five-year plan to conquer Nordics.

Host: Yeah.

Max Strand: So I think immediately like I had a different take on it and then did a short stint at McKinsey, um, and worked at Bamlo and just one week at Depict.

Host: Depict was one of those companies—is one of those companies that was an incredible talent magnet.

Max Strand: Yeah.

Host: Like some incredible people have come out of Depict like an Lovable was one of the founders. Um, but there's a bunch of others. You're starting Gora even though you spend a week there. But is it, it's like kind of cool how you have these magnets that spawned off to a bunch of other cool companies.

Max Strand: No, they're amazing and you know we're all good friends in Stockholm. It's a small ecosystem and it's really fun to kind of cheer on each other as well.

Host: And YC ended in April last year. Can you walk us through sort of like the company growth and your personal development in this time? Like you were 10, now you're 100. Um, what happened?

Max Strand: We grew really fast and we were also feeling the drag.

Host: Yeah.

Max Strand: You know, like we took the product to market and you know we would sell it in a demo.

Host: Mhm.

Max Strand: And when law firms start to buy things after one demo, you're doing something right. And so the rationale was like, we should be doing more of this and we want to do it everywhere all at once. And this is also a space where it's kind of obvious that legal and LLM is a good fit. And so there were a lot of other companies in the industry. I like to say like there were so many legal AI assistants and now it just feels like many of them have kind of fallen off and they're emerging a couple of winners. With that rationale, we wanted also to get American capital in the company because we wanted to be able to make the move from Stockholm to the US when the time was right. After we raised the money during our first board meeting, we sat down and I remembered the look on some of our board members' faces when I basically said, "We're not going to sell for the next four to five months." And the reason for that was when we got the chance to onboard a client, it took a lot of work. Took a lot of work to get them to a level of understanding of what they could accomplish in the platform. And also the first experience of a legal professional logging in is the one chance you have. If you mess that up, they're not coming back.

Host: And we had a couple of situations where we'd onboarded a lot of people and we had done, you know, some misses and we didn't want to ruin that.

Max Strand: So we worked really hard on reliability, scalability, got the system to a place where we could comfortably onboard a thousand lawyers a day. And once we had that, we kind of let it rip. And that's also when we really started to hire. So we were maybe 25 in the beginning of October. And just six months later, we're now 100.

Host: So what we did was we said, "Okay, we're now going to scale across every market in Europe and we're going to start scaling towards the US." and our initial conversations in the US took some time because we were a small Swedish startup. Um, so I made you know multiple trips back and forth to New York and now we open up hubs both in New York, London, Stockholm and also have people locally in Spain, France and Germany.

Max Strand: So we've really gone at it and just said hey, we want to do everything everywhere all at once and let's do it now.

Host: And for you personally and Sig, like what was your experience in that?

Max Strand: I think the biggest takeaway and learning is going from being an IC into delegating.

Host: Yeah.

Max Strand: And that move, you know, you know how to do something, but that's not going to scale. So you need to teach somebody else to do it. And you need to hire people who are way better than you on a lot of different topics.

Host: So one of the early sort of hires that we made were actually another YC founder and we've ended up Jake.

Max Strand: Yeah. And we actually we've scaled the team with a lot of entrepreneurs. And that's not only like the skills we're looking for, but it's also like the way that we built the company because we're effectively running multiple companies within the company.

Host: It's sort of like a secret playbook that a lot of YC companies, some of the best ones, are all following is that the first people you want to hire are all former founders. And it's kind of actually advice I got from Paul Graham back in the days is that sometimes you think you're a founder that I work in this company for three years didn't go well. Am I less attractive in the job market? Like if you're here or if you're in a startup center, you're actually more attractive in the job market because people actually want to work with people like you.

Max Strand: Yeah. And we want to hire them. So um, it's been amazing. And also the agency and the attitude to problem solving. That's kind of what you're looking for. And then sometimes you need to hire for scale, right? Like now we have a significant sales team and you need somebody who's seen the 10 million to 500 million journey because that's the journey that we're on.

Host: And my learning from McKinsey, which probably I'm sure applies to you, is the culture in the beginning is the people that you hire, of course. And when we've now scaled the hubs, um, we always send a person from Stockholm with them. It's the best people from the Stockholm office that then travels and set up the new hubs.

Max Strand: You seem like the kind of person who embodied the attributes, you can just do things. So can you tell me how that is reflected in your company?

Host: You can't just do things. And when we started building this company, we didn't know anything about law, right?

Max Strand: Um, I think that was pretty apparent in our first interview and we you know made the right moves from then to the second one where we showed that we could do it.

Host: You apply for two different batches.

Max Strand: Yeah. The first one didn't go as well. And so about this attribute, it's something I look for in others as well. Um, during a lot of the interviews I do, I often ask the question you know, what have you done outside of your role for the company and here I'm looking for creativity, ability to spot problems and solve them and to take responsibility for more things than just the stuff that you're doing.

Host: Right. Right.

Max Strand: And I think in terms of starting companies and you know, building the future, because frankly we need to reimagine a lot of the stuff that we're doing, we don't want people who are bogged down by your boss telling you to do something right. We have a very sort of flat organization where let's say our marketing team, we want generalists who are using AI to do 10x more work than they could have done in the past. And where you might have needed a 30 person marketing team, you now need five.

Host: And you want those five people then to be complete, you know, yes.

Max Strand: And to go out, you know, above and beyond. And that characteristic, I think, is increasingly important as well in an age where if you're really ambitious, you can get a lot of leverage out of tools.

Host: Absolutely. So if we fast forward like five or 10 years, uh, how does the day-to-day job of a lawyer look like?

Max Strand: That's interesting. We think about that a lot, right? Um, I'm kind of viewing it as you're more and more entering a work space of reviewing work than actually doing it and you are managing the expectations from your clients and the expectations and the work from your AI agents, right? You're effectively instructing them. You're watching them go out and do work and you're making sure that everything they're doing is not only correct and sort of at your standard but you're also managing how that work gets delivered to the client because I think you know you will always want somebody who knows their stuff.

Host: Yes.

Max Strand: On this and there's a big reason for why we're working with lawyers and not with the people who might use the legal services because a lawyer is needed and necessary to deliver the end product. But looking five to 10 years ahead in these days is also it's hard.

Host: It's hard, right? Um, if I knew where the AI models would be 10 years from now.

Max Strand: Yeah. We're looking weeks ahead right now.

Host: Yeah. It's and that's funny just with our product road map. Um, I tried to do them kind of like many quarters ahead.

Max Strand: Yeah.

Host: Yeah. It's hard.

Max Strand: It's really hard.

Host: Do you think uh that the large AI labs are going to try to attempt at doing law? Maybe not law specifically, but I do feel like they're more and more becoming platform companies rather than model providers. I mean, Google is building Google Workspace with Gemini. Anthropic is running very hard on the MCP idea of building kind of a universal entry point into a lot of applications.

Max Strand: I think the expectations on companies like us are pretty clear. You know, whatever comes out of a model lab is kind of expected and then everything else we're adding on top is kind of like icing on the cake.

Host: How does it feel to product-market fit?

Max Strand: I think the feeling is best summarized by almost like this drag feeling or kind of infinite, you're being pulled into the market, right? Um, it like it literally feels like we have infinite demand and I think that's coming from a point of the product is working and it's moved from being in this experimental AI bucket into we are relying on this for core work that we are delivering right now. If something breaks, you know, immediately we get a phone call saying hey, we can't do this, like what's going on right? And we fix it. It's basically been this point of you start out. You hope that what you're doing is the right thing and you try to get early partners excited about what you're doing. And in the beginning, to be, you know, really frank, a lot of people got on with us because they wanted to be on the journey and they took a bet.

Host: Yeah.

Max Strand: And I am so thankful and happy that they did that because now we've taken them from point A to point B and we're continuously scaling from here.

Host: So we tell companies to move to San Francisco generally. Uh, you decided to not take that advice. Can you just like tell us a bit about the thinking here and maybe like if you have some pros and cons?

Max Strand: Yeah.

Host: About not being here?

Max Strand: Yeah. The reason why we stayed in Stockholm was um, we needed a market to grow in. And if you go to the US, it's not only more competitive, but I think it kind of pushes you into becoming a more narrow company. You start building really horizontal and then you realize, wait a minute, we're really good at this. So you start to scale it in other markets and you quickly notice ah, we're the best in Finland too and we're the best in Denmark and we're the best in Norway and then you scale to Spain, France and Germany, London and then the states. And at that point, we had always, you know, we had already done 15 new market entries. The algorithm or the method was already kind of established. Of course, the US is a bigger undertaking, but we had also then grown from this small fish in a small pond to crocodile or a shark in the bigger pond now.

Host: So you've raised 80 million like in mid-May. You open an office in New York. Uh, you launched with one of the most famous law firms here in the US.

Max Strand: Um, it seems like you're trying to position yourself as the category leader of AI law in the world.

Host: Yeah, I mean 100% and I think in many aspects we're already there. It's for me more of a question around ambition and what's next. It's very easy to say, hey, we see this problem. Let's go solve it. And then you get satisfied.

Max Strand: But it feels to me like every time we solve a problem, a new one emerges. And we're finding that as we go deeper and deeper and deeper in the entire legal software stack, we're also seeing that the line between software and service is blurring. AI is continuously developing super super quickly and that means we need to do the same. And so in my mind, the category leader in the space does not only build software, they serve as the strategic partner to these large firms and they make them win in this transition because it's a very large transition. And that's also why we've basically scaled headcount as quickly as we could whilst maintaining kind of culture, urgency, and velocity.

Host: So a lot of founders that I meet are asking me questions about how you build a vertical AI company. That seems like the kind of companies people are building now. Do you have any general advice you want to give to those founders who are just starting out?

Max Strand: The first kind of obvious tip is don't get locked in with a provider and don't compete with the AI labs.

Host: The AI labs ship, right? And so does companies like Perplexity and others. And so I think you want to be really clear and honest to yourself where you're adding value and where you're adding long-term moat.

Max Strand: And this is something that we've thought a lot about at Legora, like how do we build things as moats so that when the tide rises, just everything gets better. If you're just starting out, you got to realize that you do not have the capacity to outperform any of those companies. You kind of have to find a narrow category to do it where you know the models won't get to, or either that or finding out a way to leverage the models very creatively, I mean in a way that others haven't done it. I think take AI scribing is a good one. Like typical AI scribing is hard to do and you need to embed a lot of custom prompts and ways to get it right so that it uses the right medical language, which is very similar to law. Like you needed to write clauses in a way that a lawyer would write a clause, not just what the model spits out as the most probable answer.

Host: If I'm watching this video and I'm like I'm thinking about applying for a job at Agora.

Max Strand: Yeah.

Host: Uh, tell me about what I should expect either from the application process or from working there.

Max Strand: The things that we look for are ambition and the willingness to say we got this huge problem. There's this huge mountain. How do we climb it? And we're also very upfront with candidates that this is not a 9 to 5 and we're not the traditional Swedish working environment. We have the good stuff. We have the fika, but uh we have a lot more hunger and you know, frankly, a lot higher expectations and we want that not only for ourselves but for each other because we—

Max Strand: Want to grow as people and we want to grow as entrepreneurs and as a company as leaders. And I think there, just looking at like our application process, the biggest thing we do is we look at a lot of cases, right? If you want to come in and work in our go-to-market team, you need to come and pitch us our product.

Host: Yeah.

Max Strand: And you need to do a really strong pitch. And you know, if you take the engineering team, we basically ask you to build a POC of Legora.

Host: And you know, we want you to work with AI-generated code, but we also want you to be able to explain it.

Max Strand: Yeah, right. And to design systems that scale. And I think Stockholm is a small ecosystem. And so it's also quite easy to make references and see who's actually good and who's been in a company and made them a success. You know, not only was there the right time, exactly. And another really big piece is we're hiring all over Europe. So we've had people move from Madrid, from Amsterdam, from Germany, from Paris all the way to Stockholm. We tend to not onboard them in November when it gets nasty, but I feel like we've started to build this sort of AI hub together with many other companies that is not only like super fun, but also, you know, great companies come out of it.

Gustaf Alstromer: Thank you so much for coming back to Y Combinator.

Max Strand: Thanks, Gustaf.
