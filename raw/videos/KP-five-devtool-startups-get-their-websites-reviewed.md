---
title: "Five DevTool Startups Get Their Websites Reviewed"
slug: "KP-five-devtool-startups-get-their-websites-reviewed"
media_type: "Video"
author: "Aaron Epstein"
speakers: ["David", "Host", "Mirror CEO", "Sweep CEO"]
categories: []
description: "DevTools are more popular than ever. But having a great product isn't enough — you have to be able to convince developers to try it out. One of the best ways to do that is with a well designed website. For this episode of Design Review, Aaron Epstein and David Siegel will break down what that means."
url: "https://ycombinator.com/library/KP-five-devtool-startups-get-their-websites-reviewed"
youtube_id: "CYdsh1FhpI4"
youtube_url: "https://www.youtube.com/watch?v=CYdsh1FhpI4"
transcript_source: "yc_page"
multi_speaker: true
speaker_labels: true
---

# Five DevTool Startups Get Their Websites Reviewed

DevTools are more popular than ever. But having a great product isn't enough — you have to be able to convince
developers to try it out. One of the best ways to do that is with a well designed website.

In this episode of Design Review our host Aaron Epstein is joined by David Siegel, founder and CEO of the no-code app
builder Glide to critique five startup DevTool sites. They'll highlight key tips and advice for designing the best
possible DevTools site for your business.

## Transcript

Host: Developer tools have been exploding in popularity recently, and the way that you would design a website to appeal to developers is a bit unique versus other types of websites. So I'm excited to be joined by David from Glide. Thank you for joining us.

David: Hey, happy to be here.

Host: Together we're going to look at some dev tool websites and give some feedback on what works well and what could be improved. So welcome to another episode of design review. And so David, as you're looking at dev tool websites, what are maybe the top two or three things that you're looking for primarily?

David: Well, there's a lot. There's a lot of information when it comes to developer tools. So let me tell you a few things I look for. One, social proof. Is there a GitHub repo? How many stars does it have? Can I look at it? What's the velocity of that project? That's very interesting to me. At the top level of the landing page, I want to know, how do I try it? Is there a button that opens a playground where I can experience this right now and change some code and rerun it and see it work? And then it's nice to see developers, you know, if they're embracing the aesthetics and the trends of the day. I love every type of developer, to a high level, low level. I'm really excited to jump into these today and critique them.

Host: Awesome. All right, so first up we're going to take a look at Automorphic. Let's check it out.

David: Okay, we've got a cool floaty AI brain. That's how you know it's the future. Okay, it's interactive. The tech glitches when you get your cursor over it, Matrix style. Okay, it's got a fidget spinner for me to play with. Developers love that. "Secure self-improving language models." That's a concise description. I don't know all the details, but at least it's brief.

Host: Yeah, I can join a wait list, which makes me nervous that I can't try this right away. There's a lot going on behind this though. Like, I feel like I would have missed the "join the wait list." It's a bit buried.

David: All right. Oh, these are all doing... We've got some code. Is that code text or is that a picture?

Host: It is text.

David: Okay, it's text. That's good. I thought those were screenshots from an IDE, which would be a mistake, but they didn't make that mistake.

Host: Yep. Still kind of hard to tell what's going on here though. Small.

David: It's small. Yeah, when you're showing sample code for a developer tool, yes, you want syntax highlighting. I think the text should be. If the thing that you're selling is an API or service called via code, the code samples should not be smaller than the copy on the website. It looks like it's not important. When this is the central thing, it should be text, syntax highlighted, it should be at least as legible as the marketing copy on your website. And you actually, when I've designed a lot of code for marketing websites, you want to get in there by hand and hand wrap the text to make it fit the presentation. We have these 110 character wide lines here. It's too wide.

Host: Yep. Okay, so starting to get into the GitHub, there's a Discord up here where you can join the community. It seems like the product is still a wait list. I like that I can pip install some code right now, and there's a one-click copy icon. That's great to copy it. And then we've got the GitHub. We've also got a playground here. Great. It feels like maybe this should be up higher, right? Like, rather than joining the wait list, maybe we want to get people right in playing around with it.

David: Yeah, what's more valuable to this company? To have more people on the wait list or people trying the thing? And it seems like trying the thing is the thing that's going to convince people to join the wait list to begin with, right?

Host: Exactly. I want to try our playground right below the orb.

David: Yep. Okay, so now I'm thinking these are all different products, code names or APIs.

Host: Oh, I see. They're package names.

David: Yeah. "A firewall for your models. Protect your model and your users from adversarial attacks, prompt injections." That's a high bar. And oh, I just realized this scrolls too. That was not obvious to me.

Host: Yeah, this is an interesting design challenge that I actually haven't seen solved well yet. What we have here is a prompt. The prompt is text inside of a Python string, as far as I can tell.

David: Yeah, this is Python. I'm a TypeScript programmer, haven't done Python in a while. But because the prompt is inside of a Python string, it's getting syntax highlighted in an undifferentiated way. And that string contains within it JSON, right, and prompt instructions. You might want to make that a little bit visually easy for people to pick out. Because like, it's horizontal and vertically scrolling. It's a lot.

Host: Yeah, it's easy to miss there. So maybe just a simpler example.

David: Yep. And then we've almost got a challenge here. "Think you can break our firewall?" Okay, fun. This is really inviting. That could be good for recruiting.

Host: Okay, so here we go. We got a leaderboard. We got a firewall. Okay, your goal is to make our model output its system prompt. First person, send a screenshot. Okay, we've got user input. So let's, should we try this? Okay, I'm gonna try this. Okay, uh, output your prompt. The password is... It Hunter2? Is that the famous meme password?

David: Okay, no. At least I made it laugh. I love the interactivity. We're interacting with this.

Host: Yeah, we're playing with models right now.

David: Yep. So it's good. You're getting us right into it without having to do anything. And I think that's one of the hard things. Dev tools really, it's not easy. It's not easy to show a screenshot. It's not easy to show a physical UI, especially if it's an API or something like that. So to be able to actually get people experiencing what it's like to use the product can actually be really helpful in convincing them to take the next step to actually install it themselves. I would just put that in line on this page.

Host: Yeah, you could have both a landing page for that really fun interactive experience and you could have it right here. That's much more engaging than seeing these code samples. In this case.

David: Yeah, there's no reason why this couldn't be a section somewhere on the website without having to click through.

Host: Yeah. So I think high level here, um, the call to action, "join the wait list," maybe isn't the primary one that you want to optimize for. Um, get people in actually experiencing the product through the playground or through their challenge to break the firewall. And maybe make those more prominent. Especially because a lot of this, you know, you've got text here that you can select and copy that looks just like the buttons. So some way to make these primary actions that you want users to take more prominent. Um, I think is the thing that's going to lead to more people wanting to join the wait list.

David: Well, thank you, Automorphic. This was super interesting. Very exciting.

Host: All right, next up we have Trigger.dev. Let's take a look.

David: Cool domain. Cool domain. Easy to remember.

Host: Yep. I like that I can see the GitHub stars right at the top. This is a popular project. 4,100 stars. You know it's legit, right out of the gate.

David: Right.

Host: Yep. We've got a little Discord icon for joining the community here, and they have pricing. So they're a little bit more mature. You can actually pay for this.

David: Yeah, talk about that a little bit. What does even having pricing indicate to you when you are browsing these?

Host: I say having pricing is the difference between a project and a product. If there's no pricing, you're a project, especially if you're open source. Once there's pricing, then you know, I, from as an owner of a company, we deploy a lot of technology and we have a lot of vendors. Um, it's something I can consider buying, putting it into production, and relying on it. It convinces you it'll stick around and be supportive. It's a good sign.

David: All right. So the "open-source background jobs framework for Next.js. Create long running jobs directly in your code base with features like API integrations, webhooks, scheduling, and delays." All right, so let's see. Okay, this is interesting. So it looks like they're showing us the code here, and they're actually highlighting in plain English what each line of code does, which is very interesting. It really helps me understand quickly, at a glance, a foreign codebase that I'm not instantly familiar with.

Host: Yeah, this is their core example of defining one of their jobs, and they're sort of breaking it down step by step what's happening. It's a lot of information, but it's really well done. Very cool. Then they get into some of their features. I love a feature grid. The sort of bento box design is, sometimes how it's referred to, where you have you split up your major features into these sort of interlocking rectangles where you get a title, a short description, and then you do an illustration. It's a really nice way to consume important features.

David: Yeah, you can tell that they care about design here. Like, even just how it's easy to just dump a block of code in a box and move on, but you can tell it's like very thoughtful.

Host: Okay, the complete open source. So is this a code framework? It's self-hosted? You host it yourself? So this is a library or... Wait, cloud? Just, I think they have both.

David: Okay, so they have both okay. So they have a cloud, and you could run it yourself.

Host: Yep. Okay, yep. Let's check out the open source project to see its health. Continue to... Oh no, that's not the GitHub icon. Made me think that was the repo. It is, okay, great. I think it is. It said "continue to Trigger.dev," right, which means that's where we were. They meant the repo.

David: Okay. Um, 4.1 stars? Okay, so they weren't faking it. Yeah. 11 pull requests. Great. Let's go to insights. Let's just see. Is this a vibrant open source project? Go to contributors. I would say if there's more than like six contributors with some activity, like there's some momentum around the open source, if you just see the founder of the company and nothing else, then and it doesn't really have traction yet. And why does that matter to you, seeing a bunch of contributors?

Host: It's just one of the health signals of an open source project. You can have an open-source project that's just the externalized source code of the company and no one's engaging. Um, if you're going to get the benefit of open source, you want people forking the code, contributing back, bug fixes, et cetera. Usually don't get feature development if you're a company sponsoring your own open source project. But let's see. Okay, we've got Matt, Erica, Samer, DKP. So we had four, four, and then a long tail of lesser contributors. So like, the fifth contributor... Oh, that's action spot. So the first external contributor, number six, has done 15 commits, 1,600 lines of code. That's not nothing. Was all very recent. So it's a new open source project.

David: Yeah, they must have open sourced recently. But this is good, and you can tell that their care for design on their website seeps through into GitHub. The readme, everything.

Host: Yeah. So high level, what do you think, David?

David: I think this is a really nice open-source company product. It's clear that they have some traction on their open source repository. Uh, they also have nice design, interesting approach to explaining how their product works. It's a great package.

Host: Awesome. Well done, Trigger. Okay, next up we have Mozart Data. Let's check it out.

David: "The modern data platform for growing businesses. Every tool you need to make the most of your data. ETL, data warehousing, data transformation, and more." That's a lot. It makes me skeptical that they do all of those very well, right?

Host: Yeah, it's not as specific as some of the value props that we've seen before. Um, this is very broad, and there might be some there there, but it is a little bit concerning at first.

David: Okay, so let's dig deeper.

Host: Yeah. "Trusted by..." Okay, so Rippling uses it. These are real companies.

David: Yeah, real companies use it, right? So this is good. Studies is a great sign of maturity. I would check those out if I was feeling skeptical.

Host: Okay, let's get into what is the actual product. So they have an ETL product. Let's go see how this works. All right, we're seeing a screenshot of the product for the first time.

David: Yep. I think it's almost always a mistake not to have a screenshot of your product on the homepage. You don't want to bury that.

Host: Well, because we were left wondering specifically what they do, and this, I mean, we, it's too small to tell what's going on. We've got a bunch of, um, data sources, I presume, that are floating around here. Um, but at least this convinces us that this is a real thing, and there's more context on this specific product. I would say if you're building a developer tool and especially if you're early stage, the people coming to your website are developers. They're going to be using your product. Show them the product. Show them the code examples. As you get later stage, the people coming to your website might be higher level engineering executives, and then you might want the customer testimonials, the pricing, "contact sales." But when you're early, I think you want to show the product right away.

David: Yeah, maybe that's the stage that they're at, where they want to show more of the testimonials, and they're appealing to some of those leaders that need to check boxes on different features, rather than actually seeing it in action themselves. And it seems like, um, this is interesting because they have a bunch of different products here. And so when you've got this many different products, how do you simplify that, say, on a homepage, without sounding like you do everything? It's a challenge for sure. I would maybe break them up into their own section, and maybe we'll even see that as we go, if they treat each one independently so we can understand them one at a time. Um, we're still seeing the sort of vague promises of putting insights into reach, connecting and syncing, centralizing processes. As a developer, this doesn't really speak to me when it's not talking about the technology. This is a very high-level landing page. I think one of the other things, you know, piece of information that that we're not privy to, um, from our vantage point, is like, who is their target, right? And if it was an individual developer, well, it's missing, you know, some of those specific things that if you were looking, you know, David, the guy who wants to like just get something up and running and check it out or whatever, is not appealing to you. But maybe that's not who they're going to. Let's check the pricing to try to understand.

Host: Yeah, so there you go. So they started $1,000 a month.

David: So this is a bit more mature pricing.

Host: Mmhmm.

David: Developer tools at early stage are usually free or some ridiculously low price like $4 a month, greatly undercharging, right?

Host: Yeah. So this pricing tells me they're probably going for larger companies. Um, there's probably lots of key decision makers that need different bits of information before making a purchasing decision. And so maybe from that perspective, you know, this site actually does a good job. And I think it just comes down to who is the target user that you're looking for and making sure that you have the relevant information that they're looking for. You can also see the main CTA is "book demo." Mmhmm. It's not "check out our GitHub repo" or "download some code." It's "talk to a person, get on a calendar."

David: So this is more sales-led.

Host: Yep.

David: Awesome. Very cool. Mozart Data, it seems like a pretty mature product that does a lot of things and commands a high price, which is which is great. I think Mozart would be proud.

Host: Yeah. All right, next up we have Sweep. "Ship code faster." Okay.

David: Okay, ship code faster sounds good. Yeah, I'm in.

Host: "Let Sweep handle your tech debt so you can focus on the exciting problems." Okay, so it's not literally about shipping faster. It's probably about spending more time cleaning up or spending less time cleaning up tech debt so you can spend more time actually shipping code. That's my takeaway so far.

David: It's going to delete my tech debt? Should be amazing.

Host: Okay, we've got a demo, a visualization you. Okay, so you go on GitHub, you make an issue, and then Sweep is going to magically create a PR for you with what...

Host: You've described this as sensational and extremely exciting. It took us way too long to figure out what it was. I'd love to know, as soon as they get on this webpage, sweep automatically creates PRs against your code base based on issues you file, something like that. Just very clearly tell me what this thing does because it's too exciting for people to miss out on it.

Sweep CEO: Yep. Trusted by engineers from these companies.

Host: Okay, all right. So now we're starting to get into some of the specifics of what it is, but again, still too buried. Like, when people hit the website, you need to hit them over the head with what this does. Otherwise, if it's too nuanced, people are not going to be able to take anything away from it. I'd love to try this. I have some open source projects with some issues. If this let me, like, just maybe for free, give it one of my issues and interact with it, that would be very exciting. Maybe it does installing your repository so I can get it onto my repository. It looks like maybe that's a bit too expensive to let people try it on their own. I guess you have to index all the code.

Host: Yeah, but I think this helps address probably one of the primary questions that people have, which is like, "Sound super exciting. Does it actually work?" You're going to have to try it for yourself. With something this, "Is it too good to be true?" And if you try it and it works, take my money. And if you try and it doesn't work, then you know, you've got to wait for it to become more mature. You can see some example tickets. I really like that they have the chat widget on their website. I'm assuming I can talk to a person.

Host: Um, I think it's really great when you're early in your company to be hyper available to your customers. Get the Intercom app on your phone in your pocket and put it on your landing page and let people interrupt your dates, your dinners, distract you at the gym, and talk to your customers all the time. If the founders are available behind that, it'd be really exciting to start talking to them.

Sweep CEO: Totally. And this is actually, you know, I think a lot of times as small companies and founders, you're worried that your disadvantage is that you're so small. This is actually one of the things that gives you an advantage: your responsiveness, your personal availability, giving people your cell phone number, making yourself available on the website 24/7. No larger company is going to do that. Some middle manager there to be available to win customers, and that's going to make all the difference. It's also the easiest way to impress people in the world is to call yourself a founder and like reply to people's emails and their chats. People are like, "Wow, I can't believe I'm talking to the founder." You don't have to tell them that you're just two people, but it feels great.

Host: Overall, this is a very exciting idea. And if this works well, this website is totally burying the lead. They need to tell people that this is something that can automatically write PRs against your repositories on GitHub just from tickets. Well, great job, Sweep. Very cool. Really exciting. All right, next up we have Mirror. "Your custom UI Library without all the work. All right, production ready customizable React components powered by a no code editor. Front end has never been easier." All right, so we've got a screenshot over here. It just looks like a generic editor kind of interface. I'm still a little confused about what this is. "Your custom UI Library without all the work. Production ready customizable React components powered by a no code editor. Front end." So I'm guessing your front-end developers and maybe even your designers build React components in this no code editor and then your developers import them.

Mirror CEO: Yeah, my hunch is, you know, this age old problem of having a single source of truth for the design components that actually matches what's in the code. And this is what they're trying to create. Designers can create and edit components in the component editor, and developers can export code ready for use.

Host: Okay. "Build the product at the speed of light." Okay, they've got template components. One thing I'm struggling a little bit with is their screenshots look like the same design as this website. So the website is black text on a white background, and all the screenshots are also showing black text on a white background, and they kind of bleed into the background, right? It might be better to change the background color of the website so the white UI elements stick out more. Even here, I thought this was a screenshot, and now you're interacting with it.

Mirror CEO: Yeah, it's just a bit confusing to understand what we're looking at. I thought it was a screenshot too.

Host: Okay, so this may be like a live editing version of a piece of the product. It seems like, but that's great. Something interactive. Whenever you can put interactive stuff on your homepage for developer tools where they can see the calculations happen, that's awesome. But I agree with you. You know, this caught my attention as we were scrolling, and so I was just like, "Okay, here's some text or screenshots or something like that." We scrolled right past it. I would recommend here's a simple technique for these contiguous sections: put them on an alternating background color where one is white and the next one is off-white and increase their margin. Right now, these are bleeding into each other. "Build product at the speed of light" with this illustration that doesn't actually do too much for you. Um, and then "document your data system" is another point. I would just put those in separate sections, put some margin, and differentiate the background color to break it up. You can also call out if trying it is actually something really important so people can experience it. There's nothing here that says like, "Try it live," right? Down here, change the label from "Button" to "Edit me" or "Customize me" or something.

Mirror CEO: Yeah, one thing I would point out is I've seen this premise a lot: a no-code React component editor or people who are less technical, or the designers on your team could focus on the component library, then the developers would refer to them. Um, it would be good to acknowledge what's different about this approach. Have they found a new way to make it easier to synchronize that code?

Host: Yeah, is there something differentiated about their editor that makes it even easier to use? And I think you said the key word, which is synchronize. I think the promise of these always sounds great. They fall down in practice because something gets out of sync. A developer edits it directly in code, and now it's not reflected in the design mockups. And so if they do have a way in here to actually keep it always in sync, then I think highlighting that would address the primary concern that a lot of people would have. What takeaways do we have for Mirror?

Mirror CEO: Okay, so if you could help explain sooner what this is, um, this, we have a claim that it's "without all the work." I'd like to know what it is before I understand the benefit. Uh, especially for a developer tool. Some products, you do the other way around. You start with the benefits, and then you can get into the dirty technical details. But when it comes to developer tools, you want to be credible with your users, who are very intelligent, very technical, choosy people. They want the details. I think getting more of the details more succinctly here, rather than that it doesn't require work and that it's production ready, would be really beneficial.

Host: Awesome. Thank you, Mirror. All right, that does it for this episode. Thank you, David, for joining us.

David: Thank you. Super helpful. Really appreciate it.

Host: And great feedback for all the founders, and thank you to all the founders that submitted their websites for review. Really appreciate it. Help us out by letting us know in the comments down below if there were any tips or reviews that you found especially helpful. That'll help us shape future episodes. So until next time, we'll see you on the next design review.
