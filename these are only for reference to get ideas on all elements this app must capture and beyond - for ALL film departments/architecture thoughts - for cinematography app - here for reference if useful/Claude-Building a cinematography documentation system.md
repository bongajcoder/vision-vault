# Building a cinematography documentation system

**User:** Bongani  
**Created:** 11/13/2025 13:41:35  
**Updated:** 11/13/2025 13:45:59  
**Exported:** 11/13/2025 16:10:17  
**Link:** [https://claude.ai/chat/de67d5de-6b12-4b17-8098-46473f0843a2](https://claude.ai/chat/de67d5de-6b12-4b17-8098-46473f0843a2)  

## Prompt:
11/13/2025, 1:41:40 PM

Okay, here we go. So. I need you to read the document called DP Process. Um, And you can also look on Google Drive for some of these documents if you don’t find them in the project knowledge. But DP process, Uh, there’s a document called Nail House to-do list. There’s also documents about cinematography and cinematography prep. And um, I want you to look at past conversations. Where I’m asking questions about cinematography, preparing for cinematography. Um, Coming up with budgets. Um, What else? Essentially, I want to take my entire creative process, logistics process, strategy processes. And you can go through and Look through all the project knowledge, look through past conversations to compile. What? All of this. Might be. Anyhow. Look at all the questions and things I asked for this project specifically. And let’s compile a master document that tries to detail all of the things that a cinematographer has to do to get ready for a shoot. in their own personal work and reviewing stuff. in pulling images, doing all of that stuff. And then also, let’s look at All of the logistics strategy stuff, planning stuff, figuring out execution. Let’s look at all the parts of collaboration that need to happen. between departments, in conversations with the directors, all this stuff. Also look up my own thoughts about directors boot camp and directors being the ultimate collaborators. I think I also have lists of all the different positions and what the duties of different positions are. So we need awareness of that. Um, And then, you know, you can reference books like the 5 Cs of cinematography. Uh, Bruce Block, I think, writes a book called The Visual, um, story, I think. Um, There’s a book called The New Cinematographers. Uh, Roger Deakins just released a book called Reflections. You should research that. But then that’s also research across the web. All the parts that go into a cinematographer’s work. What might be taught in schools, but also more specific, the real life experience, and also gleaning from all of the elements and projects and things that I have done. specifically. And let’s compile everything we understand about. The cinematography process from script. or even idea, to screen. Because I have been using uh, projects, right? I create a project, I put a handful of files in there for the project knowledge, including the script and all these things. And I go through this process, Of eventually, Breaking it down, looking for keywords, looking for stuff on shot deck, on the website, FLIM.AI. Um, you know, I do different cinematography analysis. Then after I’m done with the cinematography, analysis. Uh, you know, I do some story analysis stuff, right? Then I combine that with all of my own notes and thoughts about the story. And then that goes into a cinematography project, and we have a cinematography handoff. project. And all those things, Add up and add up and add up to eventually where I start working on the visual language, and all this stuff, and that’s my own personal process. And then there’s discussions with the directors. There’s the director’s notes, there’s director’s materials, and then in prep now, we’re in location scouting, and we are, Discussing shot lists and stuff like that. And personally for me, What works best is for us to just talk about everything. Even when I read a script, I do voice notes and voice dumps. And one approach I’m trying to do for this Shot list. This time around and everything around this film is I just want to record all of our conversations. Then I’m going to have you, transcribe them and then sort them into, Sort the notes. to figure out action items, to do list things, Um, you know, add to the shot list. You know, some pieces of information need to be added to several different styles of documents that we use in film processes. But I want to now create an entire system. That uses the API, And also the Claude SDK. So we can do A gentic AI, A G E N T I C. And have subagents and multiple agents that take care of all the parts. Right? So let’s architecture and think about, If we were going to, in a sense, create an AI cinematographer. But really, it’s so that I can Almost duplicate myself. And enable myself to do more work. I can ask for very specific tasks to be done. I can ask for a series of tasks to be done. For example, I could give it a script and have it go through the entire process to give me the visual language and all of those elements and then give me versions of what the shot list should be, basically from end to end so that I could read a script today and have a plan to shoot it 100% tomorrow, including things about lighting, about grip, about camera department. including making gear lists. And having actual real numbers. For all those things, you know? So it needs a knowledge base where I can fill in Stuff from previous shoots that I have that can be analyzed to add to its intelligence. But then, it needs a researcher agent that can research any part of anything. of any part of this. And there’s probably multiple researcher types, right? There’s a researcher that’s purely creative and for story and for ideating. There’s a researcher that is purely for visual language. Analysis and ideation. And creativity. There’s one that’s just creative and looks at everything only from a creative lens so that we’re always stretching the possibilities. But there’s also one that is a story expert because the best stories are fully integrated and connected to the Story, the best cinematography, sorry, is. Vendor must be a budget expert. There’s an expert at film budgets in general. But also can drill down to make the budget for camera. And for grip and electric. And then I just need an assistant that is keeping track of all the tasks I have to do. Right? So, of course, it presents all the usual things that I should do, and as long as I’ve worked through those tasks, I would have thought and touched every part that I need to be ready to shoot the film. But then also, it can keep track of extra tasks and to do list. Basically, I needed to do this so I can dump different to-do list things. Somewhere, and then it will. Add them and prioritize them, and I can have a place where I’m in putting, but then there’s a place that keeps track of all the tasks that need to be done. And who I need to contact. And so that’s why we need a collaboration agent that understands the roles of every single other department. So that if a task Might involve me asking the producer or the AD or the production designer. Then it can. Let me know who I need to talk to. But it would be great if there’s also a communication agent that will draft all the emails and draft all the communications that I need to do. And it might be able to grab an attachment that one of the other ones made. And get a little package ready to put in my email. You know, eventually it would be great if it can actually just create those drafts for me inside of my actual Gmail. Uh and Google workspace, but that, as long as the writing is done and the attachments are ready, I can do that part manually to begin with. Then, of course, it needs a voice transcription. Agent, And the voice transcription, I have whisper for Mac on my computer. So maybe you can hook to that. Um, You can also download some open source transcription models and just run them on my computer. Um, Or I can just do The Open AI API. Or we can spin up a server that’s run pod. That can do a lot of this. And I know that we also discussed, My entire Bungani, AI ecosystem, Now to include run pod. So be able to run with clone API and clawed agents. And utilize, you know, claude code if it needs to, all these sorts of things. Um, And connect to my obsidian, which I haven’t set up yet, by the way. Or at least have a database where all this stuff is stored. So I have Google Firebase, so I would love everything to always be stored. All versions of everything must be either committed to a get or a GitHub. Or, He stored in Google Firebase. So that I can also keep track of how stuff developed. And maybe then we need an agent that can keep track of how stuff has been developing and be able to reflect that back to me. As well. And then, If you were constructing this system, what other AI agents would you create? Right? Or subagents for this one Program. We’re going to make the most amazing AI powered program. For me, to make cinematography easy. It’s almost like I just, I need to clone myself. Because with my autism and ADHD now, These 8 hour, 10 hour, 12 hour days. I need to. I need to reduce my workload dramatically. And so my goal is that so many conversations can be captured. By voice. I take a lot of pictures and video, which will all be tacked by location, of course, from my phone. Um, We also had, when we were thinking about the run part, stuff and everything, we’re also going to install, I think locally on my machine and then also on one part, some of the, Newer, Open source. AI that are good at multimodal. There’s one that can actually point at stuff for visual analysis. There’s a couple that are actually better than Gemini 2.5 Pro at multimodal analysis. We had a whole system. Look that up so that you can also see how we can use those for this as well. Because I think all of the agents we’re creating will jack into that run pod system as well. And I love you to architect this entire thing with me. And then give me all the instructions I need to hand over to Claude Code so that Claude Code can make this thing. And then give me all of the implementation. And remember, this won’t take weeks. It will take hours because I’m going to spin up multiple clawed code instances. To just work. And now there’s clawed code for web. And we can just make them work endlessly. to get this stuff up and running. The most important thing is for us to design an excellent system. So, bring all of that info, research, all of that info. And less design the system and get this going. I’m going to personally run this prompt inside of my Bungani Inc. project inside of the cinematography project, inside of specific films that I have projects for. And also in Bungani Labs, and then eventually combine all of that. In Bongani labs to Combine all the ideas and systems together as one.

By the way, this is building to what I think would be a separate program, but with all the similar parts of program that I was wanting to design called I think we called it Nexus or Film Nexus, where everyone inputs all of their information all the heads of Dept and everybody working on the film so it can help the prep process be easier. You can also look at that project if you have access to it and find it for perspective, but I think we’ll build that separately because my more immediate need is the Cinematography one for me.

Also, whatever extra special knowledge you feel that you have in this project to add that would be useful for something like this please also detail that



## Response:
11/13/2025, 1:45:16 PM

````plaintext
Thought: Architecting multi-agent cinematography system with specialized subagents.
````

I'm going to approach this systematically. This is a MASSIVE undertaking, and I'm genuinely excited about it. Let me start by getting oriented and then we'll build this thing properly.

**user_time_v0**

*Request*

````javascript
{}
````

*Response*

````javascript
{"current_time":"2025-11-13T13:42:10-0800"}
````

````plaintext
Thought: Architected comprehensive research strategy for complex cinematography system design.
````

Okay, it's 1:42 PM Wednesday - you're coming out of peak window but still in solid working mode. Perfect timing for system architecture work.

Let me search strategically. I'll start with project knowledge for the core documents you mentioned, then past conversations about your cinematography process, then we'll design this beast.

**project_knowledge_search**

*Request*

````javascript
{
  "query": "DP Process cinematographer workflow prep preparation",
  "max_text_results": 10
}
````

*Response*

````plaintext
Jan 29th - Feb 10th Whole Team Thread Summary
Connections and Insights:
Collaboration and Communication: The thread demonstrates a collaborative effort among the team members, with Tracy Ip facilitating communication and ensuring everyone is on the same page.
Iterative Process: The team's workflow is iterative, with updates to schedules, documents, and the pre-vis shared as they become available.
Attention to Detail: The detailed discussion of VFX gags and the pre-vis notes show the team's focus on ensuring each aspect of the production is carefully planned and executed.
Clear Action Items: The consistent identification of action items helps keep the project moving forward and ensures individual responsibilities are understood.
Overall, the email thread provides a comprehensive overview of the pre-production process for the project, highlighting the team's collaboration, attention to detail, and commitment to delivering a high-quality final product.

It doesn’t look like there are any specific action items for Bongani, the DP, in the email thread. However, as the Director of Photography, they will be involved in the pre-vis meeting and the pre-pro meetings where shot framing, camera angles, lighting, and other visual elements will be discussed. Bongani should take note of the following:
Pre-Vis Meeting: The pre-vis meeting will frame up each shot in the script, including camera angles and movements. Bongani’s input will be valuable here.
Pre-Pro Meeting: The team will go through the entire script and shooting schedule, discussing each shot in detail. Bongani should be prepared to discuss camera and lighting requirements for each shot.
VFX Shots: Nate, the VFX artist, will be on set to check each VFX shot before recording. Bongani will need to work closely with Nate to ensure that the camera and lighting are set up correctly for these shots.
Lighting and Camera Angles: The general notes mention matching light angles and camera angles when shooting. This will be a key responsibility for Bongani.
Green Screen: Some shots will be done on green screen. Bongani will need to ensure that the lighting and camera setup are appropriate for green screen work.
Overall, while there are no explicit action items, Bongani's involvement in the meetings and their role as DP means they have a significant responsibility in realizing the visual aspects of the production.
````

````plaintext
Bongani Mlambo DP Mail - IHYH __ Cinematographer Thread-updated.pdf
Bongani Mlambo <bongani@bongaj.com>
IHYH || Cinematographer Thread
6 messages
Tracy Ip <ip.tracy.k@gmail.com> Fri, Jan 10, 2025 at 11:47 AM
To: Bongani Mlambo DP <bongani@bongaj.com>, Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>
Cc: Olivia Cade <asst@rocketjump.com>
Hi All!
Wanted to start a new thread for all things technical! Bongani is officially on board and avail for our shooting dates! Yahoo!
First and foremost- couple of updates for you Bongani:
1) Denmark is working on renders of the bedroom and will have an accurate render to share on January 17th- day of the previs. That being said, we're hoping to
have you both sync in person at the warehouse space and tape out where you'd like the bedroom set to go!
2) We're tentatively looking at a 9:00AM/ 10:00 AM start time for the previs on Jan 17!
3) Bongani- what does your next week look like? Would you have any availability to sync with Matt and Freddie and start chatting through any of the creative?
@Olivia Cade would you mind scheduling?
Thanks Bongani!
Best
Tracy
Tracy Ip
+01 949 701 8863
Showreel
www.levantblanc.com
Tracy Ip <ip.tracy.k@gmail.com> Tue, Jan 21, 2025 at 9:34 AM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: Olivia Cade <asst@rocketjump.com>, Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>
Good Morning Everyone!
1/26/25, 10:39 PM Bongani Mlambo DP Mail - IHYH || Cinematographer Thread
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-f:1820892567937801279&simpl=msg-f:1820892567937801279&simpl=msg-f:1821880784437858633&simpl=msg-a:r93221378… 1/4

I hope you had a wonderful weekend! Thank you again for your time on Friday for the Previs! Bongani I wanted to check in with you re: Crew, Gear, etc for the
project! Wanted to see if you had gear list & potential crew you'd like me to reach out to and get the process going? Here's an overview of what I have allocated
below:
1) G&E List- Budget 7K includes trucking
2) Camera- originally no budget for this as we were going to use Matt & Freddie's Gear LMK if anything has changed
3) VTR - 1K
4) Dolly $800
We're Non-Union on crew and working off invoices and not payroll. If it helps with rates I can definitely get this paid out in a NET 14.
Crew
1st AC 375/12 for (4) Days + 25 Kit - no prep day
Originally Freddie had offered to prep cam gear but LMK if we're going elsewhere for add'l rentals and I'll work on this!
2nd AC 350/12 for (4) Days + 25 Kit
VTR/ DIT person 375/12 for (4) Days
I believe his name was Nate/ or Nick? Apologies!
Gaffer 375/12 (4) Days
LMK if he/she has a kit!
Key 375/12 (4) Days
Swing 350/12 (4) Days
Equipment:
If this helps I have
(1) 19" Atmos Sumo Monitor
(1) Litemat 4 - I think it's Bicolor and not RGB
Re: Monitors- we'll have (3) Puppeteers on day 3 (shoot day 2) the day we're shooting the party scene. So we'll need at least (3) Puppeteer monitors.
````

````plaintext
Claude-Technical Requirements and Budget for Previs Project.md
## Prompt:
I have some updates as of today jan 26, 2025.

We did a scout and previs session on Friday 17th Jan, 2025.

Details and findings from the scout are in project knowledge: Previs Notes x Scout 1.17.25 .

There is an updated script for reference: "HAPPY YOURE HERE - ANXIETY - 1-7-25 - SM ..."

Please analyze and process all of the transcript and notes according to the prompt attached(pasted content).

For reference this all discusses the filming potential of the film and creative ideas and execution ideas around it done in the warehouse stage that we will shoot in. Bongani, the cinematographer mostly is narrating, but we occasionally have Matt, Freddie, and Ashly contribute.

The the png floorplan of stage is attached. the set will be a 20x16 ft sized set with 10ft walls. The dimensions are represented by the 5 chairs forming a rectangle shaped area. the bed and desk/chair will be in the actual set. This was just a mock up.

Also in knowledge "**Bongani Mlambo DP Mail - IHYH \_\_ Cinematographer Thread-updated.pdf"** are the most updated email conversations between Bongani and Tracy the producer. I need to also extract and combine this information, the asks, and figure out what is needed of me (Bongani) and any action items. Along with what you find from the transcript and previs notes.

## Response:
I'll help analyze all the information from the previs session, scout notes, updated script, and email communications to create a comprehensive understanding of the project status and action items. Let me break this down systematically following the input processing framework.

First, let me process all inputs using the Input Processing Protocol:

1.  Source Organization:

*   Jan 17, 2025: Previs & Scout Session at Nail House Stage
*   Jan 21, 2025: Tracy's email about crew/budget details
*   Jan 22-23, 2025: Follow-up emails scheduling next discussion
*   Updated script dated Jan 7, 2025
*   Stage floorplan showing 20x16ft set dimensions

2.  Key Findings & Technical Requirements:

A. Set & Space Configuration:

*   Main bedroom set: 20x16 ft with 10ft walls
*   Multiple green screen requirements:
    *   8x green screen (or seamless) for main area
    *   12x20 blue screen for window views
    *   Additional green screen for treadmill shots

B. Lighting Plan:

*   Grid system needed between beams
*   9 space lights minimum for set coverage
*   Additional lighting for:
    *   Window lighting
    *   Ground-level shaping
    *   Green screen illumination
    *   Specific puppet areas

C. Camera & Movement:

*   Need for dolly with vibration isolator
*   Possible telescoping arm (25-30ft)
*   Remote head setup (possibly Ronin)
*   Monitor requirements for puppeteers (2-3 depending on day)

D. Budget Allocations (from Tracy):

*   G&E: $7K including trucking
*   Camera: Initially no budget (using Matt/Freddie's gear)
*   VTR: $1K
*   Dolly: $800

3.  Immediate Action Items for Bongani:
4.
````

````plaintext
IHYH G&E Catch Up - 2025/02/12 17:59 PST - Notes by Gemini
ement coordination
Art department access
Power distribution
Monitor placement
Quality Control & Technical Standards
Testing Requirements
Screen evenness
Light levels
Color accuracy
Monitor positions
Puppeteer workspace
Safety Considerations
Rigging verification
Power management
Access paths
Equipment security
Set stability

Technical Workflow & Process Analysis
Camera Package & Integration
FX3 cameras being used
Light levels calibrated accordingly
Need for zoom lens capabilities
Possible tilt-shift lens for "anxiety cam"
Shot-Specific Technical Requirements
Opening Sequence
Dynamic movement requirements
Multiple puppet integration
Set coverage needs
Lighting flexibility
Bedroom Scenes
Coverage for both windows
Party sequence lighting variations
Morning/afternoon/night looks
Plant puppet considerations
Blue Screen Work
Main Character Shots
Walking sequences
Treadmill work
Park bench scene
Transition moments
Puppet-Specific Requirements
Finger puppet shots
Full-body puppet work
Multiple puppet interactions
Background puppet action
Creative Direction & Technical Implementation
Look Development
Main Set Lighting Aesthetic
Soft, glowy overall feel
Three main looks:
Morning
Late afternoon
Night/party
Matching art department's color direction
Visual References
"Waffles and Mochi" style influence
Previous work with Matt and Freddy
Art department style frames
Background plate matching
Technical Solutions for Creative Needs
Puppet Performance Support
Monitor Placement
2-3 puppeteer monitors required
Mobile monitoring solutions
Integration with dolly/slider system
Performance Spaces
Main set blocking considerations
Dedicated green screen area
Floor space requirements
Behind-window puppet positions
Optimization & Efficiency Planning
Space Utilization
Main Stage Area
Set positioning
Screen placement
Equipment storage
Movement paths
Secondary Spaces
Puppet screen room
Equipment prep area
Monitor positions
Cable management
Power Management Strategy
Available Resources
Limited stage power
Distribution needs
Backup considerations
Equipment Selection
LED priority
````

````plaintext
Bongani Mlambo DP Mail - IHYH __ Cinematographer Thread-updated.pdf
2nd AC 350/12 for (4) Days + 25 Kit
VTR/ DIT person 375/12 for (4) Days
I believe his name was Nate/ or Nick? Apologies!
Gaffer 375/12 (4) Days
LMK if he/she has a kit!
Key 375/12 (4) Days
Swing 350/12 (4) Days
Equipment:
If this helps I have
(1) 19" Atmos Sumo Monitor
(1) Litemat 4 - I think it's Bicolor and not RGB
Re: Monitors- we'll have (3) Puppeteers on day 3 (shoot day 2) the day we're shooting the party scene. So we'll need at least (3) Puppeteer monitors. All other
days we will have (2) Puppeteers so will need 2 monitors
Let me know if I've missed anything or if you'd like to chat!
Best
Tracy
[Quoted text hidden]
Bongani Mlambo DP <bongani@bongaj.com> Wed, Jan 22, 2025 at 3:48 PM
To: Tracy Ip <ip.tracy.k@gmail.com>
Cc: Olivia Cade <asst@rocketjump.com>, Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>
Hey Tracy,
Thank you for the update and summary.
I took a bunch of notes during the previs session between videos, voice notes, etc and need a bit of time to think through the lighting plan so I can give accurate
lists.
1/26/25, 10:39 PM Bongani Mlambo DP Mail - IHYH || Cinematographer Thread
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-f:1820892567937801279&simpl=msg-f:1820892567937801279&simpl=msg-f:1821880784437858633&simpl=msg-a:r93221378… 2/4

Between Thursday and Friday, I can get that to you. After you have a chance to review it, then let's connect Monday/Tuesday to chat logistics and numbers
Does that work?
If you need any particular piece more immediately, let me know.
Bongani
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
[Quoted text hidden]
Tracy Ip <ip.tracy.k@gmail.com> Wed, Jan 22, 2025 at 3:51 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: Olivia Cade <asst@rocketjump.com>, Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>
Hi Bongani!
Of course! Monday or Tuesday next week is great for me - what are some of your availabilities ?
No need for anything in particular now!
Best
Tracy
[Quoted text hidden]
Bongani Mlambo DP <bongani@bongaj.com> Thu, Jan 23, 2025 at 1:20 PM
To: Tracy Ip <ip.tracy.k@gmail.com>
Cc: Olivia Cade <asst@rocketjump.com>, Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>
Generally open Tuesday, so anytime between Noon and 3 p.m. would work for me.
````

````plaintext
Bongani Mlambo DP Mail - I'm Happy You're Here - Cinematographer Intro.pdf
I hope you had a wonderful Christmas and will have a great New Years! I'm following up with a few things:
1. Please find our Prelim Shooting Schedule HERE - this has already been OK'd by our puppeteer BJ re: timing so please let me know any call outs on your end.
The only other thing to note is that I haven't yet received storyboards for the song we will be shooting so that's still TBD. I believe we're keeping it simple though!
2. We're looking to shoot a Pre-Vis on January 17th- do you happen to have any availability to join? We anticipate that the shoot shouldn't take more than 2-3
hours.
Best
1/10/25, 2:45 PM Bongani Mlambo DP Mail - I'm Happy You're Here - Cinematographer Intro
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-f:1816951636393398189&simpl=msg-f:1816951636393398189&simpl=msg-f:1817072531457513907&simpl=msg-a:r28237231… 4/7

Tracy
[Quoted text hidden]
Bongani Mlambo DP <bongani@bongaj.com> Tue, Dec 31, 2024 at 4:54 PM
To: Tracy Ip <ip.tracy.k@gmail.com>
Cc: Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>, Ashly Burch <ashlyburch@gmail.com>
Hey Tracy,
Thank you for the update. I'll review the schedule in detail in the New Year.
Right now, the 17th is free and I can attend. I am on hold for a commercial, but it's 13/14/15th.
Please feel free to send me any more updated documents. Or can I use the same links and they are updated?
Happy New Year!
Thanks,
Bongani
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
[Quoted text hidden]
Tracy Ip <ip.tracy.k@gmail.com> Wed, Jan 1, 2025 at 7:30 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>, Ashly Burch <ashlyburch@gmail.com>
Hi Bongani!
The most up to date shooting script is HERE (11_14_LINED)! All the updated storyboards and shotlists should be consolidated into the live production shooting
schedule linked before. I'll continue to update this but ping you if any major changes occur.
re: the 17th- perfect! Please hold the 17th for our pre-vis!
Couple more updates from me:
1. I'm working on cutting a VO track with our preliminary records- these are pretty set but we do want to give the puppeteers room to improv beats/ funny moments
on the day of shooting so if that's the case we'll re-record. For now, I'll have those tracks cut for you guys to use on the previs for timing.
2. We are going to shoot the intro song and it will most likely be in the style of New Girl's Intro.
a. If you haven't heard it, this is our working intro song! IHYH INTRO
b. and THIS is our working anxiety song! I believe Matt and Freddie are planning to shoot this outside of our shoot dates with actual people.
````

````plaintext
Bongani Mlambo DP Mail - Nail House l PRELIGHT 12_02_2024 - Cam + G&E game plan.pdf
They are both really cool directors, good people, and value collaboration. I want to emphasize that while certain aspects might feel a bit loose
in terms of workflow, the creative vision and shot list are very solid. We're working off of a previs that we shot entirely the last few weeks!
Please don't hesitate to:
- Make suggestions
- Ask questions
- Flag any concerns
- Request what you need
- Communicate with our producers (Ashim and Cherish) directly as needed and cc/ping me
I am cc'ing Olivia, production coordinator, so she's in the loop.
We're making something fun and I think it's special. Tomorrow is our day to find our feet and get in sync. I'm grateful to have each of you on board.
TUESDAY PREVIEW:
- Continue prep/lighting
- Camera testing and settings optimization (Freddie has an interesting take that
- Stunt team show-and-tell/rehearsal
- Focus on exterior train lighting while stunts work interior
For Robby: Looking forward to having you join us Wednesday!
Let me know if anyone needs clarification on anything. Here's to a great week ahead.
Thanks,
Bongani
P.S. Don't hesitate to call/text if anything comes up
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
.
.
.
.
.
.
.
---------- Forwarded message ---------
From: Olivia Cade <asst@rocketjump.com>
Date: Fri, Nov 29, 2024 at 4:24 PM
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 2/6

Subject: Nail House l Call Sheet - PRELIGHT 12/02/2024
To: Cherish Chen <chen.cherish@gmail.com>, Ashim Ahuja <ashimahuja11@gmail.com>
Hi everyone!
Please find the call sheet and parking overhead attached below for Nail House Pre-Light Day 1 - MONDAY DECEMBER 2ND, 2024.
General Call Time:
PER DEPARTMENT HEADS
--------------
8:00 AM - PRODUCTION
Set Location:
2302 E 15th St
Los Angeles, CA 90021
Parking:
Please see the overhead attached below. Street and building parking are available on Imperial Street and 15th street, highlighted in GREEN. If you have any issues
or questions call Olivia (production coordinator) at 917-676-3317.
We're stoked to start working with y'all so soon!
Please don't hesitate to reach out if you have any questions.
````

````plaintext
Claude-Technical Requirements and Budget for Previs Project.md
Additional Technical Requirements:

*   VTR solution with Resolve
*   Grid system installation hardware
*   Bounce/diffusion package (20'x20' ultra bounce mentioned)
*   Special rigging for puppet-level shots </equipment\_analysis>

<questions\_for\_tracy>

1.  Budget & Equipment:

*   Is there flexibility in the G&E budget given green screen requirements?
*   Can we discuss a pre-light day addition?
*   What's the possibility of additional monitoring budget?
*   Grid installation - who handles rigging/safety?

2.  Crew Considerations:

*   Need for prep day for 1st AC
*   Additional grip for green screen setup/maintenance
*   Monitor tech/video assist position
*   Pre-light day crew requirements

3.  Schedule Clarifications:

*   Load-in timing and access
*   Tech scout scheduling with Denmark
*   Rehearsal time with puppeteers
*   Time for testing monitoring setup

4.  Technical Setup:

*   Grid installation possibilities/restrictions
*   Power distribution plan
*   Air conditioning considerations for puppet comfort
*   Cable management for multiple monitors

5.  Additional Considerations:

*   Storage for equipment between days
*   Backup equipment availability
*   Weather contingency for load-in
*   Security for overnight storage </questions\_for\_tracy>

Would you like me to continue with the creative cinematography analysis next?

## Prompt:
Continue

## Response:
Thank you, I'll continue with the creative cinematography analysis.

<creative\_analysis> Visual Style & Approach:

1.  Camera Style & Movement:

*   Three-quarter and angled shots preferred throughout
*   Dynamic movement coordinated with puppet choreography
*   Special "anxiety cam" concept:
    *   Second camera at unusual angles
    *   Super shallow depth of field
    *   Possible tilt-shift lens use
    *   Serves as alternative coverage

2.  Scene-Specific Approaches:

Opening/Title Sequence:

*   New Girl-inspired style
*   Multiple dynamic moves:
    *   Start from bed
    *   Roll to desk area
    *   Spin in chair
    *   Door interaction
*   Puppet integration through space
*   Camera follows through multiple positions
*   Quick cuts and dynamic movement

Party Scene:

*   Wide establishing shots showing full space
*   Close coverage of Winston in corner
*   Over-shoulder shots for conversations
*   Punch-outs to see full party
*   Table as central element
*   Integration of Christmas lights and atmosphere

Bedroom Coverage:

*   Long lens for plant conversations
*   Matched over-shoulders for plant dialogue
*   Multiple camera positions for bed scenes
*   Door and window integration
*   Space for puppeteer movement behind window

3.  Lighting Concepts:

*   Color-driven approach matching art direction
*   Directional light through windows
*   Three-zone lighting system:
    *   Main set illumination
    *   Window/door motivated light
    *   Puppet-specific highlighting
*   RGB capability for flexibility
*   Matching art department's lighting cues

4.
````

````plaintext
Bongani Mlambo DP Mail - I'm Happy You're Here - Cinematographer Intro.pdf
Best
Tracy
[Quoted text hidden]
Stylecard_W_Comp.png
6048K
Bongani Mlambo DP <bongani@bongaj.com> Sun, Dec 1, 2024 at 7:44 PM
To: Tracy Ip <ip.tracy.k@gmail.com>
Cc: Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>, Ashly Burch <ashlyburch@gmail.com>
Hi Tracy,
Thank you for reaching out and for sharing all these materials!
It's a pleasure to e-meet you as well. I'm excited to learn more about the project, especially given my previous work with Ashly and with puppets.
I wanted to let you know that I'm currently in pre-light and production this week on Matt and Freddie's project, which may limit my availability to thoroughly review
the materials until the weekend. However, I'd still love to connect for a call. I may have some flexibility Tuesday (pre-light), either during break times or in the
evening after wrap. Alternatively, I could review everything thoroughly bit by bit during the week and/or on Saturday and we could set up a call for Sunday if that
works better with your schedule.
What would be your preference for timing?
Also, for any specific questions about dates, rates, prep, etc., I should connect you with my agent - would you like their contact information? We can wait until after
we get a chance to chat.
Looking forward to discussing the project with you!
Best,
Bongani
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
1/10/25, 2:45 PM Bongani Mlambo DP Mail - I'm Happy You're Here - Cinematographer Intro
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-f:1816951636393398189&simpl=msg-f:1816951636393398189&simpl=msg-f:1817072531457513907&simpl=msg-a:r28237231… 2/7

[Quoted text hidden]
Tracy Ip <ip.tracy.k@gmail.com> Mon, Dec 2, 2024 at 7:59 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>, Ashly Burch <ashlyburch@gmail.com>
Hi Bongani!
Please excuse the delay- was traveling back from the East Coast! Copy you re: prelight & production- let’s set up a call for Sunday. That way there’s no rush/ no
pressure for you to review everything in the midst of filming! Would you be available to chat Sunday at 12:00 PM PST or later Sunday evening (post 7:00 PM PST)?
We can even chat the week after if that works best for you- Let me know!
Re: your agent- let’s chat first and then I’ll discuss all the specifics with them afterwards!
All the Best
Tracy
[Quoted text hidden]
Bongani Mlambo DP <bongani@bongaj.com> Tue, Dec 3, 2024 at 8:00 AM
To: Tracy Ip <ip.tracy.k@gmail.com>
Cc: Matthew Arnold <matt@rocketjump.com>, Freddie Wong <freddie@rocketjump.com>, Ashly Burch <ashlyburch@gmail.com>
Hey Tracy,
No worries. East coast, West coast travel is rough. I did that day before Thanksgiving!
Let's plan on Sunday at Noon with the option to chat the week after (though we keep filming that week till the 13th, so earlier morning or evening only).
````

````plaintext
IHYH G&E Catch Up - 2025/02/12 17:59 PST - Notes by Gemini
They also addressed the need for goalposts for the blue screen kinos to facilitate adjustments.
Rigging and Support Structure: They planned to use the existing I-beams on set to hang lights, potentially using stirrups to adjust the height of the different light fixtures.  Kyle Thor suggested using a support rig for the space lights and dropping stirrups for the kinos and lower sky panels to optimize rigging.
Additional Set and Seamless Integration: Another 12x20 blue screen was planned for a second set, with a seamless backdrop extending to the floor. They later decided to reduce the size of this screen to 10x20 for better management. The team also discussed different ways to manage the seam between the blue screen and the seamless chroma on the  floor, including speed clipping or using shorter pipes.
First Day Pre-Light and Workflow: The goal for the first day of pre-light is to set up the lighting for the two main screens before working on the bedroom set. The team planned to work with the art department to coordinate this process and minimize disruption.
Gear List and Budget:  Bongani Mlambo reviewed a gear list that included various lights (600Cs, 600Xs, sky panels, kinos, and MCs), grip equipment (frames, flags, etc.), and other items like light mats . They discussed potential cost savings by removing items already owned by the production company and others not strictly needed. The team decided to replace the 216 diffusion with a 251 for better versatility.
Meeting Conclusion: They concluded the meeting after reviewing the lighting and gear list, agreeing to collaborate further via email and continue discussions about the detailed lighting and rigging diagrams. They noted a target of reducing the current budget quote from 9500 to 8000 by removing unnecessary equipment.

You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes
Please provide feedback about using Gemini to take notes in a short survey.

ADDITIONAL NOTES (Bongani A.I. notes)

Date: February 12, 2025
Duration: 58 minutes, 39 seconds
Location: Virtual Meeting
Meeting Context & Metadata
Participants
Bongani Mlambo (DP)
Harper Thomas (Gaffer)
Kyle Thor (Key Grip)

Meeting Purpose
Technical discussion for lighting and grip requirements for "I'm Happy You're Here" (IHYH) production, including set layout, lighting plan, and equipment needs.
````

````plaintext
Thought: Good start. I found a lot of relevant information. Let me continue searching for:
1. Nail House to-do list
2. Past conversations about cinematography budgeting and prep
3. Director's bootcamp thoughts
4. Film position duties

I need to be strategic with my searches to stay within token budget and not over-retrieve.
````

**project_knowledge_search**

*Request*

````javascript
{
  "query": "Nail House to-do list tasks checklist action items",
  "max_text_results": 8
}
````

*Response*

````plaintext
Bongani Mlambo DP Mail - Nail House l PRELIGHT 12_02_2024 - Cam + G&E game plan.pdf
They are both really cool directors, good people, and value collaboration. I want to emphasize that while certain aspects might feel a bit loose
in terms of workflow, the creative vision and shot list are very solid. We're working off of a previs that we shot entirely the last few weeks!
Please don't hesitate to:
- Make suggestions
- Ask questions
- Flag any concerns
- Request what you need
- Communicate with our producers (Ashim and Cherish) directly as needed and cc/ping me
I am cc'ing Olivia, production coordinator, so she's in the loop.
We're making something fun and I think it's special. Tomorrow is our day to find our feet and get in sync. I'm grateful to have each of you on board.
TUESDAY PREVIEW:
- Continue prep/lighting
- Camera testing and settings optimization (Freddie has an interesting take that
- Stunt team show-and-tell/rehearsal
- Focus on exterior train lighting while stunts work interior
For Robby: Looking forward to having you join us Wednesday!
Let me know if anyone needs clarification on anything. Here's to a great week ahead.
Thanks,
Bongani
P.S. Don't hesitate to call/text if anything comes up
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
.
.
.
.
.
.
.
---------- Forwarded message ---------
From: Olivia Cade <asst@rocketjump.com>
Date: Fri, Nov 29, 2024 at 4:24 PM
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 2/6

Subject: Nail House l Call Sheet - PRELIGHT 12/02/2024
To: Cherish Chen <chen.cherish@gmail.com>, Ashim Ahuja <ashimahuja11@gmail.com>
Hi everyone!
Please find the call sheet and parking overhead attached below for Nail House Pre-Light Day 1 - MONDAY DECEMBER 2ND, 2024.
General Call Time:
PER DEPARTMENT HEADS
--------------
8:00 AM - PRODUCTION
Set Location:
2302 E 15th St
Los Angeles, CA 90021
Parking:
Please see the overhead attached below. Street and building parking are available on Imperial Street and 15th street, highlighted in GREEN. If you have any issues
or questions call Olivia (production coordinator) at 917-676-3317.
We're stoked to start working with y'all so soon!
Please don't hesitate to reach out if you have any questions.
````

````plaintext
Bongani Mlambo DP Mail - Nail House l PRELIGHT 12_02_2024 - Cam + G&E game plan.pdf
Bongani Mlambo <bongani@bongaj.com>
Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
5 messages
Bongani Mlambo DP <bongani@bongaj.com> Sun, Dec 1, 2024 at 7:16 PM
To: "Karson Holbrook (Kansas City 1st AC Film) (1st AC Shot of Whiskey Film LA)" <karson.holbrook@gmail.com>, Robby Marino <robbymarino@yahoo.com>, "Erique
DuBois (Film LA Key Grip Union/Non-Union)" <erique.a.duboise@gmail.com>, "Harper Holocombe Thomas (Electric Gaffer BBE Film LA Virgin Highland Park) (Gaffer
Disney Launchpad Film LA)" <harper.ht@gmail.com>, "Nicholas Kalajdzic (Film LA Gaffer Electric Union, Olivia Rocketjump)" <ndkalajdzic@gmail.com>,
allysalisbon@gmail.com
Cc: "RocketJump Superstar (Film LA)" <asst@rocketjump.com>
Hey everyone,
Here's the plan for tomorrow (Monday) and a few key notes about our shoot. Please read through and let me know if you have any questions.
MONDAY SCHEDULE:
- 9:00 AM: Camera team (Karson & Allysa) meets at warehouse. Robby, you join us Wednesday.
- 10:00 AM: G&E team (Harper, Erique, Nick) meets at warehouse for walkthrough and planning
- G&E Truck pickup timing TBD (will update in AM)
- Working until approximately 6:00 PM (flexible up to 12hr day if needed)
KEY GOALS FOR MONDAY:
1. Camera team:
- Review and pack RocketJump gear
- Head to Lightstone for integration with rental package. (~11:30 AM they'll be ready for us)(using Freddie's minivan)
- Return to set with complete camera package by EOD (flexible)
2. G&E team:
- Walk through space and review lighting plan
- Review gear lists and identify any gaps
- Focus on train interior setup (Stunts need access most of Tuesday to rehearse)
- Plan rigging and other needs for Tuesday.
IMPORTANT NOTES:
- The warehouse will be open from 8 AM if anyone wants to beat traffic.
- Breakfast will be available
- Lunch will be individual orders by production or you can get reimbursed
- Several moving pieces are coming together on the day - flexibility (and patience 😅 ) is key
- We'll assess distro and rigging needs and can add items for Tuesday pickup if needed
GENERAL APPROACH:
Matt and Freddie bring great independent film energy - sometimes high-intensity idea generation, sometimes more laid back, but always focused on maximizing
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 1/6

what we can achieve. They are both really cool directors, good people, and value collaboration. I want to emphasize that while certain aspects might feel a bit loose
in terms of workflow, the creative vision and shot list are very solid. We're working off of a previs that we shot entirely the last few weeks!
````

````plaintext
Bongani Mlambo DP Mail - Nail House l PRELIGHT 12_02_2024 - Cam + G&E game plan.pdf
General Call Time:
PER DEPARTMENT HEADS
--------------
8:00 AM - PRODUCTION
Set Location:
2302 E 15th St
Los Angeles, CA 90021
Parking:
Please see the overhead attached below. Street and building parking are available on Imperial Street and 15th street, highlighted in GREEN. If you have any issues
or questions call Olivia (production coordinator) at 917-676-3317.
We're stoked to start working with y'all so soon!
Please don't hesitate to reach out if you have any questions.
Thanks,
Olivia Cade
Production Coordinator| RocketJump
asst@rocketjump.com
C: 917-676-3317
2 attachments
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 3/6

NailHouse.Overhead.png
552K
NAIL HOUSE_Call Sheets.xlsx - Call Sheet- PRELIGHT Day 1.pdf
104K
Robby Marino <robbymarino@yahoo.com> Sun, Dec 1, 2024 at 7:41 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Received. Thank you!
Robby Marino
2nd AC
(760) 803-4636
robbymarino@yahoo.com
Sent from my iPhone
On Dec 1, 2024, at 7:17 PM, Bongani Mlambo DP <bongani@bongaj.com> wrote:
[Quoted text hidden]
<NAIL HOUSE_Call Sheets.xlsx - Call Sheet- PRELIGHT Day 1.pdf>
<NailHouse.Overhead.png>
Bongani Mlambo DP <bongani@bongaj.com> Sun, Dec 1, 2024 at 7:51 PM
To: "Karson Holbrook (Kansas City 1st AC Film) (1st AC Shot of Whiskey Film LA)" <karson.holbrook@gmail.com>, allysalisbon@gmail.com
Cc: "RocketJump Superstar (Film LA)" <asst@rocketjump.com>
Hey Karson and Allysa,
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 4/6

Revising our camera team call time to 10am.
Lightstone will only be ready for us at Noon/12pm, so we're pushing it back slightly.
Thanks,
Bongani
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
[Quoted text hidden]
Allysa Lisbon <allysalisbon@gmail.com> Sun, Dec 1, 2024 at 8:16 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: "Karson Holbrook (Kansas City 1st AC Film) (1st AC Shot of Whiskey Film LA)" <karson.holbrook@gmail.com>, "RocketJump Superstar (Film LA)"
<asst@rocketjump.com>
Copy, will be there at 10 tomorrow.
````

````plaintext
Claude-Technical Requirements and Budget for Previs Project.md
## Prompt:
I have some updates as of today jan 26, 2025.

We did a scout and previs session on Friday 17th Jan, 2025.

Details and findings from the scout are in project knowledge: Previs Notes x Scout 1.17.25 .

There is an updated script for reference: "HAPPY YOURE HERE - ANXIETY - 1-7-25 - SM ..."

Please analyze and process all of the transcript and notes according to the prompt attached(pasted content).

For reference this all discusses the filming potential of the film and creative ideas and execution ideas around it done in the warehouse stage that we will shoot in. Bongani, the cinematographer mostly is narrating, but we occasionally have Matt, Freddie, and Ashly contribute.

The the png floorplan of stage is attached. the set will be a 20x16 ft sized set with 10ft walls. The dimensions are represented by the 5 chairs forming a rectangle shaped area. the bed and desk/chair will be in the actual set. This was just a mock up.

Also in knowledge "**Bongani Mlambo DP Mail - IHYH \_\_ Cinematographer Thread-updated.pdf"** are the most updated email conversations between Bongani and Tracy the producer. I need to also extract and combine this information, the asks, and figure out what is needed of me (Bongani) and any action items. Along with what you find from the transcript and previs notes.

## Response:
I'll help analyze all the information from the previs session, scout notes, updated script, and email communications to create a comprehensive understanding of the project status and action items. Let me break this down systematically following the input processing framework.

First, let me process all inputs using the Input Processing Protocol:

1.  Source Organization:

*   Jan 17, 2025: Previs & Scout Session at Nail House Stage
*   Jan 21, 2025: Tracy's email about crew/budget details
*   Jan 22-23, 2025: Follow-up emails scheduling next discussion
*   Updated script dated Jan 7, 2025
*   Stage floorplan showing 20x16ft set dimensions

2.  Key Findings & Technical Requirements:

A. Set & Space Configuration:

*   Main bedroom set: 20x16 ft with 10ft walls
*   Multiple green screen requirements:
    *   8x green screen (or seamless) for main area
    *   12x20 blue screen for window views
    *   Additional green screen for treadmill shots

B. Lighting Plan:

*   Grid system needed between beams
*   9 space lights minimum for set coverage
*   Additional lighting for:
    *   Window lighting
    *   Ground-level shaping
    *   Green screen illumination
    *   Specific puppet areas

C. Camera & Movement:

*   Need for dolly with vibration isolator
*   Possible telescoping arm (25-30ft)
*   Remote head setup (possibly Ronin)
*   Monitor requirements for puppeteers (2-3 depending on day)

D. Budget Allocations (from Tracy):

*   G&E: $7K including trucking
*   Camera: Initially no budget (using Matt/Freddie's gear)
*   VTR: $1K
*   Dolly: $800

3.  Immediate Action Items for Bongani:
4.
````

````plaintext
Bongani Mlambo DP Mail - Nail House l PRELIGHT 12_02_2024 - Cam + G&E game plan.pdf
Lightstone will only be ready for us at Noon/12pm, so we're pushing it back slightly.
Thanks,
Bongani
--
Bongani Mlambo | Director of Photography
bongaj.com ||| vimeo | instagram | facebook | twitter
(214) 886 0288
[Quoted text hidden]
Allysa Lisbon <allysalisbon@gmail.com> Sun, Dec 1, 2024 at 8:16 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: "Karson Holbrook (Kansas City 1st AC Film) (1st AC Shot of Whiskey Film LA)" <karson.holbrook@gmail.com>, "RocketJump Superstar (Film LA)"
<asst@rocketjump.com>
Copy, will be there at 10 tomorrow.
Allysa Lisbon
Cinematographer
P: 816-785-8887
Pronouns: she/they
allysalisbon.com
[Quoted text hidden]
Karson Holbrook <karson.holbrook@gmail.com> Sun, Dec 1, 2024 at 9:23 PM
To: Bongani Mlambo DP <bongani@bongaj.com>
Cc: allysalisbon@gmail.com, RocketJump Superstar <asst@rocketjump.com>
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 5/6

Got it. Looking forward to see you Allysa!
_
Karson Holbrook
Camera & Remote Head Technician
816.853.8118
On Dec 1, 2024, at 7:51 PM, Bongani Mlambo DP <bongani@bongaj.com> wrote:
[Quoted text hidden]
1/27/25, 3:58 PM Bongani Mlambo DP Mail - Nail House l PRELIGHT 12/02/2024 - Cam + G&E game plan
https://mail.google.com/mail/u/2/?ik=dbc63a28dc&view=pt&search=all&permthid=thread-a:r-8674374263099266144&simpl=msg-a:r5702149621005779900&simpl=msg-f:1817298470332548964&simpl=msg-a:r-91808… 6/6
````

````plaintext
Notes from whole team thread email on February 3
* Tracy Ip introduced Nate, the VFX extraordinaire, to the team and outlined how VFX gags will be handled.
* Upcoming meetings include a virtual pre-vis and a pre-pro meeting to ensure all gags and moves are accounted for.
* General notes include matching light angles and camera angles during shooting, and minimizing the need for painting in post.
* Creative questions were raised about the realistic or puppetry look of special effects and whether "pick points" will be left in the final video.
* Action items include Matt and Freddie sending over the pre-vis, Tracy making a VFX shot list, Matt providing a list of puppet actions on green screen, and Tracy redoing the shooting schedule.
* A list of specific VFX gags and how they will be handled was provided, with questions highlighted in yellow.
* BJ Guyer asked about the shape of the finger puppet for the control center, and Ashly Burch suggested it could have a unique shape.
* Tracy Ip provided a ROS and schedule for the previs, outlining the agenda and scenes to be covered.

**Relevant to Bongani (DP):**
* Matching light angles and camera angle/perspective during shooting.
* Ensuring wardrobe and puppet colors don't clash with chroma blue.
* Pre-vis meeting to frame up shots and create a pre-vis video.
* Reworked shot list to be provided by EOD tomorrow or Wednesday.
* **Note:** As the previs meeting already happened, Bongani may have already addressed some of the tasks related to camera, lighting, and grip. 

**Relevant to VTR and VFX:**
* Nate will check each VFX shot before recording.
* VFX will handle specific gags (e.g., explosion, electricity on Winston's brain, adrenaline bulging pipes).
* Questions about whether VFX will be puppetry or realistic.
* Tracy will make a VFX shot list once she has the pre-vis.
````

````plaintext
Claude-Technical Requirements and Budget for Previs Project.md
Immediate Action Items for Bongani:
4.  Technical Planning:

*   Finalize lighting plan based on previs notes
*   Complete gear list within budget constraints
*   Determine monitor setup for puppeteers
*   Review camera package requirements

2.  Crew Coordination:

*   Review proposed crew rates:
    *   1st AC: $375/12 (4 days) + $25 kit
    *   2nd AC: $350/12 (4 days) + $25 kit
    *   VTR/DIT: $375/12 (4 days)
    *   Gaffer: $375/12 (4 days)
    *   Key: $375/12 (4 days)
    *   Swing: $350/12 (4 days)
*   Confirm crew availability and needs

3.  Scheduled Tasks:

*   Prepare for Tuesday Jan 28th meeting (12:30 PM PST)
*   Review updated script for any technical implications
*   Coordinate with Denmark on set design details

4.  Questions to Address with Tracy:

*   Camera package requirements beyond Matt/Freddie's gear
*   Additional monitor needs
*   Grid installation possibilities
*   Pre-light day requirements

Would you like me to expand on any of these areas or create a more detailed breakdown of specific components?

I can also create:

1.  A comprehensive technical requirements document
2.  A detailed budget allocation proposal
3.  A crew requirements and schedule analysis
4.  A shot-specific technical breakdown

Let me know which aspects would be most helpful to focus on next.

## Prompt:
Can you please go more into detail on all the equipment needs and gear described and mentioned and all technical requirements. For example, I feel like in the end a bigger green screen was decided for the main stage, but also additional one for green screen room and setup, and also for the windows and there are two windows. Let's accoutn for everytihng (and also for spelling errors in the transcript that might be film gear.

Then please list the additional potential gear. And based on what Bongani has described and cinematography.

I would also like a list of notes and questions I should think about to reply to Tracy in addition to what she has asked of me. I want to make sure to address everything in her email, but also make sure my thoughts and concerns are represented.

lastly, you can do this after can you compile all the creative cinematography type thoughts and conversation about what this might feel and look like.

## Response:
I'll break this down into the requested sections. Let me start with the technical and equipment needs.

<equipment\_analysis>

1.
````

````plaintext
Jan 29th - Feb 10th Whole Team Thread Summary
Connections and Insights:
Collaboration and Communication: The thread demonstrates a collaborative effort among the team members, with Tracy Ip facilitating communication and ensuring everyone is on the same page.
Iterative Process: The team's workflow is iterative, with updates to schedules, documents, and the pre-vis shared as they become available.
Attention to Detail: The detailed discussion of VFX gags and the pre-vis notes show the team's focus on ensuring each aspect of the production is carefully planned and executed.
Clear Action Items: The consistent identification of action items helps keep the project moving forward and ensures individual responsibilities are understood.
Overall, the email thread provides a comprehensive overview of the pre-production process for the project, highlighting the team's collaboration, attention to detail, and commitment to delivering a high-quality final product.

It doesn’t look like there are any specific action items for Bongani, the DP, in the email thread. However, as the Director of Photography, they will be involved in the pre-vis meeting and the pre-pro meetings where shot framing, camera angles, lighting, and other visual elements will be discussed. Bongani should take note of the following:
Pre-Vis Meeting: The pre-vis meeting will frame up each shot in the script, including camera angles and movements. Bongani’s input will be valuable here.
Pre-Pro Meeting: The team will go through the entire script and shooting schedule, discussing each shot in detail. Bongani should be prepared to discuss camera and lighting requirements for each shot.
VFX Shots: Nate, the VFX artist, will be on set to check each VFX shot before recording. Bongani will need to work closely with Nate to ensure that the camera and lighting are set up correctly for these shots.
Lighting and Camera Angles: The general notes mention matching light angles and camera angles when shooting. This will be a key responsibility for Bongani.
Green Screen: Some shots will be done on green screen. Bongani will need to ensure that the lighting and camera setup are appropriate for green screen work.
Overall, while there are no explicit action items, Bongani's involvement in the meetings and their role as DP means they have a significant responsibility in realizing the visual aspects of the production.
````

````plaintext
Thought: Now I'm getting good project knowledge results. Let me search for past conversations about cinematography prep and budgeting. I should be strategic here - not search too many times.
````

Now let me search past conversations about your cinematography process, budgeting, and prep work:

**conversation_search**

*Request*

````javascript
{
  "query": "cinematography budget prep director collaboration shot list visual language",
  "max_results": 8
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/9e9437bf-2979-4e83-86e9-8f20719b7e28' updated_at=2025-01-28T01:20:20.261765+00:00>Technical Requirements and Budget for Previs Project
Lighting & Grip Infrastructure
- We'll need a grid setup between the beams to properly light both the set and green screens
- Planning for approximately 9 space lights (could potentially use Astera tubes) to cover the main set area
- Additional lighting needed for window effects and ground-level shaping

2. Screen Requirements
Based on our walkthrough, we'll need:
- Main 12'x20' screen behind set
- Dedicated screens for both windows
- Additional screen setup for the permanent green screen area (for quick puppet shots)
- Separate screen for treadmill work

3. Monitoring
- Appreciate you sharing the Atmos monitor availability
- We'll need 2 monitors for regular days, expanding to 3 for the party scene
- Looking into efficient ways to handle video village and puppeteer monitoring simultaneously

4. Pre-Light Consideration
Given the complexity of:
- Grid setup
- Multiple screen positioning
- Integration of various lighting zones
- Puppeteer sight lines and monitoring
I believe we should strongly consider adding a pre-light day to ensure efficient shooting days.

I know this might stretch beyond the current budget allocation ($7K for G&E), but I'm actively working on ways to maximize efficiency while maintaining quality. I'll include detailed suggestions in the gear list tomorrow.

For crew, the rates look workable, but I'd like to discuss:
- Adding prep day for 1st AC given potential camera package needs
- Grip support for screen management
- Monitor tech considerations

Happy to get into more detail on any of these points during our Tuesday call. In the meantime, please let me know if you need any clarification on these initial thoughts.

Best,
Bongani

P.S. Do you know if there are any restrictions regarding grid installation in the space? This would be helpful to know ahead of our discussion.

Human: I am providing you with two documents. They are similar but one is more updated so that you can see another reference. Both are the template that I use for my to-do list in tracking my cinematography tasks for projects. I'd like to compile all of the tasks and notes and elements from this particular discussion of ours to add to one that I'll be making for this film that we're working on. Most of what we've discussed should be going into the up next section but we can also create things to add to the notes section or the thoughts section as well. Please analyze and look at both lists carefully to see the type of things that appear but again most things will go into the to-do list section where there is up next and where we can add a custom page for anything that's relevant. Then also notes, thoughts and questions.

You don't have to reouput the entire document. Only compile and output the new items from this conversation that will need to be added.

Assistant:  I'll help compile new items from our conversation that should be added to your cinematography task tracking document.</chat>

<chat url='https://claude.ai/chat/ab26e8d7-2738-43bf-8bed-7ce7ef9959ad' updated_at=2025-11-06T16:54:54.010073+00:00>Comprehensive project continuation and update
Telescoping Crane Demo & Key Grip Hiring
**Link:** https://claude.ai/chat/f0e631cf-78b2-4957-8ed5-7fab6f91636f  
**Date:** February 11, 2025  
**Relevant because:** Miniscope 7 demo arranged with Chapman's Eric Zucker, key grip hiring decision point, rental house relationship building  
**Key points:**
- Miniscope 7 selected (doesn't require dedicated tech, dolly grip can operate)
- Eric Zucker offered key grip recommendations (Chapman network, experts on crane equipment)
- Transparent budget discussion drafted (indie rates, $375/12 for key, kit rental possibilities)
- Demo scheduled for hands-on learning (Bongani + potentially Kyle Thor if hired)
- Decision timeline: end of week to allow prep time before Feb 19

---

## Related Project Knowledge

### From Project Documentation:

**Production Designer Coordination:**
- **Denmark** creating bedroom set renders - critical for lighting planning alignment
- Set construction timing must coordinate with pre-light grid installation
- Window placement/door swing direction final confirmation needed
- Art department's time-of-day lighting cues must match cinematography approach

**Puppeteer Requirements (BJ):**
- Puppet movement limitations dictate camera blocking (can't do certain gags)
- Multiple puppeteers needed for full-body shots (especially party scene - 3 puppeteers = 3 monitors)
- Monitor placement critical for puppeteer sight lines (behind set, specific angles)
- Special considerations: puppet-level shots require custom grip solutions (mechanic's creeper mentioned)

**VFX Workflow (Nate Sam):**
- VTR/DIT role combined - Resolve-based system ($1K budget)
- Clean plates required for all green screen work
- 50% gray for TV screens (no tracking markers needed, edge tracking sufficient)
- Shadow management critical for compositing
- Background integration: three time-of-day versions for bedroom window

**Director Vision (Matt Arnold & Freddie Wong):**
- RocketJump team (same as "We're All Gonna Die" collaboration)
- New Girl-style title sequence emphasis
- Dynamic camera movement coordinated with puppet choreography
- "Anxiety cam" secondary camera concept (unusual angles, sha</chat>

<chat url='https://claude.ai/chat/9e9437bf-2979-4e83-86e9-8f20719b7e28' updated_at=2025-01-28T01:20:20.261765+00:00>Technical Requirements and Budget for Previs Project
* Can we pre-rig before load-in day?
  * What's the available power distribution?

- Budget Clarification:
  * Is there flexibility in G&E allocation if needed?
  * Can we reallocate VTR budget to other areas?
  * What's the expendables allocation?

- Schedule:
  * Can we add dedicated pre-light day?
  * How much prep time with final art elements?
  * What's the testing schedule for puppet interactions?

Would you like me to expand on any of these sections or add additional categories?</chat_conversation></chat>

<chat url='https://claude.ai/chat/ab26e8d7-2738-43bf-8bed-7ce7ef9959ad' updated_at=2025-11-06T16:54:54.010073+00:00>Comprehensive project continuation and update
- Swing position open - potential candidates?
- Prep day for 1st AC? (Camera package familiarization, lens testing)
- Monitor tech/video assist position needed?

**Budget/Producer Communication:**
- Tracy's response to pre-light day advocacy?
- G&E budget flexibility given green screen requirements?
- Can VTR budget reallocate to camera/monitoring needs?
- Expendables allocation amount?
- Payment timing (NET-14 confirmed for crew)?

---

## Relevant Past Conversations

**Note:** These conversations are accessible within this same project. Reference them for deeper detail when needed.

### 1. Initial Project Overview & Agent Coordination
**Link:** https://claude.ai/chat/ed88a26e-8814-4113-a957-e19dfd67ff09  
**Date:** January 10, 2025  
**Relevant because:** Foundation conversation - email to agent Tara Kromer explaining project, Tracy's email threads establishing crew structure/budget, initial meeting notes with Tracy covering technical specs  
**Key points:**
- Matt/Freddie/Ashley Burch recommendation after "We're All Gonna Die" collaboration
- Project goal: pitch to Apple or self-finance for May 2025 (Mental Health Awareness Month)
- Budget constraints established early ($2500-3000 DP flat rate)
- Puppet specs defined (16-18", 2T clothing, movement limitations)
- Set builds outlined (bedroom, hypothalamus miniature, doctor's office)
- References: Waffles & Mochi, Erax, New Girl intro

### 2. Previs/Technical Scout Meeting (Full Team)
**Link:** https://claude.ai/chat/9f3c9d3e-46c0-4296-b8cd-7b3f522c2121  
**Date:** January 17, 2025  
**Relevant because:** Detailed technical meeting with entire creative team (Matt, Freddie, Ashley, Tracy, BJ puppeteer, Denmark production designer, Nate VFX, Meredith AD) - foundational decisions  
**Key points:**
- Electricity effect sequence planning (5-min mark, purple practical gag possibility)
- Bomb squad puppet flight rigging (C-stand + fishing wire)
- Party scene choreography (multiple puppeteers, table as central element, Christmas lights)
- Doctor's office minimal build (modified chair for puppeteer, green screen door)
- Monitor requirements specified (2 regular days, 3 for party scene)
- Complex shot solutions discussed (puppet-level shots, window integration, etc.)

### 3.</chat>

<chat url='https://claude.ai/chat/9e9437bf-2979-4e83-86e9-8f20719b7e28' updated_at=2025-01-28T01:20:20.261765+00:00>Technical Requirements and Budget for Previs Project
Monitoring System:
- Puppeteer Monitors:
  * Need 3 total for party scene
  * 2 for regular days
  * Current available: One 19" Atmos Sumo
  * Need additional matching monitors

5. Camera Package Considerations:
- Currently using Matt/Freddie's camera
- Potential need for additional lenses
- Zoom lens requirements mentioned
- Possible need for tilt-shift lens for "anxiety cam"

6. Specialty Items:
- Long mechanic's creeper for puppet work
- Special monitor mounts for puppeteers
- Custom grip solutions for puppet shots
- Additional photo tripods for flexible mounting

7. Additional Technical Requirements:
- VTR solution with Resolve
- Grid system installation hardware
- Bounce/diffusion package (20'x20' ultra bounce mentioned)
- Special rigging for puppet-level shots
</equipment_analysis>

<questions_for_tracy>
1. Budget & Equipment:
- Is there flexibility in the G&E budget given green screen requirements?
- Can we discuss a pre-light day addition?
- What's the possibility of additional monitoring budget?
- Grid installation - who handles rigging/safety?

2. Crew Considerations:
- Need for prep day for 1st AC
- Additional grip for green screen setup/maintenance
- Monitor tech/video assist position
- Pre-light day crew requirements

3. Schedule Clarifications:
- Load-in timing and access
- Tech scout scheduling with Denmark
- Rehearsal time with puppeteers
- Time for testing monitoring setup

4. Technical Setup:
- Grid installation possibilities/restrictions
- Power distribution plan
- Air conditioning considerations for puppet comfort
- Cable management for multiple monitors

5. Additional Considerations:
- Storage for equipment between days
- Backup equipment availability
- Weather contingency for load-in
- Security for overnight storage
</questions_for_tracy>

Would you like me to continue with the creative cinematography analysis next?

Human: Continue

Assistant:  Thank you, I'll continue with the creative cinematography analysis.

<creative_analysis>
Visual Style & Approach:

1. Camera Style & Movement:
- Three-quarter and angled shots preferred throughout
- Dynamic movement coordinated with puppet choreography
- Special "anxiety cam" concept:
  * Second camera at unusual angles
  * Super shallow depth of field
  * Possible tilt-shift lens use
  * Serves as alternative coverage

2.</chat>

<chat url='https://claude.ai/chat/ed88a26e-8814-4113-a957-e19dfd67ff09' updated_at=2025-01-10T23:55:12.121768+00:00>Overview of "I'm Happy You're Here" Project
PROJECT DESCRIPTION
"I'm Happy You're Here" is a 22-minute educational puppet show about mental health, specifically focusing on anxiety disorders. The project combines live action, puppetry, and educational content with humor to make mental health topics accessible.

2. PRODUCTION TIMELINE
Current Status: Pre-production
Key Dates:
- December 2024: VO recordings completed
- January 17, 2025: Previs shoot scheduled
- February 19-23, 2025: Principal photography
- May 2025: Target completion (Mental Health Awareness Month)

3. TECHNICAL SPECIFICATIONS

A. Set Requirements
1. Main Bedroom Set:
- Three-wall construction
- Window for green screen backgrounds
- Accommodations for plant puppets
- Party scene location
- Dimensions TBD (pending Denmark's renders)

2. Hypothalamus Control Room:
- Miniature diorama construction
- Finger puppet scale
- Practical goo effect capability
- Final size pending camera requirements

3. Doctor's Office:
- Minimal practical set
- Modified chair for puppeteer
- Green screen door element

B. Camera/Technical
- Single camera setup (FX3 or Alexa Mini)
- Green screen requirements
- VTR solution using Resolve
- Multiple monitor setup for puppeteers

4. PUPPET SPECIFICATIONS
- Size: 16-18 inches (2T clothing size)
- Movement limitations based on fabrication
- Multiple puppeteers required for full-body shots
- Special considerations for puppet interaction scenes

5. CREW STRUCTURE
Key Positions:
- Director: Matt Arnold
- Producer: Tracy Ip
- DP: Bongani Mlambo
- Production Designer: Denmark
- Lead Puppeteer: BJ
- Additional crew requirements detailed in schedule

6. BUDGET CONSIDERATIONS
Key Elements:
- DP Rate: $2500-3000 flat (includes previs)
- Crew Rates: $350-400/day range
- Limited VTR budget
- Equipment sharing opportunities identified
- Cost-saving measures implemented where possible

7. CREATIVE ELEMENTS

A. Musical Components:
- Show Theme Song (New Girl-style intro planned)
- Anxiety Coping Methods Song
- Both songs recorded and ready for production

B. Visual Style:
- Mix of practical and VFX elements
- Green screen compositing
- Puppet-scale considerations
- Reference: "Waffles and Mochi" and "Erax"

8. SHOOTING SCHEDULE BREAKDOWN

Day 1 (Feb 19):
- Pre-light and load-in
- Possible anxiety song shoot

Day 2 (Feb 20):
- Science Zone scenes
- Neighborhood Street scenes
- 17 shots scheduled

Day 3 (Feb 21):
- Winston's Brain Party
- Park Bench scenes
- 18 shots scheduled

Day 4 (Feb 22):
- Doctor's Office scenes
- Ashly's Bedroom scenes
- 20 shots scheduled

Day 5 (Feb 23):
- Bedroom continuation
- Hypothalamus Control Room
- Additional social content if time permits
- 10+ shots scheduled

9. IMMEDIATE PRIORITIES
1. Technical:
- Finalize bedroom dimensions
- Confirm monitor requirements
- Establish green screen workflow

2. Creative:
- Schedule DP/Director creative meeting
- Review previs requirements
- Finalize shot list

3.</chat>

<chat url='https://claude.ai/chat/ab26e8d7-2738-43bf-8bed-7ce7ef9959ad' updated_at=2025-11-06T16:54:54.010073+00:00>Comprehensive project continuation and update
oss-Venture Connections:

**Cinematography Philosophy:**
- IHYH puppet work = pattern recognition at different scale (same compositional principles, adjusted for 16" performers)
- Tennis coaching mindset = "see patterns others miss" = anticipating puppeteer needs before they articulate them
- **Frequency work frame:** Lighting as emotional frequency transmission (anxiety episode vs. calm bedroom scenes require different Hz)

**Project Management Approach:**
- IHYH pre-production = FRQ music release systems (delegate execution, retain creative vision)
- VA-style delegation emerging: Tracy handles crew contracts, Bongani focuses on creative/technical strategy
- **8-hour work week principle:** Strategic thinking in meetings vs. execution on set - compressed pre-production mirrors ADHD hyperfocus windows

**AuDHD Optimization in Action:**
- Comprehensive meeting notes = external memory system for detailed technical specs
- Gear list obsession = hyperfocus strength channeled productively
- Pattern recognition = connecting past projects (Nail House gear lists) to current needs
- **Executive function support:** Tracy's NET-14 payment structure, Harper/Kyle handling day-of logistics removes decision fatigue

### Emerging Themes:

**Pre-Light Day as Lynchpin:**
- Mentioned in 4+ conversations as non-negotiable
- Budget friction point but technical necessity
- **Pattern:** Indie films often skip pre-light → chaos on Day 1 → Bongani's advocacy reflects cinematography maturity

**Monitor Proliferation:**
- Started: "We need some puppeteer monitors"
- Reality: 3 puppeteer + director + AC + VFX station = 6+ screens minimum
- **Pattern:** Puppet productions have hidden technical complexity that only reveals through detailed planning

**Color/Mood as Character:**
- Art department renders driving lighting choices
- RGB Astera consideration for flexibility
- Three time-of-day window backgrounds
- **Pattern:** Mental health subject matter demands visual subtlety - lighting becomes therapeutic tool

---

## Emotional & Energy Context

### Bongani's State Throughout Project:

**January 10 (Initial Pitch):**
- Excitement about Matt/Freddie/Ash</chat>

<chat url='https://claude.ai/chat/9e9437bf-2979-4e83-86e9-8f20719b7e28' updated_at=2025-01-28T01:20:20.261765+00:00>Technical Requirements and Budget for Previs Project
Please analyze and look at both lists carefully to see the type of things that appear but again most things will go into the to-do list section where there is up next and where we can add a custom page for anything that's relevant. Then also notes, thoughts and questions.

You don't have to reouput the entire document. Only compile and output the new items from this conversation that will need to be added.

Assistant:  I'll help compile new items from our conversation that should be added to your cinematography task tracking document. Based on our discussion and the template structure, here are the key additions:

UP NEXT:
1. Equipment & Technical Planning
- Create grid system design between beams (5 rows x 3 columns layout)
- Design lighting zones for main set, green screen areas, and windows 
- Plan monitor placement and signal distribution for puppeteers
- Create overhead diagram for main 20'x16' set with camera positions
- Determine seamless vs. hard green screen approach for different areas
- Plan window lighting integration approach

2. Documentation & Creative
- Draw up lighting plot with space light placement (minimum 9 units)
- Create visual references document for "New Girl" style intro sequence
- Document puppet performance requirements for camera movement
- Plan "anxiety cam" approach and requirements
- Design party scene coverage plan with multiple puppets
- Create specific plans for miniature hypothalamus room coverage

3. Communication & Coordination
- Schedule tech scout with Denmark (production designer)
- Plan grid installation approach with rigging team
- Create comprehensive gear list within $7K G&E budget
- Design monitor layout for puppeteer sight lines
- Schedule creative meeting with Matt & Freddie
- Create pre-light day proposal and requirements

NOTES:
- Puppet Scale Considerations:
  * Main puppets: 16-18 inches (2T clothing size)
  * Hypothalamus puppet: Finger puppet scale
  * Multiple puppeteers required for full-body shots
  * Need space behind windows for puppeteer movement

- Technical Requirements:
  * Grid system between beams for flexible lighting
  * Multiple green screen zones (main, windows, dedicated room)
  * Specialized monitor setup for puppeteers
  * Custom grip solutions for puppet-level shots

THOUGHTS:
- Creative Approach:
  * Balance between practical and VFX elements
  * Dynamic movement coordinated with puppet choreography
  * Need for both wide establishing and intimate puppet coverage
  * Potential use of tilt-shift lens for "anxiety cam" perspective
  * Color-driven approach matching art direction
  * Integration of both practical and motivated lighting

QUESTIONS:
- Grid Installation:
  * Are there weight/rigging restrictions in the space?
  * Can we pre-rig before load-in day?
  * What's the available power distribution?

- Budget Clarification:
  * Is there flexibility in G&E allocation if needed?
  * Can we reallocate VTR budget to other areas?
  * What's the expendables allocation?</chat>
````

````plaintext
Thought: Good, I found very relevant past conversations. Now let me search for director's bootcamp and film position duties:
````

**conversation_search**

*Request*

````javascript
{
  "query": "directors bootcamp ultimate collaborator film positions duties responsibilities departments",
  "max_results": 5
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/c1e9b25a-03cf-4961-b1a5-192547072c50' updated_at=2025-02-07T19:16:34.389199+00:00>Comprehensive Film Equipment Recommendations
<chat_conversation>Title: Comprehensive Film Equipment Recommendations

Human: You are an AI assistant with extensive knowledge of film production equipment and practices. Your task is to analyze gear lists, understand lighting requirements, and generate comprehensive equipment lists for a short film production. You will also be prepared to answer follow-up questions about the equipment and setups.

First, review the provided gear lists:
<gear_lists_rental_house>
417057-Nail-House---Grip-
417056-Nail-House---Lighting-
LSR job_943796 (1) (1)
</gear_lists_rental_house>

the below gear lists are the ones Bongani makes then sends to rental houses/producers. The  Nail House ones below correspond to the above rental houses ones, so you can see how the extra details get added by rental house. Please make sure to read any specific notes and make notes of the color coding that is sometimes used.

<gear_lists_bongani_gogole_sheet>
Gear List - Nail House - Grip - Google Sheets
Gear List - Nail House - Lighting - Google Sheets
Gear List - Nail House - Camera - Google Sheets
Champion Short Film - Gear List example 2 -...
Champion Short Film - Gear List example - Go...
</gear_lists_bongani_gogole_sheet>


Next, carefully read the lighting discussion:
<lighting_discussion>
We are working on the list for I'm Happy You're Here. Based on Bongani discussions with Tracy and all of the notes and plan that was established through conversation in "**Claude-Technical Requirements and Budget for Previs Project.md" . **we will make a gear list accounting for everything that Bongani mentioned there and that was discussed to be needed, then also additionally analyze all of our documents and make sure to include other gear that is need, maybe required, and is suggested. We will analyze the script and cinematography goals to stay grounded and suggest truly useful items, but also be creative and help generate ideas.
</lighting_discussion>

One important note in this particular case is that Matt and Freddie own two FX3 camera packages and we will be using that same FX3, typoch lenses, tripods that they own, then supplementing. 

Analyze the gear lists:
1. Identify the types of equipment mentioned (e.g., cameras, lenses, lighting, grip gear, etc.).
2. Note any patterns or common items across different lists.
3. Recognize any specialized or unique equipment.

Understand the lighting requirements:
1. Identify the overall lighting style and mood described.
2. Note any specific lighting setups or techniques mentioned.
3. Recognize any challenging lighting situations or special effects required.

Based on your analysis and understanding, generate comprehensive equipment lists for each department:
1. Camera Department
2. Lighting Department
3. Grip Department
4. Sound Department (as it relates to cinematography needs and gear)
5. Any other relevant departments (as it relates to cinematography needs and gear)

For each department:
1.</chat>

<chat url='https://claude.ai/chat/ed88a26e-8814-4113-a957-e19dfd67ff09' updated_at=2025-01-10T23:55:12.121768+00:00>Overview of "I'm Happy You're Here" Project
IMMEDIATE PRIORITIES
1. Technical:
- Finalize bedroom dimensions
- Confirm monitor requirements
- Establish green screen workflow

2. Creative:
- Schedule DP/Director creative meeting
- Review previs requirements
- Finalize shot list

3. Logistical:
- Complete crew hiring
- Confirm equipment package
- Finalize technical scout timing

10. RISKS AND CONSIDERATIONS
- Heavy daily shot count
- Complex puppet choreography
- Limited VTR budget vs. requirements
- Set space optimization needs
- Multiple element coordination

11. NEXT STEPS
Immediate Actions:
1. Confirm January 17 previs details
2. Schedule creative meeting with directors
3. Review Denmark's bedroom renders
4. Finalize technical requirements
5. Complete contract negotiations

The project combines ambitious technical requirements with creative storytelling, requiring careful coordination between departments and efficient execution to meet the scheduled delivery date.
</comprehensive_report>

This comprehensive report captures the key elements from all provided documents while organizing the information in a clear, actionable format. Would you like me to expand on any particular section or provide additional analysis of specific aspects?

Human: Please write an email summary for me to send to my agent catchign her up to the project. We have not spoken about it so need as much detail for them. Also letting htem know that I have shared their info with Tracy. My agent knows that I worked with Matt and Freddy on the film "We're All Gonna Die" so we can mention that they're the ones that suggested me for this project. Also that Ashley Birch, the person who wrote and is starring in this, is the same actor in the film that we did "We're All Gonna Die".

Assistant:  <antThinking>I'll draft a detailed email to Tara Kromer that provides comprehensive project information while highlighting the existing relationships and context. I'll maintain a professional tone while ensuring all critical details about the project scope, schedule, and rate discussions are included.</antThinking>

Subject: New Project Details - "I'm Happy You're Here" - Puppet Series with Matt & Freddie

Dear Tara,

I hope you're well. I wanted to update you about a new project I've been approached for. Matt Arnold and Freddie Wong (from "We're All Gonna Die") recommended me for a puppet series they're directing called "I'm Happy You're Here." The project stars Ashley Burch, who we also worked with on "We're All Gonna Die" - she's both the writer and lead actor for this show.</chat>

<chat url='https://claude.ai/chat/ab26e8d7-2738-43bf-8bed-7ce7ef9959ad' updated_at=2025-11-06T16:54:54.010073+00:00>Comprehensive project continuation and update
### 3. Technical Requirements & Budget Deep Dive  
**Link:** https://claude.ai/chat/9e9437bf-2979-4e83-86e9-8f20719b7e28  
**Date:** January 26-28, 2025  
**Relevant because:** Post-scout synthesis, email analysis with Tracy, action items extraction, gear needs compilation  
**Key points:**
- 20x16' set dimensions finalized from chair mockup
- Multiple green screen areas specified (8x main, 12x20 windows, treadmill seamless)
- Grid system between I-beams conceptualized (9 space lights minimum)
- Pre-light day advocacy began here (grid + screens + zones too complex for morning setup)
- Budget allocations detailed (G&E $7K, camera using Matt/Freddie's gear, VTR $1K, dolly $800)
- Creative cinematography analysis (three-quarter angles, dynamic movement, color-driven lighting, anxiety cam concept)

### 4. Film Equipment Recommendations & Gear Planning
**Link:** https://claude.ai/chat/c1e9b25a-03cf-4961-b1a5-192547072c50  
**Date:** February 7, 2025  
**Relevant because:** Comprehensive gear list development, lighting package analysis, grip equipment specifications, budget optimization  
**Key points:**
- Examined past gear lists from "Nail House" and "Champion" short films for reference
- Detailed lighting department breakdown (space lights, Sky Panels, Kinos, diffusion)
- Grip department specifications (grip frames, flags, stands, rigging)
- Camera support needs (dolly systems, monitor solutions, specialty items)
- Expendables package (gaff tape, safety equipment, cable management)
- Cost-saving strategies (production-owned gear, rental house relationships)

### 5. Crew Outreach & Project Description
**Link:** https://claude.ai/chat/5b5c2e08-eb9d-4973-beb0-e73ce45dfafa  
**Date:** February 7, 2025  
**Relevant because:** Crafted crew hire messaging with full project details, rates, schedule  
**Key points:**
- Comprehensive text message templates for gaffer/key grip/swing positions
- Project positioning: "22-min mental health educational show with RocketJump, starring Ashley Burch"
- Full rate breakdown included ($375/12 Gaffer/Key, $350/12 Swing, kit rentals possible, NET-14)
- Technical highlights (grid-mounted space lights, green screen zones, dolly/crane work)
- Schedule transparency (pre-light Feb 19, shoot Feb 20-23, 12-hour days)

### 6.</chat>

<chat url='https://claude.ai/chat/ab26e8d7-2738-43bf-8bed-7ce7ef9959ad' updated_at=2025-11-06T16:54:54.010073+00:00>Comprehensive project continuation and update
**Check current time** (use user_time_v0) - Bongani is in LA (PST), shoot is Feb 19-23
5. **Acknowledge what was accomplished** - 1+ month of intensive pre-production captured here
6. **Pick up exactly where we left off** - focus on immediate decision points (crew, gear, pre-light)
7. **Maintain collaborative tone** - peer exploration, not expert lecturing
8. **Respect technical precision** - Bongani operates at professional DP level
9. **Surface pattern connections** - film↔tennis↔music↔ventures↔consciousness work
10. **Don't re-ask questions already answered** - budget/schedule/team/concept all established

### Specific things to remember:

- **This is SAME PROJECT continuation** - past conversations and project knowledge fully accessible via links
- **Shooting in ~6 days** - urgency is real, decisions have immediate consequences
- **Pre-light day approval pending** - this is Bongani's main advocacy point with Tracy
- **Crew hiring urgent** - Harper confirmed, Kyle confirmed, key grip from Chapman or known contacts TBD
- **G&E budget optimization** - $9.5K → $8K target through smart equipment choices
- **Mental health subject matter** - anxiety education for teens+, therapeutic approach to lighting/framing
- **Puppet technical complexity** - 16-18" performers, monitor requirements, sight line challenges
- **Bongani's AuDHD** - comprehensive responses appreciated, pattern recognition valued, hyperfocus protected

---

**Ready to continue? Start here:**

"Hey Bongani - I've synthesized everything from this project (Jan 10 - Feb 14). You're 5-6 days out from Feb 19 pre-light/load-in, with Harper and Kyle confirmed but key grip still TBD between Chapman's network and your known contacts. The big open loop is Tracy's approval on the pre-light day - have you heard back? Also, what's your timeline on finalizing that G&E gear list to hit the $8K target? Let's prioritize the must-dos before Feb 19."

---

**Last Updated:** November 6, 2025, 8:50 AM PST  
**Works with:** conversation_search, project_knowledge_search, recent_chats tools  
**Project:** Same-project continuation (links to past conversations fully functional)</chat_conversation></chat>

<chat url='https://claude.ai/chat/ab26e8d7-2738-43bf-8bed-7ce7ef9959ad' updated_at=2025-11-06T16:54:54.010073+00:00>Comprehensive project continuation and update
### What NOT to Ask Again:

- ❌ "What's your budget?" (Already established: $7K G&E, $2500-3000 DP flat)
- ❌ "Who are the directors?" (Matt Arnold & Freddie Wong, RocketJump, from "We're All Gonna Die")
- ❌ "What's the project about?" (22-min mental health puppet show, anxiety focus, Ashley Burch)
- ❌ "What's the schedule?" (Feb 19 pre-light, Feb 20-23 shoot, 12-hour days, ~70 shots)
- ❌ "Do you need a pre-light day?" (YES, strongly advocated multiple times, awaiting Tracy approval)

### Where to Pick Up:

**Immediate decision points that need resolution:**

1. **Key Grip Hire:** Eric Zucker (Chapman) offered recommendations - do you want Chapman's expert crane operator or hold for known contacts (deadline: end of this week)

2. **G&E Final Gear List:** Current quote $9.5K, target $8K - need final equipment selections to send Tracy (she's waiting)

3. **Pre-Light Day Status:** Have you heard back from Tracy about approving Feb 19 pre-light? This affects crew booking and load-in timing

4. **Miniscope Demo:** When's your Chapman visit with Eric scheduled? Do you want Kyle Thor to come?

5. **Art Department Coordination:** Denmark's bedroom renders due when? Lighting plan depends on window positions and time-of-day mood

---

## Instructions for Next Claude Instance

### When continuing this conversation:

1. **Read this entire prompt thoroughly** - all sections contain essential context
2. **Search linked past conversations if deeper detail needed** - URLs provided for 8 key chats
3. **Reference project knowledge documents** - 10+ files available in /mnt/project/
4. **Check current time** (use user_time_v0) - Bongani is in LA (PST), shoot is Feb 19-23
5. **Acknowledge what was accomplished** - 1+ month of intensive pre-production captured here
6. **Pick up exactly where we left off** - focus on immediate decision points (crew, gear, pre-light)
7. **Maintain collaborative tone** - peer exploration, not expert lecturing
8. **Respect technical precision** - Bongani operates at professional DP level
9. **Surface pattern connections** - film↔tennis↔music↔ventures↔consciousness work
10.</chat>
````

````plaintext
Thought: Synthesized research findings to architect comprehensive AI cinematography system.
````

Alright, I've gathered the foundation. Now let's BUILD this cinematographer AI agent system. This is genuinely exciting - we're essentially creating your digital DP twin.

## 🎬 **MASTER ARCHITECTURE: THE CINEMATOGRAPHER AI AGENT ECOSYSTEM**

Let me lay out the complete system architecture, then we'll break into implementation phases.

---

### **🏗️ SYSTEM OVERVIEW: "CineClone" (or whatever you want to call it)**

**Core Philosophy**: Script → Screen automation while preserving your creative vision and reducing your workload from 12-hour days to strategic decision-making only.

**Primary Goal**: You give it a script today, have a complete shooting plan tomorrow - including visual language, shot lists, gear lists, budgets, and crew communication drafts.

---

## **🧠 AGENT ARCHITECTURE**

### **1. ORCHESTRATOR AGENT** (The Brain)
**Role**: Coordinates all sub-agents, maintains state, routes tasks

**Capabilities**:
- Receives user input (voice, text, script files)
- Determines which agents to activate
- Manages workflow sequencing
- Maintains project context across sessions
- Tracks completion status
- Generates progress reports

**Tech Stack**:
- Claude SDK (primary intelligence)
- State management via Firebase Realtime Database
- Agent orchestration via LangGraph or custom state machine
- WebSocket for real-time updates

---

### **2. VOICE INTERFACE AGENT**
**Role**: Transcribe, process, and route voice input

**Capabilities**:
- Transcribe voice notes (Whisper local or OpenAI API)
- Identify intent (which agent to route to)
- Extract action items automatically
- Tag by category (creative, technical, logistics)
- Timestamped transcripts stored in Firebase

**Tech Stack**:
- Whisper for Mac (local) OR OpenAI Whisper API
- Alternative: Faster-Whisper (open source, runs on RunPod)
- Intent classification via Claude
- Auto-categorization system

**Input Methods**:
- Direct voice recording in app
- Import audio files (from phone voice memos)
- Real-time transcription during meetings

---

### **3. SCRIPT ANALYSIS AGENT**
**Role**: Deep dive into story, character, themes

**Capabilities**:
- Extract scenes, locations, characters, props
- Identify emotional beats and tonal shifts
- Generate story analysis (3-act structure, character arcs)
- Flag technical requirements (VFX, stunts, special equipment)
- Create scene breakdowns
- Identify thematic patterns

**Process**:
1. Parse script (Fountain, FDX, PDF via PyMuPDF)
2. Scene-by-scene analysis
3. Character presence tracking
4. Emotional mapping
5. Technical flags generation
6. Output: Comprehensive story analysis document

---

### **4. CINEMATOGRAPHY CREATIVE AGENT**
**Role**: Visual language development and creative exploration

**Capabilities**:
- Generate keywords from script analysis
- Search Shot Deck and FLIM.AI automatically
- Analyze reference images (color, composition, lighting)
- Propose visual language approaches
- Create mood boards
- Suggest camera movement styles
- Develop lighting philosophies per scene

**Research Tools**:
- Shot Deck API (if available) or web scraping
- FLIM.AI integration
- Pinterest API for mood boarding
- Color palette extraction from references
- Multimodal AI for image analysis (see below)

**Multimodal Models** (for visual analysis):
Based on recent research, best open-source options:
- **Qwen2-VL-72B** (better than Gemini 2.5 Pro for detailed visual analysis)
- **InternVL2** (excellent for spatial reasoning)
- **LLaVA-NeXT** (good for composition analysis)
- **CogVLM2** (strong at technical image understanding)

Deploy on RunPod with A6000 GPUs for fast inference.

---

### **5. TECHNICAL CINEMATOGRAPHY AGENT**
**Role**: Translate creative vision into technical specs

**Capabilities**:
- Generate shot lists from visual language + script
- Specify camera settings (lens, aperture, ISO, shutter)
- Lighting diagrams and setups
- Camera movement specifications
- Coverage plans (masters, mediums, close-ups, inserts)
- VFX shot identification
- Green screen requirements
- Special equipment needs

**Knowledge Base**:
- Your past projects (IHYH, Nail House, etc.)
- Standard cinematography practices
- Equipment capabilities database
- Lens characteristics database

---

### **6. BUDGET AGENT**
**Role**: Generate accurate, detailed budgets

**Capabilities**:
- **G&E Budget** (lights, grip, expendables)
- **Camera Budget** (bodies, lenses, accessories)
- **Labor Costs** (crew rates by position)
- **Rental House Integration** (pull real pricing)
- **Alternate Scenarios** (what if we cut X?)
- **Cost Optimization** (suggestions to reduce budget)

**Data Sources**:
- Your past gear lists and actual costs
- Rental house databases (scraped or API if available)
- Crew rate databases (customizable by region)
- Equipment ownership tracking (Matt/Freddie's gear, etc.)

**Output Formats**:
- Top-sheet budget summary
- Line-item detailed budget
- Department-specific breakdowns
- Excel/Google Sheets export

---

### **7. GEAR LIST AGENT**
**Role**: Generate comprehensive, accurate gear lists

**Capabilities**:
- Camera department lists
- G&E lists (lighting + grip separate if needed)
- Specialty equipment (dollies, jibs, Steadicam)
- Expendables lists
- Backup gear recommendations
- Rental house-ready formatting

**Intelligence**:
- Learns from your past lists (Nail House, Champion, etc.)
- Knows what you own vs. need to rent
- Understands gear relationships (if you rent X, you need Y)
- Flags missing items ("You specified crane but no monitor arm")

**Output Format**:
- Google Sheets (your current style)
- Rental house submission format
- Printable call sheet attachments

---

### **8. COLLABORATION AGENT**
**Role**: Understand all film departments and their needs

**Capabilities**:
- **Department Database** (Producer, AD, Production Designer, Costume, Hair/Makeup, Sound, VFX, etc.)
- **Role Descriptions** (what each person does)
- **Typical Asks** (what info they need from you)
- **Workflow Understanding** (when to loop in which department)
- **Conflict Detection** ("Art wants to paint wall blue, but you need green screen")

**Use Cases**:
- "Who do I need to talk to about getting a pre-light day?" → Producer + AD
- "The set dimensions changed, who needs to know?" → Production Designer, Key Grip, Gaffer, AD
- "We're adding a VFX shot, who should I notify?" → VFX Supervisor, Producer, AD

**Knowledge Base**:
- Standard film department structures
- Your past crew relationships
- Project-specific org charts

---

### **9. COMMUNICATION AGENT**
**Role**: Draft all emails, messages, and documents

**Capabilities**:
- Email drafts (crew hires, producer updates, vendor requests)
- Text message templates (day-of-shoot logistics)
- Call sheet contributions (camera/lighting notes)
- Tech scout reports
- Director's notes summaries
- Gear list cover letters

**Personalization**:
- Learns your voice/style from past emails
- Adjusts formality based on recipient
- Includes relevant attachments (gear lists, schedules)

**Gmail Integration** (Phase 2):
- Create drafts directly in Gmail
- Attach documents from Firebase/Drive
- Schedule sends

---

### **10. TASK MANAGEMENT AGENT**
**Role**: Track everything you need to do

**Capabilities**:
- **Standard DP Checklist** (pre-production through wrap)
- **Custom Task Capture** (add items on the fly)
- **Prioritization** (what's urgent vs. nice-to-have)
- **Dependency Tracking** (can't do X until Y is done)
- **Deadline Awareness** (shoot date countdown)
- **Delegation Flags** (what can others handle)

**Intelligence**:
- Knows standard DP workflows (you've captured this in your process docs)
- Learns your personal additions
- Reminds you of often-forgotten items
- Suggests tasks based on project phase

**Integration Options**:
- Export to Asana/Motion
- Standalone task board in app
- Daily digest emails

---

### **11. VISUAL RESEARCH AGENT**
**Role**: Autonomous creative research

**Capabilities**:
- Scrape Shot Deck, FLIM.AI, Cinematography.com
- Pull frames from Vimeo/YouTube cinematography references
- Analyze color palettes from films
- Find similar visual approaches to your keywords
- Compile reference decks automatically

**Tools**:
- Selenium/Playwright for web automation
- yt-dlp for video downloads
- FFmpeg for frame extraction
- Color Thief for palette extraction
- Claude for visual analysis

---

### **12. LOCATION ANALYSIS AGENT**
**Role**: Process scout photos/videos

**Capabilities**:
- Analyze scout photos (lighting conditions, power access, space dimensions)
- Generate lighting diagrams from location photos
- Identify challenges (low ceilings, windows, etc.)
- Suggest equipment based on location
- Create overhead diagrams
- Sun path analysis for exteriors

**Multimodal Processing**:
- Uses Qwen2-VL or InternVL2 for spatial understanding
- Extracts technical details (ceiling height from reference objects)
- Identifies practical lights and power sources
- Measures approximate distances

**Input**:
- Photos from your phone (with EXIF location data)
- Videos you shoot walking through space
- Voice notes recorded on location

---

### **13. VERSION CONTROL & HISTORY AGENT**
**Role**: Track project evolution

**Capabilities**:
- Git commits for all documents
- Version history browser
- "Show me how the shot list evolved"
- Rollback to previous versions
- Change logs with reasoning

**Storage**:
- GitHub for code/markdown documents
- Firebase for structured data (snapshots)
- Commit messages auto-generated with context

---

### **14. DOCUMENT GENERATOR AGENT**
**Role**: Create production-ready documents

**Capabilities**:
- Shot lists (formatted per your style)
- Cinematography lookbooks
- Tech scout reports
- Lighting plots
- Camera diagrams
- PDF/DOCX/Google Docs export

**Templates**:
- Your existing document formats (learned from past projects)
- Industry-standard formats (for new crew unfamiliar with your style)
- Customizable per project

---

## **🗄️ KNOWLEDGE BASE ARCHITECTURE**

### **Personal Cinematography Database**
Stored in Firebase + searchable via embeddings:

1. **Past Projects**
   - Scripts, shot lists, gear lists, budgets, post-mortems
   - What worked, what didn't
   - Crew notes, location details

2. **Equipment Knowledge**
   - Gear you own
   - Gear you've used and liked/disliked
   - Rental house relationships
   - Pricing history

3. **Cinematography Theory**
   - 5 C's of Cinematography (Mascelli)
   - The Visual Story (Bruce Block)
   - ASC Manual excerpts
   - Your personal philosophies

4. **Reference Library**
   - Saved images from Shot Deck, FLIM.AI
   - Film stills you've collected
   - Color palettes
   - Lighting diagrams

5. **Crew Database**
   - People you've worked with
   - Their rates, specialties, availability patterns
   - Contact info
   - Performance notes

---

## **🔧 TECHNICAL STACK**

### **Frontend** (User Interface)
- **Web App** (React + Tailwind - your design philosophy)
- **Mobile Companion** (React Native or PWA)
- **Voice Input** (browser Web Speech API + backend Whisper)
- **File Upload** (scripts, photos, videos)

### **Backend** (Agent Orchestration)
- **Claude SDK** (primary LLM for all agents)
- **LangGraph** OR **Autogen** (multi-agent coordination)
- **FastAPI** (Python backend services)
- **Firebase Functions** (serverless workflows)

### **Compute**
- **RunPod** (for heavy multimodal processing)
  - Qwen2-VL-72B for image analysis
  - Whisper Large v3 for transcription
  - Batch processing for efficiency

- **Local Mac** (for quick operations)
  - Whisper for Mac (local transcription)
  - Light Claude SDK operations

### **Storage**
- **Firebase Firestore** (structured project data)
- **Firebase Storage** (images, videos, audio files)
- **GitHub** (document version control)
- **Google Drive** (optional integration for easy sharing)

### **APIs & Integrations**
- **Anthropic Claude API** (all agents use this)
- **OpenAI API** (Whisper transcription alternative)
- **Google Drive API** (file sharing)
- **Gmail API** (draft creation in Phase 2)
- **Shot Deck** (if API exists, else web scraping)

---

## **🎯 WORKFLOW EXAMPLE: "Script to Shooting Plan in 24 Hours"**

**User Input**: Uploads script PDF + voice note ("This is a horror short, I want Ari Aster vibes, budget is $10K")

**STEP 1**: Script Analysis Agent
- Parses PDF
- Identifies 12 scenes, 3 locations, 2 characters
- Maps emotional beats (tension → terror → dread)
- Flags: Needs low-light capability, practical effects (blood)

**STEP 2**: Cinematography Creative Agent
- Keywords: "claustrophobic", "shadows", "Ari Aster", "creeping dread"
- Searches Shot Deck: Hereditary, Midsommar, The Witch
- Analyzes color palettes: desaturated, teal shadows, practical warmth
- Proposes: static wide shots, slow push-ins, overhead "god's eye" angles

**STEP 3**: Technical Cinematography Agent
- Generates shot list: 45 shots across 12 scenes
- Specifies: Alexa Mini, Cooke S4 primes, minimal movement
- Lighting: Motivated practicals, negative fill, hard shadows
- Coverage: Wide masters, slow push-ins (dolly), inserts on props

**STEP 4**: Budget Agent
- Camera: Alexa Mini package $1,200/day x 3 days = $3,600
- G&E: LiteMats, LED tubes, neg fill, $2,000
- Grip: Dolly, stands, $800
- Labor: Gaffer, Key Grip, 1st AC, $3,000
- **Total: $9,400** (under $10K budget)

**STEP 5**: Gear List Agent
- Camera list: Alexa Mini, Cooke S4 set, wireless follow focus
- G&E list: 4x LiteMat 4, 8x Quasar tubes, 12x4 neg fill
- Grip list: Dana Dolly, track, apple boxes, flags

**STEP 6**: Communication Agent
- Drafts email to gaffer: "Horror short, practical-heavy, here's mood board"
- Attaches: Shot list, lighting breakdown, reference images
- Drafts email to producer: "Budget breakdown attached, need 1 pre-light day"

**STEP 7**: Task Management Agent
- Presents checklist:
  - [ ] Tech scout location #1
  - [ ] Approve final shot list with director
  - [ ] Confirm crew availability
  - [ ] Reserve camera package
  - [ ] Scout for practicals (lamps, candles)

**User Action**: Reviews everything, makes tweaks, sends drafts

**Time Elapsed**: 2-4 hours of AI processing, 1-2 hours of your review/refinement

**Result**: Comprehensive shooting plan ready to execute

---

## **📱 USER INTERFACE MOCKUP**

### **Dashboard**
```
🎬 CINECLONE - [PROJECT NAME]

Status: Pre-Production (12 days to shoot)

━━━━━━━━━━━━━━━━━━━━━━
🎤 VOICE INPUT
[Record] [Upload Audio]

━━━━━━━━━━━━━━━━━━━━━━
📋 ACTIVE TASKS (7)
☑ Review lighting plot
☑ Confirm gaffer hire
☐ Tech scout Location B
☐ Finalize shot list
☐ Order expendables
☐ Call producer re: pre-light
☐ Send crew welcome email

━━━━━━━━━━━━━━━━━━━━━━
📊 PROJECT STATUS
✅ Script Analysis (Complete)
✅ Visual Language (Complete)
⏳ Shot List (85% complete)
⏳ Budget (Draft ready)
⏳ Gear Lists (In progress)
☐ Crew Communication (Pending)

━━━━━━━━━━━━━━━━━━━━━━
🔄 RECENT ACTIVITY
- Gear list updated (2h ago)
- Email draft created for Harper (5h ago)
- Shot list revised (yesterday)

━━━━━━━━━━━━━━━━━━━━━━
[QUICK ACTIONS]
+ Add Task
+ Voice Note
+ Upload Scout Photos
+ Generate Report
```

### **Agent View** (See what each agent is working on)
```
🤖 ACTIVE AGENTS

Cinematography Creative Agent
└─ Researching low-light compositions (12 images found)

Budget Agent
└─ Calculating alternate G&E scenario (standby)

Task Management Agent
└─ Monitoring 7 active tasks, 2 due tomorrow

Communication Agent
└─ 1 draft email ready for review
```

---

## **🚀 IMPLEMENTATION PHASES**

### **PHASE 1: MVP (Weeks 1-2)** ⭐ START HERE
**Goal**: Core functionality - script in, basic plan out

**Build**:
1. Orchestrator Agent (basic routing)
2. Script Analysis Agent
3. Cinematography Creative Agent (no image search yet, just text analysis)
4. Technical Cinematography Agent
5. Task Management Agent (simple checklist)
6. Basic web interface (upload script, see output)

**Tech**:
- Claude SDK + FastAPI backend
- Simple React frontend
- Firebase for storage
- No RunPod yet (all local/API)

**Output**: Upload script → get story analysis + initial shot concepts + task list

---

### **PHASE 2: Voice & Research (Weeks 3-4)**
**Goal**: Add voice input and visual research

**Build**:
1. Voice Interface Agent (Whisper integration)
2. Visual Research Agent (Shot Deck scraping)
3. Improved Cinematography Creative Agent (with image analysis)
4. Location Analysis Agent (basic version)

**Tech**:
- Whisper API integration
- Web scraping tools (Playwright)
- Multimodal model setup on RunPod (Qwen2-VL)

**Output**: Voice notes → transcribed + routed + analyzed + research images compiled

---

### **PHASE 3: Collaboration & Communication (Weeks 5-6)**
**Goal**: Full team coordination

**Build**:
1. Collaboration Agent (department database)
2. Communication Agent (email drafts)
3. Budget Agent
4. Gear List Agent
5. Enhanced Task Management (dependencies, deadlines)

**Tech**:
- Department knowledge base
- Email template system
- Budget calculation engine
- Gear database

**Output**: Complete production package - shot lists, budgets, gear lists, crew emails

---

### **PHASE 4: Advanced Features (Weeks 7-8)**
**Goal**: Power user tools

**Build**:
1. Version Control Agent
2. Document Generator Agent (beautiful PDFs)
3. Gmail integration (create drafts directly)
4. Mobile app (React Native)
5. Enhanced multimodal (video analysis, location walkthroughs)

**Tech**:
- Git integration
- PDF generation (WeasyPrint or similar)
- Gmail API
- Advanced computer vision models

**Output**: Production-ready documents, mobile access, full automation

---

## **🎨 ADDITIONAL FEATURES TO CONSIDER**

### **Learning Mode**
- Agent watches you work, learns your preferences
- "I see you always add a 4x4 bounce when shooting exteriors - should I make that default?"

### **Collaboration Mode**
- Directors can log in, add notes to shot list
- Producers can see budget updates real-time
- Crew can view their specific task lists

### **Post-Production Bridge**
- Export shot list to DaVinci Resolve database
- Track which shots were captured
- Log notes from set for editorial

### **AI Cinematographer Chat**
- Conversational interface: "What lens should I use for this intimate close-up?"
- It knows your gear, your project, your style
- Learns from every project

---

## **💾 DATA PRIVACY & SECURITY**

- **All project data** stays in your Firebase (you own it)
- **API calls** to Claude (Anthropic doesn't train on API data)
- **Multimodal processing** on your RunPod instance (private)
- **GitHub repos** private by default
- **Option for local-only mode** (no cloud, runs on Mac Mini)

---

## **📦 DELIVERABLES FOR CLAUDE CODE**

I'll create comprehensive specs including:

1. **System Architecture Document** (this, refined)
2. **Agent Specifications** (detailed for each of the 14 agents)
3. **API Contracts** (how agents communicate)
4. **Database Schemas** (Firebase structure)
5. **Frontend Mockups** (Figma or detailed descriptions)
6. **Implementation Roadmap** (step-by-step for each phase)
7. **Testing Plans** (how to validate each agent works)
8. **Deployment Guide** (RunPod setup, Firebase config, etc.)

---

## **🌟 YOUR SPECIAL KNOWLEDGE TO ADD**

From this project and your experience, key elements to encode:

1. **Your Cinematography Philosophy**
   - Collaboration over prescription
   - Story drives visuals
   - Pre-light days are essential
   - Crew relationships matter

2. **Your Workflow Patterns**
   - Voice-first ideation
   - Comprehensive documentation
   - Version tracking everything
   - Cross-department awareness

3. **AuDHD Optimizations**
   - External task capture (dump and forget)
   - Hyperfocus protection (don't interrupt with admin)
   - Pattern recognition enhancement (surface connections)
   - Executive function support (prioritization, deadlines)

4. **Technical Preferences**
   - Your gear choices (why you love certain lights/lenses)
   - Your crew standards (rates, responsibilities)
   - Your communication style (clear, comprehensive, collaborative)

---

## **🤔 QUESTIONS FOR YOU BEFORE I CREATE CLAUDE CODE SPECS**

1. **Priority**: Which phase should we build first? MVP to test concept, or jump straight to Phase 2 with voice?

2. **Compute**: Do you want to set up RunPod now, or start with API-only and add RunPod later?

3. **Interface**: Web-first (desktop) or mobile-first (iPhone)?

4. **Integration**: Must-have integrations for MVP (Google Drive? Gmail? Or standalone first)?

5. **Naming**: What should we call this thing? "CineClone"? "DPilot"? "Bongani.ai"?

6. **Film Nexus**: Should we architect this to later merge with Film Nexus (whole crew tool), or keep separate?

**Let me know your thoughts and I'll generate the complete implementation specs for Claude Code to execute. This is going to be INCREDIBLE.**

🎬🤖✨





---
Powered by [Claude Exporter](https://www.claudexporter.com)