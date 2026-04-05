---
title: "Bump to Google Photos: From Contact Sharing to a Billion Users"
type: case-study
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["Bump", "Bump app", "Google Photos", "David Lieb", "Flock app", "Photo Roll", "Bump YC"]
related: ["[[David Lieb]]", "[[Product-Market Fit]]", "[[Pivoting]]", "[[Doing Things That Don't Scale]]", "[[Talking to Users]]", "[[Growth]]", "[[AI and Startups]]", "[[Network Effects]]"]
sources: ["5f-on-starting-and-scaling-one-of-the-biggest-ios-apps"]
speakers_referenced: ["David Lieb", "Gustaf Alströmer"]
---

# Bump to Google Photos: From Contact Sharing to a Billion Users

Bump (YC S09) was one of the first breakout apps on the iPhone App Store, reaching 150 million downloads and 10 million monthly active users. Its founder, [[David Lieb]], pivoted twice before arriving at the product insight that became Google Photos, one of 17 billion-user apps at Google. The story illustrates the difference between viral adoption and sustainable business, the mechanics of pivoting from user feedback, and how an acqui-hire can become the vehicle for realizing a startup vision at massive scale.

## Origins: A Business School Side Project

Lieb was a full-time MBA student in the fall of 2008, the year the iPhone App Store opened to third-party developers. A classmate had built a WiFi-finder app and earned $200,000 over the summer selling it [1]. The business model was obvious: apps were new, people were buying them.

The product insight came from the friction of exchanging contact information. Lieb recounted doing the manual exchange -- "tell me your phone number, I'll type it in, then I'll call your phone, you miss the call" -- ten times in one day with new classmates. He emailed Andy Huibers, a former colleague from Texas Instruments, proposing they build an iPhone app to solve this. Huibers initially thought Android would be bigger, but they started with iPhone [1].

Lieb, Huibers, and Jake Mintz (a classmate also from Texas Instruments) built Bump in their spare time. They launched on March 27, 2009 [1].

## The Billionth Download and the YC Network

Growth was 100% word of mouth. Lieb estimated the total marketing spend at $42 -- "a video tape to put into a borrowed camcorder and a black piece of felt" for the demo video [1]. The chicken-and-egg problem (you cannot use Bump unless the other person also has it) turned out to be the distribution engine rather than an inhibitor: the novelty of physically bumping phones made people willing to convince friends to download it [1].

Lieb executed a press ladder strategy: he emailed a reporter at the Chicago Tribune, then forwarded that article to David Pogue at the New York Times, then escalated further. The breakthrough came when Bump was the billionth app downloaded from the App Store. Apple called Lieb to confirm his servers could handle the publicity. He called his co-founder: "Andy, are we going to be able to do this?" The answer was "I don't know," which Lieb interpreted as "that sounds like a yes" [1].

During YC, Apple included Bump in its international "There's An App For That" TV campaign. The team first learned about it when their graphs showed "a factor of 1,000 in 10 minutes" and friends started texting them saying they'd just seen Bump on Dancing with the Stars. The servers melted down. Lieb sent an email to the YC founder network asking for an Apache expert. Founders came to their office and said, "Step away from the keyboards. We'll fix it" [1]. This was the moment Lieb understood the value of the YC network, validating what Paul Graham had told him: "I won't be able to explain it a priori, why it's really valuable, but I guarantee you'll see that it's very valuable" [1].

## The YC Interview

The interview was with Paul Graham, Jessica Livingston, Robert Morris, and Trevor Blackwell. Before Lieb could speak, Graham said, "Give us your phones. We want to try it." Morris tried to hack it. Livingston asked about the founders' relationship and backgrounds. Graham put his head down, thought, and asked: "How does this become bigger than Google?" Lieb's reaction: "Dude, are you crazy?" But the question revealed how Graham evaluated ideas -- taking something that seemed frivolous and imagining what it could become [1].

## The Retention Problem: 150 Million Downloads, No Business

Fundraising was "super easy" [1]. Bump raised from Sequoia (Series A) and Andreessen Horowitz (Series B, $17 million), with Ron Conway doing the bridge. The thesis for all investors was the same: mobile is a huge wave, Bump is the most popular app, and it solves a real problem [1].

The fatal flaw was frequency of use. Lieb tracked total users and daily bumps but did not rigorously track cohort retention curves -- "I would be like, 'Oh, it's good,' and then I'd go and Google cohort retention curve" [1]. The reality: long-term retention was actually good (people kept the app on their phones and would use it again), but usage frequency was very low. With 10 million MAU but infrequent use, Bump could extract roughly $1 per user per year. "That's a nice business, but it's not a business that you go raise huge amounts of VC funding to go build" [1].

Lieb describes a broader lesson: "Our plan all to that point was just grow, grow, grow, grow. Facebook did it. Twitter's doing it. We'll just do it, too, and it'll be great. And I think we didn't understand the fundamental differences between our business and those businesses" [1].

In hindsight, Lieb believes Bump could have been profitable without VC funding. A freemium model where 1% of users paid a dollar would have been a viable business. But it would not have been profitable at the scale Sequoia or Andreessen Horowitz needed [1].

Lieb also offered a fundraising lesson: "Raise more money if you know how you're going to use that money today. If you have no idea how you're going to raise it... I'm very skeptical of raising money when you don't know why you need it." He wished he had raised less in the Series B because the extra runway delayed the existential reckoning by about a year [1].

## Pivot 1: Flock (Automated Photo Sharing)

By early 2012, growth was flattening. Lieb recalled PG's advice: "When you're stuck, go talk to your users. They will always tell you what they want" [1]. He pulled a list of the top 100 Bump users in the world and began calling them. The discovery: most heavy users were not using Bump for contact sharing. They were using it to share photos with spouses. "Well, it's just easier, and they get the full-resolution file, and I don't have to worry about attachments and emails bouncing" [1].

Simultaneously, the engineering team made a breakthrough. They had been developing Bump's pattern-matching algorithm (an early AI system that used multiple signals to predict which phones bumped). Engineers discovered they could predict who would bump with whom tomorrow by analyzing photo metadata -- the time, location, and co-occurrence of photos on different phones. If two users took photos at the same time and place, they would likely share them [1].

Flock married the user insight (people want automated photo sharing) with the tech insight (co-location can be detected from photo metadata). It looked at Facebook friends, identified when users took photos at the same time and place, and prompted one-button sharing [1].

The team loved it. Friends and family loved it. Then they launched, and "nobody downloaded it" [1]. The failure came down to the cold-start problem described in Chris Dixon's "Come for the tool, stay for the network" framework: the first user of a product must get value even if nobody else uses it. Flock required your friends to already have the app. "99% of people were like, 'Cool. Home screen,' and they never used it again" [1].

The key learning: to solve automated photo sharing, they needed to "upstream" themselves -- become the camera roll itself. If they were the camera roll, everyone would already be using the product, and sharing features would actually work [1].

## Pivot 2: Photo Roll and the Google Acquisition

The third product was Photo Roll, a better photo gallery app (inspired by how Google's Inbox reimagined email). It had Flock's sharing built in as a feature that would "light up" as friends joined. But they arrived at this insight at the end of their $20 million runway [1].

Lieb assessed the situation honestly: "We looked at it, and we said, 'I wouldn't invest in that.'" Storing all photos in the cloud would be expensive. Building this right required the resources of an operating system provider [1].

Google's acquisition brought the answer. The company's mission -- "organize the world's information" -- mapped directly onto what Lieb wanted to build. He found Google already had large teams working on face recognition, image content understanding, and scalable photo backup. "I just saw all this, and I'm like, 'Oh, this is going to be good'" [1].

What Bump's team contributed was the product insight: how people think about their photos and what the right design of a product should be. The combination of Google's AI capabilities and Bump's product vision became Google Photos [1].

## The Photo Assistant Design Method

Lieb designed Google Photos by imagining a hypothetical human photo assistant with unlimited time and intelligence. "If my co-founder, Andy, was my photo assistant, and all he did all day long was help me with my photos, what would he do?" [1]. The brainstorm produced a list of features:

- Back up every photo automatically (so losing a phone does not mean losing photos)
- Identify important people (who is mom, who is the girlfriend)
- Label every photo with its contents
- Create montage movies for anniversaries and meaningful events
- Edit dark or messed-up photos
- Suggest deleting blurry or low-quality images
- Remind you of meaningful moments from your past

This list became the product roadmap. Lieb describes this as "one of the first examples of AI solving real problems that people could resonate with" [1]. The nostalgia feature -- surfacing old photos on anniversaries -- tapped into what Lieb calls "one of the most powerful things in the human experience" [1].

## Product-Market Fit as a Spectrum

Lieb offers a nuanced view of [[Product-Market Fit]]. He argues it is not binary but staged: "You can have very great product-market fit with some customer base, but as you try to expand your customer base, you might find, 'Oh yeah, there's not product-market fit for these other people over here'" [1]. Even Google Photos, with over a billion users, has product-market fit for a large group but "there's another group of people who use our product that I wouldn't say is product-market fit necessarily" [1]. As a product scales, the next user who joins is very different from the first, and the product must evolve to serve them.

## AI in Products: Two Vectors

Lieb identifies two vectors for applying AI to products [1]:

1. **Scaling human-solvable problems.** Tasks that a skilled human can do but cannot do at scale or at an affordable price. Google Photos exemplifies this: a personal photo assistant is something any person could do; AI makes it possible for billions of people simultaneously.

2. **Solving human-unsolvable problems.** Tasks beyond human cognitive capacity, like optimizing data center power usage. These are riskier bets with potentially bigger payoffs.

Lieb advises AI startups to identify which vector they are pursuing, and then ensure the solution addresses a genuine user need. "Even though the AI tech is super cool, if the solution is like, 'Yeah, that's nice, but whatever,' then it's not going to work" [1].

## The Meta-Problem of Working on the Wrong Thing

Lieb's biggest mistake at Bump was over-focusing on system performance (optimizing microseconds) while missing the bigger picture. He cites [[Sam Altman]]: "The meta problem that kills most startups is working on the wrong thing. It's not screwing up whatever you're working on. It's not your competitors. It's that you were just focused on the wrong thing" [1].

## Advice on Acquisitions

Having experienced both sides of acquisitions (selling Bump, then acquiring companies at Google Photos), Lieb argues the most important question when evaluating an acquisition offer is: "Can you execute your vision towards a much larger audience in a better way inside this company or not?" [1]. Financial terms are secondary to mission alignment.

He notes that founders spend "laughably small" time with the people they will work with daily, while most discussion focuses on financial outcomes. Without fundamental alignment on product vision, an acquisition "is going to be a disaster" [1].

Lieb also uses a question when investing in startups: "If you could go acquire a big company with the purpose of furthering your vision, which big company would you acquire?" The answer reveals both ambition and long-term thinking [1].

## Consumer Product Durability

Lieb distinguishes between products that are popular temporarily and products that serve a durable human need. The test: "Tell me the thing that humans already do today in a limited, not as great way that you are going to somehow amplify times 10 or times 100" [1]. Facebook amplified social connection. Instagram amplified self-expression and social interaction. Products that introduce a novel format without addressing a fundamental need tend to fail once the novelty wears off. "Instagram already exists. So you're not solving a durable human need" [1].

## References

1. [On Starting and Scaling One of the Biggest iOS Apps](https://ycombinator.com/library/5f-on-starting-and-scaling-one-of-the-biggest-ios-apps) -- David Lieb, Gustaf Alströmer (n.d.)
