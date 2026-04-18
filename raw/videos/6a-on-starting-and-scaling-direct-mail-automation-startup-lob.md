---
title: "On starting and scaling direct mail automation startup Lob"
slug: "6a-on-starting-and-scaling-direct-mail-automation-startup-lob"
media_type: "Video"
author: "Harry Zhang"
speakers: ["Harry Zhang"]
categories: ["Founder Stories"]
description: "Harry Zhang, CEO & founder of Lob (YC S13), talks about his journey as a founder, the genesis and evolution of Lob, and lessons he's learned along the way."
url: "https://ycombinator.com/library/6a-on-starting-and-scaling-direct-mail-automation-startup-lob"
youtube_id: "O-LKD3yUnk0"
youtube_url: "https://www.youtube.com/watch?v=O-LKD3yUnk0"
transcript_source: "yc_page"
multi_speaker: false
speaker_labels: false
---

# On starting and scaling direct mail automation startup Lob

[Harry Zhang](https://twitter.com/harryzhang) is the cofounder of [Lob](https://lob.com/). Lob makes it possible for
enterprises to programmatically send physical mail. They were in the Summer 2013 batch of YC.

[Kevin Hale](https://twitter.com/ilikevests) is a Partner at YC.

Harry is on Twitter [@harryzhang](https://twitter.com/harryzhang) and Kevin is
[@ilikevests](https://twitter.com/ilikevests).

## Transcript

Craig Cannon [00:00] - Hey, how's it going? This is Craig Cannon, and you're listening to Y Combinator's podcast.
Today's episode is with Harry Zhang and Kevin Hale. Kevin is a partner at YC. Harry is the co-founder of Lob. Lob makes
it possible for enterprises to programmatically send physical mail. They were in the summer 2013 batch of YC. You can
try Lob at [lob.com](http://lob.com). Harry is on Twitter [@harryzhang](https://twitter.com/harryzhang), and Kevin is
[@ilikevests](https://twitter.com/ilikevests). All right, here we go. Today we have Harry Zhang, co-founder of Lob. Lob
makes APIs for companies to send letters and postcards. Kevin has a question for you.

Kevin Hale [00:41] - I'm trying to think back to when you guys applied to YC. You didn't have almost anything. I would
say it was fairly embarrassing in terms of what you guys had.

Harry Zhang [00:51] - I guess you could say that. Honestly, we were scrambling weeks before the interview to try to
come up with something that we thought was worthwhile for demoing. But I think the important thing when you're starting
a company, and for us, is thinking about the problem that you're working on versus having a bunch of stuff. For us, we
had done sort of the due diligence beforehand. We talked to a lot of customers. We had a good sense for what the core
problems are. But we didn't have the exact product just yet.

Kevin Hale [01:18] - What was that MVP when you guys applied to YC at the time?

Harry Zhang [01:21] - I think back and it's pretty fun just thinking about this. We literally had an API that took
whatever you put into it and spit it right out to you. That was our MVP, and we were secretly hoping--

Kevin Hale [01:31] - It just mirrored the response back.

Harry Zhang [01:33] - It just mirrored the response back, and we were just sort of hoping that we wouldn't have to
demo, because honestly, we hadn't built a lot of product yet. We didn't know what we wanted to build. We've always
operated from the point of view of we want customers to pay us for something before we actually go and do it.

Kevin Hale [01:47] - What's interesting to me as someone who's focusing on design interfaces at YC is that I kind of
really love API companies, because I think a lot of people think of it as "Oh, it has no sort of interface." But to me,
the interface is just documentation. It's very pure. And so I'm always interested in when I look at an API company is
looking at, "Oh, what are they doing here to say this is how we want to build community around this?" Because what
they're trying to build out is that this is something that people who build stuff want to use. What are the ways they
going to communicate that this will allow them to do something sort of cool or solve a problem, et cetera? I feel like
you learn a lot about people's thought processes and also how good someone is as an engineer or programmer by how
thoughtful that documentation is. Stripe is a classic example of this. For you guys, I remember, it's like you had the
basics down, but it was clear that you guys knew enough to be considered to anyone that would want to be using it, even
if it was their first time ever writing any API call.

Harry Zhang [02:55] - That's definitely right. Documentation to this day is still the number one thing. And I think we
take a point in pride in making sure that our documentation is something that every single developer's want to use. And
see, it's friction. When your core product is an API, you better have the best documentation on the planet.

Craig Cannon [03:13] - What was the insight you guys had early on that made you convince that you wanted to follow
this path?

Harry Zhang [03:18] - That's a good question. It actually started from the problem. It started from my time at
Microsoft. Admittedly, I did not think I was going to end up in a business that's focused on mail, nor did I think that
at a job at Microsoft, at a company that's 100% tech-based, one of the main things I was going to be working on was
actually direct mail campaign. That's sort of how we initially got started with the problem. Actually, it started from a
place of complaining. I was driving back from a ski trip with my co-founder, Leore. I was complaining to him about this
project that I was working on at Microsoft. Essentially, what we were doing is we had come up with a system for sending
out these very custom training materials and an invite to a webinar online, but for a number of different reasons, we
weren't allowed to do that using email, and telesales was too expensive. The thing I was doing was actually building a
direct mail program. That was one of the most effective things that we done to date. Honestly, it was a little out of,
we didn't have any other options. But when it worked really well, I got a huge budget

Harry Zhang [04:16] - and was asked to sort of scale across a much bigger set of customers, and different use cases,
and more products. I thought that was going to be something that was easy. But it turn out to be the bane of my
existence for the following three months.

Kevin Hale [04:27] - In the early days for YC, what did the API do?

Harry Zhang [04:32] - The API just went into a database that literally I started off using my inkjet printer. We
printed everything on my home printer out of my apartment. There hit a point where we were watching TV and stuffing like
we had an assembly line of letters that we were stuffing ourselves. It's sort of at that point, we're like, maybe we
should go get a printer to help us with this problem.

Kevin Hale [04:57] - What made you feel confident that you could just go try to sell to a company, or get someone to
program against that even though it was connected to your inkjet printer? What gave you the confidence like, "Oh, I'll
go in here and sell someone on this fake magic?"

Harry Zhang [05:10] - I guess for us, it was more just like a belief that this was a real problem for people. When we
told them about the problem that we're solving, it really resonated with the customers that we were talking to. And I
remember our very first customer. It's this guy, his name is William Whey. Last use case I'd expect for mail. He found
us on our Hacker News launch. And he sent me a note saying, "Hey, I want to use your guys' letter product, can we chat?"
I said, "Okay, well, tell me a little bit more about your business." And 16-year-old kid, awesome. I looked him up, I
was like, very little information online. But he actually ran one of the largest Team Fortress 2 stores online.

Kevin Hale [05:54] - No way.

Harry Zhang [05:54] - And if you don't know what Team Fortress 2 is, do you know what that is?

Kevin Hale [05:56] - One of my favorite games.

Harry Zhang [05:57] - Perfect. One of the things that people like to do is they buy digital items online, right?
That's a regular thing, because people don't want to go through all this time to find the right weapon or whatever that
might look like. He had one of the largest Team Fortress store 2's online. I was still super confused. I'm like, "Why
are you talking to me?" Just didn't know. But it turns out he had a problem, which was every single time people would
buy his items online, he'd deliver it, and he'd give them the item online, but he had no proof that he actually gave
them a digital item. What he had was a ridiculously high rate of fraud, which is people would charge back, and he will
lose every single dispute, because he couldn't show that he actually sent anything. His solution to his problem was I'm
also just going to send them a letter in the mail with a code, and that served at his proof. But he had to do that
himself, and he hated that. That's something that we would've never thought of out of the gate. But I think it goes to
show, right, you can always--

Kevin Hale [06:55] - How did this guy find you?

Harry Zhang [06:55] - Think you have a way to these product, but not always.

Kevin Hale [06:57] - How'd he find you?

Harry Zhang [06:59] - He found us online on Hacker News.

Craig Cannon [07:02] - So you did a Show HN type thing.

Harry Zhang [07:04] - That's right. We did a Show HN. I think that thread might still be around somewhere. But that's
sort of how he found us, right? And we basically said we have an API for sending letters. And he was like, "I have a
problem. Can you guys help me with this?"

Craig Cannon [07:17] - Once you got past having 16-year-olds as clients, how did you get the first really top-tier,
big client?

Harry Zhang [07:25] - For us, that top-tier client is a big insurance company that's currently in New York. I would
say they're pretty tech-forward. Can't tell you the name of that company. But one of the things that's exciting that we
found 'em was they had a problem in that they didn't have compliance and security around their existing printers. This
was in the midst of me as a sales rep literally sending hundreds and thousands of emails to potential companies that I
thought could be a fit. This one got a response back from the CEO. He asked a few sort of qualifying questions and
punted me to the guy who's actually in charge. He's now their VP of Data. And they had a problem that their printer,
they didn't have confidence their printer knew what HIPAA was. They didn't know what a BA was, and they were essentially
reevaluating what technology they were using to work for print shop. That's sort of where we entered. Ultimately, that
became one of our first major real customers, and they're still a client with us today.

Kevin Hale [08:27] - It's just a cold email you sent out?

Harry Zhang [08:28] - It was just a cold email.

Kevin Hale [08:29] - How long? Here's a question. Can you remember what was in that cold email? Was it super short,
was it super long, was it personalized, et cetera?

Harry Zhang [08:39] - It was definitely personalized. I had a good idea of what type of mail they could be potentially
sending. It was a short, crisp email like this is what we do, here's how we're different, and I think we can help you
with your current problem in these three ways, right? I think the key things in a cold email, you really want to hit on
why the change--

Kevin Hale [08:56] - Did you know that they were having that problem?

Craig Cannon [08:57] - I was going to say, were you clued in on the HIPAA part?

Harry Zhang [09:01] - I did not know--

Craig Cannon [09:01] - You just guessed.

Harry Zhang [09:01] - That they were having a problem at that company. We didn't know what HIPAA was and this was
sensitive information. But we didn't know that they were looking, right? So it's a little bit luck. They were looking,
we didn't know about it. We knew that they were sort of within the space that we're looking for. But honestly, in the
early days, not everyone's going to be able to find you. What's important, especially in our business as a B2B SaaS
business, is you got to find the customers that believe in the method and the methodology in how you're building the
product, not just what you serve today, but also the vision of what your product could become. That's where we found a
lot of alignment with this company,

Harry Zhang [09:41] - because they could understood exactly why building it as an API is valuable. They're super
technology-forward. While we didn't have every single capable they needed, we could cover the majority of what they
want, and they knew that we would be able to scale with them as well.

Craig Cannon [09:56] - Once you got there, how did you start expanding that, the other top-tier clients? Was it all
just cold email? These are big contracts, I imagine.

Harry Zhang [10:06] - These are definitely big contracts. Today, our contracts are everything from on the small side
for our mid-market's like 30,000 a year just to use Lob's API. We sell contracts up to like millions a year as well.
There's a big range. But I think for us, there's a couple things. It's a sort of chicken-egg problem in that you need a
lighthouse customer to get other big customers. Getting the first one is always the hardest, and that's a combination of
just combination of luck, hard work, and really understanding your problem space and what you're solving. Once you've
done that and you've successfully done that for a customer, it's much easier take that exact same story to a similar
customer and help them realize that value. And by that point, you should also understand sort of the language of the
customer. In their industry, what do they care about? What are the key problems that they have? And when you have that
insight, it makes you much more credible as a potential vendor.

Kevin Hale [10:59] - How much time do you guys spend researching before you reach out to... Let's say you have one
company. You're like, "I really want to have their business." What's the prep work that you start doing? Who do you
start contacting? How long does it sort of take?

Harry Zhang [11:10] - There's a fair amount of prep work. For us, it starts from just mapping out the organization,
right, drawing a blueprint of who are the key stakeholders in the organization. Especially for larger companies,
decisions aren't made by just one individual. They're made by different folks, and each different person may have a
slightly different motivation. We work with our sales reps to figure out what is that motivation for each of those
individual? Who are sort of the key contacts? What's the message that's going to resonate with them? We'll typically
start by having cold outreach these folks. We'll also sort of combine it with a lot of our marketing tactics in that
they're going to start seeing Lob pop up everywhere, right? Ideally, if they're not responsive to email, we'll also look
at what conferences they're going to be attending, so we can actually find these folks in person. Really, it's sort of
like a multiprong approach. It's pretty rare, and you shouldn't have expectations just like I send 10 emails, I'm going
to get eight responses back. That's not going to happen. It's a grind, but that's part of your job is to work your way
through that, and figure out who are the accounts that are going to work. Over time, you're going to get more and more
accurate about understanding, and motivation, and what resonates with people, and what people care about. You may find
that the person you thought was the person who's going to make decision might actually be someone totally different.

Kevin Hale [12:27] - Did you always know that this was going to be an enterprise company, that this will be what you'd
focus on? A lot of people will start an API coming in with anybody could use this, anybody should. How did you know
where to focus? And actually, I'm kind of interested is what is the split in AP? I imagine most of it is enterprise
usage, but how much is also SMB, how much is consumers using it?

Harry Zhang [12:50] - Absolutely. I'd say roughly about 15% or so of our business is still self-service customers
today. It's a meaningful share of our revenue. That fluctuates based on how much our big customers do. But there's a
healthy self-service segment of folks that utilize our API, and that's where we started. For us, how we ended up
focusing on enterprise is really sort of evaluation of our market. It turns out the market that we're in today, the
top 20 players send such enormous amount of mail that if you really want to capture an entire market, you have to focus
on how you're going to win those top couple folks. What we realize is one of the things that's really nice about an API
is that you can essentially give those same capabilities to people who aren't executing that type of volume. In fact,
it's a focus for our business to sign these enterprise customers, but we know a lot of the features and functionality
that these guys have or are looking for are also things that smaller customers want but don't have access to because
they're not operating at that scale or capacity just yet, and API enables them to get access to that.

Kevin Hale [13:57] - So you guys graduated up to enterprise.

Harry Zhang [14:00] - That's right.

Kevin Hale [14:02] - How long did that take?

Harry Zhang [14:04] - We're still working on it now, even today. Really, it's been a six-year journey for us. I would
say we signed our first few true enterprise accounts just two years ago. So it took us almost four years to get that.

Craig Cannon [14:16] - Yeah, so it was a while. One thing a lot of startups don't get right is pricing. When you guys
were working your way up to enterprise, by the time you got that first big client, do you feel like you had your pricing
locked down? Because if that was wrong, it could've multiplied in a bad way quickly, right?

Harry Zhang [14:31] - Definitely. We're always evaluating our pricing to make sure we have the right model. We
actually made some pretty big mistakes early on as it came to the price. I think you guys have probably all heard the
typical mistakes, right? It's like, "Hey, didn't price high enough." We didn't start talking about pricing too late. For
us, it's the structure of pricing we actually learned a lot about and was a big motivating factor in us changing our
pricing model a couple years ago. We started off thinking very much like a traditional mail provider or even someone who
sells reserve instances in AWS. Essentially, you could buy Lob, and what you were buying is you would buy 100,000
letters over the course a year. You'd pay for the 100,000 letters. You can use it whenever you want. Super logical, very
easy to understand, and it worked for us for a while. But the problem we found was we went into larger customers, they
don't look at not every single budget is made equal. When we're selling 100,000 letters, they're going to evaluate us
against 100,000 letters from another direct mail provider. Our value is five cents of that letter is going to Lob,
right? That's the value that we see in our technology. But the problem is when you're talking to customers who are used
to pricing in a specific methodology, they're comparing us to why are you five cents more expensive than everybody else?
They're starting to do the math like how many more responses do I have to get? What's the higher conversion that I'm
going to see a result?

Harry Zhang [15:58] - But in reality, it's two different investments, right? They're making a technology investment in
the technology that we're providing them, and they're buying the mailpiece. One of the big changes that we made that was
really successful in helping shift the conversations to the right level of our customers was actually creating what we
call a platform fee. Essentially now, our customers pay us $25-$30,000 a year to use Lob, and they get access to our de
facto mail pricing, which is now competitive, if not lower, than every single other offering. Now we can focus the
conversation is like how do you value Lob's technology, is that worth 25 to 30,000, instead of having a conversation
about what is the cost of a mailpiece, and what's the conversion that we're looking for. It's important differentiate
and associate the value that customers see in your technology with what they pay for versus something that could be a
commoditized product in the market today.

Craig Cannon [16:51] - Now was that pricing model only an option given your maturity?

Harry Zhang [16:56] - We could've started with that model. The reality is we just didn't know people were going to
think that way. It's hard to get everything right.

Kevin Hale [17:05] - What helped you shift to that?

Harry Zhang [17:07] - Well, we kept getting feedback from customers, right? And we could tell that the way that they
were modeling us was they would be trying to figure out--

Kevin Hale [17:14] - This apples-to-apples comparison. It wasn't the right way to do it.

Harry Zhang [17:16] - It was an apples-to-apples comparison, that's exactly right. And the part that was challenging
is they were totally okay with paying with another agency to help manage their mail sends, right? But that's not pulling
out of the same budget. And essentially, part of what we offer is we're doing that for them. But they were looking at
our mailpiece price and comparing it to another mailpiece price. But in reality, it's the mailpiece price plus whatever
they were paying this other agency to manage it for them. But those were coming out of two different budgets, right? For
us, we had this realization when we started talking to companies, and they kept trying to sort of ask, "Oh, well, why is
it more expensive?" when really the reason why it's more expensive is because we're doing more things for them, right?
And that's very logical, but help them understand in a model that they're used to, we had adapt to what they've already
seen in a market.

Kevin Hale [18:04] - One of the things that's been interesting to me as a trend is that software wanting to be a
commodity and the value and price of it getting lower and lower. Then API companies sit at very bottom of their
fundamental infrastructure for services. This is probably related, but how do you think about that as a business? Do you
guys set out to be like, "Okay, we're going to look here to compete on price or on sort of a value?" Then how can value
work in a infrastructure, sort of commodity-like business with an API?

Harry Zhang [18:43] - It's different for every single commodity, right? While you might be able to compare email or
SMS, I think those are priced differently than Lob, for us, I think what we found is we wanted to be cost-competitive,
if not the best price in the market for the actual cost of mail, which we see is a relatively commoditized product,
right? You can go to any number of commercial printers and they can produce the mail for you. Really, what's different
about buying software through Lob is that you're getting access to our entire API and all the associated offerings that
come with our platform by sending mail through Lob. So we want to differentiate what is it that a customer's paying. We
wanted them to know that they're getting the best price in the market for something that they see as a commodity, which
is the cost of the actual mailpiece. But we want them to pay us the value that they saw in using our software to send
mail. That's sort of why we made this split in having a platform fee as well as a per-piece price.

Kevin Hale [19:46] - How does that adjust your sort of product roadmap to have these technology differences that makes
you different from just a printer who can say, "Hey, I can do that digital printing?"

Harry Zhang [19:56] - Yeah, that's a good question. It goes down to a conversation of how much are these features
worth to our customers, right? Over time, we built different layers, different sort of offerings like mid-market,
enterprise offering. We realized that customers would be willing to pay more for specific features.

Kevin Hale [20:13] - What are some examples?

Harry Zhang [20:15] - A good example of this is like HIPAA. One of the key considerations for companies that are more
regulated spaces that they need to have a HIPAA-compliant offering. Now it's more expensive for us to have a
HIPAA-compliant offering. We also realize that one of the key considerations when companies are looking at printers is
can they meet these requirements? We actually charge more for those customers, because it costs us more. And also
because there's less offerings that are able to do something like that programmatically, right, that are going to manage
their customer information in a secure fashion, both in terms of how they're transitioning information to you and
transferring it to you as well as being stored in our system. This is people's names and addresses. This is very
sensitive information for a lot of companies and something that they value very highly. We had customers that will be
like, "We'll pay you if you guys can do X for us." That's when you really know you're on to a feature that's really
important, because they can actually quantify the value that that's worth to them. And it makes it easier for us to
understand and prioritize our product roadmap, because we know what customers are willing to pay for. Not just like,
hey, can they achieve a slightly higher conversion of HIPAA? Now we know that they're going to pay us an 10,000, and
it's worth it to them, because that's what they see.

Craig Cannon [21:24] - What are the other trades that you've made in the context of fulfilling the desires of these
enterprise customers when you realize, "Oh, maybe they don't care about this," for example, more vertical integration
type stuff?

Harry Zhang [21:35] - Some examples of this is we realized that the execution component, being able to track your mail
and having sort of the platform offering being available through API, that was really important. Because a lot of
companies actually are, especially larger folks, they're working with agencies that help them with a lot of the
segmentation, the actual management of the campaign, the design of the mailpieces. These are things that we've thought
about building products around, make it easier for people to build beautiful mailpieces. What we found is most people
already have that in enterprise. They're already ready to go. Their problems are not around the need for designing a
better mailpiece. They have a full-service creative agency that has like 16 different campaigns and everybody's already
thought that through. They already have it, right? So there's a good example for you.

Kevin Hale [22:23] - How many employees do you guys have at Lob? How big are you guys?

Harry Zhang [22:26] - Yeah, we've been hiring a lot this year, so we're just shy of 70 right now.

Kevin Hale [22:30] - Just shy 70. And then, don't take offense, but for an API company, I imagine it's difficult to
recruit people here. What do you guys have to do, and what have you sort of figured out that helps you sort of compete
against everyone else out here in San Francisco?

Harry Zhang [22:47] - I can tell you, mail is not exactly the most sexy thing in the world, certainly not. AI
interaction are--

Kevin Hale [22:52] - But I love these non-sexy businesses, especially ones that make money. And so to me, it's like,
that's probably a good leg up. But I'm just wondering for you guys, if you're looking for that-- Top engineer to come on
and make a difference--

Kevin Hale [23:06] - How do you inspire them with a mission like this?

Harry Zhang [23:08] - Good question. A couple things that we think about. The first thing you need to do is understand
the motivations for each individual that you're trying to hire. Everyone's going to care about something that's
different.

Kevin Hale [23:19] - Sounds a lot like your sales-- Approach.

Harry Zhang [23:24] - But it's true, right? You have to realize what is it that people want to join a company for. You
need to identify the folks that are good fit for where we're really strong. For us, if you go and you ask why some of
the folks join Lob, I think the majority is folks would tell you it's around our culture, right? And that's the reason
that they got inspired to join. So the mission is certainly important, and I think we spend a lot of time on talking not
just about what we do today, but what is it that we want to achieve. But ultimately, I think one of the key
consideration is like what's it going to be like to actually work at Lob? Am I going to be happy there? And that's a
huge motivating factor for a lot of people. We spend a lot of time internally thinking about our culture. How do we sort
of find the right folks that map into the culture that we have? How do we sort of give engineers and give potential
candidates a sense for what our culture's like? And we do that through writing blogs. We do that through having people
come on-site beforehand. They get a sense of what it's like to be there. We try to make sure that throughout sort of our
activities, we're tying together our core values and giving people a good representation of what it's like to work at
Lob.

Craig Cannon [24:28] - And so also part of this is the comp. Before we started recording, you talked about options
versus RSUs. What's your opinion on that?

Harry Zhang [24:36] - I think they're both good instruments.

Kevin Hale [24:40] - Do you mind helping for those people who might not know?

Craig Cannon [24:42] - Yeah, that would be a good idea.

Kevin Hale [24:43] - What is the difference between an RSU and an option?

Harry Zhang [24:44] - Absolutely. One of the things common misunderstood is equity compensation at companies. RSUs and
options, they're both different forms of equity that a company can offer you in your company. The main difference that
we see, options, essentially, you have to purchase. There's a strike price that's associate for options. As an employee,
you have to make a decision at some point in the company's life cycle that you want to spend your own money to purchase
shares of the company, and that's why you have essentially one option is the right to purchase shares at a particular
price point. But the reality is you're going to pay some relatively significant amount of money, potentially, in order
to acquire those shares. We've heard of people taking out loans to do this. There's companies designed to help people do
this. It's not an insignificant amount of money. RSUs are a little bit different. RSUs is actually a stock grant.
There's actual value to the RSU that you're receiving, and you're not paying for the right to the RSU. You're actually
being granted that RSU. For us at Lob, we actually decided, and I think it's a little nontraditional, that we built sort
of a unique RSU instrument that we think is sort of the best of both worlds, right? And essentially, the motivations
were we want people to be invested in the company in the long term. We want design equity compensation that didn't feel
like a risk to the employee. The whole entire reason why you want equity in a company

Harry Zhang [26:10] - is you want a share in the upside. You want to feel like you're a part owner in the company. But
if you have to spend an enormous sum of money without knowing what the outcome of the company's going to be in advance,
which you can't predict, that puts you in this weird scenario where you want to buy your shares, but you're not sure if
you want to. And we felt like that was a really tough position to be in as a potential candidate. We designed RSUs in a
way so that our employees actually get RSUs when you join Lob. So what that means is you don't have to make that
consideration of, "Should I spend the money to buy my options? When should I exercise that?" There's obviously some
differences there, right? I think the major difference is when you get taxed. But we always looked at it as you don't
get taxed in RSUs until there's actual a liquidity event in this scenario. Because we don't actually grant you the RSU
until there is liquidity event. Therefore, you owe taxes at the time of which you've probably already received money--

Kevin Hale [27:05] - When you already have money.

Harry Zhang [27:06] - From your RSUs. And I think what we found is that, especially employees who understand equity
compensation, that's something that's really attractive to them. And when we think about wanting people to be here
for 30 years, we don't want people to stay for the wrong reasons of like, "Oh, well, I don't have the money to exercise
my options, I'm going to stay." I want them to stay because they enjoy the people they work with. They enjoy what we're
working on or inspire the problems that we have. But we still want to give them the share in actually being an owner in
the company.

Craig Cannon [27:29] - How do you handle vesting?

Harry Zhang [27:31] - Vesting, essentially, you do a one-year cliff. And we essentially vest monthly thereafter. It's
the same as an option in that sense. One thing we do, we also reserve retention grants for people. So at our 2 1/2-year
mark, in every year thereafter, we continue to give people opportunity to gain additional equity in the company. And our
thought is like the longer you stay at the company, the more equity you should be able to acquire. There shouldn't be a
point where you ever stop earning equity in the company.

Kevin Hale [28:00] - What kind of mistakes did you guys make when it came to closing your first big sales?

Harry Zhang [28:07] - I actually think there's a valuable lesson we learned during our early YC days in that when
you're selling your product, you're oftentimes selling some things that you might not have just yet. But I also think
it's really important that you have to actually get alignment with your customer, and be upfront about what you can do
today and what you might be able to do in your future, and also agree on a timeline of what that looks like, get it in
writing, and have that sort of be part of the close of the deal. Where we went wrong, and I sort of laugh, because we
built what I thought was a freaking awesome product back in the day, we actually had a mugs API. This was in our demo
day slides.

Kevin Hale [28:45] - Like coffee mugs?

Harry Zhang [28:46] - Yeah, coffee mugs. There's a point where we thought it was a brilliant idea to be able to print
coffee mugs on demand through our API. We wanted to be able to print on anything. How this happened, we had a customer
who came to us and told us that they had this use case for coffee mugs, and it was a big number, a really big number for
us. And when you're small, every single deal looks super valuable, and we were like, "This is awesome. It will be so
cool to do coffee mugs!" We built the product. So we told the customer, "We can definitely do it for you. We'll have it
for you Tues." And we scrambled, and we hustled super hard. We built a fully-functioning mugs API product, but we didn't
sign any paperwork for this customer. We built this whole entire thing. We spent two weeks of valuable engineering time.
We met the customer. Mr. Customer, we have the mugs API, here's how you use it. And he was like, "Awesome, we'll get
right on it." He went dark, he stopped responding. I was super disappointed. To this day, we sold two mugs through our
mugs API, two. One of 'em went to another YC partner, actually, Dalton. He was working at [App.net](http://App.net), and I convinced him
that he should definitely do mugs as well. And I think he put in one order for it, and it worked. He's like, "This is
awesome." We killed the product a little bit shortly after. But I think it was a really valuable lesson in that you
always want to be selling a little bit ahead of where you are, but you also want to align with the customer

Harry Zhang [30:11] - what you actually have and don't have. That actually helped us close one of our biggest
customers today in [Booking.com](http://Booking.com). Essentially, how this opportunity came about is they were already
a customer of Lob using our address verification API. They had sort of this moment in time with GDPR where they started
reevaluating all their vendors for print. We sort of got roped into consideration. One of the key things that was really
important to them was actually having operations in Europe. They were familiar with our API in the US. They knew it
worked really well. But they're a global company, and of course, they want to know what our long-term plan is to support
Europe and eventually Asia. Part of the negotiation as we're working through this big deal with this customer is that we
need to align with them on a timeline in how we were going to get Europe up and running for them. For us, that's
originating letters, and postcards, and our other mail offerings in Europe, and that was sort of tricky. But I think we
had learned some valuable lessons in that we weren't going to just go and build all of Europe and scramble for
potentially months at a time. But we also weren't going to tell a customer something we didn't have either. We were
pretty upfront about them about what our capabilities look like, the timeline at which we were going to roll out. We
actually agreed to all these things at during our negotiation. What it really helped is our customer actually wanted to
help us get things going faster, right?

Harry Zhang [31:36] - They're like, "We want you guys to get up and running Europe right now." We could actually ask
for their help in building exactly what is they want. Now it's sort of like a partnership. Rather than like, "Hey, we've
oversold something," it's more about how can we work with our customer to achieve the results that we both want to get
to. I think that's really important, especially as you're talking about larger enterprise deals. You're not always going
to have everything, but really sort of structuring and not overselling it, but also setting the right expectation of
customers. It's difficult to navigate that sometimes. But we found as a policy, it's better to be upfront and honest
about what you can and can't do. Actually, if the customer really wants to work with you, they're going to find a way to
make it work with you, and that's the best position to be in.

Craig Cannon [32:17] - Are there other examples where you get a potentially incredibly high-value kind of enterprise
scale client, and they want something that you don't do. Do you now kind of fish around to see if anyone else is
interested in the mugs API before you follow through with it?

Harry Zhang [32:32] - Definitely. A common example of this is where I was evaluating a mail format. So what I mean by
that is you get different types of letters, all shape and sizes. We don't support every single different mail offering
today. But we have a list of what people have been asking for. And what we found is for us, it's a little bit of a
chicken-egg problem. We don't want to start with a really small-volume customer, because it makes it difficult for us
operationally. But same time, it's like we also know that this is a product people are interested in. They want to see
proof points. What we found is we have a list of these mail form intakes we're constantly evaluating. When we talk to
potential customers, we know here's a list that we would potentially be willing to consider. If they can agree on a
commitment level of what they're going to send, and then we're willing to entertain some of those areas. That's actually
how we built some products in the past before. We recently just launched, I think earlier this week, certified mail
receipts. We knew that when we launched certified mail, this is for William Whey, if you guys remember. He needed
certified mail. We launched certified mail, but he didn't need certified mail tracking receipts, because he didn't
really care when it received. He just cared that he had a proof point.

Harry Zhang [33:45] - But we knew that that was something that we could potentially do. We chose not to do in early
age, because we didn't have customers willing to do that en masse. So we got a few customers that were really interested
in certified mail but felt like we were missing this one little thing in mail receipts. We had that sort of plan, and we
had thought about it. Finally, we had the right customer who come if we're willing to make that commitment level, were
already familiar with our product. We actually went and built it, and we just launched that this week.

Craig Cannon [34:12] - Congrats.

Kevin Hale [34:13] - The way that API works is you guys provide this technology layer, and you connect to a network of
all these printers.

Harry Zhang [34:20] - That's correct.

Kevin Hale [34:21] - All around the world?

Harry Zhang [34:20] - That's correct.

Kevin Hale [34:23] - What I'm kind of curious about is you've seen this trend that sort of sees companies get larger
and larger where they get more vertically integrated, where they all want to do every step of the process so they can
own it in terms of quality but also in R&D, et cetera. And I'm kind of curious, do you feel like is that a thing that
you guys will eventually do? Or if not, why not? For example, it's just like basically, you buy a printer, or you own
some printing facilities and be like, okay, great. Because this whole flexibility and mail format, et cetera, part of
the reason that you have to be cautious about what you go into is because you have to go and spend time to find the
right partners, build out the integration, and then sort of make it work. I'm just kind of curious about is there a
point in the future where Lob owns a giant printer?

Harry Zhang [35:12] - We don't have that in the plan today is the short answer, right? Certainly, if there's a huge
need, we'd consider it. But the motivation for us is we see mail as this somewhat commoditized product. We also know
that it's a huge industry for a reason. There are hundreds of thousands of printers that are out there, but they all
specialize in slightly different things. For us to be good at what we do, we can't try to do everything at once. It
would actually be really difficult and super capital-intensive for us to buy all of the necessary hardware. What if our
customers need to change? We wanted that flexibility, and part of having sort of a network of folks enable us to have
that flexibility. I remember in our very early days at Lob, we were still, this is pre-Lob, or pre-YC application, one
of the things we want to do is we sort of just want to get our own printer. We were like, "Hey, it'd be nice if we could
just do it ourselves. Why do we need to rely on somebody else?" That's just another place for something to go wrong.

Kevin Hale [36:17] - Because you're looking at all these printers, and probably like, "These guys are in the Stone
Age. We should be replacing them."

Harry Zhang [36:22] - Yup, that's exactly right. We called up an HP Indigo vendor. If you guys don't know, HP Indigos
are like the commercial print standard. Everyone uses them. They're the Ferrari of printers. It's like this is what you
want, trust me. We'd figured this out. Honestly, we didn't know too much about the print world at the time. We called
the sales rep. I think the first time for him should've been like it was weird that we were meeting in a Starbucks. We
met this guy at Starbucks. We didn't have a company. We didn't have a product at the time. And we were like, we're just
going to get this printer, because we can do it better. So we start asking him all the right questions like, "Ooh, how
are we going to do inserter? Or what are the different formatting options?" We cover everything. And this guy's feeling
really good about this. And we're like, "Yeah, this guy's really smart. He knows exactly... and we're definitely get
this. My co-founder loves to negotiate. He's like, "So how much would this cost?" And he's sort of taken aback. And he's
like starts immediately talking about their leasing options.

Harry Zhang [37:19] - And in my head, I'm like, I don't want to lease this. I just want to buy it. We're about to go
get some money, and we're going to raise capital. We're going to go buy this and do it. We sort of corner him a little
bit. We're like, "All right, how much would it cost? Offer us a better price if we just buy outright." And I think, I
don't remember the exact number, but it was something like over a million dollars. And I sort of looked at Leore, I was
like, "Dude, we're not doing that." It was like no chance we're going to buy that printer. But I think thinking about
where we are today, maybe we do want to buy that printer, but it immediately creates a ton of complexity in our
business.

Kevin Hale [37:54] - Absolutely, and that's the thing I'm always curious about-- Is Amazon could've continued
using 3PL services. But at some point, they realize, we need to own and build our own warehouses to build up a certain
efficiency. We have a vision for the future that requires us to own that technology set. I'm just curious, at what point
do you guys start to be like, "Oh, you know what, we're, we're being held back by our partners?"

Harry Zhang [38:22] - That's a good question. We haven't felt that way, and our partners have been incredible
partners. Honestly, they're experts at print. They know so much more down to the color calibration that we should be
using on all of our printers. The places we'd be willing to think about it is if it could give us a competitive
advantage. If we're able to offer something by owning the print infrastructure, that would give us the ability to do
something nobody else can. But I think that's complex for us, right?

Kevin Hale [38:50] - That would be like, "Hey, we have a awesome hardware printing engineer who thought of a
completely new way to do print. And we're going to go compete with HP's imaging division. And we decided we can offer
something that nobody else has done. We can do this new method of printing on plastic." Oh, if someone came out on the
market with a brand-new type of printer that can do offset printing dynamically.

Harry Zhang [39:16] - If someone could do offset printing using a digital methodology at a price point that was not
achievable in the past. I would be interested in talking to anybody who's starting that company, by the way.

Craig Cannon [39:26] - The Tesla of printers.

Kevin Hale [39:29] - Right.

Craig Cannon [39:31] - Cool, so you guys are now six years old?

Harry Zhang [39:34] - Six years, coming up soon.

Craig Cannon [39:34] - How have you had to change as a founder and a manager over those years?

Harry Zhang [39:39] - It's a good question. I think the first thing, and I'm still getting comfortable with it now, is
understanding that your role as a founder is going to constantly keep changing. For some reason in the early days, I was
just like, "Hey, I'll just constantly be building cool product." Then I found a place where we needed somebody go do
sales, so I led the sales team for a number of years. And then all of a sudden, we were doing okay on sales, but we
didn't have any leads, so I started working on marketing. I think what I found is that my role's going to continue to
change. That's something you have to get comfortable with as a founder is that your role is going to change, and that's
okay, because what that's essentially saying is that you guys have gotten good enough that you can hire somebody else to
do that. That's an expectation everyone should have when you go into business that you should be comfortable with every
aspect. A lot of people think that they can just build product forever. Everyone should talk to customers. Everyone
should be going and trying to do sales in the early days, because if you as the founder of the company can't sell the
product, nobody else is going to be able to either.

Craig Cannon [40:44] - Yeah, that's a great piece of advice. All right, thanks, man, thanks for coming in.

Harry Zhang [40:47] - Yeah, absolutely, thanks for the time, guys.

Kevin Hale [40:49] - Thanks, Harry.
