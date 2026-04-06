---
title: Cohort Retention
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["cohort retention", "retention curves", "cohort analysis", "retention rate", "layer cake chart", "triangle chart", "user retention", "churn analysis", "flattening retention curves"]
related: ["[[Startup Metrics]]", "[[Growth]]", "[[Product-Market Fit]]", "[[David Lieb]]", "[[Network Effects]]"]
sources: ["LV-how-to-improve-cohort-retention"]
speakers_referenced: ["David Lieb"]
---

# Cohort Retention

Cohort retention is the single best quantitative method for answering the fundamental question: have we made something people want? [[David Lieb]], YC Group Partner and creator of Google Photos, defines it as tracking what fraction of new users keep using a product over time, measured by isolating groups (cohorts) of users and watching their behavior in subsequent periods [1].

Lieb learned the importance of cohort retention the hard way. While pitching a prestigious VC firm for Bump's Series A, he was asked about cohort retention, gave a hand-wavy answer, and then Googled the term after the meeting. "I realized that what I said must have made absolutely no sense" [1].

## Setting Up Cohort Retention

Three parameters must be defined before measurement begins [1]:

### 1. Cohort Definition

Group new users by when they first used the product. The most common approach: all new users acquired in January form one cohort, February another, and so on. Weekly cohorts work for faster-moving products. As analysis matures, founders can slice by additional dimensions -- country, acquisition channel, device, or customer type [1].

### 2. Action Definition

The action determines what counts as "active." The simplest version -- did they open the app or visit the site -- is often too shallow. A better approach: pick a specific behavior correlated with the user getting real value [1].

Lieb provides examples of what major companies might choose [1]:
- **Instagram**: Viewed three or more posts (filtering out users who opened the app but left immediately)
- **Uber**: Completed a ride
- **Google Photos**: Tapped in and viewed a photo full screen ("If you viewed a photo full screen, you were actually getting value from the product")

The rubric: "Imagine you're sitting next to one of your customers. They're here at the table using your product. When you watch them use your product, what is the thing that's going through your head that helps you answer the question of whether that user is a good user?" [1].

### 3. Time Period

The granularity should match the intended usage frequency [1]:
- **Daily**: Social or entertainment apps (Instagram, TikTok, YouTube)
- **Weekly**: Utility products (Google Photos, Uber)
- **Quarterly or longer**: Infrequent-use products (Airbnb -- people travel three or four times a year)

## Reading the Curves

### The Triangle Chart

The raw data appears in a triangle chart. Rows represent cohorts (months); columns represent subsequent time periods. Each cell shows how many users from that cohort performed the action in that period. A user is counted once per period regardless of frequency. The diagonal line represents a single calendar month -- adding values along it gives the total active users for that month [1].

Converting raw counts to percentages (dividing by initial cohort size) reveals trends. Reading across a row shows how one cohort decays over time. Reading down a column shows whether newer cohorts are improving or declining [1].

### The Only Thing That Matters: Does the Curve Get Flat?

Lieb presents two hypothetical products to illustrate the core insight [1]:

**Product A** starts with high retention (well above 50% after the first month) but declines steadily toward zero.

**Product B** drops sharply, losing more than half its users in the first couple of months, but then flattens at roughly 20%.

Product B wins. "The only thing that matters -- and I can't stress this enough -- the only, only thing that matters is whether your cohort curves get flat. The shape of the curve is what matters, not the absolute number" [1].

The reason: if curves flatten, the company accumulates users over time. Even a small retained fraction, compounded across many cohorts, eventually builds a large customer base. If curves trend toward zero, the company is on a treadmill -- acquiring new users and losing old ones at the same rate [1].

### Google Photos as a Case Study

Google Photos' weekly cohort retention curves dropped off quickly but flattened between 20% and 40%, depending on country and device. Lieb recalls: "If you talk to a friend and told them, 'Yeah, 80% of my users leave pretty immediately,' they would think it sounds pretty bad. But the fact that 20% of users pretty immediately demonstrated that they would stay with the product and use it every week for basically forever -- it gave me a lot of confidence." Six weeks after launch, he was confident Google Photos would eventually reach 20% of all humans. Four years later, it passed a billion users [1].

## Common Self-Deception Traps

Lieb identifies four ways founders fool themselves about retention, speaking from personal experience with every mistake [1]:

### 1. Picking Too Large a Time Period

The biggest mistake. Wider time periods produce flatter, higher-looking curves by definition. At Bump, the team started with weekly cohort retention (the right period for their product), found the curves were bad, switched to monthly ("they looked better"), then convinced themselves quarterly was reasonable. "But we were fooling ourselves. Bump was not designed to be used once every quarter" [1].

The unconscious pull toward wider periods is strong because "who doesn't want to look better for investors, for employees, just to feel better about themselves when they're falling asleep at night?" [1].

### 2. Picking Too Easy an Action

Using "opened the app" as the action invites gaming. Notifications and alerts drive inorganic opens that do not represent real usage [1].

Lieb provides a cautionary tale from Google: Google+ measured active usage by whether a user saw a notification bell in the top-right corner of any Google product. "By doing that, it made the active user numbers really big, and so everybody felt good. But if you looked at the cohort retention, it was a lie" [1].

**Counterintuitive warning about payment as an action**: "Is paying" seems like the best measure, but users stop using a product before they stop paying for it. Lieb compares this to streaming services people pay for but have not watched in over a month. A better combination: "is paying and is an active user" [1].

### 3. Looking at a Single Data Point

Founders frequently report a single number -- "We have 80% week-over-week retention" -- without knowing which week, what the numerator and denominator are, or what the trend looks like. A product might have 75% week-three retention but a curve that is clearly heading toward zero [1].

### 4. Trusting Analytics Tools Blindly

Built-in cohort retention graphs in analytics suites often do not measure exactly what founders think they measure. Some tools use rolling retention instead of separating cohorts. Some measure "has returned at all by a certain date" instead of "returned during this specific time period" [1].

Lieb's recommendation: "Build these cohort retention curves on your own using your logs via a script or in Google Sheets. Do that a little bit upfront yourself to develop your own intuition about what's going on. And then compare it to what your analytics tool is doing" [1].

## How to Improve Retention

### Improve the Product

New use cases, reduced latency, simpler flows. Improvements show up as newer cohorts that flatten at higher levels and flatten sooner [1].

### Acquire Better Users

A misunderstood lever. Building a great product but targeting the wrong customer segment produces bad retention. Lieb saw this at Google Photos: a marketing push targeting Gen Z brought users with bad retention because "Google Photos is a tool to accumulate your life's memories and reminisce. And if you're a young person, you don't have that many life memories yet" [1].

Slicing cohorts by country, device, company size, or acquisition channel often reveals that some segments retain well while others do not. This is "often the easiest way to improve the performance of your cohorts" [1].

### Improve Onboarding

Founders "immediately jump to what the product does, but often you just need to help your users get into a good state." For B2B tools, this means thinking about how to get into the user's workflow: "What are they doing yesterday before they used your product, and what do you want them to change about their life today?" Investing in onboarding is often "the cheapest and easiest way to improve your performance" [1].

### Leverage Network Effects

Products where each new user makes the product better for existing users (social networks, sharing tools, messaging apps) should see cohort improvement as the network grows. Founders with this dynamic should "focus on building good, dense networks around the users that we have" [1].

## The Holy Grail: Curves That Go Up

The best possible outcome is cohort retention curves that flatten and then increase over time. This means users who stay are using the product more over time. Combined with improving subsequent cohorts, this signals that the company has made something people deeply want [1].

## The Layer Cake

When cohort data is aligned in absolute time rather than relative time, it produces what Lieb calls a layer cake chart. Each layer represents a cohort; the total height is the active user count for that month. "If you see a layer cake that looks like this -- that the top line is growing really nicely and it's composed of thick layers coming from old cohorts -- this is the most beautiful chart that you'll ever see in your startup" [1].

If cohort retention curves do not flatten, "the one thing you can be sure of is that you need to get out there, [[Talking to Users|talk to your customers]], understand what's going on, and hopefully make something that they want" [1].

## References

1. [How To Improve Cohort Retention](https://ycombinator.com/library/LV-how-to-improve-cohort-retention) -- [[David Lieb]] (n.d.)
