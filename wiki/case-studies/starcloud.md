---
title: StarCloud
type: case-study
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["StarCloud", "Lumen Orbit", "orbital data center", "data centers in space", "space computing"]
related: ["[[Hard Tech Startups]]", "[[Sam Altman]]", "[[Founder Mindset]]"]
sources: ["N6-inside-the-startup-launching-ai-into-space"]
speakers_referenced: ["Philip Johnston"]
---

# StarCloud

StarCloud (formerly Lumen Orbit) is a YC-backed company building data centers in space. In November 2024, the company made aerospace history by launching a satellite carrying an NVIDIA H100 GPU into orbit -- "the first time anybody's tried to launch data center grade terrestrial Earth-based GPUs into space" and "a hundred times more powerful than any computer that's ever operated in the vacuum of space" [1].

## The Idea: From Space Solar to Orbital Compute

Co-founder Philip Johnston initially explored space-based solar power -- large solar panels in orbit beaming energy to Earth. The economics did not work: "You lose 95% of the energy transmitting it from space to Earth," and the break-even launch cost was approximately $50 per kilogram, far below current rates [1].

The pivot: instead of sending power down, send the data centers up. By consuming solar energy in orbit rather than transmitting it to Earth, the break-even launch cost shifted to $500 per kilogram -- "much closer to that today than we are to $50 a kilo" [1]. This became the basis for a white paper and eventually the company.

## The Technical Thesis

Operating in sun-synchronous orbit, StarCloud's satellites draw uninterrupted solar energy, radiate waste heat into deep space via large deployable radiators, and consume zero fresh water [1]. The company argues this solves three terrestrial data center constraints simultaneously:

- **Energy**: Data centers are creating an "absolute tidal wave of demand for energy" that Western infrastructure struggles to supply [1]
- **Water**: Terrestrial data centers cool through water evaporation, "causing huge problems in certain parts of the US where they're just sucking the rivers and the lakes dry" [1]
- **Land**: Orbital data centers scale without land constraints [1]

The core IP is the deployable radiator. Co-founder Ezra Feilden, who has a PhD in engineering and spent a decade designing satellites including NASA's lunar pathfinder mission, leads the thermal dissipation work. "Half our engineering team is building a very large, low-cost and low-mass deployable radiator" [1].

## The Team

The three co-founders have complementary backgrounds [1]:
- **Philip Johnston**: Applied math and theoretical physics (undergrad and masters), five years as a software engineer. Not from a space engineering background.
- **Adi Oltean**: Twenty years building data centers at Microsoft, then principal software engineer at SpaceX. Owns the compute module and radiation hardening.
- **Ezra Feilden**: PhD in engineering, decade of satellite design including deployable solar panels for NASA. Owns all satellite structure.

Johnston describes the team as covering "commercial compute, payload, and satellite structure" -- the three essential domains for the product [1].

## Speed of Execution

StarCloud went from founding to having a designed, built, and tested satellite in 15 months [1]. Johnston states that the previous record for any startup going from day one to having something on orbit was four years [1]. The speed came from building the compute module and antennas in-house by hand, with engineers "working through the night up until the day that we shipped down the payload" [1].

## The YC Path

The team applied to YC three times before being accepted [1]. In their initial application, they applied only for the near-term business of providing cloud services to other satellites. They knew about the larger vision of orbital data centers for all non-low-latency compute but were "maybe even embarrassed to talk about such a grand vision." YC "encouraged us to go for it" [1].

Johnston cites a [[Sam Altman]] talk as inspiration: "It's easier to build a hard company than it is to build an easy company. There's one hard thing, which is: can we operate data centers in space cheaply? If we can do that, everything else is easier. Hiring amazing people is easier. Getting people to write about us is easier. Even fundraising is easier" [1].

## Roadmap

- **StarCloud 1** (launched November 2024): 60 kg satellite with NVIDIA H100. Demonstration workloads including first model training in space, first fine-tuning in space, and first Gemini inference in space [1].
- **StarCloud 2** (planned October 2025): At least 10x more powerful, carrying NVIDIA Blackwell architecture with multiple GPUs and high-bandwidth optical terminals for 24/7 low-latency connectivity [1].
- **Long-term vision**: Full 40-megawatt data centers of approximately 100 tons, fitting in one Starship payload bay. The ultimate goal: "almost all data centers, anything that doesn't require very low latency, is operating in space" [1].

Johnston acknowledges they may be "a decade plus away from their grand vision of massive 5 gigawatt data centers in orbit" but notes the company is no longer alone: "Google, SpaceX, Amazon -- they are all exploring data centers in orbit" [1].

## References

1. [Inside The Startup Launching AI Into Space](https://www.ycombinator.com/library/N6-inside-the-startup-launching-ai-into-space) -- Philip Johnston (2025)
