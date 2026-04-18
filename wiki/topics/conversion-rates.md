---
title: Conversion Rates
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["conversion rate", "conversion optimization", "landing page optimization", "improving conversion", "conversion funnel", "knowledge gap"]
related: ["Growth", "[[Pete Koomen]]", "[[Dev Tools]]", "[[Startup Pricing]]", "[[Kevin Hale]]", "[[Product-Market Fit]]"]
sources: ["6l-how-to-improve-conversion-rates", "KD-how-to-convert-more-visitors-into-customers"]
speakers_referenced: ["Kevin Hale", "Pete Koomen", "Aaron Epstein"]
---

# Conversion Rates

[[Kevin Hale]] teaches that conversion is one of the two main drivers of [[Growth]], alongside churn. Growth is the gap between conversion and churn [1]. Working on churn is easier than working on conversion, but conversion is the starting point -- the thing founders must get right first [1].

## When to Work on Conversion

Hale advises that conversion optimization should only be prioritized when the startup has a "leaky bucket" -- visitors arriving but not converting [1]. He provides industry benchmarks:

| Category | Conversion Rate |
|----------|----------------|
| Shareware (pre-internet free software) | ~0.5% |
| Casual download games | ~2% |
| Freemium SaaS (average) | 1.5-5%, median ~3% |
| Flickr (heyday) | 5-10% |
| AdultFriendFinder | 10-22% |
| Children's social networks | High (parents paying to occupy children) |
| TurboTax Online | ~70% |

Once a landing page converts at approximately 3% (2-3 out of 100 visitors sign up), Hale advises that "you probably don't need to spend that much more time on this. There's probably other things you should work on instead" [1].

## The Knowledge Gap Framework

Every conversion problem is a user interface problem. Hale uses a framework called the Knowledge Spectrum, created by interface designer Jared Spool [1]. It places all knowledge on a spectrum from zero to complete. The user sits at a "current knowledge point" and the interface sits at a "target knowledge point." The space between them is the "knowledge gap" [1].

Every interface problem reduces to closing this gap. There are only two approaches [1]:
1. **Increase the user's knowledge** (teach them what they need to know)
2. **Decrease the knowledge required** to use the product (simplify the interface)

## The One-Button Interface Exercise

Hale's most practical design exercise: imagine reducing the entire landing page to a single button [1]. Then ask:
- What is the minimum information needed on this page to get someone to press the button?
- Is there any information that would prevent someone from pressing it?
- Is there any missing information whose absence prevents pressing it?

The answer to these three questions produces the ideal landing page content [1].

## Seven Questions for Every Page

Hale evaluates every landing page and conversion interface using seven questions [1]:

### 1. What Is the Call to Action?

Is the button -- the thing the founder most wants the user to do -- obvious? The call to action should be placed as close as possible to what Hale calls the **magic moment**: "the experience, the knowledge, the information, the interaction that someone has with your startup and all of a sudden they get tingly inside, the light bulb goes off, they go, 'Holy fuck, I've been waiting for this my whole life'" [1]. The number of steps between clicking the call-to-action button and experiencing the magic moment should be as close to zero as possible [1].

### 2. What Is This?

Hale's test: "Can I copy-paste a sentence on this page that I can put into an email and send it to my mom and my mom goes, 'I understand what this is'?" [1]. Ninety-nine percent of the time, landing pages are filled with jargon and marketing language, and no single sentence clearly explains what the company does [1].

### 3. Is It Right for Me?

Visitors quickly try to identify themselves on the page. They want to see a reflection of themselves or their problems. Without this recognition, they leave [1].

### 4. Is It Legit?

The threshold is low: the site cannot look like a spam website. Beyond that, templates and modern design tools make clearing this bar straightforward [1].

### 5. Who Else Is Using It?

Users want to know others have adopted the product. This serves as a shortcut for both legitimacy and self-identification. Customer logos, testimonial counts, or usage numbers all serve this purpose [1].

### 6. How Much Is It?

Hale is emphatic: "How many times do you go to a website and go like, 'Well, I'll use this without knowing how much it costs. Sounds good to me. Let's just do it.' No one does that" [1]. B2B and enterprise companies are often afraid to list pricing, but hiding it damages conversion rates. If the product is free, explain the business model -- otherwise users feel paranoid about the catch [1].

### 7. Where Can I Get Help?

A percentage of users will always want to talk to a human, regardless of how thorough the documentation is. Some want to verify a real person exists behind the product. Others cannot be bothered navigating the site. If contacting someone is difficult, these users will not convert [1].

## Common Design Failures

Hale identifies several patterns that damage conversion through his live critiques of startup landing pages [1]:

- **Competing calls to action**: Multiple buttons on a single page create confusion about what the user should do next [1]
- **Magic moment buried behind many steps**: If the core product experience requires navigating through seven-step carousels or multiple sign-up pages, conversion drops [1]
- **Carousels**: "Carousels don't work very well because you're hiding information that I might want to have to answer any one of my seven questions" [1]
- **Beta language**: Phrases like "open beta" or "closed beta" telegraph unreliability and undermine the legitimacy question [1]
- **Logos without customers**: Press logos, partner logos, and award logos are not substitutes for evidence of actual users [1]
- **Affordance problems**: When the clickable element (the call to action) does not look like a button, users miss it [1]
- **Copy that buries value**: When the most compelling features are hidden in dense paragraph text rather than highlighted prominently, users miss what makes the product special [1]

## Design Review: Conversion Pitfalls in Practice

[[Pete Koomen]], YC Group Partner and co-founder of Optimizely, and Aaron Epstein review real startup websites and identify conversion failures in practice [2]. Where [[Kevin Hale]]'s framework is diagnostic (seven questions to ask), the design review provides concrete examples of what goes wrong and why.

### Competing Calls to Action

Rivet (a multiplayer infrastructure tool) displayed five different calls to action on a single page: "Click to Start," "Sign Up," "Tutorials," "Templates," and "Open Rivet." Koomen identifies the paradox of choice: "The more things you have competing for somebody's attention, the less likely it is that they're going to take any of those actions" [2]. Worse, each CTA led to a different experience -- one opened a game demo, one opened a community registration, one opened a beta signup via Typeform. The recommendation: "Reducing down to a single call to action and seeing what impact that had" [2].

### The Two-Question Test

Koomen evaluates every page with two questions [2]:
1. **Does this convince me that I want to sign up?** (Does the page explain what it is and why I should care?)
2. **Does the signup process talk me out of it?** (Once convinced, does friction kill the conversion?)

### Repeating the Call to Action

Decoherence (an AI video generator) demonstrated a best practice: repeating the same call to action throughout the page. "Start Free Trial" appeared at the top, as "Try Now" in the middle after showing examples, and again at the bottom. "If you're at the top, you're like, 'Oh yeah, this sounds cool.' If I start scrolling down, oh, and now there's a 'Try Now' right there" [2]. This pattern keeps the conversion path available regardless of where the user is in their discovery process.

### Reducing Friction to the Aha Moment

Koomen and Epstein emphasize mapping the full conversion funnel -- every click from landing to the "aha moment" where the user experiences the core value [2]. Epstein describes the diagnostic: "Map out your conversion funnel, every single step that a user needs to take from when they first land on your website until they get to that aha moment... and figure out which ones you can actually cut" [2].

A practical example: founders whiteboard the funnel and discover the aha moment is at step seven. Steps two, four, and five are unnecessary. Cutting them moves the aha moment to step two, "and things improve a lot from there" [2].

### Social Login Reduces Friction

Decoherence used Google login exclusively. Koomen notes that offering existing login options (Google, Facebook) "can increase conversion rates a lot" because users do not need to create a new username and password [2].

### Addressing Objections Proactively

Decoherence's "No credit card required" text next to the "Start Free Trial" button addresses the most common objection before the user raises it. Epstein explains: "If there's some objection that people have, then you can address that right out of the gate, right there on the page" [2].

### Social Proof Matters for Trust

For Solve Intelligence (AI patent writing), Koomen notes the absence of social proof is especially damaging when the stakes are high: "If I write a patent with them and I spend all this money to do it and it gets rejected because the AI wasn't good enough, I'm going to be upset." Something like "100 patents have been approved that were written by this" would build confidence [2].

### Carousels and Hidden Content

InEvent buried important features behind a 10-slide carousel. Koomen and Epstein confirm the Hale principle: "When you bury things behind tabs or a slider, nine times out of 10 it's not going to be seen" [2]. Better approach: distill to the most important features and put them directly down the page. "People will scroll" [2].

### Specificity Over Breadth

InEvent's headline "Go beyond in-person events" was ambiguous -- it could mean either improving live events or replacing them with virtual ones. Koomen's fix: "Instead of 'go beyond live events,' just 'event management software for live events, webinars' -- even that would have made it much clearer" [2]. This echoes Hale's "What is this?" question [1].

### Sticky Navigation

InEvent demonstrated a positive pattern: the "Book a Meeting" CTA button stuck to the top of the page during scrolling, ensuring it was always accessible. Combined with embedding the email form directly on the page (rather than behind a click), this reduced friction significantly [2].

### Auto-Scrolling Fights the User

InEvent's carousel auto-advanced even when the user's mouse was hovering over it. Koomen notes: "People use their mouse to kind of follow along with where they are. And so it can be a good indicator for where people are actually paying attention" [2]. Fighting the user's browsing behavior damages conversion.


## References

1. [How to Improve Conversion Rates](https://www.ycombinator.com/library/6l-how-to-improve-conversion-rates) -- [[Kevin Hale]] (2019)
2. [How to Convert More Visitors into Customers](https://www.ycombinator.com/library/KD-how-to-convert-more-visitors-into-customers) -- [[Pete Koomen]], Aaron Epstein (2024)
