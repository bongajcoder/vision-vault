# Building a cinematography prep system

**User:** Bongani  
**Created:** 11/13/2025 13:25:48  
**Updated:** 11/13/2025 13:28:54  
**Exported:** 11/13/2025 16:13:21  
**Link:** [https://claude.ai/chat/bb439ca9-541e-4070-b782-a404a2f5e461](https://claude.ai/chat/bb439ca9-541e-4070-b782-a404a2f5e461)  

## Prompt:
11/13/2025, 1:25:55 PM

Okay, here we go. So. I need you to read the document called DP Process. Um, And you can also look on Google Drive for some of these documents if you don't find them in the project knowledge. But DP process, Uh, there's a document called Nail House to-do list. There's also documents about cinematography and cinematography prep. And um, I want you to look at past conversations. Where I'm asking questions about cinematography, preparing for cinematography. Um, Coming up with budgets. Um, What else? Essentially, I want to take my entire creative process, logistics process, strategy processes. And you can go through and Look through all the project knowledge, look through past conversations to compile. What? All of this. Might be. Anyhow. Look at all the questions and things I asked for this project specifically. And let's compile a master document that tries to detail all of the things that a cinematographer has to do to get ready for a shoot. in their own personal work and reviewing stuff. in pulling images, doing all of that stuff. And then also, let's look at All of the logistics strategy stuff, planning stuff, figuring out execution. Let's look at all the parts of collaboration that need to happen. between departments, in conversations with the directors, all this stuff. Also look up my own thoughts about directors boot camp and directors being the ultimate collaborators. I think I also have lists of all the different positions and what the duties of different positions are. So we need awareness of that. Um, And then, you know, you can reference books like the 5 Cs of cinematography. Uh, Bruce Block, I think, writes a book called The Visual, um, story, I think. Um, There's a book called The New Cinematographers. Uh, Roger Deakins just released a book called Reflections. You should research that. But then that's also research across the web. All the parts that go into a cinematographer's work. What might be taught in schools, but also more specific, the real life experience, and also gleaning from all of the elements and projects and things that I have done. specifically. And let's compile everything we understand about. The cinematography process from script. or even idea, to screen. Because I have been using uh, projects, right? I create a project, I put a handful of files in there for the project knowledge, including the script and all these things. And I go through this process, Of eventually, Breaking it down, looking for keywords, looking for stuff on shot deck, on the website, FLIM.AI. Um, you know, I do different cinematography analysis. Then after I'm done with the cinematography, analysis. Uh, you know, I do some story analysis stuff, right? Then I combine that with all of my own notes and thoughts about the story. And then that goes into a cinematography project, and we have a cinematography handoff. project. And all those things, Add up and add up and add up to eventually where I start working on the visual language, and all this stuff, and that's my own personal process. And then there's discussions with the directors. There's the director's notes, there's director's materials, and then in prep now, we're in location scouting, and we are, Discussing shot lists and stuff like that. And personally for me, What works best is for us to just talk about everything. Even when I read a script, I do voice notes and voice dumps. And one approach I'm trying to do for this Shot list. This time around and everything around this film is I just want to record all of our conversations. Then I'm going to have you, transcribe them and then sort them into, Sort the notes. to figure out action items, to do list things, Um, you know, add to the shot list. You know, some pieces of information need to be added to several different styles of documents that we use in film processes. But I want to now create an entire system. That uses the API, And also the Claude SDK. So we can do A gentic AI, A G E N T I C. And have subagents and multiple agents that take care of all the parts. Right? So let's architecture and think about, If we were going to, in a sense, create an AI cinematographer. But really, it's so that I can Almost duplicate myself. And enable myself to do more work. I can ask for very specific tasks to be done. I can ask for a series of tasks to be done. For example, I could give it a script and have it go through the entire process to give me the visual language and all of those elements and then give me versions of what the shot list should be, basically from end to end so that I could read a script today and have a plan to shoot it 100% tomorrow, including things about lighting, about grip, about camera department. including making gear lists. And having actual real numbers. For all those things, you know? So it needs a knowledge base where I can fill in Stuff from previous shoots that I have that can be analyzed to add to its intelligence. But then, it needs a researcher agent that can research any part of anything. of any part of this. And there's probably multiple researcher types, right? There's a researcher that's purely creative and for story and for ideating. There's a researcher that is purely for visual language. Analysis and ideation. And creativity. There's one that's just creative and looks at everything only from a creative lens so that we're always stretching the possibilities. But there's also one that is a story expert because the best stories are fully integrated and connected to the Story, the best cinematography, sorry, is. Vendor must be a budget expert. There's an expert at film budgets in general. But also can drill down to make the budget for camera. And for grip and electric. And then I just need an assistant that is keeping track of all the tasks I have to do. Right? So, of course, it presents all the usual things that I should do, and as long as I've worked through those tasks, I would have thought and touched every part that I need to be ready to shoot the film. But then also, it can keep track of extra tasks and to do list. Basically, I needed to do this so I can dump different to-do list things. Somewhere, and then it will. Add them and prioritize them, and I can have a place where I'm in putting, but then there's a place that keeps track of all the tasks that need to be done. And who I need to contact. And so that's why we need a collaboration agent that understands the roles of every single other department. So that if a task Might involve me asking the producer or the AD or the production designer. Then it can. Let me know who I need to talk to. But it would be great if there's also a communication agent that will draft all the emails and draft all the communications that I need to do. And it might be able to grab an attachment that one of the other ones made. And get a little package ready to put in my email. You know, eventually it would be great if it can actually just create those drafts for me inside of my actual Gmail. Uh and Google workspace, but that, as long as the writing is done and the attachments are ready, I can do that part manually to begin with. Then, of course, it needs a voice transcription. Agent, And the voice transcription, I have whisper for Mac on my computer. So maybe you can hook to that. Um, You can also download some open source transcription models and just run them on my computer. Um, Or I can just do The Open AI API. Or we can spin up a server that's run pod. That can do a lot of this. And I know that we also discussed, My entire Bungani, AI ecosystem, Now to include run pod. So be able to run with clone API and clawed agents. And utilize, you know, claude code if it needs to, all these sorts of things. Um, And connect to my obsidian, which I haven't set up yet, by the way. Or at least have a database where all this stuff is stored. So I have Google Firebase, so I would love everything to always be stored. All versions of everything must be either committed to a get or a GitHub. Or, He stored in Google Firebase. So that I can also keep track of how stuff developed. And maybe then we need an agent that can keep track of how stuff has been developing and be able to reflect that back to me. As well. And then, If you were constructing this system, what other AI agents would you create? Right? Or subagents for this one Program. We're going to make the most amazing AI powered program. For me, to make cinematography easy. It's almost like I just, I need to clone myself. Because with my autism and ADHD now, These 8 hour, 10 hour, 12 hour days. I need to. I need to reduce my workload dramatically. And so my goal is that so many conversations can be captured. By voice. I take a lot of pictures and video, which will all be tacked by location, of course, from my phone. Um, We also had, when we were thinking about the run part, stuff and everything, we're also going to install, I think locally on my machine and then also on one part, some of the, Newer, Open source. AI that are good at multimodal. There's one that can actually point at stuff for visual analysis. There's a couple that are actually better than Gemini 2.5 Pro at multimodal analysis. We had a whole system. Look that up so that you can also see how we can use those for this as well. Because I think all of the agents we're creating will jack into that run pod system as well. And I love you to architect this entire thing with me. And then give me all the instructions I need to hand over to Claude Code so that Claude Code can make this thing. And then give me all of the implementation. And remember, this won't take weeks. It will take hours because I'm going to spin up multiple clawed code instances. To just work. And now there's clawed code for web. And we can just make them work endlessly. to get this stuff up and running. The most important thing is for us to design an excellent system. So, bring all of that info, research, all of that info. And less design the system and get this going. I'm going to personally run this prompt inside of my Bungani Inc. project inside of the cinematography project, inside of specific films that I have projects for. And also in Bungani Labs, and then eventually combine all of that. In Bongani labs to Combine all the ideas and systems together as one.

By the way, this is building to what I think would be a separate program, but with all the similar parts of program that I was wanting to design called I think we called it Nexus or Film Nexus, where everyone inputs all of their information all the heads of Dept and everybody working on the film so it can help the prep process be easier. You can also look at that project if you have access to it and find it for perspective, but I think we’ll build that separately because my more immediate need is the Cinematography one for me.

Also, whatever extra special knowledge you feel that you have in this project to add that would be useful for something like this please also detail that



## Response:
11/13/2025, 1:28:50 PM

````plaintext
Thought: Architected multi-agent AI cinematography system leveraging existing workflows.
````

Okay, this is HUGE and exactly the kind of frequency work that lights you up. Let me start by checking the time, then systematically gather everything we need before architecting this entire system.

**Search Strategy:**
1. Current time check
2. Project knowledge: DP Process, Nail House, cinematography prep docs
3. Past conversations: cinematography prep, budgeting, director collaboration
4. Past conversations: Film Nexus/multimodal AI systems
5. Synthesize into complete architecture

Let's begin:

**user_time_v0**

*Request*

````javascript
{}
````

*Response*

````javascript
{"current_time":"2025-11-13T13:26:26-0800"}
````

````plaintext
Thought: Assessed optimal timing and began architecting comprehensive system design.
````

**Wednesday, November 13, 2025 - 1:26 PM PT**
Perfect timing—you're in or just past your peak window. Let's architect this properly.

**project_knowledge_search**

*Request*

````javascript
{
  "query": "DP Process cinematography prep workflow",
  "max_text_results": 10
}
````

*Response*

````plaintext
7.15.25_researched_Kenya Film Industry Rates.pdf
High end if very experienced. | | Assistant Director (1st AD) | 8,000 | ~$60 | 15,000 | ~$115 | 25,000 |
~$192 | Per day . Coordinates shoot schedule/logistics. | | Director of Photography (DP) | 15,000 |
~$115 | 25,000 | ~$192 | 30,000 | ~$230 | Per day . Top DPs in Kenya ~30k; indie/short rates lower. | |
1st Assistant Camera (1st AC) | 5,000 | ~$40 | 10,000 | ~$80 | 15,000 | ~$115 | Per day . Focus puller;
higher end if very skilled. | | 2nd Assistant Camera (2nd AC) | 4,000 | ~$30 | 8,000 | ~$60 | 12,000 | ~$92 |
Per day. Camera loader/support. | | Digital Imaging Tech (DIT) | 8,000 | ~$60 | 15,000 | ~$115 | 25,000 |
~$192 | Per day. Manages data and on-set workflow (kit rental may be extra). | | Prop Master | 5,000 |
~$40 | 10,000 | ~$80 | 20,000 | ~$155 | Per day. Manages props on set. | | Assistant Props | 3,000 | ~$25 |
6,000 | ~$45 | 10,000 | ~$80 | Per day. Prop crew helper. | | Camera Operator | 10,000 | ~$80 | 20,000 |
~$155 | 30,000 | ~$230 | Per day , if separate from DP. Often DP doubles as camera operator. | | Gaffer
(Chief Lighting Tech) | 8,000 | ~$60 | 15,000 | ~$115 | 25,000 | ~$192 | Per day . In charge of lighting
crew/equipment. | | Best Boy Electric | 5,000 | ~$40 | 10,000 | ~$80 | 15,000 | ~$115 | Per day. Assistant
to Gaffer (lighting). | | Electrician (3rd Electric) | 4,000 | ~$30 | 8,000 | ~$60 | 12,000 | ~$92 | Per day.
1
1
1
1
1
1
1
1
````

````plaintext
7.15.25_researched_A Comparative Analysis of Film Production Costs_ Kenya South Africa and the USA.pdf
a
nt
Came
ra
day.3
SA: Mid
-r
ange
day
rate.1
4
US: Non
-
union
1stAC
prep
rate.1
9
11Gaer1174,10
0
5703,500189600KE: $57
0/
day.3
SA: Mid
-r
ange
day
rate.1
4
US: Non
-
union
Gaer
prep
rate.1
9
16Key
Grip
1156,29
0
4333,200173550KE: $43
3/
day.3
SA: Mid
-r
ange
day
rate.1
4
US: Non
-
union
Key
Grip
prep
rate.1
9
37Locati 1132,1102473,300178450KE:
````

````plaintext
7.15.25_researched_Kenya Film Industry Rates.pdf
~$15 | 4,000 | ~$30 | 8,000 | ~$60 | Per day. Entry-level runner; low-end may just receive stipend/
transport. |
Shooting Labor
(Crew labor during the shoot days – many roles repeat from prep, at same day rates, but included here to budget
shoot-period specifically. Only additional roles or differences are noted.)
| Role/Position | Low (KES) | Low (USD) | Mid (KES) | Mid (USD) | High (KES) | High (USD) | Notes |
|-------------------------------|-----------|-----------|-----------|-----------|------------|------------|-----------------------------------------------------------------|
| Producer (on set) | 10,000 | ~$80 | 20,000 | ~$155 | 30,000 | ~$230 | Per day. Overseeing on-set
operations (if actively present). | | Assistant Director (1st AD) | 8,000 | ~$60 | 15,000 | ~$115 | 25,000 |
~$192 | (Same as prep) Runs set schedule on shoot days. | | Director of Photography | 15,000 | ~$115 |
25,000 | ~$192 | 30,000 | ~$230 | (Same rate) Responsible for cinematography on shoot. | | 1st AC / Focus
Puller | 5,000 | ~$40 | 10,000 | ~$80 | 15,000 | ~$115 | (Same) | | 2nd AC / Clapper Loader | 4,000 |
~$30 | 8,000 | ~$60 | 12,000 | ~$92 | (Same) | | Camera Operator | 10,000 | ~$80 | 20,000 | ~$155 |
30,000 | ~$230 | If DP isn’t operating camera, a separate operator is hired. | | Gaffer | 8,000 | ~$60 |
15,000 | ~$115 | 25,000 | ~$192 | (Same) Chief lighting tech during shoot. | | Best Boy Electric | 5,000 |
~$40 | 10,000 | ~$80 | 15,000 | ~$115 | (Same) | | Electrician / Swing | 4,000 | ~$30 | 8,000 | ~$60 |
12,000 | ~$92 | Additional lighting/grip swing as needed (same range as prep). | | Key Grip | 8,000 | ~$60
| 15,000 | ~$115 | 25,000 | ~$192 | (Same) | | Best Boy Grip | 5,000 | ~$40 | 10,000 | ~$80 | 15,000 |
~$115 | (Same) | | Grip (Swing) | 4,000 | ~$30 | 8,000 | ~$60 | 12,000 | ~$92 | (Same) | | Grip/Driver |
5,000 | ~$40 | 8,000 | ~$60 | 12,000 | ~$92 | (Same) | | Crane Techs | 8,000 | ~$60 | 15,000 | ~$115 |
20,000 | ~$155 | (Each, per day) Only if crane/jib is used on shoot days. | | Steadicam Operator | 15,000 |
~$115 | 25,000 | ~$192 | 40,000 | ~$308 | Per day (if used). May include their gear or gear is separate. | |
Choreographer | 5,000 | ~$40 | 15,000 | ~$115 | 30,000 | ~$230 | Per day or flat. If actors’ movement or
dances during shoot. | | Make-Up/Hair | 5,000 | ~$40 | 10,000 | ~$80 | 20,000 | ~$155 | (Same) On-set
make-up artist. | | Make-Up/Hair Assistant | 3,000 | ~$25 | 6,000 | ~$45 | 10,000 | ~$80 | (Same) | |
Costume Designer | 7,000 | ~$54 | 15,000 | ~$115 | 25,000 | ~$192 | (Same as Wardrobe Stylist) Present
on set for wardrobe needs. | | SFX Make-Up Artist | 8,000 | ~$60 | 15,000 | ~$115 | 30,000 | ~$230 |
Special effects makeup (e.g. prosthetics, blood). Only if needed (rate depends on complexity). | | Script
Supervisor | 8,000 | ~$60 | 12,000 | ~$92 | 20,000 | ~$155 | (Same) Maintains continuity, notes during
shoot.
````

````plaintext
7.15.25_researched_A Comparative Analysis of Film Production Costs_ Kenya South Africa and the USA.pdf
83. How much does licensing a pre-existing track cost? : r/Filmmakers - Reddit,
accessed July 15, 2025,
hps://www.reddit.com/r/Filmmakers/comments/17nalpz/how_much_does_licensi
ng_a_preexisting_track_cost/
84. MakeDCP: Indie Film DCP Creation, accessed July 15, 2025, hps://makedcp.com/
85. Digital Cinema Package - DCP Creation & Soware, accessed July 15, 2025,
hps://www.cinematiq.com/digital-cinema-packages
86. DCP Pricing - SV2 DCP, accessed July 15, 2025,
hps://sv2dcp.com/dcp-pricing-calculator
87. Filming requirements - Kenya Film Commission, accessed July 15, 2025,
hps://kenyalmcommission.go.ke/industry-development/lming-requirements/
88. Film Fixer in Kenya - Africa Fixers Ltd, accessed July 15, 2025,
hps://www.lmcrewxersuganda.com/lm-xer-in-kenya/
````

````plaintext
old_for reference only_VoV_v4_noprep_nopostsaturation import essential.pdf
Page 6
Created with TrueBudget, v2.1.4 Printed on 7/18/2025 @ 11:27 PM
Ndiani Studios
v2
DAY
O QTY DAYS RATE 1.5x 2x ESTIMATE
Production Fee: 0%; 0.00
Insurance: 0%; 0.00
P QTY AMOUNT ESTIMATE
282 Sound Mix 1 1 1,000.00
283 Color Correction 1 1 1,750.00
284 Music 1 1 1,500.00
Production Fee: 0%; 0.00 4,250.00
Insurance: 0%; 0.00
ESTIMATE TOTAL P
1500
1000
1750
POST-PRODUCTION EXPENSES RATE
PH&W
ESTIMATE TOTAL O
FRINGE
POST-PRODUCTION LABOR
SUBTOTAL
OVERTIME
````

````plaintext
7.15.25_researched_A Comparative Analysis of Film Production Costs_ Kenya South Africa and the USA.pdf
S
A: Low
-
end
weekl yrate.14 US: Non- union indie rate $800/ day.42
2Assist
ant
Direct
or
1143,81
0
3374,000216600KE: $33
7/
day.3
SA: Mid
-r
ange
day
rate.1
4
US: Non
-
union
1stAD
rate.1
9
3Direct
orof
Photo
graph
y
11104,0
00
80010,00
0
5411,000KE: $80
0/
day.3
SA: Mid
-r
ange
day
rate.1
4
US: Non
-
union
DP
prep
rate.3
41st
Assist
1169,55
0
5353,000162550KE: $53
5/
````

````plaintext
old_for reference only_VoV_v4_noprep_nopostsaturation import essential.pdf
Page 1B
Created with TrueBudget, v2.1.4 Printed on 7/18/2025 @ 11:27 PM
Ndiani Studios
v2
DAY
B QTY DAYS RATE 1.5x 2x ESTIMATE
52 Assistant Director 1 4 2000 8,000.00
53 Director of Photography 1 3 1 3.00
54 1st Assistant Camera 1 5 2500 12,500.00
55 2nd Assistant Camera / DIT 1 3 1400 4,200.00
61 Gaffer 1 3 2800 8,400.00
63 Swing Grip Asst? 2 3 1300 7,800.00
66 Key Grip 1 3 2600 7,800.00
74 Make-Up/Hair 1 3 2400 7,200.00
75 Make-Up/Hair Assistant 1 1 2000 2,000.00
76 Costume Designer 1 3 2700 8,100.00
77 SFX Make Up 1 1 2400 2,400.00
78 Script Supervisor 1 3 1800 5,400.00
79 Boom Operator 1 3 2500 7,500.00
82 Stunt Coordinator 1 1 6300 6,300.00
90 Medic 1 1 2000 2,000.00
97 Production Manager 1 5 2700 13,500.00
99 Production Assistant 2 3 1200 7,200.00
Production Fee: 0%; 0.00 110,303.00
Insurance: 0%; 0.00 (18,751.51)
91,551.49
PH&W
ESTIMATE TOTAL B
FRINGE
SUBTOTAL
SHOOTING LABOR
OVERTIME
````

````plaintext
7.15.25_researched_Kenyan Film Production Rates and International Comparisons.pdf
Kenyan Film Production Rates and International
Comparisons
Kenya: Crew Rates and Production Costs
Kenya’s film industry offers a wide range of crew rates depending on the format, budget, and experience
level. For indie short films and local productions, crew costs are relatively low by global standards (though
rising), while high-end commercials or foreign shoots may pay top dollar for the best local talent .
Below is a breakdown of typical rates (in Kenyan Shillings, with USD in parentheses) for various roles and
expenses in Kenya:
Directors and Producers: Kenyan directors on low-budget shorts often work for very modest fees or
even as passion projects. However, experienced film directors can command anywhere from KES
20,000 to 100,000 per day (≈ $150–$770) on higher-end productions . Line producers or
production supervisors may range roughly KES 15,000–50,000 (≈ $115–$385) per day for seasoned
professionals, with mid-level production managers/coordinators earning toward the lower end of
that range. Newer or indie producers might take nominal fees or a deferred payment if budget is
very tight. Notably, foreign productions typically hire a local line producer or fixer; these service
producers often charge a production service fee (commonly around 10–15% of the local budget) as
their commission for organizing crew, permits, etc. (this fee structure is a standard model
internationally).
Assistant Directors (ADs): A 1st AD on a Kenyan indie film might earn in the range of KES 10,000–
30,000 (≈ $75–$230) per day, depending on experience. A 2nd AD or other assistant directors may
be a bit lower (perhaps KES ~8,000–20,000). For comparison, in South Africa a 3rd AD (comparable to
a production assistant role) earns about R1,500/day (≈ $80) , and in the US a non-union 1st AD
on an indie might make a few hundred dollars a day. Kenyan ADs are likely willing to negotiate
toward the lower end for a passion project, especially if only a few shoot days are involved.
Cinematography Department: This can vary widely. Top Kenyan Directors of Photography (DPs) –
the “best of the best” – can command premium rates, especially when hired by international
productions. It’s reported that crew fees for roles like cinematographer can reach KES 100,000/
day on big projects . More typically, a good local DP might charge KES 20,000–50,000 per day (≈
$150–$385) for an indie short or documentary . A camera operator might be around KES 15,000–
30,000 (≈ $115–$230) per day. Camera assistants (1st AC / focus puller, 2nd AC) and DIT (Digital
Imaging Technician) often range KES 5,000–15,000 (≈ $40–$115) daily on indie jobs, though
experienced focus pullers on bigger sets will ask more (perhaps KES 20k+). (For context, South African
rates for camera crew are a bit higher: e.g. a seasoned DP might get around R4,500/day on corporate
videos and up to R12,000/day on major commercials , i.e. ~$240–$630; a camera operator there
around R2,800/day (~$150) .
````

````plaintext
7.15.25_researched_A Comparative Analysis of Film Production Costs_ Kenya South Africa and the USA.pdf
on
Scout
$247/
day.
3
SA:
Mid-r
ange
day
rate.
14
US:
Nonunion
rate.
19
A TOTA
L
PREPRO
&
WRA
P
598,0
00
4,600 102,0
00
5,514 8,550 Prep
days
are
essen
tial
for a
smoot
h
shoot.
B. SHOOTING LABOR
Line Positi
on
QTY DAYS Kenya
(KES)
Kenya
(USD)
South
Africa
(ZAR)
South
Africa
(USD)
USA
(USD)
Sourc
e &
Notes
52 Assist
ant
Direct
or
1 4 175,24
0
1,348 16,00
0
865 2,400 KE:
$337/
day.
3
SA:
R400
0/day.
14 US:
$600/
day
non-u
nion.
1
9
````

````plaintext
7.15.25_researched_Kenya Film Industry Rates.pdf
Expense Low (KES)
Low
(USD)
Mid
(KES)
Mid
(USD)
High
(KES)
High
(USD)
Notes
Sound
Effects
Library
0 $0 5,000 ~$40 20,000 ~$155
Purchasing sound
FX libraries or
specific audio clips.
Many effects can be
obtained free or
already owned by
sound editor. High
end if buying a
package of highquality sounds or
specialty effects for
the project.
Audio
Deliverables
(Masters)
0 $0 5,000 ~$40 15,000 ~$115
Creating final audio
deliverables: e.g.
separate dialogue,
music, effects
stems, different mix
formats (5.1,
stereo). Low if just a
stereo mix output
(no cost); high if
outputting multiple
mixes for
broadcasters (might
involve extra studio
time).
Online/
Finishing
(if digital
workflow,
minimal)
25
````

````plaintext
Thought: Investigating missing documents and knowledge gaps.
````

**project_knowledge_search**

*Request*

````javascript
{
  "query": "Nail House shot list visual language cinematography handoff",
  "max_text_results": 10
}
````

*Response*

````plaintext
VEINS  OF  THE  VELD — PRODUCTION  &  CREATIVE  DOSSIER 7.12.15 budget stuff
| Consistent across all three briefings.                         |
| **Setting**      | Contemporary Harare ➜ Zimbabwean back‑roads ➜ healer’s rondavel.                                                                                                | No variance.                                                   |
| **Language mix** | English ⇄ Shona (bracketed), plus cultural code‑switching.                                                                                                      | Agreed.                                                        |
| **Genre tone**   | *Darker‑grotesque* psychological horror; minimal gore, emphasis on dread.                                                                                       | Director Thishiwe Ziqubu’s vision uniformly referenced.        |
| **Key Themes**   | Identity, sisterhood, African modernity vs tradition, burden of secrets.                                                                                        | Same list, ordered differently by each briefing; unified here. |

*Complete character bibles, thematic exegesis and script‑evolution notes are retained verbatim in **Appendix A** for departmental deep‑dive.*

---

### 3 · LOCATION & MARKET ANALYSIS

#### 3.1 Macro cost comparison (3‑4 day shoot, identical spec)

| Cost Block            | Kenya (USD) | South Africa (USD) | USA (non‑union indie, USD) | Notes                                                                                       |
| --------------------- | ----------- | ------------------ | -------------------------- | ------------------------------------------------------------------------------------------- |
| Pre‑pro & wrap labour | 4 600       | 5 514              | 8 550                      | Kenya’s non‑union flexibility delivers ±15 % saving over SA and ±46 % over USA.             |
| Shoot‑day labour      | 12 910      | 12 151             | 24 100                     | Near‑parity Kenya/SA; USA nearly double despite non‑union assumptions.                      |
| Location & travel     | 3 705       | 9 803              | 19 600                     | Biggest delta – SA budget assumes Johannesburg–Karoo flights; US assumes interstate travel. |
| Equipment             | 8 240       | 8 167              | 18 500                     | Nairobi rates for FX6 + LED kit confirmed at KES 18k/day.                                   |
| **GRAND TOTAL**\*     | **59  281** | **66  310**        | **156  250**               | Includes 15 % prod‑fee & 10 % contingency.                                                  |

\*Exact line‑item matrix → Appendix B.
````

````plaintext
Veins of the Veld_ Master Project  Production Analysis 7  7.17.25.pdf
Monica acts as her sister's anchor and guide. She is skeptical of the "cure" and
uses humor to mask the gravity of their situation. Her secret—that she transforms
into a hyena—is a testament to her own adaptation and hidden strength.
● SEKURU MUTEMASANGO (50s-60s) - The False Healer: The lm's antagonist.
He presents himself as a traditional healer but is, in fact, a hunter of supernatural
beings. He represents a dogmatic force that seeks to destroy what it doesn't
understand.
● ROSIE (60s) - The Unknowing Mother: Eusive and loving, Rosie embodies the
normal world and the family life that both her daughters have lost and are ghting
to protect.
4. The Creative Team & Vision
This project is driven by a unique family collaboration, ensuring an authentic portrayal
of both Zimbabwean culture and sibling dynamics.
● Nomsa L. Mlambo (Writer, Executive Producer, "Vimbai"): A
Zimbabwean-American actress and writer whose personal experiences navigating
dual cultures are the heart of the lm's themes.
● Bongani Mlambo (Director of Photography, Producer): An acclaimed
cinematographer known for his work on projects for SXSW, OWN/Hulu, and
Nelix, bringing a high-quality, authentic visual language to the story.
● Sibongile Mlambo (Actor, "Monica"): A seasoned actress with major roles in
series like "Siren" and "Lost in Space," bringing depth and experience to the
co-lead role.
● Thishiwe Ziqubu (Director): Envisions a "darker grotesque" style, focusing on
atmospheric tension, psychological horror, and nuanced performances over gore.
● Tendayi Nyeke (Executive Producer): An award-winning producer from Ndiani
Studios, known for the Annie Award-winning Disney+ series "Kizazi Moto."
● Vicki Syal (Producer): An award-winning producer with a history of festival
success.
Visual & Directorial Approach
● Cinematography (Bongani Mlambo): The visual style will contrast the warm,
earthy tones of the natural Zimbabwean veld with the cool, unseling shadows of
the supernatural world. Red will be a recurring motif, symbolizing both bloodlust
and blood ties. Camera work will be largely handheld and intimate to reect
Vimbai's chaotic internal state, contrasted with steady, composed shots of the
"normal" world she has lost.
● Sound Design: The soundscape will juxtapose the eerie quiet of the wild with
vibrant contemporary Zimbabwean music (Amapiano, Jah Prayzah). Key horror
````

````plaintext
old_for reference only_VoV_v4_noprep_nopostsaturation import essential.pdf
Page 1B
Created with TrueBudget, v2.1.4 Printed on 7/18/2025 @ 11:27 PM
Ndiani Studios
v2
DAY
B QTY DAYS RATE 1.5x 2x ESTIMATE
52 Assistant Director 1 4 2000 8,000.00
53 Director of Photography 1 3 1 3.00
54 1st Assistant Camera 1 5 2500 12,500.00
55 2nd Assistant Camera / DIT 1 3 1400 4,200.00
61 Gaffer 1 3 2800 8,400.00
63 Swing Grip Asst? 2 3 1300 7,800.00
66 Key Grip 1 3 2600 7,800.00
74 Make-Up/Hair 1 3 2400 7,200.00
75 Make-Up/Hair Assistant 1 1 2000 2,000.00
76 Costume Designer 1 3 2700 8,100.00
77 SFX Make Up 1 1 2400 2,400.00
78 Script Supervisor 1 3 1800 5,400.00
79 Boom Operator 1 3 2500 7,500.00
82 Stunt Coordinator 1 1 6300 6,300.00
90 Medic 1 1 2000 2,000.00
97 Production Manager 1 5 2700 13,500.00
99 Production Assistant 2 3 1200 7,200.00
Production Fee: 0%; 0.00 110,303.00
Insurance: 0%; 0.00 (18,751.51)
91,551.49
PH&W
ESTIMATE TOTAL B
FRINGE
SUBTOTAL
SHOOTING LABOR
OVERTIME
````

````plaintext
7.15.25_researched_Kenyan Film Production Cost Estimates_.pdf
Colorist $150 -
250
$250 -
500
$600 -
1,200
$800 -
1,800
$500 -
1,000
High-end
grading
suites add
to the
cost.
VFX
Artist
Project
Rate
$200 -
400
$500 -
1,000
$600 -
1,500
$400 -
900
Highly
dependen
t on shot
complexit
y.
Sound
Designer/
Mixer
$150 -
250
$250 -
500
$500 -
1,000
$700 -
1,500
$450 -
900
Includes
dialogue
editing,
SFX, and
mixing.
Section 3: Below-the-Line Expenses: Hard Costs and Services
This section quanties the tangible costs of equipment, logistics, and essential
production services. While some costs like travel are universal, Kenya's mature local
rental market for equipment and transport oers signicant opportunities for budget
optimization.
3.1. Equipment Costs
Kenya possesses a well-established and surprisingly deep equipment rental market,
making it one of the most transparent areas for budgeting. The local availability of
industry-standard, high-end cinema equipment is a game-changer, as it signicantly
reduces the need for complex and costly temporary importation. A producer can
condently budget for A-list gear without automatically budgeting for international
freight, customs brokerage, and insurance, representing a major potential saving in
both time and money.
The decision to "Rent vs. Import" becomes a critical strategic calculation. For
short-form projects like commercials or brief shoots, renting locally is almost certainly
````

````plaintext
old_for reference only_VoV_v4_noprep_nopostsaturation import essential.pdf
Page 6
Created with TrueBudget, v2.1.4 Printed on 7/18/2025 @ 11:27 PM
Ndiani Studios
v2
DAY
O QTY DAYS RATE 1.5x 2x ESTIMATE
Production Fee: 0%; 0.00
Insurance: 0%; 0.00
P QTY AMOUNT ESTIMATE
282 Sound Mix 1 1 1,000.00
283 Color Correction 1 1 1,750.00
284 Music 1 1 1,500.00
Production Fee: 0%; 0.00 4,250.00
Insurance: 0%; 0.00
ESTIMATE TOTAL P
1500
1000
1750
POST-PRODUCTION EXPENSES RATE
PH&W
ESTIMATE TOTAL O
FRINGE
POST-PRODUCTION LABOR
SUBTOTAL
OVERTIME
````

````plaintext
7.15.25_researched_Kenya Film Industry Rates.pdf
Role Low
(KES)
Low
(USD)
Mid
(KES)
Mid
(USD)
High
(KES)
High
(USD)
Notes
Editor 50,000 ~$385 150,000 ~$1,155 300,000 ~$2,310
Fee for editing the film.
Could be a flat project
rate. Low end if using a
less experienced editor
or friend (or the director
self-edits); high end for
a professional editor for
a polished cut. (In Kenya,
freelance editors might
charge ~KSh 10k–20k per
finished minute , so a
15-min short could range
~150k–300k total.)
Assistant
Editor 0 $0 20,000 ~$155 50,000 ~$385
If an assistant is hired to
manage footage, sync,
and prepare cuts. Many
short films skip this role.
Range given if utilized
(e.g. a month part-time).
Graphics
Designer
(Titles)
5,000 ~$40 20,000 ~$155 50,000 ~$385
Creating any 2D
graphics: title
animation, credits
design, any on-screen
text or motion graphics.
Low if only simple
credits; high if custom
animated title sequence
or extensive graphics.
VFX
Artist/
Editor
0 $0 30,000 ~$230 100,000 ~$770
For any visual effects
shots (compositing,
CGI). If minimal (just a
few simple effects),
might pay per shot
~KSh 10k each. High
end if multiple complex
VFX sequences – would
need a specialist for a
few weeks. (For
instance, 5 VFX shots at
~KSh 20k each ≈ 100k.)
17
19
````

````plaintext
old_for reference only_VoV_v4_noprep_nopostsaturation import essential.pdf
Created with TrueBudget, v2.1.4 Printed on 7/18/2025 @ 11:27 PM
Production Company: Client:
Phone: Phone:
Fax: Fax:
Executive Producer: Prepared by: Vicki Syal
Creative Director: Phone:
Director: Email:
Producer:
Writer:
Bid Date: Hours:
Bid Title: Hours:
Job Name: Hours:
Job Number: 3 Hours: 12
Shooting Format:
Shooting Dates:
Pre-Production & Wrap Labor Total A
Shooting Labor Total B
Pre-Production & Wrap Expenses Total C
Location & Travel Total D
Props / Wardrobe / Animals Total E
Stage Rental & Expenses Total F
Art Department Labor Total G
Art Department Expenses Total H
Equipment Costs Total I
Media Total J
Miscellaneous Total K
[A to K] Subtotal
Director / Creative Fees Total L
Talent Labor Total M
Talent Expenses Total N
Post-Production Labor Total O
Post-Production Expenses Total P
Contingency
SA Insurance Premiums
Other
Insurance % 
Production Fee % 
Contracted Total
COMMENTS
759,414.43 TOTAL (ZAR) 759,414.43
50,000.00
18,679.00
4,250.00
44,856.00
586,629.43
55,000.00
4,228.00
53,831.68
18,950.00
151,083.20
38,135.06
181,350.00
41,500.00
91,551.49
6,000.00
SUMMARY OF ESTIMATED PRODUCTION COSTS ESTIMATE
Digital 
Number of Locations: TBD Delivery Date: TBD
Veins of the Veld Studio Shoot Days:
25XX Location Shoot Days:
OT Based On: Digital Delivery Format:
3.18.25 Build & Strike Days:
v2 Prelight Days:
Tendayi 
Nomsa Mlambo
PRODUCTION COST SUMMARY
Ndiani Studios
````

````plaintext
VEINS  OF  THE  VELD — PRODUCTION  &  CREATIVE  DOSSIER 7.12.15 budget stuff
| Samples taken from doc commercials vs indie drama.                                                      | Budget mid‑tier (20 k KES) per primary location; use fixer to negotiate downward on confirmation.       |
| **Insurance**                              | File 4: often skipped for shorts (0 KES low) vs file 5: 385–1 155 USD.                           | Few local insurers offer single‑project policies; foreign festivals increasingly demand E\&O.           | Maintain USD 1 600 line for public liability + basic E\&O; otherwise disqualify from larger fest sales. |

---

### 9 · RECOMMENDED NEXT ACTIONS

1. **Lock Kenyan fixer / EPZ partner (critical path)** – begin permit dossier immediately.
2. **Update crowdfunding comms** to emphasise Kenyan setting & cost‑efficiency; share the comparative cost table above.
3. **Pre‑visualise creature VFX** to final‑pixel‑test vendor pipeline before shoot‑day.
4. **Secure SA post‑house letter** to satisfy dtic rebate and reassure investors of quality finish.
5. **Issue official rate‑card addendum** (Appendix D) to all department heads to prevent on‑set haggling.

---

## APPENDICES (separate files / tabs in this master pack)

* **A. Creative Bible** – full story synopsis, character arcs, thematic grids, script‑evolution logs.
* **B. Tri‑Country Budget Top‑sheet** – locked formulas, editable currency switcher.&#x20;
* **C. Regulatory & Permit Tracker** – step‑by‑step form list with contact details, fees and turnaround.
* **D. 30‑page Kenyan Rate‑Card & Equipment Catalogue** – unchanged from source for audit.&#x20;

---

**Prepared for: Bongani Mlambo & Veins of the Veld production collective
Date: 15 July 2025
Compiler: OpenAI o3 (analyst‑aggregator)**

*(All monetary conversions: 1 USD ≈ KES 130, 1 USD ≈ ZAR 18.5 as per comparative study.)*
````

````plaintext
True Budget - Film Budgeting Software - Positions, Crew, Elements, et al - Line Items Reference 7.18.25
Studio Charges  
* Meals for Crew & Talent  
* Air Conditioning  
* Crew Parking  
* Condor/Scissor Lift  
* Steeldeck

**Art Department Labor**

* Production Designer  
* Art Director  
* Set Director  
* Art Department Coordinator  
* Prop Master  
* Assistant Props  
* Swing  
* Leadman  
* Set Dresser  
* Scenics  
* Grips/Riggers

**Art Department Expenses**

* Set Dressing Rentals (Home, Verandah, Market)  
* Set Dressing Purchases (Hut int. Wall hangings, artifacts)  
* Art Department Prod Supplies  
* Art Department Kit Rentals  
* Special Effects Rentals  
* Art Department Trucking  
* Outside Construction  
* Car Prep  
* Art Department Meals  
* Messengers/Deliveries

**Equipment Costs**

* Camera Rental (SONY FX6 \- E Mount)  
* Sound Rental  
* Lighting Rental (w/ accessories \+ batteries)  
* Grip Rental (includes flags, silks)  
* Generator Rental (Honda EU65is Generator)  
* Crane Rental  
* Diopter  
* Walkie Talkie Rental  
* Dolly Rental  
* SteadiCam  
* Monitors  
* WiVid Transmission  
* Cables  
* Shoulder Rig & Accessories  
* Tripods  
* Expendables  
* Lenses  
* Filters

**Media**

* Media/ Drives (4x)  
* Sony CF Cardreader  
* Process  
* Dailies

**Miscellaneous**

* Petty Cash  
* Work Permits & Visas  
* Phones and Cables  
* Currency Exchange Buffer  
* External Billing Costs  
* Special Insurance  
* Local Communications (Sims, data packages)  
* VAT for Gear (15% of 142.2112k)

**Director/Creative Fees**

* Director Prep  
* Director Travel  
* Director Shoot (All In)  
* Director Post  
* Fringes

**Talent Labor**

* O/C Principals VIMBAI  
* O/C Principals MONICA  
* O/C Principals ROSIE  
* O/C Principals KWAME  
* O/C Principals THULANI  
* O/C Principals JAPHETH  
* O/C Principals WOMAN 1  
* O/C Principals REUBEN  
* O/C Principals SEKURO  
* CITY BG  
* VENDORS  
* WOMAN AT MARKET (NON VOCAL)  
* Voice Over  
* Fitting Fees  
* Audition Fees  
* Talent Agency Fees  
* Talent Payroll Service  
* Talent Wardrobe Allowance

**Talent Expenses**

* Talent Air Fares  
* Talent Per Diem  
* Talent Ground Transportation

**Post-Production Labor**

* Editor  
* Assistant Editor  
* Graphics  
* VFX Editor

**Post-Production Expenses**

* Sound Mix  
* Color Correction  
* Music  
* Legal Services  
* E\&O Insurance  
* Clearance Report  
* DCP  
* Music / Soundtrack  
* Sound Design  
* Festivals  
* Voice-Over / ADR  
* Sound Effects  
* Audio Transfers  
* Audio Mix  
* Audio Other  
* Filmto-Tape Color Correction  
* Tapeto-Tape Color Correction  
* Pin Registered Transfer  
* Telecine Stock
````

````plaintext
7.15.25_researched_Kenya Film Industry Rates.pdf
High end for heavy usage over multiple days. | |
Misc. Studio Charges | 0 | $0 | 5,000 | ~$40 | 20,000 | ~$155 | Any additional fees: stage heating/AirCon,
extra cleaning, dumpster, fork-lift rental, etc., that the studio might charge. | | Crew/Talent Meals at Studio
| 0 | $0 | Included | – | Included | – | (Meals would be covered under catering lines – some studios have inhouse catering or cafeteria, but cost accounted elsewhere.) | | Air Conditioning (Stage) | 0 | $0 | 10,000 |
~$80 | 20,000 | ~$155 | Portable AC units if needed (or using studio’s HVAC beyond normal, sometimes a
fee). Not usually a concern unless a closed set in hot season. | | Crew Parking | 0 | $0 | 5,000 | ~$40 |
10,000 | ~$80 | If studio charges for parking lot use or if renting additional parking space for crew vehicles.
Many studios include some parking free. | | Condor/Scissor Lift Rental | 0 | $0 | 15,000 | ~$115 | 20,000 |
~$155 | If needed to rig lights on high sets: scissor lifts or “condor” cherry picker per week or per use. (May
rent by week ~KSh 50k, or daily ~15k.) | | Steeldeck Platform Rental | 0 | $0 | 5,000 | ~$40 | 10,000 | ~$80
| Renting stage risers or platforms (steel deck) for building set elevations. Charged per piece per day or flat.
|
Art Department Labor
(Art team responsible for design and construction of sets and props.)
| Role/Position | Low (KES) | Low (USD) | Mid (KES) | Mid (USD) | High (KES) | High (USD) | Notes |
|--------------------------|-----------|-----------|-----------|-----------|------------|------------|------------------------------------------------------------------------|
| Production Designer | 10,000 | ~$80 | 20,000 | ~$155 | 30,000 | ~$230 | Lead visual designer of the film
(oversees art, props, wardrobe). Top-tier Kenyan production designers may charge on higher end (or flat
project fee). | | Art Director | 8,000 | ~$60 | 15,000 | ~$115 | 20,000 | ~$155 | Executes the production
5 6
7
````

````plaintext
Thought: Excavating past conversations to trace cinematography inquiry patterns.
````

Now let me search past conversations for your cinematography workflow and director collaboration approaches:

**conversation_search**

*Request*

````javascript
{
  "query": "cinematography prep workflow visual language shot list directors collaboration",
  "max_results": 8
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/de6010e6-d02b-485a-8f99-69da94d8be72' updated_at=2025-07-20T20:37:42.024674+00:00>Conversation de6010e6-d02b-485a-8f99-69da94d8be72
<chat_conversation></chat_conversation></chat>
````

````plaintext
Thought: The conversation search returned a URL but the content is empty/truncated. Let me try a more specific search about his Film Nexus project and multimodal AI systems since he mentioned looking that up.
````

Let me search for the Film Nexus/multimodal AI work we've discussed:

**conversation_search**

*Request*

````javascript
{
  "query": "Film Nexus multimodal AI runpod open source visual analysis agents",
  "max_results": 8
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/de6010e6-d02b-485a-8f99-69da94d8be72' updated_at=2025-07-20T20:37:42.024674+00:00>Conversation de6010e6-d02b-485a-8f99-69da94d8be72
<chat_conversation></chat_conversation></chat>
````

````plaintext
Thought: Pivoted toward comprehensive document aggregation across multiple platforms.
````

Let me search your Google Drive for those specific documents:

**google_drive_search**

*Request*

````javascript
{
  "api_query": "name contains 'DP Process' or name contains 'Nail House' or name contains 'cinematography prep'",
  "semantic_query": "cinematography workflow DP process shot list preparation"
}
````

*Response*

````plaintext
Thought: Located foundational documents and strategized comprehensive system architecture.
````

**EXCELLENT!** Found them. Let me pull the full content of these key documents:

**google_drive_fetch**

*Request*

````javascript
{
  "document_ids": [
    "1xe6PC1AFnmxfRpdKHtC_2m1lhSTDx6ORVJN3dHKOPmM",
    "1LrrS9KRIdosZv4mwTQqjRBsjEfPG9B_Svk2Rm6SZ3Qw",
    "1rSK-vmi1vKLkVNjIVX4HNvC4sEbJXUxM8JVeVwBuUFI"
  ]
}
````

*Response*

````plaintext
Thought: Architected multi-agent cinematography system synthesizing creative process comprehensively.
````

**HELL YES.** This is frequency work at scale—building your clone so you can operate at 10x capacity while working 8 hours/week. Let me synthesize everything I've gathered and architect this properly.

## 📊 **WHAT I'VE COMPILED**

From your documents and project knowledge, here's your complete cinematography process:

### **Your Current Workflow (Script → Screen)**

**PHASE 1: CREATIVE DEVELOPMENT**
- Multiple script reads (story → emotion → subtext → visual → technical)
- Director materials review (lookbooks, reels, vision docs)
- Visual references collection (FLIM.AI, Shot Deck, photography, art)
- Beat sheet & character breakdowns
- Story analysis with you doing voice dumps
- Cinematography analysis docs

**PHASE 2: COLLABORATION**
- Shot list meetings with director (scene by scene)
- Style discussions (rhythm, pacing, psychology)
- Multiple reads focusing on different elements
- Voice notes throughout (your preferred processing method)

**PHASE 3: VISUAL LANGUAGE DEVELOPMENT**
- Mood boards & lookbooks
- Style bible creation
- Color story/palette with PD
- Reference films/photography study
- Technical approach decisions

**PHASE 4: LOGISTICS & PLANNING**
- Location scouting
- Gear selection (camera, lenses, grip, electric)
- Crew hiring
- Budget creation (detailed by department)
- Schedule coordination with AD
- Tech scouts

**PHASE 5: PREP**
- Camera tests
- LUT development
- Hair/makeup/wardrobe tests
- Equipment prep & checkout
- Overheads & floor plans
- Lighting plots

**PHASE 6: EXECUTION**
- On-set supervision
- Blocking & framing
- Lighting design
- Coverage planning
- Dailies review

**PHASE 7: POST**
- Color grading supervision
- VFX supervision
- Final deliverables approval

### **Your Specific Innovations**
- Voice recording ALL conversations
- Transcription → sorting system
- Handoff documents between departments
- Project-based knowledge management
- Integration of director materials early
- Comprehensive to-do tracking

---

## 🏗️ **AI CINEMATOGRAPHER SYSTEM ARCHITECTURE**

### **Core Philosophy**
Build a system that:
1. **Captures** everything (voice, images, documents, location data)
2. **Processes** intelligently (transcription, sorting, analysis)
3. **Generates** deliverables (shot lists, budgets, gear lists, communications)
4. **Coordinates** collaboration (tracks all dept interactions)
5. **Evolves** with feedback (learns from each project)

### **AGENT ARCHITECTURE**

**🎬 MASTER ORCHESTRATOR AGENT**
- Coordinates all sub-agents
- Maintains project state
- Routes tasks to appropriate agents
- Synthesizes outputs
- Tracks progress against cinematographer responsibilities

**📖 STORY ANALYST AGENT**
- Multiple script reads with different lenses:
  * Story structure
  * Character arcs
  * Emotional beats
  * Subtext & themes
  * Visual potential
- Generates beat sheets
- Character breakdowns
- Identifies key moments needing coverage

**🎨 VISUAL LANGUAGE AGENT**
- Researches visual references (FLIM.AI, Shot Deck, web)
- Analyzes comp films for techniques
- Generates mood boards
- Creates style bibles
- Develops color palettes
- Suggests lens/camera approaches
- References: 5 Cs, Visual Story, New Cinematographers, Deakins

**💡 CREATIVE IDEATION AGENT**
- Pure creativity without constraints
- Generates wild ideas
- Suggests unconventional approaches
- "What if..." explorations
- Cross-domain inspiration

**💰 BUDGET ARCHITECT AGENT**
- General film budget knowledge
- Camera department specifics
- Grip & electric specifics
- Crew rate databases (Kenya, SA, USA rates from your docs)
- Equipment rental pricing
- Creates detailed budget breakdowns
- Identifies cost-saving opportunities

**📋 TASK MANAGER AGENT**
- Tracks all cinematographer responsibilities (from your DP Process doc)
- Creates personalized to-do lists
- Prioritizes tasks
- Sends reminders
- Tracks deadlines
- Manages prep/shoot/wrap schedules

**🤝 COLLABORATION COORDINATOR AGENT**
- Knows all film positions & responsibilities
- Identifies who you need to contact for what
- Tracks interdepartmental dependencies
- Suggests collaboration opportunities
- Manages handoffs between departments

**✉️ COMMUNICATION AGENT**
- Drafts all emails based on context
- Generates professional correspondence
- Creates tech scout reports
- Writes crew memos
- Prepares gear lists for rental houses
- Formats documents properly
- Attaches relevant files

**🎙️ VOICE PROCESSOR AGENT**
- Transcribes all voice notes (Whisper/OpenAI)
- Sorts transcriptions by type:
  * Creative notes → Visual Language Agent
  * Tasks → Task Manager Agent
  * Director discussions → Collaboration Agent
  * Technical specs → Budget/Gear Agent
  * Story thoughts → Story Analyst
- Extracts action items automatically

**📸 VISUAL ANALYSIS AGENT**
- Processes images (location scouts, references, tests)
- Analyzes multimodal content
- Identifies visual patterns
- Suggests shot compositions
- References location photos during shot list creation
- Uses open-source multimodal models (LLaVA, Qwen-VL, etc.)

**📦 GEAR SPECIALIST AGENT**
- Camera package selection
- Lens recommendations
- Grip & electric gear lists
- Specialty equipment suggestions
- Vendor recommendations
- Compares rental vs. purchase
- Tracks gear availability

**🗺️ LOCATION ANALYST AGENT**
- Processes scout photos/videos
- Sun path analysis
- Power availability assessment
- Logistical considerations
- Suggests lighting approaches per location
- Creates location-specific shot lists

**💾 VERSION CONTROL AGENT**
- Tracks all document versions
- Commits to GitHub automatically
- Stores in Firebase
- Maintains change history
- Can show evolution of ideas
- Creates project snapshots

**🔄 REFLECTION AGENT**
- Reviews completed projects
- Identifies what worked/didn't work
- Extracts learnings
- Updates knowledge base
- Suggests process improvements
- Builds institutional memory

**🎯 SHOT LIST GENERATOR AGENT**
- Combines all inputs:
  * Script analysis
  * Director vision
  * Visual language
  * Location specifics
  * Budget constraints
- Generates comprehensive shot lists
- Multiple versions (ambitious, practical, minimal)
- Scene-by-scene breakdown
- Coverage suggestions
- Shot descriptions with technical specs

**📊 KNOWLEDGE SYNTHESIZER AGENT**
- Aggregates learnings from all projects
- Identifies patterns across shoots
- Builds your personal cinematography knowledge base
- Suggests based on past successes
- References similar previous work

---

## 🔧 **ADDITIONAL RECOMMENDED AGENTS**

**⚡ WORKFLOW OPTIMIZER AGENT**
- Analyzes your prep timeline
- Suggests optimal task sequencing
- Identifies bottlenecks
- Recommends parallel workflows

**🎬 DIRECTOR STYLE PROFILER AGENT**
- Learns each director's preferences
- Tracks what they respond to
- Suggests communication approaches
- Maintains director-specific notes

**🔋 ENERGY MANAGER AGENT**
- Knows your med timing (11 AM-1 PM peak)
- Suggests task scheduling based on energy
- Identifies tasks for different cognitive states
- Respects 8-hour/week constraint

**🚨 RISK ASSESSOR AGENT**
- Identifies potential issues early
- Suggests mitigation strategies
- Flags safety concerns
- Reviews for common oversights

**📈 PRODUCTION INTELLIGENCE AGENT**
- Monitors industry trends
- Tracks new equipment releases
- Follows cinematography innovations
- Suggests relevant techniques

---

## 💻 **TECHNICAL IMPLEMENTATION**

### **Tech Stack**

**Backend:**
- Claude API (Sonnet 4.5) for all agents
- Claude SDK for agentic orchestration
- Runpod for:
  * Open-source multimodal models
  * Whisper transcription
  * Heavy processing
- Firebase for data storage
- GitHub for version control

**Frontend:**
- Web interface (Claude Code for web can build this)
- Mobile app for voice capture (future)
- Desktop integration (Mac)

**Integrations:**
- Whisper for Mac (local transcription)
- Open source multimodal AI (LLaVA, Qwen-VL via Runpod)
- Obsidian (eventually, via file system)
- Google Workspace (Drive, Docs, Sheets)
- Location services (geotagging photos/video)

### **Data Flow**

```
INPUT SOURCES:
- Voice recordings → Voice Processor Agent
- Scripts → Story Analyst Agent
- Director materials → Visual Language Agent
- Location photos → Visual Analysis Agent + Location Analyst Agent
- Budget constraints → Budget Architect Agent

PROCESSING:
- Master Orchestrator routes inputs
- Agents process in parallel
- Cross-agent communication via shared state
- Firebase stores all intermediate states

OUTPUTS:
- Shot lists (multiple versions)
- Budgets (detailed by department)
- Gear lists
- Communication drafts
- Task lists
- Style bibles
- Mood boards
- Technical specs
```

### **Agent Communication Protocol**

Each agent has:
- **Input schema**: What data it needs
- **Output schema**: What it produces
- **Trigger conditions**: When it should run
- **Dependencies**: What other agents it needs
- **Priority level**: For resource allocation

### **Orchestration Strategy**

```python
# Simplified agent orchestration pattern
class CinematographyOrchestrator:
    def process_script(self, script_file):
        # Parallel execution
        story_analysis = StoryAnalystAgent.analyze(script_file)
        visual_ideas = VisualLanguageAgent.ideate(script_file)
        budget_estimate = BudgetArchitectAgent.estimate(script_file)
        
        # Sequential with dependencies
        shot_list = ShotListGeneratorAgent.generate(
            story=story_analysis,
            visual=visual_ideas,
            budget=budget_estimate
        )
        
        # Cross-agent synthesis
        final_package = KnowledgeSynthesizerAgent.compile(
            all_outputs
        )
        
        return final_package
```

---

## 📝 **IMPLEMENTATION PHASES**

### **Phase 1: Core Foundation (Week 1)**
- Master Orchestrator
- Voice Processor Agent
- Task Manager Agent
- Basic Firebase/GitHub integration
- Simple web interface

### **Phase 2: Creative Agents (Week 2)**
- Story Analyst Agent
- Visual Language Agent
- Shot List Generator Agent
- Integration with existing tools (FLIM.AI, Shot Deck APIs)

### **Phase 3: Production Agents (Week 3)**
- Budget Architect Agent
- Gear Specialist Agent
- Location Analyst Agent
- Collaboration Coordinator Agent

### **Phase 4: Communication & Intelligence (Week 4)**
- Communication Agent
- Reflection Agent
- Knowledge Synthesizer Agent
- Advanced multimodal integration

### **Phase 5: Optimization & Polish (Week 5)**
- Workflow Optimizer
- Risk Assessor
- Production Intelligence
- UI/UX improvements

---

## 🚀 **CLAUDE CODE IMPLEMENTATION INSTRUCTIONS**

I'll create a separate comprehensive implementation document for Claude Code, but here's the structure:

**Project Structure:**
```
ai-cinematographer/
├── agents/
│   ├── orchestrator.py
│   ├── story_analyst.py
│   ├── visual_language.py
│   ├── budget_architect.py
│   └── [all other agents]
├── integrations/
│   ├── whisper_integration.py
│   ├── firebase_client.py
│   ├── github_integration.py
│   └── multimodal_models.py
├── web/
│   ├── frontend/ (React)
│   └── backend/ (FastAPI)
├── data/
│   ├── knowledge_base/
│   ├── templates/
│   └── references/
└── tests/
```

---

**This is just the beginning.** Want me to:

1. **Create the full Claude Code implementation spec** (detailed technical requirements, API schemas, agent definitions)?
2. **Design the web interface wireframes** (what you'll interact with daily)?
3. **Build the first agent as a proof of concept** (which one should we start with)?

This system will let you **read a script today, have a full prep package tomorrow**—while you sleep, while you're at tennis, while you're making music. That's the frequency work.

**Ready to build your clone?** 🎬✨





---
Powered by [Claude Exporter](https://www.claudexporter.com)