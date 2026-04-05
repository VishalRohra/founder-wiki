---
title: "Lob: From Inkjet Printer to Enterprise Mail API"
type: case-study
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["Lob", "Lob case study", "direct mail API", "mail automation startup", "Harry Zhang Lob"]
related: ["[[Harry Zhang]]", "[[Enterprise Sales]]", "[[Startup Pricing]]", "[[B2B Pricing]]", "[[Doing Things That Don't Scale]]", "[[Hiring Engineers]]"]
sources: ["6a-on-starting-and-scaling-direct-mail-automation-startup-lob"]
speakers_referenced: ["Harry Zhang", "Kevin Hale"]
---

# Lob: From Inkjet Printer to Enterprise Mail API

Lob (YC S13) makes APIs for enterprises to programmatically send physical mail -- letters, postcards, and other mail formats. Founded by [[Harry Zhang]] and co-founder Leore, Lob grew to nearly 70 employees over six years and signed enterprise contracts ranging from $30,000 to millions per year [1].

## Origin: A Problem Found at Microsoft

The idea started from complaining. Zhang was driving back from a ski trip with co-founder Leore and venting about a project at Microsoft. His team had built a system for sending custom training materials and webinar invitations, but email was not allowed and telesales was too expensive. The fallback was a direct mail campaign. It worked so well that Zhang received a large budget to scale it -- then spent three months struggling with the operational complexity of sending physical mail at scale [1].

## The Minimal MVP: An API That Did Nothing

When Zhang and Leore applied to YC, they had almost nothing built. Their MVP was an API that took whatever input it received and mirrored it back. "We were secretly hoping that we wouldn't have to demo, because honestly, we hadn't built a lot of product yet" [1]. [[Kevin Hale]], who evaluated them, confirms: "I would say it was fairly embarrassing in terms of what you guys had" [1].

What they did have was a deep understanding of the problem. They had talked to many potential customers and understood the core pain points of sending physical mail programmatically. Zhang frames their philosophy: "We've always operated from the point of view of we want customers to pay us for something before we actually go and do it" [1].

## First Customer: A 16-Year-Old Team Fortress 2 Merchant

Lob's first customer came from a Hacker News Show HN post. William Whey, a 16-year-old who ran one of the largest Team Fortress 2 stores online, had a fraud problem: when customers bought digital items, he had no proof of delivery, leading to chargebacks. His solution was to also send a physical letter with a confirmation code. He needed an API to automate this [1].

The use case was one Zhang would never have imagined. "I think it goes to show, you can always think you have a way to build a product, but not always" [1]. This early lesson about unexpected use cases shaped Lob's product strategy.

## The Assembly Line: Doing Things That Don't Scale

In the earliest days, the API connected to a database that Zhang serviced with his home inkjet printer. "We printed everything on my home printer out of my apartment" [1]. At one point, he and his co-founder were watching TV while running an assembly line of letters they stuffed by hand. Only when volume exceeded what they could manually handle did they seek commercial printing partners [1].

## The Lighthouse Customer Problem

Zhang describes the enterprise sales flywheel as a chicken-and-egg problem: "You need a lighthouse customer to get other big customers. Getting the first one is always the hardest" [1]. Lob's first major enterprise client was a large New York insurance company, found through cold email. The CEO responded, asked qualifying questions, and connected Zhang to the VP of Data. The insurance company needed HIPAA-compliant printing and had lost confidence in their existing print vendor [1].

Zhang's cold email approach: short, personalized, specific about the problem. "This is what we do, here's how we're different, and I think we can help you with your current problem in these three ways" [1]. He did not know about their specific HIPAA problem -- the timing was lucky, but the targeting was deliberate.

For subsequent enterprise deals, Lob maps out each target organization before outreach: who are the key stakeholders, what motivates each person, what's the right message [1]. They combine cold outreach with conference attendance and marketing that makes "Lob pop up everywhere" for the target account [1].

## The Mugs API: A Cautionary Tale

During YC, a customer requested coffee mugs printed on demand through the API. The revenue number looked enormous for a small company. Zhang's team scrambled for two weeks, built a fully functioning mugs API, then went to the customer. "He was like, 'Awesome, we'll get right on it.' He went dark, he stopped responding" [1].

Total mugs sold through the API: two. One went to [[Dalton Caldwell]], who was running App.net at the time [1].

The lesson: "You always want to be selling a little bit ahead of where you are, but you also want to align with the customer what you actually have and don't have" [1]. The team had built without getting commitment in writing.

## Booking.com: The Right Way to Sell Ahead

The mugs lesson paid off when Lob closed Booking.com, one of their largest customers. Booking.com was already using Lob's address verification API when GDPR prompted them to reevaluate all print vendors. They needed European operations, which Lob did not yet have [1].

Instead of over-promising, Zhang was upfront about current capabilities and negotiated a timeline for European expansion as part of the deal. "Our customer actually wanted to help us get things going faster" [1]. The transparency turned the deal into a partnership rather than a gamble. "If the customer really wants to work with you, they're going to find a way to make it work with you, and that's the best position to be in" [1].

## Pricing: The Platform Fee Innovation

Lob's biggest pricing mistake was structural. Initially, customers bought bundles of mail pieces (e.g., 100,000 letters per year) at a per-piece price. The problem: enterprise customers compared Lob's price directly to traditional mail providers and asked "why are you five cents more expensive?" [1]. The five cents represented Lob's technology value, but it was invisible in the per-piece comparison.

The fix: separate the technology from the commodity. Lob introduced a platform fee of $25,000-$30,000 per year for API access, with mail pricing at or below market rates for the physical product. "Now we can focus the conversation on how do you value Lob's technology, is that worth 25 to 30,000, instead of having a conversation about what is the cost of a mailpiece" [1].

This worked because enterprise customers were already paying agencies separately to manage mail campaigns -- money from a different budget line. Lob's platform fee captured the same value but made it legible within the customer's existing budget categories [1].

## HIPAA as a Pricing Lever

Regulated industries provided natural pricing power. HIPAA compliance costs Lob more to provide, but the pool of competitors capable of handling sensitive information programmatically is small. "We actually charge more for those customers, because it costs us more. And also because there's less offerings that are able to do something like that programmatically" [1].

The strongest signal for feature prioritization: "We had customers that will be like, 'We'll pay you if you guys can do X for us.' That's when you really know you're on to a feature that's really important" [1].

## API Documentation as Product Design

Hale observes that API companies are a pure expression of interface design: "the interface is just documentation" [1]. For Lob, documentation is the number one product priority. "When your core product is an API, you better have the best documentation on the planet" [1]. Hale compares this to Stripe, which set the standard for developer-facing API documentation.

## Vertical Integration: Why Lob Does Not Own Printers

Hale pressed Zhang on whether Lob would eventually vertically integrate and buy printing facilities, as Amazon eventually built its own warehouses. Zhang's answer: no. Printing is a commodity with hundreds of thousands of specialized providers. The network model gives Lob flexibility to support different mail formats and customer needs without massive capital expenditure [1].

The team almost bought an HP Indigo commercial printer before YC. They met a sales rep at Starbucks, went through the specifications, and then asked the price. "Something like over a million dollars. And I sort of looked at Leore, I was like, 'Dude, we're not doing that'" [1]. Zhang acknowledges they might eventually consider vertical integration, but only if it provides a competitive advantage that the network model cannot [1].

## RSUs Over Options

Lob uses a non-traditional RSU (restricted stock unit) structure instead of standard options. Zhang's reasoning: options require employees to spend their own money to purchase shares without knowing the outcome. "That puts you in this weird scenario where you want to buy your shares, but you're not sure if you want to" [1]. Lob's RSUs vest on a one-year cliff with monthly vesting thereafter, and taxes are owed only at a liquidity event -- when the employee already has money from the RSUs [1].

The retention mechanism: at the 2.5-year mark and every year after, employees receive additional retention grants. "The longer you stay at the company, the more equity you should be able to acquire. There shouldn't be a point where you ever stop earning equity" [1].

## The Founder's Evolving Role

Zhang describes the founder's role as perpetually shifting: from product builder, to sales leader, to marketing driver. "Your role is going to continue to change. That's something you have to get comfortable with as a founder" [1]. The shift is a positive signal -- it means the company has gotten good enough in one area to hire someone else. But the implication is clear: "If you as the founder of the company can't sell the product, nobody else is going to be able to either" [1].

## References

1. [On starting and scaling direct mail automation startup Lob](https://ycombinator.com/library/6a-on-starting-and-scaling-direct-mail-automation-startup-lob) -- Harry Zhang, Kevin Hale (2019)
