---
title: "Dalton & Michael: Things that don't scale, the software edition"
slug: "Ig-dalton-michael-things-that-don-t-scale-the-software-edition"
media_type: "Video"
author: "Dalton Caldwell, Michael Seibel"
speakers: ["Dalton Caldwell", "Michael Seibel"]
categories: ["Product", "Building Product", "Experimentation"]
description: "Dalton Caldwell and Michael Seibel on software hacks that don't scale. Companies discussed include Google, Facebook, Twitch, and imeem. "
url: "https://ycombinator.com/library/Ig-dalton-michael-things-that-don-t-scale-the-software-edition"
youtube_id: "TCPjk8Tpb5c"
youtube_url: "https://www.youtube.com/watch?v=TCPjk8Tpb5c"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Dalton & Michael: Things that don't scale, the software edition

Dalton Caldwell and Michael Seibel on software hacks that don't scale. Companies discussed include Google, Facebook,
Twitch, and imeem.

## Transcript

Dalton Caldwell: We'll get a founder that's like, "Oh, how do I test my product before I launch to make sure it's gonna work?" And I always come back and tell the founders the same thing. Like, if you have a house and it's full of pipes and you know some of the pipes are broken and they're gonna leak, you can spend a lot of time trying to check every pipe, guess whether it's broken or not, and repair it. Or you can turn the water on and like, you'll know. You'll know exactly what work needs to be done.

Michael Seibel: Hey, this is Michael Seibel with Dalton Caldwell. Today we're going to talk about what does it mean to do things that don't scale—the software edition. In this episode, we're going to go through a number of great software and product hacks that software companies used to figure out how to make their product work when perhaps they didn't have time to really build the right thing.

Now, Dalton, probably the master of this, is a person we work with named Paul Buchheit who invented this term, the 90/10 solution. He always says something like, "How can you get 90 percent of the benefit for 10 percent of the work?" This is what he always puts to people when they tell him it's really hard to build something or it takes too long to code it. He'll just always push on this point. And you know, founders don't love it, right? Would you say that's a fair assessment?

Dalton Caldwell: That's a fair assessment. Yes, founders hate it.

Michael Seibel: Tell the audience why it's worth listening to this guy. Like, why does he have the credibility to say that to people?

Dalton Caldwell: Well, PB is the inventor of Gmail. And as kind of a side project at Google, he invented something that 1.5 billion people on Earth actively use. And he literally did it doing things that don't scale. I'll start the story and then please take it over.

Michael Seibel: So as I remember it, PB was pissed about the Gmail product—sorry, the email product he was using. And so Google had this newsletter product, the first version of Gmail. He basically figured out how to put his email into this Google Groups UI. And as he tells the story, his eureka moment was when he could start reading his own email in this UI. And then from that point on, he stopped using his old email client. And what I loved about this is that as he tells the story, every email feature that any human would want to use, he just started building from that point on.

So, you know, he would talk to YC batch and he's like, "And then I wanted to write an email, so I built writing emails." And if you know PB, he could have gone a couple days reading emails without replying at all. So like, he didn't need writing emails to start.

Dalton Caldwell: I remember him telling about the first time he got his coworker—literally his desk mate or something—to try to use it. And his destiny is like, "This thing's pretty good. It loads really fast. It's really great. The only problem is, PB, it has your email in it, and I wanted to have my email."

And PB was like, "Oh, okay. Well, I gotta build that."

Michael Seibel: A forgotten solution. And so then it started spreading throughout Google. Do you remember when it broke?

Dalton Caldwell: No, what happened?

Michael Seibel: Oh, so he told the story where like one day PB came in late to work—which, you know, knowing PB, every day—and everyone was looking at him really weird. They're all like a little pissed. They got to his desk and someone came over to him was like, "Don't you realize that Gmail's been down like all morning? People was like, no, I just got to work. I didn't know."

And so he's like trying to fix it, trying to fix it. And then his coworkers see him like grab a screwdriver and go to the server room. It was like they were like, "Oh god, why don't we trust PB with our email? Like, we're totally screwed."

And I think he figured out like there was a corrupted hard drive. And I remember at that point of the story, he was like, "And that day I learned that people really think email's important and it's gotta always work."

Dalton Caldwell: Yeah. Yeah. I think the reason he did it, man, is because he liked to run Linux on the desktop and he didn't want to run Outlook. Like, the Google suits were trying to get him to run Outlook on Windows, and he was like, "I don't really want Windows." But yeah, it was the dirtiest hack.

Michael Seibel: And as I recall in this, you know, final part of the story, it was hard for him to get Google to release it because they were afraid it was going to take up too much hardware. So there was all these—there was all these issues where there's a good—there was a decent chance, I think, it never would have been released.

Dalton Caldwell: Well, this part was that everyone thought Gmail's like invite system was like some cool growth hacking virality hack. Yeah, like virality hack. It's like, "Oh, you got access to Gmail? You got, I think, four invites to give to someone else," and these are like precious commodities. And it was just another product. It was just another version of things that don't scale. They didn't have enough server space, so they had to build an invite system.

Michael Seibel: Yes. There was not an option to not do it. But basically there was no option other than building an invite system. It was not like genius PM growth hacking. It was like, "Yeah, well, we saturated the hard drives. They're full, so I guess we can't invite anyone else in Gmail today." That's it.

Dalton Caldwell: That's it.

Michael Seibel: So you had another story about Facebook in the early days that is similar in this light.

Dalton Caldwell: So let me paint the picture. Back when you started a startup a long time ago, you had to buy servers and put them in a data center, which is a special room that's air-conditioned that just has other servers in it. And you plug them in and they have fast internet access. So being a startup founder, until AWS took off, part of the job was to drive to the suburbs or whatever, drive to some data center—which is an anonymous warehouse building somewhere—go in there and like plug things in.

Michael Seibel: And what was funny is when your site crashed, it wasn't just depressing that your site crashed. It actually meant getting in your car. Like, part of being a startup founder was waking up at 2 AM and getting in your car and driving to like Santa Clara because your code wedged. You have to physically reboot the server, and your site was down until you physically rebooted the server.

Dalton Caldwell: So I'm just trying to set the stage for people. This was what our life was like, okay? And so my company, I Meme, we had a data center in Santa Clara, and there was a bunch of other startups there as well. And so something that I like to do was to look at who my neighbors were, so to speak. There were never people there. It was just their servers. And there'd be a label at the top of the rack, and you could see their servers and you can see the lights blinking on the switch. Okay, so this is what I was like.

And so our company was in the data center in Santa Clara, and then one day there's a new tenant—oh, a new neighbor. So I look at it, and the label at the top of the cage next to ours, you know, three feet away, the label said "the [Facebook.com](http://Facebook.com)." And I remember being like, "Oh, yeah, I've heard of this. Like cool, like sounds good."

Michael Seibel: And they had these super janky servers. I think there was maybe eight of them when they first moved in. And they were like super cheap. They're like Super Micro servers, you know? Like the wires were hanging out. Like, did you know? I'm like, "Cool." But the lights were blinking really fast, okay?

Dalton Caldwell: And so what I remember was that there were labels on every server, and the labels were the name of a university. So at the time, one of them—one of the servers was named Stanford. One of them was named Harvard, you know? Like, and it made sense because I was familiar with the Facebook product at the time, which was like a college social network that was at like eight colleges, okay?

So then I watched. Every time we would go back to the data center, they would have more servers in the rack with more colleges. And it became increasingly obvious to me that the way they scaled Facebook was to have a completely separate PHP instance running for every school. They copy-pasted the code to them. They would have a separate MySQL server for every school, and they would have like a Memcache instance for every school. So you'd see like the University of Oklahoma. You know, you'd see the three servers next to each other.

And the way that they managed to scale Facebook was to just keep buying these crappy servers. They would launch each school, and it would only talk to a single school database. And they never had to worry about scaling a database across all the schools at once because, again, at the time, hardware was bad. MySQL was bad. Like, the technology was not great. If they had to scale a single database, a single user's table to hundreds of millions of people would have been impossible. And so their hack was the 90/10 solution, like PB used for Gmail, which is like, "Just don't do it."

So at the time, if you were like a Harvard student and you wanted to log in, the URL was hardcoded to [Harvard.thefacebook.com](http://Harvard.thefacebook.com), right? And then if you try to go to [Stanford.facebook.com](http://Stanford.facebook.com), it'd be like, you know, error. Like, that was just a separate database.

Michael Seibel: And so then they wrote code so you could bounce between schools. And it actually took them years to build a global user's table, as I recall, and avoid this hack. And so anyway, the thing they didn't scale is they copy and pasted their code a lot and had completely separate database instances and then talk to each other. And I'm sure people that work at Facebook today, I bet a lot of people don't even know the story, but like, that's what it took. That's the real story behind how you start something big like that versus what it looks like today.

Dalton Caldwell: So in the case of Twitch, all, if not all, like most of the examples of this came from this core problem. And it's why I tell people to not create a live video site. A normal website, even a video site on a normal day, will basically have peaks and troughs of traffic, and the largest peaks will be two to four times the steady state traffic. So you can engineer your whole product such that if we can support two to four times steady state traffic, and our site doesn't go down, we're good.

On a live video product, our peaks were 20x. Now, you can't even really test 20x peaks. You just experience them and fix what happens when 20x more people than normally show up on your website because some pop star is streaming something.

Michael Seibel: And so two things kind of happened that were really fun about this. So the first hack we had was if suddenly some famous person was streaming on their channel, there'd be a bunch of dynamic things that could load like your username would load up on the page, or our channel, and the view count would load up, and a whole bunch of other things that would basically hit our application servers and destroy them if a hundred thousand people were trying to request the page at the same time.

So we actually had a button that could make any page on Justin TV a static page. All those features would stop working. Your name wouldn't appear. The view count wouldn't update. Like, literally a static page that loaded our video player. And you couldn't touch us. We could just cache that static page as many people as possible want to look at it.

Now, to them, certain things might not work right, but they were watching the video. The chat worked because that was a different system. The video worked. That was a different system. And we didn't have to figure out the harder problems until later. Later, actually, Kyle and Emmett worked together to figure out how to cache parts of the page, make other parts of the page dynamic. But that happened way, way later.

Dalton Caldwell: Dude, let me give you a quick anecdote. Yes. Remember Friendster before MySpace?

Michael Seibel: Yeah, of course.

Dalton Caldwell: Every time you would log in, it would calculate how many people were two degrees of separation from you. And it would fire off on MySQL thread. You would log in. It would look at your friends and it would calculate your friends and friends and show you a live number of how big your extended network was. And the founders, you know, John Abrams, he thought this was like a really important feature. I remember talking about it. Guess what? MySpace is a do-things-that-don't-scale solution. I mean, if they were in your friends list, you would say, "This person is in your friends." You know, so-and-so is in your friends list. And if it wasn't, it'd say, "So-and-so is in your extended network." There it is. That was it. That was the feature.

Michael Seibel: And so Friendster was like trying to hire engineers and scale MySQL, and they ran into like too many threads on Linux issues and like updating the kernels. And MySpace was like, "So-and-so is your extended network. That's our solution." Anyway, carry on. But that's the same deal.

Dalton Caldwell: So our second one was if you imagine if someone is really popular and there's a hundred thousand people want to watch their stream, we actually need multiple video servers to serve all of those viewers. So we basically propagate the original stream coming from the person streaming across multiple video servers until there is enough video servers to serve all the people who are viewing.

The challenge is that we never had a good way of figuring out how many video servers we should propagate the stream to. And if a stream would slowly grow in traffic over time, we had a little algorithm that could work and like spin up more video servers and be fine. But what actually happened was that a major celebrity would announce they were going on, and all their fans would descend on that page. So the second they started streaming, a hundred thousand people would be requesting the live stream. Bam. Video server dies.

Michael Seibel: And so we were trying to figure out solutions and solutions and like, "How do we, how do we model this? How do we like?" There were all kinds of like overly complicated solutions we came up with. And then once again, Colin and Emma got together and they said, "Well, the video system doesn't know how many people are sitting on the website before the video stream before it starts trying to start video. But the website does. All the website has to do is communicate that information to the video system, and then it could pre-populate the stream to as many video servers as they would need to, and then turn the stream onto users."

So what happened now in this setup is that some celebrity would start streaming. They would think they were live. No one was seeing their stream while we were propagating their stream to all the video servers that are needed. And then suddenly the stream would appear for everyone and would look like it worked well. And like, the delay was a couple seconds. It wasn't that bad, right? But like, dirty, super dirty, but it worked.

Dalton Caldwell: And honestly, that's going to be kind of the theme of this whole setup, right? Super dirty, but it worked.

Michael Seibel: You had a couple of these at IME, right?

Dalton Caldwell: Yeah, there was a couple that we had at I Mean. So one of them—so at the time, again, like to set the stage, the innovation of showing video in a browser without launching RealPlayer—no one here probably knows what that is, but it used to be that to launch a video, it would launch another application in the browser that sucked. And it would like crash your browser, and you hated your life, okay? So one of the cool innovations that YouTube the startup YouTube had before it was acquired by Google was...

Michael Seibel: To play video in Flash in the browser that required no external dependencies or just play right in the browser at the time that was like awesome. Like, it was a major product innovation to do that. Yeah, and so we wanted to do that for music. At I mean, and we were looking at the tools available to do it and we saw all this great tooling to do it for video. And so rather than rolling our own tools that was music specific, we just took all of the open source video stuff and hacked the other video code that we had so that every music file played on—I mean, was actually a video file. It's a dot flv back in the day and it was actually a Flash video player. Um, and the entire—it was basically—we were playing video files that had like a zero bit in the video field and it was just audio. And we actually were transcoding uploads into video files. You know I'm saying? Like, the whole entire thing was a video site with no video. I don't know how to explain it. Um, and it works. And I do think this is a recurring theme: a lot of the best product decisions are ones made kind of fast and kind of under duress. I don't know what that means, but it's like when it's like eight p.m. in the office and the site's down, you tend to come up with good decisions on this stuff.

So we had two more at Twitch that were really funny. Um, the first one talking about duress was our free peering hack. So streaming live video is really expensive. Back then it was really expensive, and we were very bad fundraisers. That was mostly my fault. And so we were always in the situation where we didn't have enough money to stream as much video. And we had this global audience of people who want to watch content. And so we actually hired one of the network ops guys from YouTube who had figured out how to kind of scale a lot of YouTube's early usage. And he taught us that you could have free peering relationships with different ISPs around the world. And so that you wouldn't have to pay a middleman to send video to folks in Sweden. You can connect to yourself, your servers. You—I forgot what they're doing—it saves you money and it saves them money. That's what they wanted.

Yeah, and there were these massive like switches where you could basically like run some wires to the switch and bam, you can connect to the Swedish ISP now. The problem is that some ISPs wanted to do this free peering relationship where basically you can send them traffic for free, they can send you traffic for free. Others didn't. They didn't want to do that, or like they weren't kind of with it. And so I think it was Sweden, but I don't remember. Some ISP was basically not allowing us to do free peering. And we were spending so much money sending video to this country and we're generating no revenue from it. It's like we couldn't make a dollar on advertising. And so what we did is that after ten minutes of people watching free live video, we just put up a big thing that blocked the video that said, "Your ISP is not doing a free peering relationship with us, so we can no longer serve you video. If you'd like to call to complain, here's a phone number and email address." And that worked.

Dalton Caldwell: How fast did it take for that to work?

Michael Seibel: I don't remember how fast. I just remember it worked. And I remember thinking to myself, "It's almost unbelievable that that ISP was a real company. Like, we were like a website in San Francisco. Um, and hey, that worked."

And then the second one was translation. So we had this global audience and we would like call these translation companies and we'd ask them like, "How much would it cost to translate our site into these like forty different languages?" And they were like, "Infinite money." And we're like, "We don't have infinite money."

And so I think we stole the solution from Reddit. We were like, "What happens if we just build a little website where our community translates everything?" And so basically it would just like serve up every string in English and it was like served to anyone who came to the site who wasn't from an English-speaking country and was like, "Do you want to volunteer to translate the string in your local language?" And of course, you know, people are like, "Well, what if they do a bad job translation?" I was like, "Well, the alternative is it's not in their language at all. So let's not make the perfect the enemy of the good."

And I think we had something where like we would get three different people to translate and they would match, but like that happened later. We basically got translation for a whole product for free.

Um, maybe to end because I think this might be like the funniest of them all, tell the Google story. Because I think this one's like really—so, so look, for the Facebook story that was firsthand where I personally witnessed the servers with my own eyes, so I'm 100 percent confident that is what happened because it was me, right? This Google story is secondhand. And so I may get some of the details wrong. I apologize in advance. But I'll tell you, this was related to me by someone that was there. All right, you ready?

So look, the original Google algorithm was based on a paper that they wrote which you can go read—Page Rank. Um, it worked really well. It was a different way to do search, okay? It worked. They always didn't have enough hardware to scale it because remember, there was no cloud back then. You had to run your own servers. And so as the internet grew, it was harder and harder to scale Google. You still with me? Like, there were just more web pages on the internet. So it worked great when the web was small, but then they kept having more web pages really fast. And so Google had to run as fast as they could to just stay in the same place. Just to run a crawl and re-index the web was like a lot of work. And so the way the work of the time is they weren't re-indexing the web in real time constantly. They had to do it in one big batch process back in the day, okay?

And so there was some critical point—this was probably in the 2001 era. Again, this is secondhand. I don't know exactly what it was. But there was some critical point where this big batch process to index the web started failing. And it would—it would take three weeks to run the batch process. It was like the you know, reindex\_web.sh, you know, it was like one script that was like, you know, and it started failing. And so they tried to fix the bug and they restarted it and then it failed again.

And so the story that I heard is that there was some point where for maybe three months, maybe four months—I don't remember the exact details—there was no new index of Google. They had stale results. So any user of Google, they didn't know that, you know, the users didn't know this, but a user of Google was seeing stale results and no new websites were in the index for quite some time, okay?

And so obviously they were freaking out inside of Google. Um, and this was the genesis for them to create MapReduce, which they wrote a paper about, which was a way to parallelize and break into pieces all the little bits of crawling and re-indexing the web. And, um, you know, Hadoop was created off of MapReduce. There's a bunch of different software used, and I would argue every big internet company now uses the descendants of this particular piece of software. And then it was created under duress when Google secretly was completely broken for an extended period of time because the web grew too fast.

But I think this is the most fun part about this story. When the index started getting stale, did Google shut down the search engine?

Dalton Caldwell: Did you like that? That's the coolest part. Like, people just didn't realize they didn't know.

Michael Seibel: And did they build this first again? In terms of "do things they don't scale," did they build MapReduce before they had any users?

Dalton Caldwell: No, like they basically made it this far by just building a monolithic product. And they only dealt with this issue when they had to.

Michael Seibel: You know, I think this is like such a common thing that comes up when we give startup advice. You know, we'll get a founder that's like, "Oh, how do I like test my product before I launch to make sure it's going to work?" And I always come back and tell the founders the same thing. Like, if you have a house and it's got full of pipes and you know some of the pipes are broken and they're going to leak, you can spend a lot of time trying to check every pipe, guess whether it's broken or not, and repair it. Or you can turn the water on and like, you'll know. Like, you'll know exactly the work to be done when you turn the water on. I think people are always surprised that that's basically all startups do: just turn the water on, fix what's broken, rinse and repeat. And like, that's how big companies get built.

Dalton Caldwell: It's never taught that way, though, right? It's always taught like, "Oh, somebody had a plan and they wrote it all down." And it's like, never, never.

Michael Seibel: And you earned the privilege to work on scalable things by making something people want first. You know what I think about sometimes with Apple is picture like Wozniak hand soldering the original Apple computer. And like, those techniques compared to like whoever it is works in Apple to design the AirPods. Like, it's the same company, but like, Wozniak hand soldering is not scalable. But you know, they earned because that worked. They earned the privilege to be able to make AirPods now. And because Google search was so good, they earned the privilege to be able to create super scalable stuff like MapReduce and all these other awesome internal tools they built, right?

Dalton Caldwell: Yes. But if they wouldn't put that stuff first, it wouldn't be Google, man.

Michael Seibel: And so to wrap up, kind of what I love about things that don't scale is that it works in the real world, right? The Airbnb founders taking photos, the DoorDash folks doing deliveries. It also works in the software world, right? Like, don't make the perfect the enemy of the good. Just try to figure out any kind of way to give somebody something that they really want, and then solve all the problems that happen afterwards. And you're doing way better. All right, thanks so much for watching the video.
