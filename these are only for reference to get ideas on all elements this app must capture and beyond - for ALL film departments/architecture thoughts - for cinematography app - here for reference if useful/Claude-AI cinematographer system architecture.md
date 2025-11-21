# AI cinematographer system architecture

**User:** Bongani  
**Created:** 11/13/2025 13:42:43  
**Updated:** 11/13/2025 16:09:05  
**Exported:** 11/13/2025 16:09:44  
**Link:** [https://claude.ai/chat/9f9abeb5-5d28-4636-b5f0-bce2d1600a0a](https://claude.ai/chat/9f9abeb5-5d28-4636-b5f0-bce2d1600a0a)  

## Prompt:
11/13/2025, 1:44:13 PM

Okay, here we go. So. I need you to read the document called DP Process. Um, And you can also look on Google Drive for some of these documents if you don’t find them in the project knowledge. But DP process, Uh, there’s a document called Nail House to-do list. There’s also documents about cinematography and cinematography prep. And um, I want you to look at past conversations. Where I’m asking questions about cinematography, preparing for cinematography. Um, Coming up with budgets. Um, What else? Essentially, I want to take my entire creative process, logistics process, strategy processes. And you can go through and Look through all the project knowledge, look through past conversations to compile. What? All of this. Might be. Anyhow. Look at all the questions and things I asked for this project specifically. And let’s compile a master document that tries to detail all of the things that a cinematographer has to do to get ready for a shoot. in their own personal work and reviewing stuff. in pulling images, doing all of that stuff. And then also, let’s look at All of the logistics strategy stuff, planning stuff, figuring out execution. Let’s look at all the parts of collaboration that need to happen. between departments, in conversations with the directors, all this stuff. Also look up my own thoughts about directors boot camp and directors being the ultimate collaborators. I think I also have lists of all the different positions and what the duties of different positions are. So we need awareness of that. Um, And then, you know, you can reference books like the 5 Cs of cinematography. Uh, Bruce Block, I think, writes a book called The Visual, um, story, I think. Um, There’s a book called The New Cinematographers. Uh, Roger Deakins just released a book called Reflections. You should research that. But then that’s also research across the web. All the parts that go into a cinematographer’s work. What might be taught in schools, but also more specific, the real life experience, and also gleaning from all of the elements and projects and things that I have done. specifically. And let’s compile everything we understand about. The cinematography process from script. or even idea, to screen. Because I have been using uh, projects, right? I create a project, I put a handful of files in there for the project knowledge, including the script and all these things. And I go through this process, Of eventually, Breaking it down, looking for keywords, looking for stuff on shot deck, on the website, FLIM.AI. Um, you know, I do different cinematography analysis. Then after I’m done with the cinematography, analysis. Uh, you know, I do some story analysis stuff, right? Then I combine that with all of my own notes and thoughts about the story. And then that goes into a cinematography project, and we have a cinematography handoff. project. And all those things, Add up and add up and add up to eventually where I start working on the visual language, and all this stuff, and that’s my own personal process. And then there’s discussions with the directors. There’s the director’s notes, there’s director’s materials, and then in prep now, we’re in location scouting, and we are, Discussing shot lists and stuff like that. And personally for me, What works best is for us to just talk about everything. Even when I read a script, I do voice notes and voice dumps. And one approach I’m trying to do for this Shot list. This time around and everything around this film is I just want to record all of our conversations. Then I’m going to have you, transcribe them and then sort them into, Sort the notes. to figure out action items, to do list things, Um, you know, add to the shot list. You know, some pieces of information need to be added to several different styles of documents that we use in film processes. But I want to now create an entire system. That uses the API, And also the Claude SDK. So we can do A gentic AI, A G E N T I C. And have subagents and multiple agents that take care of all the parts. Right? So let’s architecture and think about, If we were going to, in a sense, create an AI cinematographer. But really, it’s so that I can Almost duplicate myself. And enable myself to do more work. I can ask for very specific tasks to be done. I can ask for a series of tasks to be done. For example, I could give it a script and have it go through the entire process to give me the visual language and all of those elements and then give me versions of what the shot list should be, basically from end to end so that I could read a script today and have a plan to shoot it 100% tomorrow, including things about lighting, about grip, about camera department. including making gear lists. And having actual real numbers. For all those things, you know? So it needs a knowledge base where I can fill in Stuff from previous shoots that I have that can be analyzed to add to its intelligence. But then, it needs a researcher agent that can research any part of anything. of any part of this. And there’s probably multiple researcher types, right? There’s a researcher that’s purely creative and for story and for ideating. There’s a researcher that is purely for visual language. Analysis and ideation. And creativity. There’s one that’s just creative and looks at everything only from a creative lens so that we’re always stretching the possibilities. But there’s also one that is a story expert because the best stories are fully integrated and connected to the Story, the best cinematography, sorry, is. Vendor must be a budget expert. There’s an expert at film budgets in general. But also can drill down to make the budget for camera. And for grip and electric. And then I just need an assistant that is keeping track of all the tasks I have to do. Right? So, of course, it presents all the usual things that I should do, and as long as I’ve worked through those tasks, I would have thought and touched every part that I need to be ready to shoot the film. But then also, it can keep track of extra tasks and to do list. Basically, I needed to do this so I can dump different to-do list things. Somewhere, and then it will. Add them and prioritize them, and I can have a place where I’m in putting, but then there’s a place that keeps track of all the tasks that need to be done. And who I need to contact. And so that’s why we need a collaboration agent that understands the roles of every single other department. So that if a task Might involve me asking the producer or the AD or the production designer. Then it can. Let me know who I need to talk to. But it would be great if there’s also a communication agent that will draft all the emails and draft all the communications that I need to do. And it might be able to grab an attachment that one of the other ones made. And get a little package ready to put in my email. You know, eventually it would be great if it can actually just create those drafts for me inside of my actual Gmail. Uh and Google workspace, but that, as long as the writing is done and the attachments are ready, I can do that part manually to begin with. Then, of course, it needs a voice transcription. Agent, And the voice transcription, I have whisper for Mac on my computer. So maybe you can hook to that. Um, You can also download some open source transcription models and just run them on my computer. Um, Or I can just do The Open AI API. Or we can spin up a server that’s run pod. That can do a lot of this. And I know that we also discussed, My entire Bungani, AI ecosystem, Now to include run pod. So be able to run with clone API and clawed agents. And utilize, you know, claude code if it needs to, all these sorts of things. Um, And connect to my obsidian, which I haven’t set up yet, by the way. Or at least have a database where all this stuff is stored. So I have Google Firebase, so I would love everything to always be stored. All versions of everything must be either committed to a get or a GitHub. Or, He stored in Google Firebase. So that I can also keep track of how stuff developed. And maybe then we need an agent that can keep track of how stuff has been developing and be able to reflect that back to me. As well. And then, If you were constructing this system, what other AI agents would you create? Right? Or subagents for this one Program. We’re going to make the most amazing AI powered program. For me, to make cinematography easy. It’s almost like I just, I need to clone myself. Because with my autism and ADHD now, These 8 hour, 10 hour, 12 hour days. I need to. I need to reduce my workload dramatically. And so my goal is that so many conversations can be captured. By voice. I take a lot of pictures and video, which will all be tacked by location, of course, from my phone. Um, We also had, when we were thinking about the run part, stuff and everything, we’re also going to install, I think locally on my machine and then also on one part, some of the, Newer, Open source. AI that are good at multimodal. There’s one that can actually point at stuff for visual analysis. There’s a couple that are actually better than Gemini 2.5 Pro at multimodal analysis. We had a whole system. Look that up so that you can also see how we can use those for this as well. Because I think all of the agents we’re creating will jack into that run pod system as well. And I love you to architect this entire thing with me. And then give me all the instructions I need to hand over to Claude Code so that Claude Code can make this thing. And then give me all of the implementation. And remember, this won’t take weeks. It will take hours because I’m going to spin up multiple clawed code instances. To just work. And now there’s clawed code for web. And we can just make them work endlessly. to get this stuff up and running. The most important thing is for us to design an excellent system. So, bring all of that info, research, all of that info. And less design the system and get this going. I’m going to personally run this prompt inside of my Bungani Inc. project inside of the cinematography project, inside of specific films that I have projects for. And also in Bungani Labs, and then eventually combine all of that. In Bongani labs to Combine all the ideas and systems together as one.

By the way, this is building to what I think would be a separate program, but with all the similar parts of program that I was wanting to design called I think we called it Nexus or Film Nexus, where everyone inputs all of their information all the heads of Dept and everybody working on the film so it can help the prep process be easier. You can also look at that project if you have access to it and find it for perspective, but I think we’ll build that separately because my more immediate need is the Cinematography one for me.

Also, whatever extra special knowledge you feel that you have in this project to add that would be useful for something like this please also detail that



## Response:
11/13/2025, 1:50:23 PM

````plaintext
Thought: Architecting a multi-agent AI cinematography system for autonomous workflow.
````

Okay, this is EXACTLY the kind of systems architecture challenge that lights me up. Let me dive deep into this with you.

First, let me check the time and then systematically gather everything we need.

**user_time_v0**

*Request*

````javascript
{}
````

*Response*

````javascript
{"current_time":"2025-11-13T13:44:44-0800"}
````

````plaintext
Thought: Architected comprehensive AI agent system for cinematography workflow automation.
````

Perfect—1:44 PM, so you're likely in a good focus window. Let me systematically gather everything we need to architect this beast.

## Phase 1: Knowledge Retrieval

**project_knowledge_search**

*Request*

````javascript
{
  "query": "DP process cinematography prep workflow",
  "max_text_results": 10
}
````

*Response*

````plaintext
story dev  1  Invocation of Cinematography Knowledge.pdf
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
Claude-An Overview of a Film Director's Complete Process.md
2.  Pre-production Planning Pre-production is the crucial stage where you lay the groundwork for your film. This is the time to make key creative decisions, plan your shots, and ensure that everything is in place for a smooth production. Storyboarding and shot-listing help you visualize the film and communicate your vision to the crew. Scheduling and budgeting are essential to ensure that you can make the most of your resources and time on set. Effective pre-production planning allows you to anticipate challenges and find creative solutions before the cameras start rolling. a. Storyboarding and shot-listing
    
    *   How can you use storyboards to plan visual symbolism and metaphors?
    *   What shots and sequences are crucial for conveying the story's themes and emotions?
    *   What is the most visually compelling way to tell each part of the story, and how can camera angles enhance the emotion or tension?
    
    b. Scheduling and budgeting
    *   How can you prioritize scenes and allocate resources based on their narrative significance?
    *   What creative solutions can you find to maximize production value within budget constraints?
3.  Casting Casting is one of the most important decisions you'll make as a director. The right actors can bring your characters to life, elevate the material, and create memorable performances that resonate with audiences. When casting, consider not only an actor's talent and experience but also how they embody the specific qualities and traits of each character. Rehearsals and table reads are valuable opportunities to explore the script, build chemistry between actors, and refine performances before shooting begins. a. Choosing actors
    
    *   What specific qualities and traits should each character embody?
    *   How can you ensure that the cast aligns with the script's themes and tonal consistency?
    *   Does each actor convey the character's essence, and how do they interact with other characters?
    
    b. Rehearsals and table reads
    *   How can you use rehearsals to explore subtext, character dynamics, and emotional arcs?
    *   What exercises can you employ to help actors inhabit their roles and build chemistry?
    *   Work with actors to explore different emotional depths and nuances in key scenes.
4.  Visual Style and Cinematography Cinematography is the art of capturing your story visually. It encompasses the technical aspects of camera operation and lighting and the creative decisions that shape the look and feel of your film. Your visual style should enhance the story's themes, emotions, and genre elements, creating a cohesive and immersive experience for the audience. Collaborating closely with your cinematographer is essential to develop a shared vision and find innovative ways to bring your story to life on screen. a. Choosing a visual style
    
    *   How can the visual style enhance the story's themes, emotions, and genre elements?
````

````plaintext
Claude-Sandura - Mastering the Pitch! Elements of an Amazing Script Pitch Deck.txt
Not all films are suited for social engagement, but if yours is, what actions do you hope for viewers to take after seeing your film? Potential activities could include organizational partnerships, educational guides, targeted stakeholder/community screenings, social media strategies, multi-platform activity, or social change campaigns. Do you have partnerships with organizations in your issue area already, and if so, how are these relationships informing your project development?)Answer:
While our film does not have a direct social impact focus, we have a great desire to inspire more african filmmakers and storytellers to make movies. 
Workshops, Education, interns, DP workshops. Encourage more stories by African filmmakers. Local production companies and schools. Four wall screenings of the film in ZImbabwe and SOuth Africa with Q&As. 
Social Responsibility Campaigns - We will encourage community engagement and volunteerism by participating in events or initiatives inspired by vampire themes such as blood drives.
We want our film to be as culturally authentic as possible. To that end, we will be shooting in South Africa.  We are planning to work with local production companies, host workshops (e.g DP workshops and hire interns in order to encourage community engagement and to honor our african grats should we receive them

## Response:
Here are three options for expanding your answer to address the social impact and audience engagement aspects of your film:
Option 1:
Veins of the Veld, while primarily a genre film, has the potential to create significant social impact and engage audiences in meaningful ways:

Empowering African Filmmakers:

Host workshops and masterclasses in Zimbabwe and South Africa, leveraging our team's Hollywood experience to nurture local talent.
Offer internships on our production, providing hands-on experience to aspiring African filmmakers.
Collaborate with local film schools to provide guest lectures and mentorship opportunities.


Cultural Authenticity and Exchange:

Partner with local production companies in South Africa for our shoot, fostering skill-sharing and cultural exchange.
Organize Q&A sessions and workshops during production to engage the local community and share our filmmaking process.
Create behind-the-scenes content showcasing our collaboration with local talent, highlighting the richness of African filmmaking.


Building Bridges:

Establish a network connecting African filmmakers with resources and opportunities in Hollywood.
Create a mentorship program pairing emerging African filmmakers with established industry professionals.
Host screenings in both Africa and the USA, facilitating cross-cultural dialogue and appreciation.


Community Engagement:

Organize "Vamp It Up" blood drives, partnering with local blood banks to raise awareness about blood donation.
Collaborate with African cultural centers for special screenings and discussions about representation in genre films.
````

````plaintext
Claude-An Overview of a Film Director's Complete Process.md
over-the-shoulder, singles, two-shots) each create a different feeling.
*   Editing connects shots visually, spatially and logically to create meaning and propel the story forward via "question & answer" dynamics.
*   Format (aspect ratio), lens choice, and depth of field are key photographic decisions that shape a scene's look and feel.

Suggested Additions to the Novice Director's List:

*   Collaborate with the production designer early regarding visualization and storyboards to determine the "circle of dramatic action" - what the camera will and won't see.
*   When planning shots and edits, consider the "question & answer" relationship between them to create narrative momentum for the viewer. What new story information does each shot provide or withhold?
*   Experiment with different actor staging patterns (frontality, profiles, over-the-shoulder, deep staging) and camera angles to explore their emotional effects. Wide shots permit body language; close-ups permit subtler facial expressions.
*   Depth can be used symbolically to juxtapose foreground/background elements. Shallow focus guides attention.
*   Camera movement and editing compress or expand time and space. How the viewer is "moved through" a scene shapes their experience of it.
*   Storyboard difficult camera moves like crane shots to determine their ideal framing, timing and dramatic emphasis. Simple floor plans and stick figures can help.
*   Selecting format and aspect ratio is an important decision that shapes compositions. Consider how each would impact the story and production logistics.

In summary, Katz provides an in-depth exploration of the visual grammar of film directing, empowering directors to make use of framing, camera movement, staging, editing, and photographic decisions to shape the viewer's experience and the story's emotional impact. Novice directors would benefit from consciously experimenting with these tools during visualization to expand their creative options and ability to communicate their intentions to cast and crew. Storyboarding is essential for working out ideas, even in a simple form. Ultimately, shot flow stems from interpreting the script and the director's dramatic and thematic priorities.

## Prompt:
I'd like you to read a document that has more to do with creating an effective pitch deck or look book that would be used in development and trying to sell a film that I thought is also relevant to directing since I think it might have some questions and considerations and things a director should think about and maybe widen the scope to not just the director but any kind of creator of a project in terms of an executive producer for example. So still with the focus on a director but maybe think of everything in a wider scope and more expansive and let me know what things in here we should include in our directing process document and let me know where I should edit and put them in.
````

````plaintext
Claude-An Overview of a Film Director's Complete Process.md
So still with the focus on a director but maybe think of everything in a wider scope and more expansive and let me know what things in here we should include in our directing process document and let me know where I should edit and put them in.

## Response:
After reviewing the document on creating pitch decks, lookbooks, and series bibles, I agree that many of the elements discussed are relevant to the directing process and the broader scope of project creation. Here are some key elements we should consider incorporating into our directing process document:

1.  Logline and Synopsis: Add this to the "Story and Script" section. Directors should be able to concisely summarize their project, as it helps focus their vision and communicate effectively with cast and crew.
2.  Character Breakdowns: Expand the "Characters" subsection under "Story and Script". Include more detailed questions about character motivations, arcs, and relationships.
3.  Visual Style: Add this to the "Visual Style and Cinematography" section. Encourage directors to think about the overall look and feel they want to achieve, including specific visual techniques or styles they plan to use.
4.  Tone and Genre: Create a new subsection under "Story and Script" to address this. It's crucial for directors to understand and communicate the emotional atmosphere of their project.
5.  Target Audience: Add this as a consideration in the "Story and Script" section. While primarily a producer's concern, directors should be aware of their intended audience as it can influence creative decisions.
6.  Mood: Incorporate this into the "Visual Style and Cinematography" section. Encourage directors to consider how images, color palettes, and typography can convey the project's atmosphere.
7.  World-building: Add this to the "Production Design and Art Direction" section. For projects set in unique worlds, directors need to consider the rules, history, and unique elements of their story's universe.
8.  Themes: Create a new subsection under "Story and Script" to address the central ideas explored in the project and how they influence directorial choices.
9.  Sound and Music: Add a new section on "Sound Design and Music" to address the audio landscape of the project, including potential music styles or sound design elements.
10.  Storyboards and Concept Art: Expand the "Storyboarding and Shot Planning" section to include more about creating conceptual sketches for key scenes or sequences.
11.  Comparable Works: Add this as a consideration in the "Visual Style and Cinematography" section. Encourage directors to think about existing works that share similarities with their project or inspire their approach.
12.  Season Arc(s) and Episode Outlines: For TV directors, add a section on understanding and planning for long-term character and story development across multiple episodes or seasons.
13.
````

````plaintext
Claude-An Overview of a Film Director's Complete Process.md
*   How can you work together to create a consistent, impactful visual language?
5.  Production Design and Art Direction a. Collaborating with the production designer
    *   Discuss the overall aesthetic, color palette, and visual motifs.
    *   How do these design elements enhance the story, characters, and themes? b. Set design and location scouting
    *   Choose locations and sets that fit the script and visual style.
    *   How can you use these spaces to create the desired atmosphere and production value?
6.  Directing Actors a. Communicating your vision
    *   Clearly convey the story, themes, and emotional arcs to the actors.
    *   What techniques can you use to help actors understand their characters? b. Blocking and staging
    *   Plan the actors' movements and positioning within each scene.
    *   How do these choices underscore the emotional dynamics and story beats? c. Eliciting authentic performances
    *   Create a safe, trusting environment for actors to explore and take risks.
    *   What methods can you use to help actors access genuine emotions and reactions? d. Handling challenging scenes and situations
    *   Be prepared to guide actors through difficult or emotionally intense moments.
    *   How can you maintain a supportive, professional environment throughout?
7.  Working with the Crew a. Collaborating with key department heads
    *   Establish clear lines of communication with the cinematographer, production designer, sound designer, etc.
    *   How can you foster a collaborative, creative atmosphere while maintaining your vision? b. Delegating tasks and responsibilities
    *   Identify the strengths of your crew members and delegate accordingly.
    *   How can you ensure everyone understands their roles and feels valued? c. Effective communication on set
    *   Be clear, concise, and respectful when giving directions or feedback.
    *   What communication strategies can you employ to keep the production running smoothly?
8.  Technological Considerations a. Camera equipment and techniques
    *   Familiarize yourself with the camera gear, lenses, and rigs used in your production.
    *   How can you use these tools to achieve your desired visual style and storytelling? b. Lighting design
    *   Understand the basics of lighting (e.g., three-point lighting, color temperature).
    *   How can you use light to create mood, depth, and visual interest? c. Sound recording and design
    *   Ensure high-quality sound recording on set and plan for post-production sound design.
    *   How can you use sound to enhance the story, atmosphere, and emotional impact?
9.  Post-production a. Editing and pacing
    *   Collaborate with the editor to assemble the footage into a coherent, engaging story.
    *   How does the pacing and structure of the edit serve the narrative and emotional arcs?
````

````plaintext
Incentives Worksheet - Full List of Rewards - Expanded.csv
Bloodsucker's Bargain ($500),,,,,,,9. Bloodsucker's Bargain ($500)
Enhance your own creative skills with our talented team!,,,,,,,Enhance your own creative skills with our talented team!
• Social media shoutout,,,,,,,"• All rewards from Veld Visionary tier (excluding 30-min Virtual Q&A), plus:"
• Digital thank you card,,,,,,,• Choice of one 1-hour professional workshop:
• Personalized vampire themed Veins of the Veld digital profile photo,,,,,,,"- Virtual cinematography consultation with Bongani (camera, lighting, or creative process)"
• Be bestowed a vampire moniker on Veins of the Veld digital concept art,,,,,,,OR
• Access to a curated playlist inspired by the film,,,,,,,- Acting lesson or character development session with Sibongile
• Digital copy of the film poster with personalized easter egg (hidden name or initials),,,,,,,
• Digital copy of the film's lookbook,,,,,,,• Personalized video shoutout from main creators or cast
• Exclusive behind-the-scenes photos,,,,,,,
• Special thanks in the film credits,,,,,,,
"• Exclusive ""Veins of the Veld"" Enamel Pin",,,,,,,
• Signed digital copy of script,,,,,,,
• Exclusive early access screening of the film,,,,,,,
"• Limited Edition ""Veins of the Veld"" Poster",,,,,,,
• Choice of one 1-hour professional workshop:,,,,,,,
"- Virtual cinematography consultation with Bongani (camera, lighting, or creative process)",,,,,,,
OR,,,,,,,
- Acting lesson or character development session with Sibongile,,,,,,,
• Personalized video shoutout from main creators or cast,,,,,,,
,,,,,,,
"10. Veld Champion ($1,000)",,,,,,,"10. Veld Champion ($1,000)"
Become an integral part of our film's legacy!,,,,,,,Become an integral part of our film's legacy!
````

````plaintext
Claude-An Overview of a Film Director's Complete Process.md
a. Understanding the story - What is the central dramatic conflict, and how does it drive the narrative? - What are the primary and secondary themes, and how are they explored?

b. Script analysis - Identify the key plot points, subplots, and how they contribute to the overall story. - How does the script's structure escalate conflict and tension?

c. Characters - What are the main characters' functions, motivations, arcs, and emotional journeys? - How do the secondary characters support the main characters and contribute to the story?

d. Genre and tone - What genre conventions does the script follow or subvert, and how does this impact the story? - How can you maintain a consistent tone throughout the film?

2.  Pre-production Planning Pre-production is the crucial stage where you lay the groundwork for your film. This is the time to make key creative decisions, plan your shots, and ensure that everything is in place for a smooth production. Storyboarding and shot-listing help you visualize the film and communicate your vision to the crew. Scheduling and budgeting are essential to ensure that you can make the most of your resources and time on set. Effective pre-production planning allows you to anticipate challenges and find creative solutions before the cameras start rolling. a. Storyboarding and shot-listing
    
    *   How can you use storyboards to plan visual symbolism and metaphors?
    *   What shots and sequences are crucial for conveying the story's themes and emotions?
    
    b. Scheduling and budgeting
    *   How can you prioritize scenes and allocate resources based on their narrative significance?
    *   What creative solutions can you find to maximize production value within budget constraints?
3.  Casting Casting is one of the most important decisions you'll make as a director. The right actors can bring your characters to life, elevate the material, and create memorable performances that resonate with audiences. When casting, consider not only an actor's talent and experience but also how they embody the specific qualities and traits of each character. Rehearsals and table reads are valuable opportunities to explore the script, build chemistry between actors, and refine performances before shooting begins. a. Choosing actors
    
    *   What specific qualities and traits should each character embody?
    *   How can you ensure that the cast aligns with the script's themes and tonal consistency?
    
    b. Rehearsals and table reads
    *   How can you use rehearsals to explore subtext, character dynamics, and emotional arcs?
    *   What exercises can you employ to help actors inhabit their roles and build chemistry?
4.  Visual Style and Cinematography Cinematography is the art of capturing your story visually. It encompasses the technical aspects of camera operation and lighting and the creative decisions that shape the look and feel of your film.
````

````plaintext
Incentives Worksheet - Full List of Rewards - Expanded.csv
Bloodsucker's Bargain ($500),,,,,,,9. Bloodsucker's Bargain ($500)
Enhance your own creative skills with our talented team!,,,,,,,Enhance your own creative skills with our talented team!
• Social media shoutout,,,,,,,"• All rewards from Veld Visionary tier (excluding 30-min Virtual Q&A), plus:"
• Digital thank you card,,,,,,,• Choice of one 1-hour professional workshop:
• Personalized vampire themed Veins of the Veld digital profile photo,,,,,,,"- Virtual cinematography consultation with Bongani (camera, lighting, or creative process)"
• Be bestowed a vampire moniker on Veins of the Veld digital concept art,,,,,,,OR
• Access to a curated playlist inspired by the film,,,,,,,- Acting lesson or character development session with Sibongile
• Digital copy of the film poster with personalized easter egg (hidden name or initials),,,,,,,
• Digital copy of the film's lookbook,,,,,,,• Personalized video shoutout from main creators or cast
• Exclusive behind-the-scenes photos,,,,,,,
• Special thanks in the film credits,,,,,,,
"• Exclusive ""Veins of the Veld"" Enamel Pin",,,,,,,
• Signed digital copy of script,,,,,,,
• Exclusive early access screening of the film,,,,,,,
"• Limited Edition ""Veins of the Veld"" Poster",,,,,,,
• Choice of one 1-hour professional workshop:,,,,,,,
"- Virtual cinematography consultation with Bongani (camera, lighting, or creative process)",,,,,,,
OR,,,,,,,
- Acting lesson or character development session with Sibongile,,,,,,,
• Personalized video shoutout from main creators or cast,,,,,,,
,,,,,,,
"10. Veld Champion ($1,000)",,,,,,,"10. Veld Champion ($1,000)"
Become an integral part of our film's legacy!,,,,,,,Become an integral part of our film's legacy!
````

````plaintext
Claude-An Overview of a Film Director's Complete Process.md
*   What regular meetings or check-ins can you establish to foster ongoing collaboration and communication?
    
    b. Delegating tasks and responsibilities
    
    *   How can you empower your crew members to take ownership of their roles and contribute creatively?
    *   What systems can you put in place to ensure smooth delegation and accountability?
    
    c. Effective communication on set
    *   How can you adapt your communication style to different crew members' needs and personalities?
    *   What protocols can you establish to ensure clear, efficient communication during high-pressure situations?
8.  Technological Considerations As a director in the modern era, it's essential to have a strong understanding of the technological tools and techniques that bring your vision to life. From cameras and lenses to lighting and sound equipment, the choices you make in this area can have a significant impact on the look and feel of your film. Collaborating with your cinematographer and other department heads to develop a clear plan for your technical setup can help you make the most of your resources and ensure that your creative vision is fully realized on screen. a. Camera equipment and techniques
    
    *   How can you leverage the capabilities of your chosen camera equipment to enhance the story's visuals?
    *   What innovative camera techniques can you employ to create unique, impactful moments?
    
    b. Lighting design
    
    *   How can you use lighting to convey mood, emotion, and thematic elements?
    *   What specific lighting setups can you plan for key scenes to enhance their dramatic impact?
    
    c. Sound recording and design
    *   How can you work with the sound department to capture authentic, immersive audio on set?
    *   What opportunities exist to use sound design to reinforce the story's themes and emotional beats?
9.  Post-production Post-production is where all the elements of your film come together to create the final product. As a director, your involvement in this stage is crucial to ensuring that the edit, visual effects, sound design, and music all align with your original vision. Collaborating closely with your editor to refine the pacing, structure, and emotional arc of the film can help you create a compelling and cohesive narrative. Similarly, working with your composer and sound designer to develop a unique and evocative soundscape can enhance the story's impact and immerse the audience in the world of the film. a. Editing and pacing
    
    *   How can you collaborate with the editor to ensure the pacing aligns with the story's emotional journey?
    *   What editing techniques can you employ to enhance the story's themes, symbolism, and character arcs?
    
    b. Visual effects and color grading
    
    *   How can visual effects be used to enhance the story's supernatural or magical realism elements?
````

![image/webp](data:image/webp;base64,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)

![image/webp](data:image/webp;base64,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)

````plaintext
Thought: Good, I found several relevant documents. Let me continue searching for more specific documents he mentioned, and then search past conversations.
````

**project_knowledge_search**

*Request*

````javascript
{
  "query": "Nail House todo list tasks",
  "max_text_results": 10
}
````

*Response*

````plaintext
Story as Living Architecture_ A Comprehensive Guide to Narrative Development and Creative Vision I.pdf
This living document will continue to evolve with each project, each collaboration, and each
story told. It represents not an end point but a continuously developing approach to the art and
craft of storytelling in all its forms.
- Holistic Story Synthesis (HSS) Method document - 16 Narrative Structures to Plot a Book With
- Director's Process and Responsibilities - Creative Collaboration Goals - Marketing and
Distribution Strategies - Nail House project analysis and lookbook - Various narrative structure
documents (Hero's Journey, Heroine's Journey, Save the Cat, etc.) - Cinematography and visual
storytelling discussions - Henry James' Art of Fiction - Multiple conversations about story
development and creative process
````

````plaintext
Potential Tools for Reward Fulfillment and Social Media Calendar Structure and Sheet
Story Stickers: Any stickers to be used (for Stories)
17. Alt Text: For accessibility
18. Geotag: Location tag for the post
19. Mood/Theme: To help with visual consistency
20. Campaign Phase: Pre-launch, Active Campaign, Post-campaign
21. Key Message: Main point or theme of the post
22. Team Member Responsible: Who is responsible for creating/posting this content
23. Status: Planned, Created, Scheduled, Posted, Needs Review
24. Later/Hootsuite Status: Draft, Scheduled, Posted (if using these tools)
25. Google Calendar Color Code: For easy visual reference in Google Calendar
26. Notes: Any additional information or instructions

Folder Structure for Images:
/Veins of the Veld Campaign Images
  /Pre-Launch
  /Campaign
    /Week1
    /Week2
    /Week3
    /Week4
  /Post-Campaign
  /Team Member Posts
    /Nomsa
    /Sibongile
    /Bongani
  /Collaborative Posts
  /Stories
  /Reels

Image Naming Convention:
YYMMDD_AccountInitial_ContentType_BriefDescription
Example: 240801_F_FeedPost_VampireTeaser.jpg (For a film account feed post on August 1, 2024)

Google Calendar Integration:
To help with Google Calendar integration, include these columns:
27. Calendar Event Title: Short, descriptive title for the calendar event
28. Calendar Event Description: Brief description or key points for the calendar event
29. Calendar Color Code: Specific color to use in Google Calendar (can correspond to post type, account, or campaign phase)

This structure allows for a comprehensive overview of your posting schedule, with enough detail to manage complex posting requirements across multiple accounts. The team can easily filter or sort based on any of these columns to focus on specific aspects of the campaign.

For ease of use:
1. Use data validation for columns with preset options (e.g., Post Type, Account, Status)
2. Use conditional formatting to highlight different types of posts or statuses
3. Create separate sheets for each week of the campaign, with a master sheet that pulls all data together
4. Use formulas to automatically populate certain fields (e.g., Day number based on Date)

This setup should provide a clear, detailed plan for your Instagram campaign, making it easier for all team members to understand their responsibilities and maintain consistency across posts.

</response>

<references>
- Team composition: Nomsa, Sibongile, Bongani
- Focus on Instagram for crowdfunding campaign
- Need for detailed post planning including collaborations
- Integration with Google Calendar
- Use of image folder in Google Drive
- Potential use of Later or similar tools for scheduling
- Campaign phases: Pre-launch, Active Campaign, Post-campaign
- Need for accessibility considerations (Alt Text)
- Importance of consistent branding and messaging
</references>
````

````plaintext
Claude-An Overview of a Film Director's Complete Process.md
*   How can you use light to create mood, depth, and visual interest? c. Sound recording and design
    *   Ensure high-quality sound recording on set and plan for post-production sound design.
    *   How can you use sound to enhance the story, atmosphere, and emotional impact?
9.  Post-production a. Editing and pacing
    *   Collaborate with the editor to assemble the footage into a coherent, engaging story.
    *   How does the pacing and structure of the edit serve the narrative and emotional arcs? b. Visual effects and color grading
    *   Identify areas where visual effects or color grading can enhance the final product.
    *   How do these post-production elements contribute to the overall look and feel? c. Sound mixing and music
    *   Work with the sound mixer and composer to create a compelling soundscape and score.
    *   How do the audio elements work together to support the story and emotional beats?
10.  Leadership and Problem-solving a. Maintaining a positive, collaborative set environment
    *   Lead by example, fostering respect, open communication, and teamwork.
    *   How can you keep morale high and encourage creative contributions from all team members? b. Adapting to challenges and changes
    *   Be prepared for unexpected setbacks, such as weather, equipment issues, or schedule changes.
    *   How can you remain flexible and find creative solutions to keep the production on track? c. Making difficult decisions
    *   Take responsibility for tough calls, such as cutting scenes or making script changes.
    *   How can you balance the needs of the story, the cast and crew, and the production constraints?

Remember, directing is a complex, multifaceted role that requires a blend of creative vision, technical knowledge, leadership skills, and adaptability. By breaking down the responsibilities and consistently asking yourself how each choice serves the story and the overall production, you'll be well on your way to becoming a successful director.

## Prompt:
Great. Now please consider this document and after reading it, let's incorporate even more tasks and things to think about for a novice director. This document has more to do with breaking down a script, but conversely, these are all things a director should be thinking about for their story. Use it as inspiration, to add to our current list.

Then please also re-do our current list, adding these new revelations, and also expanding on what is already there. Ask more questions, so a novice director reading this list, would end up thinking about all sides of their story, the pre production process, production, and post, and also be able to collaborate effectively with their department heads and other artists.

## Response:
Absolutely! Let's expand our list for the novice director, incorporating the script breakdown elements and adding more tasks and considerations.
````

````plaintext
Potential Tools for Reward Fulfillment and Social Media Calendar Structure and Sheet
Story Stickers: Any stickers to be used (for Stories)
17. Alt Text: For accessibility
18. Geotag: Location tag for the post
19. Mood/Theme: To help with visual consistency
20. Campaign Phase: Pre-launch, Active Campaign, Post-campaign
21. Key Message: Main point or theme of the post
22. Team Member Responsible: Who is responsible for creating/posting this content
23. Status: Planned, Created, Scheduled, Posted, Needs Review
24. Later/Hootsuite Status: Draft, Scheduled, Posted (if using these tools)
25. Google Calendar Color Code: For easy visual reference in Google Calendar
26. Notes: Any additional information or instructions

Folder Structure for Images:
/Veins of the Veld Campaign Images
  /Pre-Launch
  /Campaign
    /Week1
    /Week2
    /Week3
    /Week4
  /Post-Campaign
  /Team Member Posts
    /Nomsa
    /Sibongile
    /Bongani
  /Collaborative Posts
  /Stories
  /Reels

Image Naming Convention:
YYMMDD_AccountInitial_ContentType_BriefDescription
Example: 240801_F_FeedPost_VampireTeaser.jpg (For a film account feed post on August 1, 2024)

Google Calendar Integration:
To help with Google Calendar integration, include these columns:
27. Calendar Event Title: Short, descriptive title for the calendar event
28. Calendar Event Description: Brief description or key points for the calendar event
29. Calendar Color Code: Specific color to use in Google Calendar (can correspond to post type, account, or campaign phase)

This structure allows for a comprehensive overview of your posting schedule, with enough detail to manage complex posting requirements across multiple accounts. The team can easily filter or sort based on any of these columns to focus on specific aspects of the campaign.

For ease of use:
1. Use data validation for columns with preset options (e.g., Post Type, Account, Status)
2. Use conditional formatting to highlight different types of posts or statuses
3. Create separate sheets for each week of the campaign, with a master sheet that pulls all data together
4. Use formulas to automatically populate certain fields (e.g., Day number based on Date)

This setup should provide a clear, detailed plan for your Instagram campaign, making it easier for all team members to understand their responsibilities and maintain consistency across posts.

</response>

<references>
- Team composition: Nomsa, Sibongile, Bongani
- Focus on Instagram for crowdfunding campaign
- Need for detailed post planning including collaborations
- Integration with Google Calendar
- Use of image folder in Google Drive
- Potential use of Later or similar tools for scheduling
- Campaign phases: Pre-launch, Active Campaign, Post-campaign
- Need for accessibility considerations (Alt Text)
- Importance of consistent branding and messaging
</references>
````

````plaintext
Rewards and Incentives for Seed and Spark Campaign
Here's a summary of our conversation about the crowdfunding campaign for "Veins of the Veld" as an artifact:

<artifact>
Crowdfunding Campaign Summary: "Veins of the Veld"

1. Reward Tiers:
We have established 13 reward tiers ranging from $10 to $10,000:

1. Fanged Friend ($10)
2. Nightcrawler's Delight ($25)
3. Moonlight Maverick ($50)
4. Vampire's Embrace ($75)
5. Shapeshifter's Secret ($100)
6. Nocturnal Patron ($200)
7. Veld Visionary ($300)
8. Veld Supporter ($500)
9. Bloodsucker's Bargain ($500)
10. Veld Champion ($1,000)
11. Master of the Veld ($2,500)
12. Eternal Champion ($5,000)
13. Eternal Patron ($10,000)

2. Key Rewards:
- Digital content (thank you cards, behind-the-scenes photos, film poster, playlist, lookbook, video content)
- Special thanks and credits (film credits, Associate Producer, Executive Producer)
- Physical items (enamel pin, limited edition poster, signed script)
- Exclusive experiences (early access screening, virtual Q&A, professional workshop, dinner with creators)
- High-tier rewards (custom artwork, limited edition prop/costume piece, exclusive insider access)

3. Fulfillment Considerations:
- Timing: Varies from end of campaign to film release
- Modes: Email, USPS, in-person/virtual meetings, in-film credits
- Costs: Most digital rewards are $0, physical items and experiences have associated costs

4. Task Management:
- Each reward has a list of specific tasks for fulfillment
- Tasks include design, creation, packaging, shipping, and follow-up activities
- Assigned persons need to be determined for each task

5. Tracking and Fulfillment:
- A detailed spreadsheet has been created to track each reward, its tasks, and fulfillment status
- Consider using project management tools like Trello or Asana for task tracking

6. Special Considerations:
- Physical rewards (poster, pin) added to enhance perceived value
- Virtual Q&A sessions limited to specific tiers
- Exclusive insider access for top-tier backers includes potential set visits or post-production sessions

7. Marketing Approach:
- Unique, thematic names for each tier to enhance appeal
- Emphasis on the film's African vampire theme throughout rewards
- Consideration of creating visual representations for each tier

8. Future Steps:
- Finalize assigned persons for each task
- Determine exact costs for physical items and experiences
- Create a system for tracking individual backer fulfillment
- Design and source physical items (poster, pin, props)
- Plan for the execution of experiential rewards (workshops, dinners, set visits)

This summary encapsulates the key points of our reward structure, fulfillment planning, and overall approach to the crowdfunding campaign for "Veins of the Veld".
</artifact>

This artifact provides a comprehensive overview of the crowdfunding campaign strategy and can be used to quickly brief others or as a starting point for further discussions or planning.
````

````plaintext
Potential Tools for Reward Fulfillment and Social Media Calendar Structure and Sheet
Story Stickers: Any stickers to be used (for Stories)
17. Alt Text: For accessibility
18. Geotag: Location tag for the post
19. Mood/Theme: To help with visual consistency
20. Campaign Phase: Pre-launch, Active Campaign, Post-campaign
21. Key Message: Main point or theme of the post
22. Team Member Responsible: Who is responsible for creating/posting this content
23. Status: Planned, Created, Scheduled, Posted, Needs Review
24. Later/Hootsuite Status: Draft, Scheduled, Posted (if using these tools)
25. Google Calendar Color Code: For easy visual reference in Google Calendar
26. Notes: Any additional information or instructions

Folder Structure for Images:
/Veins of the Veld Campaign Images
  /Pre-Launch
  /Campaign
    /Week1
    /Week2
    /Week3
    /Week4
  /Post-Campaign
  /Team Member Posts
    /Nomsa
    /Sibongile
    /Bongani
  /Collaborative Posts
  /Stories
  /Reels

Image Naming Convention:
YYMMDD_AccountInitial_ContentType_BriefDescription
Example: 240801_F_FeedPost_VampireTeaser.jpg (For a film account feed post on August 1, 2024)

Google Calendar Integration:
To help with Google Calendar integration, include these columns:
27. Calendar Event Title: Short, descriptive title for the calendar event
28. Calendar Event Description: Brief description or key points for the calendar event
29. Calendar Color Code: Specific color to use in Google Calendar (can correspond to post type, account, or campaign phase)

This structure allows for a comprehensive overview of your posting schedule, with enough detail to manage complex posting requirements across multiple accounts. The team can easily filter or sort based on any of these columns to focus on specific aspects of the campaign.

For ease of use:
1. Use data validation for columns with preset options (e.g., Post Type, Account, Status)
2. Use conditional formatting to highlight different types of posts or statuses
3. Create separate sheets for each week of the campaign, with a master sheet that pulls all data together
4. Use formulas to automatically populate certain fields (e.g., Day number based on Date)

This setup should provide a clear, detailed plan for your Instagram campaign, making it easier for all team members to understand their responsibilities and maintain consistency across posts.

</response>

<references>
- Team composition: Nomsa, Sibongile, Bongani
- Focus on Instagram for crowdfunding campaign
- Need for detailed post planning including collaborations
- Integration with Google Calendar
- Use of image folder in Google Drive
- Potential use of Later or similar tools for scheduling
- Campaign phases: Pre-launch, Active Campaign, Post-campaign
- Need for accessibility considerations (Alt Text)
- Importance of consistent branding and messaging
</references>
````

````plaintext
Rewards and Incentives for Seed and Spark Campaign
Here's a summary of our conversation about the crowdfunding campaign for "Veins of the Veld" as an artifact:

<artifact>
Crowdfunding Campaign Summary: "Veins of the Veld"

1. Reward Tiers:
We have established 13 reward tiers ranging from $10 to $10,000:

1. Fanged Friend ($10)
2. Nightcrawler's Delight ($25)
3. Moonlight Maverick ($50)
4. Vampire's Embrace ($75)
5. Shapeshifter's Secret ($100)
6. Nocturnal Patron ($200)
7. Veld Visionary ($300)
8. Veld Supporter ($500)
9. Bloodsucker's Bargain ($500)
10. Veld Champion ($1,000)
11. Master of the Veld ($2,500)
12. Eternal Champion ($5,000)
13. Eternal Patron ($10,000)

2. Key Rewards:
- Digital content (thank you cards, behind-the-scenes photos, film poster, playlist, lookbook, video content)
- Special thanks and credits (film credits, Associate Producer, Executive Producer)
- Physical items (enamel pin, limited edition poster, signed script)
- Exclusive experiences (early access screening, virtual Q&A, professional workshop, dinner with creators)
- High-tier rewards (custom artwork, limited edition prop/costume piece, exclusive insider access)

3. Fulfillment Considerations:
- Timing: Varies from end of campaign to film release
- Modes: Email, USPS, in-person/virtual meetings, in-film credits
- Costs: Most digital rewards are $0, physical items and experiences have associated costs

4. Task Management:
- Each reward has a list of specific tasks for fulfillment
- Tasks include design, creation, packaging, shipping, and follow-up activities
- Assigned persons need to be determined for each task

5. Tracking and Fulfillment:
- A detailed spreadsheet has been created to track each reward, its tasks, and fulfillment status
- Consider using project management tools like Trello or Asana for task tracking

6. Special Considerations:
- Physical rewards (poster, pin) added to enhance perceived value
- Virtual Q&A sessions limited to specific tiers
- Exclusive insider access for top-tier backers includes potential set visits or post-production sessions

7. Marketing Approach:
- Unique, thematic names for each tier to enhance appeal
- Emphasis on the film's African vampire theme throughout rewards
- Consideration of creating visual representations for each tier

8. Future Steps:
- Finalize assigned persons for each task
- Determine exact costs for physical items and experiences
- Create a system for tracking individual backer fulfillment
- Design and source physical items (poster, pin, props)
- Plan for the execution of experiential rewards (workshops, dinners, set visits)

This summary encapsulates the key points of our reward structure, fulfillment planning, and overall approach to the crowdfunding campaign for "Veins of the Veld".
</artifact>

This artifact provides a comprehensive overview of the crowdfunding campaign strategy and can be used to quickly brief others or as a starting point for further discussions or planning.
````

````plaintext
Rewards and Incentives for Seed and Spark Campaign
Here's a summary of our conversation about the crowdfunding campaign for "Veins of the Veld" as an artifact:

<artifact>
Crowdfunding Campaign Summary: "Veins of the Veld"

1. Reward Tiers:
We have established 13 reward tiers ranging from $10 to $10,000:

1. Fanged Friend ($10)
2. Nightcrawler's Delight ($25)
3. Moonlight Maverick ($50)
4. Vampire's Embrace ($75)
5. Shapeshifter's Secret ($100)
6. Nocturnal Patron ($200)
7. Veld Visionary ($300)
8. Veld Supporter ($500)
9. Bloodsucker's Bargain ($500)
10. Veld Champion ($1,000)
11. Master of the Veld ($2,500)
12. Eternal Champion ($5,000)
13. Eternal Patron ($10,000)

2. Key Rewards:
- Digital content (thank you cards, behind-the-scenes photos, film poster, playlist, lookbook, video content)
- Special thanks and credits (film credits, Associate Producer, Executive Producer)
- Physical items (enamel pin, limited edition poster, signed script)
- Exclusive experiences (early access screening, virtual Q&A, professional workshop, dinner with creators)
- High-tier rewards (custom artwork, limited edition prop/costume piece, exclusive insider access)

3. Fulfillment Considerations:
- Timing: Varies from end of campaign to film release
- Modes: Email, USPS, in-person/virtual meetings, in-film credits
- Costs: Most digital rewards are $0, physical items and experiences have associated costs

4. Task Management:
- Each reward has a list of specific tasks for fulfillment
- Tasks include design, creation, packaging, shipping, and follow-up activities
- Assigned persons need to be determined for each task

5. Tracking and Fulfillment:
- A detailed spreadsheet has been created to track each reward, its tasks, and fulfillment status
- Consider using project management tools like Trello or Asana for task tracking

6. Special Considerations:
- Physical rewards (poster, pin) added to enhance perceived value
- Virtual Q&A sessions limited to specific tiers
- Exclusive insider access for top-tier backers includes potential set visits or post-production sessions

7. Marketing Approach:
- Unique, thematic names for each tier to enhance appeal
- Emphasis on the film's African vampire theme throughout rewards
- Consideration of creating visual representations for each tier

8. Future Steps:
- Finalize assigned persons for each task
- Determine exact costs for physical items and experiences
- Create a system for tracking individual backer fulfillment
- Design and source physical items (poster, pin, props)
- Plan for the execution of experiential rewards (workshops, dinners, set visits)

This summary encapsulates the key points of our reward structure, fulfillment planning, and overall approach to the crowdfunding campaign for "Veins of the Veld".
</artifact>

This artifact provides a comprehensive overview of the crowdfunding campaign strategy and can be used to quickly brief others or as a starting point for further discussions or planning.
````

````plaintext
Incentives Worksheet - Deliverables x Fullfillment.csv
eo file,
,,,,,,Verify all emails sent,
Dinner with director/producers,"[Name 1], [Name 2]",In-person/Virtual,Post-production,$X/dinner,$2500+,Contact backers for availability and location,
,,,,,,Find Restaurant,
,,,,,,Schedule dinners,
,,,,,,Make reservations (if in-person),
,,,,,,Send calendar invites,
,,,,,,Attend dinners,
,,,,,,Follow up with thank you notes,
Executive Producer credit,[Name],In the film & IMDb,Film release,$0,$5000+,Verify names and spellings,
,,,,,,Add to film credits,
,,,,,,"Add credits to IMDb, create Veins Page",
,,,,,,Verify that their credit is on IMDB,
,,,,,,Notify backers when credits are live,
Film festival premiere invitation,[Name],Email,Film release,$0,$5000+,"Secure festival details - ask about passes, comp tickets",
,,,,,,Create invitations,
,,,,,,Send email invitations,
,,,,,,Manage RSVPs,
,,,,,,Send final details to attendees,
Exclusive insider access,"[Name 1], [Name 2]","Email, Video call, In-person",Throughout production,$X,"$10,000",Check availablility and location,
,,,,,,Schedule set visit or post-production session,
,,,,,,Arrange necessary clearances,
,,,,,,Prepare safety briefings (if on set),
,,,,,,Find a Host for visit/session,
,,,,,,"Send regular production updates, bi-weekly email",
,,,,,,Follow up after each major interaction,
Custom artwork,[Name],USPS,Post-production,$X,"$10,000",BTS / Unit Stills of empty sets to comp into,
,,,,,,Ask donor for series of photos (with recommendations for poses),
,,,,,,Figure out artwork concept,
,,,,,,"Commission artist , Hire Graphic Designer",
,,,,,,Receive final artwork,
,,,,,,Frame artwork,
,,,,,,Package securely,
,,,,,,Ship artwork,
,,,,,,Track shipment,
Limited edition prop/costume piece,[Name],USPS,Film release,$X,"$10,000",Select appropriate prop/costume piece,
,,,,,,Create certificate of authenticity,
,,,,,,Professionally clean item,
,,,,,,Package securely,
,,,,,,Ship item,
,,,,,,Track shipment,
````

````plaintext
Potential Tools for Reward Fulfillment and Social Media Calendar Structure and Sheet
Based on the information provided and the specific needs of your crowdfunding campaign for "Veins of the Veld", here are some recommendations for programs and tools to help manage and automate various tasks:

1. Email Management and Mail Merges:
- MailChimp: Great for creating email campaigns, managing subscriber lists, and automating email sequences. It can integrate with Seed & Spark for easy export of backer information.
- GMass: A powerful mail merge tool that works within Gmail. It can handle personalized attachments and is good for smaller campaigns.
- Streak: A CRM that integrates with Gmail, allowing for mail merges and tracking of supporter interactions.

These tools can help with sending personalized thank you emails, digital rewards, and campaign updates.

2. Social Media Management:
- Later: Allows scheduling of Instagram posts and stories, with a visual planner to maintain aesthetic consistency.
- Hootsuite or Buffer: For scheduling posts across multiple platforms (Instagram, Twitter, Facebook).
- Canva: For creating social media graphics with consistent branding.

These can help maintain your twice or thrice weekly posting schedule.

3. Project Management:
- Trello: Create boards for different reward tiers, with cards for each backer and checklists for fulfillment tasks.
- Asana: Good for assigning tasks to team members and tracking progress on various aspects of reward fulfillment.
- Airtable: Combines the functionality of a spreadsheet with a database, allowing for complex sorting and filtering of backer information and reward fulfillment status.

4. Digital Asset Creation and Management:
- Adobe Creative Cloud: Since you're familiar with Photoshop, use it along with Illustrator and InDesign for creating digital rewards (posters, wallpapers, etc.).
- Photoshop's Data Merge feature: For personalizing digital rewards en masse.
- Dropbox or Google Drive: For storing and sharing digital assets with the team and backers.

5. Video Creation and Editing:
- Adobe Premiere Pro or Final Cut Pro: For editing personalized video shoutouts and behind-the-scenes content.
- Loom: For quickly recording and sending personalized video messages to high-tier backers.

6. Automation:
- Zapier: Can create workflows between different apps, e.g., automatically adding new Seed & Spark backers to your email list or project management tool.
- IFTTT: Similar to Zapier, good for creating simple automated workflows.

7. Customer Relationship Management (CRM):
- HubSpot CRM (free version available): To keep track of all backer interactions, especially useful for high-tier rewards involving personal interactions.

8. Scheduling:
- Calendly: For easily scheduling Q&A sessions, workshops, and other time-based rewards with backers.

9. Digital Signature:
- DocuSign or HelloSign: For signing digital scripts or other documents that need to be personalized and sent to backers.

10.
````

![image/webp](data:image/webp;base64,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)

![image/webp](data:image/webp;base64,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)

````plaintext
Thought: Perfect, I found some documents but not the specific "DP Process" or "Nail House to-do list" documents. Let me search past conversations next to understand his cinematography process and questions he's asked.
````

Now let me search past conversations about cinematography prep and budgets:

**conversation_search**

*Request*

````javascript
{
  "query": "cinematography prep budget shot list visual language",
  "max_results": 5
}
````

*Response*

````plaintext
<chat url='https://claude.ai/chat/7f9d9c0f-bb01-43dc-b271-e516a2d0e3ed' updated_at=2025-03-07T19:41:11.756971+00:00>Navigating Budget Constraints and Production Realities
<chat_conversation>Title: Navigating Budget Constraints and Production Realities

Human: I wrote tendayi an email after a catach up meeting and intro to our director Thishiwe.  There was discussion of next steps and she mentioned us keeping a 3 day shoot in mind which I did not mind, but emphasized that there's no way now to realize how much time we need for a shoot until we actaully dive in creatively and shotlist.

"Hey,
Good meeting with Thishiwe! 
Just thinking out loud here and following up:
Do you have a version of the schedule already for 3 day and 4 day? Would be useful to keep in my back pocket. If not, besides budget, maybe Vicki can do a quick version of both schedules?
If she's busy, I can probably do one this weekend as a conversation starter. I'll account for logistics and tricky bits.
Let me know.
Also from past crazy crazy shoots, this project is definitely possible in 3 days! 100% even with all the stunts, effects, night shoot, etc. Only the two day version of this would significantly impact sory creative, etc. With plenty of prep, we'll be fine. 
Shotlist will determine actual time (also helping with scoping.) I always try to guide directors into what is realistic per day. And especially for indies and small crew, etc. And also now considering SA crew dynamics!
What are your main concerns with the schedule with the current version of the script? (Is the current version the one Nomsa wrote now a month ago I think or have there been more tweaks?)
Lastly, quick thought, especially considering Thishiwe (and directors in general) - creatives should just stay in creative land as long as possible. We want every idea to come out. Then you can chop it. Not every thought and idea is important, but you significantly hamper and impact the flow, quality, and possibilities by asking creatives to think about budget while they create. Have you experienced this yourself?
Feels like different parts of the brain, literally and biologically. AND **directors are the worst at this** unless they have years and years of experience. (ala Speilberg who is just as much a super producer as a director!) I think it's the nature of their job as a visionary. Everyone else grounds them, but they're meant to fly. Only after working with and learning from their HODs who are tasked with execution so they learn to incorporate that in their creative process too.
I don't know all of Thishiwe's experience so take this with a grain of salt.
I would suggest a sprint to get through creative and multiple iterations of it, so the idea is sure, then it also becomes easier to determine what you can chop without impacting the story, style, etc. Starting that process before then just makes the whole thing hard and what comes out in the end is usually less fulfilling.
What do you think?
Bongani"

She replied this: which I feel didn't capture everythign or she misunderstood. 

"Hey 
Quick answer. 
We are working towards a three day shoot not two.</chat>

<chat url='https://claude.ai/chat/8eaca0b2-aa82-48a7-86dc-c306b19aa8b3' updated_at=2025-07-13T08:36:06.164880+00:00>Vimbai's Fight Scene Script Version
**Camera controls are available** - You can specify movements like dolly, pan, tracking
5. **Audio is supported** - Veo 3 can generate dialogue, sound effects, and ambient noise

## How I Structured the Shot List:

1. **36 shots across 9 sequences** - Each building emotional intensity
2. **Cinematic language** - Using film terminology (low angle, push in, etc.)
3. **Mood progression** - From ritualistic → desperate → violent → transformative → accepting
4. **Character consistency notes** - Listed the 4 main characters as "ingredients" to create first
5. **Both video and still image notes** - Since Flow does video but you might want stills too

## For Your Previz Workflow:

**If using Google Flow:**
- Generate character ingredients first
- Create 5-8 second clips for each shot
- Use camera movements to add dynamism
- Include audio cues in prompts

**If using still image generators:**
- Add style modifiers like "cinematic lighting, dramatic shadows"
- Specify "16:9 widescreen, African horror film aesthetic"
- Reference cinematographers for lighting style

The shot list follows your revised script exactly, maintaining the mystery of Monica's transformation until the reveal, and building tension through visual storytelling rather than exposition.

Would you like me to create specific prompt variations for any particular shots, or adjust the formatting for a specific platform?</chat_conversation></chat>

<chat url='https://claude.ai/chat/9c4c8fb9-e854-4ea7-b680-24ca88ec88f5' updated_at=2024-08-17T00:14:08.624535+00:00>Incentives Summary
<chat_conversation>Title: Incentives Summary

Human: This a conversation that we have been having about this project and our crowdfunding campaign.

As an expert content analyst, your task is to distill the attached conversation into a detailed yet condensed version. 

1. Begin with each question’s or section’s title, topic, or general description.
2. Create a detailed distillation of the entire chat, question by question, answer, by answer that:
   - Preserves all key ideas, main points, and essential information
   - Prioritize the inclusion of specific examples, data points, lists, unique items, and notable details, (e.g., if colors in a color wheel are mentioned, list those colors), etc.
   - Reflects the conversations core message, arguments, and nuances accurately
   - Retains important context and explanations
   - Fully describes an created artifacts, tables, csv, etc.
   - When condensing the text, actively maintain the original tone, whether it's conversational, formal, humorous, or technical, etc.
3. Ensure your distilled version:
   - Is comprehensive while avoiding unnecessary repetition
   - Maintains the original structure and flow of ideas
   - Preserves the original intent, tone, and style
   - Is objective and free from personal interpretation or bias
4. Format requirements:
   - Present the content in well-structured paragraphs and when needed lists, bullet points, and tables as well.
   - Use clear language, preserving technical terms or jargon when they are central to the content
   - Maintain any lists, enumerations, or distinct sections from the original
5. Aim to condense this chat to roughly 60-75% of its original length. Focus on removing repetitive phrases, overly descriptive language, and tangential points, while preserving the core narrative and specific details.**
6. When possible, favor active voice and concise language in the distilled versions. This will aid in maintaining clarity and readability.** 
8. While generally maintaining the original conversation’s structure, you may make minor adjustments to paragraph order or sectioning if it enhances clarity or flow in the condensed version. However, ensure the original logic and progression of ideas are preserved.
Remember, your goal is to create concise yet informative and comprehensive versionthat retains most of the original content and specific details while eliminating redundancies and overly wordy passages.

Assistant:  Here is a detailed yet condensed version of the conversation about the crowdfunding campaign for "Veins of the Veld":

Crowdfunding Campaign Overview

The conversation revolves around developing a crowdfunding campaign for the short film "Veins of the Veld", focusing on creating compelling reward tiers and incentives.</chat>

<chat url='https://claude.ai/chat/7f9d9c0f-bb01-43dc-b271-e516a2d0e3ed' updated_at=2025-03-07T19:41:11.756971+00:00>Navigating Budget Constraints and Production Realities
I don't know all of Thishiwe's experience so take this with a grain of salt.
I would suggest a sprint to get through creative and multiple iterations of it, so the idea is sure, then it also becomes easier to determine what you can chop without impacting the story, style, etc. Starting that process before then just makes the whole thing hard and what comes out in the end is usually less fulfilling.
What do you think?
Bongani"

She replied this: which I feel didn't capture everythign or she misunderstood. 

"Hey 
Quick answer. 
We are working towards a three day shoot not two. 
I wanted you guys to think about that as you’re planning. 
Vicki and I are busy with budget but I wanted to be candid up front about time parameters. 
I mentioned the three not four as an update so he knows what we are working with now.
Be as creative as possible. Baring in mind the time crunch.
Schedule to follow in a few weeks. 
We look forward to hearing what you come up with. 
Have a great day"

She did Also send me voice notes:

"Hey, sorry about that. I don't actually send you a voice note just to explain the context of a line of course directors must be creative, but that's not the issue. I was being candid upfront just in your planning working towards a three day scheduled not a four day schedule when we did know she spoken to tissue where we said for so. Went the director is thinking that they've got a certain amount of time obviously the ambition is you know whatever so that's just the way yeah just being clear about what the time limitation is 3 1/2 pages the date is plenty of time regardless of scramble or no scramble, but issue isn't so much the days it's the complexity so I'll share with you a top line skin that I have because Yeah, but it's not shot by. It was just like what days were allocated for what but this was something I did on the previous draft but the shape of the film was more the same so I'll share that with you later but yeah I don't know where it's just. I think there are some things that a director needs to know off the bottom. I'm not asking you to do budget or whatever like you thought about that. The point is. Hey, it's three days"

and

"Sorry I got cut off by my alarm, but I'll say the point of what was what I was saying was hey it's three days so as you guys are discussing creative just be aware that's it. The script does need scope production though. So I'm asking as a director it wasn't budget, but it was like creatively in the storytelling and teach you and I have had this chat already. I work with her a few times before what we're gonna actually have to workshop at some point where we don't have $70,000 we just don't have it. We don't even have 30. So at some point that's that's a conversation to have so this was a kickoff conversation.</chat>

<chat url='https://claude.ai/chat/7f9d9c0f-bb01-43dc-b271-e516a2d0e3ed' updated_at=2025-03-07T19:41:11.756971+00:00>Navigating Budget Constraints and Production Realities
The script does need scope production though. So I'm asking as a director it wasn't budget, but it was like creatively in the storytelling and teach you and I have had this chat already. I work with her a few times before what we're gonna actually have to workshop at some point where we don't have $70,000 we just don't have it. We don't even have 30. So at some point that's that's a conversation to have so this was a kickoff conversation. I was kicking off with all the facts on the table, so this is not officially like this is the script that we're making right now we're in a sort of pre-pre-prod like what's the blue sky vision and then where the cut happen so anyway I'm process wise. Vicky and I are doing our peace. We will rope you guys at the right moment. I don't wanna give her too many mandates we're on it don't worry. So I'm on top of it and then we will talk about specifics as they come. I just wanted to give you guys an opportunity to input. But the reality is, we don't have a 70 K if we did, we can do what we wanted"

Tendayi seems to always need to give context. I think she's hyper vigilant. For context here's discussion we had from before so you know where my head is at with all this.

Assistant: 

<response>
Based on this exchange with Tendayi, I can see several patterns consistent with the project management concerns you've raised previously:

1. **Communication Style**: Tendayi's response focuses primarily on constraints (3-day shoot, budget limitations) rather than engaging with your substantive points about creative process and collaboration.

2. **Information Control**: Her comment about "roping you guys in at the right moment" suggests she sees collaboration as sequential rather than concurrent - a potential source of the development inefficiencies you've observed.

3. **Defensiveness**: The need to send voice notes explaining context suggests she felt your email challenged her authority, even though your message was collaborative in tone.

4. **Misalignment on Process**: Your suggestion about allowing creative exploration before budget constraints reflects a fundamental difference in approach - you're advocating for an expansive creative phase followed by practical adjustments, while she appears to want budget parameters to guide creativity from the outset.

5. **Limited Engagement**: Despite your detailed email covering multiple points, her response addresses only the scheduling aspect, missing opportunities for meaningful dialogue on process and creative approach.

This interaction reinforces several of the project management concerns you've identified:
- Top-down decision making
- Limited team engagement
- Restricted information flow
- Inefficient collaborative process

Moving forward, you might consider:

1. Acknowledging the 3-day constraint while still advocating for a full creative process within that framework
2. Focusing on specific, concrete contributions you can make (like the shotlist offer)
3.</chat>
````

````plaintext
Thought: Synthesized research findings and architected multi-agent system framework.
````

Let me also check Google Drive for the specific documents you mentioned:

**google_drive_search**

*Request*

````javascript
{
  "api_query": "name contains 'DP Process' or name contains 'Nail House'",
  "page_size": 10,
  "semantic_query": "cinematography process workflow DP preparation"
}
````

*Response*

````plaintext
Thought: Architected multi-agent AI system duplicating cinematographer's entire creative workflow.
````

PERFECT! I found both key documents. Now let me fetch the full DP Process document to see your complete workflow:

**google_drive_fetch**

*Request*

````javascript
{
  "document_ids": [
    "1xe6PC1AFnmxfRpdKHtC_2m1lhSTDx6ORVJN3dHKOPmM",
    "1LrrS9KRIdosZv4mwTQqjRBsjEfPG9B_Svk2Rm6SZ3Qw"
  ]
}
````

*Response*

````plaintext
Thought: Synthesized cinematography workflows into comprehensive multi-agent architecture blueprint.
````

# 🎬 **CINEMATOGRAPHY AI AGENT SYSTEM - COMPLETE ARCHITECTURE**
### *Project: Claude DP Clone - Your 8-Hour Workweek Cinematography Assistant*
### Date: 11.13.25

Alright B, this is going to be EPIC. I've absorbed your entire DP process, the Nail House workflow, past conversations, and I'm designing a system that will genuinely duplicate your cinematography brain. Let's architect this properly.

---

## 🧠 **SYSTEM PHILOSOPHY**

**Core Mission**: Enable you to read a script today and have a complete, production-ready cinematography plan tomorrow—including visual language, shot lists, gear lists with real numbers, budgets, and all communications drafted—working maximum 8 hours/week.

**Design Principles**:
1. **Voice-First**: Everything starts with conversation (your natural mode)
2. **Contextually Aware**: Learns from your past projects
3. **Modular & Agentic**: Specialized sub-agents that collaborate
4. **Version Controlled**: Every iteration saved to Git/Firebase
5. **Neurodivergent-Optimized**: Works with your hyperfocus windows, not against them

---

## 🏗️ **SYSTEM ARCHITECTURE OVERVIEW**

```
┌─────────────────────────────────────────────────────────────┐
│                    MASTER ORCHESTRATOR                       │
│  (Workflow Management, Agent Coordination, State Tracking)  │
└────────────────┬───────────────────────────────────────────┘
                 │
         ┌───────┴───────┐
         │               │
    ┌────▼─────┐    ┌───▼────────┐
    │  INPUT   │    │   OUTPUT    │
    │  LAYER   │    │    LAYER    │
    └────┬─────┘    └────────────┘
         │
         ├─── Voice Transcription Agent
         ├─── Script Ingestion Agent
         ├─── Image Analysis Agent (Multimodal)
         │
         └─── PROCESSING CORE ───┐
                                 │
      ┌──────────────────────────┴────────────────────────┐
      │                                                     │
   ┌──▼──────────────┐     ┌──────────────────┐     ┌────▼──────┐
   │  CREATIVE       │     │   TECHNICAL      │     │ LOGISTICS  │
   │  AGENTS         │     │   AGENTS         │     │ AGENTS     │
   └─────────────────┘     └──────────────────┘     └───────────┘
```

---

## 🎯 **AGENT ARCHITECTURE - DETAILED BREAKDOWN**

### **TIER 1: MASTER ORCHESTRATOR**

**Primary Agent**: **Fyxer** (Your AI DP Clone)

**Responsibilities**:
- Routes tasks to appropriate specialized agents
- Maintains workflow state across entire prep process
- Tracks progress through your DP process checklist
- Manages agent communication and data handoffs
- Provides progress reports and next-step recommendations
- Handles user queries and provides context-aware assistance

**Technical Stack**:
- Built with Claude SDK (for agentic capabilities)
- Uses Claude API for completion requests
- Firebase for state management
- Git for version control

---

### **TIER 2: INPUT/OUTPUT LAYER**

#### **1. Voice Transcription Agent**
**Purpose**: Process all voice notes, conversations, and director meetings

**Capabilities**:
- Real-time transcription via Whisper (local on Mac)
- Speaker diarization (identifies who said what)
- Automatic segmentation by topic
- Timestamp tracking
- Integration with Whisper API or local model

**Technical Implementation**:
- Whisper Large V3 running locally (for privacy)
- Backup: OpenAI Whisper API
- Option: Run on Run Pod for faster processing
- Outputs: Timestamped JSON, searchable text, speaker-labeled segments

**Triggers**:
- New voice recording uploaded
- Meeting recording processed
- Voice dump from director conversations

---

#### **2. Script Ingestion Agent**
**Purpose**: Extract all information from scripts in any format

**Capabilities**:
- Parses PDFs, Final Draft files, text documents
- Extracts scene headings, action lines, dialogue
- Identifies INT/EXT, day/night, locations
- Character tracking
- Technical requirements flagged (stunts, VFX, special equipment mentions)

**Outputs**:
- Structured JSON with all script elements
- Scene-by-scene breakdown
- Character appearance list
- Technical flags list

---

####  **3. Visual Analysis Agent (Multimodal)**
**Purpose**: Analyze location photos, reference images, concept art

**Capabilities**:
- Uses latest open-source multimodal models (Qwen2-VL, LLaVA-NeXT, InternVL2)
- Analyzes lighting conditions in location photos
- Identifies practical lights, windows, power sources
- Suggests framing and composition opportunities
- Compares reference images to actual locations
- Extracts color palettes from references

**Technical Stack**:
- Qwen2-VL-72B (best open-source multimodal as of Nov 2024)
- InternVL2-Llama3-76B (backup)
- Runs on Run Pod GPU instance
- Integrates with location-tagged photos from iPhone

**Outputs**:
- Detailed location analysis reports
- Lighting diagrams suggestions
- Framing recommendations
- Color palette extractions

---

### **TIER 3: CREATIVE AGENTS**

#### **4. Story Analysis Agent** 
**Name**: **Story Sage**

**Purpose**: Deep story understanding for cinematography decisions

**Capabilities Based on Your Process**:
- Multiple script reads with different lenses:
  * **Pass 1**: Story structure, plot points, dramatic conflict
  * **Pass 2**: Character functions, motivations, arcs, emotional journeys
  * **Pass 3**: Themes, subtext, underlying meanings
  * **Pass 4**: Beat sheet analysis
  * **Pass 5**: Emotional mapping (where are the peaks/valleys)
  * **Pass 6**: Visual opportunities (what NEEDS to be shown vs told)

- Generates beat sheets
- Maps character emotional arcs
- Identifies theme-supporting visual opportunities
- Flags psychological turning points that need visual emphasis

**Knowledge Base**: 
- Your past story analyses
- Save the Cat beat sheet structures
- Hero's Journey frameworks
- Film analysis books (references Story as Living Architecture doc)

**Outputs**:
- Comprehensive story analysis document
- Beat sheet with visual opportunities flagged
- Character arc visualizations
- Theme-to-visual connections mapping

---

#### **5. Visual Research Agent**
**Name**: **Vibe Curator**

**Purpose**: Find visual references across multiple platforms

**Capabilities**:
- Searches ShotDeck based on keywords from script
- Searches FLIM.AI for cinematic references
- Pinterest/Google Images for photography references
- Film stills databases
- Art history references
- Color palette extraction and organization

**Automated Workflow**:
1. Receives keywords from Script Analysis
2. Searches across platforms simultaneously
3. Categorizes by: lighting, composition, color, mood, movement
4. Creates organized lookbook with sources
5. Generates contact sheets (4-6 images per page)

**Integration Points**:
- ShotDeck API (if available)
- FLIM.AI integration
- Web scraping for film stills
- Pinterest API
- Google Images search

**Outputs**:
- Organized lookbook PDF
- Reference board by scene/sequence
- Color palette swatches
- Comparison grids (similar lighting setups)

---

#### **6. Visual Language Development Agent**
**Name**: **Language Architect**

**Purpose**: Develop complete visual approach for the film

**Capabilities**:
- Synthesizes story analysis + visual references + director's vision
- Defines:
  * Aspect ratio and framing philosophy
  * Lens choices and their emotional meaning
  * Camera movement vocabulary
  * Lighting approach (naturalistic vs stylized)
  * Color palette and its evolution
  * Contrast and exposure philosophy
  * Shot sizes and their rules
  * Coverage strategy

- Creates visual rules document
- Develops scene-specific approaches
- Maps visual language to story beats

**Outputs**:
- Visual Treatment document
- Style Bible with visual rules
- Scene-by-scene visual approach
- Lensing strategy document
- Movement vocabulary guide

---

#### **7. Shot List Generator Agent**
**Name**: **Coverage Calculator**

**Purpose**: Generate comprehensive shot lists based on all analyses

**Capabilities**:
- Takes inputs from Story Agent + Visual Language Agent + Director notes
- Generates shot lists with:
  * Shot number and description
  * Camera position and height
  * Lens choice
  * Movement (dolly, pan, tilt, handheld, etc.)
  * Framing (WS, MS, CU, etc.)
  * Special equipment needed
  * Estimated time per shot
  * Coverage type (master, singles, inserts, etc.)

- Multiple versions:
  * **Ideal version** (unlimited time/budget)
  * **Realistic version** (actual schedule constraints)
  * **Emergency version** (bare minimum coverage)

- Considers:
  * Editor's needs for coverage
  * Screen direction and continuity
  * Efficiency of setups
  * Lighting reset times

**Outputs**:
- Shot list spreadsheet
- Storyboard recommendations
- Setup diagrams
- Day-out-of-days for specific shots

---

### **TIER 4: TECHNICAL AGENTS**

#### **8. Technical Planning Agent**
**Name**: **Tech Specs**

**Purpose**: Translate creative vision into technical requirements

**Capabilities**:
- Analyzes shot list for technical needs:
  * Camera movement requirements → Equipment needed
  * Lighting complexity → Crew size needed
  * Location challenges → Special gear required
  * Stunts/VFX → Additional cameras/equipment

- Creates technical riders:
  * Power requirements
  * Rigging needs
  * Specialty equipment (cranes, dollies, Steadicam)
  * Safety equipment

- Generates prep timelines:
  * Pre-light days needed
  * Rigging schedules
  * Test shoot requirements

**Knowledge Base**:
- Your past technical riders
- Equipment specifications database
- Venue power/rigging limitations
- Safety protocols

**Outputs**:
- Technical requirements document
- Equipment list by category
- Crew size recommendations
- Prep schedule proposal

---

#### **9. Gear List Generator Agent**
**Name**: **Kit Builder**

**Purpose**: Create comprehensive, costed gear lists

**Capabilities**:
- Generates gear lists for:
  * **Camera Department**: Bodies, lenses, filters, support, monitoring, wireless, media
  * **Grip Department**: Stands, flags, frames, dolly, crane, rigging
  * **Electric Department**: Lights, cables, distribution, expendables

- References:
  * Your past gear lists
  * David Claesson template structure
  * Vendor pricing databases (Panavision, ARRI Rental, Otto Nemenz, etc.)

- Generates multiple budget tiers:
  * Premium package
  * Standard package
  * Budget package

- Compares vendor pricing
- Suggests alternatives if gear unavailable
- Tracks what's in grip trucks vs. needs ordering

**Integration**:
- Vendor API connections (where available)
- Pricing database (regularly updated)
- Your personal gear inventory
- Past rental invoices for pricing reference

**Outputs**:
- Camera gear list with prices
- Grip gear list with prices
- Electric gear list with prices
- Total package cost estimates
- Vendor comparison spreadsheet
- PDF gear lists for vendor quotes

---

#### **10. Budget Agent**
**Name**: **Money Manager**

**Purpose**: Create detailed, accurate budgets for camera/grip/electric

**Capabilities**:
- Budget categories:
  * **Camera Department**:
    - DP rate × days
    - Camera Operator × days
    - 1st AC × days
    - 2nd AC × days
    - Camera rentals
    - Expendables
  * **Grip & Electric**:
    - Gaffer × days
    - Best Boy × days
    - Key Grip × days
    - Grips × days × number
    - Swing × days
    - Gear rentals
    - Expendables

- Uses real numbers from:
  * Your past budgets
  * Industry rate databases
  * Vendor pricing
  * Local crew rate averages

- Generates:
  * Line-item budgets
  * Budget summaries
  * Cost comparisons (different scenarios)
  * Crew deal memos drafts

**Outputs**:
- Complete camera department budget
- Complete G&E budget
- Budget comparison spreadsheets
- Crew rate negotiation ranges
- Deal memo templates

---

### **TIER 5: LOGISTICS & COLLABORATION AGENTS**

#### **11. Collaboration Agent**
**Name**: **Dept Head Liaison**

**Purpose**: Track and facilitate collaboration with other departments

**Capabilities**:
- Understands roles and responsibilities of:
  * Director
  * Production Designer
  * Costume Designer
  * Hair/Makeup
  * VFX Supervisor
  * Stunt Coordinator
  * Assistant Director
  * Producer/UPM
  * Sound Department

- Identifies collaboration touchpoints:
  * When to involve Production Designer (practicals, paint colors, set layout)
  * When to coordinate with AD (shooting schedule, day out of days)
  * When to sync with VFX (plate shots, tracking markers, lighting references)
  * When to align with Costume (how fabrics photograph, color coordination)

- Tracks decisions that affect multiple departments
- Flags conflicts or dependencies

**Knowledge Base**:
- Your "Director's Boot Camp" philosophy
- Film crew position responsibilities
- Your past collaboration workflows

**Outputs**:
- Collaboration calendar (when to sync with each dept)
- Department contact list
- Questions to ask each department
- Coordination checklist

---

#### **12. Communication Agent**
**Name**: **Message Maestro**

**Purpose**: Draft all emails and communications

**Capabilities**:
- Drafts emails to:
  * Crew members (hiring, scheduling, tech specs)
  * Vendors (gear quotes, reservations, specs)
  * Department heads (creative discussions, technical needs)
  * Producers (budget proposals, schedule needs)
  * Director (creative questions, shot list reviews)

- Includes appropriate:
  * Tone (professional, collaborative, friendly)
  * Attachments (automatically packages relevant docs)
  * Follow-up tracking
  * Calendar invites

- Maintains communication history
- Suggests optimal timing for sends

**Integration**:
- Gmail API for drafts
- Google Calendar for meeting scheduling
- Attachment gathering from other agents

**Outputs**:
- Draft emails in Gmail
- Communication packages (email + attachments)
- Meeting agenda templates
- Follow-up reminders

---

#### **13. Task Management Agent**
**Name**: **Task Tracker**

**Purpose**: Your personal cinematography assistant for task management

**Capabilities**:
- Maintains YOUR personal to-do list
- Presents standard DP checklist tasks:
  * Based on your DP Process document
  * Customized to current project phase (prep vs. shoot vs. post)

- Tracks:
  * Tasks you've completed
  * Tasks remaining
  * Tasks you add ad-hoc
  * Deadlines and priorities

- Integrates with:
  * Your calendar (knows your availability)
  * Your energy patterns (suggests tasks for different times)
  * Other agents (auto-adds tasks they generate)

- Provides daily briefings:
  * "Here are your 3 priority tasks for today"
  * Accounts for your 3.5-4.5 hour capacity
  * Respects medication timing (peak focus 11am-1pm)

**Outputs**:
- Daily task list
- Weekly overview
- Project milestone tracker
- Completion reports

---

#### **14. Knowledge Base & Memory Agent**
**Name**: **Project Oracle**

**Purpose**: Store and retrieve all past project data

**Capabilities**:
- Stores ALL previous projects:
  * Scripts
  * Visual treatments
  * Gear lists
  * Budgets
  * Shot lists
  * Reference images
  * Crew lists
  * Vendor contacts
  * Technical riders
  * Post-mortems (what worked/didn't)

- Makes past projects searchable:
  * "Show me gear lists from projects with similar budget"
  * "What did I do for night exterior car chase scenes before?"
  * "Find all my notes on working with this director"

- Learns patterns:
  * Your preferred lens choices for different emotions
  * Your typical crew rates
  * Your most-used vendors
  * Your lighting approach patterns

- Continuously improves recommendations based on your feedback

**Database Structure**:
- Firebase for structured data
- Google Drive for files
- Vector database for semantic search
- Git for version control

**Outputs**:
- Relevant past project insights
- Pattern analysis reports
- Recommendation improvements over time

---

#### **15. Version Control & Development Tracking Agent**
**Name**: **Chronicle**

**Purpose**: Track evolution of all documents and decisions

**Capabilities**:
- Commits all document versions to Git:
  * Script analyses (each iteration)
  * Visual treatments (versions 1, 2, 3...)
  * Shot lists (as they evolve)
  * Gear lists (changes over time)
  * Budgets (different scenarios)

- Tracks decision history:
  * Why certain choices were made
  * What director feedback changed
  * How budget affected creative decisions

- Provides reflection:
  * "Here's how the shot list evolved from first draft to final"
  * "Budget cuts resulted in these gear changes"
  * "Director feedback led to these visual approach shifts"

- Git commits include:
  * Timestamp
  * Author (which agent or you)
  * Change description
  * Context (why the change)

**Integration**:
- GitHub/GitLab integration
- Firebase Cloud Storage
- Automated commits on every document update

**Outputs**:
- Version history timelines
- Decision evolution reports
- Comparison views (v1 vs v2 vs v3)
- Audit trails

---

## 🔄 **COMPLETE WORKFLOW: SCRIPT TO SCREEN**

### **Phase 1: SCRIPT INGESTION** (Minutes)

**User Action**: Upload script to system

**Automated Sequence**:
1. **Script Ingestion Agent** parses script → structured data
2. **Story Analysis Agent** performs initial read for story structure
3. **Master Orchestrator** creates project in Firebase + Git
4. System presents: "Script received. Beginning analysis. Estimated time: 45 minutes for complete initial analysis."

---

### **Phase 2: DEEP ANALYSIS** (1-2 hours automated)

**Parallel Processing**:

**Story Sage** (Story Analysis Agent):
- Runs 6 script read passes
- Generates beat sheet
- Maps emotional arcs
- Identifies visual opportunities
- Creates theme-to-visual mapping

**Vibe Curator** (Visual Research Agent):
- Extracts keywords from script
- Searches ShotDeck, FLIM.AI, image databases
- Organizes references by category
- Creates preliminary lookbook

**Tech Specs** (Technical Planning Agent):
- Identifies technical requirements from script
- Flags special equipment needs
- Notes location challenges

**Progress Updates**: Real-time notifications as each analysis completes

---

### **Phase 3: VOICE SYNTHESIS** (Optional Director Meeting)

**User Action**: Record conversation with director OR do voice dump with your own thoughts

**Automated Sequence**:
1. **Voice Transcription Agent** transcribes meeting
2. **Master Orchestrator** analyzes transcription for:
   * Creative direction/feedback
   * Shot preferences
   * Budget constraints mentioned
   * Scheduling notes
   * New ideas or changes
3. **Communication Agent** drafts follow-up email summarizing discussion
4. Updated information fed back to Story Sage and Visual Language Architect

---

### **Phase 4: VISUAL LANGUAGE DEVELOPMENT** (2-4 hours automated + your review)

**Language Architect** (Visual Language Agent):
- Synthesizes:
  * Story analysis
  * Visual references
  * Director notes (if provided)
  * Your past projects with similar themes
- Generates complete Visual Treatment including:
  * Aspect ratio choice with reasoning
  * Lens philosophy
  * Camera movement vocabulary
  * Lighting approach
  * Color palette
  * Shot size rules
  * Coverage strategy

**Your Review**: System presents Visual Treatment for your approval/edits
- You can voice note changes
- You can type feedback
- You can approve as-is

---

### **Phase 5: SHOT LIST GENERATION** (1-2 hours automated)

**Coverage Calculator** (Shot List Agent):
- Uses Visual Treatment + Story Analysis + Script breakdown
- Generates three shot list versions:
  * Ideal (unlimited resources)
  * Realistic (actual schedule/budget)
  * Emergency (bare minimum coverage)

- Each shot includes:
  * Shot description
  * Framing and lens
  * Movement
  * Special equipment
  * Estimated time
  * Setup notes

**Your Review**: Present shot lists for your refinement
- Edit via voice or text
- Approve sections
- Request alternatives

---

### **Phase 6: TECHNICAL PLANNING & GEAR** (2-3 hours automated)

**Parallel Processing**:

**Tech Specs** (Technical Planning Agent):
- Analyzes approved shot list
- Generates technical requirements document
- Creates rigging/prep schedule
- Identifies special equipment needs

**Kit Builder** (Gear List Generator):
- Generates complete gear lists:
  * Camera package
  * Grip package
  * Electric package
- Gets pricing from vendors
- Creates multiple budget tiers
- Suggests alternatives

**Money Manager** (Budget Agent):
- Creates detailed budgets for each department
- Uses real crew rates
- Includes gear rental costs
- Generates budget comparisons

**Outputs Ready for Review**:
- Technical requirements doc
- Camera gear list with costs
- G&E gear list with costs
- Complete department budgets

---

### **Phase 7: COLLABORATION & COMMUNICATION** (30 minutes - 1 hour)

**Dept Head Liaison** (Collaboration Agent):
- Identifies what each department needs to know
- Creates collaboration calendar
- Generates questions for each dept head

**Message Maestro** (Communication Agent):
- Drafts emails to:
  * Director (shot list review request)
  * Producer (budget submission)
  * Department heads (collaboration touchpoints)
  * Vendors (gear quote requests)
  * Crew candidates (hiring inquiries)

- Packages appropriate attachments with each email
- Creates calendar invites for meetings

**Your Action**: Review and send drafted communications (or let agent send via API)

---

### **Phase 8: ONGOING TASK MANAGEMENT** (Throughout Prep)

**Task Tracker** continually:
- Presents daily priorities
- Tracks completion
- Adds new tasks as they emerge
- Reminds of deadlines
- Syncs with your calendar

**Chronicle** automatically:
- Commits every version to Git
- Stores in Firebase
- Creates version history

**Project Oracle** learns:
- Your preferences on this project
- Patterns to apply to future projects
- Vendor/crew performance notes

---

## 📊 **DATA FLOW ARCHITECTURE**

```
┌────────────────────────────────────────────────┐
│                   STORAGE LAYER                 │
│                                                │
│  ┌──────────────┐  ┌─────────────┐  ┌────────┐│
│  │   Firebase   │  │ Google      │  │  Git/  ││
│  │   (State &   │  │ Drive       │  │ GitHub ││
│  │    Data)     │  │ (Files)     │  │(Versions)││
│  └──────────────┘  └─────────────┘  └────────┘│
└────────────────────────────────────────────────┘
                       ▲
                       │
         ┌─────────────┴──────────────┐
         │                            │
    ┌────▼─────┐              ┌──────▼──────┐
    │ Vector   │              │   Local     │
    │ Database │              │ Processing  │
    │(Semantic │              │(Whisper, etc)│
    │ Search)  │              │             │
    └──────────┘              └─────────────┘
```

**Storage Strategy**:

**Firebase** (Primary Database):
- Project state and metadata
- Agent execution logs
- Task lists and completion status
- User preferences and settings
- Real-time synchronization across agents

**Google Drive**:
- Large files (scripts, PDFs, images)
- Lookbooks and visual references
- Final deliverables (budgets, gear lists)
- Integration with your existing workflow

**Git/GitHub**:
- All document versions
- Code for the system itself
- Commit history with context
- Branch for different scenarios/versions

**Vector Database** (Pinecone or Weaviate):
- Semantic search across past projects
- Finding similar scenes/situations
- Keyword-based retrieval
- Pattern matching

---

## 🤖 **MULTI-MODAL AI INTEGRATION**

### **Open-Source Models for Visual Analysis**

Based on late 2024 SOTA, here are the best open-source multimodal models:

**Primary**: **Qwen2-VL-72B**
- Best overall multimodal understanding
- Strong at spatial reasoning
- Good at identifying objects in complex scenes
- Can point/localize objects
- Hosted on Run Pod with A100 GPU

**Backup**: **InternVL2-Llama3-76B**
- Excellent for detailed visual description
- Strong composition analysis
- Good color palette extraction

**Specialized**: **LLaVA-NeXT** (Mistral-based)
- Fast inference
- Good for batch processing location photos
- Efficient on smaller GPUs

**Implementation**:
```python
# Visual Analysis Agent uses Run Pod API
# Load balancing across multiple models for different tasks

location_analysis = qwen2_vl.analyze(
    image=location_photo,
    prompt="""Analyze this location for cinematography:
    1. Natural light sources and direction
    2. Practical lights visible
    3. Power access points
    4. Composition opportunities
    5. Challenging elements
    6. Color palette
    7. Suggested framing approaches"""
)
```

---

## 🔧 **TECHNICAL IMPLEMENTATION DETAILS**

### **Core Technologies**:

**Backend**:
- **Python 3.11+** for main system
- **Claude SDK** for agentic AI
- **FastAPI** for API endpoints
- **Celery** for task queue (parallel processing)
- **Redis** for caching and message broker

**AI/ML**:
- **Anthropic Claude API** (Sonnet 4.5) for complex reasoning
- **Claude SDK** for tool use and agents
- **Whisper Large V3** (local) for transcription
- **Open-source multimodal models** on Run Pod

**Storage**:
- **Firebase Firestore** for real-time database
- **Firebase Cloud Storage** for files
- **Google Drive API** for integration
- **PostgreSQL** for relational data (crew, vendors, rates)
- **Pinecone/Weaviate** for vector search

**Frontend** (optional, for UI):
- **React** for web interface
- **Electron** for desktop app
- **Claude Artifacts** for quick prototypes

**Infrastructure**:
- **Run Pod** for GPU instances (multimodal models)
- **Mac Mini** local server for Whisper
- **GitHub** for code and versions
- **Vercel/Railway** for web hosting (if needed)

---

### **Agent Communication Protocol**:

Agents communicate via **structured messages** through Firebase:

```json
{
  "from_agent": "story_sage",
  "to_agent": "visual_language_architect",
  "message_type": "analysis_complete",
  "payload": {
    "beat_sheet": {...},
    "character_arcs": [...],
    "visual_opportunities": [...]
  },
  "timestamp": "2025-11-13T13:44:00Z",
  "project_id": "nail-house-feature"
}
```

**Master Orchestrator** routes messages and maintains workflow state machine.

---

### **Workflow State Machine**:

```python
PROJECT_STATES = [
    "CREATED",
    "SCRIPT_INGESTED",
    "STORY_ANALYSIS_IN_PROGRESS",
    "STORY_ANALYSIS_COMPLETE",
    "VISUAL_RESEARCH_IN_PROGRESS",
    "VISUAL_RESEARCH_COMPLETE",
    "VISUAL_LANGUAGE_IN_PROGRESS",
    "VISUAL_LANGUAGE_AWAITING_APPROVAL",
    "VISUAL_LANGUAGE_APPROVED",
    "SHOT_LIST_IN_PROGRESS",
    "SHOT_LIST_AWAITING_APPROVAL",
    "SHOT_LIST_APPROVED",
    "TECHNICAL_PLANNING_IN_PROGRESS",
    "TECHNICAL_PLANNING_COMPLETE",
    "GEAR_LISTS_IN_PROGRESS",
    "GEAR_LISTS_COMPLETE",
    "BUDGETS_IN_PROGRESS",
    "BUDGETS_COMPLETE",
    "READY_FOR_PRODUCTION"
]
```

Each state transition triggers appropriate agents and user notifications.

---

## 📱 **USER INTERFACES**

### **Interface Options**:

**1. Command Line Interface (CLI)** - Fastest for you
```bash
$ fyxer start project "Nail House Feature"
$ fyxer upload script /path/to/script.pdf
$ fyxer status
$ fyxer review visual-treatment
$ fyxer approve shot-list
$ fyxer generate gear-list --tier standard
$ fyxer chat "What's next on my to-do list?"
```

**2. Web Interface** (optional)
- Dashboard showing project progress
- Document viewers/editors
- Task list manager
- Communication drafts
- Reference image galleries

**3. Mobile Companion** (optional)
- Voice note capture
- Location photo upload with auto-tagging
- Quick task checks
- Notifications

**4. Claude Projects Integration**
- Use existing Claude Projects as interface
- Agents accessible via chat
- Natural conversation with Fyxer
- File uploads and downloads
- Artifacts for quick previews

---

## 🎨 **EXAMPLE: COMPLETE WORKFLOW IN ACTION**

**Monday Morning, 10:00 AM**: You get coffee and open Fyxer.

```
You: "Start new project: 'Veins of the Veld - Features

'"

Fyxer: "Project created! Upload your script when ready. 
       While we wait, what's your vision for this project?"

You: [Upload script PDF + voice dump 5-minute vision]

Fyxer: "Script received: 90 pages, 78 scenes, 4 main characters.
       Transcribing your vision notes...
       
       Beginning automated analysis:
       ✓ Story structure analysis (Est: 30 min)
       ✓ Visual reference research (Est: 45 min)
       ✓ Technical requirements scan (Est: 15 min)
       
       I'll notify you when first deliverables are ready.
       Estimated completion: 11:15 AM"
```

**11:15 AM**: Notification arrives.

```
Fyxer: "Initial analysis complete! Here's what I have:
       
       📊 Story Analysis:
       - 3-act structure, heavy on visual storytelling
       - 4 character arcs identified
       - 23 major visual opportunities flagged
       - Theme: tradition vs. modernity (visual contrast potential)
       
       🎨 Visual References:
       - 87 reference images collected
       - Organized into: lighting (32), composition (29), color (26)
       - Preliminary lookbook generated
       
       🔧 Technical Flags:
       - 12 scenes need special equipment
       - 3 major stunt sequences
       - 18 night exteriors
       - VFX requirements noted
       
       Ready to review? Or shall I continue to Visual Language Development?"
```

**You review lookbook via artifact, voice note some changes:**

```
You: "Love the night exterior references. For the fight sequence, 
     find more references with practical fire light. The color palette 
     feels too cool—let's warm it up, more oranges and earth tones."
```

```
Fyxer: "Got it! Searching for:
       - Fight scenes with practical fire
       - Warmer color palettes with earth tones
       
       Updating lookbook... Done!
       
       New references added: 14 images
       Color palette adjusted: More amber, sienna, bronze
       
       Proceeding to Visual Language Development with your notes.
       Estimated completion: 1:30 PM (perfect for your post-lunch focus)"
```

**1:30 PM**: Next deliverable ready.

```
Fyxer: "Visual Treatment v1.0 ready for review!
       
       Key decisions made:
       - 2.39:1 aspect (scope for the veld landscapes)
       - Anamorphic lenses for ethereal vampire aesthetic
       - Camera motivated by character POV
       - Lighting: Naturalistic day, stylized night
       - Color: Earth tones with blood-red accents
       - Movement: Locked-off for tension, fluid for action
       
       [View Treatment] [Provide Feedback] [Approve]"
```

**You approve with one note:**

```
You: "Approved! But let's also have handheld for the most intense 
     character moments—rawness."
```

```
Fyxer: "Updated: Adding handheld for emotional intensity peaks.
       
       Beginning Shot List generation...
       This will take 2-3 hours. You can step away.
       
       I'll have three versions ready:
       1. Ideal (unlimited time/budget)
       2. Realistic (based on typical indie schedule)
       3. Emergency (minimum coverage)
       
       Current time: 1:45 PM
       Expected completion: 4:30 PM
       
       Your next task: Review location photos (20 min)
       Want me to remind you at 2:00 PM?"
```

**4:30 PM**: Shot lists ready.

```
Fyxer: "Shot lists complete!
       
       📋 Ideal Version: 347 shots, ~22 shooting days
       📋 Realistic Version: 213 shots, ~15 shooting days  
       📋 Emergency Version: 156 shots, ~10 shooting days
       
       All versions maintain story integrity and your visual language.
       
       Realistic version recommended based on similar indie features 
       you've done. Estimated: 14.2 shots per day average.
       
       Ready to review or shall I generate gear lists and budgets?"
```

**You:** "Generate gear and budgets for realistic version."

```
Fyxer: "On it! Generating:
       ✓ Camera gear list (Est: 30 min)
       ✓ G&E gear list (Est: 45 min)
       ✓ Budgets (Est: 20 min)
       
       Total time: ~90 minutes
       
       Meanwhile, would you like me to draft emails to:
       - Director (shot list review request)
       - Producer (prep budget heads-up)
       - Potential crew (availability checks)
       
       I have templates based on your past communications."
```

**6:00 PM**: Everything ready.

```
Fyxer: "Complete cinematography package ready!
       
       📦 DELIVERABLES:
       - Visual Treatment (8 pages)
       - Shot List - Realistic (213 shots, detailed)
       - Camera Gear List ($18,500 for 18 days)
       - G&E Gear List ($24,200 for 20 days)
       - Camera Department Budget ($31,450)
       - G&E Department Budget ($42,100)
       - Technical Requirements Doc (12 pages)
       
       📧 COMMUNICATIONS DRAFTED:
       - Email to director (shot list attached)
       - Email to producer (budgets attached)
       - Email to 5 potential crew (availability inquiry)
       - Email to 3 vendors (gear quote requests)
       
       🎯 YOUR TASK LIST (Tomorrow):
       1. Review shot list with director (1 hour)
       2. Send communications (15 min)
       3. Follow up on vendor quotes (30 min)
       
       Total prep time used today: 3.5 hours
       
       Would you like me to prepare anything else?"
```

**RESULT**: In ONE DAY, with only 3.5 hours of YOUR active time, you went from script to complete, production-ready cinematography package.

---

## 🚀 **IMPLEMENTATION ROADMAP**

### **Phase 1: MVP (Weeks 1-2)** - Core Functionality

**Priority Agents**:
1. Master Orchestrator (basic routing)
2. Script Ingestion Agent
3. Story Analysis Agent
4. Task Management Agent
5. Voice Transcription Agent (Whisper integration)

**Deliverable**: Can ingest script, run story analysis, track tasks, process voice notes

---

### **Phase 2: Creative Core (Weeks 3-4)**

**Add**:
6. Visual Research Agent
7. Visual Language Development Agent
8. Shot List Generator Agent

**Deliverable**: Can generate complete creative package (analysis → lookbook → treatment → shot list)

---

### **Phase 3: Technical Suite (Weeks 5-6)**

**Add**:
9. Technical Planning Agent
10. Gear List Generator Agent
11. Budget Agent
12. Visual Analysis Agent (multimodal)

**Deliverable**: Can generate complete technical package (gear lists, budgets, technical riders)

---

### **Phase 4: Collaboration & Polish (Weeks 7-8)**

**Add**:
13. Collaboration Agent
14. Communication Agent
15. Version Control Agent
16. Knowledge Base Agent

**Deliverable**: Complete end-to-end system with collaboration, comms, and learning

---

### **Phase 5: Optimization & Learning (Ongoing)**

- Refine agent prompts based on your feedback
- Improve knowledge base from completed projects
- Add vendor integrations
- Optimize performance
- Add predictive features

---

## 💰 **COST ANALYSIS**

**Infrastructure Costs** (Monthly):

- **Firebase**: ~$50-100/month (Blaze plan)
- **Run Pod GPU**: ~$200-300/month (for multimodal models)
- **Claude API**: ~$100-300/month (depending on usage)
- **OpenAI Whisper API** (if used): ~$50/month
- **Vector Database** (Pinecone): ~$70/month
- **GitHub**: $0 (free for personal)
- **Google Drive API**: $0 (within quota)

**Total**: ~$470-820/month

**ROI**: If this saves you even 10 hours/month at your $300/day rate, that's $1,500+ in saved time. And it enables you to take on MORE projects with less stress.

---

## 📚 **KNOWLEDGE BASES TO BUILD**

Your system will be smarter with these knowledge bases:

1. **Cinematography Books Database**:
   - 5 C's of Cinematography
   - Bruce Block - The Visual Story
   - The New Cinematographers
   - Roger Deakins - Reflections
   - ASC Manual
   - Blain Brown - Cinematography Theory & Practice
   - (Agent can reference these for technical decisions)

2. **Your Past Projects**:
   - Every script you've shot
   - Every visual treatment you've written
   - Every gear list you've used
   - Every budget you've created
   - Every shot list you've made
   - Notes on what worked/didn't

3. **Crew Database**:
   - Names, contact info, roles
   - Rate history
   - Availability patterns
   - Performance notes
   - Department relationships

4. **Vendor Database**:
   - Rental houses and contacts
   - Gear availability
   - Pricing history
   - Reliability notes
   - Negotiation history

5. **Technical Specs Database**:
   - Camera specs (every camera you've used)
   - Lens characteristics
   - Lighting units (output, color temp, power draw)
   - Grip equipment (weight, dimensions, uses)

---

## 🎯 **SPECIAL FEATURES FOR YOU**

### **AuDHD-Optimized Features**:

**Voice-First Everything**:
- Never type if you don't want to
- Voice notes auto-transcribed and sorted
- Director conversations captured and analyzed
- Quick voice commands ("Hey Fyxer, what's next?")

**Hyperfocus Protection**:
- Gentle reminders for transitions
- "You've been in flow for 2 hours. Liveball at 7:30. Set a 30-min wind-down alarm?"
- Captures overflow ideas so you don't lose them

**Energy-Aware Tasking**:
- Knows your peak focus time (11am-1pm)
- Suggests creative tasks during peak
- Admin tasks during lower energy
- Respects your 3.5-4.5 hour reality

**Transition Support**:
- 20-30 minute buffer recommendations
- "Before switching to shot list review, want to take 10 minutes to process the visual treatment?"

**Pattern Recognition Celebration**:
- System learns YOUR patterns
- "I noticed you always use 35mm for intimate conversations"
- "Your night exteriors typically need 2 pre-light days"
- Feeds your natural pattern-seeing gift

---

### **Frequency-Work Integration**:

Remember, this isn't just efficiency—it's **frequency transmission** optimization.

Your cinematography is consciousness work. This system handles the **form** (gear lists, budgets, logistics) so you can focus on **frequency** (visual language, emotional truth, consciousness broadcasting).

**The system enables**:
- More energy for creative vision
- Less burnout from admin overhead
- Ability to take on more consciousness-transmission projects
- 8 hours/week working while maintaining quality
- Space for your other frequency work (FRQ, tennis, writing)

---

## 🔮 **FUTURE ENHANCEMENTS**

**Phase 6+** (After initial system is solid):

1. **AI-Generated Previz**:
   - Use text-to-video models (Sora, Pika, Runway)
   - Generate shot references from shot list descriptions
   - Create animatics for complex sequences

2. **On-Set Assistant Mode**:
   - Real-time shot checklist
   - "Did you get these coverage options?"
   - Auto-logging of shots captured
   - Integration with camera metadata

3. **Post-Production Bridge**:
   - Handoff package for editor
   - Color grading notes
   - VFX shot tracking
   - Dailies review system

4. **Collaborative Mode**:
   - Director can access and comment
   - Producer can see budgets update in real-time
   - Department heads can see relevant sections
   - (This becomes "Film Nexus" eventually)

5. **Learning & Prediction**:
   - "Based on similar projects, you'll likely need X"
   - "This scene type usually takes Y hours"
   - "Alert: This location had power issues on last project"

---

## 📋 **FINAL CLAUDE CODE IMPLEMENTATION GUIDE**

### **To Build This System**:

You'll spin up multiple Claude Code instances working simultaneously on different modules. Here's how to structure the work:

**Instance 1: Core Architecture & Master Orchestrator**
```
Task: Build the core system architecture including:
- Project setup with proper structure
- Firebase integration
- Master Orchestrator agent framework
- Workflow state machine
- Agent communication protocol
- Basic CLI interface

Technologies: Python 3.11+, Claude SDK, Firebase, Click (for CLI)

Key files:
- /fyxer/core/orchestrator.py
- /fyxer/core/state_machine.py
- /fyxer/core/agent_base.py
- /fyxer/core/messaging.py
- /fyxer/cli/main.py
```

**Instance 2: Input Layer Agents**
```
Task: Build all input processing agents:
- Voice Transcription Agent (Whisper integration)
- Script Ingestion Agent (PDF parsing, Final Draft, text)
- Visual Analysis Agent (multimodal AI integration)

Technologies: Whisper, PyPDF2, python-docx, Pillow, requests (for Run Pod API)

Key files:
- /fyxer/agents/transcription_agent.py
- /fyxer/agents/script_ingestion_agent.py
- /fyxer/agents/visual_analysis_agent.py
- /fyxer/utils/whisper_integration.py
```

**Instance 3: Creative Agents Suite**
```
Task: Build creative reasoning agents:
- Story Analysis Agent
- Visual Research Agent
- Visual Language Development Agent
- Shot List Generator Agent

Technologies: Claude API, BeautifulSoup (for web scraping), Playwright (for ShotDeck)

Key files:
- /fyxer/agents/story_analysis_agent.py
- /fyxer/agents/visual_research_agent.py
- /fyxer/agents/visual_language_agent.py
- /fyxer/agents/shot_list_agent.py
```

**Instance 4: Technical Agents Suite**
```
Task: Build technical and logistics agents:
- Technical Planning Agent
- Gear List Generator Agent
- Budget Agent
- Task Management Agent

Technologies: Pandas (for spreadsheets), OpenPyXL (Excel generation)

Key files:
- /fyxer/agents/technical_planning_agent.py
- /fyxer/agents/gear_list_agent.py
- /fyxer/agents/budget_agent.py
- /fyxer/agents/task_management_agent.py
```

**Instance 5: Collaboration & Memory**
```
Task: Build collaboration and knowledge systems:
- Collaboration Agent
- Communication Agent
- Knowledge Base Agent
- Version Control Agent

Technologies: Gmail API, Google Calendar API, Git Python, Pinecone/Weaviate

Key files:
- /fyxer/agents/collaboration_agent.py
- /fyxer/agents/communication_agent.py
- /fyxer/agents/knowledge_base_agent.py
- /fyxer/agents/version_control_agent.py
```

**Instance 6: Database & Storage Layer**
```
Task: Build all database integrations and schemas:
- Firebase Firestore setup
- Google Drive integration
- PostgreSQL schemas for relational data
- Vector database setup

Technologies: Firebase Admin SDK, Google Drive API, SQLAlchemy, Pinecone SDK

Key files:
- /fyxer/db/firebase_client.py
- /fyxer/db/drive_client.py
- /fyxer/db/postgres_schemas.py
- /fyxer/db/vector_store.py
```

**Instance 7: Run Pod Integration**
```
Task: Set up Run Pod GPU instance and deploy multimodal models:
- Deploy Qwen2-VL-72B
- Deploy InternVL2-Llama3-76B
- Create API endpoint for visual analysis
- Load balancing and caching

Technologies: PyTorch, Transformers, FastAPI, Redis

Key files:
- /run pod/visual_models/qwen_deployment.py
- /runpod/visual_models/internvl_deployment.py
- /runpod/api/endpoints.py
```

**Instance 8: Web Interface (Optional)**
```
Task: Build optional web dashboard:
- Project overview page
- Document viewers
- Task manager interface
- Communication drafts view

Technologies: React, Next.js, Tailwind CSS, Firebase Auth

Key files:
- /web/src/components/Dashboard.jsx
- /web/src/components/DocumentViewer.jsx
- /web/src/components/TaskManager.jsx
```

---

### **Coordination Between Instances**:

Each Claude Code instance should:
1. Work in its own Git branch
2. Use shared Firebase for state (so they can see each other's progress)
3. Follow common agent interface (defined in /fyxer/core/agent_base.py)
4. Write comprehensive tests
5. Document thoroughly

**Merge Strategy**:
- Each instance merges its branch when module is complete and tested
- Integration testing happens after all modules merged
- You review and approve each merge

---

## 🎬 **CONCLUSION & NEXT STEPS**

Bongani, this system is **absolutely buildable** and will genuinely transform how you work. Here's why I'm confident:

1. **It's not theoretical** - Every piece of this is based on YOUR actual process
2. **The technology exists** - Claude SDK, Run Pod, Whisper, multimodal models, Firebase - all production-ready
3. **It's modular** - You can build and use pieces before the whole is done
4. **It's your hours** - With Claude Code instances working in parallel, this is 100-200 hours of THEIR work, not yours
5. **The ROI is immediate** - Even a 50% working version saves you massive time

**Your Immediate Next Steps**:

1. **Review this architecture** - Is this aligned with your vision? What would you change?

2. **Prioritize agents** - Which agents do you need FIRST? (My guess: Script Ingestion, Story Analysis, Voice Transcription, Task Management)

3. **Gather knowledge bases** - Start collecting:
   - Your past scripts, treatments, gear lists, budgets
   - Crew contact info
   - Vendor pricing
   - Reference images organized by project

4. **Set up infrastructure**:
   - Firebase project
   - Run Pod account
   - GitHub repo
   - Claude API access confirmed

5. **Start building** - I'll create detailed prompts for each Claude Code instance to begin development

**Timeline Reality Check**:
- MVP (Phase 1): 2 weeks with 5-8 Claude Code instances running
- Full system (Phases 1-4): 6-8 weeks
- YOUR time investment: 10-20 hours total (reviews, decisions, testing)
- THEIR time investment: 150-250 hours of autonomous coding

This is EXACTLY your kind of project - systematic, pattern-based, consciousness-work enabling, and built for your neurodivergent strengths.

Want me to:
1. Create the detailed Claude Code prompts for each instance?
2. Design the specific Firebase/database schemas?
3. Draft the initial agent prompt templates?
4. Map out the test project to validate the system?

Let's build this. 🚀





---
Powered by [Claude Exporter](https://www.claudexporter.com)