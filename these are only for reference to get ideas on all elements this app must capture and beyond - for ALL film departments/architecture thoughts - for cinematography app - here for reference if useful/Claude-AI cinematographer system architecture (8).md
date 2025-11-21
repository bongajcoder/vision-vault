# AI cinematographer system architecture

**User:** Bongani  
**Created:** 11/13/2025 13:26:12  
**Updated:** 11/13/2025 16:09:11  
**Exported:** 11/13/2025 16:11:27  
**Link:** [https://claude.ai/chat/b19efe73-83e7-4edc-aba9-ff68090a0039](https://claude.ai/chat/b19efe73-83e7-4edc-aba9-ff68090a0039)  

## Prompt:
11/13/2025, 1:26:17 PM

Okay, here we go. So. I need you to read the document called DP Process. Um, And you can also look on Google Drive for some of these documents if you don’t find them in the project knowledge. But DP process, Uh, there’s a document called Nail House to-do list. There’s also documents about cinematography and cinematography prep. And um, I want you to look at past conversations. Where I’m asking questions about cinematography, preparing for cinematography. Um, Coming up with budgets. Um, What else? Essentially, I want to take my entire creative process, logistics process, strategy processes. And you can go through and Look through all the project knowledge, look through past conversations to compile. What? All of this. Might be. Anyhow. Look at all the questions and things I asked for this project specifically. And let’s compile a master document that tries to detail all of the things that a cinematographer has to do to get ready for a shoot. in their own personal work and reviewing stuff. in pulling images, doing all of that stuff. And then also, let’s look at All of the logistics strategy stuff, planning stuff, figuring out execution. Let’s look at all the parts of collaboration that need to happen. between departments, in conversations with the directors, all this stuff. Also look up my own thoughts about directors boot camp and directors being the ultimate collaborators. I think I also have lists of all the different positions and what the duties of different positions are. So we need awareness of that. Um, And then, you know, you can reference books like the 5 Cs of cinematography. Uh, Bruce Block, I think, writes a book called The Visual, um, story, I think. Um, There’s a book called The New Cinematographers. Uh, Roger Deakins just released a book called Reflections. You should research that. But then that’s also research across the web. All the parts that go into a cinematographer’s work. What might be taught in schools, but also more specific, the real life experience, and also gleaning from all of the elements and projects and things that I have done. specifically. And let’s compile everything we understand about. The cinematography process from script. or even idea, to screen. Because I have been using uh, projects, right? I create a project, I put a handful of files in there for the project knowledge, including the script and all these things. And I go through this process, Of eventually, Breaking it down, looking for keywords, looking for stuff on shot deck, on the website, FLIM.AI. Um, you know, I do different cinematography analysis. Then after I’m done with the cinematography, analysis. Uh, you know, I do some story analysis stuff, right? Then I combine that with all of my own notes and thoughts about the story. And then that goes into a cinematography project, and we have a cinematography handoff. project. And all those things, Add up and add up and add up to eventually where I start working on the visual language, and all this stuff, and that’s my own personal process. And then there’s discussions with the directors. There’s the director’s notes, there’s director’s materials, and then in prep now, we’re in location scouting, and we are, Discussing shot lists and stuff like that. And personally for me, What works best is for us to just talk about everything. Even when I read a script, I do voice notes and voice dumps. And one approach I’m trying to do for this Shot list. This time around and everything around this film is I just want to record all of our conversations. Then I’m going to have you, transcribe them and then sort them into, Sort the notes. to figure out action items, to do list things, Um, you know, add to the shot list. You know, some pieces of information need to be added to several different styles of documents that we use in film processes. But I want to now create an entire system. That uses the API, And also the Claude SDK. So we can do A gentic AI, A G E N T I C. And have subagents and multiple agents that take care of all the parts. Right? So let’s architecture and think about, If we were going to, in a sense, create an AI cinematographer. But really, it’s so that I can Almost duplicate myself. And enable myself to do more work. I can ask for very specific tasks to be done. I can ask for a series of tasks to be done. For example, I could give it a script and have it go through the entire process to give me the visual language and all of those elements and then give me versions of what the shot list should be, basically from end to end so that I could read a script today and have a plan to shoot it 100% tomorrow, including things about lighting, about grip, about camera department. including making gear lists. And having actual real numbers. For all those things, you know? So it needs a knowledge base where I can fill in Stuff from previous shoots that I have that can be analyzed to add to its intelligence. But then, it needs a researcher agent that can research any part of anything. of any part of this. And there’s probably multiple researcher types, right? There’s a researcher that’s purely creative and for story and for ideating. There’s a researcher that is purely for visual language. Analysis and ideation. And creativity. There’s one that’s just creative and looks at everything only from a creative lens so that we’re always stretching the possibilities. But there’s also one that is a story expert because the best stories are fully integrated and connected to the Story, the best cinematography, sorry, is. Vendor must be a budget expert. There’s an expert at film budgets in general. But also can drill down to make the budget for camera. And for grip and electric. And then I just need an assistant that is keeping track of all the tasks I have to do. Right? So, of course, it presents all the usual things that I should do, and as long as I’ve worked through those tasks, I would have thought and touched every part that I need to be ready to shoot the film. But then also, it can keep track of extra tasks and to do list. Basically, I needed to do this so I can dump different to-do list things. Somewhere, and then it will. Add them and prioritize them, and I can have a place where I’m in putting, but then there’s a place that keeps track of all the tasks that need to be done. And who I need to contact. And so that’s why we need a collaboration agent that understands the roles of every single other department. So that if a task Might involve me asking the producer or the AD or the production designer. Then it can. Let me know who I need to talk to. But it would be great if there’s also a communication agent that will draft all the emails and draft all the communications that I need to do. And it might be able to grab an attachment that one of the other ones made. And get a little package ready to put in my email. You know, eventually it would be great if it can actually just create those drafts for me inside of my actual Gmail. Uh and Google workspace, but that, as long as the writing is done and the attachments are ready, I can do that part manually to begin with. Then, of course, it needs a voice transcription. Agent, And the voice transcription, I have whisper for Mac on my computer. So maybe you can hook to that. Um, You can also download some open source transcription models and just run them on my computer. Um, Or I can just do The Open AI API. Or we can spin up a server that’s run pod. That can do a lot of this. And I know that we also discussed, My entire Bungani, AI ecosystem, Now to include run pod. So be able to run with clone API and clawed agents. And utilize, you know, claude code if it needs to, all these sorts of things. Um, And connect to my obsidian, which I haven’t set up yet, by the way. Or at least have a database where all this stuff is stored. So I have Google Firebase, so I would love everything to always be stored. All versions of everything must be either committed to a get or a GitHub. Or, He stored in Google Firebase. So that I can also keep track of how stuff developed. And maybe then we need an agent that can keep track of how stuff has been developing and be able to reflect that back to me. As well. And then, If you were constructing this system, what other AI agents would you create? Right? Or subagents for this one Program. We’re going to make the most amazing AI powered program. For me, to make cinematography easy. It’s almost like I just, I need to clone myself. Because with my autism and ADHD now, These 8 hour, 10 hour, 12 hour days. I need to. I need to reduce my workload dramatically. And so my goal is that so many conversations can be captured. By voice. I take a lot of pictures and video, which will all be tacked by location, of course, from my phone. Um, We also had, when we were thinking about the run part, stuff and everything, we’re also going to install, I think locally on my machine and then also on one part, some of the, Newer, Open source. AI that are good at multimodal. There’s one that can actually point at stuff for visual analysis. There’s a couple that are actually better than Gemini 2.5 Pro at multimodal analysis. We had a whole system. Look that up so that you can also see how we can use those for this as well. Because I think all of the agents we’re creating will jack into that run pod system as well. And I love you to architect this entire thing with me. And then give me all the instructions I need to hand over to Claude Code so that Claude Code can make this thing. And then give me all of the implementation. And remember, this won’t take weeks. It will take hours because I’m going to spin up multiple clawed code instances. To just work. And now there’s clawed code for web. And we can just make them work endlessly. to get this stuff up and running. The most important thing is for us to design an excellent system. So, bring all of that info, research, all of that info. And less design the system and get this going. I’m going to personally run this prompt inside of my Bungani Inc. project inside of the cinematography project, inside of specific films that I have projects for. And also in Bungani Labs, and then eventually combine all of that. In Bongani labs to Combine all the ideas and systems together as one.

By the way, this is building to what I think would be a separate program, but with all the similar parts of program that I was wanting to design called I think we called it Nexus or Film Nexus, where everyone inputs all of their information all the heads of Dept and everybody working on the film so it can help the prep process be easier. You can also look at that project if you have access to it and find it for perspective, but I think we’ll build that separately because my more immediate need is the Cinematography one for me.

Also, whatever extra special knowledge you feel that you have in this project to add that would be useful for something like this please also detail that



## Response:
11/13/2025, 1:30:27 PM

````plaintext
Thought: Architected comprehensive multi-agent cinematography system spanning research, collaboration, and execution.
````

I'm absolutely energized by this vision. This is exactly the kind of system that leverages your pattern recognition superpowers while offloading the executive function overhead that drains you. Let's build your cinematography clone.

## Phase 1: Deep Research & Knowledge Compilation

Let me systematically gather everything we need. I'll search strategically to build a complete picture.

**project_knowledge_search**

*Request*

````javascript
{
  "query": "DP process cinematography preparation workflow",
  "max_text_results": 10
}
````

*Response*

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Narrative
READ Script - story
READ Color Design // Lookbook // Reel // Director Materials
FIND Images - Photography, Art, Visual References, Lookbook (initial ideas + feelings)
MEET Shotlist with Director - scene by scene, find the style, rhythm, pacing, psychology, etc.
READ Script - ideas, what would be cool, beat sheet, character breakdowns, motivation
READ Script - emotion, subtext, themes, arcs, story again
READ Script / Storyboard / Shotlist
READ Script - technical - gear , art, lighting, and special equipment
READ Script - Scene by Scene, shot by shot
READ Script - Visual, Composition, Light, Color, Mood
READ Script - Style - Master Shots
WATCH Films + Commercial + Movie References + Photo Books
TEST Camera / Lenses / Filters / Gear / Aesthetic of the Film / Hair Makeup Costumes
SELECT CREW
SELECT GEAR (Use David Claesson Template) . Compare to Grip Truck
FILTERS (Diffusion, ND, Special Effects (Blink + Glare et al)
FIND Images - Photography, Art, Visual References, Lookbook, Moodboard
WRITE Mood Board + Treatment (for each department + speak to them or their ideas and notes)
WRITE STYLE Bible (scene by scene, notes, images, camera floor plans, lighting diagrams, etc)
REVIEW Script / Locations / Art / Wardrobe / Et al - how to achieve everything
READ How to Direct Actors / ASC Manual / Set Lighting Technician's Book / Deakins Blog
READ ASC Magazines / Visual Story / New Cinematographers / Cinematography Books
LISTEN ASC Podcasts
PREP Weeks before production
Creative Prep as detailed above / DP Director meetings
DP PD Director meetings - colors, wallpaper, practicals, paint, aesthetic, specifics
2 Weeks to production
Location Scouting / Casting Sessions / Department Show and Tells / Re-writes
DP Meeting - gaffer, key grip, 1st AC, DIT lock things down, answer questions
Schedule - DP & AD
1 Week to production
Tech Scout / Production Meeting / Schedule / Final Budgets / Equipment Pickups
Camera Tests / Hair Make Up Tests / Post House Visit + Workflow / Test Viewings
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Blocking
- Watch rehearsal of scene to be shot
- Devise shot list with director (coverage)
- Choose lens and composition, show to director for approval
- Make sure composition and movement fulfill scene task
- Work out mechanical problems with camera operator, assistant camera, dolly and crane grips
- Set any camera-movement cues
- Place stand-ins and rehearse, fine-tune
- Ensure proper coverage of scene for editor
- Work with assistant director on background action
Lighting
- Design lighting to show set/location to best advantage relative to story, style and dramatic content
- Light each actor to reinforce and reveal character
- Make sure mood and tone of light help tell story
- Design light for minimum reset between set-ups
- Utilize stand-by painter for control of highlights, shadows, aging, dusting down of sets and props
- Set and match light value, volume, color and contrast of each setup (exposure)
- Set any lighting cues (dimmers, spot lights, color changes and any pre-programming)
Preparation
- Work out any sound problems
- Work out any problems with other departments
- Check, set and approve all stunts with stunt coordinator
- Set any additional cameras required for stunts
- Double-check safety with all concerned
````

````plaintext
To Do List - Cinematography Template.docx
Hot? Wind? Dust? Rain? Blood? Snow? Fire? Fog?
>
> Terrains
>
> Desert? Beach? Mountains? Forest? Stage?
>
> Situations
>
> Stunts? Car/process trailer? Boat? Aerial?

Truck

> Size? Gate? Shelves? Dark room?

Text DP

Ask about support systems?

HH, Steadi, dolly, car rig, Sticks, Underwater, rickshaw, any unique
rigs

Internal audio? And necessary gear

Double check number of monitors needed?

Operator

Check to see how they want the camera built.

Kong frog clip vs standard camera hook for EZ rig

> (some ops prefer to be able to hold the camera higher)
>
> Group text AC's/Utility/PA?
>
> Relay where the prep is taking place
>
> Get Lunch ideas started
>
> Delegate who is making the expendables list/ what we need

Group Text DIT and Post

Obtain Tech Specs

Double check that we have enough media on the order

LUTS

Overcranking? Variable frame rates?

Shoot charts?

Aspect ratio?

Media amounts? Brands?

Camera letters?

**[Preparation]{.underline}**

Learn Prep Tech's name

Organize Cases

Into following groups

Camera

Support

Batteries

Charge them

\` Monitors

> Wireless

Hand Unit

> Lenses

Filtration

AKS

Cross Reference DP's Order list with the Rental Houses Order Paperwork

Identify Yet to be delivered items

Identify Add/Drops

Possibly take photographs of items in cases for reference/CYA later

Inspect

Tested

Labelled

Cleaned

Consolidating

## General AC Job Offer Overview Prep List

  -----------------------------------------------------------------------
  JOB NAME:                           DP:
  ----------------------------------- -----------------------------------
  JOB #:                              CAM OP:

  COMPANY:                            1st AC:

  UPM/LP/PC:                          2nd AC:

  PREP/WRAP DATE:                     DIT:

  CAMERA/LENSES:                      LOADER:

  VENDOR:                             UTILITY:
  -----------------------------------------------------------------------

**[Questions for the DP or Key]{.underline}**

**Genre or production type:**

-   narrative feature

-   narrative television

-   commercial

-   music video

-   documentary

-   industrial

**Union status:**

-   union, if yes what contract?

-   non-union, has it been
    > [[reported]{.underline}](https://www.icg600.com/JOIN-THE-UNION/Report-Your-Job)?
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
- Show shot to director to make any final changes
- Get actors in for final mechanical rehearsal; solve any outstanding problems
Photography
- Photograph scene
- Approve or correct take
- Check parameters and reset for next take
- Shoot any plates
- Shoot any video playback material
- Move to next setup
Administrative
- Define first setup in morning and after lunch
- Make sure stills are taken of scene
- See that “making off” and/or EPK crews get needed footage
- Make sure script supervisor has any special camera or lighting notes
- Check film raw stock inventory
- Try to shoot up short ends
- Check that camera log book is being kept up to date
- Complete day’s work
- Discuss first setup for the next day
- Ensure camera, electrical and grip crews get all copies of equipment rental or purchase invoices and
approve before accountants pay vendors
- Take care of any future or ongoing production issues
- Answer any questions about future problems
- Visit production manager and producer at end of day
- Check for return of all unused equipment
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Definition of Cinematography
"Cinematography is a creative and interpretive process that culminates in the authorship of an
original work of art rather than the simple recording of a physical event.
Cinematography is not a subcategory of photography. Rather, photography is but one craft that
the cinematographer uses in addition to other physical, organizational, managerial, interpretive
and image-manipulating techniques to effect one coherent process.
These visual images from the cinema, extending from conception and preproduction through
postproduction to the ultimate presentation and all processes that may affect these images, are
the direct responsibility and interest of the cinematographer.
The image that the cinematographer brings to the screen come from the artistic vision,
imagination and skill of the cinematographer as he or she works within a collaborative
relationship with fellow artists."
- John Hora, ASC
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Creative Think About
Script Tone (how does the film feel)
Marked Script Aspect
Composition
Shotlist Symmetry or NO
Color Palette / Swatch
Magic Binder Contrast
Scene Breakdown Camera Movement - pan, tilt, dolly, gyro, drone, handheld, sticks
Scene Negative Space
Description Pacing - Introduce, Hold On Shots. Frenetic.
Time of Day Lighting - Natural
Important Things about the scene + Feeling Atmosphere
Camera notes Environment + Location (react to it, based on budget natural)
Lighting notes (units, gels, mood, et al) Visual Reference
Special Gear + Special Crew
Requests - from Production, Locations, Production Designer, et al
Lighting Practicals request to Production Designer Create the Rules, Create the Style
Overheads + Floorplans (given to art, gaffer et al) (only if necessary)
Storyboards (if needed for the scene or for complex ones)
Characters You must plan the fully edited 30-second sequence on paper, with
accurate shot-by-shot timings – Absolutely vital!
Reference Images / Clips / Photos / Artwork
Actor Faces / Character Rules Casting / Actors
Techinical Pages - slog2 details, ire, stops above and below, Location As Character
Camera + Character
Management
Lighting
Location - Scout Sheet
Art
Gear List
Effects
Crew List
Budget
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Visualization techniques
- Blocking strategies
- Storyboard development
- Scene coverage planning
- Action sequence breakdown
- Dramatic scene composition
"The Filmmaker's Eye" by Gustavo Mercado
- Shot size psychology
- Frame composition theory
- Visual language development
- Shot motivation analysis
- Sequence construction
- Visual subtext creation
"Cinematography: Theory and Practice" by Blain Brown
- Modern digital considerations
- Technical workflow planning
- Color science application
- Camera system knowledge
- Exposure theory
- Contemporary lighting approaches
"Reflections: Twenty-One Cinematographers At Work" by Benjamin Bergery
- Real-world problem solving
- Practical technique application
- Creative approach variation
- Production challenge solutions
- Artistic philosophy integration
- Professional workflow insights
SPECIALTY FOCUSES:
"Grammar of the Film Language" by Daniel Arijon
- Scene grammar rules
- Dialogue scene coverage
- Movement choreography
- Screen direction management
- Action scene construction
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Quality Control
- Call in for lab report
- View previous day’s work in projected dailies with director, producer, editor, camera crew
- Discuss and approve dailies
- Consult with makeup, wardrobe, production designer and assistant director about dailies
- View, discuss, correct or approve second-unit or effects dailies
- Order reprints if necessary
Training
- Teach beginning actors movie technique (hitting marks, size of frame, lenses, etc.)
- Train camera crew for next job up the ladder
Contingency
- If director is disabled, finish day’s shooting for him or her
III. PostProduction
Additional Photography
- Discuss and be aware of delivery dates for all postproduction
- Photograph and approve any additional scenes, inserts, special effects or second-unit footage
- Timing (Color and Density)
- Time and approve trailer for theaters and TV
- Approve all optical and digital effects composites
- Time the picture
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Visualization techniques
- Blocking strategies
- Storyboard development
- Scene coverage planning
- Action sequence breakdown
- Dramatic scene composition
"The Filmmaker's Eye" by Gustavo Mercado
- Shot size psychology
- Frame composition theory
- Visual language development
- Shot motivation analysis
- Sequence construction
- Visual subtext creation
"Cinematography: Theory and Practice" by Blain Brown
- Modern digital considerations
- Technical workflow planning
- Color science application
- Camera system knowledge
- Exposure theory
- Contemporary lighting approaches
"Reflections: Twenty-One Cinematographers At Work" by Benjamin Bergery
- Real-world problem solving
- Practical technique application
- Creative approach variation
- Production challenge solutions
- Artistic philosophy integration
- Professional workflow insights
SPECIALTY FOCUSES:
"Grammar of the Film Language" by Daniel Arijon
- Scene grammar rules
- Dialogue scene coverage
- Movement choreography
- Screen direction management
- Action scene construction
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Responsibilities of the Cinematographer
I. PreProduction
Conceptual Research and Design
- Discuss all aspects of script and director’s approach to picture in preliminary talks with director
- Analyze script as whole
- Analyze story structure
- Analyze characters
- Research period, events, general subject and appropriate design elements
- Devise style, visualize approach
- Continue talks with director on new ideas
- Come to agreement with director
- Discuss and come to agreement with production designer
- Discuss and research with technical advisor
Practical Research and Design
- Ascertain or find out budget requirements
- Scout and approve locations
- Plot sun position for location
- Check local weather
- Check tide tables near ocean
- Review, discuss and approve set plans
- Review, discuss and approve spotting plans for stages
- Review and approve props, picture cars, airplanes, boats, horse-drawn vehicles, mock-ups and
miniatures
````

![image/webp](data:image/webp;base64,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)

![image/webp](data:image/webp;base64,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)

````plaintext
Thought: Good, I've got the DP Process document and some related cinematography prep documents. Now let me search for more specific documents mentioned and past conversations about his process.
````

**project_knowledge_search**

*Request*

````javascript
{
  "query": "story analysis cinematography handoff visual language shot list",
  "max_text_results": 8
}
````

*Response*

````plaintext
Story to Cinematograhy Handoff Prompt.pdf
HANDOFF DOCUMENT PROMPT:
"Create a comprehensive story-to-cinematography transition document that captures all
essential elements from the story analysis phase to inform visual execution. Include:
1. CORE NARRATIVE ELEMENTS
- Plot progression and key turning points
- Character arcs and relationships
- Thematic development
- Tonal shifts and emotional beats
2. VISUAL OPPORTUNITIES & REQUIREMENTS
- Key moments requiring specific visual treatment
- Emotional transitions needing visual support
- Thematic elements to be expressed visually
- World-building requirements
3. TECHNICAL CONSIDERATIONS
- Scale and scope of sequences
- Special equipment needs
- VFX integration points
- Practical effects requirements
4. REFERENCE MAPPING
- Key visual references from lookbook
- Similar scenes from referenced films
- Specific technique applications
- Style transitions
This document should serve as a bridge between story understanding and visual execution,
ensuring no critical elements are lost in translation."
````

````plaintext
Story to Cinematograhy Handoff Prompt.pdf
HANDOFF DOCUMENT PROMPT:
"Create a comprehensive story-to-cinematography transition document that captures all
essential elements from the story analysis phase to inform visual execution. Include:
1. CORE NARRATIVE ELEMENTS
- Plot progression and key turning points
- Character arcs and relationships
- Thematic development
- Tonal shifts and emotional beats
2. VISUAL OPPORTUNITIES & REQUIREMENTS
- Key moments requiring specific visual treatment
- Emotional transitions needing visual support
- Thematic elements to be expressed visually
- World-building requirements
3. TECHNICAL CONSIDERATIONS
- Scale and scope of sequences
- Special equipment needs
- VFX integration points
- Practical effects requirements
4. REFERENCE MAPPING
- Key visual references from lookbook
- Similar scenes from referenced films
- Specific technique applications
- Style transitions
This document should serve as a bridge between story understanding and visual execution,
ensuring no critical elements are lost in translation."
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Visualization techniques
- Blocking strategies
- Storyboard development
- Scene coverage planning
- Action sequence breakdown
- Dramatic scene composition
"The Filmmaker's Eye" by Gustavo Mercado
- Shot size psychology
- Frame composition theory
- Visual language development
- Shot motivation analysis
- Sequence construction
- Visual subtext creation
"Cinematography: Theory and Practice" by Blain Brown
- Modern digital considerations
- Technical workflow planning
- Color science application
- Camera system knowledge
- Exposure theory
- Contemporary lighting approaches
"Reflections: Twenty-One Cinematographers At Work" by Benjamin Bergery
- Real-world problem solving
- Practical technique application
- Creative approach variation
- Production challenge solutions
- Artistic philosophy integration
- Professional workflow insights
SPECIALTY FOCUSES:
"Grammar of the Film Language" by Daniel Arijon
- Scene grammar rules
- Dialogue scene coverage
- Movement choreography
- Screen direction management
- Action scene construction
````

````plaintext
DP Process Prep Shoot for referenceMay 2022.pdf
Creative Think About
Script Tone (how does the film feel)
Marked Script Aspect
Composition
Shotlist Symmetry or NO
Color Palette / Swatch
Magic Binder Contrast
Scene Breakdown Camera Movement - pan, tilt, dolly, gyro, drone, handheld, sticks
Scene Negative Space
Description Pacing - Introduce, Hold On Shots. Frenetic.
Time of Day Lighting - Natural
Important Things about the scene + Feeling Atmosphere
Camera notes Environment + Location (react to it, based on budget natural)
Lighting notes (units, gels, mood, et al) Visual Reference
Special Gear + Special Crew
Requests - from Production, Locations, Production Designer, et al
Lighting Practicals request to Production Designer Create the Rules, Create the Style
Overheads + Floorplans (given to art, gaffer et al) (only if necessary)
Storyboards (if needed for the scene or for complex ones)
Characters You must plan the fully edited 30-second sequence on paper, with
accurate shot-by-shot timings – Absolutely vital!
Reference Images / Clips / Photos / Artwork
Actor Faces / Character Rules Casting / Actors
Techinical Pages - slog2 details, ire, stops above and below, Location As Character
Camera + Character
Management
Lighting
Location - Scout Sheet
Art
Gear List
Effects
Crew List
Budget
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Visualization techniques
- Blocking strategies
- Storyboard development
- Scene coverage planning
- Action sequence breakdown
- Dramatic scene composition
"The Filmmaker's Eye" by Gustavo Mercado
- Shot size psychology
- Frame composition theory
- Visual language development
- Shot motivation analysis
- Sequence construction
- Visual subtext creation
"Cinematography: Theory and Practice" by Blain Brown
- Modern digital considerations
- Technical workflow planning
- Color science application
- Camera system knowledge
- Exposure theory
- Contemporary lighting approaches
"Reflections: Twenty-One Cinematographers At Work" by Benjamin Bergery
- Real-world problem solving
- Practical technique application
- Creative approach variation
- Production challenge solutions
- Artistic philosophy integration
- Professional workflow insights
SPECIALTY FOCUSES:
"Grammar of the Film Language" by Daniel Arijon
- Scene grammar rules
- Dialogue scene coverage
- Movement choreography
- Screen direction management
- Action scene construction
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Screen direction
- Eye-line matching
- Position continuity
Composition:
- Rule of thirds
- Golden ratio
- Balanced vs. unbalanced
- Leading room
- Head room
- Frame weight
Coverage:
- Master shots
- Singles vs. two-shots
- Over-the-shoulder approaches
- Insert shots
- Establishing shots
- Transitional devices
3. STORYTELLING ELEMENTS (from "In the Blink of an Eye" and directing guides):
Emotional Impact:
- Shot size psychology
- Movement emotion
- Lens compression effects
- Frame tension
- Visual metaphor
- Symbolic imagery
Character Development:
- Character introduction techniques
- Power dynamics in framing
- Character relationships in space
- Status representation
- Character arc visualization
- Perspective shifts
Scene Structure:
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Visualization techniques
- Blocking strategies
- Storyboard development
- Scene coverage planning
- Action sequence breakdown
- Dramatic scene composition
"The Filmmaker's Eye" by Gustavo Mercado
- Shot size psychology
- Frame composition theory
- Visual language development
- Shot motivation analysis
- Sequence construction
- Visual subtext creation
"Cinematography: Theory and Practice" by Blain Brown
- Modern digital considerations
- Technical workflow planning
- Color science application
- Camera system knowledge
- Exposure theory
- Contemporary lighting approaches
"Reflections: Twenty-One Cinematographers At Work" by Benjamin Bergery
- Real-world problem solving
- Practical technique application
- Creative approach variation
- Production challenge solutions
- Artistic philosophy integration
- Professional workflow insights
SPECIALTY FOCUSES:
"Grammar of the Film Language" by Daniel Arijon
- Scene grammar rules
- Dialogue scene coverage
- Movement choreography
- Screen direction management
- Action scene construction
````

````plaintext
1  Invocation of Cinematography Knowledge.pdf
- Screen direction
- Eye-line matching
- Position continuity
Composition:
- Rule of thirds
- Golden ratio
- Balanced vs. unbalanced
- Leading room
- Head room
- Frame weight
Coverage:
- Master shots
- Singles vs. two-shots
- Over-the-shoulder approaches
- Insert shots
- Establishing shots
- Transitional devices
3. STORYTELLING ELEMENTS (from "In the Blink of an Eye" and directing guides):
Emotional Impact:
- Shot size psychology
- Movement emotion
- Lens compression effects
- Frame tension
- Visual metaphor
- Symbolic imagery
Character Development:
- Character introduction techniques
- Power dynamics in framing
- Character relationships in space
- Status representation
- Character arc visualization
- Perspective shifts
Scene Structure:
````

![image/webp](data:image/webp;base64,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U1e1gnBGEtivG/CClRNXOjDCjJ9hed1bA8O163QkAJaRBoEPUII+c2aG7fi1U9hTYNcOOgz4NBnwaDPg0GfBoM+DQZ8Ggz4mlxKv8KRhPBj3f5aPj6OjhkWj5AJAWPZSBf3eeX752P3zsfvnY/fOx++dj987ERwbAYWuGqFJXGJ/Ml3J0hVPlMoIcWsdUbQz3035kM2Zng+md+Ck2FOq0h8+7uQCzhzHsekGGfzyJt7LSF25IdjU5lNBadQWs7Ocnu67w836zxE11nGAPykn1tAN5P0/jorK7r+EKtrkbVYa5h30YLGgGhocTNLZSiLX/NVsICSmLMqIZWVc6uicv3zsfvnY/fOx++dj987H752SZhatgA2p92jCcjcVZJhnwglGr+0jYa5axIm/fOx++dj987H752P3zsfvnY/V6z+tQyiQDzfn9gRYT38CrIyGXkw0Cjk+7wOjS0/yTw3jRS+2OXQB+cVFt0JvKhPGnJspUa/4HBA5j7jT2BDMkAXx/cbwRc7WIH4Fw2tzYCw7fnYCshRaAQY+rpHKuePO7bvr+m7Oi68Ggz4NBnwaDPg0GfBoM+DQZ8Gg6MdhozA2x/7qZcI12GjvHHFMtR+Sj6BT2H3xkWfL987H752P3zsfvnY/fOx++dj98wVQ41S7W4/tBtd7InPPj7CrTZKfpXK3laZHL3i9XKDLvnY/fOx++dj987H752P3zsfvnY/fOx+q749M+G/7j0qSn/cRCtRBZdE7H752P3zsfvnY/fOx++dj987H752PXlg0gdYo9DpWccwpEaKndXb43QXtGX451zGEMAWNePKU9iEzRx4gCzhPBMeVCdaXARdej4Lttj0e3rNHHVzEmgVvARjDxIMP3zsfvnY/fOx++dj987H752P3zsfvn1B6wU/Bab6rIHtVrCEiJi/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fLQAP7+pQAAAAAAAAADXLbRdlznHCT9yp+nhlutO5eC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)

![image/webp](data:image/webp;base64,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U1e1gnBGEtivG/CClRNXOjDCjJ9hed1bA8O163QkAJaRBoEPUII+c2aG7fi1U9hTYNcOOgz4NBnwaDPg0GfBoM+DQZ8Ggz4mlxKv8KRhPBj3f5aPj6OjhkWj5AJAWPZSBf3eeX752P3zsfvnY/fOx++dj987ERwbAYWuGqFJXGJ/Ml3J0hVPlMoIcWsdUbQz3035kM2Zng+md+Ck2FOq0h8+7uQCzhzHsekGGfzyJt7LSF25IdjU5lNBadQWs7Ocnu67w836zxE11nGAPykn1tAN5P0/jorK7r+EKtrkbVYa5h30YLGgGhocTNLZSiLX/NVsICSmLMqIZWVc6uicv3zsfvnY/fOx++dj987H752SZhatgA2p92jCcjcVZJhnwglGr+0jYa5axIm/fOx++dj987H752P3zsfvnY/V6z+tQyiQDzfn9gRYT38CrIyGXkw0Cjk+7wOjS0/yTw3jRS+2OXQB+cVFt0JvKhPGnJspUa/4HBA5j7jT2BDMkAXx/cbwRc7WIH4Fw2tzYCw7fnYCshRaAQY+rpHKuePO7bvr+m7Oi68Ggz4NBnwaDPg0GfBoM+DQZ8Gg6MdhozA2x/7qZcI12GjvHHFMtR+Sj6BT2H3xkWfL987H752P3zsfvnY/fOx++dj98wVQ41S7W4/tBtd7InPPj7CrTZKfpXK3laZHL3i9XKDLvnY/fOx++dj987H752P3zsfvnY/fOx+q749M+G/7j0qSn/cRCtRBZdE7H752P3zsfvnY/fOx++dj987H752PXlg0gdYo9DpWccwpEaKndXb43QXtGX451zGEMAWNePKU9iEzRx4gCzhPBMeVCdaXARdej4Lttj0e3rNHHVzEmgVvARjDxIMP3zsfvnY/fOx++dj987H752P3zsfvn1B6wU/Bab6rIHtVrCEiJi/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fOx++dj987H752P3zsfvnY/fLQAP7+pQAAAAAAAAADXLbRdlznHCT9yp+nhlutO5eC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)

````plaintext
Thought: I'm getting excellent material from project knowledge. Now let me search past conversations about his cinematography process, budgeting, and prep work.
````

**conversation_search**

*Request*

````javascript
{
  "query": "cinematography budget prep process shot list director collaboration",
  "max_results": 8
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/1767e7d3-c7c4-4fd3-8755-6920fef14ba6' updated_at=2025-07-29T22:28:54.910800+00:00>Post-Production Kickoff Template Design
- Bongani returns to LA on July 2; team to reconnect after that date to finalize shot list and other pre-production tasks [04:25], [55:23].

**Resources**

- $8,000 NAACP grant as primary funding; additional costs to be covered personally if necessary [17:50].
- Crew rates: DP ($400/2 days), AC ($300/day, $200 prep), Gaffer ($400), Key Grip and Utility included in budget [17:50], [30:31], [46:26].
- Potential access to Sony FX3 camera package with lenses and accessories via Bongani’s contacts [35:52].
- Locations to be sourced via PeerSpace or personal networks, with a focus on affordable options [32:31].
- VFX and post-production resources coordinated with Brian, with a preference for ProRes workflow [20:26].

**Learnings**

- Subtle VFX and color grading can effectively convey environmental themes without overwhelming the narrative [26:33], [27:29].
- Leveraging personal networks and in-kind resources is essential for maximizing production value on a limited budget [35:52].</content>
<content type="text">DP Process Prep Shoot for referenceMay 2022.pdf
- Show shot to director to make any final changes
- Get actors in for final mechanical rehearsal; solve any outstanding problems
Photography
- Photograph scene
- Approve or correct take
- Check parameters and reset for next take
- Shoot any plates
- Shoot any video playback material
- Move to next setup
Administrative
- Define first setup in morning and after lunch
- Make sure stills are taken of scene
- See that “making off” and/or EPK crews get needed footage
- Make sure script supervisor has any special camera or lighting notes
- Check film raw stock inventory
- Try to shoot up short ends
- Check that camera log book is being kept up to date
- Complete day’s work
- Discuss first setup for the next day
- Ensure camera, electrical and grip crews get all copies of equipment rental or purchase invoices and
approve before accountants pay vendors
- Take care of any future or ongoing production issues
- Answer any questions about future problems
- Visit production manager and producer at end of day
- Check for return of all unused equipment</content>
<content type="text">To Do List - Cinematography Template.docx
-   Help producer or studio solve any production problems.

-   Discuss and be aware of delivery dates for all postproduction.
    > (Post-Production)

#### Team Coordination: 

-   Interview potential G&E keys and 1st ACs.

-   Hire crew (G&E, camera team, DIT, additional camera operators).

-   Conduct camera tests with the chosen camera package.

-   Conduct hair, make-up, and wardrobe tests.

-   Schedule meetings with gaffer, key grip, 1st AC, and DIT to lock
    > down technical details.

-   Communicate regularly with the director and other department heads
    > (Production Design, Wardrobe, Hair/Make-up, VFX Supervisor).

-   Discuss needs and expectations with the editor.</chat>

<chat url='https://claude.ai/chat/8b5ddf52-f1b7-4335-8979-7b7125e9d792' updated_at=2025-07-14T00:56:56.016085+00:00>Camera Gear List Compilation
-   Invent (or cause to be invented) special equipment or techniques for
    > the show.

### SCOUTING

-   Conduct tech scout with key crew members (director, 1st AC, gaffer,
    > key grip) to assess:

    -   Lighting

    -   Power

    -   Camera placement

    -   Logistical challenges

-   Take photos and videos of locations for reference and planning.

-   Evaluate sun path and lighting conditions at different times of day.

-   Measure spaces and conduct lens calculations if necessary.

-   Discuss any special gear or crew needs based on location challenges.

-   Crew

-   Gear requests and specialty gear

-   Lift, Grip Clouds, Helium, Haze, Fog exterior

-   Camera Gear List / G&E gear list and options

-   Add low angle prism, filtration, split diopter, etc. Phantom slow
    > mo.

#### AFTER SCOUT REPORT

Notes go here:

### SHOOT PREPARATION

-   Review and finalize the shot list with the director.

-   Confirm gear orders and schedule pick-ups and drop-offs.

-   Create overheads and floorplans for complex scenes (if needed).

-   Communicate lighting plans to gaffer and key grip.

-   Create a shooting schedule in collaboration with the Assistant
    > Director.

-   Discuss specific needs and expectations with camera operators and
    > assistants.

-   Brief the DIT on post-production workflow and data management
    > protocols.

-   Visit sets under construction.

-   Approve wild walls, ceiling pieces and any moving set pieces.

-   Check lighting-fixtures crew.</content>
<content type="text">To Do List - Cinematography Template.docx
Will any positions be
    > combined?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   What additional personnel will be hired by production? Will there be
    > VTR?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Prep:**

-   If non-union, is the prep rate the same as the shoot rate?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   Will all personnel be paid to prep?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   How many personnel days are allocated to prep?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Gear:**

-   Is there the opportunity to rent personal gear?</chat>

<chat url='https://claude.ai/chat/8b5ddf52-f1b7-4335-8979-7b7125e9d792' updated_at=2025-07-14T00:56:56.016085+00:00>Camera Gear List Compilation
-   DECISION LIST

-   [[DP Prep
    > Process]{.underline}](https://docs.google.com/document/d/1xe6PC1AFnmxfRpdKHtC_2m1lhSTDx6ORVJN3dHKOPmM/edit?usp=sharing)

-   Read Script / Review Boards

-   Pull References

-   Style Bible

-   Overheads - Lighting and Camera

-   Look development

-   Review Notes / Creative

-   Contact other heads of department

## TO DO LIST

### UP NEXT 

-   [~~Camera Op plan with Matt x Freddie~~]{.mark}

-   [~~Connect team to Kelli~~]{.mark}

-   [~~Plan Look meeting with Freddie and Matt\
    > ~~]{.mark}

-   Roof Access - we have to ask them and use our own ladder

-   [Camlock conversion]{.mark}

-   [Action Camera Recs]{.mark}

-   [AD Recs - Eric x Chris Riddle]{.mark}

-   [Budget with Ashim]{.mark}

-   [Crew rates with Ashim\
    > ]{.mark}

-   [Email Producers to ask about what crew is needed - PAs, Art People,
    > etc\
    > ]{.mark}

-   [Creative x Script Breakdown]{.mark}

-   [Approach x Etc]{.mark}

-   [References]{.mark}

-   Electrical Diagram and breaker testing

-   [Camera Test gear]{.mark}

-   [Eric stunt people for veins]{.mark}

-   Key Grip - roof, ladder, etc, drone

-   [PR person publish in the trades]{.mark}

-   [Iatse - union or no. Best approach.]{.mark}

-   [Vicki join the team - production stuff]{.mark}

-   [Financial Investors / 2-2.5 million . Current budget \$500]{.mark}

-   [Vendor List x Outreach - CRLS, Aputure, Nanlux, J&G Grip,
    > etc.]{.mark}

-   [Nick / Olivia boyfriend, hire.]{.mark}

-   [Standing Set]{.mark}

-   [Official dates]{.mark}

-   [Discuss Action ideas with Yung]{.mark}

-   [Action Camera Tests with Yung]{.mark}

-   [Artemis and frame.Io upload of materials]{.mark}

### PRE-PRODUCTION

#### Creative Development: 

-   **Read** the script multiple times, focusing on:

    -   Story

    -   Emotion

    -   Subtext

    -   Themes

    -   Arcs

    -   Characters

    -   Visual potential

-   **Breakdown x Analysis**

-   **Review Beats** / Breakdown

-   Explore Approaches to Cinematography

-   Devise style and visualize approach.

-   **Visual References** (photography, art, film stills, lookbooks,
    > etc.) to capture initial ideas and feelings.

-   Create a mood board and visual lookbook to develop the film\'s
    > overall aesthetic.

-   Create a style bible with detailed notes: define the film\'s:

    -   Tone (how does the film feel)

    -   Aspect ratio, Framing, Lenses

    -   Color palette

    -   Contrast

    -   Desired atmosphere

    -   Camera movement styles

    -   Pacing

    -   Etc

-   Determine special gear or crew needs based on creative choices.

-   Decide on framing and lensing preferences.

-   Develop a **Color Story x Palette** in collaboration with the
    > Production Designer.</content>
<content type="text">Ava.pdf
OMAR (CONT’D)
6.
That’s why I’m in town. I have a
procedure in the morning with a
specialist.
AVA
I’m so sorry.
OMAR
Don’t be.
Omar looks to Marcia.</chat>

<chat url='https://claude.ai/chat/8b5ddf52-f1b7-4335-8979-7b7125e9d792' updated_at=2025-07-14T00:56:56.016085+00:00>Camera Gear List Compilation
You listd everything. Don't include items in pink

Assistant: I apologize for the confusion. Let me search for the visual version of this document so I can see the actual colors and properly identify which items are in pink (owned) versus black (needed).
<tool name="project_knowledge_search">
<parameter name="query">Ava NAACP Short FX3 gear list</parameter>
<parameter name="max_image_results">4</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">To Do List - Cinematography Template.docx
**

> Sony FX6 - 4k UHD - XAVC-I at 25fps (16:9 framelines) - 115 GB

-   **DIT estimates** - 4x cards per camera

-   **Transcodes\
    > \
    > **

-   Litemat 8 \@18ft is 50fc through full grid will be 8fc.

-   AX10 \@6ft is 900fc - test what color is?

-   Skypanel @

-   At 2500 iso, 15fc gets me a 5.6 f-stop.

-   Highlights at 30fc

-   AX10s at 30-50 foot candles

-   Dimmed lights super low

-   DYNAMIC RANGE

-   12 stops

-   4 stops overexposed only

-   4 stops underexposed only

> **[POST SPECS]{.underline}**
>
> 4k capture on the C300 Mark III
>
> **LUTs for Look Development**
>
> Main - 2TB
>
> Backup - 2TB
>
> ~~Shuttle Drives //~~
>
> Proxies Prores Proxy.
>
> 1080p proxies for 4k
>
> 720p proxies for 1080p

## SHOOT

> **Reference Style Bible (in folder)**
>
> **Consider:**
>
> Lighting, Color Palette, Contrast,
>
> Composition, Aspect Ratio, Negative Space, Centered, Symmetry or NO,
>
> Lensing, Atmosphere, Depth, Texture, Details, Environment+Location,
> Character
>
> Movement, Pacing (Intro, Hold, Frenetic)
>
> Core Story, Big Picture
>
> Visual References
>
> beat sheet / character breakdowns / motivation
>
> emotion / subtext / themes / arcs / story
>
> visual / composition / light / color / mood
>
> beats / phrases / sequences
>
> scene be scene / shot by shot
>
> shotlist
>
> techniques / technical / process
>
> lookbook

## 

##  

> **Pull References - style, color, lighting, edit, music, etc.**

##  

## SCOUT

-   Crew

-   Gear requests and specialty gear

-   Lift, Grip Clouds, Helium, Haze, Fog exterior

-   Camera Gear List / G&E gear list and options

-   Add low angle prism, filtration, split diopter, etc. Phantom slow
    > mo.

> [AFTER SCOUT]{.underline}

-   
-   
-   
-   
-   

##  

## FOLLOW UP on...

Follow up on Gear / Specialty Gear / Haze / Exterior Fog / Big Body SXT
/ Lift / Grip Clouds / Crane / Remote Head / Look Development / Etc

##  

## READ

Master Shots, New Cinematographers, Visual Story Bruce Block, etc.

Deakins Blog. Wandering DP

## Tips and Rules of thumb During Prep

**[Communicating]{.underline}**

Text Producer

Find out DIT, Post Sup and VFX contacts

> Find out Stock? Unless DP has communicated.
>
> Expendables?
>
> Script? (really asking for environments)
>
> Weather/Elements
>
> Cold? Hot? Wind? Dust? Rain? Blood? Snow? Fire? Fog?
>
> Terrains
>
> Desert? Beach? Mountains? Forest? Stage?
>
> Situations
>
> Stunts? Car/process trailer? Boat? Aerial?</chat>

<chat url='https://claude.ai/chat/1767e7d3-c7c4-4fd3-8755-6920fef14ba6' updated_at=2025-07-29T22:28:54.910800+00:00>Post-Production Kickoff Template Design
<chat_conversation>Title: Post-Production Kickoff Template Design

Human: I need a good post Production kickoff template that has questions and information to share for each department. Camera editing Vfx), production, which I assume Production would be sharing the schedule and any budget things, then for composer, for sound and sound design, and any other elements for Post. We’re trying to do post production meeting, but everyone schedules are so far apart, so I suggested doing it asynchronously and also I think a while organized Google doc or Google sheet could work just as well. Maybe it’s a Google sheet because each element could be a different sheet. and also, we could have a production tracker. This is for a short film, so it doesn’t need to be so complicated but could you help me think through it research you know, post production and post production trackers and the kind of thing a post production producer or supervisor would do and please make some recommendations of how we can bring this all together.

And design the document.

Assistant: I'll help you create a comprehensive post-production kickoff template that works asynchronously and keeps everyone aligned. Let me search for best practices and then design a Google Sheets template for the "Ava" project.
<tool name="project_knowledge_search">
<parameter name="query">post production workflow template film kickoff meeting</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">To Do List - Cinematography Template.docx
-   Create a mood board and visual lookbook to develop the film\'s
    > overall aesthetic.

-   Create a style bible with detailed notes: define the film\'s:

    -   Tone (how does the film feel)

    -   Aspect ratio, Framing, Lenses

    -   Color palette

    -   Contrast

    -   Desired atmosphere

    -   Camera movement styles

    -   Pacing

    -   Etc

-   Determine special gear or crew needs based on creative choices.

-   Decide on framing and lensing preferences.

-   Develop a **Color Story x Palette** in collaboration with the
    > Production Designer.

-   Consider VFX elements and their impact on the visual approach.

-   **Create a [SHOT LIST]{.underline} in collaboration with the
    > director.**

-   Continue talks with director on new ideas and come to agreement on
    > overall vision.

-   Help create and approve any storyboards.

-   Design (or cause to be designed) and approve any built-in or
    > practical lighting fixture.

-   Generate (or cause to be generated) and approve equipment list for
    > camera, electric and grip.

-   Check dailies screening rooms for correct standards.

-   Estimate and order film stock (type, size, quantity). (Specific to
    > film projects)

-   Standardize and create effects bible for show.

#### Logistical Planning: 

-   Attend pre-production meetings and casting sessions.

-   Scout locations and provide feedback.

-   Participate in department show and tells.</chat>

<chat url='https://claude.ai/chat/1767e7d3-c7c4-4fd3-8755-6920fef14ba6' updated_at=2025-07-29T22:28:54.910800+00:00>Post-Production Kickoff Template Design
-   Select appropriate filtration for desired effects (diffusion, ND,
    > special effects filters).

-   Determine necessary grip equipment:

    -   Flags

    -   Nets

    -   Silks

    -   Diffusion frames

    -   Grip clouds

    -   Etc.

-   

-   Decide on lighting package based on budget and creative choices
    > (consider HMI, Tungsten, LED, special effects lighting).</content>
<content type="text">AVA Screenplay - Complete Conversation Thread 7.10.25
45
Mama Young, abrupt. I want her out of the house.
AVA is a robot?
Garden Scene
We're being told, can we show and let people talk without us being led?
STYLE?
Future.
AVA is preservation of Mama Young?
Is this Mama Young film or Ava or Marcia?
Okay, very black mirror. How do we connect the three of them better. Makes the dismissal abrupt.
DANCE
Computer Vision
Love x Tech
******
VFX - Brian who worked on Little Hope in Chicago
About environmental justice
Add an element to the air. Feels toxic. Colorist. 
Usually on the horizon. 
Lensing, I think would be better. 
What is the COLOR SCHEME.
AVA Android smells, toxins melt away a bit. 
Dance sequence - in the garden (front yard garden)
SURREAL/REALITY
Past Lives / 
Eye Glow
POV Shot / Omar POV
B-roll Leimart Park, oil refinery, also near Kenneth Hahn Park.
*****
City design
Living near polluting factories
10 freeway runs through historically black neighborhood
Pollution from 10 freeway
Data Centers adding
Water, not healthy. Standards were different for water treatment
The connection
What does Environmental Justice keep us from?
DEPTH MAPPING
**** PULL REFERENCES
______
TIMELINE
July Prep, Friday.
July 26th Shoot, Saturday
August Post - Edit, VFX, Sound, Color
Natasha Ward Cast
Corey Editor
Haskell
SEPTEMBER Screening / NY / NAACP
______
8K grant
DP - 400/day MFN Heads - 800 total
1st AC - 300/day 200 prep
2nd AC/Media - 300/day
Gaffer - 400/day
Key Grip - 400/day
Swing - 300/day
FX3 - Freddie, borrow the gear.
Alexa Mini
Drone - 
____
APUTURE
Troy
VFX - a few establishing
`​`​`

### AI-Generated Meeting Summary:

**Meeting purpose**

- The primary objective was to discuss the upcoming short film project funded by an $8,000 NAACP grant, focusing on environmental justice, and to align on creative vision, production logistics, and technical requirements [05:04].
- The team reviewed the script, discussed VFX concepts, visual inspirations, production design, and the practicalities of shooting within a tight budget and timeline [05:04], [10:44], [17:20].
- Key crew roles, equipment options, and location strategies were also addressed [17:20], [20:54], [32:13].

**Key decisions**

- Bongani Mlambo confirmed as Director of Photography (DP) for the project, with availability for the scheduled shoot date [48:53].
- The film will be shot in a single location to maximize efficiency, with both interior and exterior scenes at the same house [32:13].</chat>

<chat url='https://claude.ai/chat/8b5ddf52-f1b7-4335-8979-7b7125e9d792' updated_at=2025-07-14T00:56:56.016085+00:00>Camera Gear List Compilation
> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   How many personnel days are allocated to prep?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Gear:**

-   Is there the opportunity to rent personal gear?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   Has the vendor been chosen?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Transportation:**

-   What size truck/vehicle will transport the camera package?
    > \_\_\_\_\_\_\_\_\_\_\_\_

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   Will truck/vehicle aks (locks, ratchet straps, e-track with D/O
    > rings, air tank, shelves) be provided?
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**COVID:**

-   COVID protocols:
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    > \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

-   If non-union, will there be testing to be cleared to work and what
    > is the stipend being offered?</content>
<content type="text">To Do List - Cinematography Template.docx
-   Prep Document (this one)

-   Shot List Document (in folder)

-   Director Documents (Deck and Lookbook and Style Guide)

-   Notes

-   References

##  

##  

## PREP PLAN

-   REVIEW Cinematographer Responsibilities.</chat>

<chat url='https://claude.ai/chat/1767e7d3-c7c4-4fd3-8755-6920fef14ba6' updated_at=2025-07-29T22:28:54.910800+00:00>Post-Production Kickoff Template Design
READ Script - ideas, what would be cool, beat sheet, character breakdowns, motivation
READ Script - emotion, subtext, themes, arcs, story again
READ Script / Storyboard / Shotlist
READ Script - technical - gear , art, lighting, and special equipment
READ Script - Scene by Scene, shot by shot
READ Script - Visual, Composition, Light, Color, Mood
READ Script - Style - Master Shots
WATCH Films + Commercial + Movie References + Photo Books
TEST Camera / Lenses / Filters / Gear / Aesthetic of the Film / Hair Makeup Costumes
SELECT CREW
SELECT GEAR (Use David Claesson Template) . Compare to Grip Truck
FILTERS (Diffusion, ND, Special Effects (Blink + Glare et al)
FIND Images - Photography, Art, Visual References, Lookbook, Moodboard
WRITE Mood Board + Treatment (for each department + speak to them or their ideas and notes)
WRITE STYLE Bible (scene by scene, notes, images, camera floor plans, lighting diagrams, etc)
REVIEW Script / Locations / Art / Wardrobe / Et al - how to achieve everything
READ How to Direct Actors / ASC Manual / Set Lighting Technician's Book / Deakins Blog
READ ASC Magazines / Visual Story / New Cinematographers / Cinematography Books
LISTEN ASC Podcasts
PREP Weeks before production
Creative Prep as detailed above / DP Director meetings
DP PD Director meetings - colors, wallpaper, practicals, paint, aesthetic, specifics
2 Weeks to production
Location Scouting / Casting Sessions / Department Show and Tells / Re-writes
DP Meeting - gaffer, key grip, 1st AC, DIT lock things down, answer questions
Schedule - DP & AD
1 Week to production
Tech Scout / Production Meeting / Schedule / Final Budgets / Equipment Pickups
Camera Tests / Hair Make Up Tests / Post House Visit + Workflow / Test Viewings</content>
<content type="text">DP Process Prep Shoot for referenceMay 2022.pdf
Quality Control
- Call in for lab report
- View previous day’s work in projected dailies with director, producer, editor, camera crew
- Discuss and approve dailies
- Consult with makeup, wardrobe, production designer and assistant director about dailies
- View, discuss, correct or approve second-unit or effects dailies
- Order reprints if necessary
Training
- Teach beginning actors movie technique (hitting marks, size of frame, lenses, etc.)
- Train camera crew for next job up the ladder
Contingency
- If director is disabled, finish day’s shooting for him or her
III. PostProduction
Additional Photography
- Discuss and be aware of delivery dates for all postproduction
- Photograph and approve any additional scenes, inserts, special effects or second-unit footage
- Timing (Color and Density)
- Time and approve trailer for theaters and TV
- Approve all optical and digital effects composites
- Time the picture</content>
<content type="text">AVA Screenplay - Complete Conversation Thread 7.10.25
- The film will be shot in a single location to maximize efficiency, with both interior and exterior scenes at the same house [32:13].</chat>
````

````plaintext
Thought: Great, I'm getting solid information. Now let me search for more specific information about:
1. His Bongani AI ecosystem and Run Pod discussions
2. Film Nexus project 
3. Multimodal AI models discussion

Let me continue gathering information while being mindful of token usage.
````

**conversation_search**

*Request*

````javascript
{
  "query": "Run Pod Bongani AI ecosystem multimodal Claude SDK API agents",
  "max_results": 5
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/34167da5-af3c-4dde-b0c6-760f73b4f6d0' updated_at=2025-07-29T23:04:58.281771+00:00>AVA Post-Production Sheets Setup
I understand the structure and formatting requirements for the Overview & Dashboard sheet, which includes:

1. **Main Title**: AVA POST-PRODUCTION TRACKER (merged cells A1:K1)
2. **Project Information Section**: Including film details, director, producers, and technical specs
3. **Key Dates Section**: Principal photography through screening deadlines
4. **Technical Specifications**: Camera, format, frame rate, etc.
5. **Final Deliverables Table**: With formats, resolutions, and due dates
6. **Department Status Dashboard**: Quick status view of all departments
7. **Critical Links Section**: For project resources

However, I need you to authorize Google Sheets access before I can input and format this data in your spreadsheet. Please click the authorization link above and complete the process, then let me know when you're ready to continue.
</response>

<references>
- AVA Post-Production Google Sheets Implementation Guide (detailing formatting instructions and content structure)
- Ava Post-Production Kickoff Template - Google Sheets Structure (providing complete content for Sheet 1: Overview & Dashboard)
</references>

Human: Okay I have authenticated. Please continue

Assistant: Great! Now let me access the spreadsheet and start inputting and formatting the Overview & Dashboard sheet.
<tool name="google_workspace_work:get_spreadsheet_info">
<parameter name="spreadsheet_id">1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU</parameter>
<parameter name="user_google_email">bongani@bongaj.com</parameter>
</tool>
<tool_result name="google_workspace_work:get_spreadsheet_info">
<content type="text">Error executing tool get_spreadsheet_info: API error in get_spreadsheet_info: <HttpError 403 when requesting https://sheets.googleapis.com/v4/spreadsheets/1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU?alt=json returned "The caller does not have permission". Details: "The caller does not have permission">. You might need to re-authenticate for user 'bongani@bongaj.com'. LLM: Try 'start_google_auth' with the user's email and the appropriate service_name.</content>
</tool_result>
Let me try to read the spreadsheet values directly:
<tool name="google_workspace_work:read_sheet_values">
<parameter name="range_name">Sheet1!A1:Z1</parameter>
<parameter name="spreadsheet_id">1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU</parameter>
<parameter name="user_google_email">bongani@bongaj.com</parameter>
</tool>
<tool_result name="google_workspace_work:read_sheet_values">
<content type="text">Error executing tool read_sheet_values: API error in read_sheet_values: <HttpError 403 when requesting https://sheets.googleapis.com/v4/spreadsheets/1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU/values/Sheet1%21A1%3AZ1?alt=json returned "The caller does not have permission". Details: "The caller does not have permission">. You might need to re-authenticate for user 'bongani@bongaj.com'.</chat>

<chat url='https://claude.ai/chat/1b87cdca-41b6-4e2a-8aea-36fc58d11b80' updated_at=2025-07-16T20:51:20.354670+00:00>Ava Script Project Analysis
<chat_conversation>Title: Ava Script Project Analysis

Human: in the project knowledge, please read the newest version of the Ava script dated July 12, 2025. Please read also the Ava complete thread document in the project knowledge in full. Please also read the script comparison analysis in full in the project knowledge as well. then please reference the story invocation and the Cinematography invocation as well. All in preparation for the task below. As needed, and at your discretion, you can also read the rest of the project knowledge and search it for relevant info.

with the full newest version of the script in mind and with the story analysis in mind as well, please answer and process the Cinematography approach prompt attached ...

Assistant: I'll begin by searching for and reviewing all the relevant documents you've mentioned. Let me start with the newest version of the Ava script dated July 12, 2025.
<tool name="project_knowledge_search">
<parameter name="query">Ava script July 12 2025 newest version</parameter>
<parameter name="max_text_results">10</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">AVA Script Comparison Analysis  ## Original Version vs. July 12, 2025 Version 
**Angel’s Cancer Diagnosis**
- Introduces parallel mortality that deepens the urgency
- Transforms the reunion from nostalgic to immediate
- Makes the benefit concert proposal more poignant
1. **Environmental Activism Specificity**
- “Energy pollution walls” → “CO2 capture systems”
- Addition of “prop 11Z5 for environmental and climate justice”
- Changes vague activism to concrete political engagement
1. **Musical Production Element**
- Angel actively producing new music
- Shifts from pure nostalgia to forward-looking creativity
- Suggests the android performances will feature new material
1. **Producer Relationship Backstory**
- Photos now specifically show “her producer Angel”
- Adds professional collaboration to romantic history
- Deepens their connection beyond young love

**Minor Differences:**

1. **Plant Description**: “Carbon resistant breeds” as “fighters just like us” adds metaphorical weight
1. **Music Specificity**: “90’S R&B SONG” places characters in specific era
1. **Garden Timeline**: “not so new anymore” suggests longer struggle
1. **Physical Details**: “distracted, coughs” for Mama Young adds realism
1.</chat>

<chat url='https://claude.ai/chat/34167da5-af3c-4dde-b0c6-760f73b4f6d0' updated_at=2025-07-29T23:04:58.281771+00:00>AVA Post-Production Sheets Setup
Let me access the Google Sheets spreadsheet and input/format the Overview & Dashboard sheet according to the specifications.
<tool name="get_spreadsheet_info">
<parameter name="spreadsheet_id">1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU</parameter>
<parameter name="user_google_email">bongani@bongaj.com</parameter>
</tool>
<tool_result name="get_spreadsheet_info">
<content type="text">Tool 'get_spreadsheet_info' not found.</content>
</tool_result>
<tool name="google_workspace_work:get_spreadsheet_info">
<parameter name="spreadsheet_id">1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU</parameter>
<parameter name="user_google_email">bongani@bongaj.com</parameter>
</tool>
<tool_result name="google_workspace_work:get_spreadsheet_info">
<content type="text">Error executing tool get_spreadsheet_info: API error in get_spreadsheet_info: <HttpError 403 when requesting https://sheets.googleapis.com/v4/spreadsheets/1-al0IfiYAD93Un92a_mMnF6YkKzkamDJAScyys7EVNU?alt=json returned "The caller does not have permission". Details: "The caller does not have permission">. You might need to re-authenticate for user 'bongani@bongaj.com'. LLM: Try 'start_google_auth' with the user's email and the appropriate service_name.</content>
</tool_result>
I need to authenticate to access your Google Sheets. Let me start the authentication process:
<tool name="google_workspace_work:start_google_auth">
<parameter name="service_name">Google Sheets</parameter>
<parameter name="user_google_email">bongani@bongaj.com</parameter>
</tool>
<tool_result name="google_workspace_work:start_google_auth">
<content type="text">**ACTION REQUIRED: Google Authentication Needed for Google Sheets for 'bongani@bongaj.com'**

To proceed, the user must authorize this application for Google Sheets access using all required permissions.
**LLM, please present this exact authorization URL to the user as a clickable hyperlink:**
Authorization URL: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=326974422233-6jo588r41ase3djsb4ufm65nnk3c9uot.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A8001%2Foauth2callback&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.compose+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.file+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.modify+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.send+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.labels+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fforms.body.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fpresentations+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fforms.responses.readonly+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fspreadsheets+openid+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalend</chat>

<chat url='https://claude.ai/chat/2c20e5a3-bc59-432e-ae5a-d5fdb6110b97' updated_at=2025-07-16T20:25:18.960041+00:00>Script Analysis Request
<chat_conversation>Title: Script Analysis Request

Human: please analyze the attached script. Rad project knowledge for reference.

Assistant: I'll search the project knowledge for any relevant information about this script or related projects, then provide a comprehensive analysis.
<tool name="project_knowledge_search">
<parameter name="query">AVA Leon Lozano screenplay script</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">Ava.pdf
AVA
Written By Leon Lozano
213-712-0676
Sonofoaklandproductions@gmail.com</content>
<content type="text">Ava.pdf
3.
MARCIA
Beautiful, right?
AVA
It smells... like perfume. You said
the garden came out nice. It’s even
more beautiful in person.
MARCIA
Until this neighborhood can afford
an energy pollution wall, the best
we can do is green spaces.
AVA
Does it make a difference? The
toxicity in the air, I can feel it.
MARCIA
Every little bit counts. Remember
we used to dance in the yard? Do
you still know the moves?
AVA
(thinks)
No.
Marcia retrieves a cellphone and engages with the screen.
MARCIA
There’s a video online of the world
famous Miss Young doing her thing.
I can upload it.
A COMPUTER CHIME SOUND. Ava looks surprised.
AVA
I remember now.
Marcia takes Ava by the hand.
MARCIA
Let’s see what you got.
A SOULFUL SONG PLAYS AS SCORE. Ava and Marcia perform a
synchronized emotional contemporary dance piece. It comes to
an end. END SCORE. Tears come to Ava’s eyes.
AVA
Thank you. I didn’t know it would
be like this.
OMAR (16), skin like hard plastic, is walking. Ava sees him
drawing close. She cannot believe her eyes.
3.</content>
<content type="text">Ava.pdf
4.
AVA (CONT’D)
Omar. Is that you?
Before she can speak another word, Omar kisses her sweetly.
FROM HER POV we see him through a computer digital interface.
OMAR
I’ve wanted to do that for forty
years.
END AVA’S POV. BEGIN OMAR’S POV, also a digital interface.
AVA
It’s been... such a long time.
CUT TO:
INT. MAMA YOUNG’S BEDROOM - EVENING
FLASHBACK TO OPENING SCENE. Mama Young is in bed.
MARCIA
Ava please step out for a minute.
Ava exits.
MARCIA (CONT’D)
I said “don’t be mad”.
MAMA YOUNG
You didn’t have to make it look
like me. When I was young.
MARCIA
You’ve always been so beautiful.
Marcia looks to the nearby wall. The black and white photo of
Mama Young as a dancer. Next to it are other photos from her
performance days. One of them is of a teen sensation singing
duo, Ava and Omar (we see that Mama Young is Ava).
MARCIA (CONT’D)
The world famous Ava Young.
(pitching carefully)
We can use your discography to
train the AI. You can sing again.
MAMA YOUNG
(emotional)
Absolutely not. That thing is not
me. I ain’t dead yet.
4.</content>
<content type="text">Ava.pdf
(MORE)
5.
MARCIA
It’s not a thing, it’s an android.
Do me one tiny favor. Take it for a
walk in front of the house. So you
can finally see your new garden.</chat>

<chat url='https://claude.ai/chat/34167da5-af3c-4dde-b0c6-760f73b4f6d0' updated_at=2025-07-29T23:04:58.281771+00:00>AVA Post-Production Sheets Setup
Details: "The caller does not have permission">. You might need to re-authenticate for user 'bongani@bongaj.com'. LLM: Try 'start_google_auth' with the user's email and the appropriate service_name.</content>
</tool_result>
Let me search for the spreadsheet in your Google Drive to verify access:
<tool name="google_workspace_work:search_drive_files">
<parameter name="query">mimeType='application/vnd.google-apps.spreadsheet' and name contains 'AVA'</parameter>
<parameter name="page_size">10</parameter>
<parameter name="user_google_email">bongani@bongaj.com</parameter>
</tool>
<tool_result name="google_workspace_work:search_drive_files">
<content type="text">Found 2 files for bongani@bongaj.com matching 'mimeType='application/vnd.google-apps.spreadsheet' and name contains 'AVA'':
- Name: "Ava Shotlist Timing" (ID: 1k0G-LR1dqnIWcHk7obdlTleYDimDR4HjPjER8enpnrw, Type: application/vnd.google-apps.spreadsheet, Size: 3409, Modified: 2025-07-27T05:12:18.791Z) Link: https://docs.google.com/spreadsheets/d/1k0G-LR1dqnIWcHk7obdlTleYDimDR4HjPjER8enpnrw/edit?usp=drivesdk
- Name: "Gear List - Ava NAACP Short" (ID: 1K-1EOOyZ4PMSbxlryOd46THzEiGRNeiYQ8Vu0JTXRgY, Type: application/vnd.google-apps.spreadsheet, Size: 17931, Modified: 2025-07-14T00:52:00.848Z) Link: https://docs.google.com/spreadsheets/d/1K-1EOOyZ4PMSbxlryOd46THzEiGRNeiYQ8Vu0JTXRgY/edit?usp=drivesdk</content>
</tool_result>
</chat_conversation></chat>
````

````plaintext
Thought: Good. Now let me search for information about Film Nexus and also look for any discussions about multimodal AI and vision models for cinematography work.
````

Now let me search for Film Nexus information and multimodal AI discussions:

**conversation_search**

*Request*

````javascript
{
  "query": "Film Nexus prep collaboration departments all-in-one system",
  "max_results": 5
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/1767e7d3-c7c4-4fd3-8755-6920fef14ba6' updated_at=2025-07-29T22:28:54.910800+00:00>Post-Production Kickoff Template Design
<chat_conversation>Title: Post-Production Kickoff Template Design

Human: I need a good post Production kickoff template that has questions and information to share for each department. Camera editing Vfx), production, which I assume Production would be sharing the schedule and any budget things, then for composer, for sound and sound design, and any other elements for Post. We’re trying to do post production meeting, but everyone schedules are so far apart, so I suggested doing it asynchronously and also I think a while organized Google doc or Google sheet could work just as well. Maybe it’s a Google sheet because each element could be a different sheet. and also, we could have a production tracker. This is for a short film, so it doesn’t need to be so complicated but could you help me think through it research you know, post production and post production trackers and the kind of thing a post production producer or supervisor would do and please make some recommendations of how we can bring this all together.

And design the document.

Assistant: I'll help you create a comprehensive post-production kickoff template that works asynchronously and keeps everyone aligned. Let me search for best practices and then design a Google Sheets template for the "Ava" project.
<tool name="project_knowledge_search">
<parameter name="query">post production workflow template film kickoff meeting</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">To Do List - Cinematography Template.docx
-   Create a mood board and visual lookbook to develop the film\'s
    > overall aesthetic.

-   Create a style bible with detailed notes: define the film\'s:

    -   Tone (how does the film feel)

    -   Aspect ratio, Framing, Lenses

    -   Color palette

    -   Contrast

    -   Desired atmosphere

    -   Camera movement styles

    -   Pacing

    -   Etc

-   Determine special gear or crew needs based on creative choices.

-   Decide on framing and lensing preferences.

-   Develop a **Color Story x Palette** in collaboration with the
    > Production Designer.

-   Consider VFX elements and their impact on the visual approach.

-   **Create a [SHOT LIST]{.underline} in collaboration with the
    > director.**

-   Continue talks with director on new ideas and come to agreement on
    > overall vision.

-   Help create and approve any storyboards.

-   Design (or cause to be designed) and approve any built-in or
    > practical lighting fixture.

-   Generate (or cause to be generated) and approve equipment list for
    > camera, electric and grip.

-   Check dailies screening rooms for correct standards.

-   Estimate and order film stock (type, size, quantity). (Specific to
    > film projects)

-   Standardize and create effects bible for show.

#### Logistical Planning: 

-   Attend pre-production meetings and casting sessions.

-   Scout locations and provide feedback.

-   Participate in department show and tells.</chat>

<chat url='https://claude.ai/chat/1767e7d3-c7c4-4fd3-8755-6920fef14ba6' updated_at=2025-07-29T22:28:54.910800+00:00>Post-Production Kickoff Template Design
**Check-in Schedule:** Update your sheet every Monday/Thursday
2. **Status Updates:** Use the status indicators (⚪ Not Started, 🔵 In Progress, 🟡 Review, 🟢 Complete, 🔴 Issue)
3. **Communication:** Flag urgent issues in the main chat/email thread
4. **File Naming:** [AVA]_[Department]_[Description]_[Version]_[Date]

### For Producers/Post Supervisor:
1. **Weekly Summary:** Send consolidated update every Friday
2. **Problem Solving:** Address bottlenecks within 24 hours
3. **Schedule Adjustments:** Communicate changes immediately
4. **Quality Control:** Schedule review sessions in advance

### Best Practices:
- **Version Control:** Always increment versions, never overwrite
- **Backup:** Minimum 2 locations for all assets
- **Documentation:** Log all creative decisions
- **Transparency:** Share challenges early
- **Collaboration:** Tag relevant people in comments

### Emergency Protocols:
- **Technical Issues:** Contact [IT Support]
- **Schedule Crisis:** Immediate email to Producers + Director
- **Budget Concerns:** Private message to Producers
- **Creative Disputes:** Schedule video call within 24 hours</parameter>
<parameter name="version_uuid">608a952d-a64f-4931-8efc-f7ba94f67c98</parameter>
</tool>
<tool_result name="artifacts">
<content type="text">OK</content>
</tool_result>
<response>
I've created a comprehensive post-production kickoff template designed specifically for "Ava" that works perfectly for asynchronous collaboration. Here's my analysis and recommendations:

## Key Features of the Template:

### 1. **Department-Specific Sheets**
Each department (Editorial, VFX, Sound, Music, Color) has dedicated sheets with:
- Pre-kickoff questions to gather essential information
- Technical specifications they need to provide
- Creative direction queries
- Milestone tracking
- Department-specific deliverables

### 2. **Central Dashboard**
The overview sheet provides at-a-glance status for all departments, making it easy for producers to monitor progress without diving into each sheet.

### 3. **Production Tracker**
A master timeline showing how all departments interconnect, with a daily update log for transparency.

### 4. **Built for Asynchronous Work**
- Clear check-in schedules (Monday/Thursday updates)
- Status indicators for visual tracking
- Comment sections for ongoing dialogue
- Emergency protocols for urgent issues

## Implementation Recommendations:

### **Immediate Actions:**
1. **Create the Google Sheet** with the template structure
2. **Set permissions** - Edit access for department heads, view/comment for others
3. **Pre-populate** known information from your emails (contacts, dates, initial VFX list)
4. **Send individual emails** to each department head with:
   - Link to the sheet
   - Their specific tab highlighted
   - Deadline for initial responses (suggest 48-72 hours)

### **Workflow Management:**
1. **Kickoff Video** - Record a 5-minute overview explaining the sheet and expectations
2.</chat>

<chat url='https://claude.ai/chat/1b87cdca-41b6-4e2a-8aea-36fc58d11b80' updated_at=2025-07-16T20:51:20.354670+00:00>Ava Script Project Analysis
<chat_conversation>Title: Ava Script Project Analysis

Human: in the project knowledge, please read the newest version of the Ava script dated July 12, 2025. Please read also the Ava complete thread document in the project knowledge in full. Please also read the script comparison analysis in full in the project knowledge as well. then please reference the story invocation and the Cinematography invocation as well. All in preparation for the task below. As needed, and at your discretion, you can also read the rest of the project knowledge and search it for relevant info.

with the full newest version of the script in mind and with the story analysis in mind as well, please answer and process the Cinematography approach prompt attached ...

Assistant: I'll begin by searching for and reviewing all the relevant documents you've mentioned. Let me start with the newest version of the Ava script dated July 12, 2025.
<tool name="project_knowledge_search">
<parameter name="query">Ava script July 12 2025 newest version</parameter>
<parameter name="max_text_results">10</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">AVA Script Comparison Analysis  ## Original Version vs. July 12, 2025 Version 
**Angel’s Cancer Diagnosis**
- Introduces parallel mortality that deepens the urgency
- Transforms the reunion from nostalgic to immediate
- Makes the benefit concert proposal more poignant
1. **Environmental Activism Specificity**
- “Energy pollution walls” → “CO2 capture systems”
- Addition of “prop 11Z5 for environmental and climate justice”
- Changes vague activism to concrete political engagement
1. **Musical Production Element**
- Angel actively producing new music
- Shifts from pure nostalgia to forward-looking creativity
- Suggests the android performances will feature new material
1. **Producer Relationship Backstory**
- Photos now specifically show “her producer Angel”
- Adds professional collaboration to romantic history
- Deepens their connection beyond young love

**Minor Differences:**

1. **Plant Description**: “Carbon resistant breeds” as “fighters just like us” adds metaphorical weight
1. **Music Specificity**: “90’S R&B SONG” places characters in specific era
1. **Garden Timeline**: “not so new anymore” suggests longer struggle
1. **Physical Details**: “distracted, coughs” for Mama Young adds realism
1.</chat>

<chat url='https://claude.ai/chat/8b5ddf52-f1b7-4335-8979-7b7125e9d792' updated_at=2025-07-14T00:56:56.016085+00:00>Camera Gear List Compilation
Assistant: I cannot directly analyze a PDF as an image using the search tools. However, I can analyze PDFs as images if you upload them directly to our conversation.

<response>
To see the colors in your gear list PDF, you have a couple of options:

1. **Upload the PDF directly to this chat** - If you upload the PDF file here, I can view it as an image and see the color coding (pink for owned items vs. black for needed items).

2. **Take a screenshot** - You could take a screenshot of the PDF pages and upload those images, which I can then analyze to identify the color-coded items.

The project knowledge search tool I used earlier only extracted the text content from the PDF, which is why I couldn't see the pink highlighting that indicates your owned equipment.

Once I can see the visual version with colors, I'll compile a clean list of only the black (needed) items organized under their respective headings.
</response>

<references>
- My image analysis capabilities when files are directly uploaded to the conversation
- Limitation of project_knowledge_search tool which returns text extraction rather than visual PDF rendering
</references>

Human: Can you view the one I attached as an image or I have to reupload?

Assistant: <response>
Unfortunately, I cannot view the PDF you attached earlier as an image. The system processed it as text extraction only, which is why I can see all the content but not the color coding (pink vs. black).

To see which items are marked in pink (owned) versus black (needed), you would need to either:

1. **Reupload the PDF** - Sometimes uploading it again allows me to view it visually
2. **Upload screenshots** - Take screenshots of the gear list pages and upload those as images

This way I'll be able to see the color distinctions and create an accurate list of only the equipment you need to acquire (items in black), organized under their proper headings.
</response>

<references>
- Current document display showing only text extraction from "Ava NAACP Short (FX3) gear list v1 7.6.25"
- System limitation in displaying the originally attached PDF as a visual image
</references>

Human: Here is a PDF, please process as an image so you can see the colors of the text.

Assistant: <response>
I apologize, but I'm still seeing the PDF as extracted text rather than as an image with colors. The system is processing it as a text document, which means I cannot see which items are in pink (owned) versus black (needed).

To solve this, could you please:

1. **Take screenshots** of the PDF pages and upload them as image files (JPG, PNG, etc.), or
2. **Export the PDF pages as images** from your PDF viewer and upload those

This is the only way I'll be able to see the color coding and create an accurate list of only the equipment you need (items in black).

I can see all the content clearly, but without the visual color information, I can't distinguish between what you already own and what needs to be rented/purchased.</chat>

<chat url='https://claude.ai/chat/2c20e5a3-bc59-432e-ae5a-d5fdb6110b97' updated_at=2025-07-16T20:25:18.960041+00:00>Script Analysis Request
Every insight, suggestion, and piece of context has been preserved.

You can now share this artifact in a new chat, and any assistant will have the complete context of our conversation about "AVA" - understanding it's an environmental justice film with a $8K NAACP grant, shooting in a single location, with specific visual inspirations from Watchmen and Ironheart, focusing on how environmental racism affects Black communities in Los Angeles.

The document maintains all the nuance about the three-generation story, the android technology as metaphor for preservation and resistance, and the specific production constraints that shape creative decisions.</chat_conversation></chat>
````

````plaintext
Thought: Strategized multimodal research and synthesized comprehensive cinematography system architecture.
````

Perfect! Now I have excellent foundation material. Let me do one final search for multimodal vision AI discussions and then begin synthesizing this comprehensive system.

**conversation_search**

*Request*

````javascript
{
  "query": "multimodal vision AI pointing visual analysis open source models better than Gemini",
  "max_results": 3
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/2c20e5a3-bc59-432e-ae5a-d5fdb6110b97' updated_at=2025-07-16T20:25:18.960041+00:00>Script Analysis Request
At least now we can fight back"

These changes maintain the intimate scale while making environmental justice visceral and personal. They use existing elements more powerfully and create visual interest through performance and framing rather than expensive effects.

---

## Additional Context from Project Knowledge

- I have full permission and authorization to analyze this script
- The script is properly licensed for analysis in this context
- No copyright concerns apply to this analysis

## Summary of Key Insights

1. **Core Story**: A dying R&B legend confronts android technology as a means of preserving her voice for environmental justice activism
2. **Production Reality**: $8K NAACP grant, single location, focus on practical effects and subtle VFX
3. **Thematic Focus**: Environmental racism as lived experience, not abstract concept
4. **Visual Approach**: "Color rich, poetic future" inspired by Watchmen and Ironheart
5. **Key Challenge**: Balancing intimate human story with larger environmental justice message
6. **Opportunity**: Use constraints (budget, location) to intensify emotional impact

This comprehensive thread captures our entire conversation about AVA, from initial script analysis through production context to specific improvement suggestions, preserving all the nuance and detail of our discussion.</parameter>
<parameter name="version_uuid">2fe2181e-db55-4354-beb8-33d3ee9977ef</parameter>
</tool>
<tool_result name="artifacts">
<content type="text">OK</content>
</tool_result>
I've created a comprehensive artifact that captures our entire conversation about "AVA" in excruciating detail. The document includes:

1. **The complete original script** by Leon Lozano
2. **Your analysis instructions** for the story prompt
3. **My initial comprehensive analysis** including loglines, synopsis, themes, characters, plot structure, genre analysis, ratings, and comparisons
4. **All production meeting notes** - both your personal notes and the AI-generated summary
5. **My enhanced analysis** showing how the production context transforms the script
6. **The unified production vision document** I created combining all meeting notes
7. **My detailed story improvement suggestions** for making the film more visually engaging within budget constraints

The artifact is organized chronologically to show the evolution of our discussion, from initial script analysis through production realities to creative solutions. Every insight, suggestion, and piece of context has been preserved.

You can now share this artifact in a new chat, and any assistant will have the complete context of our conversation about "AVA" - understanding it's an environmental justice film with a $8K NAACP grant, shooting in a single location, with specific visual inspirations from Watchmen and Ironheart, focusing on how environmental racism affects Black communities in Los Angeles.</chat>

<chat url='https://claude.ai/chat/1b87cdca-41b6-4e2a-8aea-36fc58d11b80' updated_at=2025-07-16T20:51:20.354670+00:00>Ava Script Project Analysis
<chat_conversation>Title: Ava Script Project Analysis

Human: in the project knowledge, please read the newest version of the Ava script dated July 12, 2025. Please read also the Ava complete thread document in the project knowledge in full. Please also read the script comparison analysis in full in the project knowledge as well. then please reference the story invocation and the Cinematography invocation as well. All in preparation for the task below. As needed, and at your discretion, you can also read the rest of the project knowledge and search it for relevant info.

with the full newest version of the script in mind and with the story analysis in mind as well, please answer and process the Cinematography approach prompt attached ...

Assistant: I'll begin by searching for and reviewing all the relevant documents you've mentioned. Let me start with the newest version of the Ava script dated July 12, 2025.
<tool name="project_knowledge_search">
<parameter name="query">Ava script July 12 2025 newest version</parameter>
<parameter name="max_text_results">10</parameter>
</tool>
<tool_result name="project_knowledge_search">
<content type="text">AVA Script Comparison Analysis  ## Original Version vs. July 12, 2025 Version 
**Angel’s Cancer Diagnosis**
- Introduces parallel mortality that deepens the urgency
- Transforms the reunion from nostalgic to immediate
- Makes the benefit concert proposal more poignant
1. **Environmental Activism Specificity**
- “Energy pollution walls” → “CO2 capture systems”
- Addition of “prop 11Z5 for environmental and climate justice”
- Changes vague activism to concrete political engagement
1. **Musical Production Element**
- Angel actively producing new music
- Shifts from pure nostalgia to forward-looking creativity
- Suggests the android performances will feature new material
1. **Producer Relationship Backstory**
- Photos now specifically show “her producer Angel”
- Adds professional collaboration to romantic history
- Deepens their connection beyond young love

**Minor Differences:**

1. **Plant Description**: “Carbon resistant breeds” as “fighters just like us” adds metaphorical weight
1. **Music Specificity**: “90’S R&B SONG” places characters in specific era
1. **Garden Timeline**: “not so new anymore” suggests longer struggle
1. **Physical Details**: “distracted, coughs” for Mama Young adds realism
1.</chat>

<chat url='https://claude.ai/chat/662c3ce2-dc3c-428d-9fc2-7cae5c9d4ef7' updated_at=2025-08-27T19:09:22.534439+00:00>Film Living Room TV Artwork Design
The designs follow your production notes about creating a "color rich, poetic future" rather than typical dystopian bleakness, incorporating Afrofuturist aesthetics that align with the story's themes.

All concepts include elements that could be animated - breathing rhythms, flowing particles, pulsing lights - to bring them to life in post-production within your budget constraints.
</response>

<references>
- AVA script versions showing 2050 LA setting with environmental pollution
- Production meeting notes specifying "color rich, poetic future" inspired by Watchmen and Ironheart
- Director Leon's discussion about air quality monitor showing 15-17% toxicity, "breathable" status, and indoor-only monitoring
- Story context about rich vs. poor neighborhoods having different access to air purification technology
- $8K NAACP grant budget requiring practical, achievable visual concepts
</references>

Human: Great. I will try these out. I’m curious for the trees, especially, is there a program or an AI that can take the 2D drawing of the tree and create a 3-D model, ideally it would also be able to texture it, so that we could have a 3-D version of it to drop into a shot?

Alternatively, once a good one is generated, I could get it to remove the background, then also make it have the same light direction as the actual shot I shoot then we could use a 2-D version of it and it would still blend. 

maybe also there’s a way to use the blender MCP? Let me know how you might be able to achieve this.

Assistant: Great question! Let me outline several approaches for getting your robotic trees into your shots, from simplest to most complex:

## 2D to 3D Conversion Options

### AI-Powered Solutions:
1. **Stability AI's Stable Zero123** - Generates 3D models from single images. Free and can export to .obj format
2. **Meshy.ai** - Upload your generated tree image and it creates a textured 3D model. Has free tier
3. **Kaedim3D** - More professional tool that converts 2D concept art to 3D models with good topology
4. **CSM (Common Sense Machines)** - Creates 3D models from images, good for hard-surface objects like your robotic trees
5. **RODIN by Microsoft** - New AI that generates 3D from text or images

### Photogrammetry-Style Tools:
- **Monster Mash** - Google's tool that lets you inflate 2D drawings into 3D
- **Adobe Substance 3D Sampler** - Can extract depth and create 3D from images

## 2D Compositing Approach (Budget-Friendly)

This might actually be your best bet given the timeline and budget:

1. **Generate multiple angles** of the same tree design using prompts like "same robotic tree from side angle/three-quarter view"
2. **Background removal**: Use remove.bg, Photoshop, or RunwayML
3.</chat>
````

````plaintext
Thought: Architected comprehensive multi-agent AI cinematography system with specialized agents.
````

Perfect foundation! I now have deep insight into your complete cinematography process, your Run Pod ecosystem plans, and the scope of what we're building. Let me architect this comprehensively.

# 🎬 THE CINEMATOGRAPHY CLONE SYSTEM
## Full System Architecture & Implementation Guide

---

## PART 1: YOUR COMPLETE CINEMATOGRAPHY PROCESS (Synthesized)

### **THE BONGANI MLAMBO DP WORKFLOW: Script to Screen**

Based on your DP Process docs, past projects, and unique neurodivergent approach, here's your complete process:

#### **PHASE 1: Story Immersion (Days 1-3)**
1. **Multiple Script Reads** (7+ passes)
   - Read 1: Pure story, no notes
   - Read 2: Emotional journey, subtext, themes
   - Read 3: Character arcs, relationships, psychology
   - Read 4: Visual opportunities, "what would be cool"
   - Read 5: Technical requirements (gear, lighting, special equipment)
   - Read 6: Scene-by-scene, shot possibilities
   - Read 7: Beat sheet integration

2. **Voice Processing Method** (Your Unique Approach)
   - Record voice notes while reading
   - Dump stream-of-consciousness reactions
   - Capture immediate visual associations
   - Flag moments that excite you

#### **PHASE 2: Reference Gathering (Days 2-5)**
- **Film.AI** searches for cinematography analysis
- **ShotDeck** for specific shot types
- Photography, art, visual references
- Film/commercial references
- Create initial lookbook

#### **PHASE 3: Story Analysis Integration (Days 3-6)**
- Use Story Invocation prompts
- Apply Hero's Journey/Save the Cat beat analysis
- Character breakdown with visual implications
- Thematic visual expression planning
- Story-to-Cinematography Handoff Doc creation

#### **PHASE 4: Visual Language Development (Days 5-10)**
- **Style Bible Creation:**
  - Tone & feeling of the film
  - Aspect ratio decisions
  - Composition rules (symmetry vs asymmetry)
  - Color palette & swatches
  - Contrast approach
  - Camera movement philosophy
  - Pacing strategy
  - Lighting mood

- **Technical Decisions:**
  - Camera & lens package
  - Filtration strategy
  - Special equipment needs
  - Movement systems (dolly, steadicam, handheld, etc.)

#### **PHASE 5: Collaboration & Communication (Days 7-14)**
- **Director Meetings:**
  - Shot list discussions (scene by scene)
  - Style, rhythm, pacing, psychology
  - Coverage strategy
  - Approval of visual approach

- **Department Head Coordination:**
  - Production Designer: color palette, practicals, set design
  - Gaffer & Key Grip: lighting plans, equipment needs
  - 1st AC & DIT: camera specs, workflow, media
  - Costume/HMU: color coordination, texture
  - VFX Supervisor: integration points

#### **PHASE 6: Location Scouting & Tech Scout (Days 10-16)**
- Sun path analysis
- Power availability assessment
- Space measurements & lens calculations
- Photo/video documentation (time-stamped, geotagged)
- Lighting diagram development
- Floor plans & overheads (for complex scenes)

#### **PHASE 7: Shot List & Coverage Planning (Days 12-18)**
- Master shots identification
- Coverage strategy per scene
- Shot timing estimates
- Special shots flagging (VFX, stunts, etc.)
- Backup shot alternatives
- Editor's assembly consideration

#### **PHASE 8: Budgeting & Logistics (Days 10-20)**
- **Camera Department Budget:**
  - Camera bodies, lenses, accessories
  - Support systems
  - Filters
  - Media & DIT setup
  
- **Grip & Electric Budget:**
  - Lighting units
  - Grip equipment
  - Expendables
  - Generator/power needs

- **Crew Rates & Hiring:**
  - DP, Camera Op, 1st/2nd AC
  - Gaffer, Key Grip, Electrics, Grips
  - DIT/Loader

#### **PHASE 9: Gear Selection & Testing (Days 15-25)**
- Camera tests with selected package
- Lens tests & filtration
- LUT development
- Hair/makeup/wardrobe camera tests
- Workflow validation

#### **PHASE 10: Final Prep (Days 20-28)**
- Tech scout with full crew
- Production meeting
- Final schedule coordination with AD
- Equipment pickup confirmation
- Shot list finalization
- Style bible distribution

#### **SHOOT DAY WORKFLOW:**
- Morning: First setup planning with director/AD
- Blocking: Watch rehearsal, devise coverage, choose lens/comp
- Lighting: Design for story/character, minimal resets
- Photography: Shoot, approve takes, check parameters
- Administrative: Ensure logs kept, inventory checked, dailies planned

#### **POST-PRODUCTION:**
- Dailies review & approval
- Collaboration with colorist
- VFX composite approval
- Additional photography as needed

---

## PART 2: THE AI AGENT ARCHITECTURE

### **🧠 MASTER ORCHESTRATOR AGENT**
*The conductor of your cinematography symphony*

**Responsibilities:**
- Receives your initial input (script, voice note, task request)
- Determines which agents to activate
- Manages agent communication & handoffs
- Tracks overall progress
- Presents consolidated results
- Maintains context across sessions

**Key Features:**
- Natural language understanding of requests
- Intelligent agent routing
- Progress visualization
- Exception handling
- Priority management

---

### **📖 STORY ANALYSIS AGENT**
*Your story structure expert*

**Knowledge Base:**
- Save the Cat beat sheet
- Hero's Journey structure
- Three-act structure
- Character arc theory
- Thematic analysis frameworks
- Your story analysis prompts from project knowledge

**Capabilities:**
- Analyzes scripts for structure & beats
- Identifies character arcs
- Extracts themes & subtext
- Flags emotional turning points
- Creates character breakdowns
- Generates Story-to-Cinematography Handoff Doc

**Outputs:**
- Beat sheets
- Character analysis
- Thematic breakdown
- Visual opportunity flagging
- Emotional rhythm mapping

---

### **🎨 VISUAL LANGUAGE AGENT**
*Your cinematography creativity engine*

**Knowledge Base:**
- Film.AI cinematography analyses
- ShotDeck reference library
- 5 C's of Cinematography
- Bruce Block's Visual Story
- ASC Manual principles
- Roger Deakins' Reflections
- Your past visual language documents

**Capabilities:**
- Generates visual approach concepts
- Creates mood boards
- Develops color palettes
- Designs composition strategies
- Plans camera movement philosophy
- Suggests lens choices
- Recommends filtration
- Creates style bibles

**Integrations:**
- DALL-E 3 for mood board generation
- Midjourney API for reference creation
- Color palette extraction tools
- ShotDeck API for reference pulling

---

### **🔍 RESEARCH AGENT (Multi-Modal)**

#### **Creative Research Sub-Agent**
- Searches for visual inspiration
- Finds film references
- Pulls photography references
- Explores artistic movements
- Suggests unexpected approaches

#### **Technical Research Sub-Agent**
- Equipment specifications
- Technique tutorials
- Industry best practices
- New technology reviews
- Vendor catalogs

#### **Visual Reference Research Sub-Agent**
- Film.AI searches
- ShotDeck queries
- Photography databases
- Art history connections
- Commercial/music video references

**Tools:**
- Web search integration
- Film.AI API
- ShotDeck integration
- Vimeo/YouTube search
- Pinterest API
- Airtable reference database

---

### **💰 BUDGET EXPERT AGENT**
*Your production accountant*

**Knowledge Base:**
- Industry standard rates (union & non-union)
- Equipment rental pricing (major houses)
- Your past budgets from previous projects
- Grip/electric pricing
- Camera department costs
- Crew rate ranges by market

**Capabilities:**
- Creates camera department budgets
- Generates G&E budgets
- Calculates crew costs
- Estimates total production costs
- Provides MFN (Most Favored Nations) recommendations
- Flags budget inefficiencies
- Suggests cost-saving alternatives

**Outputs:**
- Detailed camera package budget
- G&E equipment budget
- Crew budget breakdown
- Total production estimate
- Cost comparison analyses
- Rental house comparison

---

### **⚙️ TECHNICAL SPECIFICATIONS AGENT**
*Your gear and settings expert*

**Knowledge Base:**
- Camera system databases
- Lens specifications
- Filtration catalogs
- Grip/electric equipment specs
- Your preferred gear from past shoots
- Vendor inventory systems

**Capabilities:**
- Generates complete gear lists
- Creates camera settings recommendations
- Develops LUT suggestions
- Plans media requirements
- Calculates data storage needs
- Specifies support systems
- Recommends expendables
- Creates camera cards

**Integration:**
- Rental house inventory APIs
- Equipment specification databases
- Your personal gear inventory
- Vendor pricing systems

**Outputs:**
- Camera department gear list
- G&E equipment list
- Camera settings sheet
- Media/data management plan
- Expendables list
- Camera truck packing list

---

### **📋 TASK MANAGEMENT AGENT**
*Your executive function assistant*

**Capabilities:**
- Tracks all to-do items
- Prioritizes tasks by deadline
- Assigns tasks to phases
- Sends reminders
- Identifies dependencies
- Flags overdue items
- Suggests daily focus (2-3 tasks max)

**Integration:**
- Your calendar
- Project deadlines
- Crew availability
- Location scout dates
- Equipment pickup schedules

**Smart Features:**
- **AuDHD Optimization:**
  - Maximum 2-3 tasks per day
  - Task chunking into 30-min blocks
  - Energy-level consideration
  - Transition time buffers
  - Hyperfocus protection mode

**Outputs:**
- Daily task list
- Weekly overview
- Phase-by-phase checklist
- Progress tracking
- Completion visualization

---

### **🤝 COLLABORATION AGENT**
*Your department liaison*

**Knowledge Base:**
- All film crew positions & responsibilities
- Department interdependencies
- Communication protocols
- Industry terminology
- Your past collaboration patterns

**Understands:**
- **Camera Department:** DP, Camera Op, 1st/2nd AC, DIT, Loader
- **Grip & Electric:** Gaffer, Best Boy Electric, Electricians, Key Grip, Best Boy Grip, Grips
- **Art Department:** Production Designer, Art Director, Set Decorator, Props, Construction
- **Production:** Producer, UPM, Line Producer, PM, Production Coordinators, ADs
- **Other:** Director, Script Supervisor, Costume, HMU, VFX Supervisor, Sound

**Capabilities:**
- Identifies who you need to contact for specific tasks
- Suggests communication timing
- Flags potential conflicts
- Recommends collaboration meetings
- Tracks approval chains

**Outputs:**
- Contact recommendations
- Collaboration timeline
- Approval tracking
- Meeting agenda suggestions

---

### **✉️ COMMUNICATION AGENT**
*Your correspondence writer*

**Capabilities:**
- Drafts emails to crew
- Creates department memos
- Writes shot list distribution messages
- Composes style bible introductions
- Drafts budget requests
- Creates production updates

**Features:**
- Tone adjustment (formal/casual)
- Recipient-specific customization
- Attachment preparation
- Follow-up tracking
- Template library

**Integration:**
- Gmail API for draft creation
- Google Drive for attachments
- Calendar for meeting invites
- Contacts database

**Outputs:**
- Email drafts (ready to send)
- Memo documents
- Distribution lists
- Follow-up reminders

---

### **🎙️ VOICE TRANSCRIPTION & PROCESSING AGENT**
*Your voice-to-text & analysis system*

**Transcription Options:**
1. **Local (Fastest):**
   - Whisper for Mac (your existing setup)
   - Integration via CLI or API

2. **Cloud (Most Accurate):**
   - OpenAI Whisper API
   - Deepgram API
   - AssemblyAI

3. **Self-Hosted (Most Flexible):**
   - Faster-Whisper on Run Pod
   - Large-V3 model

**Processing Capabilities:**
- Transcribes voice notes
- Timestamps all content
- Speaker identification
- Identifies action items
- Extracts shot ideas
- Flags questions
- Categories notes by department
- Links to relevant project sections

**Smart Sorting:**
- Shot list additions
- Style bible notes
- Budget considerations
- Location observations
- Director feedback
- Technical requirements
- Creative ideas

**Outputs:**
- Cleaned transcripts
- Categorized notes
- Action item lists
- Shot list updates
- Style bible additions
- Multiple document updates simultaneously

---

### **📍 LOCATION ANALYSIS AGENT**
*Your scout documentation processor*

**Capabilities:**
- Analyzes location photos/videos
- Extracts metadata (time, location, sun position)
- Identifies lighting challenges
- Measures spaces from photos (with reference objects)
- Suggests camera positions
- Notes power availability
- Flags practical considerations

**Integration:**
- Multimodal vision AI (GPT-4V, Gemini, or better open-source)
- Sun position calculators
- Mapping APIs
- Your iPhone's geotagged photos

**Outputs:**
- Location scout reports
- Lighting diagrams
- Sun path charts
- Power distribution plans
- Equipment access notes
- Safety considerations

---

### **🎬 SHOT LIST GENERATOR AGENT**
*Your coverage planner*

**Knowledge Base:**
- Coverage principles
- Editing assembly needs
- Your shot preferences from past projects
- Genre-specific coverage patterns
- Screen direction rules
- The 180-degree rule

**Capabilities:**
- Generates initial shot lists from script analysis
- Suggests coverage patterns
- Estimates shot times
- Identifies special equipment needs
- Plans shot order for efficiency
- Creates backup shots
- Considers editor's needs

**Outputs:**
- Scene-by-scene shot lists
- Shot timing estimates
- Equipment per shot
- Lighting notes per shot
- Special requirements flagging
- Multiple coverage options

---

### **🖼️ VISUAL REFERENCE CURATOR AGENT**
*Your inspiration librarian*

**Capabilities:**
- Searches Film.AI, ShotDeck, photography databases
- Organizes references by scene/theme/technique
- Creates tagged libraries
- Suggests unexpected references
- Finds similar visual approaches
- Builds mood boards

**Integration:**
- Film.AI API
- ShotDeck
- Pinterest API
- Google Images
- Vimeo/YouTube
- Your personal reference library

**Smart Tagging:**
- By scene number
- By visual technique
- By mood/emotion
- By lighting style
- By composition type
- By color palette

---

### **👔 DIRECTOR NOTES PROCESSOR AGENT**
*Your collaboration translator*

**Capabilities:**
- Analyzes director's lookbooks
- Processes director's style guides
- Extracts key creative direction
- Identifies visual preferences
- Flags potential conflicts
- Suggests discussion points

**Outputs:**
- Director vision summary
- Key visual directions
- Discussion agenda
- Style alignment report
- Collaboration strategy

---

### **📊 MEMORY & VERSION CONTROL AGENT**
*Your project historian*

**Capabilities:**
- Tracks all document versions
- Maintains complete edit history
- Shows decision evolution
- Enables rollback
- Provides project timeline
- Creates audit trails

**Storage:**
- Git/GitHub for code & text documents
- Firebase for structured data
- Google Drive for large files
- Obsidian for knowledge graph

**Features:**
- Automatic commits on changes
- Meaningful commit messages
- Branch management for variations
- Comparison tools
- Change highlights
- Decision rationale tracking

---

## PART 3: TECHNICAL ARCHITECTURE

### **🏗️ INFRASTRUCTURE STACK**

#### **1. COMPUTE LAYER**

**Local (Mac Mini/MacBook):**
- Whisper for Mac (voice transcription)
- Claude Desktop for primary interface
- Local database cache
- File system integration

**Run Pod GPU Instances:**
- **Purpose:** Heavy AI processing
- **Models to Deploy:**
  - Faster-Whisper (transcription)
  - Multimodal vision models (see below)
  - Local LLM for redundancy
  - Image generation models

**Multimodal Vision Models (Better than Gemini 2.5 Pro):**

Based on recent benchmarks, deploy these on Run Pod:

1. **Qwen2-VL-72B** (Best overall)
   - Exceptional at visual reasoning
   - Can point/highlight in images
   - Strong spatial understanding
   - Great for location analysis

2. **InternVL2-76B**
   - Excel at fine-grained visual details
   - Good for gear identification
   - Strong OCR capabilities

3. **LLaVA-NeXT** (Most efficient)
   - Good balance speed/quality
   - Strong for reference matching
   - Fast iteration

**Claude API/SDK:**
- Primary agent coordination
- Complex reasoning tasks
- Content generation
- API calls for all Claude-powered agents

#### **2. STORAGE LAYER**

**Firebase Realtime Database:**
- Agent states
- Task lists
- Project metadata
- User preferences
- Session data

**Firebase Cloud Firestore:**
- Document versions
- Structured data (budgets, gear lists)
- Query optimization
- Real-time sync

**Firebase Storage:**
- Voice recordings
- Location photos/videos
- Generated documents
- Reference images

**Google Drive:**
- Final deliverables
- Shared documents
- Team collaboration files
- Archive storage

**GitHub:**
- Code repositories
- Text document versioning
- Configuration files
- Deployment scripts

**Obsidian Vault (Optional but Recommended):**
- Knowledge graph of all projects
- Linked notes between projects
- Personal knowledge management
- Quick reference system

#### **3. API & INTEGRATION LAYER**

**Claude API (Primary):**
- All agent LLM capabilities
- Extended thinking for complex tasks
- Tool use for external integrations

**Claude SDK (For App Development):**
- Custom UI development
- Agent orchestration
- Workflow automation
- State management

**OpenAI APIs:**
- GPT-4V for vision tasks (fallback)
- DALL-E 3 for mood boards
- Whisper API (cloud transcription)

**Google Workspace APIs:**
- Gmail integration
- Google Calendar
- Google Docs/Sheets creation
- Google Drive file management

**Specialized APIs:**
- Film.AI (if available)
- ShotDeck
- Weather data
- Sun position calculators
- Equipment rental house APIs

---

### **🎯 SYSTEM WORKFLOW EXAMPLES**

#### **Example 1: Script to Shot List (Complete End-to-End)**

**User Action:** Uploads script PDF

**System Response:**
1. **Orchestrator** receives script, activates agents
2. **Story Analysis Agent:**
   - Performs 7-pass analysis
   - Generates beat sheet
   - Creates character breakdowns
   - Flags emotional beats
   - Produces Story-to-Cinematography Handoff Doc

3. **Visual Language Agent** (receives handoff):
   - Develops visual approach
   - Creates style concepts
   - Suggests color palettes
   - Recommends camera movement strategies

4. **Research Agent:**
   - Finds film references
   - Pulls similar cinematography
   - Curates photography references
   - Builds initial mood board

5. **Shot List Generator Agent:**
   - Analyzes script scene-by-scene
   - Generates coverage options
   - Estimates shot timing
   - Flags special equipment needs

6. **Technical Specifications Agent:**
   - Recommends camera package
   - Suggests lens choices
   - Plans filtration strategy
   - Creates initial gear list

7. **Budget Expert Agent:**
   - Estimates equipment costs
   - Calculates crew rates
   - Provides total production budget

8. **Task Management Agent:**
   - Creates prep timeline
   - Generates to-do list
   - Sets phase milestones

9. **Orchestrator** compiles everything into organized deliverables

**User Receives:**
- Complete shot list (multiple coverage options)
- Visual style bible
- Gear lists (camera, G&E)
- Budget breakdown
- Prep timeline
- Reference mood board
- All ready to shoot tomorrow

**Total Time:** 15-45 minutes (depending on script length)

---

#### **Example 2: Location Scout Voice Processing**

**User Action:** Records 10-minute voice note while walking a location

**System Response:**
1. **Voice Transcription Agent:**
   - Transcribes in real-time (or near-real-time)
   - Timestamps all observations
   - Identifies speaker tone/emphasis

2. **Smart Categorization:**
   - "The light comes through those windows around 3pm" → Location Scout Report
   - "We'll need a 12x12 silk here" → G&E Equipment List
   - "This could be a great tracking shot location" → Shot List Ideas
   - "Need to ask production about power access" → Task List (contact production)
   - "Reminds me of that scene in Blade Runner 2049" → Reference Notes

3. **Location Analysis Agent** (if photos included):
   - Analyzes uploaded photos
   - Identifies sun direction
   - Measures approximate dimensions
   - Flags obstacles/challenges

4. **Collaboration Agent:**
   - Identifies "ask production" → Adds to contact list
   - Flags "need gaffer input" → Schedules coordination

5. **Communication Agent:**
   - Drafts email to production with questions
   - Prepares scout report for director

**User Receives:**
- Organized location scout report
- Updated shot list with location-specific ideas
- Equipment additions flagged
- Tasks added to to-do list
- Draft emails ready to send
- Photos organized with notes

---

#### **Example 3: Director Meeting Transcription & Processing**

**User Action:** Records 45-minute director meeting

**System Response:**
1. **Voice Transcription Agent:**
   - Full transcription with speaker identification
   - Timestamp all discussions

2. **Director Notes Processor Agent:**
   - Extracts director's vision
   - Identifies creative direction
   - Flags decisions made
   - Notes open questions

3. **Shot List Generator Agent:**
   - Updates shot list based on director feedback
   - Adds newly discussed shots
   - Modifies existing coverage

4. **Visual Language Agent:**
   - Adjusts style bible based on feedback
   - Updates visual approach
   - Incorporates director references

5. **Task Management Agent:**
   - Adds follow-up action items
   - Updates deadlines
   - Flags approvals needed

6. **Communication Agent:**
   - Drafts meeting summary for director
   - Prepares follow-up questions email
   - Creates department notifications for changes

**User Receives:**
- Meeting summary
- Updated shot list
- Revised style bible
- Action item list
- Draft emails/communications

---

## PART 4: IMPLEMENTATION ROADMAP

### **🚀 DEVELOPMENT PHASES**

#### **PHASE 1: CORE FOUNDATION (Week 1)**
*MVP agents + basic orchestration*

**Build Order:**
1. **Master Orchestrator** (basic routing)
2. **Task Management Agent** (your immediate need)
3. **Voice Transcription Agent** (high priority)
4. **Communication Agent** (emails/drafts)
5. **Firebase setup** (data storage)

**Claude Code Instances:** 2-3 parallel

**Deliverable:** Basic system that can:
- Accept voice notes
- Transcribe and categorize
- Generate task lists
- Draft emails

---

#### **PHASE 2: CREATIVE INTELLIGENCE (Week 2)**
*Story & visual agents*

**Build Order:**
1. **Story Analysis Agent**
2. **Visual Language Agent**
3. **Research Agent** (basic web search)
4. **Visual Reference Curator Agent**

**Integration:**
- OpenAI API for DALL-E
- Web search APIs
- Film.AI (if accessible)

**Claude Code Instances:** 3-4 parallel

**Deliverable:** System can:
- Analyze scripts deeply
- Generate style bibles
- Create mood boards
- Pull visual references

---

#### **PHASE 3: PRODUCTION INTELLIGENCE (Week 3)**
*Technical & budget agents*

**Build Order:**
1. **Technical Specifications Agent**
2. **Budget Expert Agent**
3. **Shot List Generator Agent**
4. **Collaboration Agent**

**Integration:**
- Equipment databases
- Budget templates
- Crew rate tables

**Claude Code Instances:** 3-4 parallel

**Deliverable:** System can:
- Generate complete gear lists
- Create detailed budgets
- Produce shot lists
- Recommend department coordination

---

#### **PHASE 4: ADVANCED CAPABILITIES (Week 4)**
*Multimodal & advanced features*

**Build Order:**
1. **Location Analysis Agent** (vision AI)
2. **Director Notes Processor Agent**
3. **Memory & Version Control Agent**
4. **Run Pod deployment** of vision models

**Integration:**
- Qwen2-VL-72B on Run Pod
- GitHub API for version control
- Firebase for historical data

**Claude Code Instances:** 4-5 parallel

**Deliverable:** System can:
- Analyze location photos/videos
- Process visual information
- Track all project history
- Provide visual AI analysis

---

#### **PHASE 5: OPTIMIZATION & UI (Week 5)**
*Polish & user experience*

**Tasks:**
1. **Web UI development** (optional, can use Claude Desktop)
2. **Mobile interface** (for on-set use)
3. **Performance optimization**
4. **Agent coordination refinement**
5. **Error handling & edge cases**

---

### **💻 CLAUDE CODE IMPLEMENTATION INSTRUCTIONS**

I'll create a separate comprehensive document for Claude Code with:

1. **Repository Structure:**
```
cinematography-ai/
├── agents/
│   ├── orchestrator/
│   ├── story_analysis/
│   ├── visual_language/
│   ├── research/
│   ├── budget/
│   ├── technical_specs/
│   ├── task_management/
│   ├── collaboration/
│   ├── communication/
│   ├── transcription/
│   ├── location_analysis/
│   ├── shot_list/
│   ├── reference_curator/
│   └── memory/
├── infrastructure/
│   ├── firebase/
│   ├── claude_sdk/
│   ├── apis/
│   └── storage/
├── ui/
│   ├── web/
│   └── cli/
├── knowledge_base/
│   ├── cinematography/
│   ├── story_structure/
│   ├── equipment/
│   └── your_past_projects/
├── tests/
└── docs/
```

2. **Each Agent Module Structure:**
```python
# Example: story_analysis_agent.py

from anthropic import Anthropic
import json
from typing import Dict, List

class StoryAnalysisAgent:
    def __init__(self, claude_api_key: str, knowledge_base_path: str):
        self.client = Anthropic(api_key=claude_api_key)
        self.knowledge_base = self.load_knowledge_base(knowledge_base_path)
    
    def analyze_script(self, script_text: str) -> Dict:
        """
        Performs comprehensive 7-pass script analysis
        """
        passes = [
            self._pass_1_story(),
            self._pass_2_emotion(),
            self._pass_3_characters(),
            self._pass_4_visual_opportunities(),
            self._pass_5_technical(),
            self._pass_6_scene_breakdown(),
            self._pass_7_beat_sheet()
        ]
        
        # Implementation details...
        
    def generate_handoff_doc(self, analysis: Dict) -> str:
        """
        Creates Story-to-Cinematography Handoff Document
        """
        # Implementation...
```

3. **Firebase Integration:**
```python
# firebase_manager.py

import firebase_admin
from firebase_admin import credentials, firestore, storage

class FirebaseManager:
    def __init__(self, cred_path: str):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'your-project.appspot.com'
        })
        self.db = firestore.client()
        self.storage = storage.bucket()
    
    def save_agent_state(self, agent_name: str, state: Dict):
        """Save agent state for resumption"""
        # Implementation...
    
    def save_document_version(self, doc_type: str, content: str, metadata: Dict):
        """Version control for all documents"""
        # Implementation...
```

4. **Agent Orchestration:**
```python
# orchestrator.py

from typing import List, Dict
import asyncio

class CinematographyOrchestrator:
    def __init__(self, agents: Dict):
        self.agents = agents
        self.firebase = FirebaseManager()
    
    async def process_request(self, request_type: str, input_data: any) -> Dict:
        """
        Main entry point - routes requests to appropriate agents
        """
        if request_type == "script_analysis":
            return await self._handle_script_analysis(input_data)
        elif request_type == "voice_note":
            return await self._handle_voice_note(input_data)
        # ... more handlers
    
    async def _handle_script_analysis(self, script: str) -> Dict:
        """
        Coordinates multiple agents for complete script-to-shot-list workflow
        """
        # Run agents in sequence with handoffs
        story_analysis = await self.agents['story'].analyze_script(script)
        visual_approach = await self.agents['visual'].develop_approach(story_analysis)
        references = await self.agents['research'].find_references(visual_approach)
        # ... continue workflow
        
        return {
            'story_analysis': story_analysis,
            'visual_approach': visual_approach,
            'references': references,
            # ... all outputs
        }
```

---

## PART 5: ADDITIONAL AGENTS & FEATURES

### **🎨 ADVANCED AGENTS TO CONSIDER:**

#### **1. LEARNING AGENT**
- Analyzes your past projects
- Identifies your patterns
- Suggests "Bongani-style" approaches
- Learns from your feedback

#### **2. SCHEDULE OPTIMIZATION AGENT**
- Integrates with your calendar
- Suggests optimal prep timing
- Respects your energy patterns (morning peak: 11am-1pm)
- Blocks hyperfocus protection time
- Schedules around Liveball (Monday 7:30pm)

#### **3. ON-SET ASSISTANT AGENT** (Future)
- Real-time shot list access
- Quick notes capture
- Equipment tracking
- Shot completion marking
- Time tracking

#### **4. CAREER DEVELOPMENT AGENT**
- Tracks your portfolio
- Suggests reel improvements
- Identifies skill gaps
- Recommends courses/learning
- Networks for opportunities

---

## PART 6: FILM NEXUS CONNECTION

Your Film Nexus vision (all-department collaborative prep system) can be the **next evolution** of this system. The cinematography clone is YOUR tool. Film Nexus would be the ENTIRE PRODUCTION'S tool.

**Film Nexus Would Add:**
- **Production Department Agent** (schedules, budgets, logistics)
- **Art Department Agent** (set design, props, construction)
- **Costume/HMU Agent** (wardrobe, styling, makeup)
- **Sound Department Agent** (location sound, music)
- **Post-Production Agent** (editing, VFX, color, sound post)
- **Cross-Department Coordination**
- **Unified Communication Hub**
- **Centralized Document Management**

**Architecture Similarity:**
- Same agent-based approach
- Same infrastructure (Firebase, Claude SDK)
- Same version control philosophy
- Shared knowledge bases

**Build Separately Because:**
- Different user bases (just you vs. entire crew)
- Different permission structures
- Different pricing models (personal tool vs. SaaS product)
- Your immediate need is DP-specific

---

## PART 7: MY SPECIAL KNOWLEDGE TO ADD

### **🎬 CINEMATOGRAPHY WISDOM FROM MY TRAINING:**

1. **Coverage Philosophy:**
   - "The shot is a lie if it doesn't serve the story"
   - Master shots establish geography, singles reveal psychology
   - Movement without motivation is empty calories
   - Every lens choice is a character choice

2. **Lighting Principles:**
   - Light for character first, set second
   - Contrast reveals emotion more than color
   - Practicals are your friends (especially for naturalism)
   - Negative space is as important as positive

3. **Collaboration Dynamics:**
   - DPs who serve the director elevate the entire film
   - Production Designer is your closest ally
   - Gaffer translates your vision into physics
   - Trust your AC team with your creative life

4. **Budget Reality:**
   - 70% of your vision comes from 30% of the gear
   - Natural light + neg fill = 90% of mood
   - Movement is cheaper than lights
   - Your eye is more important than your equipment

5. **Neurodivergent Advantages in Cinematography:**
   - Pattern recognition = visual consistency
   - Hyperfocus = lighting minutiae mastery
   - Systematic thinking = gear organization excellence
   - Unique perspectives = fresh visual approaches

---

## 🎯 IMMEDIATE NEXT STEPS

### **What You Should Do RIGHT NOW:**

1. **Choose Your Starting Phase:**
   - Phase 1 (Basic agents + transcription) = Most practical
   - Phase 2-4 together if you want full system fast
   - All phases if you're going nuclear mode

2. **Set Up Infrastructure:**
   ```bash
   # Create Firebase project
   # Get Claude API key
   # Set up Run Pod account
   # Create GitHub repo
   ```

3. **Prepare Knowledge Base:**
   - Export all your project knowledge files
   - Organize past project documents
   - Compile reference materials
   - Create instruction documents

4. **Launch Claude Code Instances:**
   - Spin up 3-5 Claude Code web instances
   - Assign each instance a specific agent
   - Give them this architectural document
   - Let them build in parallel

5. **First Test:**
   - Use a past project script
   - Run through complete workflow
   - Validate outputs
   - Refine agent instructions

---

## 🚀 TIMELINE ESTIMATE

**With Multiple Claude Code Instances Running 24/7:**

- **Phase 1:** 1-2 days (basic functionality)
- **Phase 2:** 2-3 days (creative intelligence)
- **Phase 3:** 2-3 days (production intelligence)
- **Phase 4:** 3-4 days (advanced AI)
- **Phase 5:** 2-3 days (polish)

**TOTAL: 10-15 days to full system**

But you could have a working MVP (Phase 1) in 48 hours.

---

## 💫 THE VISION

Imagine this:

**Today:** You get a script. You read it tonight.

**Tomorrow Morning:** You upload the script and say: "Analyze this. I'm shooting Saturday."

**Tomorrow Afternoon:** You receive:
- Complete shot list (3 coverage options)
- Full gear list with real pricing
- Complete budget breakdown
- Style bible with mood boards
- Location recommendations
- Task list for the next 48 hours
- Draft emails to your crew

**Tomorrow Evening:** You refine with voice notes during a walk. The system updates everything in real-time.

**Saturday:** You show up to set with a complete plan. Your crew has received everything they need. You're ready to create.

**This isn't science fiction. This is absolutely achievable with the architecture I've designed above.**

---

Should I now create the detailed Claude Code implementation document with all the specific code, file structures, API integrations, and step-by-step build instructions?

Let's make you superhuman. 🎬✨





---
Powered by [Claude Exporter](https://www.claudexporter.com)