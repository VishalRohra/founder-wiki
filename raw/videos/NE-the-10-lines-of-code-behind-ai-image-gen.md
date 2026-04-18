---
title: "The 10 Lines of Code Behind AI Image Gen"
slug: "NE-the-10-lines-of-code-behind-ai-image-gen"
media_type: "Video"
author: "Y Combinator"
speakers: ["Francois", "Host"]
categories: []
description: "Diffusion is the foundational machine learning framework behind state-of-the-art AI image and video generation, including Sora, Midjourney and Google Veo. In this episode of Decoded, YC General Partner Ankit Gupta sits down with YC Visiting Partner Francois Chaubard to discuss how diffusion works, walk through a code sample, and explain why everyone training models should understand it."
url: "https://ycombinator.com/library/NE-the-10-lines-of-code-behind-ai-image-gen"
youtube_id: "dC_3ys349bU"
youtube_url: "https://www.youtube.com/watch?v=dC_3ys349bU"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# The 10 Lines of Code Behind AI Image Gen

Diffusion is the foundational machine learning framework behind state-of-the-art AI image and video generation,
including Sora, Midjourney and Google Veo. In this episode of Decoded, YC General Partner Ankit Gupta sits down with YC
Visiting Partner Francois Chaubard to discuss how diffusion works, walk through a code sample, and explain why everyone
training models should understand it.

## Transcript

Host: Welcome back to another episode of Decoded. Today I'm sitting down with YC visiting partner Francois Shaard to talk about one of the most important topics in AI today, diffusion. Francois has been doing computer vision since 2012 when he started in Fei-Fei's lab. And after a decade running Focal Systems, he's currently back at Stanford finishing his PhD working on diffusion-based world models for AGI. We're going to break down what diffusion is, how it's evolved over the past decade, and how it's used today.

Francois: Thank you for having me.

Host: Well, we just got back from NeurIPS. We just spent a lot of time talking to researchers and thinking about all the newest models out there. Um, I think we saw diffusion pop up over and over in newer versions of these type of approaches that are not autoregressive LLMs. And so I wanted to talk to you about those today. So first, why don't we start by defining what is diffusion?

Francois: Diffusion is a very fundamental machine learning framework that allows you to learn any P data, any probability of data for any domain, as long as you have the data.

Host: So you're trying to learn some data distribution.

Francois: That's right.

Host: Now in a sense, all LLMs or all machine learning models are about learning data distributions. How does diffusion in particular—what stance does it take or what approach does it take to being able to learn distribution?

Francois: Yeah, I mean, I think you can use diffusion to always do that. The thing where it stands out in particular is mapping from high dimensions to high dimensions, especially in low data regimes. So, say I only have 30 images of Gary, which I actually have some code that we're going to walk through. Um, I only have 30 images of Gary, and again, we're in this thousand by 10,000 by 3 dimensional space, and I want to map to another 3 million dimensional space with only 30 training samples. And I can still do it, and it's pretty powerful in that way.

Host: Okay, cool. So you have this ability to use relatively small amounts of data compared to the dimensionality to learn a P data.

Francois: That's right.

Host: Um, what's the basic process by which diffusion works? Like, just walk through at a very high level, and we'll walk through the math a little bit later, but at a very high level, how does this process actually work?

Francois: We take some sample of the data—an image of Anka, an image of Gary—and we just hit it with noise. And then we just keep hitting it with noise and we create this train of noised-up images. It's very easy to create noisy images, right? It's hard to go backwards and create from noise images of you or Gary. And so then we flip it and then we try to have the model learn to reverse that process. And that's basically it.

Host: Okay, cool. So it's basically a noiser and a denoiser, and the denoiser is the model that you end up training.

Francois: Exactly, yeah. You will basically teach your model and give it noised-up images, and then have it learn intermediate representations to get back to P data.

Host: Cool. Nice. And what kinds of stuff is diffusion used for today? What are some applications that it's widely deployed in?

Francois: It's honestly surprising how applicable this process is. I think the original 2015 Joshua Sixine paper was on CIFAR-10, which is just images. Um, and I think it has its roots in images, but it is far more sprawling than just images. As you've seen, you know, DeepMind just won the Nobel Prize for doing this exact procedure on protein folding. Uh, you can drive cars with this with the diffusion policy paper, which is like an insane result. Um, you can predict the weather. Um, there's really no limit to the things that this can do.

Host: Yeah, it's pretty incredible to see. I mean, we have these image and video generation models that seem to be really advancing over the last few years. Stable diffusion is the one that I think many people have heard of, and then newer versions of it seem to be using this as well. And then yeah, in the world of life sciences that my company was in too, I think we see this newest generation of life sciences AI companies are heavily investing in this set of technologies. There's a model called DiffDock that works really well for predicting small molecule binding to proteins, and then yeah, AlphaFold, especially the newest AlphaFold versions, use diffusion pretty heavily. It's really cool to see the same core piece of technology apply to so many different domains.

Francois: Yeah.

Host: This class of models has evolved over the years, and you know, there's a whole slew of papers someone could read. So you should probably go read the papers to learn all the details. But maybe at a high level, we can try to trace out a few of the key innovations that happened, starting with the paper you already mentioned, that now led to the newest versions of these models. So how would you map those out? Like, what was the first kind of turn of the crank from this very high-level diffusion process you outlined? What was the first version of that that started to work?

Francois: Yeah, so I think that the 2015 original Joshua paper put up all the key pieces, all the key components of modern diffusion. And so like now we're just playing with different things. So the Euler schedule—how do we add noise at what weight? Like, that's a whole part that we can discuss. What's the loss function? Should I predict—should the deep learning model condition upon x of t, predict the actual data x of t minus one, or should it predict the error that was just added to it? Or should it predict the velocity, which is the error divided by the time? Should it predict the velocity of the start and the end? That's called flow matching. There's so many different plays on what the loss function is.

Host: So in all of those, the idea is still to do denoising.

Francois: Yes.

Host: Uh, but the objective for each of them is somewhat different from each other. And they're all pretty closely related—whether it's basically a delta between two things or the previous step or the first step—how did these all actually come together? But these are a series of papers that happened one after another.

Francois: Yeah, I think we just kind of hill-climbed on this Fréchet inception distance metric, which is kind of a kooky, weird measure to see how good an image is. Um, but we just kept getting better and better and better on it by doing these little tricks. And so like, it turns out that predicting the actual data itself is actually quite hard. And like, maybe predicting the error is actually easier. And predicting the velocity was even easier than that. And then predicting the global error across the entire diffusion schedule is even easier than that. And we just kept finding easier and easier ways to basically sample from noise to data.

Host: And here, when you say easier, was the ease largely driven by it being mathematically simpler, or it was easier to implement and engineer, or simpler to reason about? Or what got easier really?

Francois: It actually is that too, but I didn't mean it that way. What I actually meant was it's easier for the model to learn.

Host: Um, but it is also, and we'll go through some coding examples, the math actually got easier, yeah. And the code got smaller, which is actually oppositely true in most cases of machine learning. You actually—things get more complicated. I think we started with UNets and that was like the predominant architecture. We didn't really talk about architectures that much, but then we got into these diffusion transformers and like this cross-attention mechanism and things like that. And so, um, yeah, we just kept getting better and better at reducing FID.

Host: Interesting. Should we dive into some code examples?

Francois: Let's do it.

Host: I'll walk you through. I made about one, two, three, four, five, six, seven of these that I implemented with varying levels of success, but the structures are going to be the same. So the Joshua paper, the non-equilibrium thermodynamics paper—uh, you can see here, here are some nice images of Gary. You can see here, very nice. This is what I could find online.

Host: Nice.

Francois: Um, and so those are images of Gary that you've downsampled so that they're, um, they're smaller. These are 64 by 64 by 3.

Host: Yeah, they're really small. This is just a very small example, 64 by 64 by 3. And then I randomly augment it to create more data.

Francois: Great. Um, because I was lazy and that was easier than downloading more images.

Host: Cool. [laughter] Didn't want to get security call on you.

Francois: Exactly. So, and then wait, I implemented this diffusion schedule, and this is probably one of the most important, like, of all the parts of diffusion that's difficult to comprehend. I would say that the noise schedule is actually the hardest part to understand. I really—I struggled with it myself. And so if you can see here, the noise that's added from time step zero to t to 10 to 25 all the way to 100 is clearly destroying the structure.

Host: Yes.

Francois: And then we want to train—

Host: Where you end is basically random static.

Francois: Exactly. And we want to basically reverse this, and from here get to here, and have the model get to that point, get to this point, get to that point, et cetera. And so the interesting part—and this is Joshua, really—you know, implemented almost everything that we needed for diffusion. Um, and there was just a few little tweaks that were missing, and he didn't scale it up. That's to me the part that was missing. And if you see here, the noise schedule. So it would make sense to me that I would have linear interpolation between the image and the noise, and I would start with like one and zero—one being the image and zero being the noise. You gradually add it.

Host: And I gradually add it. But if you do that, it actually is massively unstable because the instantaneous amount of error that you're adding is very small in the beginning. If you think about like an image—

Francois: On a relative basis.

Host: On a relative basis. And then at the end, you have to destroy all the structure, to get to complete noise you need to add a lot of error.

Francois: And so like, if you're a model and you're just looking at this little chunk of the noise schedule, then you have to handle a lot of error in one step. And on this side of the schedule, you need to handle such small amounts of error. And what you actually want is constant relative—like, relatively constant amount of error being introduced every single time step, right? And the cumulative sum of all that error actually ends up looking like this curve here.

Host: That's the pink curve.

Francois: Yeah.

Host: And so they call this a beta schedule. Beta is the diffusion rate, the rate of diffusion that I'm doing, while I'm rolling this thing out from time zero to time capital T. And uh, and so you can see here the beta schedule. So we usually have some beta min to beta max, and then one minus that is the alpha. And you can think about the beta as like, how much noise I'm adding at every time step.

Francois: Yep.

Host: And you think about the alpha as how much is being retained. And then the term that really matters is the alpha bar. And these are the weights that are used, and it has this kind of like one minus sigmoid looking thing. Um, but that's basically the noise schedule. And once you get that right, really, this part here, then everything else just works. And then I train some model, and then we can actually—so there, what was the training objective again? So you were adding this noise, and the training objective was to do what exactly?

Francois: The training objective in this case is to minimize the Kullback-Leibler divergence between the distribution—the real distribution and the distribution that I'm learning. And so um, I won't go through the code for this one because it's a little bit hairier, but you can kind of see the result on these generated images. Um, after 100 diffusion steps at inference time. And you can see that the Fréchet inception distance is 222, which is like extremely high. Today, like, modern day would be like maybe eight or 10 or something.

Host: And what's interesting here—I mean, you kind of scroll through it there—but it's, and you mentioned it, there's quite a lot of code that it actually takes to do that Kullback-Leibler divergence base loss. I suspect that in these later models you're going to show, it gets significantly simpler. So I'm just mentally noting that because I suspect there's going to be interesting contrast to draw between these two.

Francois: Yeah. So the next one I would like to show is flow matching, which is just so beautiful and simple. Uh, and this was out of Meta by Yann Lecun—uh, where he basically said, "We don't need a lot of this stuff. What we need to do—forget the—if you think about the noising process as being this like, um, I start from data. I randomly sample a vector of noise and I just go in this direction. And then I do it again. I go in this direction, and I do it again. I go in that direction. I go in this direction, that direction, and then I'm here at noise. And then you have to teach the thing to go in the exact opposite path, and you have to do this very circuitous path. And so at test time, it's actually quite expensive. You have to do—we've all waited for, you know, ChatGPT or Midjourney to like make an image, and it takes a while. It's doing like a thousand calls to the model, again and again, iterating through to get to that point of P data, right?

Host: Instead—

Francois: And like, intuitively, it's like, okay, we're doing the circuitous path, but surely there's a shorter path between those two. And so that's what makes flow matching so cool to me, at least. Is that they said, "Forget all of that intermediary stuff. There is a velocity—a global velocity between the noise and the data, and it's just this direction. It's just this straight line. And I don't care where you are. Go in that line. Wherever you are, you're over here, go in that line," and teach it to go in that line. And that's what flow matching does. And so I'll show that in the code. I bet it's like five lines of code. It really is quite simple. And so this is pretty cool. So here you go.

Host: You basically have like 10, 15 lines of code that is the most powerful machine learning procedure ever.

Francois: So I have some data. I have an image of Gary.

Host: Yep.

Francois: I have some noise—that I—some isotropic Gaussian noise that I sample from.

Host: Yep.

Francois: There's some time that I'm trying to index into in the diffusion schedule. And I create XT, which is the noised-up image that's somewhere between extremely noisy and not noisy at all.

Host: And that's basically just the sampling procedure. It's T times data.

Francois: Yep.

Host: Plus one minus that times noise.

Francois: Yeah, that's right. And then I compute the velocity, which is independent of the time. I don't care where you are. It's this global velocity, which is just the noise minus the data. And then it I return that back to my training loop, which is the shortest amount of code training loop I've ever written, which is five lines of code. Um, I have my batch. I have some time. I sample from that function I just explained before. And then I have my prediction from the model. I feed it in—some element, some noise-up image, somewhere between lots of noise and little.

Francois: Noise x of t, let's call it, and I just want it to predict the velocity that I want to go.

Host: And this is also really powerful because here you know you have model abstractor, but that model can be any model right? So you can put in whatever the relevant model is for your distribution, whether that's a protein model for proteins or if it's an LLM for text or an image-based model for images.

Francois: That is a very clean abstraction as long as you can predict this velocity and then move in that direction.

Host: That's right. This code here has nothing to do with images. It could be weather data. It could be, you know, stock market data. It could be trajectories from a robotics in a teaops setup. It could be proteins. It could be DNA. It doesn't really matter. It's all the exact same code. And so, we haven't talked about the architecture. So like this model here could be anything you want it to be. It could be a RNN, it could be a UNET, which is typically, you know, traditionally, and modernly they use these diffusion transformers doing this cross attention mechanism. So it can be whatever you want. But all that is independent from whether or not you're doing flow matching or not. I think this is like a really profoundly interesting result in that, especially this. I think we often assume as models have gotten more sophisticated that they become less accessible for people to understand, but this is quite literally ten lines of code, right?

Francois: That explains essentially all of the most important kind of mathematical and fundamental foundations of the models that we all see as generating basically like magical AI results on our phones.

Host: Of course, there's lots of engineering how you scale them up. That model could be a hundred billion parameter across transformer data centers, you know, GPUs.

Francois: Totally. Yeah, 100%.

Host: So it's the engineering that's the really hard part there, but a lot of the basic machine learning math is actually quite straightforward.

Francois: That's right. Yeah. And so there's a bunch of these like tangent fields to diffusion that all have some different interpretation on what's actually happening, but it's all the same exact math. And most people learning diffusion actually get quite confused because if you talk to some probabilistic graphical model people, they'll say, "Oh, this is a probabilistic graphical model," and "What's actually this is a hidden Markov model," and "What we're doing is we're learning this like Markovian thing or whatever." It's like, okay fine, but like it's just noise.

[laughter]

And like you should just show that first. And then like if you think about it from like a physics perspective, and there's all this stat mech people that have that interpretation. There's a whole bunch of different interpretations. I think it gets a little bit confusing. And the whole stochastic differential equation people, like thinking about that this is an SDE. I think that's all fine and it probably is helpful to think about, but in terms of teaching it, it's actually quite quite simple, which is powerful.

Host: Cool. So if we go back to here, you can see that this just literally predicting the velocity. Your goal is to have the model predict you're minimizing the loss between predictive velocity and velocity.

Francois: And the actual velocity. That's it. And that's super stable. And it's really clean. And then at test time, for the physics people, this is like an Euler step kind of thing that you're doing, where you call the model a bunch of times and you iteratively refine. So back to the hill climbing that we were talking about, I'll grab some random noise here, x, and I just do and I call basically reverse that noising process to denoise, denoise, denoise, and it's literally Euler's method.

Host: Like you're using the velocity to point in the direction you want?

Francois: Point in the direction and just keep going, keep going, keep going until you've done the number of steps. The one thing that I really don't like about diffusion as it's done today is that I can't keep calling it beyond if I only trained on 100 diffusion steps in my diffusion schedule. If I change that at test time, it doesn't work. And so you can't like, "Oh, I want it even better, so I'll call it even more." That doesn't work. I've tried it. It doesn't work.

Host: Yeah. There's various tricks people try there, but yeah.

Francois: Yeah. And so like there's games played that is actually quite exciting. All the expense.

Host: But wait, sorry, should be clear here. Here you're saying that's not relevant, right? Because these in this type of model, you don't have this time dependency.

Francois: Well, so you do. So at this time, if you change, for example, the number of steps, if you double it, let's say that, and you expect to get even higher resolution images, it actually will just turn into like white. Like it actually just like doesn't work at all. So you can't step beyond number of steps that was trained.

Host: That's an important detail. There are tricks that people are doing to try to compress that representation. So like if at train time I train for a hundred steps and at test time I want to do ten steps, then what you can do is you can do distillation into the model to try to have the ten-step model learn the hundred step model's thing, but then you still got to train with ten steps. So if you're training with X steps, you have to be using X steps at test time.

Francois: I see. Interesting.

Host: You've talked about this concept of a squint test. Why don't you define the squint test for a second? Tell me a little about where this comes from and then I'd be curious to hear how you think about diffusion models in the context of general intelligence broadly.

Francois: Yann LeCun has this like interesting lecture where he talks about our discovery of flight and that we didn't need flapping wings. We kept trying to mimic a bat, and how that was a waste of time. And to that I say you're 100% right. However, we did need two wings. You look at the Wright brothers' original plane and you squint and you look at a bird, you're just like, hmm, while we have helicopters and we have jets and things like that, and rockets, like we got there eventually. And so there's many elements in the set of things that can achieve flight and they have different pros and cons. And there are many elements in the set of things that can achieve intelligence. We are the only existence proof of it at all. And like I'm sure there will be more elements in the set and maybe LLMs, broadly speaking, can get there. But if I squint and I look at LM setup, which I see this you know, monolithic stack transformers, the same thing, stack, stack, stacked, and there's three stages of training. We do this pre-train, you know, SFT, you know, post-train, and then no learning at all beyond that. And it produces exactly one token at a time.

Host: Right? So iterative token.

Francois: Iterative token at a time. And it never goes backwards. And then you look at a brain. Massively massive amounts of recursion. You have one learning procedure the whole time. You have these two lobes that with a corpus callosum between them that's kind of going back and forth like this. And we think, and then I definitely don't think in one token at a time. When I write code, I don't write one little character at a time. I never go backwards, and I kind of like am going backwards. I'm recursively improving. I'm going backwards again and again. I'm thinking in concepts. There's this like dynamic process that's emitting concepts and then higher level, higher level concepts, and then lower level manifestations of them.

Host: And I'm sure that may be happening inside the LLM, but it's like it's almost like stuck. It can't do more than in one step even though it might want to, because it has to is the way that we trained it, right?

Francois: Like it might have all that in the LLM, but then it's it's sort of bottlenecked, ultimately by only its action space is one.

Host: One token at a time.

Francois: And so I think that that's where I think about diffusion. There's like two main things that diffusion gives me. It doesn't get me all the way to pass my squint test, but it gives me two things that I for sure the brain is doing. Number one, the entire all of biology and nature leverages randomness. Randomness is good. And what is diffusion doing is leveraging randomness. If you give me data and I noise it up and from that I can learn about the data and like, is the can the brain add noise to input data? Absolutely. Absolutely. Like neurons are massively random. Lognormal distributions, spike patterns, and things like that. And the other one is this emission of one thing at a time versus thinking in concepts and then decoding into a big chunk of text and thought and revisioning of the previous thoughts and things like that. And so I think diffusion gives me both of those things for sure.

Host: People have probably heard of Stable Diffusion as a very common application of this. It's an image generation model that was pretty widely available for the last few years. What people may not be so aware of is all the other ways that diffusion is used in the last few years in products that people are widely using. So what are some of the areas in which diffusion is most widely accessible?

Francois: Yeah, it's really any mapping from very high-dimensional data to very high-dimensional action spaces or data that you may want to map to. And so, yeah, of course everyone knows generating images because we've done Midjourney and things like that, and even more modern versions of that with Sora and Veo and Flux and SD3 now and things like that. And we're generating videos, which is just images stable together, and videogen and imagegen and things like that. However, there's so many more applications that now we're seeing. That's the most exciting part in my view of all the new applications. And so whether or not you're now creating sentences, I mean diffusion LLMs was one of the biggest topics that we saw in Europe. Whether it's continuous diffusion LLMs or discrete diffusion LLMs, it's writing code now. It's creating proteins. I mean DeepMind won the Nobel Prize for that. There is robotic policies. This diffusion policy thing, which I think might actually be one of the biggest uses of it and will result in like robotics actually working and Boston Dynamics robot actually working. There's weather forecasting. For the GenCast, it is the most accurate weather forecasting system in the world. It's really anything. Even I mentioned Harrison working on the diffusion for failure sampling, just like sampling from for failures and like bad things that could happen. We can do that as well.

Host: So a lot of the products where we see people actually using AI, especially for things other than just text-based chat, a lot of them are using diffusion, especially on images and videos increasingly now, things like code and the life sciences. So yeah, pretty pretty wide birth of things.

Francois: Yeah, in fact, I would say the only two holdouts right now where state-of-the-art is not diffusion. Diffusion has eaten all of AI except two. LLMs still are outperforming, and gameplay and things like AlphaGo. And so MCTS is still state-of-the-art for those types of things. And so we haven't seen diffusion really take a step in those two areas, but more research is needed.

Host: So to bring the conversation to a head now, how should people think about this research area either as researchers contributing to the field or as founders looking to build a new product?

Francois: Yeah, I mean I would think about maybe there's falls in two camps. If you're training models yourself or if you're using models and you know, not in the business of training models. If you're in the business of training models, I would seriously look at diffusion. I don't care what your application is. You should be looking at this procedure. Even if it's just to get a latent space that you can then train off of. And so there's no application in machine learning that I don't think you should be heavily looking at diffusion procedures as a fundamental piece of your training loop. In the case of people who are not training models, I would just like update your prior on how good these things are getting. And if you just look in the last five years on how good image generation got from Midjourney when we first came out to Veo and Sora and Flux and SD3 now, it's like it's like a thousand times better, right? The answer was just scale it up. And that takes time and that takes money and all those things and data. And now you apply that to proteins. You apply that to DNA. You apply that to robotics policies, a self-driving car. I mean it is, skate to where the puck's going to go. All these things are going to work and we're watching it happen. It may cost money and time and you know those kinds of things, but those are solvable things. Those are tractable problems that we can go solve. And also the core procedure of diffusion is getting better. That's another major. Simpler a lot simpler, and it's getting like it's just working better. So skates to where the puck's going to go. Bet that Boston Dynamics robot will work in people's homes. Bet that the protein folding is only going to get better and now we're going to apply that to DNA and all these other metabolomics and things like that.

Host: We see founders develop new models for robotics or for text generation or for video using diffusion. And we see founders who are using all these methods coming from other places build companies on top of them. And it seems like there's this whole new wave of companies that can be built on either end of this now, right?

Francois: I think it's going to redefine the entire economy.

Host: Thanks so much for joining us. We're going to keep digging in on topics related to machine learning research like diffusion. Can't wait to see you at the next one.
