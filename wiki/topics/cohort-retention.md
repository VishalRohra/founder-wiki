---
title: Cohort Retention
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["cohort retention", "retention curves", "cohort analysis", "retention metrics", "layer cake chart", "triangle chart", "user retention"]
related: ["[[Growth]]", "[[Product-Market Fit]]", "[[Product Development]]", "[[David Lieb]]"]
sources: ["LV-how-to-improve-cohort-retention"]
speakers_referenced: ["David Lieb"]
---

# Cohort Retention

Cohort retention is the practice of tracking what fraction of new users keep using a product over time, grouped by when they first started. [[David Lieb]], YC Group Partner and the person whose work at Bump became the basis for Google Photos (which serves over a billion users), describes it as "the single best way I have found" to answer whether a startup has made something people want [1].

The YC motto is "make something people want." Cohort retention is the quantitative answer to whether you have done it [1].

## Defining the Three Variables

To measure cohort retention, three things must be defined [1]:

### 1. Cohorts

How to group new users into individual groups. The most common method is by when they first used the product -- all new users in January form one cohort, February another. As analysis matures, cohorts can be sliced by country, acquisition channel, device, or customer characteristics [1].

### 2. Actions

What counts as a user being "active" in a given period. The simplest definition -- "did they open the app?" -- is often too shallow. A better approach is to pick a specific action correlated with the user actually getting value [1]:

| Product | Recommended Action |
|---|---|
| Instagram | Viewed 3+ posts (filters out accidental opens) |
| Uber | Completed a ride |
| Google Photos | Tapped to view a photo full screen |

Lieb's rubric: "Imagine you're sitting next to one of your customers. They're using your product. When you watch them, what is the thing going through your head that helps you answer whether that user is a good user?" Whatever that answer is, use it as the action [1].

### 3. Time Period

The granularity at which subsequent usage is measured. This should match the product's intended frequency of use [1]:

| Product Type | Time Period |
|---|---|
| Social/entertainment (Instagram, TikTok) | Daily |
| Utility (Google Photos, Uber) | Weekly |
| Travel (Airbnb) | Quarterly or annually |

## The Core Insight: Flatness Is Everything

The single most important thing about cohort retention curves is whether they get flat. "The only, only thing that matters is whether your cohort curves get flat. The shape of the curve is what matters, not the absolute number" [1].

Lieb illustrates with two products: Product A retains 75% of users after month two but continues declining toward zero. Product B drops to 20% quickly but then flattens. Product B is in a far stronger position because it can accumulate users over time. Product A is on a treadmill -- acquiring new users while losing old ones [1].

Even Google Photos had curves that "would drop off pretty quickly, but then they would get flat somewhere between 20% and 40%." Lieb recalls: "If you talk to a friend and told them '80% of my users leave pretty immediately,' they would think it sounds pretty bad. But the fact that 20% of users pretty immediately demonstrated that they would stay with the product and use it every week for basically forever" gave him confidence that Google Photos would eventually reach a billion users. Four years later, it did [1].

## The Triangle Chart and Layer Cake

The raw data is organized in a triangle chart: rows represent cohorts (months), columns represent subsequent months, and cells show how many users from each cohort returned [1]. Each user is counted once per period, regardless of whether they returned once or ten times. The number can go up or down but never exceed the initial cohort size [1].

The diagonal of the triangle chart represents a single calendar month -- showing how many active users came from each cohort in that month [1].

Converting to percentages (dividing by initial cohort size) normalizes the data and reveals whether newer cohorts perform better than older ones [1].

The layer cake chart aligns cohorts by absolute time rather than relative time, stacking them to show total active users. "If you see a layer cake where the top line is growing really nicely and it's composed of thick layers coming from old cohorts, this is like the most beautiful chart that you'll ever see in your startup" [1].

## Common Ways to Fool Yourself

Lieb speaks from personal experience, having made every one of these mistakes at Bump [1]:

### Picking Too Large a Time Period

The most common mistake. By widening the measurement window (from weekly to monthly to quarterly), curves appear flatter and higher by definition. At Bump, the team looked at weekly cohort retention, saw bad numbers, widened to monthly (which looked better), then convinced themselves quarterly was reasonable. "But we were fooling ourselves. Bump was not designed to be used once every quarter" [1].

### Picking Too Easy an Action

Using "opened the app" as the active user definition is gameable through notifications. Google+ defined active users as anyone who saw a notification bell in the corner of any Google product. "It made the active user numbers really big, and so everybody felt good. But if you looked at the cohort retention, it was a lie" [1].

### Using Payment as the Only Action

Counterintuitively, "is paying" is often not the best action. Users first stop using a product and then stop paying. "I'm sure we each have streaming services like Netflix that we're paying for, and the last time you watched a show might be more than a month ago, but you probably haven't canceled" [1]. Better: pair "is paying" with "is an active user" [1].

### Looking at a Single Data Point

Founders commonly report a metric like "80% week-over-week retention" without knowing the numerator, denominator, or which week it refers to. A single point tells nothing about whether the curve is flat or heading to zero [1].

### Trusting Analytics Tools Blindly

Built-in cohort analysis in tools like Mixpanel or Amplitude may not measure exactly what founders think. Some tools measure "rolling retention" rather than per-period cohort separation. Lieb recommends building cohort retention curves manually using logs or Google Sheets first, then comparing to analytics tools [1].

## How to Improve Cohort Retention

### Improve the Product

New use cases, reduced latency, simpler flows. Product improvements show up as newer cohorts performing better -- flattening sooner and at higher levels [1].

### Acquire Better Users

Often the easiest improvement. If a product targets the wrong customers, switching acquisition channels can dramatically improve retention. Lieb describes Google Photos targeting Gen Z users at one point: "Those cohorts had really bad retention. And it kind of makes sense -- Google Photos is a tool to accumulate your life's memories and reminisce. If you're a young person, you don't have that many life memories yet" [1].

Slicing cohorts by dimension (country, device, company size, acquisition channel) can reveal which segments retain well and which do not [1].

### Improve Onboarding and Activation

Often overlooked. Companies invest in building the tool itself but not in teaching people to use it. "What are they doing yesterday before they used your product, and what do you want them to change about their life today? Investing in this often is the cheapest and easiest way to improve your performance" [1].

### Build Network Effects

Products where each subsequent user makes the product better for existing users -- social networks, messaging apps, sharing platforms -- naturally see cohort improvement as the network grows and becomes denser [1].

## The Holy Grail: Curves That Go Up

The best of the best is cohort curves that do not just get flat but actually increase over time. Users who stick with the product start using it more and more. "If you see that your cohort curves are getting flat and then increasing, and subsequent cohorts are getting better and better over time, you should be feeling really good" [1].

## Connection to Growth

Cohort retention is the prerequisite for sustainable [[Growth]]. [[Anu Hariharan]]'s growth team guide is explicit: do not build a growth team before you have proven retention. The retention benchmarks by vertical in the Growth article provide specific targets for what "good" looks like [1].

## References

1. [How to Improve Cohort Retention](https://www.ycombinator.com/library/LV-how-to-improve-cohort-retention) -- [[David Lieb]] (2024)
