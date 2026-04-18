---
title: "Building AI Models Faster And Cheaper Than You Think  [Lightcone Podcast Ep. 4]"
slug: "Kl-building-ai-models-faster-and-cheaper-than-you-think-lightcone-podcast-ep-4"
media_type: "Video"
author: "Y Combinator"
speakers: ["Diana Hu", "Harj", "Host", "Speaker"]
categories: []
description: "Garry, Diana, Harj, and Jared discuss the strategies to build a foundational AI model with examples of YC companies doing just that. We also get an exclusive look at OpenAI's Sora!"
url: "https://ycombinator.com/library/Kl-building-ai-models-faster-and-cheaper-than-you-think-lightcone-podcast-ep-4"
youtube_id: "fmI_OciHV_8"
youtube_url: "https://www.youtube.com/watch?v=fmI_OciHV_8"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Building AI Models Faster And Cheaper Than You Think  [Lightcone Podcast Ep. 4]

If you read articles about companies like OpenAI and Anthropic training foundation models, it would be natural to assume
that if you don’t have a billion dollars or the resources of a large company, you can’t train your own foundational
models. But the opposite is true.

In this episode of the Lightcone Podcast, we discuss the strategies to build a foundational AI model with examples of YC
companies doing just that. We also get an exclusive look at OpenAI's Sora!

## Transcript

Host: A lot of the sci-fi stuff is actually now becoming possible. What happens when you have a model that's able to simulate real world physics?

Host: Wouldn't it be cool if this podcast were actually an Infinity AI video?

Host: One thing I noticed is that the lip syncing is extremely accurate. Like, it really looks like he's actually speaking Hindi.

Host: How do YC companies build foundation models during the batch with just $500,000? This is literally built by 21-year-old new college grads and they built this thing in two months. I think he like locked himself in his apartment for a month and just read AI papers. You can actually be on the cutting edge in relatively short order, and that's an incredible blessing.

Host: Welcome back to another episode of the Light Cone. Today we're talking about generative AI. First, there was GPT-4, then there was Midjourney for image generation, and now we're making the leap into video.

Harj: We got access to Sora, and we're about to take a look at some clips that they generated just for us.

Host: Yep, should we take a look?

Harj: Okay, so here's the first one. The prompt is: "It's the year 2050, a humanoid robot acting as a household helper walks someone's golden retriever down a pretty tree-lined suburban street." What do we think?

Host: I like how it actually spells out "help." It's like a flex, like "I can spell now."

Harj: Yeah, which was not true with the image models. It always screwed up the text. Image Stable Diffusion, DALL-E, were notoriously bad at spelling text, so that is a major advance that no one's really talked about yet.

Host: I mean, it's wild how high definition it is. Like, that's almost realistic, and the other really cool thing is the physics. The way the robot walks, for the most part, is very accurate. You do notice a little kind of shuffle that's a little bit off, but for the most part is believable. And the way the golden retriever moves—I have a golden retriever, so I can personally vouch that like they perfectly modeled the life.

Harj: Yeah, you have one, right? Like your dog, right?

Host: Yeah, perfect. A perfect representation of how a golden retriever walks. I also like that with DALL-E and Stable Diffusion, as you made your prompts longer and longer, it would just start ignoring it and not actually do exactly what you told it to do. And like, we gave it a very specific prompt here and it did exactly the thing that we told it to. You can see it's not—it's still not exactly perfect. So I think towards the end you see like a floating dog or something in there.

Harj: Okay, I was going to call out a couple of other imperfections here, which is that like the street is not a street, guys. Like, carpet. It's a—

Host: Yeah, and like what's up with that? It's like a weird—it's like not quite a sidewalk, not quite a street.

Harj: Yeah, but in the future we won't need cars anymore. And then like only one side structure is like jumping. There's this floating object thing. Here's a floating object on the right. If you watch carefully, which looks like a little dog or something. I'm not sure. But this is still a real breakthrough. If you look at, you know, some of the stuff that Meta put out—I mean, I always think about what is it Will Smith trying to eat a plate of spaghetti, and that looks insane. Um, and it's sort of just what you would do if you fed the previous frame into the same model to try to generate the next frame, and it just wasn't durable. And that wasn't too long ago.

Host: Yeah, the other thing that I find really impressive about these Sora videos is that they have long-term visual consistency, so it's like a minute long, and like all the houses are similar architectural style. There's no like discontinuity. All the trees look similar. It's clearly all takes place in the same world.

Harj: Next one's a drone camera circles around the Golden Gate Bridge. The view showcases the magnificent cliffs and ocean waves with views of San Francisco in the background. The view is stunning, captured with beautiful photography. That is the Golden Gate. That is the Golden Gate. Knows what the Golden Gate Bridge looks like. And I think you can see Alcatraz there a little bit too.

Host: Yeah, I'm like, the high definition is amazing, and you can see the city in the background as we asked for it. It's definitely not geographically accurate, but yeah, like the terrain is not quite actually the way it is in the real world, but it looks visually kind of similar.

Harj: Yeah, and you can see it's not quite perfect because early on in the clip, if you look at sort of one of the columns of the bridge from a particular angle, it looks disjointed. Like, can you see that one?

Host: Oh, yeah, the back, yeah. And then it sort of lines up when we get to this angle. Also, if you go back to the beginning of the clip and you look at the cars driving on the bridge, they're driving on the wrong side of the road. Like, that one's about to cause a traffic accident.

Harj: Maybe there's some data from the UK?

Host: Maybe, yeah, there is, I guess. The other detail is in computer graphics, it's incredibly difficult to simulate fluid, and it's still a little bit wonky with the waves. They're a little bit static.

Harj: Yeah, I've seen other Sora clips where it captures the motion of water just incredibly. One thing I'm really curious about is just how Sora works under the hood and just how they're generating these videos. So, uh, could you even say a brief primer on just like what's actually going on?

Host: And one thing I was particularly curious about is like, is this a new model? Or is this like an extension of the Transformer model that we all know about as powering ChatGPT?

Harj: I think the TLDR and the really cool thing here is it is really a combination of a Transformer model, which typically has been mostly used for text, and a diffusion model, which has been used—a lot of the tech behind DALL-E, Midjourney—to generate images. So it's combining these two and then adding a temporal component so you can see the consistency between frames over time. And I think the key thing that OpenAI did was to train this with videos and with what they call spacetime patches. So it is like this basically a 3x3 matrix of pixels, so you have the spatial, and then patches of temporal, which is like multiple frames create a video. And the way they do it, they have a variation of the sizes of these patches. They could be size smaller to bigger in XYZ basically, right? And then they basically train all this in this giant architecture, which is really expensive.

Host: So the patches are these spacetime patches the video equivalent of tokens?

Harj: Sort of. Because I think there's a lot of prior work behind Sora. Because the first thing is Transformers have been mostly applied to text, and one of the prior work was Google's work on demonstrating that you could do Transformer models not just for English text but for images. So that was a foundational paper that came back in—I think they published it in 2020, and the paper was called "Image is Worth 16x16." So they call it a visual Transformer. So they demonstrated that you could create and use Transformer models for image recognition tasks because the state of the art up to then was convolutional neural networks, which was very expensive to compute. So that was one piece of the puzzle. The other piece of the puzzle was kind of the spacetime concept, and I think a sum of that comes from stitching some different work on the past. This other paper, "World Models," came out in 2018 that separated—it's for robotics actually—that separates the detection piece, so that's kind of the perception of the visual part, and then the other piece is the memory model for the temporal aspect. And the temporal aspect in the World Models paper uses LSTMs, and then there's a controller model that combines it. So what I mean, they don't explain too much at OpenAI—this is just a bit of me looking at it. I don't know. This is one of the things that OpenAI is a bit coy about it, but we can only speculate. It's a combination of like robotics papers plus Transformer plus text. And then how much more expensive is it to generate one of these videos compared to generating text? Like, how do we even think about that?

Host: Oh man, so imagine GPT-4 is like a trillion parameters, and imagine that's only two dimensions, right? Text is just the matrix of two by two. Now this is like an order of magnitude. So I can imagine it's like at least one order magnitude—10 trillion. Okay, that's amazing. Probably 10 times the amount of GPUs. I can only imagine. I think it was about 20, 30,000. I forget exactly the number of GPUs that took for GPT-4. Okay, what's crazy is that we have companies within Y Combinator that have also been able to achieve similar types of functionality, and they clearly have way less resources than OpenAI does. And so I'm curious how they manage to do that. And the way I kind of think about this is that there's the components of building one of these like foundational models like data, compute, and expertise. Should we talk through some of the YC companies and how they've managed to like hack each or all of those things basically? How do YC companies build foundation models during the batch with just $500,000?

Harj: Yeah, I think it's an important topic because I think because people know how much money OpenAI is spending on GPUs, there's this meme going around that in order to do this you need to like have raised like billions of dollars and have like a data center full of GPUs. And we've actually seen that is not true. There's actually a bunch of companies in the current batch, Winter '24, right now that just in the time of the batch with just the $500k that YC gives them have actually built really awesome foundational models that are producing like magical results. Should we look at some of these demos and see and talk about how they managed to get this to work?

Host: Yeah, let's start with Infinity AI. Infinity AI is coming in the current batch, and what they do is they make deepfake videos of a particular person. So for example, they have an AI replica of Elon Musk, and you can just tell Infinity AI what you want Elon Musk to say, and they will produce a video of Elon Musk saying exactly that thing. Watch a demo.

Harj: Yeah, let's see a demo. Let's watch the demo. Speaking of YC companies training their own models, did you guys see the Infinity AI demo last week?

Speaker: Yeah, they're a company in my group. Infinity allows people to make videos by just typing out a script.

Harj: Wouldn't it be cool if this podcast were actually an Infinity AI video?

Speaker: That'd be super cool. You think they'd be up for that?

Harj: Well, guys, I have a surprise for you. Here we are.

Speaker: That was pretty good. So special thanks to the Infinity AI team who made a model for the Light Cone podcast. And the way that they did this is they literally just downloaded our YouTube videos from the first three episodes and they trained their model on that. And the cool thing about these models now is like you don't need that much data once you've trained the foundation model. To adapt it, to learn a new person, so just the like hour or so of YouTube video that we had was enough for them to get a really accurate representation.

Host: I could talk about another company. So I'll explain what Synlab is. Synlab is an API for creating real-time lip syncing. And the crazy thing about this team is that they trained the models on a single A100 and is generating these clips of results. So let's take a look at it. I'm guessing this guy doesn't actually speak Hindi.

Speaker: No, no.

Host: Okay, okay. One thing I noticed is that the lip syncing is extremely accurate. Like, it really looks like he's actually speaking Hindi.

Harj: Yeah, and if we put it in this framework that you were mentioning with how YC companies do this, there's different vectors: computation, dataset, and speed. So they kind of hacked all of those. So for the dataset, the clever thing they've done is unheard of—chaining a video model, video audio model with so little resources. They compress a lot of the data and low-res video, so you don't need the high-res video because if you have a high-res of 1080p versus let's say the 240p version, that's like a factor quadratic factor less because it's two dimensions, right? So they've done that. The other thing that enabled them to really move a lot faster is the deal that we did with Azure, where we have a dedicated GPU cluster for companies in the batch. They've been able to iterate 100 times faster than they were before in the batch. So a lot of companies out there, they decide they need to do fine-tuning, they need access to GPUs, and they just can't get it. Or you've got to pay an arm and a leg and prepay for a year in advance, and maybe you'll get it in 2025. But if you're in the YC batch, turns out you can get them.

Host: Yeah, you get over half a million in credits, and there's no contention for resources. You actually get instant access within 24 hours for a GPU cluster, which is pretty cool. Because YC invests half a million dollars—but I think all the companies in the YC batch to train these models, I think they literally didn't have to touch the YC money to train the models. Like, that was all extra free money, like unrelated—unrelated to the YC investment.

Harj: Should we talk about Sonado? So Sonado is another company in the Winter '24 batch, um, and they have built a text-to-song model. So you can give their model lyrics to a song and tell it who you want to perform the song. Like, you can tell it "I want Taylor Swift to sing a birthday song for my dog," and it will make exactly that song. There's only like two or three models in the world that have ever been trained that actually do this, and I think Sonado is actually the best one.

Host: Oh wow, um, and the really cool thing is that the founders of Sonado are literally like 21 years old. So, Harj, to your point about expertise, this was not built by like PhD machine learning researchers who have been working in machine learning for like 10 years or something. This is literally built by 21-year-old new college grads, and they built this thing in months. And they did it basically—they just taught themselves. Just like went online and they figured out how to do it. That is very impressive. Should we take a look at it?

Harj: Yeah, so this is a song that they made for the YC batch, and it's like a power march about Y Combinator.

Speaker (singing): Fine in the heart of the valley where futures are made, founders...

Host: Is this how we're going to open the batch from now on?

Harj: That's a good idea. We need big orange banners behind us, and we have to wear um, military garb though with orange armory.

Host: Gary, we could do our own song for Demo Day AI generated.

Harj: I think we have to now.

Host: You have to. This is very impressive. One thing I really like about this is like you can actually understand the lyrics. Like, we really does do the lyrics, but it really does sound like someone is singing it. This is the first time I've heard AI vocals like that.

Harj: Yeah, and to your point of Jared, there's another company that also didn't have the expertise of PhDs of machine learning. It is called Metalware. They're building a co-pilot for hardware. And these were founders who used to work as hardware engineers at SpaceX and they had to build all these hardware designs. So they're very familiar with building hardware. And when they came into the batch, they decided to build basically a co-pilot for hardware design. And they didn't have much AI background, and they figured it out. And one of the cool things about them is they also trained a foundation model for this because there's no model available for this. And they were able to do it during the batch. And in that same framework of the things that they hacked with data and computation, in terms of the data, they got away with—

Harj: using less data but more high quality. What they did is they took a bunch of figures and information from textbooks on hardware and they scanned all of that and added that as input, which is clever, right? The other problem, the other thing—because they didn't need as much data—then they could choose to work with a model that's less computationally intensive. So they actually use GPT 2.5, which seems counterintuitive because the 2.5 GPT only has like one billion plus parameters. I think it's one billion, right?

Host: Yeah, versus GPT-4 is like a trillion.

Harj: And they were able to get away with using less computational resources because they use a smaller model and better data. And then they could do all these hardware design copilot tasks, which is really cool. So when you kind of constrain a lot of your tasks and you're very specific and the data set is very high quality, that's another way you could hack and build a foundation model during the batch and therefore all different kinds of applications—not just generating video text. There's one that I'm really excited in the current batch called Guab. They're building an explainable foundation model because one of the things with all these foundation models and deep learning is kind of this black box magic. Nobody knows what's going on. You put in the data, it kind of predicts the label, and you have no idea how that happened. Prior to deep learning, you could, because you could have the weights and understand which feature indicated and gave the weight for the label. So this team is building a foundation model that can explain the outputs. And they trained a model doing the batch. Nice.

Host: As a founder, like when is it the right call to invest in building your own model versus just using one of these open source models and fine-tuning and tweaking it to fit what you need?

Harj: Well, I guess it depends, right? Depends on what you're really looking to build. If you're in a very specific and it can be niche space, you can get away with training your own foundation model, like the metal ware guys. But if you're, let's say, doing something more with language, GPT-4 gets you quite far along. So it depends on the task too, right?

Host: So if we're thinking about it as like the DIA computer expertise, like we're basically saying expertise is maybe overrated? Like we're proving that if you're just like smart and willing to read the papers, you can figure it out. Compute there are ways—like being in YC is one way to get around that. Like you can get credits and you can take some of that cost off. And so then is it like the data piece is sort of where all the edge is? Like if you can find high quality—I say like high quality, but not like giant data sets—that's the hack?

Harj: Oh, yes. Let's talk about—uh, find. So find is this company that's building a co-pilot for software. The answers that they're generating are even better than Stack Overflow. Interesting. And these were also kids out of college with not a lot of like a background. And they done a very clever hack to build their own model for the data. They created a bunch of synthetic data for programming competitions. So they would have a bunch of those data sets generated, and that got like a lot higher quality. Imagine that—it's like basically infinite if it's synthetic. It's interesting 'cause I feel like synthetic data has been looked down on.

Host: It was controversial, yeah. Initially, yeah. Why? Like why was it originally controversial, and why does it actually seem to be working?

Harj: It seemed like circular. It seemed like it would be impossible for a model to generate its own data. And how like how can you learn from the data that you generated?

Host: Yeah.

Harj: It wasn't obvious that such a thing could be possible. It seemed like it would violate some like conservation of energy. I remember the meme that was going around on Twitter was like the mosquito drinking its own blood, and like this is how synthetic data works.

Host: Yeah. Um, but then it turns out it actually works. Interesting. I think maybe this is related to the idea that, you know, some of these LLMs are actually capable of reasoning. And once you can reason, maybe that's the part that sort of spins up the flywheel and makes it possible. And you know, there are other interesting analogues that I think there's a healthy debate out there whether or not this will come together. But you could look at self-driving car models are often trained on massive amounts of simulation data instead of actually real drive time, you know, sometimes by a factor of 10 to one or more. And that might end up being true for some of the generative AI models too. Is it possible Sora will do that as well? Like Sora generate its own video to continue improving its own model?

Harj: Probably. I know OpenAI doesn't share much about their data sources because that's part of the secret sauce, but 100% they're using video footage that's generated from Unreal Engine, probably, or Unity—one of these game engines—because they have a full physics simulator. So you could create multiple scenes of the same, uh, let's say if you have the example of the car driving on the cliff, they could generate it from all multiple camera angles because what that game engine does—you can position the camera anywhere. And you could basically generate all the footage on all possible camera views. The physics part of this is really interesting. I—you know, most people when they see these Sora demos or just generally get this concept, your mind goes to, "Oh, this will be cool for generating films or video games, like entertainment." But if what you're saying is it can actually like simulate the real world, there's probably going to be lots of far reaching implications for that. Like what are some of like, what happened in America? And so like, no commercial company has been able to create their own version because it's too expensive to do it the old school physics-based way. And so what's really cool about AtMo is instead of using the old school physics way, they've trained a foundational model. And using machine learning, it's like a million times more efficient to run the same calculation or something like that. And because of that, this startup, which is only raised a seed round, is actually able to make a weather prediction model that is more accurate than the NOAA-funded one that cost over a billion dollars. Interesting. What's really surprising about the text-to-video is like just how far-reaching like the implications are. So you can go way beyond just generating like video games. Like we can do weather. Like what are other examples of cool things that we could do if we can generate like have a physics simulation of the real world?

Host: Well, there's a bunch of companies that are applying it to biology. Diana, do you want to talk about a couple of those?

Diana Hu: Yeah, so it turns out all these foundation models are great function approximators for anything. So function—they're general purpose learning algorithms. And the human body can be simulated with functions too. So one of the companies that we funded as well is called The Use Bio. They're building generative AI for proteins. So what they're doing is building these big models to be able to create new molecules for new types of drugs and new kinds of gene therapies. And in order to hack this aspect of how do they make progress with not as much resources, they had a lot of expertise. This is different than the set of founders we talked about that don't come from the background. Namada, the founder, she has published some very legit papers in Nature before this. She had a lot of expertise in terms of how to short-circuit the computation loop. What she did is build custom kernels on the models so that the whole process of building the foundation models is a lot faster with less resources. So on the other company in the current batch is a Pyramidal. Do you want to talk about them? They're building a foundation model for the human brain, which turns out they're predicting EEG signal, which could be used for all sorts of applications from predicting stroke to reading. At some point, they could—your brain could be read, perhaps. And what EEG signals are? They're also Pearl. So sort of like Sora—Sora has like images plus images over a time stamp, so that's video. So EEG is the same thing. It's just electrical impulse, but over a time period. So they kind of do something similar with chunking space-time chunk, but for EEG. So they're able to train this model. And the way they were able to train and iterate during the batch, they were experts in the space. So they also did a lot of hacks around the computation where they found a way to divide a lot of the sequential data into chunks, sort of like what Sora has done. And that actually reduced the runtime complexity by quadratic, which is like impressive. And they could get a single run of an iteration of an initial model with just 800 hours of compute GPU compute, which is really cool.

Host: One thing that's really cool about that is like if people sat down and tried to think of different applications for foundational models, EEG would not be the one that would like immediately come to mind. And to me, that suggests that there's probably a lot of other application areas like EEG data that just people haven't thought of yet.

Diana Hu: Yeah, it's like who would have thought that EEG is sort of like videos? It's just this whole concept with space-time. You space-time lots of things. It's also possible that applications of AI that people thought would exist will now exist. Like robotics, I think, is a good one. A huge one.

Host: You remember, I think we talked about this in a previous episode about how when Sam was starting OpenAI, he talked about they originally thought that, you know, AI in robots and AI in the real world would be like the first application. And I remember I went over to the OpenAI office in like the first year or two, and they had all these robots trying to like learn how to solve the Rubik's Cube by like reinforcement learning. Y, which is also kind of an interesting side note because like OpenAI is so wildly successful right now that it's easy to think that they knew that like they had this like straight-line path to get there. But it was definitely not that. It was like a meandering path. They pursued a bunch of dead-end ideas, like the reinforcement learning robots that didn't work well. Even the researcher working on Transformer architecture at OpenAI was like off in the corner, I think, at the start. Like it wasn't clear even within OpenAI that that was going to be the thing—the right thread to pull on, right? But so like the Sora and just like text-to-videos, pretty interesting because again, if we have a real physics simulator for the world, like that potentially getting plugged into robots is like a breakthrough to make the sort of the AI robot a reality.

Diana Hu: We actually have a company in the current YC batch, K Scale Labs, that's working on consumer humanoid robots. Um, yeah, yeah, and they have like pretty cool demos. Very early, but like a lot of the sci-fi stuff is actually now becoming possible. The cool thing about Ben, who is the founder for K Scale, he was the guy that built the foundation robotics model for Tesla.

Host: Y? Oh, cool. He put it into the Optimus Prime robot as well?

Diana Hu: Oh, awesome. The about the real world is governed by the laws of physics. And it turns out we have a bunch of equations that can describe it for different things. Like weather, there's also the space. Um, for example, there's this company that we funded called Draft A that is building AI models for CAD design. So CAD follows a lot of the laws of physics with Newton, right, with force, shear, etc. And a lot of software behind SolidWorks and AutoCAD run on these really old kernels that basically again solve these giant piles of lots of equations. So that when you do a design of a structure and you want to calculate the force and the tolerances, it's accurate because you don't want a building to just flop, right? So what they—and it's very expensive. I mean, whenever you build all these models in CAD and these kernels are super old, and they kind of at the end of the day they run on these equations that compile. I don't know, to some wild thing like FORTRAN, because they haven't been updated. What Draft A is doing, they are short-circuiting some of these with AI models that can do some of the predictions. So it's a lot faster and cheaper in terms of computation. There's a lot of geometry computational geometry computation behind the scenes that's really cool.

Host: That's a perfect example of just like a valuable problem to solve that the general purpose model is just not going to get around to specializing. That's a great point. And there's a lot of startups that are very worried that if they like go into AI, they're going to get run over by OpenAI or other foundational model companies. And so one solution to that is like train your own model that's doing something else.

Harj: Yeah, a great point. Uh, there's actually a YC company called Playground run by our friend Suel Doshi that is a good example of actually, you probably can go up against people who are really well-funded and come up with something that is far better. What we're looking at here is the newest version of Playground 2.5, and you're they're hot on the heels of Midjourney. But at the same time, like the models that they've actually even released open source go toe-to-toe against stuff, you know, the latest versions of Stable Diffusion, and in a lot of cases way outperform that. And they've done it on far less money than Stability AI and other teams in the space. So I think Suel and Playground are really ones to watch to sort of go toe-to-toe with Midjourney and in the long run potentially beat it. Because I would never bet against Suel Doshi. That guy is a beast. The image quality is super impressive. That is looks so cool. And maybe some of the audience would have thought that Suel comes from an AI background, but he doesn't. Yeah, he started Mixpanel before when he was 19. And Playground is also an interesting example of something that Harj was talking about last night, which is the phenomenon of companies pivoting into AI because Playground actually did not start with this idea. When it started, it was a completely different idea. And a couple of years in, Sue, after raising a bunch of money, Sue hard-pivoted the thing into AI. And he literally just taught himself AI. I think he like locked himself in his apartment for a month and just read AI papers. And then he built Playground. So don't be afraid. I mean, I think that that's one of the most interesting things that we've seen across many of these different examples. That if you're looking for a reason why you can't succeed, guess what, you're right. But on the other hand, the field itself is so new, so brand new, that if you spend six or nine months literally reading every paper and then meeting all the people who are in the space and they'll meet you, um, you can actually be on the cutting edge in relatively short order. And that's an incredible blessing.

Diana Hu: Totally, it's a really important message actually, right? Because we're all grateful to Sam and OpenAI for like bringing this field forward and making all of this stuff possible. But at the same time, all of the news headlines tend to be around the companies that are raising like huge amounts of money or about, you know, like Sam himself, as a world celebrity at this point. But you can actually like compete with OpenAI for very valuable verticals and use cases by training your own model without having to be Sam Altman or having a $100 million.

Host: So we're out of time for today, but we could talk for hours about the crazy things that we're seeing in AI being built by people who are probably not that different than you who's watching right now. Uh, a lot of the world right now is looking at people like Sam Altman and Dario Amodei and some of the luminary figures who have really pushed forward the whole space. But remember, all of these people started someplace. And we hope that...

Host: Y Combinator might actually be the place for you to start, just like it was for Sam Altman back in the day. That's it. Catch you next time.
