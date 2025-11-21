# Cinematography app knowledge foundation

**User:** Bongani  
**Created:** 11/19/2025 0:17:15  
**Updated:** 11/19/2025 10:56:09  
**Exported:** 11/21/2025 0:59:27  
**Link:** [https://claude.ai/chat/39423cec-f403-4772-9946-20bc41fe617a](https://claude.ai/chat/39423cec-f403-4772-9946-20bc41fe617a)  

## Prompt:
11/19/2025, 12:17:19 AM

> File: 

read all the project knowledge books for grounding in cinematography knowledge and process. Then answer this:



## Response:
11/19/2025, 12:18:59 AM

````plaintext
Thought: Deliberated research sequencing and clarifying questions before proceeding.
````

I'm going to read through the cinematography project knowledge, then ask a few clarifying questions before diving into the deep research needed to architect this system. Let me start by exploring what's in the knowledge base.

**project_knowledge_search**

*Request*

````javascript
{
  "query": "cinematography process preparation DP workflow script to screen",
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
Cinematography Theory and Practice 3rd editions 2016.pdf
In effect,
the ACES process potentially gives the DP even greater control over the final
image. We now have tools to enormously change the image digitally; this is
wonderful, but it also means that other people have even more opportunities to
mess with our images later on. This degree of control on the set and in post is
also what makes the DIT such an important part of the process. The DP has
specific ideas about what a scene should look like, but the cinematographer is
doing several jobs at once—he or she rarely has time to dial in a CDL or work
on a look in color correction software. The DIT can function as the implementer
of the DP’s vision for the scene by communicating with the cinematographer,
perhaps even getting to know their preferences and artistic tendencies; offering
them alternate looks to approve or disapprove and then translating that look into

•
•
•
•
a CDL, a LUT, or a color grade to make sure that the look of the scene that the
DP and director agreed on is then translated into a form that can pass down the
line, either as a starting point or guidance or the final color correction process.
THE STAGES
As shown in Figure 6.21, the ACES workflow involves four basic stages in the
process, which are defined by their transforms. They are Input Device
Transform, Look Modification Transform, Reference Rendering Transform, and
Output Device Transform. It looks a bit complex but, in reality, it is rather
simple and elegant in its design. Here are some very brief definitions of the
primary steps of the workflow. The overall concept of the ACES workflow is
much easier to understand once you break it down and look at each individual
stage:
IDT—Input Device Transform. A calculation to convert a camera or
other image sources to the Academy Color Encoding Specification, at
which point the image will be scene referred and in an RGB floating
point format. Each camera will need its own IDT, in most cases
provided by the manufacturer.
LMT—Look Modification Transform. This is where the colorist, DP,
and director work their artistry, in other words, it is color correction.
There is often a temporary transform to some kind of log or proxy
space (depending on the color correction system). It can be guided by
an ASC-CDL decision list, LUT, or dailies color grade.
RRT—Reference Rendering Transform. A single transform that is
designed to be the standard; it is also where picture rendering is done.
Scene referred images do not look right to the eye, so the RRT
converts the image to output referred. The RRT is an important part of
making the final image.
ODT—The Output Device Transform, also referred to as Electro-
Optical Conversion Function, takes the output of the RRT and finishes
the process to map data to the actual display devices where the project
will be seen at home or in theaters.
ACES TERMINOLOGY
Let’s go over some of the new terminology used in the ACES workflow.
````

````plaintext
The Cinematic Blueprint: Deconstructing the Shot List from Script Subtext to Visual Strategy
The Cinematic Blueprint: Deconstructing the Shot List from Script Subtext to Visual Strategy
This report details the comprehensive, multi-stage process utilized by professional film crews, from independent productions to major studio blockbusters, to translate a written screenplay into a precisely executed visual blueprint—the shot list. It emphasizes the symbiotic relationship between the Director and the Cinematographer (DP), detailing how theoretical visual grammar is intentionally applied to achieve critically acclaimed and commercially successful storytelling.
I. The Foundation of Visual Storytelling: From Script to Concept
The creation of a shot list is not a creative outburst but an iterative process rooted in meticulous textual analysis and systematic preparation. The objective is to ensure that every planned image is justified by the narrative intent and emotional requirements of the script.
1.1. Deep Script Analysis and Deconstruction: Finding the Visual Thesis
The process begins with the transformation of the linear screenplay into a multidimensional production document. This administrative phase, known as the systematic script breakdown, involves the thorough dissection of the script to identify and categorize all required production elements, including characters, locations, props, and costumes.[1] This comprehensive organization is essential for accurate resource allocation, scheduling, and budgeting, providing a detailed blueprint for the entire production.[1] Historically, this was a manual process that took weeks for large-scale productions like Gone with the Wind.[1]
Beyond logistics, the creative analysis involves distilling the narrative into its essential story beats. Utilizing a tool such as a beat sheet helps outline the story from the first act to the final image, ensuring that all critical plot points and major emotional shifts are identified.[2, 3] This narrative map keeps the story on track and establishes the dramatic structure that the visual language must parallel.
The most advanced stage of cinematic deconstruction involves mapping the subtext and theme. Filmmakers must move beyond the literal dialogue to grasp the underlying objective or theme—the moral of the story.[4] Subtext is defined as the "hidden goals under the surface," the emotional undercurrent not explicitly announced by characters.[4, 5] This deeper understanding provides the fundamental justification for all shot decisions. For instance, if a character's underlying objective is psychological isolation, the script breakdown must not only note the required props but also establish the need for specific visual devices to communicate that isolation, such as the strategic use of negative space or a certain focal length.[6, 7]
A failure to map this subtext results in a merely administrative, rather than cinematic, breakdown.
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
1 - The Visual Story Bruce Block.pdf
261
Spontaneity can create unique visuals, but it’s hard to maintain, difficult for
coworkers to prepare or follow, and potentially unreliable.
Make notes about your plan before you get to the set. Write down ideas in
your script about the meaning and point-of-view of a scene.
Translate the visual component graphs into simple reminder notes. If
a component is going to gain contrast or affinity, write a note to yourself
about that change. Directors often keep notes in their script about an actor’s
emotional state or the staging of a scene. Reminders about the visual
component choices and the visual structure can also be written in the
script margins. Quick notes about tonal contrast, camera movement, lens
choice, or fragmentation, for example, can remind the director of the visual
structure.
The earlier you begin this process the better. As you prepare, collaborate
with your photographer and production designer about how to choose
and control the visual components. Leave time to allow your visual ideas
to mature. Then review and refine your visual structure plan. On the set,
your notes will remind you to implement your visual ideas and keep your
thoughts on track.
Draw storyboards. The main purpose of storyboards is to visualize shots before
you shoot. If storyboards are to be of any use, they can’t be taken lightly.
Well-conceived storyboards are as important a commitment as the script.
You may need to redraw the storyboards many times just as a writer must
rewrite a script. Creating storyboards is a chance to previsualize shots and
improve them. Use storyboards to discover how to compose shots, stage
actors, and make use of the visual components.
Use previsualization. Pre-Viz is a software program that creates virtual sets and
actors in a computer. This virtual studio provides a real-time, lens-accurate
storyboard with movement that can be edited together like a finished film.
There are several programs available that allow you to build virtual sets or
enter measurements of locations, add moving actors, and choose accurate
camera positions and lenses.
Complex action sequences for special effects films usually are tested in Pre-
Viz so that problems can be solved during preparation. For his film The Panic
Room (2002), David Fincher previsualized his entire film before he began
shooting with actors on the actual sets. Spielberg used an on-set real-time
Pre-Viz system to combine live action with special effects for his remake of
War of the Worlds.
Approach the preparation process like a stage play. Assemble your actors and
rehearse your production as if it were a theatre play. Since you can rehearse
your entire script in real time, you’ll have a unique opportunity to see the
story uninterrupted from beginning to end. You won’t have this view of your
production again until you’re in the editing room.
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
Cinematography Theory and Practice 3rd editions 2016.pdf
ough the Window
Available Natural Light

Available Light Windows
Motivated Light
Carrying a Lamp
Day Exteriors
Fill
Silks and Diffusion
Open Shade and Garage Door Light
Sun As Backlight
Magic Hour
optics & focus
The Physical Basis of Optics
Refraction
Focal Length and Angle of View
F/Stop
Focus
Mental Focus
Circle of Confusion
Depth-of-Field
How Not to Get More Depth-of-Field
Hyperfocal Distance
Nodal Points
The Rear Nodal Point and Special Effects Shots
Zooms and Depth-of-Field
Macrophotography
Exposure Compensation in Macrophotography
Depth-of-Field in Close-Up Work
Calculating Depth-of-Field in Close-Up Work
Close-Up Tools
Diopters
Extension Tubes or Bellows
Macro Lenses
Snorkels and Innovision
Specialized Lenses
Lens Extenders and Filter Factors
Lens Care

Back Focus
camera movement
Camera Movement in Filmmaking
Motivation and Invisible Technique
Basic Technique
Types of Moves
Pan
Tilt
Move In/Move Out
Zoom
Punch-in
Moving Shots
Tracking
Countermove
Reveal with Movement
Circle Track Moves
Crane Moves
Rolling shot
Camera Supports for Movement
Drones
Handheld
Stabilizer Rigs
Camera Heads
The Tripod
High-Hat
Rocker Plate
Tilt Plate
The Crab Dolly
Dolly Terminology
Car Shots
Camera Positions for Car Shots
Vehicle to Vehicle Shooting
Aerial Shots
Other Types of Camera Mounts
Steadicam
Rickshaw, Wheelchair, and Garfield

Cable-Cam
Crash Cams
Splash Boxes
Underwater Housings
Motion Control
set operations
Making It Happen
The Director of Photography
The Cinematographer’s Tools
Gaffer Glass
Laser Pointer
Director’s Viewfinder
Digital Still Camera
The Shot List
Putting the Order Together
Reading the Script
Talking to the Director
Location Scouts and Tech Scouts
Coordinating with Other Departments
The Team and the Order
The Page Turn
Tests
Camera Crew
Operator
First AC Duties
Second AC
Loader
DIT
DIT Workflow
Simple Data Workflow
Advanced Workflow
Digital Loader/Media Manager
Utility
Camera Crew Reports, Equipment & Tools
Camera Reports
Camera Assistant Tools and Supplies

AC Prep
Camera Prep Checklist
The Team
Lighting Technicians (Electricians or Sparks)
Grips
Other Units
Set Procedures
Block, Light, Rehearse, Shoot
The Process
Room Tone
Set Etiquette
Set Safety
Lighting, Electrical, and Grip
Crane Safety
Slating Technique
Verbal Slating
Tail Slate
MOS Slating
Slating Multiple Cameras
Timecode Slates
Jamming the Slate
What to Write on the Slate
When to Change the Letter
The European System of Slating
Pickups, Series, and Reshoots
VFX
Bumping a Slate
Insert Slates
Finding the Sun
data management
Data Management
Basic Principles
Cover your Rear
Standard Procedures
Maintain Your Logs

Procedure—Best Practices
Locked and Loaded
Get Your Signals Straight
Always Scrub
Three Drives
Do Nor Drag and Drop
Logs
File Management
File Naming
Download/Ingest Software
ShotPut Pro
Silverstack
Double Data
Proprietary Data Management Software
External Recorders
Hard Drives & Raids
RAID
Transfer/Shuttle Drives
How Much Storage Do You Need?
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
Cinematography Theory and Practice 3rd editions 2016.pdf
(Photo courtesy Owen Stephens at Fill-Light).

•
•
•
•
•
•
•
•
•
•
•
Stay calm, listen,
observe and lead by
example.
Jonathan Taylor,
ASC
THE DIRECTOR OF PHOTOGRAPHY
Every director has a different style of working: some will be very specific about
a certain look they want and exact framing, while others want to focus on
working closely with the actors, and staging the scenes and leave it to the DP to
decide on exact framing, camera moves and the lighting style, filtration, and so
on.
Ultimately the director is the boss; he or she
may work in whatever fashion they wish. A
professional DP should have the flexibility to
work with a director in whatever manner they
choose. Ultimately it is up to the DP to deliver for
the director the kind of look and visual texture
they are looking for and ensure that the director and editor have all the footage
they need and that it is all editorially usable. The DP’s responsibilities are
numerous. They include:
The look of the scenes, in consultation with the director.
Directing the lighting of the project.
Communicating to the gaffer and key grip how the scene is to be lit:
specific lights to be used, gels, cuts with flags, silks, overheads,
diffusion, and so on. Directing and supervising the lighting process.
Coordinating with the production designer, wardrobe, makeup, and
effects crew concerning the overall look of the film.
Filtration on the camera.
Lenses: including whether to use a zoom or a prime lens (though this
may sometimes be the director’s call).
Ensuring that there are no flicker problems (see the chapter on The
Tools of Lighting).
Being constantly aware of and consulting on issues of continuity:
crossing the line, screen direction, and so on.
Being a backstop on insuring that the director hasn’t forgotten specific
shots needed for good coverage of the scene.
Supervising their team: camera operator, the camera assistants, the
electricians, the grips, and any second camera or second unit camera
crews; also the data wrangler and DIT.
Watching out for mistakes in physical continuity: clothing, props,
scenery, and so on. This is primarily the job of continuity and the

•
•
•
department heads, but the eye looking through the lens is often the best
way to spot problems.
Specifying the specific motion picture film raw stock(s) or type of
video camera to be used and any special processing or the workflow
for video footage.
Determining the exposure and informing the First AC what T-stop to
set on the lens.
Ensuring that all technical requirements are in order: correct film
speed, shutter angle, and so on.
Typically, when starting to light and set up a new scene, the assistant director
will ask for an estimate of how long it will take to be ready to shoot. This is not
an idle question, and it is very important to give an accurate estimate. The AD is
not just asking this to determine if the company is on schedule: there is another
important consideration.
````

![image/webp](data:image/webp;base64,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)

![image/webp](data:image/webp;base64,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)

````plaintext
Thought: Excavating Bongani's methodology and consulting prior exchanges.
````

**project_knowledge_search**

*Request*

````javascript
{
  "query": "Master Shots visual language composition camera movement shot selection",
  "max_text_results": 10
}
````

*Response*

````plaintext
MasterShots Volume 2_ 100 Ways - Christopher Kenworthy.pdf




“A terrific sequel to the first Master Shots. If there’s a cool way to move the camera, Christopher
Kenworthy has explained it to us. I can’t wait to get it in my students’ hands.”
— John Badham, director, Saturday Night Fever, WarGames; author, I’ll Be in My Trailer
“The most comprehensive and practical breakdown of shooting technique, Kenworthy’s Master
Shots, Volume 2, is required ‘bedside reading’ for anyone who’s serious about making movies.”
— Neill D. Hicks, author, Screenwriting 101: The Essential Craft of Feature Film Writing;
Writing the Action-Adventure Film: The Moment of Truth; and Writing the Thriller Film:
The Terror Within
“Christopher Kenworthy’s second volume of Master Shots will inspire every filmmaker to think
carefully about placement and movement of actors as seen through the camera lens. This book
increases the reader’s appreciation for the critical work of the cinematographer and the director as
they speak the language of film through images.”
—Mary J. Schirmer, screenwriter, screenwriting instructor, www.screenplayers.net
“Master Shots, Volume 2, is an inspiration for every director, cinematographer, and writer. When
breaking down a script, I always have Master Shots laying open within arm’s reach.”
— Stanley D. Williams, PhD., executive producer, director, Nineveh’s Crossing, LLC & SWC
Films
“Kenworthy has delivered one of the greatest no-filler books on camera technique I’ve ever seen,
pairing motivation and mechanics to achieve maximum visual impact. This isn’t a book of glossary
terms, it’s a game-changer.”
— Troy DeVolld, author, Reality TV: An Insider’s Guide to TV’s Hottest Market
“Master Shots, Volume 2, tells you how to achieve powerful dialogue scenes. Each explanation is
clearly and simply illustrated by stills from popular movies. Computer-generated illustrations
accompany each scene to show exactly where to place the camera. Master Shots, Volume 2 is
brilliant. A must-have companion to the first Master Shots.”
— Tony Levelle, author, Digital Video Secrets
“Any director should read this book to get a feel of the scope of potential in shooting dialogue.
And if you can convince your actors to read it as well, finally everyone will be on the same page on
set.”
— Erin Corrado, onemoviefivereviews.com
“This encyclopedia of 100 industry-standard master shots tells you how to best communicate any
storytelling idea — through framing, positioning, and dynamic movement. And it doesn’t just tell you
how, but why. After reading this book you’ll never neglect the importance of that living and breathing,
yet invisible actor in every scene: the camera.”
— Carl King, author, So, You’re a Creative Genius... Now What?



Published by Michael Wiese Productions
12400 Ventura Blvd. #1111
Studio City, CA 91604
(818) 379-8799, (818) 986-3408 (FAX)
mw@mwp.com
www.mwp.com
Cover design by Johnny Ink.
````

````plaintext
Master Shots Vol 3 - Christopher Kenworhty.pdf


“Finally! Someone has had the cleverness,
initiative, and imagination to set down on paper
a film language that has been passed down and
amalgamated only by word of mouth since the
days of Méliès and D. W. Griffith. Like Dr.
Johnson’s Dictionary of the English
Language, Christopher Kenworthy’s Master
Shots series seeks to make tangible and
permanent what otherwise might be gone with
the wind.”
— John Badham, Director, Saturday
Night Fever, WarGames, Short
Circuit; Author, I’ll Be in My Trailer
and John Badham on Directing;
Professor of Media Arts, The Dodge
School, Chapman University
“I’ve directed five features and a ton of TV and I
wish to God I’d had this book at the beginning

of my career. It’s an unbelievably
comprehensive resource for filmmakers. I
can’t wait to go back and look at Volumes 1 and
2.”
— Tom Lazarus, Screenwriter, Director,
Educator, Author, The Last Word
“You can take ten years to figure out lensing or
you can read this book and use that ten years to
create your art instead. Your choice.”
— Tony Levelle, Author, Digital Video
Secrets; Co-author, Producing with
Passion
“The latest installment in Kenworthy’s Master
Shots series lives up to its predecessors and
then some, offering up even more exciting
ways to frame and follow your action. All three
Master Shots books belong on the bookshelf
of every serious filmmaker.”
— Troy DeVolld, Author, Reality TV

“Christopher Kenworthy’s Master Shots Vol 3
is essential reading for both directors and
cameramen, and helpful to anyone who works
in or studies the art of filmmaking. The book is
clear and instructive with great visual samples.”
— Catherine Ann Jones, Author, The
Way of Story and Heal Your Self with
Writing; Screenwriter and TV Writer,
Touched by an Angel and The
Christmas Wife
“Christopher Kenworthy teaches readers the
nouns and verbs and participles and definite
articles of the language of cinema, equipping
them to tell stories on the screen with the
power that flows from fluency. Kenworthy
understands the interplay between image,
character, story, and emotion. He writes so that
his readers will understand, too.”
— Chris Riley, Author, Hollywood
Standard, 2nd Edition

“Master Shots Vol 3 continues this ultimate
reference-book series that is a must-have guide
for directors and cinematographers on how to
find interesting ways to tell your story
visually.”
— Marx H. Pyle, Producer/Co-host,
GenreTainment; Director/Creator,
Reality On Demand
“A fascinating look at amazingly simple ways to
use the camera, making this an essential read
for anyone looking to hone the craft of visual
storytelling.”
— Erin Corrado,
www.onemoviefiveviews.com
“Master Shots Vol 3 offers fabulous insight
into the purpose behind each shot.
````

````plaintext
MasterShots Vol 1_ 100 Advanced - Christopher Kenworthy (1).pdf
The way
Kenworthy breaks down
shots makes it so clear and
simple I was inspired to

pick up a camera and start
filming! And if you’re a
writer, you must read this.
Understanding the way shots
are actually set up will not
only give you a greater
visual sense but also
increase your ability to
write scripts that can
actually be filmed! This is a
worthy addition to any
filmmaker’s library.”
— Derek Rydall,
screenwriter, author of I
Could’ve Written a Better
Movie Than That! and
There’s No Business Like Soul

Business, founder,
ScriptwriterCentral.com
“Christopher Kenworthy’s
Master Shots provides an
excellent breakdown of the
underlying narrative
structure of scenes. No
matter how exciting car
chases or fistfights may be,
they are dramatically static
until the audience knows
the final result. Kenworthy
shows us how to make these
scenes work.”
— Neill D. Hicks, author of
Screenwriting 101: The
Essential Craft of Feature

Film Writing, Writing the
Action-Adventure Film: The
Moment of Truth and
Writing the Thriller Film: The
Terror Within
“‘Sometimes one punch can
tell the whole story….’ Such
begins the line in
Kenworthy’s vividly
written, descriptive book. A
winner.”
— Marisa D’Vari, author of
Creating Characters: Let
Them Whisper Their Secrets
“Kenworthy has captured
the unwritten and visual

language of the moving
picture in this essential
reference tool. Techies,
directors, and writers should
read this book to practically
and collectively harness this
powerful language.”
— Deborah S. Patz,
Executive in Charge of
Production, Magician’s
House
“Master Shots gives every
filmmaker out there the
blow-by-blow setup
required to pull off even the
most difficult of setups
found from indies to the big

Hollywood blockbusters. It’s
like getting all of the
magician’s tricks in one
book.”
— Devin Watson, producer,
The Cursed
“Good books on film
directing are rare,
specifically books which
focus on staging and framing
challenging sequences like
action scenes and chase
scenes. In this engagingly
written book, with helpful
illustrations from actual
films, Chris Kenworthy goes
a long way towards bridging

this knowledge gap.
Essential for beginners or
those looking for a refresher
before (or during) their next
film.”
— Christopher Riley, author
of The Hollywood Standard
“Master Shots is not only a
great how-to manual for
budding directors, it’s a
terrific book for anyone who
must communicate with
directors or understand their
language. Whether you’re a
director, writer, actor,
designer, or producer,
Master Shots helps you think

about storytelling from the
camera’s perspective,
making you a better
filmmaker and collaborator
no matter what your
discipline.”
— Chad Gervich, TV
writer/producer (Reality
Binge, Foody Call) and
author of Small Screen, Big
Picture: A Writer’s Guide to
the TV Business
“THIS BOOK SHOULD BE
BANNED! These are the
really cool tricks and
techniques of shooting
professional directors keep

secret just for themselves to
use.
````

````plaintext
Master Shots Vol 3 - Christopher Kenworhty.pdf
A strong scene is
determined from where you
put the camera and how you
position and direct your
actors. This is especially
true when shooting dialogue.
The techniques in Master
Shots, Vol. 2 ensure that
every plot point, every
emotion, and every subtle
meaning is communicated
clearly.
This is the first book to
show how important it is to
shoot dialogue well. What’s
the point of opening your

scene with a great camera
move, if you then just shoot
the actors like a couple of
talking heads? Master
Shots, Vol. 2 gives you
control of dialogue scenes,
whether you’re shooting two
characters or a room filled
with multiple conversations.
Using examples from well-
known films, the book gives
100 techniques, lavishly
illustrated with movie
frame-grabs, and overhead
diagrams, to show exactly
what you need to get the
required result. At all times,
the techniques have been

broken down to their core
points, so they will work on
a fully equipped Hollywood
set, or with the most basic
video camera.
“A terrific sequel to the
first Master Shots. If there’s
a cool way to move the
camera, Kenworthy has
explained it to us. I can’t
wait to get this book into
my students’ hands.”
— John
Badham,
director,
Saturday
Night

Fever,
WarGames;
author, I’ll
Be in My
Trailer
“Master Shots, Vol 2 will
inspire every filmmaker to
think carefully about
placement and movement of
actors as seen through the
camera lens. This book
increases the reader’s
appreciation for the critical
work of the
cinematographer and the
director as they speak the
language of film through

images.”
— Mary J.
Schirmer,
screenwriter,
screenwriting
instructor,
www.screenplayer
CHRISTOPHER
KENWORTHY has worked

as a writer, director, and
producer for the past ten
years. He directed the
feature film The Sculptor,
which played to sold-out
screenings in Australia and
received strong reviews.
Recent works include sketch
comedy for the BBC’s
Scallywagga, a title
sequence for National
Geographic Channel, visual
effects for 3D World, music
videos for Pieces of Eight
Records and Elefant
Records, and an animated
wall projection for The Blue
Room Theatre in Perth,

Australia. Kenworthy is the
author of the best-selling
Master Shots, two novels:
The Winter Inside and The
Quality of Light, and many
short stories. Current
projects include
screenwriting, several
directing assignments, and
the development of
additional Master Shots
applications.
$26.95 | 240 PAGES
| ORDER
NUMBER 167RLS |
ISBN:

9781615930555

CINEMATIC
STORYTELLING
THE 100 MOST
POWERFUL FILM
CONVENTIONS EVERY
FILMMAKER MUST
KNOW
JENNIFER VAN SIJL
BEST SELLER
How do directors use screen
direction to suggest conflict?
How do screenwriters

exploit film space to show
change? How does editing
style determine emotional
response?
Many first-time writers and
directors do not ask these
questions. They forego the
huge creative resource of the
film medium, defaulting to
dialog to tell their screen
story. Yet most movies are
carried by sound and
picture.
````

````plaintext
Cinematography Theory and Practice 3rd editions 2016.pdf
•
•
•
•
language of the lens
Figure 3.2. An extremely long lens compresses space and brings the cloud-covered sun dramatically into
this image from Apocalypse Now.
The language of the lens encompasses how the lens mediates and interprets the
physical world for us; how it “renders” the image in different ways that can be
used for effective visual storytelling. It is important for both the DP and the
director to understand how lenses can be used and what effects can be achieved
for particular visual purposes in the story. In this discussion, it includes also the
placement of the lens which is an important directorial decision in framing up
any shot—placement works together with the optical characteristics of the lens
in creating the overall effect. The key optical aspects of a lens include:
Perspective
Compression or expansion
Soft/hard
Contrast

THE LENS AND THE FRAME
As we use the term in this book, cinematic technique means the methods and
practices we use to add additional layers of meaning, nuance, and emotional
context to shots and scenes in addition to their objective content. The lens is one
of the prime tools in achieving these means. Together with selecting the frame, it
is also the area of cinematography in which the director is most heavily
involved.
FOREGROUND/MIDGROUND/BACKGROUND
As we discussed in Visual Language, one of the key elements of film is that we
are projecting three-dimensional space onto a two-dimensional plane. Except
where we want this flatness, it is a goal to recreate the depth that existed in the
scene.
A big part of this is to create shots with a foreground, midground, and
background. In the book Hitchcock/Truffaut, Hitchcock makes the point that a
basic rule of camera position and staging is that the importance of an object in
the story should equal its size in the frame.
Figure 3.3. The use of wide lenses to create deep focus was pioneered by cinematographer Gregg Toland
on films like The Long Voyage Home, seen here.
LENS PERSPECTIVE

As we discussed in the previous chapter, the fundamental aspect of the frame is
that it constitutes a selection of what the audience is going to see. Some things
are included, and some are excluded. The first decision is always where the
camera goes in relation to the subject, but this is only half of the job. Once the
camera position is set, there is still a decision to be made as to how much of that
view is to be included. This is the job of lens selection.
Human vision, including peripheral, extends to around 180°. Foveal (or
central) vision, which is more able to perceive detail, is around 40°. In 35mm
film, the 50mm is generally considered the normal lens. In fact, something
around a 40mm is closer to typical vision. In video, the “normal” lens varies
depending on the size of the video receptor—16mm film, 70mm, and all the
others would have a different “normal,” as do all video sensor sizes and formats.
````

````plaintext
The Cinematic Blueprint: Deconstructing the Shot List from Script Subtext to Visual Strategy
The Cinematography of Roger Deakins: How His Visual Storytelling Reflects His Philosophies - NET, https://eloncdn.blob.core.windows.net/eu3/sites/153/2020/06/11-Leu.pdf
24. The Visual Story | Summary, Quotes, FAQ, Audio - SoBrief, https://sobrief.com/books/the-visual-story
25. When abstract becomes concrete, naturalistic encoding of concepts in the brain - PubMed, https://pubmed.ncbi.nlm.nih.gov/39636743/
26. Visual Metaphors and Symbolism | Advanced Film Writing Class Notes - Fiveable, https://fiveable.me/advanced-film-writing/unit-8/visual-metaphors-symbolism/study-guide/JrYcdfH5MbAeNhsY
27. Master Shots: 100 Setups, Scenes, and Moves for Your Breakthrough Movie. The Director's Vision - CRAFT|Film School, https://www.craftfilmschool.com/userfiles/files/Master%20Shots%20Vol%203_%20The%20Director%E2%80%99s%20Vision_%20100%20Setups%2C%20Scenes%20and%20Moves%20for%20Your%20Breakthrough%20Movie.pdf
28. Villeneuve & Deakins on Visual Storytelling using Lighting, Composition, and Framing, https://www.youtube.com/watch?v=iWecEjVP61E
29. Roger Deakins & Denis Villeneuve: Why This Is Their Best Shot | A Cinematography Video Essay - YouTube, https://www.youtube.com/watch?v=vT0_tPnwsJ4
30. Birdman Director and Cinematographer Talk the Film's One Shot - Collider, https://collider.com/birdman-alejandro-inarritu-emmanuel-lubezki-interview/
31. 5 Coverage Methods For No-Budget Productions - Noam Kroll, https://noamkroll.com/5-coverage-methods-for-no-budget-productions/
32. TOP 6 QUOTES BY EMMANUEL LUBEZKI - A-Z Quotes, https://www.azquotes.com/author/35802-Emmanuel_Lubezki
33. The Psychology Of Film Editing & Its Impact On Your Audience - Noam Kroll, https://noamkroll.com/the-psychology-of-film-editing-the-impact-on-your-audience/
34. Camera Movement, Lenses & Framing in Film | Film Aesthetics Class Notes - Fiveable, https://fiveable.me/film-aesthetics/unit-4
35. Bruce Block's Visual Components For Filmmakers | PDF - Slideshare, https://www.slideshare.net/slideshow/bruce-blocks-visual-components-for-filmmakers/11355392
36. What is cinematography: Basics, elements & techniques - Adobe, https://www.adobe.com/creativecloud/video/production/cinematography.html
37. The Ultimate Guide to Color Theory, Color Correction, and Shot Composition in Filmmaking, https://delhi.cybertizemedia.com/post/the-ultimate-guide-to-color-theory-color-correction-and-shot-composition-in-filmmaking
38. The Essential Guide to Depth of Field [with Examples] - StudioBinder, https://www.studiobinder.com/blog/depth-of-field/
39. Lensing for Character Perspective - YouTube, https://www.youtube.com/watch?v=4SIQ03OztNo
40. Camera Focal Length and the Perception of Pictures - PMC - NIH, https://pmc.ncbi.nlm.nih.gov/articles/PMC4114730/
41. Film Blocking Tutorials: Master Camera Movement, Actor Positioning & Scene Composition, https://blog.studiovity.com/film-blocking-tutorials/
42.
````

````plaintext
Film Directing Shot By Shot.pdf
This type of software, now affordable for personal computers, lets the
filmmaker preview a camera move in full motion for any lens. Complex
locations can be designed on the computer within several hours. Once the
architectural or location plan is entered, camera moves can be animated in a
few minutes so that several versions can be compared side-by-side and stored
for reference. Key frames from two computer-rendered crane shots are shown
in Figures 18.6 and 18.7. Unlike the frame excerpts seen here, the computer
can play back the actual move in full motion on the screen. These examples
were created in Virtus WalkThrough, which operates in real time, permitting
the filmmaker to move through the three-dimensional space onscreen as if he
were really on location. Any camera move can be recorded in the program and
saved for comparison with any other camera move. The speed, timing, focal
length and the direction of the move can all be varied easily and minute
corrections can be made and viewed instantly.
Learning the Moves
Beyond the obvious advantage CAD programs offer for planning difficult
shots, this type of visualization is a tremendous tool for learning the subtleties
of camera movement. Like any skill that involves movement and perception,
such as dance or gymnastics, the control of camera choreography improves
with practice. Unfortunately, without a crane or dolly to work with on a regular
basis a filmmaker has little chance of refining his kinesthetic perception and
skills. The new CAD programs go a long ways towards solving this problem
by providing a very credible substitute for any type of camera move. At
present, Virtus WalkThrough offers the best learning environment for camera
movement since you are able to walk or fly through a location in real time once
it has been created. This allows the filmmaker to repeat a camera move until it
has the precise framing and ballistics he's looking for. Every move has a
unique feel and a crane shot with a steep ascent frames a narrative differently
from a crane shot that moves laterally while ascending. Using CAD programs
as a workshop, a filmmaker can acquire skills that previously took years to
learn.
Figure 18.6: CAD model, example one.

Figure 18.7: CAD model, example two.



T
19 THE TRACKING
SHOT
he tracking shot is used to follow a subject or explore space. This can be a
simple shot framing one subject or a complex sequence shot that connects
multiple story elements varying the staging and composition in a single flowing
movement. However, even the most intricate tracking shots can be understood
more easily if we look at the narrative and pictorial building blocks on which
they are based.
The Circle of Action and the Moving Camera
The circle of dramatic action is almost the same for the moving camera as it is
for the stationary camera we looked at in Chapter 13. For instance, if there is a
ballroom dance and the camera is on the floor surrounded by dancers, it is in
the action.
````

````plaintext
Cinematography Theory and Practice 3rd editions 2016.pdf
An image should convey meaning,
mode, tone, atmosphere, and subtext on its own—without regard to voice-over,
dialog, audio, or other explanation. This was in its purest essence in silent film,
but the principle still applies: the images must stand on their own.
Good composition reinforces the way in which the mind organizes
information. In some cases, it may deliberately run counter to how the eye/brain
combination works in order to add a new layer of meaning or ironic comment.
Composition selects and emphasizes elements such as size, shape, order,
dominance, hierarchy, pattern, resonance, and discordance in ways that give
meaning to the things being photographed that go beyond the simple: “here they
are.” We will start with the very basic rules of visual organization then move on
to more sophisticated concepts of design and visual language. The principles of
design and visual communication are a vast subject; here we will just touch on
the basics in order to lay the foundation for discussion.

Figure 2.3. The symmetrical balance created by the shadows and light on the floor is in visual tension with
the off-center figure in the frame; The Man Who Wasn’t There.
Figure 2.4. (bottom) The rhythm of repeated elements is an important component of this shot from Eternal
Sunshine of the Spotless Mind. The position of the figure also adds some visual tension.

•
•
•
•
•
•
•
•
The language of
film is further and
further away from
the language of the
theater and is closer
to music. It’s
abstract but still
narrative.
Emmanuel Lubezki
(Birdman, The
Revenant, Children
of Men)
DESIGN PRINCIPLES
Certain basic principles pertain to all types of visual design, whether in film,
photography, painting, or drawing. These techniques of basic design work
interactively in various combinations to add depth, movement, and visual force
to the elements of the frame. We can think of them as guidelines for visual
organization.
Unity
Balance
Visual tension
Rhythm
Proportion
Contrast
Texture
Directionality
UNITY
Unity is the principle that the visual organization
be a “whole,” self-contained, and complete. This
is true even if it is a deliberately chaotic or
unorganized composition. In Figure 2.2, this
climactic final shot from The Big Combo uses
frame-within-a-frame composition to tell the story
visually: having defeated the bad guys, the hero
and femme fatale emerge from the darkness into
the light of morning.

Figure 2.5. Lighting, perspective, choice of lens, and camera position combine to give this Gregg Toland
shot tremendous depth and threedimensionality in Citizen Kane.
BALANCE
Visual balance (or lack of balance) is an important part of composition. Every
element in a visual composition has a visual weight. These may be organized
into a balanced or unbalanced composition. The visual weight of an object is
primarily determined by its size but is also affected by its position in the frame,
its color, movement, and the subject matter itself.
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
The Cinematic Blueprint: Deconstructing the Shot List from Script Subtext to Visual Strategy
[31]
Master + Purposeful Cutaway
Low-Budget / Mid-Budget
Dialogue scenes with environment significance.
Offers utility for splicing takes; cutaways add tone/subtext; fast to shoot.[3, 31]
Requires the master to be flawless; can feel disjointed if cutaways are used as a crutch.
Standard Coverage (Master + CU/Reverse)
Mid-Budget / Big Budget
Standard dramatic dialogue, complex action needing clear orientation.
Maximum flexibility for the editor (Murch's Rule of Six); ensures continuity.[46, 47]
Slowest on set; high setup time; requires diligence in maintaining continuity.[50]
Multi-Cam Setup
Big Budget / Episodic TV
High-stakes dialogue, complex performances, non-repeatable action.[51]
Capture real-time reactions; minimizes performance fatigue; fastest for coverage volume.
Less creative control over individual frames; lighting compromises; technically complex rigging.[51]
5.3. Final Shot List Construction and Logistical Optimization
The final shot list must be a simple, scannable checklist for the crew.[45] It is essential to include all relevant data points for coordination: Scene number, Shot number, Location, Shot Type, Camera Angle, Movement, Lens (focal length), Equipment, Cast, and Continuity Notes.[44, 45, 50] Over-detailing the list should be avoided, as this diminishes its usefulness as a quick reference.[45]
The most effective shot lists function as logistics engines. Once the creative details are finalized, the list must be strategically arranged for the shooting day. This is achieved by grouping shots by setup, starting first by location and then by required technical configuration (same lens, same lighting setup, same support gear).[3, 50] This tactical decision transforms the shot list from a simple inventory of images into a flow chart for physical production, minimizing the setup time between shots and allowing the process to "hum along without too many hitches".[50] Complex, time-intensive shots should be scheduled early in the day when energy is high, while simple inserts are best left for the end of the day.[50]
VI. Conclusions and Recommendations
The creation of a critically and commercially successful shot list is a sophisticated exercise in translating psychological subtext and abstract emotional intent into quantifiable technical commands, governed by the theoretical framework of visual grammar.
The central mechanism for generating dynamic storytelling is the systematic application of the Principle of Contrast & Affinity across the seven visual components. By consciously logging every decision as either affinity (similarity, stability) or contrast (difference, dynamic), filmmakers can precisely control the emotional intensity of every frame and ensure the visual structure aligns perfectly with the narrative progression. The DP's advanced role is detecting abstract directorial intent and deconstructing it into simultaneous, concrete visual commands involving lens psychology, compositional choice, and lighting tone.
````

![image/webp](data:image/webp;base64,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)

![image/webp](data:image/webp;base64,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)

````plaintext
Thought: Synthesized cinematography foundations and strategized targeted research approach.
````

Perfect! I have comprehensive cinematography knowledge from your project files. Now let me search through past conversations to see your specific approaches, questions, and workflows you've discussed.

**conversation_search**

*Request*

````javascript
{
  "query": "cinematography preparation shot list visual language breakdown script analysis",
  "max_results": 8
}
````

*Response*

````plaintext
No matching conversations found.
````

````plaintext
Thought: No matches found. Let me try a different search with broader terms.
````

**conversation_search**

*Request*

````javascript
{
  "query": "film production budget crew gear lighting camera",
  "max_results": 8
}
````

*Response*

````plaintext
No matching conversations found.
````

````plaintext
Thought: Attempting targeted search with specialized terminology.
````

**conversation_search**

*Request*

````javascript
{
  "query": "director collaboration department roles shot deck FLIM.AI location scouting",
  "max_results": 8
}
````

*Response*

````plaintext
No matching conversations found.
````

````plaintext
Thought: Formulated clarifying questions to architect comprehensive system design.
````

Alright, I've absorbed your comprehensive cinematography knowledge base and understand the scope of what you're building. Before I launch into deep research and system architecture, I need to clarify a few critical factors:

**1. Timeline & Scope Priority**

Are you building this for:
- **Immediate use** on your current film in prep (minimum viable version first, iterate later)?
- **Full vision** upfront (comprehensive system architecture, then implement all at once)?
- **Hybrid** approach (design full system, but identify which 2-3 agents to build first)?

**2. Most Critical Agent First**

Given you're in active prep right now, which agent would give you the most immediate relief:
- **Voice Transcription + Note Sorting** (capture your director conversations and auto-sort into shot list/action items)?
- **Visual Language Generator** (feed it script, get back lookbook/references/initial shot ideas)?
- **Budget/Gear List Generator** (input requirements, get back actual costs and equipment packages)?

**3. Existing Infrastructure Status**

What's already set up vs needs to be built:
- **Firebase**: Project created and configured, or need to set up?
- **Run Pod**: Account active, or need to create?
- **GitHub**: Repos ready for this project, or start fresh?
- **Obsidian**: Still pending setup as you mentioned?
- **Whisper**: Already installed on Mac?
- **Claude SDK/API keys**: All configured?

These answers will help me design the optimal architecture for YOUR specific situation rather than a theoretical ideal system.



## Prompt:
11/19/2025, 12:22:10 AM

Full vision upfront (comprehensive system architecture, then implement all at once). Voice Transcription + Note Sorting (capture your director conversations and auto-sort into shot list/action items) is the most important right now. I can give it voice notes or text transciptions. I have both. I have not setup a specific firebase, but I have firebase. I have a runpod account. I will start a github repo for this.  Obsidian is still pending. I have MacWHisper on my computer that can bathc proceess audio and use a watch folder to auto process. I ahve teh API keys.



## Response:
11/19/2025, 12:30:15 AM

````plaintext
Thought: Architected comprehensive AI cinematography agent system with voice transcription priority.
````

Alright Bongani, let's architect this beast. I've absorbed your cinematography knowledge base and I'm going to design the complete system, then give you everything you need to hand to Claude Code for rapid implementation.

# 🎬 THE CINEMATOGRAPHY AI CLONE SYSTEM
## Full Vision Architecture - "VISION AI" 

---

## 🎯 EXECUTIVE SUMMARY

You're building an agentic AI system that replicates your complete cinematography workflow from script receipt to production day, with emphasis on voice-first capture, intelligent note sorting, and automated document generation. This system integrates with your existing neurodivergent-optimized workflow and reduces your prep workload from weeks to hours.

**Primary Output**: Read script today → Complete shot list, visual language doc, gear lists, and budget ready tomorrow.

**Core Innovation**: Voice-first capture of all director conversations, location scouts, and creative thoughts, with AI that understands cinematography deeply enough to auto-sort into the right documents and formats.

---

## 🏗️ SYSTEM ARCHITECTURE OVERVIEW

### THE AGENT ECOSYSTEM (13 Core Agents + 1 Orchestrator)

```
VOICE INPUT → Transcription Agent → Note Intelligence Agent → [ORCHESTRATOR] → Specialized Agents → OUTPUT DOCUMENTS
                                                                        ↓
                                                            Firebase + GitHub Storage
```

---

## 📋 COMPLETE AGENT SPECIFICATIONS

### **AGENT 0: THE ORCHESTRATOR** 
*The brain that routes everything*

**Purpose**: Central intelligence that receives all inputs, understands context, and routes tasks to appropriate specialist agents.

**Capabilities**:
- Analyzes incoming request type (voice note, script, image, question)
- Maintains conversation context across all agents
- Handles agent-to-agent communication
- Manages parallel processing of multiple agents
- Prioritizes tasks based on production timeline
- Stores all outputs to Firebase with proper metadata
- Commits all changes to GitHub with meaningful commits

**Technical Stack**:
- Claude SDK for orchestration logic
- Firebase Functions for serverless triggers
- Redis for state management between agents
- WebSocket connection for real-time updates

**Integration Points**:
- Receives from: MacWhisper watch folder, direct text input, uploaded files
- Sends to: All specialist agents based on task analysis
- Stores to: Firebase Firestore for metadata, Cloud Storage for files, GitHub for versions

---

### **AGENT 1: VOICE TRANSCRIPTION AGENT** ⭐ PRIORITY
*Your voice becomes text, automatically*

**Purpose**: Monitor, transcribe, and preprocess all audio inputs using MacWhisper's batch processing.

**Workflow**:
1. MacWhisper watches designated folder(s)
2. Auto-transcribes any new audio files
3. Agent monitors MacWhisper output folder
4. Picks up completed transcriptions
5. Adds metadata (timestamp, duration, speaker identification if possible)
6. Formats for Note Intelligence Agent
7. Stores raw transcript in Firebase

**Configuration**:
```javascript
{
  watchFolders: [
    "/Users/bongani/Dropbox/Voice Notes",
    "/Users/bongani/Voice Memos",
    "/Users/bongani/Director Conversations"
  ],
  macWhisperOutputFolder: "/path/to/macwhisper/output",
  processingInterval: "real-time", // Check every 10 seconds
  speakerDiarization: true, // If MacWhisper supports it
  outputFormat: "structured_json"
}
```

**Output Structure**:
```json
{
  "transcript_id": "uuid",
  "timestamp": "2025-11-19T14:30:00Z",
  "duration_seconds": 342,
  "raw_text": "full transcript...",
  "speakers": ["Bongani", "Director"],
  "audio_file_path": "path/to/original.m4a",
  "processing_status": "complete"
}
```

**Technical Implementation**:
- Node.js file watcher using `chokidar`
- Firebase Cloud Functions triggered on new transcriptions
- Claude API for any text cleanup/formatting

---

### **AGENT 2: NOTE INTELLIGENCE AGENT** ⭐ PRIORITY
*Understands cinematography context and auto-sorts everything*

**Purpose**: The most sophisticated agent - takes raw transcripts or text and intelligently categorizes, extracts, and routes information into the correct cinematography documents.

**Core Intelligence** - This agent knows:
- Cinematography terminology and workflow
- Script breakdown structure
- Shot list formats
- Budget categories
- Department collaboration patterns
- Production timeline phases

**Processing Pipeline**:

**STEP 1: Context Identification**
```
Analyzes transcript to determine conversation type:
- Director collaboration (shot discussion, visual approach, story)
- Location scout (lighting notes, practical considerations)
- Tech scout (specific gear needs, rigging requirements)
- Department meeting (art, costume, G&E collaboration)
- Personal creative notes (visual references, ideas)
- Budget discussion (rates, rentals, scheduling)
- Production logistics (schedule, crew, locations)
```

**STEP 2: Entity Extraction**
```
Identifies and extracts:
- Scene numbers/names
- Shot descriptions  
- Camera specs (lens, movement, angle)
- Lighting notes (units, gels, motivation)
- Grip requirements (rigging, support)
- Color/tone references
- Action items and owners
- Questions that need answers
- Research tasks
- Collaboration needs
```

**STEP 3: Document Routing**
```
Sorts extracted information into appropriate documents:

SHOT LIST:
- Scene number
- Shot number  
- Shot description
- Camera specs
- Lens choice
- Movement type
- Coverage notes

LIGHTING PLAN:
- Scene/setup
- Key light approach
- Fill strategy
- Practical requests to art dept
- Specific units needed
- Gel choices
- Mood/tone notes

CAMERA DEPARTMENT NOTES:
- Camera body
- Lens package
- Support gear (dolly, crane, sticks)
- Special requirements (underwater, car mounts)
- Focus/framing notes

GRIP & ELECTRIC LISTS:
- Specific gear callouts
- Rigging needs
- Stands/hardware
- Flags/cutters/diffusion

PRODUCTION COORDINATION:
- Questions for producers
- AD schedule requests
- Location department needs
- Art department collaboration
- Costume/makeup considerations

PERSONAL TO-DO:
- Research tasks
- Tests to conduct
- References to find
- Decisions to make
- People to contact

BUDGET ITEMS:
- Gear rental needs
- Special equipment costs
- Crew additions
- Location requirements
```

**STEP 4: Action Item Extraction**
```
Creates structured tasks:
{
  "task": "Test anamorphic lenses for night scenes",
  "priority": "high",
  "category": "camera_test",
  "deadline": "2 weeks before production",
  "assigned_to": "Bongani + 1st AC",
  "dependencies": ["Lens package confirmation", "Night exterior location locked"]
}
```

**STEP 5: Smart Synthesis**
```
When multiple conversations reference same scene:
- Combines information intelligently
- Flags contradictions
- Suggests decisions needed
- Maintains conversation thread
```

**Advanced Features**:
- **Pattern Recognition**: "Bongani always wants 5:1 lighting ratios for dramatic scenes" → auto-suggests when new dramatic scene discussed
- **Incomplete Information Flagging**: "Director mentioned 'that dolly move' but no specifics" → creates follow-up question
- **Department Dependency Mapping**: "Bongani needs practical bulbs at 3200K" → auto-generates request to Production Designer
- **Visual Language Consistency**: Tracks visual approach across scenes, flags when shot description doesn't match established style

**Output Example**:

From transcript: *"So for the kitchen scene, I'm thinking we go handheld, something intimate, maybe 35mm on the FX6. Keep it warm, practical motivated from that window we saw. I want to feel the morning light. Oh, and we need to talk to Sarah about dimming those overhead lights."*

Generates:
```
SHOT LIST UPDATE:
Scene 12 - Kitchen Morning
- Shot type: Handheld coverage
- Lens: 35mm
- Camera: Sony FX6
- Mood: Intimate, warm
- Lighting motivation: Window (natural morning light)

LIGHTING PLAN:
Scene 12 - Kitchen
- Approach: Natural/practical motivated
- Key source: Window (morning sunlight)
- Color temp: Warm (3000-3200K)
- Note: Overhead practicals need dimming capability

COLLABORATION TASK:
To: Production Designer (Sarah)
Re: Scene 12 Kitchen
Request: Overhead practical lights need to be dimmable
Priority: Medium
Context: Want to control levels for morning light balance

PERSONAL TO-DO:
- Confirm FX6 availability for handheld work
- Test 35mm look for kitchen intimacy
- Scout kitchen window timing for sun angle
```

**Technical Implementation**:
- Claude Sonnet 4.5 API for intelligence (needs the reasoning capability)
- Custom prompt templates for each document type
- Structured output using Claude's JSON mode
- Embeddings for context retrieval (previous conversations about same scene)
- Firebase for storage and retrieval

---

### **AGENT 3: SCRIPT ANALYSIS AGENT**
*Multiple deep reads, extracting everything*

**Purpose**: Performs the comprehensive script analysis Bongani does manually - multiple passes for different aspects.

**The 7-Pass Analysis** (Based on your DP Process doc):

**PASS 1: Story Structure**
- Three-act breakdown
- Story beats and turning points
- Dramatic question
- Character introductions
- Scene purposes
- Narrative flow

**PASS 2: Emotion & Subtext**  
- Underlying objectives per scene
- Emotional arcs
- What's NOT being said
- Psychological states
- Thematic elements
- Scene subtexts

**PASS 3: Visual Opportunities**
- Moments that need visual emphasis
- Contrast/affinity opportunities per scene
- Key image identification
- Symbolic visual moments
- Where camera becomes subjective

**PASS 4: Technical Requirements**
- Location needs (practical, stage, exterior/interior)
- Time of day for each scene
- Special gear requirements (crane, underwater, drone)
- VFX shots
- Stunt coordination needs
- Complex rigging requirements

**PASS 5: Scene-by-Scene Breakdown**
- Cast per scene
- Extras needed
- Props list
- Costume changes
- Makeup/hair notes  
- Special effects
- Animals/children

**PASS 6: Character Analysis**
- Character arcs
- Emotional journey per character
- Visual representation of character state
- How to SHOW character changes
- Blocking implications

**PASS 7: Master Shot Strategy**
- Coverage approach per scene type
- Action sequence blocking
- Dialogue scene strategies
- Complex staging needs
- Editor coverage requirements

**Output Format**: Comprehensive analysis document with all seven passes clearly sectioned, cross-referenced, and tagged by scene number.

**Technical Implementation**:
- Claude Opus 4.1 for deep analysis (need that horsepower)
- Structured prompt that enforces the 7-pass method
- Output to Markdown for readability
- Firebase storage with searchable metadata
- Export to PDF for sharing with director

---

### **AGENT 4: VISUAL LANGUAGE AGENT**
*Translates story into specific visual strategies*

**Purpose**: Takes script analysis and generates the complete visual approach using Bruce Block's Visual Structure principles and cinematography theory.

**Core Framework** - Analyzes and applies:

**1. The 7 Visual Components** (Bruce Block):
```
For each major scene/sequence, defines:

SPACE: Deep/Flat/Limited/Ambiguous
- Lens choice implications  
- Depth of field strategy
- Foreground/mid/background staging

LINE: Horizontal/Vertical/Diagonal/Curved
- Composition orientation
- Emotional implications
- Stability vs. dynamic

SHAPE: Geometric/Organic/Positive/Negative
- Frame composition
- Character/environment relationship
- Visual motifs

TONE: High key/Low key/Contrast ratio
- Lighting approach
- Mood establishment
- Psychological state

COLOR: Palette/Temperature/Saturation/Symbolism
- Color script per scene
- Emotional associations
- Character color relationships

MOVEMENT: Camera/Subject/Speed/Direction
- When static/when moving
- Type of movement (dolly, pan, handheld)
- Choreography approach

RHYTHM: Cutting/Duration/Tempo/Visual beats
- Shot duration implications
- Scene pacing strategy
- Visual punctuation
```

**2. Contrast & Affinity Mapping**:
```
Scene-by-scene analysis of whether to use:
AFFINITY (similarity, calm, unity): Similar compositions, consistent color, smooth movement
CONTRAST (difference, intensity, conflict): Varied compositions, color shifts, dynamic movement

Creates "intensity graph" of visual energy across film
```

**3. Lens Psychology**:
```
Wide Lenses (18-35mm): Expansive, inclusive, environmental context
Normal Lenses (40-50mm): Neutral, realistic, intimate
Telephoto Lenses (85mm+): Isolated, compressed, focused, voyeuristic

Maps lens choices to character psychology and story beats
```

**4. Camera Position & Angle**:
```
Eye Level: Neutral, observational
Low Angle: Power, dominance, heroic
High Angle: Vulnerability, weakness, overview  
Dutch/Canted: Instability, unease, chaos

Subjective vs. Objective camera positioning
```

**5. Reference Gathering**:
```
Searches and compiles:
- Film references (similar scenes, visual approaches)
- Photography references (lighting, composition)
- Painting references (color, mood)
- Architecture/design references (space, shape)

Organized by scene/visual element
```

**Output**: 
- Visual Language Bible (comprehensive document)
- Lookbook/Moodboard (curated images)
- Shot Inspiration (specific reference frames)
- Visual Components chart per major scene
- Lens/camera strategy document

**Technical Implementation**:
- Claude Sonnet 4.5 for analysis
- Integration with Shot Deck API (if available)
- Web scraping for FLIM.AI references
- Multimodal AI (Run Pod) for image analysis
- Firebase for image storage
- Auto-generates PDF lookbook

---

### **AGENT 5: SHOT LIST GENERATOR AGENT**
*Creates comprehensive, production-ready shot lists*

**Purpose**: Takes script analysis + visual language and generates detailed, organized shot lists optimized for production.

**Generation Strategy**:

**Phase 1: Coverage Analysis**
```
For each scene, determines appropriate strategy:
- Minimal Coverage (single camera angle, long takes)
- Standard Coverage (master + OTS + CU + inserts)
- Maximum Coverage (multi-angle, safety, editorial options)
- Oner/Sequence Shot (choreographed continuous shot)
- Action Coverage (multiple cameras, crash cams, high frame rate)
```

**Phase 2: Shot Design**
```
For each shot, specifies:
SHOT NUMBER: 15A
SCENE: 12 - Kitchen Morning  
SHOT TYPE: Medium handheld
FRAMING: Medium shot, chest up, Sarah
LENS: 35mm (T2.8)
CAMERA: Sony FX6
MOVEMENT: Handheld follow, smooth
ANGLE: Eye level, slight offset
MOTIVATION: POV proximity, intimate
COVERAGE PURPOSE: Master for action, edit point options
LIGHTING NOTES: Window key, practical fill
SPECIAL REQUIREMENTS: Wireless focus, cage rig
ESTIMATED DURATION: 45 seconds
SETUP TIME: 15 minutes
```

**Phase 3: Production Optimization**
```
Reorganizes shots by:
- Location (all kitchen shots together)
- Lighting setup (similar setups grouped)
- Camera configuration (same lens package)
- Time of day requirements

Creates "shooting order" vs. "scene order"
```

**Phase 4: Overhead/Floor Plans**
```
Generates (or notes need for):
- Camera positions marked
- Actor blocking paths
- Lighting unit placement
- Grip equipment locations
- 180-degree line
- Safety zones
```

**Output Formats**:
1. **Comprehensive Shot List** (scene order) - for creative review
2. **Production Shot List** (shooting order) - for actual filming
3. **Department Shot Lists** (filtered by dept) - for G&E, Camera, etc.
4. **Overhead Diagrams** (when complex) - visual staging
5. **One-liner Summary** (quick reference) - for call sheets

**Advanced Features**:
- **Multiple Coverage Options**: Generates 2-3 approaches per scene, Bongani picks preferred
- **Editorial Awareness**: Ensures proper coverage for editing (Rule of Six)
- **Continuity Notes**: Flags potential continuity issues
- **Time Estimates**: Predicts setup/shooting time per shot
- **Gear Implications**: Notes when shot requires special equipment

**Technical Implementation**:
- Claude Sonnet 4.5 for shot design
- Template system for different scene types
- Overhead diagram generation (SVG or integration with shot design tools)
- Export to multiple formats (Excel, PDF, CSV for other tools)
- Firebase storage + GitHub version control

---

### **AGENT 6: BUDGET AGENT**
*Real numbers, real fast*

**Purpose**: Generates accurate budgets based on gear lists, crew needs, and production requirements.

**Data Sources**:
```
RENTAL HOUSES (needs API integration or web scraping):
- Panavision rates
- ARRI Rental rates  
- Local camera houses
- Grip & Electric rental houses
- Specialty equipment vendors

CREW RATES:
- Local rate guides (IATSE, regional standards)
- Personal database of previous crew deals
- Market rate research

LOCATION COSTS:
- Permit fees by city/region
- Common location day rates
- Insurance requirements

PRODUCTION COSTS:
- Expendables
- Transportation
- Catering minimums
- Miscellaneous
```

**Budget Generation Process**:

**Camera Department Budget**:
```
CAMERA BODY: Sony FX6 x2 @ $750/day x 10 days = $15,000
LENS PACKAGE: Cooke Anamorphic Set @ $2,500/day x 10 days = $25,000  
SUPPORT: Dolly + Track @ $500/day x 6 days = $3,000
ACCESSORIES: Filters, Mattebox, Follow Focus = $1,200
CREW:
  DP: $2,500/day x 10 days = $25,000
  Operator: $850/day x 10 days = $8,500
  1st AC: $650/day x 10 days = $6,500
  2nd AC: $500/day x 10 days = $5,000
  DIT: $750/day x 10 days = $7,500

SUBTOTAL CAMERA: $96,700
```

**Grip & Electric Budget**:
```
[Similar detailed breakdown]
Lighting units, grip gear, labor, expendables
```

**Overall Production Budget**:
```
Rolls up all departments
Adds contingency (10%)
Provides budget tiers (minimal/preferred/ideal)
```

**Budget Variations**:
- **No-Budget/Micro**: Owned gear, favors, minimal crew
- **Low-Budget**: Rental packages, small crew, limited days
- **Mid-Budget**: Full packages, standard crew, proper time
- **High-Budget**: Best gear, full crew, padding

**Output**:
- Detailed line-item budget (Excel/Google Sheets format)
- Department subtotals
- Alternative package options ("save $5K by swapping X for Y")
- Justification notes for creative choices
- Rental house contact info and availability

**Technical Implementation**:
- Web scraping for current rental rates (or manual database updates)
- Claude for alternative package suggestions
- Google Sheets API for export
- Budget templates specific to different production scales
- Firebase for historical budget data analysis

---

### **AGENT 7: RESEARCH AGENT NETWORK**
*Multiple specialized researchers*

Four specialized research agents that know how to find different types of information:

**7A: CREATIVE RESEARCHER**
```
Searches for:
- Film references (IMDb, Letterboxd, ASC articles)
- Director interviews about visual approach
- Behind-the-scenes content
- ASC podcasts relevant to similar projects
- Cinematographer websites/reels

Sources: Web search, Shot Deck, FLIM.AI, YouTube, ASC Magazine archives
```

**7B: TECHNICAL RESEARCHER**  
```
Searches for:
- Camera/lens specifications
- Lighting techniques for specific scenarios
- Grip rigging solutions
- Workflow optimization
- Camera test results and comparisons
- New gear releases

Sources: Manufacturer specs, CineD, Y.M.Cinema, No Film School, Roger Deakins Forum
```

**7C: VISUAL RESEARCHER**
```
Searches for:
- Photography (specific photographers for mood/style)
- Fine art (paintings, sculpture, installation)
- Architecture and interior design
- Fashion photography
- Graphic design and color theory

Sources: Photographer websites, museum collections, Pinterest, Behance, photography books
```

**7D: STORY RESEARCHER**
```
Searches for:
- Similar stories and their visual treatment
- Thematic precedents
- Character arc visual representation examples
- Genre conventions and innovations
- Narrative structure analysis

Sources: Film analysis sites, screenwriting resources, academic articles
```

**Coordination**: Orchestrator determines which researcher(s) to deploy based on query type.

---

### **AGENT 8: COLLABORATION COORDINATOR AGENT**
*Knows every department's role and manages dependencies*

**Purpose**: Understands film production hierarchy and collaboration needs, ensuring proper interdepartmental communication.

**Department Knowledge Base**:
```
PRODUCTION:
- Producers: Budget, schedule, deals
- UPM: Resources, logistics, problem-solving
- Line Producer: Daily operations, spending
- Production Coordinator: Communication hub
- ADs: Schedule, safety, set management

CAMERA:
- DP: Visual approach, lighting, camera
- Operator: Framing, movement execution
- 1st AC: Focus, camera prep, lens
- 2nd AC: Loading, slate, reports, camera moves
- DIT: Data, on-set color, monitoring

GRIP:
- Key Grip: Rigging, support, logistics
- Dolly Grip: Camera movement execution
- Grips: Physical support, flags, diffusion

ELECTRIC:
- Gaffer: Lighting design execution
- Best Boy Electric: Logistics, crew, equipment
- Electricians: Units, power, rigging

ART:
- Production Designer: Visual world creation
- Art Director: Set construction, dressing
- Set Decorator: Dressing, props
- Props Master: Practical objects

COSTUME/HAIR/MAKEUP:
- Costume Designer: Character through clothing
- Key Hair: Hair styling and continuity
- Key Makeup: Makeup and special effects

POST:
- Editor: Story assembly, pacing
- Colorist: Final color grade
- VFX Supervisor: Digital effects integration

SOUND:
- Production Sound: On-set recording
- Sound Designer: Post audio creation
```

**Dependency Mapping**:
```
Example: "DP wants practical bulbs at 3200K"

Agent analyzes:
- Primary: Production Designer (controls practicals)
- Secondary: Gaffer (may need dimming control)
- Tertiary: Art Director (installation logistics)

Generates communication sequence:
1. Email to Production Designer with request
2. Loop in Gaffer for dimming discussion
3. Add to tech scout agenda
4. Create follow-up task to confirm
```

**Collaboration Templates**:
```
DP → DIRECTOR: Creative discussions, shot approval, visual alignment
DP → PRODUCER: Budget, schedule, resource needs
DP → AD: Timing, schedule, crew calls
DP → PRODUCTION DESIGNER: Color palette, practicals, set considerations
DP → GAFFER: Lighting design, units, gels, approach
DP → KEY GRIP: Support, rigging, movement
DP → COSTUME: Color coordination, practical considerations
DP → SOUND: Frame space, boom shadows, lighting noise
DP → VFX: Plate requirements, tracking marks, lighting ref
DP → EDITOR: Coverage strategy, preferred takes
```

**Output**: 
- Identifies who needs to know what
- Drafts appropriate communications
- Tracks collaborative decisions
- Flags when dependencies block progress

---

### **AGENT 9: COMMUNICATION AGENT**
*Writes all external communications*

**Purpose**: Drafts professional emails, memos, documents for all external communication, ready to send.

**Communication Types**:

**1. Department Emails**
```
To: Production Designer
Subject: Scene 12 Kitchen - Practical Lighting Request

Hi [Name],

For Scene 12 (Kitchen Morning), we're planning to use the natural window light as our key source. To balance this effectively, we'll need the overhead practical lights to be dimmable.

Could we discuss options for:
- Installing dimmer-capable fixtures, or  
- Using practical bulbs we can control via our dimmer board?

Our gaffer [Name] is looped in and can coordinate on the technical details.

Thanks!
Bongani
```

**2. Crew Memos**
```
Subject: Camera Department - Scene 45 Special Requirements

Team,

For Scene 45 (Car Chase), please note:

SPECIAL GEAR:
- Russian Arm with Stabileye head
- 2x GoPros for interior car mounts
- Wireless focus + monitor system

CREW:
- Need additional utility for rigging
- Stunt coordinator will be on set

TIMING:
- Rig day: [Date]
- Shoot day: [Date]
- Location: [Address]

Questions to [Contact]

Best,
Bongani
```

**3. Call Sheets** (if needed)
```
Formatted properly with:
- Scene numbers
- Cast call times
- Crew call times
- Equipment needs
- Location details
- Special requirements
```

**4. Shot List Distribution**
```
Creates department-specific versions:
- Camera department: All shots with camera/lens specs
- G&E: Lighting notes per setup
- AD: Setup time estimates and sequence
- Production: Special requirements and costs
```

**5. Budget Presentations**
```
Formats budget data for:
- Producer deck (high-level, alternatives)
- Department breakdown (detailed line items)
- Executive summary (total with justification)
```

**Advanced Features**:
- **Tone Matching**: Adjusts formality based on recipient
- **Follow-up Tracking**: Notes what was sent, when response expected
- **Attachment Gathering**: Pulls referenced docs from Firebase
- **Gmail Integration** (future): Creates drafts directly in inbox

**Technical Implementation**:
- Claude for communication drafting
- Templates for common communication types
- Integration with Communication Coordinator for recipient determination
- Firebase storage of sent communications
- Could integrate with Gmail API to create drafts

---

### **AGENT 10: TASK MANAGEMENT AGENT**
*Your intelligent to-do system*

**Purpose**: Maintains comprehensive task list combining standard DP workflow with custom additions, prioritizes, and tracks progress.

**Task Sources**:

**1. Standard DP Checklist** (from DP Process doc):
```
PRE-PRODUCTION:
□ Script read - story
□ Script read - emotion/subtext
□ Script read - visual opportunities
□ Script read - technical requirements
□ Find visual references
□ Create lookbook
□ Meet with director - shot list
□ Meet with director - visual approach
□ Department meetings (PD, Gaffer, Key Grip)
□ Location scout
□ Tech scout
□ Camera tests
□ Costume/makeup tests
□ Gear selection
□ Crew hiring
□ Budget creation
□ Schedule review

PRODUCTION:
□ Daily call sheet review
□ Equipment check
□ Blocking with director
□ Lighting design
□ Shot execution
□ Dailies review

POST:
□ Color timing
□ VFX review
□ Final delivery
```

**2. Dynamic Task Capture**:
```
From voice notes: "Remember to test those anamorphics"
From conversations: "Need to call that gaffer Sarah recommended"
From shot list: "Research car mount solutions for Scene 45"
From collaboration: "Wait for AD's revised schedule before confirming crew"
```

**3. Task Intelligence**:
```
Each task gets:
- Priority (High/Medium/Low)
- Category (Creative/Technical/Logistic/Budget/Collaboration)
- Deadline (relative to production start)
- Dependencies (what must happen first)
- Owner (if not Bongani)
- Estimated time
- Status (Not Started/In Progress/Blocked/Complete)
```

**4. Smart Prioritization**:
```
Factors:
- Production timeline (things needed sooner = higher priority)
- Dependencies (unblocking others = higher priority)
- Bongani's current context (prep phase vs. production)
- Energy level (complex tasks during peak hours)
- Collaboration needs (requiring others' input = coordinate early)
```

**5. Daily Task Recommendations**:
```
"Based on your timeline, today you should:
1. Review director's script notes from yesterday [30 min]
2. Finalize shot list for Scene 12-15 [1 hour]
3. Email production designer about practical lights [15 min]

You have 3.5 hours of focused work available in your peak window (11 AM-2 PM)."
```

**Output Formats**:
- Daily task list (prioritized for that day)
- Weekly overview (what needs to happen this week)
- Master list (everything, organized by category)
- Blocked items (waiting on someone else)
- Completion tracking (progress visualization)

**Integration**:
- Can send to iOS Reminders for notification
- Can integrate with Motion for AI scheduling
- Updates based on other agents' outputs

---

### **AGENT 11: GEAR LIST GENERATOR AGENT**
*From shot list to specific equipment orders*

**Purpose**: Analyzes shot list and generates comprehensive, organized gear lists for each department.

**Analysis Process**:

**From Shot List to Requirements**:
```
Shot: "Dolly push-in, 50mm, low angle, dramatic lighting"

Generates requirements:
CAMERA:
- Camera body (specified in shot list)
- 50mm lens
- Low-angle mounting solution (cheese plate, offset arm)

GRIP:
- Dolly
- Track (length calculated from shot description)
- Low-angle adapter for dolly
- Apple boxes for height adjustment

ELECTRIC:
- (Looks at "dramatic lighting" + scene analysis)
- Determined from Lighting Plan
```

**Department-Specific Lists**:

**CAMERA DEPARTMENT**:
```
CAMERA BODIES:
□ Sony FX6 x2 (A-Cam, B-Cam)
□ GoPro Hero 12 x2 (car mounts, crash cam)

LENSES:
□ Cooke Anamorphic Set (25, 32, 50, 75, 100mm)
OR
□ Zeiss Super Speeds (18, 25, 35, 50, 85mm)

SUPPORT:
□ Dana Dolly + 8ft track
□ Sachtler Video 25 Fluid Head
□ Sticks (medium, baby)
□ Doorway dolly
□ Steadicam rig

ACCESSORIES:
□ Wireless follow focus (3x motors)
□ Wireless video (Teradek Bolt 4K)
□ SmallHD 703 monitor x2
□ Mattebox + filter trays
□ ND filters (.3, .6, .9, 1.2)
□ Polarizer
□ Camera cases
□ Media (CFexpress cards, SD cards)
□ Batteries + chargers

SPECIALTY:
□ Car door mount rig
□ Suction cup mounts x4
□ Underwater housing
```

**GRIP DEPARTMENT**:
```
SUPPORT:
□ C-stands x12 (with arms + knuckles)
□ Combo stands x8
□ Low boys x4
□ Hi-boys x4
□ Apple boxes (full, half, quarter, pancake)
□ Sandbags (25lb, 15lb)

RIGGING:
□ Speed rail (assorted lengths)
□ Clamps + adapters
□ Chain vice grips
□ Come-alongs
□ Scaffolding (if needed)

MODIFIERS:
□ 8x8 solid frame + fabric
□ 12x12 silk frame + fabric
□ 4x4 floppy + fabrics (solid, single, double)
□ Flags (18x24, 24x36)
□ Dots + fingers kit
□ Cutters (2x3, 4x4)

SPECIALTY:
□ Crane (if specified in shot list)
□ Hostess tray
□ Tube stretchers
□ Bead board
```

**ELECTRIC DEPARTMENT**:
```
LIGHTS:
□ ARRI SkyPanel S60 x4
□ ARRI M18 HMI x2
□ ARRI 650W Fresnel x6
□ Litepanels Gemini 2x1 x4
□ Kino Flo 4-bank x4
□ Practical bulbs (3200K, dimmable)

CONTROL:
□ DMX controller
□ Wireless DMX
□ Distro boxes
□ Stingers (25', 50', 100')

MODIFIERS:
□ Softboxes for SkyPanels
□ Chimera for M18
□ Diffusion (Full, Half, Quarter CTO/CTB)
□ Gels (various)
□ Egg crates
□ Louvers

POWER:
□ Genie lift
□ Cable (assorted gauge and length)
□ Generator (size calculated from power draw)
```

**Intelligent Features**:
- **Package Suggestions**: "All your needs fit in [Rental House] Package B, would save $3K vs. à la carte"
- **Alternative Options**: "Could substitute SkyPanel S60 with Aputure 600d Pro, save $500/day"
- **Missing Items Flag**: "Shot 23 requires underwater housing, not in current list"
- **Redundancy Check**: "You have dolly and Steadicam for same scene, confirm both needed?"

**Output Formats**:
- Master gear list (everything)
- Department lists (specific to dept)
- Rental house order sheets (formatted for submission)
- Checklist format (for prep day)
- Budget implications (cost per item)

**Technical Implementation**:
- Analysis of shot list using Claude
- Database of gear categories and typical needs
- Integration with Budget Agent for cost
- Templates for different rental houses
- Export to Excel/PDF

---

### **AGENT 12: VERSION CONTROL AGENT**
*Every version, every change, tracked forever*

**Purpose**: Maintains complete history of all documents, enabling rollback, comparison, and understanding of how decisions evolved.

**What Gets Versioned**:
```
DOCUMENTS:
- Shot lists (every revision)
- Script analysis (each pass)
- Visual language docs
- Lookbooks
- Budget versions
- Gear lists
- Call sheets
- Shot notes

CONVERSATIONS:
- Director meetings
- Department discussions
- Creative decisions
- Technical problem-solving

TESTS:
- Camera test results
- Lighting tests
- Location photos with analysis
```

**Version Control Strategy**:

**Git Repository Structure**:
```
/project-name/
  /scripts/
    script-v1.pdf
    script-v2-revisions.pdf
  /analysis/
    script-analysis-pass1.md
    script-analysis-complete.md
  /visual-language/
    visual-approach-v1.md
    visual-approach-final.md
  /lookbook/
    references-kitchen-scenes.pdf
    references-night-exteriors.pdf
  /shot-lists/
    shot-list-v1-scene-order.xlsx
    shot-list-v2-production-order.xlsx
    shot-list-final.pdf
  /gear-lists/
    camera-department-v1.xlsx
    grip-electric-v1.xlsx
  /budget/
    budget-v1-initial.xlsx
    budget-v2-revised.xlsx
  /transcripts/
    /director-meetings/
      2025-11-15-kitchen-discussion.txt
      2025-11-18-location-scout.txt
    /voice-notes/
      2025-11-16-creative-ideas.txt
  /tests/
    camera-test-anamorphic-notes.md
    location-scout-photos/
```

**Commit Strategy**:
```
Meaningful commits with context:

"feat: Add Scene 12-15 shot coverage options
- Generated 3 coverage strategies for kitchen scenes  
- Includes handheld intimate vs dolly smooth options
- Lighting notes for morning window motivation
- Related to director meeting 2025-11-15"

"update: Revised budget based on producer feedback
- Reduced camera package from Alexa to FX6
- Savings: $15K
- Maintains visual approach with S35 sensor
- Alternative lens options documented"

"test: Anamorphic lens test results  
- Tested Cooke vs Atlas Orion anamorphics
- Cooke preferred for close-ups (smoother bokeh)
- Atlas better for landscape (sharper edges)
- Recommendation: Cooke set"
```

**Firebase Storage Strategy**:
```
Firestore Documents:
{
  "project_id": "nail-house-film",
  "document_type": "shot_list",
  "version": 3,
  "created_at": "2025-11-19T10:30:00Z",
  "created_by": "agent_5_shot_list_generator",
  "changes_from_v2": "Added Scene 45 car chase coverage",
  "git_commit": "abc123def456",
  "file_path": "gs://bucket/nail-house/shot-lists/v3.xlsx"
}

Cloud Storage:
Actual files stored in Google Cloud Storage buckets
```

**Comparison Features**:
```
"Show me what changed from shot list v2 to v3"
→ Highlights new shots, deleted shots, modified shots

"What was our lighting approach before the director meeting on 11/15?"
→ Shows evolution of lighting plan based on conversation

"Why did we switch from Alexa to FX6?"
→ Pulls commit message + budget analysis + decision context
```

**Output**:
- Complete change history
- Easy rollback to any version
- Comparison tools
- Decision documentation
- Timeline of project evolution

---

### **AGENT 13: MULTIMODAL ANALYSIS AGENT**
*Sees and analyzes images with cinematography understanding*

**Purpose**: Analyzes photos, location scouts, costume tests, set designs, reference images using advanced multimodal AI with cinematography-specific understanding.

**Powered By**: Open source multimodal models on Run Pod (better than Gemini 2.5 Pro for specific visual analysis tasks)

**Use Cases**:

**1. Location Scout Photo Analysis**:
```
Input: 15 photos of kitchen location
Output:
- Natural light analysis (window positions, time of day, direction)
- Existing practicals inventory (what's there, what needs adding)
- Power access points
- Rigging possibilities (ceiling height, wall strength, mounting points)
- Background control (what's visible through windows, what to flag)
- Color palette (existing colors, what to coordinate with costume)
- Space dimensions (estimated, for dolly/crane clearance)
- Potential challenges (mirrors, glass, reflective surfaces)
```

**2. Reference Image Analysis**:
```
Input: "Analyze this Roger Deakins frame from 1917"
Output:
- Composition breakdown (rule of thirds, balance, tension)
- Lighting analysis (key source, fill ratio, practical motivation)
- Color palette extraction (specific hex codes)
- Depth strategy (foreground/mid/background separation)
- Lens estimation (focal length, aperture)
- Technical recreation (how to achieve this look)
```

**3. Costume/Makeup Test Review**:
```
Input: Photos of actors in costume under test lighting
Output:
- Color conflicts with set design (flag potential issues)
- Lighting interaction (how fabrics reflect, skin tone rendering)
- Texture analysis (how materials read on camera)
- Recommendations (gel choices to flatter skin, flags for specular)
```

**4. Set Design Review**:
```
Input: Production designer's set photos or renderings
Output:
- Lighting opportunities (where to place units, practicals to add)
- Camera position analysis (best angles, frame depth potential)
- Color coordination (with established visual language)
- Practical concerns (eye lines, sight lines, blocking space)
```

**5. Visual Reference Matching**:
```
Input: "Find images that match this mood"
Output: Search and return similar images with analysis of why they match
```

**6. Lighting Diagram Interpretation**:
```
Input: Hand-drawn or sketched lighting diagram
Output:
- Identifies units by shape
- Reads labels and annotations
- Generates clean digital version
- Calculates inverse square law for positioning
- Suggests gel/diffusion based on setup
```

**Models to Use** (Research needed for current best options):
```
Candidates as of knowledge cutoff:
- LLaVA-NeXT
- CogVLM
- InternVL
- GPT-4V (via API as backup)
- Specialized models for specific tasks

Run Pod Setup:
- GPU instance (A40 or better)
- Model optimized for fast inference  
- API endpoint for Vision AI agents to call
- Batch processing capability for multiple images
```

**Output Formats**:
- Structured analysis (JSON)
- Natural language description
- Annotated images (with overlays/markup)
- Comparison charts
- Actionable recommendations

**Technical Implementation**:
- Run Pod GPU instance running multimodal model
- API endpoint for agents to call
- Firebase storage for images and analysis results
- Integration with Visual Language Agent and Shot List Generator

---

## 🔌 SYSTEM INTEGRATION MAP

### **Data Flow Architecture**

```
INPUT SOURCES:
├── MacWhisper (watch folders) → Audio transcriptions
├── Manual text input → Direct to Note Intelligence
├── Uploaded scripts (PDF) → Script Analysis
├── Uploaded images → Multimodal Analysis
└── Firebase (existing data) → Context retrieval

PROCESSING LAYERS:
├── ORCHESTRATOR (routes all requests)
├── SPECIALIST AGENTS (process specific tasks)
└── STORAGE AGENTS (version control, Firebase)

OUTPUT DESTINATIONS:
├── Firebase Firestore (metadata, structured data)
├── Firebase Cloud Storage (files, images)
├── GitHub (version control)
├── User interface (web app or CLI)
└── External systems (Gmail, Google Sheets, iOS Reminders)
```

### **Technology Stack**

```
INFRASTRUCTURE:
- Firebase (Firestore + Cloud Storage + Functions)
- GitHub (version control)
- Run Pod (GPU compute for multimodal AI)
- Google Cloud Functions (serverless agent execution)

AI/ML:
- Claude API (Sonnet 4.5 for most agents, Opus 4.1 for deep analysis)
- Claude SDK (agent orchestration)
- Open source multimodal models (Run Pod)
- MacWhisper (local transcription)

DEVELOPMENT:
- Node.js (backend orchestration)
- Python (AI model inference on Run Pod)
- React (web interface - future)
- Claude Code (rapid implementation)

INTEGRATION:
- Gmail API (communication drafting)
- Google Sheets API (budget export)
- iOS Shortcuts/Reminders (task sync)
- Motion API (scheduling - if available)

DATA:
- Firestore (structured data, metadata)
- Cloud Storage (files, images, media)
- Redis (agent state management)
- PostgreSQL (relational data like gear catalogs, pricing)
```

---

## 🚀 IMPLEMENTATION ROADMAP

### **Phase 1: Core Foundation (PRIORITY - Implement First)**
*Goal: Voice capture → intelligent note sorting → document population*

**Week 1-2: Build These Agents**
1. **Orchestrator** (basic routing logic)
2. **Voice Transcription Agent** (MacWhisper integration)
3. **Note Intelligence Agent** (the sophisticated one)
4. **Version Control Agent** (Git automation)

**Deliverables**:
- Voice note → auto-transcribed → auto-sorted into shot list/lighting notes/to-dos
- All outputs committed to GitHub
- Basic Firebase storage

**Why This First**: Solves your immediate need for current film in prep. Captures director conversations automatically.

---

### **Phase 2: Creative Intelligence (Implement Second)**
*Goal: Script → complete visual approach*

**Week 3-4: Build These Agents**
1. **Script Analysis Agent** (7-pass system)
2. **Visual Language Agent** (Bruce Block + cinematography theory)
3. **Shot List Generator Agent** (comprehensive coverage)
4. **Research Agent Network** (all 4 researchers)

**Deliverables**:
- Upload script → get back complete analysis
- Visual language document with lookbook
- Multiple shot list options
- Reference image compilation

**Why This Second**: Enables the "read script today, ready to shoot tomorrow" vision.

---

### **Phase 3: Production Tools (Implement Third)**
*Goal: Logistics and collaboration optimization*

**Week 5-6: Build These Agents**
1. **Gear List Generator Agent**
2. **Budget Agent**
3. **Collaboration Coordinator Agent**
4. **Communication Agent**
5. **Task Management Agent**

**Deliverables**:
- Gear lists from shot list
- Accurate budgets with real numbers
- Auto-drafted emails/memos
- Intelligent task prioritization

**Why This Third**: Production tools that make execution smooth.

---

### **Phase 4: Advanced Analysis (Implement Fourth)**
*Goal: Visual intelligence and optimization*

**Week 7-8: Build This Agent**
1. **Multimodal Analysis Agent** (Run Pod setup)

**Deliverables**:
- Location photo analysis
- Reference image matching
- Lighting diagram interpretation
- Costume/set review

**Why This Last**: Most technically complex, least immediately critical.

---

## 📦 FIREBASE ARCHITECTURE

### **Firestore Collections Structure**

```javascript
/projects/{project_id}/
  - name: "Nail House"
  - status: "prep" | "production" | "post" | "complete"
  - created_at: timestamp
  - director: "Director Name"
  - production_start: date
  
  /scripts/{version}
    - file_url: Cloud Storage URL
    - uploaded_at: timestamp
    - version_number: int
    
  /analysis/{analysis_id}
    - type: "script" | "visual_language" | "scene"
    - content: JSON or Markdown
    - created_by: agent_id
    - git_commit: string
    
  /shot_lists/{version}
    - scenes: array
    - version_number: int
    - production_order: boolean
    - created_at: timestamp
    
  /transcripts/{transcript_id}
    - raw_text: string
    - speakers: array
    - duration: int
    - audio_file_url: string
    - processed_by_intelligence: boolean
    
  /notes/{note_id}
    - type: "shot_list" | "lighting" | "camera" | "todo" | "collaboration"
    - content: JSON
    - source_transcript: transcript_id
    - scene_reference: string
    
  /tasks/{task_id}
    - title: string
    - priority: "high" | "medium" | "low"
    - status: "not_started" | "in_progress" | "blocked" | "complete"
    - category: string
    - deadline: timestamp
    - dependencies: array
    
  /gear_lists/{version}
    - department: "camera" | "grip" | "electric"
    - items: array
    - budget_total: float
    
  /budgets/{version}
    - total: float
    - departments: object
    - version_notes: string
    
  /conversations/{conversation_id}
    - participants: array
    - date: timestamp
    - location: string
    - transcripts: array (reference to transcripts)
    - decisions_made: array
```

### **Cloud Storage Bucket Structure**

```
/projects/{project_id}/
  /scripts/
    script-v1.pdf
    script-v2.pdf
  /analysis/
    script-analysis.md
    visual-language.md
  /lookbooks/
    lookbook-v1.pdf
  /shot-lists/
    shot-list-scene-order.xlsx
    shot-list-production-order.xlsx
  /audio/
    /raw/
      2025-11-19-director-meeting.m4a
    /transcripts/
      2025-11-19-director-meeting.txt
  /images/
    /location-scouts/
      kitchen-wide.jpg
      kitchen-window.jpg
    /references/
      deakins-1917-frame.jpg
```

---

## 🧠 RUN POD SETUP FOR MULTIMODAL AI

### **Instance Configuration**

```yaml
GPU: A40 (48GB VRAM) or A100 (40GB)
vCPU: 8+
RAM: 32GB+
Storage: 100GB SSD

Template:
- PyTorch 2.0+
- CUDA 12+
- Transformers library
- FastAPI for API endpoint

Models to Install:
1. Primary: LLaVA-NeXT-34B (or current best open source)
2. Backup: InternVL or CogVLM
3. Specialized: If available, cinematography-specific fine-tuned model

API Endpoint:
POST /analyze-image
{
  "image_url": "https://...",
  "analysis_type": "location_scout" | "reference" | "costume_test" | "lighting_diagram",
  "context": "Optional context about what to look for"
}

Response:
{
  "analysis": {
    "lighting": {...},
    "composition": {...},
    "technical_notes": {...},
    "recommendations": [...]
  }
}
```

### **Cost Optimization**

```
Strategy:
- Use Spot instances (70% savings)
- Auto-scale down when not in use
- Batch process multiple images together
- Cache common analyses

Estimated Cost:
- A40: ~$0.50-0.80/hour
- Usage estimate: 10 hours/week during prep
- Monthly cost: ~$40-80
```

---

## 💬 VOICE TRANSCRIPTION DEEP DIVE (Priority Agent)

Since this is your immediate need, let me detail the complete implementation:

### **MacWhisper Integration**

```javascript
// File watcher setup
const chokidar = require('chokidar');

const watchFolders = [
  '/Users/bongani/Dropbox/Voice Notes',
  '/Users/bongani/Director Conversations',
  '/Users/bongani/Creative Ideas'
];

const macWhisperOutputFolder = '/path/to/macwhisper/output';

// Watch MacWhisper output folder for completed transcriptions
const watcher = chokidar.watch(macWhisperOutputFolder, {
  persistent: true,
  ignoreInitial: false,
  awaitWriteFinish: {
    stabilityThreshold: 2000,
    pollInterval: 100
  }
});

watcher.on('add', async (filePath) => {
  console.log(`New transcription detected: ${filePath}`);
  
  // Read transcription file
  const transcript = await fs.readFile(filePath, 'utf-8');
  
  // Extract metadata from filename or MacWhisper output
  const metadata = parseMetadata(filePath);
  
  // Send to Orchestrator
  await sendToOrchestrator({
    type: 'voice_transcription',
    transcript: transcript,
    metadata: metadata,
    source_audio: metadata.original_audio_path
  });
});
```

### **MacWhisper Configuration**

```
Settings:
- Watch Folders: Enable
- Model: Large-v3 (best accuracy)
- Language: Auto-detect (or force English if preferred)
- Output Format: Plain text + SRT (for timestamps)
- Speaker Diarization: Enable if available
- Auto-process: Enable

Folder Structure:
Input: /Users/bongani/Dropbox/Voice Notes
Output: /Users/bongani/MacWhisper/Transcripts

Naming Convention:
Input: voice-note-2025-11-19.m4a
Output: voice-note-2025-11-19.txt + voice-note-2025-11-19.srt
```

### **Note Intelligence Processing**

This is the most sophisticated agent. Here's the detailed prompt architecture:

```
SYSTEM PROMPT:
You are a cinematography intelligence system with deep knowledge of:
- Film production workflows (camera, lighting, grip, electric departments)
- Shot list formats and conventions
- Lighting terminology and approaches
- Collaboration patterns between departments
- Production logistics and scheduling
- Budget structures for camera department

Your task is to analyze raw transcriptions from a cinematographer's voice notes or conversations and intelligently extract, categorize, and route information into appropriate production documents.

You understand context: When someone says "let's go handheld for this," you know that implies:
- Camera support: handheld rig
- Lens: likely wider (18-35mm range for stability)
- Movement: organic, following action
- Lighting: needs to accommodate camera movement
- Crew: operator + 1st AC focus puller

USER PROMPT STRUCTURE:
Transcript Source: [Director Meeting | Location Scout | Personal Note | Tech Scout]
Project: [Project Name]
Context: [Current prep phase, specific scenes being discussed if known]

Raw Transcript:
[Full transcription text]

Please analyze this transcript and extract:

1. SHOT LIST ADDITIONS
   For each shot mentioned or implied:
   - Scene number (if stated or infer from context)
   - Shot description
   - Camera type (if mentioned)
   - Lens suggestion (if mentioned, or suggest based on description)
   - Movement type
   - Framing
   - Any special notes

2. LIGHTING NOTES
   For each lighting discussion:
   - Scene/setup reference
   - Key source approach
   - Specific units mentioned
   - Practical lighting requests
   - Mood/tone descriptions
   - Department collaboration needed

3. CAMERA DEPARTMENT NOTES
   - Camera body requirements
   - Lens needs
   - Support gear (dolly, crane, sticks, Steadicam)
   - Special equipment
   - Tests needed

4. GRIP & ELECTRIC REQUIREMENTS
   - Specific gear mentioned
   - Rigging needs
   - Flags/diffusion
   - Special requests

5. ACTION ITEMS
   For each task or to-do:
   - Task description
   - Priority (High/Medium/Low)
   - Owner (Bongani or delegate)
   - Deadline (if mentioned)
   - Category (Creative/Technical/Logistic/Budget)

6. COLLABORATION TASKS
   Who needs to be contacted and why:
   - Person/department
   - Topic
   - Urgency
   - Context

7. QUESTIONS/DECISIONS NEEDED
   Things that were discussed but not decided

8. RESEARCH TASKS
   Things mentioned that need further exploration

Format your output as structured JSON that can be directly imported into production documents.

IMPORTANT CONTEXT RULES:
- If scene number not mentioned but context implies it, make educated guess with [Scene X - INFERRED] notation
- When movement described casually ("smooth in on her"), translate to technical terms ("Dolly push-in")
- Flag ambiguous statements that need clarification ("Director said 'that lens' but didn't specify which")
- Connect related items (if lighting discussed for Scene 12, link to Scene 12 shot list items)
- Preserve creative intent language but also translate to technical execution
```

### **Example Processing**

**Input Transcript**:
```
"Okay so for the kitchen scene, the morning scene with Sarah, I really want to feel that golden hour light coming through the window. Let's go handheld, something intimate, 35mm feels right. Keep it warm, motivated by that east-facing window we saw on the scout. We'll need to talk to production design about those overhead lights – can we put those on a dimmer? And maybe we do a slow push-in as she reads the letter, starts wide, ends tight on her face. We'll need to test that lens for close-ups, make sure the fall-off is soft enough."
```

**Note Intelligence Output**:
```json
{
  "shot_list_additions": [
    {
      "scene": "12 [INFERRED - Kitchen Morning]",
      "shot_number": "12A",
      "description": "Handheld medium wide to close-up, Sarah reading letter",
      "camera": "[To be determined from gear list]",
      "lens": "35mm (T2.0-2.8 suggested for close-up softness)",
      "movement": "Handheld dolly push-in, slow",
      "framing": "Start: Medium wide (waist up), End: Close-up (face)",
      "motivation": "Emotional intimacy as she discovers letter content",
      "special_notes": "Need lens test for close-up fall-off quality",
      "estimated_duration": "30-45 seconds"
    }
  ],
  
  "lighting_notes": [
    {
      "scene": "12 - Kitchen Morning",
      "key_source": "East-facing window (natural golden hour light)",
      "approach": "Motivated practical/natural",
      "color_temp": "Warm (3000-3200K to match golden hour)",
      "mood": "Intimate, morning warmth, emotional vulnerability",
      "specific_requirements": [
        "Time-sensitive: Must shoot during actual golden hour",
        "Window direction: East-facing (morning light)",
        "Practical overhead lights need dimmer control"
      ],
      "collaboration_needed": {
        "production_design": "Overhead lights dimmable",
        "gaffer": "Golden hour quality matching, practical control"
      }
    }
  ],
  
  "camera_notes": [
    {
      "requirement": "35mm lens with soft fall-off for close-ups",
      "test_needed": true,
      "test_description": "Test 35mm for close-up work, evaluate bokeh quality and fall-off"
    },
    {
      "requirement": "Handheld rig for smooth push-in",
      "support_gear": "Handheld shoulder rig or Easyrig for stability during movement"
    }
  ],
  
  "action_items": [
    {
      "task": "Test 35mm lens for close-up fall-off and softness",
      "priority": "High",
      "category": "Camera Test",
      "owner": "Bongani + 1st AC",
      "deadline": "Before kitchen scene shoot date",
      "dependencies": ["Lens package confirmation"]
    },
    {
      "task": "Coordinate golden hour window timing at kitchen location",
      "priority": "High",
      "category": "Location Logistics",
      "owner": "Bongani + AD",
      "note": "Scene 12 must be scheduled for actual golden hour timing"
    }
  ],
  
  "collaboration_tasks": [
    {
      "department": "Production Design",
      "contact": "[Name from project context]",
      "topic": "Scene 12 Kitchen - Overhead practical lights need dimmer capability",
      "priority": "Medium",
      "context": "For lighting control during golden hour scene",
      "suggested_communication": "Draft email requesting dimmable practicals for Scene 12"
    },
    {
      "department": "Gaffer",
      "topic": "Scene 12 - Golden hour matching and practical control strategy",
      "priority": "High",
      "context": "Discuss how to maintain/extend golden hour quality, control overhead practicals"
    }
  ],
  
  "questions_decisions_needed": [
    {
      "question": "Specific camera body for handheld work in Scene 12?",
      "context": "Need to confirm which camera body from package is best for handheld",
      "impacts": "Lens testing, rig configuration"
    }
  ],
  
  "research_tasks": [],
  
  "metadata": {
    "conversation_type": "Director Collaboration",
    "scenes_discussed": ["12 - Kitchen Morning"],
    "participants": ["Bongani", "Director"],
    "key_decisions": [
      "Handheld intimate approach for kitchen scene",
      "35mm lens choice",
      "Golden hour window as key source",
      "Slow push-in on emotional moment"
    ]
  }
}
```

**This JSON then automatically populates**:
- Shot list document (adds Scene 12A with all details)
- Lighting plan (adds Scene 12 lighting approach)
- Camera department notes (adds 35mm lens test requirement)
- Task list (adds two new high-priority tasks)
- Collaboration tracker (creates draft email to Production Designer)

---

## 🎨 EXAMPLE WORKFLOW: FULL SYSTEM IN ACTION

Let me show you the complete workflow from script to shoot-ready:

### **Day 1: Script Received**

**9:00 AM**: Upload script to system
```
→ Script Analysis Agent activates
→ Performs 7-pass analysis (2 hours processing)
→ Output: Comprehensive analysis document
→ Committed to GitHub
→ Stored in Firebase
```

**11:00 AM**: Review script analysis, record voice thoughts
```
"Okay so reading this, the kitchen scene feels like the emotional center. I'm thinking we lean into that isolation she's feeling with the framing..."
→ MacWhisper transcribes
→ Voice Transcription Agent picks up
→ Note Intelligence Agent processes
→ Creates personal creative notes document
```

**2:00 PM**: Request visual language generation
```
→ Visual Language Agent analyzes script + your voice notes
→ Applies Bruce Block principles
→ Maps contrast/affinity across scenes
→ Generates visual approach document
→ Research Agents find reference images
→ Creates lookbook draft
```

**End of Day 1**: 
- Complete script analysis
- Visual language document  
- Lookbook with 30+ reference images
- Your creative thoughts documented

---

### **Day 2: Director Meeting**

**10:00 AM**: Meeting with director to discuss visual approach
```
[Recording automatically captures conversation]
→ MacWhisper transcribes in real-time
→ Note Intelligence processes as it completes
```

**Director says**: "I love the handheld idea for the kitchen, but what if we go even more aggressive in the confrontation scene? Like, really unstable."

**Note Intelligence extracts**:
- Agreement on kitchen handheld approach ✓
- New direction for confrontation scene
- Updates shot list to reflect "aggressive handheld, intentionally unstable"
- Flags research task: "Find reference for aggressive unstable handheld in confrontation"

**12:00 PM**: Lunch break, system processing
```
→ Shot List Generator creates initial shot list based on director discussion
→ Generates 3 coverage options for kitchen scene
→ Generates 2 aggressive handheld approaches for confrontation
→ Research Agent finds Safdie Brothers, Dardenne Brothers references for aggressive handheld
```

**End of Day 2**:
- Shot list v1 (scene order)
- Multiple coverage options per scene
- Updated visual language incorporating director feedback
- Research images for aggressive handheld approach

---

### **Day 3: Tech Scout**

**Morning**: Location scout at kitchen location
```
[You take 20 photos of location]
→ Upload to system
→ Multimodal Analysis Agent processes
→ Output:
  * Natural light analysis (east window, morning sun 7-9am)
  * Existing practicals identified (3 overhead fixtures, wall sconces)
  * Power access mapped (outlets marked in photos)
  * Rigging points identified (ceiling beams, wall strength estimated)
  * Color palette extracted (cream walls, wood cabinets, blue accents)
  * Space dimensions estimated (12x14 feet, 9ft ceiling)
  * Potential challenges (mirror on wall, windows may need ND)
```

**Afternoon**: Voice notes during drive back
```
"That kitchen is actually perfect for the golden hour stuff. The window faces exactly the right direction. We're definitely going to need NDs for those windows though, and I think we should request those overhead lights be swapped for dimmable fixtures. Note to self: test the 35mm for close-ups, I want to make sure the bokeh is soft enough for Sarah's face."

→ Note Intelligence processes:
  * Confirms location works for Scene 12
  * Adds ND filter requirement to gear list
  * Creates collaboration task: request dimmable fixtures from Production Design
  * Creates action item: 35mm lens test for close-up bokeh
  * Updates lighting plan with specific notes about window ND
```

**End of Day 3**:
- Location photos analyzed with technical notes
- Updated lighting plan with location-specific details
- Gear list updated (ND filters added)
- Collaboration email drafted to Production Designer
- Task list updated with lens test

---

### **Day 4: Finalizing**

**Morning**: Review and refine everything
```
You review:
→ Shot list (make some manual tweaks)
→ Visual language doc (approve)
→ Lookbook (remove 3 images, add 2 new ones manually)

System:
→ Version Control Agent commits all changes
→ All documents now at v3-4
→ Change log automatically maintained
```

**Midday**: Generate production documents
```
Request:
→ Gear List Generator creates department-specific lists
→ Budget Agent calculates costs ($85K camera dept, $45K G&E)
→ Communication Agent drafts emails to gaffer, key grip
→ Shot List Generator creates production-order version (optimized)
```

**Afternoon**: Final review with director
```
[Recording of meeting]

Director approves everything, makes one change: "Actually, let's do the confrontation scene on sticks, not handheld. I want it to feel more formal, trapped."

→ Note Intelligence catches this
→ Updates shot list immediately
→ Removes aggressive handheld references
→ Adds "locked off, formal framing" notes
→ Updates gear list (tripods instead of handheld rig for that scene)
```

**End of Day 4**:
- Final shot list (production ready)
- Final gear lists (ready to order)
- Final budget (ready to submit)
- All communications drafted
- Version history preserved
- Ready to shoot

**Time Spent**: 
- Day 1: 3 hours (script review + system review)
- Day 2: 4 hours (director meeting + review)
- Day 3: 5 hours (location scout + review)  
- Day 4: 3 hours (refinement + final meeting)
- **Total: 15 hours of active work** (vs. 2-3 weeks traditional)

---

## 🛠️ TECHNICAL IMPLEMENTATION GUIDE FOR CLAUDE CODE

Now here's everything you need to hand to Claude Code to actually BUILD this:

### **Repository Structure**

```
cinematography-ai/
├── README.md
├── .env.example
├── .gitignore
├── package.json
├── firebase.json
├── docker-compose.yml
│
├── /agents/
│   ├── orchestrator.js
│   ├── voice-transcription.js
│   ├── note-intelligence.js
│   ├── script-analysis.js
│   ├── visual-language.js
│   ├── shot-list-generator.js
│   ├── budget-agent.js
│   ├── research-network.js
│   ├── collaboration-coordinator.js
│   ├── communication-agent.js
│   ├── task-management.js
│   ├── gear-list-generator.js
│   ├── version-control.js
│   └── multimodal-analysis.js
│
├── /lib/
│   ├── firebase-client.js
│   ├── claude-client.js
│   ├── github-client.js
│   ├── file-watcher.js
│   └── utils.js
│
├── /prompts/
│   ├── note-intelligence-prompt.txt
│   ├── script-analysis-prompt.txt
│   ├── visual-language-prompt.txt
│   ├── shot-list-prompt.txt
│   └── ...
│
├── /templates/
│   ├── shot-list-template.xlsx
│   ├── lighting-plan-template.md
│   ├── gear-list-template.xlsx
│   └── email-templates/
│
├── /runpod/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── multimodal-api.py
│   └── model-loader.py
│
├── /firebase-functions/
│   ├── index.js
│   ├── triggers.js
│   └── storage-triggers.js
│
├── /tests/
│   ├── agent-tests/
│   ├── integration-tests/
│   └── fixtures/
│
└── /docs/
    ├── ARCHITECTURE.md
    ├── AGENT-SPECS.md
    ├── API-REFERENCE.md
    └── USER-GUIDE.md
```

---

### **Claude Code Implementation Instructions**

I'm going to create a separate artifact with complete implementation instructions, as this is getting quite long. One moment...

Actually, before I do that - do you want me to:

1. **Continue with the complete Claude Code instructions here** (will be very comprehensive)
2. **Create a separate deliverable document** you can save and use as reference
3. **Focus on getting Phase 1 (Voice + Note Intelligence) fully specified first** so you can start building that immediately

Which approach serves you best for actually implementing this?

Also, quick clarifying questions on the immediate implementation:

1. **MacWhisper**: Do you know its output folder path already, or do we need to configure that?
2. **Firebase Project**: Should I include instructions for setting up a new Firebase project, or do you have one ready to use?
3. **GitHub Repo**: What's your preferred naming convention? "cinematography-ai", "vision-ai", "bongani-dp-system"?
4. **Run Pod**: Are you comfortable with Docker, or should I give you a no-Docker setup approach?

Let me know and I'll dial in the implementation guide precisely for your needs!



## Prompt:
11/19/2025, 8:23:36 AM

Would be immediately useful, actually something else. I kind of need the intelligence and methodology of the voice note part very quickly so that I can process three different voice transcriptions for meetings. I’ve already had with the directors. For these I would either upload the text to a chat here or I would ask Claude code to process the text file. Can you provide the prompt?

After that, we will continue with coding.



## Response:
11/19/2025, 8:25:12 AM

# 🎯 IMMEDIATE DIRECTOR CONVERSATION PROCESSING PROMPT

Bongani, I'm giving you the complete prompt architecture you can use **right now** - either paste your transcripts directly into a chat with me, or give this to Claude Code to process text files. This is the sophisticated Note Intelligence system distilled into a single, powerful prompt.

---

## THE PROMPT (Copy Everything Below This Line)

```
# CINEMATOGRAPHY NOTE INTELLIGENCE SYSTEM

You are an AI system with deep expertise in professional cinematography, film production workflows, and the collaborative language used between directors and cinematographers. Your purpose is to analyze raw transcripts from director-DP conversations and intelligently extract, categorize, and structure information into production-ready documents.

## YOUR KNOWLEDGE BASE

**Cinematography Workflows**: You understand the complete DP preparation process from script analysis through production, including the 7-pass script analysis method, visual language development using Bruce Block's principles, shot list creation, lighting design, camera department logistics, and crew collaboration patterns.

**Technical Fluency**: You know cinematography terminology (lens focal lengths and their psychological implications, camera movement types, lighting ratios and approaches, grip and electric equipment, coverage strategies), production department structures and responsibilities, and how information flows between departments.

**Contextual Intelligence**: You can infer unstated information (when someone says "go handheld," you understand the implications for camera support, lens choice, lighting flexibility, and crew requirements), recognize when creative language needs technical translation, identify ambiguities that need clarification, and connect related information across different parts of conversations.

---

## PROCESSING INSTRUCTIONS

### STEP 1: CONTEXT IDENTIFICATION
First, analyze the transcript to determine:
- **Conversation Type**: Director collaboration, location scout, tech scout, creative brainstorm, department meeting, or personal notes
- **Participants**: Who is speaking and their roles
- **Project Phase**: Prep, active production, or post
- **Scenes/Sequences Discussed**: Specific scene numbers or descriptions mentioned
- **Tone/Urgency**: Casual exploration vs. final decisions

### STEP 2: ENTITY EXTRACTION
Identify and extract all mentions of:

**Shot Descriptions**:
- Scene identifiers (numbers, names, or descriptions)
- Shot types (wide, medium, close-up, insert)
- Camera movement (dolly, pan, tilt, handheld, Steadicam, crane)
- Lens choices (focal lengths, characteristics)
- Framing details (composition, angle, height)
- Coverage approaches (master, singles, OTS, inserts)

**Lighting & Visual Approach**:
- Lighting sources and motivation (natural, practical, artificial)
- Mood descriptors (warm, cold, harsh, soft, dramatic, naturalistic)
- Color references and palettes
- Contrast ratios or tonal approaches
- Specific units or techniques mentioned
- Time of day implications

**Camera & Grip Needs**:
- Camera bodies mentioned or implied
- Specific lens packages or focal lengths
- Support gear (dolly, track, crane, Steadicam, tripods)
- Special equipment (drones, underwater housings, car mounts)
- Rigging requirements

**Collaboration Needs**:
- Requests to other departments
- Questions that need answering
- Decisions deferred to others
- Interdepartmental dependencies

**Action Items**:
- Tasks to complete
- Tests to conduct
- Research to do
- People to contact
- Deadlines mentioned

**Creative Intent & Subtext**:
- Story motivations behind visual choices
- Character psychology reflected in cinematography
- Emotional beats and how to support them
- Thematic visual elements

### STEP 3: INTELLIGENT SORTING
Route extracted information into these document categories:

**SHOT LIST ADDITIONS**: Complete shot specifications with scene number, description, camera specs, lens, movement, framing, and special notes

**LIGHTING PLAN**: Scene-by-scene lighting approach, key source, mood, specific units, practical requirements, and department collaboration needs

**CAMERA DEPARTMENT NOTES**: Body requirements, lens needs, support gear, special equipment, and tests needed

**GRIP & ELECTRIC REQUIREMENTS**: Specific gear callouts, rigging needs, modifiers, and special requests

**ACTION ITEMS**: Structured tasks with priority, category, owner, deadline, and dependencies

**COLLABORATION TASKS**: Department/person, topic, priority, context, and suggested communication

**QUESTIONS/DECISIONS NEEDED**: Items discussed but not finalized, requiring follow-up

**RESEARCH TASKS**: References to find, techniques to explore, or information to gather

### STEP 4: TECHNICAL TRANSLATION
When converting creative language to technical execution:

- **"Intimate feel"** → Suggest: Handheld, closer focal lengths (35-50mm), shallow depth of field, warmer tones
- **"Smooth movement"** → Dolly on track, Steadicam, or gimbal; avoid handheld
- **"Isolated and trapped"** → Longer lens (85mm+), compressed space, limited depth staging, high-key lighting or deep shadows
- **"Raw and immediate"** → Handheld, wider lens, practical lighting, minimal diffusion
- **"Dreamy quality"** → Soft focus techniques, diffusion filters, glowing highlights, warm or cool color push

Always preserve the creative intent language while providing technical translation.

### STEP 5: CONTEXTUAL CONNECTIONS
- Link related items (if lighting discussed for Scene 12, connect to Scene 12 shot list entries)
- Note when multiple conversations reference the same scene or shot
- Flag contradictions between different discussions
- Track evolving decisions across conversation timeline
- Identify dependencies (e.g., "need location confirmed before finalizing coverage")

### STEP 6: FLAG AMBIGUITIES
Clearly mark when:
- Scene numbers aren't specified but can be inferred: [Scene 12 - INFERRED]
- References are unclear: "Director said 'that lens' [WHICH LENS - CLARIFY]"
- Decisions seem contradictory: [CONFLICT: Previous discussion said static, this says handheld]
- Information is incomplete: [INCOMPLETE: Mentioned special rig but no details]

---

## OUTPUT FORMAT

Provide your analysis in structured JSON format with clear sections. Use this exact structure:

```json
{
  "metadata": {
    "conversation_type": "string",
    "participants": ["array", "of", "names"],
    "date_if_mentioned": "string or null",
    "scenes_discussed": ["array of scene identifiers"],
    "key_decisions_made": ["array of major decisions"]
  },
  
  "shot_list_additions": [
    {
      "scene": "Scene number or [INFERRED] description",
      "shot_number": "Suggested shot number",
      "description": "Full shot description",
      "camera": "Camera body if specified, or [TBD]",
      "lens": "Focal length and characteristics",
      "movement": "Type of camera movement",
      "framing": "Composition and framing details",
      "angle": "Camera height/angle",
      "coverage_purpose": "What this shot accomplishes",
      "motivation": "Story/emotional reason for shot",
      "special_notes": "Any additional requirements or considerations",
      "estimated_duration": "Shot length if mentioned"
    }
  ],
  
  "lighting_notes": [
    {
      "scene": "Scene identifier",
      "key_source": "Primary light source and approach",
      "mood": "Lighting mood and emotional tone",
      "color_temp": "Color temperature preference",
      "approach": "Naturalistic, stylized, motivated, etc.",
      "specific_requirements": ["Array of specific needs"],
      "practical_requests": "Requests to art department",
      "collaboration_needed": {
        "department": "What's needed and why"
      }
    }
  ],
  
  "camera_department_notes": [
    {
      "requirement": "What's needed",
      "category": "body/lens/support/special",
      "test_needed": true/false,
      "test_description": "What to test if applicable",
      "priority": "high/medium/low"
    }
  ],
  
  "grip_electric_requirements": [
    {
      "item": "Specific gear",
      "category": "grip/electric",
      "purpose": "What it's for",
      "scenes": ["Which scenes need it"]
    }
  ],
  
  "action_items": [
    {
      "task": "Clear task description",
      "priority": "high/medium/low",
      "category": "creative/technical/logistic/budget/collaboration",
      "owner": "Who's responsible",
      "deadline": "When needed (relative to production)",
      "dependencies": ["What must happen first"],
      "notes": "Additional context"
    }
  ],
  
  "collaboration_tasks": [
    {
      "department": "Which department/person",
      "topic": "What needs discussion",
      "priority": "high/medium/low",
      "context": "Why this is needed",
      "suggested_communication": "Draft email/message text"
    }
  ],
  
  "questions_decisions_needed": [
    {
      "question": "What needs to be decided",
      "context": "Background information",
      "impacts": "What this decision affects",
      "options": ["Possible approaches if apparent"]
    }
  ],
  
  "research_tasks": [
    {
      "topic": "What to research",
      "purpose": "Why this research is needed",
      "priority": "high/medium/low",
      "sources": ["Suggested places to look"]
    }
  ],
  
  "creative_notes": [
    {
      "note": "Important creative observations or inspirations",
      "context": "When/where this applies"
    }
  ]
}
```

---

## SPECIAL INSTRUCTIONS

**For Bongani's Neurodivergent Workflow**:
- Capture EVERYTHING, even tangential thoughts—filtering comes later
- Flag when a thought seems incomplete or might need revisiting: [THREAD TO FOLLOW]
- Note when energy/excitement is high around an idea: [HIGH ENTHUSIASM]
- Preserve the exact creative language used, not just technical translation

**Pattern Recognition**:
- If Bongani consistently prefers certain approaches (e.g., "always wants 5:1 lighting ratios for drama"), note: [PATTERN: Consistent with previous dramatic lighting preference]
- Connect to his established visual vocabulary from other projects when apparent

**Context Preservation**:
- Maintain the flow and evolution of ideas through the conversation
- Note when decisions change: [REVISION: Previously discussed X, now Y]
- Preserve "thinking out loud" moments that reveal creative process

**Practical Production Focus**:
- Prioritize information that has immediate production implications
- Flag items that need quick turnaround
- Note budget implications when apparent: [BUDGET NOTE: This requires special rental]

---

## EXAMPLE PROCESSING

### Sample Input:
*"So for the kitchen scene, the morning scene with Sarah, I really want to feel that golden hour light coming through the window. Let's go handheld, something intimate, 35mm feels right. Keep it warm, motivated by that east-facing window we saw on the scout. We'll need to talk to production design about those overhead lights – can we put those on a dimmer? And maybe we do a slow push-in as she reads the letter, starts wide, ends tight on her face. We'll need to test that lens for close-ups, make sure the fall-off is soft enough."*

### Expected Output Structure:
```json
{
  "shot_list_additions": [
    {
      "scene": "Kitchen Morning - [INFERRED: Scene 12]",
      "shot_number": "12A",
      "description": "Handheld push-in, Sarah reading letter",
      "lens": "35mm (T2.0-2.8 for close-up softness)",
      "movement": "Handheld dolly push-in, slow",
      "framing": "Start: Medium wide (waist up), End: Close-up (face)",
      "motivation": "Emotional intimacy as letter content revealed",
      "special_notes": "Test lens for close-up fall-off quality"
    }
  ],
  "lighting_notes": [
    {
      "scene": "Kitchen Morning",
      "key_source": "East window, natural golden hour",
      "mood": "Warm, intimate, morning vulnerability",
      "color_temp": "Warm (3000-3200K, golden hour quality)",
      "specific_requirements": [
        "Time-sensitive: actual golden hour timing required",
        "Overhead practicals need dimmer control"
      ],
      "collaboration_needed": {
        "production_design": "Dimmable overhead fixtures for Scene 12"
      }
    }
  ],
  "action_items": [
    {
      "task": "Test 35mm lens for close-up bokeh and fall-off",
      "priority": "high",
      "category": "technical",
      "owner": "Bongani + 1st AC",
      "deadline": "Before kitchen scene shoot date"
    }
  ],
  "collaboration_tasks": [
    {
      "department": "Production Design",
      "topic": "Kitchen overhead lights need dimmer capability",
      "priority": "medium",
      "suggested_communication": "For Scene 12 (Kitchen Morning), we're using natural window light as our key. To balance effectively, can we make the overhead practicals dimmable?"
    }
  ]
}
```

---

## YOUR TASK NOW

I will provide you with a raw transcript from a director-cinematographer conversation. Please analyze it using the complete intelligence system described above and provide the structured JSON output.

Be thorough but concise. Capture all production-relevant information. Flag ambiguities clearly. Connect related items. Preserve creative intent while providing technical translation.

**TRANSCRIPT TO ANALYZE:**

[PASTE YOUR TRANSCRIPT HERE]

---

END OF PROMPT
```

---

## 🎬 HOW TO USE THIS RIGHT NOW

### **Option 1: Process with me directly**

Just paste your three transcripts into our chat, one at a time, prefaced with:

```
"Using the Cinematography Note Intelligence system, please analyze this transcript:

[PASTE TRANSCRIPT]"
```

I'll process each one and give you the complete JSON output that you can then copy into your shot lists, lighting plans, etc.

---

### **Option 2: Give to Claude Code**

Save the prompt as `cinematography-intelligence-prompt.txt`, then give Claude Code this instruction:

```
Read the prompt in cinematography-intelligence-prompt.txt

Then process these three transcript files:
- transcript-meeting-1.txt
- transcript-meeting-2.txt  
- transcript-meeting-3.txt

For each one, output a separate JSON file with the complete analysis:
- meeting-1-analysis.json
- meeting-2-analysis.json
- meeting-3-analysis.json

Use the exact JSON structure specified in the prompt.
```

---

### **Option 3: Run it yourself with Claude API**

If you want to process multiple transcripts quickly via API:

```python
import anthropic
import json

client = anthropic.Anthropic(api_key="your-key")

with open('cinematography-intelligence-prompt.txt', 'r') as f:
    system_prompt = f.read()

with open('transcript-1.txt', 'r') as f:
    transcript = f.read()

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    system=system_prompt,
    messages=[{
        "role": "user",
        "content": f"TRANSCRIPT TO ANALYZE:\n\n{transcript}"
    }]
)

# Parse and save the JSON
analysis = json.loads(message.content[0].text)
with open('analysis-output.json', 'w') as f:
    json.dump(analysis, indent=2, fp=f)
```

---

## 💡 IMMEDIATE NEXT STEPS FOR YOUR THREE TRANSCRIPTS

1. **Paste them to me one at a time** - I'll process them using this system
2. **I'll give you structured JSON** for each conversation
3. **You review and extract** what you need for your current prep
4. **Then we continue** with the full system architecture

This gets you immediate relief for your active production while we build the complete automated system.

**Ready?** Paste your first transcript and I'll show you the intelligence system in action.





---
Powered by [Claude Exporter](https://www.claudexporter.com)