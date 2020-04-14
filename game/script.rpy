
##### Declare images used by this game. #####

## Character Sprites ##

image side robin an = "robin_angry.png"
image side robin fr = "robin_frown.png"
image side robin frbl = "robin_frown_blush.png"
image side robin grin = "robin_grin.png"
image side robin sm = "robin_smile.png"
image side robin smbl = "robin_smile_blush.png"
image side robin smirk = "robin_smirk.png"
image side robin surprise = "robin_surprise.png"
image side robin surprisebl = "robin_surprise_blush.png"
image side robin sus = "robin_suspicious.png"

image dylan an = "dylan_angry.png"
image side dylan an = "dylan_s_angry.png"
image dylan fr = "dylan_frown.png"
image side dylan fr = "dylan_s_frown.png"
image dylan frbl = "dylan_frown_blush.png"
image side dylan frbl = "dylan_s_frown_blush.png"
image dylan grin = "dylan_grin.png"
image side dylan grin = "dylan_s_grin.png"
image dylan sm = "dylan_smile.png"
image side dylan sm = "dylan_s_smile.png"
image dylan smirk = "dylan_smirk.png"
image side dylan smirk = "dylan_s_smirk.png"
image dylan surprise = "dylan_surprise.png"
image side dylan surprise = "dylan_s_surprise.png"
image dylan sus = "dylan_suspicious.png"
image side dylan sus = "dylan_s_suspicious.png"

image anderson an = "anderson_angry.png"
image side anderson an = "anderson_s_angry.png"
image anderson fr = "anderson_frown.png"
image side anderson fr = "anderson_s_frown.png"
image anderson sm = "anderson_smile.png"
image side anderson sm = "anderson_smile.png"
image anderson smirk = "anderson_smirk.png"
image side anderson smirk = "anderson_s_smirk.png"
image anderson surprise = "anderson_surprise.png"
image side anderson surprise = "anderson_s_surprise.png"
image anderson sus = "anderson_suspicious.png"
image side anderson sus = "anderson_s_suspicious.png"

## Background Images ##

image bg homelit = "bg_bedroom_lit.png"
image bg homeunlit = "bg_bedroom_unlit.png"
image bg conferencehall = "bg_conferencehall.png"
image bg library = "bg_library.png"
image bg streetday = "bg_street_day.png"
image bg streetnight = "bg_street_night.png"
image bg black = "bg_black.png"



##### Declare characters used by this game. #####

define r = Character("{b}Robin{/b}", image="robin", color="#FFFFFF")
define d = Character("{b}Dylan{/b}", image="dylan", color="#FFFFFF")
define a = Character("{b}Anderson{/b}", image="anderson", color="#FFFFFF")

define m = Character("{b}A Man{/b}", image="dylan", color="#FFFFFF")
define c = Character("{b}Cassidy{/b}", color="#FFFFFF")
define u = Character("{b}Unknown Man{/b}", color="#FFFFFF")
define h = Character("{b}Heather{/b}", color="#FFFFFF")



##### Initiate variables used in this game. #####

init python:
    _preferences.set_volume('music', 0.3)

init:
    $ centerpos = Position(xpos=0.40, xanchor=0)        # only used when leftpos and rightpos not in use
    $ leftpos = Position(xpos = 0.30, xanchor=0)
    $ rightpos = Position(xpos = 0.60, xanchor=0)

    $ CASSIDY_ARRESTED = False
    $ ADDICT_SAVED = True
    $ DYLAN_KISS = True
    



##### Start the game. #####

label start:


# ################################################
# REGULAR SCENE: Robin and Anderson hunt a dealer.
# ################################################


    stop music fadeout 1.0

    scene bg black with fade
    pause(0.5)

    "One: They deal hard drugs."
    "Two: They're still not behind bars."
    "That's all I need to know."

    scene bg streetnight with fade
    
    # play music "BGM_suspicious.mp3" fadein 1.0 fadeout 1.0 loop


    "The night wind whipped my hair around my face."
    "Perching on the roof with my knees to my chest, I felt the chill of the clay tiles sapping warmth from my body."
    "From this position, I could see both the back and front exits of the house next door."
    "It was a nondescript suburban house trying to blend in with its neighbors. The only thing that gave it away was the dirt path out front, worn down with the steps of dozens of customers."

    r sus "\"Tch.\""

    "None of those customers would have to get caught up in this, if Anderson would just show up on time."
    "My fingers felt like they were chilled to the bone."
    "I tapped them across my phone screen impatiently."

    r sus "<no one's approached in half an hour. where are you?>"

    "Anderson's response was immediate."

    a smirk "<almost there, get ready>"

    "I slid my legs under me, pointing my camera at the backyard fence."
    "It wasn't like I could do a whole lot alone, but if anyone tried to flee, at least I'd be able to capture the evidence under their own motion-activated lights."
    "Not long after, two police cars rolled into the street, illuminating the quiet neighborhood with their headlights."

    a fr "<back exit?>"
    r fr "<clear>"
    a fr "<ok>"

    "Four navy-clad officers approached the residence's front door. I glanced away, keeping an eye on the backyard."
    "It took my eyes a minute to readjust to the dark."
    "But there was no movement from the yard."

    r sus "\"...\""

    "Several minutes later, my phone vibrated."

    a sus "<there were two like you said>"
    a fr "<come on down, the others left>"

    "I tucked my camera into my sling bag."
    "I glanced down at the sidewalk, which was a mistake. The ground seemed to tilt. It was so far down."
    "It was impossible to step carefully down the way I'd climbed up, using individual footholds."

    r sus "(... I should be behind a computer, not out here.)"

    "With a sigh, I slowly made my way down, stepping on the recycling bins that I'd dragged by the wall earlier."

    show anderson sus at centerpos with dissolve

    a an "\"If we'd caught them with a buyer, we would've been able to charge them with heroin distribution, not just possession.\""

    r fr "\"It's fine.\""
    r an "\"It's more important to get them behind bars at all.\""
    r fr "\"They did have heroin, right?\""

    a sus "\"Yep. Like you said.\""

    r fr "\"Good. That's two years in prison, at least.\""

    show anderson an

    "Anderson's nose wrinkled. I opened my mouth before he could object."

    r sus "\"It's more important to stop them before they hurt more people.\""

    r fr "(Besides… I don't want to implicate any more addicts, either. They're just victims.)"

    a sus "*sigh*"
    a fr "\"It'd be easier to extend their sentences if you gave me more evidence to work with.\""

    r fr "\"I trust you can do it.\""

    a fr "\"What a slave driver.\""

    r sus "\"What was that?\""

    a fr "\"Nothing.\""

    "Anderson glanced back at his police car. The other one had driven off with the suspects."

    a fr "\"Let's get out of here. Talk in the car.\""

    "I nodded."


    scene bg black with fade

    "I climbed into the passenger seat."

    scene bg streetnight with fade

    r surprise "\"The other three left?\""
    a fr "\"Yup.\""
    r surprise "\"I didn't know they trusted you enough to drive the cruiser yourself.\""

    "Anderson snorted."

    a an "\"Hardly.\""
    a sus "\"They still won't let me do the arrests. I'm just the information gofer for 'em.\""

    "In profile, the passing streetlights threw shadows on his face. It made his expression look stormier than usual."
    "I wasn't sure if I'd ever seen him without a furrowed brow."
    "My coworkers often told me to smile more, but they'd never seen someone as tense as Anderson."

    r fr "\"...\""
    r fr "\"Their loss.\""
    r fr "\"Without you, they wouldn't be able to flex their power over anyone.\""

    a sus "\"It's not the same.\""

    "We sat in silence for a time, watching the road fly by."

    a fr "\"You've been going after small fry recently.\""

    "His tone was conversational, but underneath his words was a question."

    r fr "\"Yes.\"" 
    r "\"The small-time dealers are careless and easy to track down.\""

    a "\"You should start going for bigger targets.\""

    r sus "\"No.\""
    r "\"I'm going after easy prey because they're all garbage — the more of them behind bars, the better. This is more value for my time.\""

    a an "\"I thought you wanted to prevent them from making more addicts.\""
    a "\"These college hobbyists don't have the same power and reach as—\""

    r an "\"—as cartels, and I should go after crime lords again?\""

    a fr "\"Think about it.\""

    r an  "\"Even if I spent my time hunting them down, how could you guarantee they wouldn't get acquitted?\""
    r sus "\"People like that know how to slip away under the law.\""

    a an "\"Not under my...\""
    a "\"...\""
    a fr "*sigh*"
    a "\"I guess I can't really complain. The more people you can net me, the better.\""
    a "\"But I wonder if you really don't see any distinction between amateurs like this and cartels.\""

    r sus "\"...\""
    r "(And I wonder if you need those high-profile arrests to prove yourself in the force.)"
    r fr "(We're the same inside, aren't we?)"



# ################################################
# REGULAR SCENE: Robin meets Dylan at the library.
# ################################################


    scene bg library with fade
    pause(0.5)


    r sus "\"Haaa…\""

    "Hazy black spots danced across my vision."
    "I braced my hands against my desk to stop myself from falling over. Blinking the fatigue out of my eyes, I smiled at no one, trying to look friendly as library visitors passed."
    "One man who walked in started to smile back, then saw my haggard expression and quickly looked away."

    r fr "\"...\""

    "The stint last night with Anderson had ended past 1AM. As a result, I'd only been able to get five hours of sleep."
    "Which wouldn't have been so bad if five hours wasn't the best I'd managed this whole week. Caught up in the rush of researching and tracking down information about that dealer, I hadn't gotten much sleep the previous nights either."

    r sus "\"Haa…\""

    "Vigilante by night, librarian by day. None of the storybooks ever mentioned how {i}tired{/i} the heroes were."
    "I was just going to end up scaring the kids if I smiled at them like this."
    "I turned back to my computer."
    "Despite the sprawl of the four-story library and the open atrium running down the center, the library was a cozy place to be."
    "Warm lighting and bright, modern furniture helped portray the library as somewhere students and adults wanted to relax, even if they didn't borrow books anymore."
    "Because my library was near a large university, we frequently had students coming in for resources."
    "Though we had fewer research journal subscriptions than their university libraries, our recent remodel gave our library a much more spacious feeling than theirs."

    r fr "(I feel like I've seen more undergraduates coming in recently.)"

    "I rubbed my eyes and glanced around the library, then looked back down at my computer."

    r "(Oh, a new shipment of orders. I'd better go shelve those.)"


    scene bg library with fade


    m fr "\"Excuse me, d-\""
    r surprise "\"Whoa!\""

    "A loud voice behind me made me jump."
    "I fumbled the book I was placing on a high shelf, barely catching it by the front cover as it fell out of my hands."

    r "\"Oh no-\""

    "I quickly flipped through the pages."
    "Thank goodness - I hadn't damaged the pages or the spine."

    m surprise "\"Oh!\""

    show dylan surprise at centerpos with dissolve

    m fr "\"I didn't mean to startle you. Do you need help with that?\""

    "The blonde man gestured to the high shelf. He had gangly, long arms, and was taller than me — the type of guy who would always be asked to reach high shelves."

    r sm "\"Thank you, but I'm good.\""

    "Tiptoeing to reach the top shelf, I slid the book back where it belonged."

    r fr "\"Can I help you with anything?\""

    m "\"Yes, we're looking for a paper published by Dr. Chen and Lee in the Journal of Deep Learning and Neural Networks. Does this library have a subscription to that journal?\""

    r sm "\"Yes, we do.\""

    "A small woman wearing a big student's backpack peeked out from behind the man. She didn't look much younger than us, despite her diminutive size."

    r fr "\"I'll take a look at getting you access to the journal right now. Do you have a library card with us?\""

    m sm "\"No, but we'll be happy to apply for them if we need to.\""

    r sm "\"Great.\""

    "I headed back to the row of computers stationed at the help desk. The two of them followed."
    "They looked about my age - possibly college students."

    r fr "\"Do you know any students or faculty at the university nearby, by any chance?\""

    "After past mishaps and accidentally offending older patrons, I'd taken to asking this instead of if they were students of the local university themselves."

    r "\"Their libraries have a subscription to the Journal of Deep Learning and Neural Networks as well.\""

    m fr "\"We're students there, actually.\""
    m "\"I'm both student and staff — I'm her TA.\""

    "He gestured to his student trailing nervously behind him."

    m sus "\"Unfortunately, we can only access the journals when connected to university internet. Our university VPN hasn't been working recently, so more reliable access to scientific journals would be nice.\""

    r fr "\"Downloading the journals wouldn't work, I assume?\""

    m "\"Only if we know what we want beforehand.\""
    m "\"Consistent access to the online archives would be invaluable.\""

    r fr "\"Right.\""

    show dylan fr

    "I loaded up the information he needed and swiftly e-mailed it to him, trying to stifle a yawn the whole time."

    r "\"Want a paper copy, too?\""

    m sm "\"Sure, it couldn't hurt.\""

    hide m

    "I wrestled with my fatigue, hiding it behind my polite smile."
    "And so another day at the library passed peacefully."



# #################################
# EVENING SCENE: Robin is fatigued.
# #################################


    scene bg homeunlit with fade    
    pause(0.5)

    "As soon as I flicked on my apartment's light switch, I dumped my bag on the floor and beelined for my desk."
    "The apartment was tiny — just a studio. My bed was just steps away from my kitchen."
    "I could've chosen to live farther from work in exchange for a bigger apartment, but I hadn't had a car until just recently."

    r fr "(It's annoying to scout arrest locations without a car. Exposing myself by walking around isn't safe, either.)"
    r sus "(Not that it's ever really safe…)"

    scene bg homelit with dissolve 

    "I booted up my computer and turned to my kitchen."

    r fr "(If I make cup ramen instead of cooking today, I'll have four or five whole hours to finish gathering information on Cassidy.)"

    "I glanced longingly at my empty condiments rack." 
    "Just like I'd done yesterday, and the day before that, and every day for the last several weeks."
    "But of course it remained empty."
    "I'd tossed all my spicy foods and condiments away."
    "It felt like ages ago. Every day without them was a struggle to avoid thinking about food, about the next time I could eat more, the next time I could drown my thoughts by burning up my tongue—"
    "But another day with an empty spice rack meant another day not binge-eating."

    r fr "(Regular ramen it is.)"

    "I sat down in a plastic folding chair, waiting for the water to boil."
    "The night after the successful arrest, I'd begun wrapping up my plans for the next target."
    "While posing as a university student and customer, I'd baited her into agreeing to meet me for two grams of crack cocaine."

    r sus "(Cassidy's just a student who chose to deal cocaine for side income.)"

    "I shook my head."
    "No matter how pitiful the person, roping customers further into addiction - further into ruining their lives - was something I should punish."

    r "(If I just push myself a little more, I can get her locked up tomorrow or the day after tomorrow.)"

    "I glanced at my bed."
    "My sluggish muscles pleaded with me. Napping wouldn't be so bad. Just a few minutes."
    "Losing my train of thought, my mind hazed over for a moment."

    r an "(No…)"

    "I blinked rapidly, lifting one of my eyelids open with a finger. It felt weird, so I let it go."
    "I thought back to how my mother had done that before, too, right after she had overdosed. Using her fingers to keep her eyes open."
    "Trying to stay lucid long enough to say something to me."

    r sus "(... Why is my mind veering off to just my worst memories today?)"
    r fr "*sigh*"
    r sus "(I don't have time to rest.)"
    r "(I have to keep working.)"


    scene bg homelit with fade
    pause (0.5)


    r fr "\"Whew.\""

    "That should be everything I need for Friday."
    "I glanced at the time on my desktop's smaller monitor. It was half an hour before midnight."

    r "(I still have time before I should sleep.)"

    r sus "\"...\""

    "... What do I usually do when I have free time?"
    "When was the last time I read a book for fun?"
    "Who did I talk to?"

    r surprise "\"...\""

    "A feeling of emptiness settled over me."
    "I tried to shake it off. I was sure there was something I could do. Something…"

    "Right. More work. I had been meaning to take some time and follow up with Anderson after the most recent bust."
    "But during that bust, I had also been made well aware of how out-of-shape I was. It would probably do me some good to get back to exercising regularly."
    "Or I could take a nice, warm bath. It's been so long since I've taken care of my body and been able to just relax. I missed it."

# #########################
# TODO: ADD EVENING CHOICES
# #########################

    r "(I should do something nice tonight.)"





# ##########################################################
# REGULAR SCENE: Robin hunts down Cassidy at the university.
# ##########################################################


    scene bg black with fade
    pause (0.5)


    "Friday was here in a blink."
    "Today, I'd be helping Anderson arrest the cocaine dealer, a student from the local university."

    scene bg conferencehall with fade
    pause (0.5)


    "I peeked into a large lecture hall at the local university."
    "The room was empty, save for a dozen students at the front of the room. There were over a hundred chairs, but everyone was concentrated at the front of the room, listening to one man speak."
    "I couldn't make out the words from here. The PowerPoint slides at the front of the room indicated it was some sort of computer programming course."
    "It was hard to tell if Cassidy was here, from the backs of the student's heads."

    r fr "(Maybe I should go around to the front of the room to check.)"

    "But then they'd probably see my face as I peeked in."
    "I scanned the students in the room. There were only two women, and one had the short brown hair that Cassidy's photos had."
    "That was probably her. It wasn't enough to say for sure, so I decided to wait and follow her out of the room."

    r sus "(Don't want to call Anderson here only to arrest the wrong person.)"

    "I settled in to wait on a bench outside the front door, fiddling with my cell phone as if I were scrolling down social media. With the backpack I'd brought on campus, nobody looked at me twice."

    r fr "(I guess I still look like a student.)"

    "I'd only graduated two years ago. I blend right in."

    "Several minutes later, students started filing out of the lecture hall. I glanced up as they passed."
    "After a moment, I realized neither the short-haired girl nor the man who had been lecturing had walked out."

    r surprise "(Are they still inside? Or did they go out the back door?)"

    "I should have found a spot where I could've seen both exits. I frowned."
    "I opened the door to the lecture room and peeked inside."
    "Two people were standing by the podium at the front of the room, talking quietly. Apparently they hadn't left after all."
    "I went around the outside of the building and nudged open the door to the lecture hall close to them."

    m sus "\"—I'm concerned for your safety, Cassidy.\""

    "The man seemed to be struggling with his thoughts."

    m an "\"I hadn't realized these issues extended beyond your project grades, and I'm sorry for not noticing.\""

    c "\"Don't be. Honestly, I'd be fuckin' weirded out if you'd found out any other way.\""
    c "\"I'm still fuckin' weirded out, Dylan.\""
    c "\"Imagine your TA walkin' in on you shooting up coke. Nobody wants that.\""
    c "\"You probably wish you could just forget it, too. So just do that.\""

    "I frowned."
    "Shooting up coke? In my search, I'd only found that she had been dealing crack cocaine."
    "Perhaps my information had been off."
    "But it was her. I pulled out my phone to text Anderson our location."
    "Squatting down outside the building's back door, I inched closer, leaning against the wall and peeking through the door."

    d sus "\"It's more than just… 'shooting up.' Using cocaine at parties will destroy your body, but selling it could get you imprisoned to boot.\""

    c "\"You think I don't know that?\""
    c "\"It's not that easy. It's good money, and I can't afford to live near this stupid university without it.\""
    c "\"Maybe you can afford to by teachin'. I don't have that privilege. And I'm not leaving with half a degree.\""

    d surprise "\"By teaching…\""
    d "\"Have you tried?\""

    c "\"Huh?\""

    d fr "\"Tried teaching. You're a fantastic student, Cassidy — one of my best. It pays well, and any student would be lucky to have you as a tutor.\""

    c "\"Fuck no, they wouldn't. Have you seen my face?\""
    c "\"If I applied to be a teacher, any interviewer would just think I'm a stupid sorority girl. And they wouldn't even be wrong.\""

    d an "\"You're underselling yourself. You're far from stupid, and there's nothing wrong with being a sorority girl.\""
    d fr "\"How much money do you need every month?\""

    c "\"What?\""

    d "\"I don't know if tutoring will cover your expenses.\""

    c "\"Um. One thousand, give or take.\""
    c "\"Don't ya look at me like that's weird. I have to send some back home.\""

    d sus "\"No, that's fine. I'm thinking — the Engineering Honors Society on campus pays tutors $35 per hour. That's seven or eight hours of tutoring a week.\""
    d fr "\"If you want to tutor for them, I'll put in a recommendation for you.\""
    d "\"With that, you're almost guaranteed a position.\""
    d "\"... Would you want to?\""

    c "\"Um…\""
    c "\"Well, tutoring means no sketchy ass distributors to deal with.\""
    c "\"My customers won't be happy, though…\""

    d sus "\"Will you be in danger if you stop selling to them?\""

    c "\"Probably not.\""
    c "\"I make sure they don't know much about me.\""

    d an "\"Then don't act based on what they want. Act for what you want.\""

    c "\"... I guess.\""
    c "\"Tutoring sounds... safe enough.\""
    c "\"Seven or eight hours isn't that shitty… I can pick my own hours?\""

    d fr "\"Yes. Though the times when most students are on campus tend to have the most demand.\""

    c "\"I guess that's fine…\""
    c "\"I don't know. It sounds too good to be true. Like, I could get fired at any time and be fucked.\""

    d sus "\"I have a hard time picturing that. What are you planning to be fired for?\""

    "The voices were silent for several seconds. I strained to hear what they were saying. There was nothing but shuffling noises inside the room."

    c "\"Nothing. I just don't like working for other people.\""

    d fr "\"You could try being a freelance tutor. But it's harder to get pupils that way."

    c "\"Mmm…\""
    c "\"I guess I'll take you up on your offer, then.\""
    c "\"But I'll only stop dealing once I have a job offer in my hand.\""

    d fr "\"Fair enough. I'll put in a good word for you.\""

    "More rustling noises, as if someone was putting things in their bag. I realized I'd been squatting outside the room for several minutes, phone in one hand, head leaning against the wall."
    "I probably looked very suspicious."
    "Luckily, no students ever walked around the back side of this building."

    c "\"Why are you going so far to help me?\""

    d "\"Am I?\""

    "The rustling noises stopped."

    d sus "\"I'm concerned, I guess.\""
    d fr "\"I meant it when I said you were one of the best students I'd ever had. You care about your work and take initiative to do well.\""
    d sus "\"No matter what path you end up choosing — software engineer, researcher, teacher — you are going to succeed.\""
    d fr "\"It'd be a shame if you got caught by law enforcement and lost the ability to choose that future.\""

    "I hesitated, my phone still in my hand."

    c "\"I... appreciate that.\""

    "She sounded like she was on the verge of crying."

    c "\"I think I needed to hear that...\""

    r sus "\"...\""


    scene bg black with fade
    pause (0.5)

    r an "\"You're exploiting those addicts by selling to them…\""
    r fr "\"Please... please stop. There are so many other ways you can make money—\""

    u "\"Girl, they're the ones that want to buy. If I don't sell to them, they'll just find someone else.\""
    u "\"I didn't come here to be preached to. By a kid, no less.\""
    u "\"Get out.\""

    r fr "\"But—\""

    "The man pulled out a small pistol from under his coat."

    r surprise "\"...!\""
    r an "(Concealed carry is illegal!)"

    u "\"Get OUT!\""

    "He roared at me, pointing the pistol in my direction."
    "I turned and fled."


    scene bg conferencehall with fade
    pause (0.5)

    r sus "..."
    r "(When had I stopped trying to convince them?)"

    "It seemed like so long ago that I hadn't been turning over these people to the police."
    "The sound of the door opening — not three feet away from me — broke me out of my thoughts."

    scene bg streetday with fade
    show dylan fr at centerpos with dissolve

    d fr "\"I'll be heading to my office hours, then.\""
    d "\"The Engineering Honors Society should get back to you within a week or so.\""

    "I was still leaning my head pressed to the wall. I jerked back and fumbled with my phone, trying to look inconspicuous."
    "The man glanced at me."
    "I probably looked anything but inconspicuous."

    r "(Oh god. I definitely just looked like I was listening in on them.)"

    d sus "\"...\""
    c "\"Thanks, Dylan. I… really appreciate your help. And for reaching out to me.\""

    "He turned back to her, and I straightened up, cringing."

    d sm "\"Don't worry about it. I hope it works out for you.\""

    hide dylan

    "The two said their goodbyes and left in separate directions."
    "Cassidy was, no doubt, heading to the meetup spot where I said I'd buy from her."
    "I hesitated. I could follow Cassidy and help Anderson arrest her without the other guy interfering, but…"
    "I wasn't sure if it felt right anymore."

    r sus "(Look at me, being soft on a criminal.)"

    "But it was hard to shake off what I'd heard today."

# **************
# *** CHOICE ***
# **************

    menu: 
        "Help Anderson arrest her.":
            jump cassidy_arrest
        "Let her go.":
            jump cassidy_free


# ################################
# IF: HELP ANDERSON ARREST CASSIDY
# ################################

label cassidy_arrest:

    $ CASSIDY_ARRESTED = True

    "I shook my head. I couldn't be going soft on her, especially because she hadn't actually given up drug dealing yet."
    "Too many things could go wrong — she could change her mind, fail to get the job, get fired. Maybe she was lying to her teacher's assistant to begin with."
    "It didn't matter."
    "She had harmed others, brought them further into the throes of addiction. Ruining lives so carelessly… that was unforgivable. Let the law deal with her."
    "I texted Anderson the building Cassidy had just left."

    r sus "<i'll be tailing her from a distance>"

    a an "<got it, i'll be there soon.>"

    "Good. As it should be."

    jump post_cassidy


# ##################
# IF: LET CASSIDY GO
# ##################

label cassidy_free:

    $ CASSIDY_ARRESTED = False

    "I wasn't sure what got to me."
    "Was it that she had promised to stop? That she seemed willing to pursue a better path?"
    "Or… because her teacher's assistant had tried to convince her — something I'd given up on long ago?"

    r an "(This is crazy. I've spent days gathering all the information I need to arrest her.)"

    "But my hands were already moving, typing out a message to Anderson. My eyes, watching Cassidy as she moved further and further away."

    r sus "<actually, i think i messed up, anderson>"
    r "<listened to a conversation between her and some dude. i think i got the wrong person>"
    r fr "<or if she's the right person, i don't have enough evidence to get her convicted>"
    r sus "<sorry bout the hassle.>"
    r fr "<you don't need to come out today>"

    "My phone pinged a response almost immediately."

    a surprise "<a mistake from you? that's rare.>"
    a fr "<ok, that's fine. i'll find some other work today. tell me earlier next time>"

    "This was crazy. I was crazy."
    "She'd harmed others. She'd brought others further into the throes of addiction, ruining their lives."
    "I could open up my text messages again and tell Anderson to come right now."
    "But my hand slid into my pocket, leaving my phone there. I watched Cassidy's back retreat further into the distance."
    "Then I turned and headed back to my apartment."

    jump post_cassidy



# ################################################
# REGULAR SCENE: DYLAN APPROACHES ROBIN AT LIBRARY
# ################################################

label post_cassidy:

    scene bg library with fade
    pause (0.5)

    "Several days passed. Over the weekend, the library was busy as usual, with children and families pouring in to read and shelter from the rain."
    "It cheered me up to see them. It was a reminder that my work helped people like them."

    "Young Child" "\"Hey! You can't be loud in the library!\""
    "Other Young Child" "\"You're even louder!!!\""
    "Young Child" "\"No I'm not!\""

    r sus "\"...\""

    "Well, sometimes."
    "Today was a slow day. I helped someone from acquisitions before returning back to my station."
    "I liked talking to people from that department — even though I'd decided I didn't want to join them, it was nice to learn more about how the library worked as a whole."
    "It was like a well-oiled machine. The librarians I'd admired as a child, the ones who helped me find books and seemed to know everything in the world, were just the surface of the iceberg."
    "Behind them were teams negotiating to acquire books and movies. Teams deciding which scientific journals were worth subscribing to."
    "Teams transporting materials between sister libraries to avoid stock shortages. Teams trying to get us more funding."
    "All of them worked together in harmony."

    d fr "\"Hello.\""

    show dylan fr at centerpos with dissolve

    "I looked up to find a tall blonde man holding a laptop."

    r "(I feel like I've seen this guy before. Must be a regular.)"
    r sm "\"Hello. Can I help you find anything?\""

    d sus "\"No.\""
    d "\"I remember you from last week. I didn't realize you were a student as well.\""

    r surprise "\"Last week?\""

    "Oh. He was the one who asked about that research journal."

    r fr "\"Glad I could be of help.\""
    r sm "\"I guess I do look young. I'm not a student, though — I work here.\""

    d an  "\"Really? Why were you crouched behind Engineering IV, then?\""
    d sus "\"You looked quite out of place.\""

    r surprise "\"...!\""

    "And in that second, it clicked. He was the man talking to Cassidy last Friday!"
    "Shootshootshoot."
    "I did {i}not{/i} need anyone linking Robin The Librarian to Robin The Vigilante."
    "This guy needed to get out."

    r an "\"I don't know what you mean, sir.\""
    r sus "\"You have me mistaken for someone else.\""

    "He gave me a disapproving look, like I was a student that had disappointed him. That expression thoroughly irritated me."

    d sus "\"Your hair is very recognizable.\""

    r surprise "\"Uh—\""

    "Fuck. I needed to start wearing a hat."

    r fr "\"In any case, I'm not a student at the local university.\""

    d "\"...\""
    d an "\"That just makes you more suspicious, squatting behind the door.\""
    d "\"I don't know who you are—\""

    "He glanced down at my name tag, which read ROBIN in large blocky letters."

    d "\"—but if you're one of the 'clients' she mentioned, and you're stalking her, I won't hesitate to report you to the authorities.\""


    if CASSIDY_ARRESTED == True:
        d fr "\"Not that you could even reach her, but—\""
    

    r an "\"What the fuck! Do I {i}look{/i} like a crack addict to you?\""

    "I demanded, raising my voice indignantly."
    "The nerve of him! That was literally everything I worked against!"

    d sus "\"...\""
    d an "\"How did you know about the—\""

    r an "\"I heard you guys talking loudly through the door, bird brain. I am not a crack addict — don't you dare insinuate I am.\""

    d sus "\"Nobody said anything about crack.\""

    "I wracked my memory of that afternoon, trying to remember if that was true. Had she mentioned crack cocaine? I remembered being surprised she was shooting up, which implied powder cocaine instead."

    d fr "\"Are you her friend, then?\""

    "I said nothing, not wanting to dig my hole deeper."

    d sus "\"...\""
    r fr "\"...\""

    "Finally, the man shifted his laptop to the other arm and sighed."

    r fr "\"Don't worry. I don't have any business with Cassidy.\""

    "Anymore."

    d fr "\"...\""
    d sus "\"Who are you, then?\""

    r fr "\"Robin. I work here.\""

    "I held up my nametag sarcastically."

    r an "\"You?\""

    d "\"...\""
    d fr "\"Dylan. Pleased to meet you.\""

    "He didn't look all that pleased, really. He looked at me like I was a trinket his dog had found in the dirt: an expression that was curious, but wary."

    d sus "\"We'll probably see each other around. Have a good day.\""

    hide dylan

    r surprise "\"See each other around?\""

    "But he had already turned and walked away."

    r sus "\"...\""
    r "\"Don't come back.\""


# ####################################################################################
# TODO: Add more evening choices + variable measuring rest so choices change the scene
# ####################################################################################


# ################################################################
# CONDITIONAL SCENE: Day job at the library based on fatigue level
# ################################################################

    scene bg library with fade
    pause (0.5)

    "I smiled at no one again, struggling to keep fatigue from showing in my expression."
    "Hazy black spots filled my vision. I tried to blink them away, but they kept respawning in."

    r fr "\"...\""

    "What was I doing again? I was pretty sure I had to do… something… something for one of our journal subscriptions today."
    "I pressed a hand to my forehead." 
    "I hadn't been getting enough sleep again. It was really showing."
    "I raised a hand to the computer monitor in front of me, trying to trace the words my eyes had wandered away from."
    "My fingernails were long, too long — how long had it been since I'd trimed them?"
    "Come to think of it, how long had it been since I'd taken care of myself in general?"

    r fr "\"...\""

    "It was no use. I struggled through my work all day, fighting fatigue every step of the way."



# ##############################################
# REGULAR SCENE: Wary of Dylan but he seems okay
# ##############################################


    scene bg library with fade
    pause (0.5)


    "Since that day the blonde man — Dylan? — talked to me, I'd seen him around the library several times."
    "Whenever I saw him, I always ducked out of sight, moving between floors and busying myself helping others around the library."
    "Several times, he saw me and nodded in my direction, but he never approached me when I looked like I was working. Instead, he was often working on his laptop, and occasionally scribbled notes on a pad of paper."
    "Sometimes he was with others, who all worked silently together on their computers. Most of the time, he was alone."

    show dylan fr at centerpos with dissolve

    r fr "(He's here again today.)"

    "I was on my lunch break when I spotted Dylan at his usual seat on the second floor. His back was to me."
    "I resisted the urge to move closer and look at his screen."

    r fr "(Come to think of it, what does he do here all the time?)"
    r "(I guess he was Cassidy's teaching assistant. For engineering or something?)"
    r "(I thought TAs had offices to themselves.)"
    r sus "(He's not here just to stalk me, is he?)"

    "I paused."
    "But he'd been here with a student before, that first time I'd met him."
    "And even though he'd seen me several times, he hadn't bothered me when I was busy with work."
    "Most of the time, he didn't even sit close to my workplace on the second floor — he usually sat at the other end of the library, near the sunny windows."

    r sus "(Okay.)"

    "I thought begrudgingly to myself."

    r sus "(He's probably not here to stalk me.)"

    "Even though I worried so much about being outed by him, he probably didn't even remember our conversation."

    r fr "(I wonder what he's so busy with.)"

    "Walking closer to the windows, I glanced out over the city below, trying not to look conspicuous."
    "When I was several steps behind Dylan, I looked down at his screen."
    "To my surprise, it was filled with several applications, each with light text on a dark background."
    "Each window was crammed full with tiny text, and he navigated between them without using a mouse or trackpad — only quick fingers over his keyboard."
    "It reminded me of hacking scenes in movies."

    r smirk "(If only his code was bright green. That would nail the aesthetic.)"

    "I left the study area without him noticing, and went to eat my lunch."


    scene bg library with fade
    pause(0.5)

    show dylan fr at centerpos with dissolve


    d fr "\"Slow day?\""

    "I whirled around to see that Dylan had walked up to the information desk, carrying his laptop as usual."
    "I narrowed my eyes."

    r sus "\"Can I help you find anything?\""

    d fr "\"No, not really.\""


#   IF ROBIN HAS NOT BEEN TAKING CARE OF HERSELF IN THE EVENINGS:

    d sus "\"Wow, you look exhausted. Are they running you ragged here or something?\""
    r sus "\"No. And that's none of your business.\""
    "But I tried to discreetly rub my eyes and open them wider."
    d "\"... Okay.\""


    d fr "\"I figured you could use some conversation.\""

    r an "\"In that case, I'm busy.\""

    d smirk "\"Is that so?\""

    "I looked back at my computer monitor, where I'd been browsing the quantity of Oathbringer copies at every library in our system."

    r fr "\"No.\""

    "I admitted begrudgingly."

    d sm "\"Oh, good.\""

    "Dylan followed my line of sight and spotted a large image of the book cover on my screen."

    d surprise "\"Is that Oathbringer? I wasn't aware you guys had it in stock already.\""
    d "\"Wasn't it just released last weekend?\""

    "My eyes lit up. This stoic-looking man kept up with fantasy novels?"

    r grin "\"Yeah! I'm second on the waitlist now — I've been keeping an eye on which of our libraries have it.\""
    r surprise "\"I was so tempted to just buy a copy, but I'm {i}this{/i} close to being able to read it.\""
    r "\"I gotta hold out.\""

    "I leaned forward in my seat, thinking of the hundreds of pages of new lore and if maybe, maybe there would be more insight on Shallan's backstory—"

    d fr "\"Just borrow the e-book. The wait times are a lot shorter.\""

    "I'd actually considered it for once in my life. But…"

    r surprise "\"Not anymore! It's like, ten weeks for the e-book now.\""
    r sm "\"Besides, I really like holding the book in my hand when I read. A screen just can't compare to paper.\""

    d smirk "\"Ah, you're one of {i}those{/i}.\""

    "I crossed my arms and huffed, which felt weird as I was still sitting, and Dylan loomed over me across the desk."

    r an "\"Staring at my laptop for hours on end gives me headaches!\""

    d fr "\"You don't have an e-reader?\""
    d "\"I'm surprised. I thought you would, working here and all.\""

    r sus "\"No. You think I can afford one?\""

    "Dylan paused, then shrugged."

    d "\"I don't know.\""

    "An awkward silence settled in between us."
    "Dylan glanced away."
    "I shifted in my seat, wondering if it would be okay to turn back to my computer and keep scrolling."
    "If Heather saw me turn my back to a library visitor, though, I wouldn't hear the end of it…"

    d sus "\"I still don't really know what you do.\""

    r surprise "\"Huh?\""

    d "\"If you were really a librarian here, that'd be full-time work.\""
    d "\"But you were also on our university campus on a weekday afternoon, when you should be working.\""

    "My hope that he'd forgotten our conversation had not been well-founded. I shouldn't have entertained talking to him."

    d "\"Considering you were outside with your ear pressed to the wall, it was ostensibly to listen in on Cassidy, but she doesn't know anyone matching your description.\""

    "I made a low growling noise in my throat."

    r an "\"You asked her about me?\""

    d fr "\"Of course I did.\""

    "I pressed my fingers to my forehead and sighed."

    r sus "\"I already told you I don't have any business with her. And I was not pressing my ear to the wall.\""
    r "(I was a lot more covert than that! … I think.)"

    "Dylan eyed me skeptically."

    d sus "\"Then what were you doing?\""

    r sus "\"I was waiting for someone to pick me up, and happened to be leaning against the wall.\""

    d "\"By the back door? On campus, on a weekday?\""

    r an "\"I get out of work early on Fridays, idiot. I was on campus to talk to a friend.\""

    "Dylan eyed me, clearly not buying the story. I imagined he would've crossed his arms if he hadn't been holding a laptop under one arm."

    r sus "\"Besides, I don't appreciate being asked personal questions while at work. This is the library information desk, not the Robin information desk.\""
    r "\"I can see you clearly care about Cassidy, and I want to be sympathetic, but I am at {i}work{/i}.\""

    "Dylan considered that, then tilted his head."

    d sus  "\"Fine. Then tell me about library… information.\""

    "I narrowed my eyes at him."
    "He sighed, but gestured to my screen."

    d fr "\"You're looking forward to Oathbringer, right? What books did you like that were similar to Sanderson's other works?\""

    "What is this man up to? Making excuses to avoid ending the conversation?"

    r "(At least this is something I can answer easily.)"
    r fr "\"Well, the first recommendation I always give is to check out Wheel of Time, which Sanderson actually finished posthumously after the original author passed away…\""

    hide dylan

    "We talked for a while about books, trading recommendations and opinions on my favorite author's works, until another library visitor came up to the information desk."
    "When Dylan saw her approach, he left me to go back to work."

    r fr  "\"...\""
    r sus "(I wonder what that was about.)"



# #######
# EVENING
# #######

    scene bg homelit with fade
    pause(0.5)

    r sus "(Today was a long day…)"

    "I sighed. I hoped Dylan would let go of his questions."
    "I wanted to put Cassidy's situation behind me… especially because my next raid with Anderson wasn't far off."
    "For now, though, I had to continue working."


# ############################################
# REGULAR SCENE: Dylan visits the library more
# ############################################

    scene bg library with fade
    pause(0.5)

    "Another day of work, another day of children coughing on each other."

    r sus "(Flu season is hitting pretty hard this month. I wonder if we should step up the disinfectants?)"
    r "(I'll ask Heather about it later.)"

    "I busied myself helping others find what they needed and running errands for the acquisitions team."
    "I caught myself glancing around the second floor as I hurried back to my station."
    "Since that day, Dylan had occasionally approached me at work. He only talked to me when I wasn't busy, and he never stayed long."
    "He hadn't brought up Cassidy again. But I was always waiting for the question ⁠— I still felt that initial wariness as we talked about things like books, authors, and library work."

    r sus "(Come to think of it, he always asks me questions. But I haven't really asked him any myself.)"
    r fr "(I feel like I don't know anything about him. The other library regulars I talk to are much less of a mystery.)"
    r sus "\"...\""
    r fr "(Oh well. It's not like I need to get to know him.)"

    "Like clockwork, that day Dylan found me manning the station with little to do again."

    show dylan fr at centerpos with dissolve

    d fr "\"Slow day again, huh?\""

    r sus "\"Hello, Dylan.\""
    r fr "\"Only because I've taken care of all the work I need to do. Can you say the same for yourself?\""

    "He grimaced."

    d sus "\"No.\""

    r surprise "\"Oh.\""

    "That was surprisingly straightforward of him."

    r fr "\"Anything I can help you find?\""

    "He stared at me, tilting his head just a little."
    "It would've been a cute look on anyone else. On him, it looked like he was deciding if I was worth dissecting or not."

    d "\"How much do you know about the current literature in deep learning?\""

    "I remembered he'd been Cassidy's teaching assistant. Perhaps he was trying to be a better teacher?"

    r surprise "\"Like guides for teachers? Research on active learning and stuff? We have several⁠—\""

    d fr "\"Not that kind of learning. Deep learning in computer science.\""

    "He saw my blank expression and continued."

    d "\"Artificial intelligence. Neural networks. Things like that.\""

    r surprise "\"Oh.\""
    r fr "\"We have subscriptions to a bunch of research journals on artificial intelligence. A dozen or so — we can pull up more with neural networks and deep learning as keywords. I can run you a comprehensive search if you want.\""
    r "\"We also have a couple of textbooks with neural networks in the title, but they're from several years ago, and research moves fast.\""
    r "\"I can't say I'm familiar with deep learning myself, but I can find you anything you need.\""

    d sus "\"...\""
    d fr "\"Hmm… no, that's all right.\""

    "I paused halfway through turning back to my monitor."

    r sus "\"Pardon?\""

    d "\"I don't need to find anything. I'm just hoping for a fresh perspective.\""

    r fr "\"On what?\""

    "The words left my mouth before I'd thought them through."

    d sus "\"My thesis.\""

    "Well, that was something I could help with."
    "As a librarian, I was trained for this. I felt my competitive spirit rise."
    "Dylan saw my curious expression and continued talking."

    d "\"Part of my research involves building an artificial intelligence model that can use pictures to diagnose cutaneous disorders. Skin diseases, basically.\""
    d fr "\"After a couple years, we've gotten down a model that works — we just need to fine-tune it to make sure it works with images of different quality.\""
    d sus "\"But my ultimate goal was to create a system that can help doctors diagnose any physical issue. Skin issues, lung issues, heart disease, leg fractures, blood clots.\""
    d fr "\"Obviously, a system like that is too ambitious for a PhD thesis.\""
    d sus "\"I set it aside for a long time and figured I'd be able to use my thesis model to create models for other disorders, but… after working on finding just skin disorders, it turns out the framework we built can't be reused for much else.\""
    d "\"Especially because most things can't be diagnosed with images.\""

    "I nodded."

    r fr "\"Or the pictures are useless.\""
    r "\"Like for a broken bone. The AI would diagnose it as broken from the x-ray, but anyone who bothered to get an x-ray in the first place could see that with their own eyes.\""

    d sm "\"Right.\""

    "A faint smile appeared on Dylan's lips. It was the first time I'd seen him smile."
    "The expression looked nice on him — he should smile more to lighten up that dour face."

    d fr "\"Anyway, I've been thinking recently about how to make a system to help diagnose all illnesses.\"" 
    d "\"There are other models out there for other illnesses. For example, there is a lot of very successful research in cancer detection. Models that are significantly better than mine.\""
    d sus "\"But they all need different inputs. Like…\""

    "He faltered, thinking about how to phrase his sentences."

    d fr "\"A doctor might need to submit surface images for one model, CT scans for another model, and compression ultrasounds for a third. It'd be a huge hassle to run more than one at a time.\""
    d sus "\"Also, obviously, I can't steal other people's work.\""
    d "\"I can't even find some of it — some people inexplicably don't release their models with their research.\""

    d "\"Is this too complicated for you?\""

    "I bristled."
    "His expression wasn't condescending, though. It was like the well-meaning concern of a teacher."

    r sus "\"No.\""
    r surprise "\"I don't think there's any way to get around those limitations, though. I'm sure some disorders have to be diagnosed through blood tests, and others through ultrasounds.\""

    d "\"Yeah…\""

    "Inexplicably, I found myself smiling."
    "Dylan's ambitions were clear. Straightforward. Aimed at doing something good in the world."
    "It shone through from behind his grim expressions."

    r sm "\"If I were you, I would reorient my goal towards making something that patients can use on their own.\""
    r surprise "\"If a doctor has the ability to run CT scans and ultrasounds on you, they probably already know what type of issue you have. Plus, running each scan is expensive.\""

    "I'd gotten one for my lungs as a kid, when my mother was terrified that I had pneumonia. It cost five thousand dollars."

    r fr "\"In terms of usefulness, it'd be much better to make something that patients can use themselves.\""
    r sus "\"Something for people to use when they can't afford a doctor, or all the doctors don't open until the next morning.\""

    "I thought about my mother, who would often think she was dying during withdrawal."
    "She'd often scream that she could hear her heartbeats, that her head hurt, that she wanted to throw up."
    "Always in agony. Never knowing which of them indicated she really needed to be hospitalized immediately."

    r fr "\"For example, a model where you can check the symptoms you have. Then it tells you what you're probably suffering from.\""

    d sus "\"How is that different from Googling your symptoms?\""
    d smirk "\"Headache and cough — could be the flu, could be cancer.\""

    "I snorted."

    show dylan fr 

    r surprise "\"You could enter your family's medical history and your past medical issues. Make the model take that into account.\""
    r "\"You could make the symptoms much more detailed.\""
    r "\"Let people upload pictures, or say the pain is happening where they fractured their wrist last year.\""
    r fr "\"Whatever.\""
    r "\"It doesn't have to be a symptoms checklist. But I think something that patients can use themselves without requiring expensive scans from doctors—\""
    r sm "\"That would help a lot more people than an all-encompassing system that requires doctors to upload CT scans, blood tests, and ultrasounds just to use all the systems.\""

    "Dylan considered it. He tapped his finger to his chin."

    d "\"Well, it'd be a lot easier to make. And it probably would help patients…\""
    d sus "\"It just seems so mundane. A simple tree model would be enough to build a symptoms checklist.\""
    d fr "\"I also wonder if there are legal issues with telling people your model can diagnose their issues without a certified doctor.\""

    r fr "\"Probably.\""
    r surprise "\"Don't take what I said seriously. I'm not gonna be held responsible if your model kills someone.\""
    r sm "\"Just giving you that fresh perspective you asked for.\""

    d smirk "\"Thanks. I won't take your advice.\""

    "I raised an eyebrow at him."

    d sm "\"But you're right that the goal is more important than how to get there.\""
    d "\"No point in building a model that requires ten different types of scans to diagnose anything.\""

    r surprise "\"Well… glad to be of help?\""

    "It felt wrong to be thanked by this guy. I felt my face growing warm."
    "Shifting in my seat, I glanced around the room."

    r "\"Is that what brings you to the library so often?\""
    r fr "\" Your thesis, I mean.\""

    "Dylan raised an eyebrow at me."

    d surprise "\"'So often'? I only come a few times a week.\""

    r surprise "\"That's more often than most people!\""

    show dylan fr 

    r fr "\"We don't get a lot of regulars from the university, either. I think most people prefer to use their on-campus libraries.\""

    "Dylan shrugged, shifting from one foot to the other."

    d sus "\"It can be distracting to run into my students when I'm trying to work.\""

    r "\"Oh.\""
    r surprise "\"Your students. You're a TA?\""

    d "\"Yes, I am. I thought you overheard my conversation with Cassidy — that should've made it clear.\""

    "I flushed. There it was, the elephant in the room."

    r sus "\"Just let me be the normal library employee pretending to get to know one of our valued library regulars, okay?\""

    "I raised my voice into a fake, extra-polite pitch."

    r grin "\"Hi, I'm Robin. It's nice to meet you. What subject do you teach, Dylan?\""

    "Dylan grimaced."

    d "\"Don't do that.\""

    r sm "\"Heh.\""

    "He ignored my smile."

    d fr "\"This quarter, I'm teaching Advanced Computer Networks.\""

    r surprise "\"Uh…\""
    r "\"Well, I can't say I know much about computer science, but that doesn't sound anything like your research.\""

    d sus "\"It's really not. The school just assigns us to a course they need TAs for.\""
    d "\"One of my friends had to teach a course in the chemistry department — she's a materials engineer.\""

    r "\"Wow. I thought this was a top university?\""

    d smirk "\"It is. That doesn't mean the quality of lecture is good.\""

    "I chuckled."

    r smirk "\"Are you talking about yourself?\""

    d an "\"No!\""

    "He paused, then took a deep breath."
    "A second passed, then another."

    d "\"No, I'm not. I'd like to think I'm… helpful.\""

    "I wanted to jab back the way I usually did, but something in his voice stopped me."
    "I opened my mouth, then closed it."

    r surprise "(Is he… insecure?)"

    "Dylan eyed me warily. Then he said something I'd never have expected to hear from him."

    d sus "\"What, you want to find out?\""

    r "\"Uh…\""

    r fr "(No, not really?)"


    if CASSIDY_ARRESTED == True:
        "But there had to be something to him asking about it. Did he want to get me in a room with Cassidy's classmates?"
        r sus "(Come to think of it, if he thinks I've been listening to Cassidy's conversations, he might think his other students are implicated, too.)"


    if CASSIDY_ARRESTED == False:
        "But there had to be something to him asking about it. Did he want to get me in a room with Cassidy?"
        "That seemed strange."
        r sus "(I really don't have any more business with her, but if I were him, I'd be a lot more suspicious of myself.)"
        r "(Doesn't he think I'm stalking her or something?)"


    r "(Though, given how much he seemed to care for his student, I'd expect him to be a lot more hostile to me if so…)"
    r "(What is he thinking?)"

    r surprise "\"What, are you inviting me to watch you teach?\""

    d an "\"No!\""
    d surprise "\"But you know when my discussions are. If you showed up, I … wouldn't kick you out.\""

    r surprise "\"...\""
    r sus "(Is this guy a tsundere?)"

    "Maybe he just wanted someone to reassure him that he was a good teacher."
    "In that case, I wasn't going to be the one to quell his insecurities for him."

    r "\"I'm busy this Friday.\""

    "Which was not a lie — Anderson was busting a major heroin ring that afternoon."

    d sus "\"Suit yourself.\""

    hide dylan

    "The conversation didn't last much longer than that. Dylan bid me farewell and left."
    "I swiveled back to my computer monitor, thinking back on our conversation."
    "Did he really ask me to watch him lecture because of his own insecurities?"

    r sus "(What a silly concern for him to have.)"

    "I'd seen him reach out to his student when he was concerned about her. That alone made him a better teacher than most."

    r "(If all teachers genuinely cared, how many more people would have grown up not to ruin their lives with addiction?)"

    "There was no way he was a bad teacher. It was dumb to even entertain the thought."



# #################
# EVENING: Pre-raid
# #################

    scene bg homeunlit with fade
    pause(0.5)

    "The evenings after that, I spent working on preparations for Anderson's heroin ring hunt."
    "It was back to serious mode. There was no time to spare."

    scene bg homelit with dissolve

    "I spent my evenings digging up information any way that I could — research, interviews, and social engineering."
    "This heroin ring was, unbeknownst to their clients, spiking their heroin with the lethal fentanyl."
    "Figures. The stronger they could claim their product was, the more fame they could gain in their early years."
    "I sipped my tea with two hands, warming my fingers around the mug."
    "While pretending to be a well-liked client, I'd found out that the heroin ring was also implicated with another major Silk Road group."
    "A former member of that group had recently made the news for getting caught hiring assassinations on the dark web."

    r sus "\"...\""
    r "(I almost wish I hadn't found out about this.)"
    r "(Why do all these shady groups have to be so buddy-buddy with each other? Making more work for me.)"

    "I tried to blink the fatigue out of my eyes, then glanced at the clock. The hour hand was rapidly approaching midnight."

    r fr "(Guess I'll make cup noodles again.)"



# ##############################
# REGULAR SCENE: Raid goes wrong
# ##############################

    scene bg streetday with fade
    pause(0.5)

    show anderson sus at centerpos with dissolve 

    a sus "\"All right. Here we go.\""

    "It was Friday afternoon, and I was in Anderson's backseat as we drove to the site where he'd capture two of this heroin ring's ringleaders."
    "This was going to be a higher-profile capture than his usual runs. Though this group wasn't huge, it had connections with several larger groups, and needed to be stopped."
    "Anderson looked incredibly nervous. It always showed on his face, to his anguish."

    r sus "\"Good luck.\""
    r surprise "\"You still want me to sit in the back? I'm pretty sure investigations don't look kindly on civilians getting caught up in this mess.\""

    "I saw Anderson grimace in the rearview mirror."

    a "\"I wouldn't want you here either, but the boss thinks you might be able to confirm their faces once we bring them in.\""

    r fr "\"Wouldn't I just wait at the police station?\""

    a an "\"That's what I said, but he couldn't find an aboveboard way of assigning you any security detail.\""

    r "\"Oh.\""

    "Right. Only Anderson and his boss knew about how I was the source of information behind most of Anderson's drug dealer arrests."
    "His boss apparently thought I was a critical witness, someone too important to be left without security detail. But there wasn't any way for him to explain why I should have any."

    r sus "\"I don't think I'm in danger. Nobody knows my face.\""

    "Though, remembering Dylan's words from several weeks ago, I'd covered my head this time."

    a "\"Yeah, I thought so too. But I guess I'll have to babysit you. Sorry 'bout that.\""

    "Anderson's voice was bitter, too."
    "He hated being treated like he wasn't important in these arrests. Even his boss often only used him for information from me, and from his other connections."
    "Among his peers who'd entered the police force at the same time, he was often treated as backup."

    r fr "\"... Don't worry about it.\""

    "He had his own issues."
    "Now wasn't the time to get upset about anything."
    "I looked out the backseat window. We were cruising at a slow pace, slowing down behind a side alley in the city."

    r "\"Are you going to leave the car here?\""

    a fr "\"Yeah.\""

    "We crawled to a stop."

    a "\"Gonna lock the car. In the case of an emergency, backup keys are in the glove box.\""

    "I nodded. We'd been through this before. His boss had cleared me to drive his car today only, in case he was unconscious."
    "It seemed overkill to me. Anderson wasn't going to be unconscious. But then again, it was better for me to know."

    r sus "(I'm not used to what happens in the field… I'm better off behind a computer.)"

    "I remembered the last time I'd been in the field. I'd had to climb up, and then down from a roof. I shuddered."
    "At least this time I'd be chilling in the car."

    r sm "\"Good luck.\""

    a sm "\"Thanks. Be back in thirty.\""


    hide anderson 

    "Anderson locked the car and left."
    "I glanced around. This empty area didn't look ghetto, per se, but these back streets were definitely not somewhere I'd want to be at night."
    "It wasn't dark yet, but I crawled down into the footrest, just in case."
    "I felt a little silly ducking away from view of the darkly tinted windows, but I didn't want my face to suffer collateral damage if someone tried to smash the window in."

    r surprise "(Guess I'll browse the internet.)"

    "I checked my place in the library waitlist for Oathbringer. Still first. Had been for a week."

    r sm "(Bless the souls of everyone who returns the book before their whole 21-day lending period is up.)"
    r sus "(Please, let one more person do that! One is all I need!)"

    "Fifteen minutes passed."
    "Then thirty."
    "I frowned and checked the time on my phone again. It was approaching thirty-five minutes with no response from Anderson."

    r "(We didn't talk about what to do if he didn't come back.)"

    "I was pretty sure I wasn't supposed to call him. What if his phone vibrated in the middle of him sneaking around?"

    r fr "(How long should I wait, though?)"
    r sus "(If no one knows I'm here, I can't just call the police to come and get this car.)"

    "I wished I'd gotten the contact information of Anderson's boss."

    r "\"...\""
    r fr "(I wonder if it's safe to look outside.)"
    r "(It's probably fine… I haven't heard anyone around this whole time.)"

    "I edged forward in the footrest, then wrapped my hands around the passenger seat's headrest and hauled myself up."
    "The area was still mostly empty. Just a side alley, barely wide enough for one car lane."
    "To my right was a series of tall buildings. To my left, a tiny sidewalk, then a chain-link fence."
    "A man in a button-down shirt was hurrying along the left side, shaking as he walked. His tousled hair looked like it had been neatly gelled back in the morning, but now flopped into his face."
    "I flinched. I was pretty sure there hadn't been anyone here earlier."
    "The man ignored the police car as if it were empty. Instead, he quickly unbuttoned his shirt and reached into it with one hand."
    "I watched, confused, as he took off one sleeve."

    r sus "(Is that… a syringe?)"

    r surprise "\"No!\""

    "He'd just come from the direction of the building Anderson had gone into!"

    r sus "(Our data said they spiked their heroin with lethal doses of fentanyl.)"
    r "(What are the chances—)"

    "I fumbled for my phone and punched in the number for an ambulance."
    "As I brought the phone to my ear, I glanced back towards that building frantically."

    r an "(Please, let Anderson be coming back soon…)"

    "Instead, I saw a middle-aged man enter the alley from the direction Anderson had gone."
    "He looked at my police car and broke into a run in the other direction."

    r surprise "(Wait, is that…)" 

    "Startled, I watched as his thin ponytail flapped in the wind."
    "His unzipped jacket flew behind him, up until he slipped into the driver's seat of a silver car and raced out of the alley."

    r "(No way.)"

    "That man looked just like Theodore, one of the two major ringleaders Anderson had set out to arrest today."
    "Down to the hair and jacket."

    r an "(I thought that car blocking the alley was undercover for the police!)"

    "Hatred bubbled up inside me. That man needed to be behind bars."
    "I pulled my phone away from my ear, ready to call Anderson. But I glanced back at the man in the alley, who had collapsed on the sidewalk."
    "His hand was still in his sleeve — as if he'd fallen before he could even pull the needle out."

    r "(There's no time...!)"

    
    menu: 

        "Try to capture the ringleader.":
            jump raid_capture

        "Try to get the man emergency treatment.":
            jump raid_protect



# IF: Chose to pursue criminal during raid

label raid_capture:

    $ ADDICT_SAVED = False

    "I glanced one more time back at the building. Anderson was still nowhere in sight."
    "Someone in a police uniform finally stepped out on a balcony, but it would take them entire minutes to get downstairs and in a car."
    "I had to stop Theodore."
    "I threw my phone to the front and flung myself into the driver's seat."
    "Fumbling with the glove box on the passenger side, I found the keys Anderson had left for me and started the ignition."

    r sus "(Sorry, stranger.)"
    r an "(I need to help you, but… if Theodore goes free, more people are going to suffer like you did.)"
    r "(I have to at least try to prevent those deaths!)"

    "I raced down the alley and turned the same way Theodore's car had gone."
    "I glanced down at my phone as I swerved between cars."
    "Canceling my call for an ambulance, I punched in Anderson's number. He picked up almost immediately."

    r an "\"I have your car and I'm tailing Theodore!\""

    "I paused. Chaotic background noise filtered through the phone."
    "For a moment, I panicked. What if that man hadn't been Theodore and I'd just stolen Anderson's police vehicle?"
    "But his voice came on a second later."

    a sus "\"We need to talk about you taking the car later—\""

    r "\"Later!\""

    "The silver car swerved abruptly into a right turn lane just before an intersection."
    "With one hand, I jerked the wheel right. I barely managed to follow without crashing into the streetlight."

    r sus "\"I need help! Theodore did escape, right? Where are the other police vehicles?\""

    a surprise "\"He wasn't in the building.\""
    a an "\"I'm getting into my coworker's car right now. Don't move.\""

    r an "\"If I don't move, I'm going to lose his car! Is anyone else on his tail?\""

    "There were some yelling noises on Anderson's end. I heard him pleading with a female voice, and then slamming some car doors."

    a "\"We're on our way.\""
    a "\"Press the yellow square button on the dashboard. It'll give us your location.\""

    "I punched it with the hand holding my phone. The button lit up."

    r an "\"Done! What next?\""

    "More arguing noises. I heard the words 'civilian' and 'authorized.'"

    a "\"Press the big black button on the top. It—\""

    "I punched it. Loud siren noises immediately shook the car, and I nearly jumped out of my seat."

    a "\"—will turn on the siren.\""
    a sus "\"You can ignore traffic lights while it's on. Don't hit anyone! Just follow Theodore's car.\""
    a "\"We'll find you and set up a police barricade!\""

    r sus "\"But how long am I going to have to—\""

    "I looked down at my phone. Anderson had hung up."
    "I cursed, then threw my phone into the passenger seat and put both hands on the wheel."
    "Fear raced through my body. My heart pounded as I stepped on the gas."

    r an "(I'm not authorized to drive this thing!)"
    r "(What if he has allies and someone starts shooting at my car?)"

    "I sucked in a short breath."

    r sus "(Don't think. Just follow.)"
    r "(He needs to be behind bars. He needs to be behind bars…)"
    r an "(All I have to do is follow long enough until reinforcements come.)"

    "I narrowed my vision to only the silver car in front of me and vehicles in my way."
    "Conveniently, most cars pulled to the side of the road as I approached."
    "However, others inexplicably slowed down when they heard my siren."

    r "\"I'm not here to give you speed tickets, idiots!\""

    "Radio" "\"BZZT.\""

    "A static noise came from the car's radio."

    a surprise "\"Hello? Can you hear me?\""
    a an "\"Press the green button if you can hear me.\""

    "The silver car was making a turn again. I tightened my hands on the wheel and followed it."
    "Then I reached over and hit the green button on the dashboard."

    r sus "\"Still on his tail. What next?\""

    a sus "\"Great. What's the license plate?\""

    "I rattled off the letters as I stared forward at the car."

    a "\"Okay. Silver car?\""

    r surprise "\"Yes! Ford logo.\""

    a an "\"Great. I see your location. We've barricaded the roads ahead.\""
    a smirk "\"Keep following him. You're doing incredible!\""

    "I gritted my teeth."
    "It had to have been ten minutes already. I kept my eyes on the road, and on Theodore's car."
    "One foot was perpetually hovering the gas pedal."

    r surprise "\"Oh wait! Can you hear me?\""

    a surprise "\"Yeah, what's up?\""

    r sus "\"There was some guy in the alley who shot up and collapsed. Near where you parked this car.\""
    r "\"Probably one of Theodore's victims, overdosed on the fentanyl.\""
    r "\"Call an ambulance for him.\""

    a an "\"Got it. Calling one right now.\""

    "The radio was quiet from then on."
    "The silver car eventually slowed. I spotted a barricade in front of us, with police cars lined up horizontally against the road."
    "I squinted. There were tire spikes on the ground."
    "Theodore must've seen them too. He swerved into a side lane, and I followed by jerking the wheel."
    "But that one was blocked off, too."
    "His car turned 180 degrees, as if he were going to ram his car into mine."

    r surprise "(What the...)"

    "Ice shot through my veins."

    r an "(I'm going to die here, aren't I—)"

    "Instead, he moved around me, trying to get back out."
    "I was a second too slow to react. His car got around me."
    "I screamed."

    "But another police car was already there, blocking his exit."

    r surprise "\"What…\""

    "I slowed to a stop."
    "Police vehicles surrounded his car in no time. In fifteen seconds, I blended in as just one of a mass of police cars."
    "I sat, numb, as policemen and policewomen approached and arrested Theodore."
    "There had only been one person in the car. Just him."
    "I breathed a sigh of relief."

    r sm "\"Guess I'm not dying today…\""

    a smirk "\"Good.\""

    "I jumped. Anderson was still on the radio."

    r surprise "\"What the— where are you?\""

    a an "\"In another police car.\""
    a "\"They're securing Theodore and bringing him to the station. I'll come back to my car once his car leaves.\""

    "Right. This was the vehicle Anderson had been assigned to, and I'd stolen it for this chase."
    "They wouldn't have caught Theodore without me, but…"
    "I was probably in for a world of trouble."
    "Oddly, I didn't feel scared. I breathed out deeply."

    r sus "(The guy in the alley… Did the ambulance reach him in time?)"

    "Theodore was caught. But one of his victims might not have made it."

    r "(I should've told Anderson to call the ambulance first thing.)"


    scene bg black with fade
    pause(0.5)

    "I squeezed my eyes shut. Still no word from the ambulance Anderson had called."
    "I knew I did the right thing. Theodore needed to be stopped."
    "But… if the stranger died, it would be my fault."
    "I left him to die to chase my own idea of justice."

    r an "(If I had stayed to help him, Theodore might not have been caught…)"
    r sus "(...)"

    "I could tell myself that I was preventing future deaths instead of saving one person now."
    "I could tell myself that I couldn't do anything for that stranger, anyway."
    "I could tell myself that an ambulance would come in time to help him."
    "But at the end of the day, it was me who hung up on emergency medical services."
    "It was me who left that stranger to die alone in an alley."
    "On a cold tile floor... just like her."

    r an "\"No…\""

    jump post_raid


# IF: Chose to save addict during the raid

label raid_protect:

    $ ADDICT_SAVED = True

    "I remembered the day my mother overdosed. The way she'd been collapsed on our kitchen floor, dead in minutes."
    "This man was not going to survive without emergency care. And someone had to tell the ambulance what he'd collapsed from."
    "I hauled myself into the car's passenger seat and rifled through the front drawers until I found an emergency medical pouch."

    "Emergency Services" "\"Hello?\""

    r an "\"Hi! Yes!\""
    r sus "\"I just saw a man collapse on the street. I saw him holding a syringe. I think he overdosed on heroin with fentanyl.\""
    r "\"Also, I'm with the police. Please get this man emergency care.\""

    "I tacked on that bit at the end, hoping they would take me more seriously."

    "Emergency Services" "\"Can you tell me your location and any identifying markers nearby?\""

    "I rattled off the information after finding my location on Maps."
    "My other hand was digging through the medical pouch. In it, I found a small can of Narcan nasal spray."

    r sus "(I don't know why the hell this is in a police car, but bless you, whoever put it here.)"

    "Emergency Services" "\"We'll be right there in four to six minutes.\""

    "I glanced at the man outside. He was still collapsed on the ground, arm under his unbuttoned shirt."
    "I could've sworn his lips were turning blue. Another sign of fentanyl overdose."

    r an "(He's only going to get worse in that four to six minutes…!)"

    r sus "\"Hey, I'm 99% certain what he overdosed on was heroin spiked with fentanyl. His lips are turning blue, too.\""
    r "\"This police car carries Narcan. Should I administer it?\""

    "Emergency Services" "\"Yes, but only if you can approach the patient safely.\""
    "Emergency Services" "\"Administer one dose at most, no more.\""

    r an "\"Got it. Thanks. Please hurry!\""

    "The call ended."
    "I glanced down the alley again. The silver car had long since left."

    r sus "\"...\""

    "No. It wasn't within my power to chase him down. The police would catch him."
    "And I couldn't leave this man to die… just to chase my idea of justice."

    r "(Right. Time to get out of the car.)"

    "I watched the collapsed stranger warily, but he hadn't moved since I'd seen him fall."
    "I opened the car door and cautiously creeped forward."

    r fr "(He's still not moving… Guess it's okay.)"

    "Crouching down, I hoisted the Narcan under his nose and sprayed."
    "The man didn't even flinch; a true sign of unconsciousness. The wet nasal spray couldn't have felt good."
    "Instead, he kept breathing steadily."
    "I moved back to stand by the police car, just in case, but nothing happened."
    "Out of the corner of my eye, I saw people in police uniforms emerge from the building."

    r "\"Hey!\""

    show anderson fr at centerpos with dissolve

    "Anderson jogged back to me. He looked down at the standard issue medical pouch in my hand and opened his mouth."

    r sus "\"Overdose. Ambulance told me to administer Narcan.\""
    r "\"I saw a silver car leave the alley down there. Have the police caught him yet?\""

    a an "\"No! He got out before we noticed.\""

    "Guilt crashed over me."

    r surprise "\"You didn't know…?\""

    a sus "\"We found out, but too late. Another division is trying to catch him now.\""
    a "\"It's not looking good.\""

    "I should've called Anderson first thing…!"
    "Or should I have? I wavered."
    "If I'd cancelled my call to the ambulance, this guy might not have survived long enough."

    r sus "(There would be no point in letting this guy die {i}and{/i} not going after Theodore.)"
    r "(At the very least, I have to see this through to the end. Make sure this man is okay.)"

    hide anderson

    "Anderson waited to take me back to the station. They'd caught the other guy, at least. He still needed me to witness his face."
    "The ambulance came shortly. I felt numb as I gave them the details of what I'd administered, and how long it had been since the man had fallen."
    "The emergency personnel were quick, professional, and thorough. In two minutes, they were gone with the man."

    "Emergency Services" "Don't worry, Ma'am. He has a very high chance of recovery. Thank you for administering the Narcan — that helped his body hang in there."

    "I nodded."
    "They left."


    scene bg black with fade
    pause(0.5)

    "Only after Anderson drove me to the station did the reality of today sink in."

    r sus "(I chose to help one man instead of trying to save countless more.)"
    r "(There has to have been something I could've done… something to get Theodore behind bars and away from the people he was harming.)"

    "I could tell myself I hadn't chased Theodore because I didn't know how to drive a police car."
    "That I wasn't authorized to drive a police car, and would've gotten myself in trouble with the police department."
    "That it wasn't my job to chase down active criminals when the police were on the job."
    "That I thought the police already knew how to corner him."
    "But all of those things were lies."
    "At the end of the day, I'd valued this stranger's life over preventing future deaths."

    r "(...)"
    r an "(Why…? Why did I try to save this one person?)"
    r sus "(What I've done today…)"
    r "(... goes against everything I've worked for in years.)"

    r "\"No…\""

    jump post_raid



# ######################################
# REGULAR SCENE: Depressed library hours
# ######################################

label post_raid:

    scene bg library with fade
    pause(0.5)

    "It's Saturday."
    "Why was it Saturday?"
    "Why did I have to get out of bed on a Saturday?"
    "I wanted to fall asleep and never wake up."

    h "\"Robin?\""

    "Like I deserved to."

    h "\"ROBIN!\""

    r sus "\"What?\""

    h "\"I've been calling you forever!\""

    "My boss narrowed her eyes at me."

    h "\"Acquisitions got back to me on the missing children's series you asked for last week.\""
    h "\"We'll be getting one copy of each that you requested, plus a few more that you should review. I want you to get back to me on whether we have space on our shelves for all of them, and which ones to cut if not.\""

    r fr "\"Oh.\""
    r "\"Okay.\""
    r "\"No cutting. I'll make space for them elsewhere.\""

    h "\"How?\""

    "I shrugged."

    r "I'll figure it out."

    "Heather studied me. She looked concerned, but I knew her concern was primarily for the library, not for me."

    h "\"Take your lunch break soon, will you? You look like you've been run ragged.\""

    "For once, she was wrong."

    r "\"Okay.\""

    "As if lunch mattered."
    "Still, if she ordered it, then I'd eat."


    scene bg library with fade
    pause(0.5)

    "Anderson texted me after lunch. I glanced down at my phone, a spark of interest compelling me to pick it up."


    if ADDICT_SAVED == False:
        a sm "<both the culprits are being interrogated now. you did a really good job yesterday.>"
        a "<i hate to say it, but without you we probably wouldn't have gotten T. good work>"
        a fr "<by the way, the ambulance i called for the guy in the alley just got back to us. they were too late to help him, but the police department is helping his family with the funeral costs.>"
        a surprise "<pretty rare of em lol>"
        a sm "<don't beat yourself up about it, you stopped tons of people from suffering like him>"
        a "<again, good work. let me know when you're up for the next target>"

        "I stared at my phone for several minutes before dropping it back into my purse."

        r sus "\"...\""
        r "('Let me know when you're up for the next target'?)"
        r an "(He {i}died{/i}.)"
        r sus "(I didn't know he had a family.)"


    if ADDICT_SAVED == True:
        a sm "<the ambulance that picked that guy up just got back to us about him, they say he's gonna make it>"
        a smirk "<he was really mad that his high got interrupted with narcan though lol>"
        a sm "<anyway, just wanted to let you know that you did good helping him out>"
        a an "<also, the one that got away is still being chased down. don't think we're gonna get him tbh>"
        a "<really hope we do…>"

        "I stared at my phone for several minutes before dropping it back into my purse."

        r sus "\"...\""
        r an "(Theodore got away.)"
        r sus "(And for what? All so I could administer Narcan to some stranger who'd hate me for it?)"

        "I knew that wasn't a fair way to look at it. He hadn't even been conscious. There was no high to interrupt, and it'd be worth saving a life any time."
        "But I could've done something. I made the choice to let Theodore drive away."
        "Against all of my principles."

        r "\"...\""



    "Several hours later, Dylan spotted me across the floor."

    show dylan fr at centerpos with dissolve

    r sus "(Here we go.)"

    "As I expected, he approached the desk I was sitting at."

    d fr "\"You look dour today.\""

    r an "\"Shut it.\""
    r sus "\"I'm not in the mood for small talk, Dylan.\""

    d surprise "\"Uh ⁠— what happened to you? You look worse for wear than usual, and that's saying something.\""
    d sus "\"Did something happen?\""

    r fr "\"It's none of your business.\""

    d "\"Are you sure? You don't look well… If there's anything you need⁠—\""

    r an "\"I said. I was not. In the mood. For small talk.\""

    "I snapped at him, my voice filled with hatred."
    "It wasn't hatred at Dylan. Not really. Not like I would've expected weeks ago."
    "It was hatred at myself. The weight of yesterday on my shoulders."

    r sus "\"...\""
    d sus "\"...\""

    r fr "(... That's not an excuse to lash out at this random guy.)"

    r "\"Sorry.\""
    r "\"I'm going through a rough time.\""
    r "\"Not a fair reason to yell at you.\""

    d fr "\"It's okay.\""
    d "\"I appreciate the apology.\""

    r "(...)"
    r "(And I appreciate that you don't claim to understand.)"

    "I couldn't muster up the effort to say it out loud."

    d "\"Should I leave, then?\""

    r surprise "\"No.\""

    "The answer came without thinking."
    "I didn't want him to leave."
    "His presence was… grounding."
    "It made me feel like there was more to think about than yesterday."

    d "\"...\""
    d sus "\"Are you the kind of person who likes distractions?\""

    r fr "\"Um… maybe?\""
    r "\"I'm not sure.\""

    "Dylan left, then came back pulling a chair over to my table."
    "Just that simple act — someone actually wanting to sit with me — made me want to cry."
    "Dylan started talking, unaware of my thoughts."

    d surprise "\"I tried out the symptoms checklist model you suggested last time. It was annoying finding all the medical data I needed in the right format.\""
    d fr "\"I found out psychologists and therapists use a similar program.\""
    d sm "\"Which makes sense, in retrospect. I always wondered what they did with those pre-appointment surveys, where I checked off all my feelings and answered questions on those 1-5 scales.\""

    "He said that so casually, with a smile on his lips."

    r sus "(I wonder what kind of people he surrounds himself with, that seeing a therapist is such a normal thing.)"
    r "(I think my mother would have screamed.)"

    d fr "\"I don't know if the model works. It's hard to test it on my own.\""
    d "\"I also haven't added anything interesting to it, like the family history idea. I'm guessing I'd just weigh certain responses as more likely, but I haven't tried it yet.\""

    r fr "\"I'm surprised you put so much effort into it. It was just a passing thought.\""

    "Dylan shrugged."

    d "\"It sounded interesting, and I had some free time.\""

    r "\"I see.\""

    "Silence."
    "I felt like I should say something, since he was going to the effort of conversing with me."

    r "\"Been up to anything else interesting recently?\""

    d sm "\"Hmm… Yeah.\""
    d "\"I'm presenting my thesis at a research conference tomorrow.\""

    r surprise "\"...\""
    r "\"Wait, that's pretty important.\""
    r "\"Is it a speech?\""

    d fr "\"No.\""
    d sm "\"It's at a banquet hall where everyone can set up their research posters and people walk around.\""
    d "\"There are keynote speakers, but those are usually famous researchers.\""

    r sm "\"Still, that's pretty amazing.\""

    d "\"Want to come?\""

    r fr "\"Um…\""

    "To be honest, no. I didn't want to muster the energy to go anywhere. But the word research ignited a tiny flame in me — a small curiosity."
    "Maybe it would be good to take my mind off things."

    r surprise "\"Maybe.\""
    r fr "\"Where is it?\""

    d fr "\"It's in one of the halls of the city conference center. I'll forward you the information if you want it.\""

    r surprise "\"Sure.\""

    "Dylan handed me his phone, and I typed in my phone number before handing it back."
    "A second later, my phone vibrated."

    d sm "\"There. Just sent the text.\""

    r fr "\"If I go, how will I find you?\""

    "Dylan thought about it for a moment, then shrugged."

    d smirk "\"I don't know. Take some time to browse everyone's work, I guess.\""

    "I eyed him suspiciously and crossed my arms."

    r sus "\"Well, if you don't see me tomorrow, you'll know why.\""

    "Dylan chuckled."

    d sm "\"Hey, your loss.\""

    hide dylan

    "He didn't stay much longer before bidding me farewell, wanting to rest for his conference tomorrow."

    r "(Hmm… Maybe I'll go check it out tomorrow afternoon.)"

    "Having something to look forward to was a strange feeling."
    "It didn't take the weight off my shoulders, but I didn't dislike it."



# #############################
# EVENING: Post-raid depression
# #############################

    scene bg homeunlit with fade
    pause(0.5)

    r fr "(Oh… looks like I can pick up my copy of Oathbringer now.)"

    r sus "\"...\""

    r fr "(Too much work…)"

    "I tossed my phone onto my bed and flopped on top of it."
    "As I stared up at my ceiling, I felt as blank as the white paint looked."

    r "(I was so excited to read just yesterday.)"
    r sus "(I checked my waitlist position while in the backseat of a police car.)"
    r fr "\"...\""
    r "(Come back, my excitement for Oathbringer.)"



# #################################
# REGULAR SCENE: Dylan's conference
# #################################

    scene bg homeunlit with fade
    pause(0.5)

    "I rolled over in my bed, pulling the blankets over my head to block out the sunlight streaming in my window."

    r sus "\"Mnrngngngn…\""

    "Sunlight streaming in? That meant it was still morning."
    "I curled deeper into the blankets. It was kind of cozy, being a blanket burrito."
    "But… I couldn't go back to sleep."

    r fr "\"Ugh…\""

    "Eventually, I gave up and raised one hand in the direction of my phone, curling my fingers around empty air."
    "Instead, I smacked my fingers into the edge of my glass nightstand and nearly broke a fingernail."

    r an "\"Gah!\""

    "Take two. I grabbed my phone successfully."

    r sus "(Only 10:42 AM…)"
    r "\"...\""
    r fr "(I guess I'll go to his conference after all.)"
    r "(Better than staying here with nothing to do but think…)"

    "I stumbled out of bed and rifled through my dresser."
    "Anything would do, as long as it was clean."



    scene bg conferencehall with fade
    pause(0.5)

#    <fade in sfx people talking>

    "Whoa… it's absolutely packed in here."
    "I checked my phone. This room was supposed to be the one with the keynote speakers."
    "Nobody was on the stage — instead, the room was packed with makeshift poster stands and people eagerly talking in small groups."
    "The massive banner on the far side of the wall said APPLIED MACHINE LEARNING CONFERENCE, LOS ANGELES SUMMIT."

    r sus "(Maybe I should've read up on computer science terminology before coming here.)"
    r fr "(I wonder how beginner-friendly these people are.)"

    "Oddly, despite how massive the crowd was, I didn't feel anxious. The atmosphere of the room reminded me of TED Talks I'd attended when I was a student."
    "The place buzzed with quiet excitement."
    "I glanced around the room, listening to people chatter. Listening to ideas being shared and connections being made."

    r surprise "(How do I put it…?)"
    r "(It's like everyone here is talking about contributing to human progress.)"
    r fr "(... Maybe that's dramatic.)"

    "I waded through the crowd and spotted a small group of people gathering around a poster."
    "Craning my neck, I read the words in blocky letters at the top: RETROACTIVE REVIEW OF PREDICTIVE DATA ANALYTICS MODELS OF COVID-19 PANDEMIC."
    r surprise "(Wow…)"

    "Two young adults were standing by the poster, each talking to a different group. One gestured excitedly to a graph on their poster."

    r "(I wonder if models like that affected the international response to the pandemic.)"

    "I left that group and continued walking around, stopping at posters I found interesting."
    "Some groups had a better understanding of presentation than others. Researchers with attractive posters tended to have bigger groups surrounding them."
    "Some unfortunate researchers stood awkwardly next to their posters as visitors ignored them."
    "I walked around, listening to some of the researchers speak. Most groups clearly intended to speak to professionals in computer science — some of the poster titles were completely unintelligible to me."

    r sus "(A MODIFIED MAXIMUM RELEVANCE MINIMUM REDUNDANCY FEATURE SELECTION METHOD BASED ON TABU SEARCH FOR HUNTINGTON'S DISEASE MINING.)"
    r "(Um… yeah. Those are definitely words.)"
    r fr "\"...\""
    r sus "(I'm pretty sure feature selection doesn't mean what I think it means here.)"

    "Other groups, though, actually had readable titles."

    r surprise "(MACHINE LEARNING APPLICATIONS IN SKIN CANCER PROGNOSIS AND PREDICTION. Nice.)"

    "I shuffled around some people to get a closer look at that poster."
    "Among the posters here, it wasn't particularly well-designed. Too many dark colors, hard to read."
    "The poster next to it, though, had a large group of people surrounding it. That was why I'd had to squeeze past people."
    "Curious, I tip-toed and tried to see what was so popular."

    r "(DIAGNOSING CUTANEOUS DISORDERS AND SKIN CANCER WITH CONVOLUTIONAL NEURAL NETWORKS.)"

    "That was when I noticed the mop of blonde hair next to it."

    
    show dylan sm at centerpos with dissolve

    r surprise "(Oh! This must be Dylan's thesis.)"

    "He was talking to a small group of older men and occasionally gesturing at the poster stand."
    "He was so well-presented, his hair neatly styled, his outfit clearly pressed. I almost felt bad for not dressing up more."

    r sus "(No, that doesn't make sense, Robin… he's presenting here. Of course he has to look professional.)"

    "Presenting. I glanced at him."

    d grin "\"—the importance of classifying cancer patients into high or low risk groups. Machine learning methods, though, are able to—\""

    "I tried to inch closer, squinting at the words on his poster."

    r surprise "(It's a nice poster, but why does the text on all of these have to be so small?)"
    r fr "(I guess they didn't expect a crowd around them. If I was standing closer, it'd be fine.)"

    "After a moment, I gave up and just started listening to what Dylan was saying."

    r surprise "(Unexpectedly, he's a good speaker.)"

    "Dylan was a bit stiff and shifted from foot to foot, but his words came out smoothly, as if he'd practiced them a thousand times."
    "Whenever one of the men had a question, his answer was succinct and confident."

    d fr "\"Of course, for models like these to be used in everyday clinical practice, they need to be accompanied by review from trained medical professionals. Outside of the legal—\""

    show dylan surprise

    "Dylan's eyes met mine, and he faltered."
    "He immediately straightened up and looked back to the men he was talking to."

    d surprise "\"—er— outside of the legal ramifications that would happen if we claimed to replace trained medical professionals…\""

    "He continued speaking with them, but glanced in my direction now and then."
    "He shifted from foot to foot again."

    r fr "(Is he nervous? He's doing fine.)"
    r sm "(Go Dylan!)"

    show dylan sm

    "I listened to him talk to the small group that had gathered around him. Luckily, it seemed like many of them were also unfamiliar with the industry jargon, so Dylan explained much of it to them."
    "People left his presentation nodding, or smiling, or discussing his paper. But more people came than left, so in the end, I wasn't able to speak with him."

    r fr "(Well, it's nice to see him succeeding at what he's doing.)"
    r surprise "(I didn't realize he was so proficient at his work.)"
    r fr "(It makes me feel like I should try harder to be a good librarian.)"
    r sus "\"...\""
    r fr "(I'll think about it.)"

    "After a while, I waved to Dylan and left the conference."

    r surprise "(I feel like I don't really know a lot about Dylan, but every time I see him, I learn a little more.)"

    scene bg black with fade
    pause(0.5)

    r surprise "(That was nice.)"
    r sm "(I… should go to these events more often.)"



# ########################
# EVENING: Post-conference
# ########################

    scene bg homeunlit with fade
    pause(0.5)

    r fr "(Oh. I have free time again.)"
    r "\"...\""
    r "(What an unpleasant feeling.)"

    "I looked down at my phone, and the single text I'd gotten from Dylan about the location of the conference."

    r surprise "(I suppose… it… wouldn't be weird to text him about today, right?)"
    r fr "(Just something saying he did a good job, or I felt like I learned a lot.)"
    r "(... Yeah, I'll do that.)"



# ######################################
# REGULAR SCENE: Library post-conference
# ######################################

    scene bg library with fade
    pause(0.5)

    r surprise "(Oh! I can pick up Oathbringer today.)"

    "As soon as I got into work on Monday, I immediately went to get the book."
    r an "(Oh god, I can't read it until lunch break. No!)"
    "I fidgeted, wondering if I could get away with reading on the job."

    r sus "(I mean… I work at a library… and no one comes here on Monday mornings…)"
    r "(Ugh, but if Heather catches me…)"

    "In the end, I decided not to read on the job. It took most of my willpower, though."
    "Since there was still no one around, I helped acquisitions run some errands and restocked the shelves, then sat back at my desk."

    r fr "\"...\""

    "Glancing around at the library, I noticed there were only one or two people on my floor."
    "I wanted to keep my mind busy. I turned to my monitor and thought about what I'd seen yesterday at Dylan's conference."

    r "(There were a lot of words I didn't recognize. Some of them were in nearly every presentation.)"
    r sus "(Neural networks, machine learning, deep learning… Are these all the same thing?)"
    r fr "(Guess I'll read up on it.)"


    scene bg library with fade
    pause(0.5)

    r sus "(Thirty minutes is not long enough to read Oathbringer.)"

    "I tossed my empty sandwich wrapper in the trash and hefted the thousand-page book in my arms."
    "It was brilliant. A masterpiece. And I could not wait until I could get home and read more."
    "On my way back, I saw Dylan working at a desk by the sunny windows."

    r surprise "\"Dylan!\""

    show dylan surprise at centerpos with dissolve

    "He turned, his expression perplexed. When he saw me, he smiled."

    d surprise "\"Wow.\""
    d smirk "\"This is the first time you've ever looked happy to see me. Are you starting to want me around?\""

    r fr "\"Of course I do. What do you mean?\""

    "I gave him a blank look. Did he really think I'd have put up with him for so long if I hadn't?"

    d surprisebl "\"...\""
    d "\"Er…\""
    d frbl "\"I see.\""

    "He looked down."
    "Then he noticed the book I was clutching."

    d surprise "\"Is that your copy of Oathbringer?\""

    "I nodded, smiling widely."

    r sm "\"Just got it this morning. I can't wait to go home and read it.\""

    d "\"Wow, that took a while. Almost a month.\"" 
    d smirk "\"You should consider reserving e-books through this library. I'm halfway through the book already.\""

    r an "\"No spoilers!\""

    "I shrieked quietly, clutching the book to my chest."
    "Dylan laughed."

    d "\"Fine, fine. Let me know when you get to the part where Kala—\""

    r "\"No!\""

    "Dylan broke into a smile so wide that I wanted to smile, too."
    "Instead, I grabbed a chair and sat next to him."
    r fr "(Still got five minutes on my lunch break.)"

    r surprise "\"I saw you at the conference yesterday. You looked like you were in your element.\""
    r sm "\"Pretty much everyone left your presentation talking about your research. It was amazing.\""
    r "\"Is that what conferences are always like?\""

    d frbl "\"...\""

    "Dylan scratched the back of his neck bashfully."

    d fr "\"Now, yeah.\""
    d "\"I used to be really awkward. It took a long time for me to learn how to do those presentations.\""

    r sm "\"Heh.\""
    r smirk "\"I can picture that so easily.\""

    d frbl "\"Hey!\""

    r sm "\"You did a good job, though. I wouldn't have noticed.\""
    r surprise "\"I mean, I noticed you were nervous, but it wasn't too bad.\""

    d "\"...\""

    r fr "\"A lot of the presentations there were hard to understand without industry knowledge. Yours was pretty easy to listen to, though.\""

    d fr "\"Oh, right. Research conferences are always like that.\""
    d "\"Don't worry too much about it. I'd be surprised if you understood much of anything without a computer science background.\""

    "I nodded."

    r surprise "\"I looked some of it up afterwards. I probably should've done that before going, but it hadn't occurred to me.\""

    show dylan surprise

    r fr "\"Anyways, it was a pretty big rabbit hole. I spent an hour reading up on the current research in machine learning, but I still feel like I don't know much.\""

    "Dylan's eyes lit up."

    d surprise "\"You read up on it on your own?\""
    d gr "\"Don't worry about not getting it at first — it's hard to understand a lot of the research output without knowing some computer science theory and some linear algebra.\""

    r surprise "\"How so?\""

    d sm "\"Papers always assume a base level of familiarity with the field. How much do you know about computer programming?\""

    r fr "\"Not much. I studied a bit back in the Tumblr era, when…\""



# ###################################
# REGULAR SCENE: Kids and the library
# ###################################

    scene bg library with fade
    pause(0.5)

    "Teenager" "Thank you so much!"

    r sm "\"No problem. Let me know if you need any more help.\""

    "I walked back to the information desk with a smile on my face. Today was a good weekend day — plenty of people were coming in to relax with a book or two."
    "I passed a table of teenagers working on math homework and talking in hushed voices."

    r fr "(I wonder if Heather ever did restock on our disinfectants. Maybe I should go check while no one needs help around here?)"

    show dylan fr at centerpos with dissolve

    "As I approached my desk, I saw Dylan sitting at a table nearby, his back to me."

    r sm "\"Heh.\""

    "I slowed my pace, rolling my steps along the outsides of my soles so they were quiet against the carpet."
    "Then I clapped my hands down on Dylan's shoulders."

    d surprise "\"Gah!\""

    r grin "\"Ahaha!\""
    r sm "\"Good morning. What're you up to?\""

    "Dylan rubbed his shoulders, glaring at me halfheartedly."

    d fr "\"Just grading some exams.\""

    r surprise "\"Oh, I think that's the first time I've seen you do…\""

    "I trailed off, then looked away. I didn't want to remind him of the last time I'd seen him doing TA work — the Cassidy situation."
    "Dylan must've known what I meant, but he chose to ignore it."

    d "\"I don't spend a lot of time grading — there's just one midterm in this class. I'm almost done, anyway.\""

    r fr "\"Oh, I see.\""

    "I idly watched Dylan flip through the pages of an exam packet."
    "Recently, it had become a normal thing for him to greet me at the library. We'd taken to talking several times a week."

    "Kid" "Umm… miss?"

    "I looked around to see no one."
    "Then I looked down. A tiny girl at my side was clutching a piece of paper to her chest and staring up at me."

    "Kid" "\"You have a nametag… do you work here?\""

    r fr "\"Yes, I do. What can I help you with?\""

    "I stared at the girl curiously. She started shaking."
    "Dylan glanced over at us."

    "Kid" "\"U-um… never mind.\""

    d sm "\"Were you looking for a book?\""
    d smirk "\"Don't mind how scary her face looks — the librarians here are actually very helpful.\""

    show dylan sm 

    "I opened my mouth to protest, but Dylan smiled at the girl, and she relaxed a little."

    "Kid" "\"O-oh… okay.\""

    r sus "(What the—)"

    "The girl unfolded the piece of paper she was holding and started reading off it. Her voice was shaky."

    "Kid" "\"I want to find… a book I read here… last week. It had a red cover. There was a dog…\""

    "I glanced at Dylan, then tried for a smile. My face felt stiff, but I hoped it worked."

    r grin "\"Do you remember where you found it?\""

    "She shook her head and looked down like she was ashamed."

    r sm "\"That's okay. Hmm, let's see. A red cover and a dog… Was it Clifford the Big Red Dog? Magic Treehouse?\""

    "Kid" "\"Yes! Um! The first one!\""

    r "\"Great. Let's go get the books now, then.\""

    hide dylan

    "I led her to the children's section and showed her the large shelf dedicated to the Clifford series."
    "Despite her cautious expression, as soon as she saw them, she bounded towards the shelves and started pulling books out."

    r "(Cute. Reminds me of me as a kid.)"
    r fr "\"...\""
    r sus "(Hopefully not too much like that.)"
    r fr "(I wonder where her parents are.)"

    show dylan fr at centerpos with dissolve

    "I returned to my information desk, where Dylan had gone back to grading exams."
    "Glancing around, I saw that my floor of the library was mostly empty, despite the activity downstairs and in the children's section."
    "Since no one was around, I pulled out a chair and sat down across from Dylan."

    r sus "\"... Do I have a scary face, Dylan?\""

    show dylan grin

    "Dylan looked over at me and started laughing."

    r "\"I'm serious!\""

    d grin "\"You…\""
    d "\"Well, you do look intimidating with that stare of yours.\""

    r "\"...\""

    "I groaned and put my face in my hands."

    r "\"My coworkers always tell me to smile more... I always thought it was just because I looked tired.\""

    r "\"But I've actually been taking care of myself and sleeping more recently.\""
    d sm "\"Well, that's a good thing, even if you still scare little kids.\""
    r "\"Dylan!\""
    "He chuckled again and set down his pen."

    d fr "\"It will help if you smile more at the library visitors. Especially kids.\""

    r fr "\"I know, but... in the past, I think I used to scare people with my smile.\""

    d surprise "\"...\""

    "The look of disbelief on his face was almost funny — one eyebrow furrowed, the other raised, his mouth slightly open in confusion."

    d fr "\"Are you sure you weren't grimacing at them?\""

    r an "\"Of course not!\""
    r fr "\"...\""
    r "\"I think.\""

    d smirk "\"You think.\""
    d "\"Well, I've seen you smile, and you look nice. Smile at visitors like that.\""

    r frbl "\"O-Okay.\""

    "I mumbled under my breath."
    "Inexplicably, I felt my face warming up. I ducked my head down, hiding my face from Dylan."

    show dylan frbl

    "Dylan seemed to realize what he'd said just then, and looked away."
    "We sat together in comfortable silence for a while. I laced my fingers together, tapping them on the desk."

    r fr "\"...\""
    r "\"I wonder where that girl's parents were.\""

    show dylan fr

    "Dylan glanced up at me, his expression concerned."

    d fr "\"Is that something we should worry about?\""

    r "\"Not necessarily. Sometimes, the parents are just browsing a different section of the library.\""
    r "\"That kid wasn't too young. It wouldn't be weird for the parents to let her look for books herself.\""
    r sus "\"Still… I worry sometimes.\""

    r "(She looked so anxious. I know that's not always a sign of a bad home situation, but for a kid that young…)"

    d sus "\"...\""
    d fr "\"Is there any particular reason you're worried? Or is it more of a general concern?\""



    menu: 
    
        "The library is a safe escape for some people.":
            jump kid_escape
    
        "Just general concern.":
            jump kid_general



# IF: The library is a safe escape for some people.

label kid_escape:

    r sus "\"Some of the anxious kids come to the library to escape their home situation.\""
    r "\"Anxiety and nervousness in kids that young is one sign. Behavioral issues are another. Like the kids who run around throwing books.\""
    r fr "\"I know it's not always a sign of a bad home life, but… it makes me nervous.\""
    r sus "\"I want to help them, if I can. But I can't really do that if they're scared of me.\""

    "Dylan was looking at me with an unreadable expression."

    r fr "\"What?\""

    "Slowly, deliberately, trying not to scare me — he put one hand over mine."
    "His fingers were long, long enough to wrap around my hands."

    r surprisebl "(It feels warm…)"

    d "\"You're a good person.\""

    show dylan frbl

    "Then he pulled his hand back and folded it gently into his lap."
    "That jarred me back to my senses."

    r fr "\"No, I'm not.\""

    "I spread my fingers on the table, trying not to think about how much I wanted that warmth back."

    r sus "\"I was just one of those kids myself. And the library saved me.\""

    d surprise "\"From your home situation?\""

    r fr "\"Yeah.\""
    r "\"My mom was a junkie. I got out of the house as much as I could.\""
    r sus "\"The local librarians became my second family. I guess they sort of knew what was happening... there were probably a lot of kids like me around.\""

    show dylan fr

    "I looked down at the table, afraid to see Dylan's expression. Was that too much information?"

    r "\"Anyways, I used to be like that girl — terrified of adults, shaking in my shoes.\""
    r fr "\"A lot of kids come to the library. After a while, you learn how to tell which ones have healthy families and which ones don't.\""
    r sus "\"There isn't a whole lot we can do about it.\""
    r "\"Once my coworker called CPS for a kid who opened up to her, but most never do. All we can do is be supportive and kind. Show them that not all adults are bad.\""

    "Dylan nodded."
    "I looked up, and my eyes met his."
    "He was… listening. Not trying to give me his opinion. Not trying to tell me what to do. Just listening."
    "For some reason, that made my insides feel incredibly warm."

    d "\"Is—\""

    r surprise "\"That's—\""

    "We spoke at the same time."

    d "\"...\""
    r fr "\"...\""
    r "\"You first.\""

    d "\"...\""
    d "\"Is that why you're a librarian now? To give back to the community?\""

    r "\"Yeah.\""
    r sus "\"... That sounds too nice, though. I mean, it's also a stable career. I'm not altruistic.\""
    r "\"Also, I'm pretty sure I'm not helping kids like me. I scare away the ones that are anxious.\""

    d sm "\"But you're patient and strict with the troublemakers, and you said that was also a symptom of a bad home.\""
    d fr "\"I think you're doing well.\""

    "I took a shaky breath."

    r surprise "\"Thank you.\""

    "I cleared my throat and met Dylan's eyes properly."

    r sm "\"Thank you for validating my efforts. It's… nice to hear.\""

    "He nodded."

    d "\"What were you going to say?\""

    r surprise "\"Uh…\""
    r fr "(Oh, right.)"

    "I had almost forgotten—"

    r "(I was thinking back to the time he seemed insecure about his own job. When I insinuated he might've been a bad teacher.)"
    r "(I was going to say, that's why I don't think you could ever be a bad teacher. Because you're the kind that reaches out to your students when you're concerned about them.)"
    r sus "(But I don't think I should bring up Cassidy.)"

    "Especially because I just mentioned my mother had been a junkie."
    "Someone like Dylan could easily put two and two together."

    r fr "\"Hmm…\""
    r "\"I forgot what I was going to say.\""
    r "\"Probably wasn't important.\""

    d sus "\"Oh. A shame.\""

    show dylan fr

    "I glanced around the library a bit. There was still no one on this section of the floor."

    r "\"By the way, you've been coming by to my work a lot, but I never took you up on your offer to see you at work.\""

    d sus "\"Hey, I come to the library all the time anyway.\""
    d "\"...\""
    d fr "\"Well… you've already seen me presenting at a conference. You're welcome to come to my discussion if you want, but I don't see how it would be much different for you.\""

    r sm "\"I'll think about it. Friday afternoon, right?\""

    d surprise "\"Yeah.\""

    "I nodded. Then I got up from my seat."

    r fr "\"See you there, then. I'm going to go check if that girl's parents came back for her.\""

    d sm "\"Good luck.\""

    jump post_kid



# IF: Just general concern.

label kid_general:

    r fr "\"Just general concern.\""
    r sus "\"... I'm going to go check on her in a bit, just in case.\""

    d sm "\"That sounds good.\""

    "We sat in comfortable silence for a while. I watched Dylan grade exams for a bit longer."

    r surprise "(I wonder if Dylan was reading Oathbringer and I was standing behind him, would it still look like I'm reading a book on the job?)"
    r fr "\"...\""
    r "(No… I shouldn't think about reading Oathbringer at work…)"

    r surprise "\"By the way, you've been coming by to my work a lot, but I never took you up on your offer to see you at work.\""

    d sus "\"Hey, I come to the library all the time anyway.\""
    d fr "\"...\""
    d "\"Well… you've already seen me presenting at a conference. You're welcome to come to my discussion if you want, but I don't see how it would be much different for you.\""

    r sm "\"I'll think about it. Friday afternoon, right?\""

    d "\"Yeah.\""

    "I nodded. Then I got up from my seat."

    r fr "\"See you there, then. I'm going to go check if that girl's parents came back for her.\""

    d sm "\"Good luck.\""

    jump post_kid



label post_kid:



# #############################
# REGULAR SCENE: Watch Dylan TA
# #############################

    scene bg streetday with fade
    pause(0.5)

    "I felt silly with my beanie on my head and backpack on my shoulders — like I was imitating something I wasn't."
    "I had never really paid attention to that feeling."
    "It wasn't that I belonged here any less than the last time I'd been here. It was just that today, someone I knew would see me pretending to blend in."
    "Dylan."

    r sus "\"...\""

    "Well. Maybe it was normal to be nervous when dressing up as a fake student just to visit your friend. It wasn't like I had a ton of experience doing that."
    "Trying to ignore the small flips my stomach was doing, I triple-checked the sign on the door before entering the lecture hall."


    scene bg conferencehall with fade
    pause(0.5)

    r fr "(Hmm. Guess I'm a little early.)"
    "I glanced around the lecture hall. Several students were seated near the front of the room, but nowhere near the number that had been here last month."
    "Dylan wasn't here yet, either."
    "I picked a seat in the middle of the room — not too far back that I'd look out of place, but not in the front where I'd be expected to participate."
    "Then I pulled out my copy of Oathbringer and opened it to my bookmarked page."

    r "(I'm almost halfway through this thousand-page tome already.)"

    "I glanced around the room. Was it weird to have a novel out while everyone else was on their laptops?"
    "None of the other students seemed to care."
    "I caught myself observing their faces, checking if any of them were Cassidy."

    r sus "\"...\""

    if CASSIDY_ARRESTED == True:
        "I couldn't help but associate this place with her, and the time I'd helped get her arrested."
        r fr "(I wonder what she's doing right now.)"
        r surprise "\"...!\""
        r sus "(I don't think I've ever thought that about a criminal…)"

    if CASSIDY_ARRESTED == False:
        "I couldn't help but associate this place with her, and the time I'd let her get away from Anderson."
        r fr "(After all those nights I spent getting enough information to help Anderson arrest her… I ended up feeling sympathetic to her.)"
        r "\"...\""
        r sus "(I hope she's super successful as a tutor and gave up on dealing coke.)"
        "I'd have to swallow my pride, but I'd at least know I'd been right to let her go."
        r fr "(It would be nice if I could ask Dylan about it.)"


    "I glanced around one more time, then turned back to my book."


    scene bg conferencehall with fade
    pause(0.5)

    show dylan fr at centerpos with dissolve

    "It wasn't much longer before Dylan and the rest of his students filed into the room."
    "I glanced up from my book as he lectured. Even though I wasn't familiar with most of the topics he covered, it was clear that he spoke with confidence and gentle authority."

    if CASSIDY_ARRESTED == False:
        r fr "(Oh, there's Cassidy.)"
        "I glanced around the room and spotted her cropped brown hair from behind."


    "The lecture hall was filled with the sound of fingers tapping keyboards. From behind most of the students, I could see that their computers were open to notes."

    r surprise "(Wow. If I were still in university, I'd definitely be browsing Discord during lecture.)"
    r "(And so would everyone else in the class, unless the lecturer was really good.)"

    "I ended up watching the class, closing my book and leaning back in my chair."

    show dylan sm

    "Occasionally, students would ask questions about the material. One man was clearly lost as to what Dylan was saying, but Dylan answered his questions patiently and thoroughly."
    "Because of his basic questions, I actually ended up learning a little more about computer networking protocols."
    "After half an hour, Dylan ended his lecture."

    d fr "\"That's all for today's lecture. I'll be here for the rest of the discussion if you have any questions or want project help.\""

    "To my surprise, almost no one left."
    "Instead, some students went up to him with their laptops and started talking with him. Others got together in small groups, talking about the material in the lecture and their progress on the project."

    r fr "(Hmm… it feels a little awkward to sit here now. I guess I'll wait for him outside.)"

    "I gathered my things and stood up. Dylan glanced over at me and met my eyes."
    "I smiled and gave him a little wave."
    "Then I headed back outside."


    scene bg streetday with fade
    pause(0.5)

    "I set my things down on a bench outside the front door of Engineering IV, then sat down and stretched."

    r fr "(I guess this is the side of the building where students normally walk… there are a lot of people around campus right now.)"

    "I resumed reading Oathbringer, glancing up every time I saw someone leave the building."
    "People started trickling out of the lecture hall one by one."
    "It wasn't much longer before Dylan came out of the building and spotted me."

    show dylan sm at centerpos with dissolve

    d sm "\"Hey.\""

    r surprise "\"Hey.\""

    "I closed Oathbringer and put it back into my bag as he approached."

    d surprise "\"I didn't think you'd really show up.\""

    r sm "\"I hope it didn't cause any trouble for you.\""

    d fr "\"No, it's fine.\""

    "He gestured to the empty space on the bench next to me."

    d "\"Mind if I join you?\""

    "I scooted over to make more space. He hesitated, then sat down next to me and set his bag on the floor."
    "Wind gusted past us, and I reached up to prevent my beanie from flying off."
    "Dylan noticed me reaching up and pulling my hat back down."

    d surprise "\"You covered your hair today.\""

    r fr "\"Well… you said it was really recognizable.\""

    d sm "\"Ah. It is.\""

    "We sat in comfortable silence for a while, watching students pass us by."

    r surprise "\"I think it was that same day — or the next time you came to talk to me at the library.\""
    r fr "\"You were insecure about your teaching and invited me to watch you TA, even though you were suspicious of me.\""

    d an "\"I was not insecu—\""
    d "\"...\""

    "Dylan cleared his throat."

    d sus "..."
    d fr "Well… I guess."

    "I cracked a smile at the grimace on his face."

    r sm "\"I remember thinking back then that you probably weren't a bad teacher. And I was right.\""

    d sus "\"...\""
    d fr "\"Even if you're just being polite… it's nice to hear that.\""

    r surprise "\"I'm not.\""
    r "\"Not just being polite, I mean.\""
    r sm "\"All of your students respect you. The way they pay attention in your class proves it.\""
    r "\"Not a single person was browsing Discord, or Facebook, or the news. Everyone was referencing your lecture slides or taking notes.\""
    r smirk "\"The way they asked you questions was pretty comfortable, too. Everyone sitting in your class treats you like you're their smarter older brother.\""

    d surprise "\"Wow.\""
    d smirk "\"That … might be the best compliment anyone has ever given me.\""
    d grin "\"... Thank you.\""

    show dylan smirk 

    "Dylan bit his lip and shifted in his seat."

    d "\"...\""
    d "\"Their smarter older brother, huh?\""
    d "\"Would you see me as a smart older brother if you were in my class?\""


    
    menu: 

        "I'd rather not think of you like an older brother.":
            jump bro_no

        "Sure. You seem like you'd be a chill sibling.":
            jump bro_sure



# IF "I'd rather not think of you like an older brother."

label bro_no:

    r surprise "\"Er…\""
    r sus "\"I'd rather not think of you like an older brother.\""

    show dylan surprise 

    "I was suddenly aware of how he was sitting just inches away from me on this bench, and thought of how warm his hand had been when he'd put it over mine a few days ago—"
    "I clenched my fist and pulled it back against my chest, resisting the thought of reaching for his hand."

    d surprisebl "\"... Ah.\""

    "Was Dylan turning pink?"

    r frbl "(Please tell me I'm not blushing just as much as he is right now.)"

    "He cleared his throat."

    d smirk "\"Right. That's a weird thing to ask, sorry.\""

    hide dylan

    "Slowly, we eased into more regular conversation."
    "We talked about his class, what his students were like, how busy our schedules were."
    "But through it all, it felt like that moment was still in the air — a slight tension that kept the blush in his face and the warmth in mine."
    "When he shifted in his seat, or gestured with his hands, my eyes were drawn to his movement."

    r frbl "\"...\""
    r surprisebl "(Focus on what he's saying, dammit.)"

    "\"When the sun started setting and we bid each other farewell, I gathered my things and headed back to my car.\""

    r frbl "\"...\""

    "I touched my cheek. It still felt warm."

    jump bro_done



#   ELSE IF "Sure. You seem like you'd be a chill sibling."

label bro_sure:

    r sm "\"Sure. You seem like you'd be a chill sibling.\""
    r smirk "\"Plus, you'd probably do my homework for me if I pestered you enough.\""

    d an "\"What? Hell no I wouldn't.\""
    d smirk "\"A bratty little sister like you? I'd just give you a math textbook for your birthday. To help you figure it out on your own.\""

    r surprisebl "\"...\""

    "My heart did several little flips at his smile."
    r "(Oh no. It's cute.)"

    r frbl "\"Uh—\""

    "I cleared my throat."

    r surprisebl "\"I mean, we were just talking about your teaching skills. If you had a sibling, I'd— I think you'd teach them how to do their homework themselves.\""

    "Grasping at straws to keep the conversation going, I rushed the words out."
    "Dylan met my eyes."

    d frbl "\"...\""

    "He looked away, his cheeks tinged pink."

    d "\"...\""
    d fr "\"Well, I actually do have a brother. A younger brother. And you're right, I always taught him how to do the problems himself.\""
    d smirk "\"When he was younger, he often tried to trick me into just doing his homework for him, but he eventually gave up.\""

    "I laughed."

    r grin "\"Of course he did. That sounds just like you.\""
    r "\"Did you ever give him a math textbook for his birthday?\""

    d grin "\"What? Of course not.\""
    d smirk "\"That'd be reserved for people who like math, and people like you.\""

    r surprise "\"Hey!\""

    "Dylan chuckled."

    hide dylan

    "We ended up talking for a while longer, until the campus was washed in orange light from the sunset."
    "When we gathered up our things and waved goodbye to each other, I turned away with a smile."

    jump bro_done



label bro_done:



# ##############################################################
# REGULAR SCENE: Dylan brings Robin food during menstrual cramps
# ##############################################################

    scene bg homeunlit with fade
    pause(0.5)

    "My Sunday began when I woke up to my abdomen screaming in pain."
    "I groaned and rolled over in bed, trying to ignore it. But a second later, I swung my legs over the side of the bed and climbed out."

    r sus "(Don't want to get the sheets bloody…)"

    "My period always heralded its arrival with cramps so bad I was certain my uterus was making an attempt to tie itself into knots."
    "I stumbled across my studio to clean up."
    "On the way, I grabbed medicine for the pain and a glass of water."

    r "\"Ugh.\""

    r "(Pretty sure I'm not supposed to take this without food.)"

    "I thought about it for a second, then took the medicine anyway, chasing it down with several large gulps of water."
    "It always took time to kick in. In the meantime, sporadic spasms would render me mostly immobile."
    "Crawling back into my bed, I checked my phone."

    r fr "(Only 9 AM…)"

    "A few new messages at the top of my phone caught my eye."
    "Some were from Dylan, sent this morning. The others were from Anderson, sent last night."

    d sm "<How are you enjoying Oathbringer? I saw you reading it when you were on campus, but I forgot to ask how far you'd gotten.>"
    d "<I finished it last week. It'd be nice to discuss it with you if you're done.>"

    "I squinted at the message timestamp. Why was he awake at 8 AM on a Sunday?"
    "I glanced up at where the book was sitting on my nightstand."
    "I'd spent some time reading it last night. It felt nice to go back to reading in my free time, instead of pushing myself to hunt down dealers."
    "Moving carefully to avoid the cramps flaring up, I typed a response back to him, my hands shaking."

    r surprise "<i'm like 3/4ths through the book, i think king t is gonna end up betraying the new alliance.>"
    r sus "<wish i could finish it today but prob can't. im bedridden today, gonna try and sleep until it's over>"

    "I glanced at the notifications labeled ANDERSON, set my phone down on my nightstand, then curled back into my blankets."

    r fr "(I don't want to deal with those ones right now…)"

    "My phone vibrated less than a minute later, though."
    "I groaned as I reached a hand out of my blanket burrito to grab it."

    d surprise "<Bedridden? Did something happen?>"

    r sus "<yeah it's just period cramps fucking me up really bad>"

    "I paused with my finger over the send button. Was that too much information?"

    r "(I'm too tired to second-guess myself right now…)"

    "I hit the send button and wrapped my blankets back around me, this time with my phone in my hands."

    r "<it's hard to get out of bed and move when they're bad, but it's nothing unexpected>"

    d fr "<That sounds rough… Will you be able to eat and drink water if you can't move from your bed today?>"

    r "<i wasn't really planning on eating>"

    d surprise "<For the whole day?>"

    r "<yeah, no food left>"

    d sus "<That seems like it would make you feel even weaker. It's really important to eat, especially if you're already bedridden.>"

    r fr "\"Well, not like I can do much about it now.\""
    "I mumbled aloud."
    "My phone vibrated with a new message before I could respond."

    d fr "<Do you want me to bring you food?>"

    "I hesitated."

    d fr "<I was just about to make breakfast. If you want eggs and potatoes, I can bring some over.>"


    menu: 
    
        "That's really kind of you. Are you sure?":
            jump dylan_visit
    
        "Is that your ploy to find out where I live?":
            jump dylan_no_visit



# IF: "That's really kind of you. Are you sure?"

label dylan_visit:

    $ DYLAN_KISS = True

    r surprise "<that's really kind of you>"
    r fr "<are you sure?>"

    "I waited a little longer before I received his message this time. The vibration was a little reassuring."

    d fr "<Yeah. It's really important that you eat when you're already weak. It'll take me 20 minutes to cook, then more to drive over. Where is your place?>"

    "I texted him my address."

    d "<Maps says it's ten minutes from my place. Be there in 30-35 min.>"

    r sm "<thank you, i appreciate you>"

    "I hesitated, then hit the send button without thinking too much about it."
    "There was a pause."

    r frbl "(Oh god, was that weird?)"

    "I stuffed my face into my pillow. I was too tired to overthink something this mundane."
    "A minute later, my phone vibrated."

    d sm "<No problem.>"

    "I sighed with relief."
    "With that conversation over, I glanced at my phone's other notifications."
    "I didn't really want to deal with Anderson right now, but I was already wide awake. I reluctantly clicked on the messages."

    a surprise "<hey, you haven't really been that involved with arrests recently so i want to fill you in on what's happening this week>"
    a sus "<i'm gonna be part of a pretty big arrest on wednesday. it's for a guy with a couple of homicide charges against him. not really your usual forte, but i figured you should know because the arrest is happening close to your workplace>"


    "I tensed up, which was a mistake, because my cramps immediately flared up again."

    r sus "\"Ow…!\""

    "I took several shallow breaths, gasping through the pain."
    "Black spots danced in my vision. I dropped my phone and tried to relax. Breathe. Breathe…"
    "After what felt like minutes later, the pain finally subsided to a low rumble."

    r sus "\"Ugh…\""

    "Sweat had beaded up on my forehead and trickled down into my pillow."
    "I picked up my phone again, trying to ignore the dampness of my pillow and pain in my abdomen."

    a fr "<it's the old building right next to your library>"
    a sus "<we're gonna smoke him out, figuratively>"
    a "<the bosses think it'll go fine but i'm sus because arson is in his list of charges. don't want him to endanger any civilians before he gets arrested…>"
    a an "<anyway, this isn't public knowledge so you can't tell your coworkers to be on alert, but you should know at least>"
    a "<took us a while to find out enough info to smoke him out, he put some effort into hiding>"
    a fr "<i still think you'd be able to do good if you joined our force and helped with the info team, you find stuff faster than any two of em combined>"

    "I glanced over his messages one more time before responding."

    r fr "<thanks for telling me>"
    r sus "<i don't think i could do anything about that arrest anyway, but i'll stay on alert>"

    "I ignored his implicit question about joining the police and set my phone back on my nightstand."

    r "(Ugh…)"

    "I rolled over and tried to fall back asleep."


    
    scene bg homeunlit with fade
    pause(0.5)

    "I was woken up by two things this time: my phone ringing, and my abdomen screaming."

    r an "(Oh god. Ow. Ow.)"

    "When I got cramps this bad, it was always better to lay down straight and stretch, rather than curl myself into a ball. But it was always tempting to curl up."
    "I took a minute to try to relax my body."
    "My phone's ringtone slowly faded into silence as my face beaded with sweat."
    "Eventually, the cramping did calm down."

    r surprise "(Phew…)"
    r sus "(It's not as bad now that the meds have kicked in, but it still sucks.)"

    "I checked my phone, then bolted upright in bed."
    "<1 missed call from: DYLAN>"

    r surprise "(Oh fuck, I overslept!)"

    "I punched in a new call back to him as I scrambled to my door, nearly tripping over my blanket as my feet dragged it to the floor." 
    "He answered the call just as I opened my front door."

    
    show dylan fr at centerpos with dissolve

    d fr "\"Hello.\""

    r "\"Sorry I missed your call, I fell back asleep—\""

    "Dylan was standing outside my apartment with a large lunch box in his hands."
    "Seeing him standing there, his hair tousled, wearing a nice sweater and jeans, I realized I was still in my pajama shirt and old shorts."
    "I froze."

    d sm "\"Don't worry about it. I'm glad I caught you before I left.\""

    "He held out the lunch box to me."
    "Through the glass lid, I could see he'd brought me an assortment of scrambled eggs, fried potatoes laden with spices, sausages."

    r surprise "(Wow. I can't remember the last time I ate a home-cooked meal like this…)"

    "I took the lunch box with both hands, carefully holding it as if it were a treasure."

    r sm "\"Thank you. I… really appreciate it.\""
    r grin "\"Also, you're a good cook.\""

    "Dylan chuckled."

    d smirk "Say that after you've eaten it."

    "I nodded."

    r surprise "\"Do you want to come in?\""

    d surprisebl "\"Er…\""
    d fr "\"Are you sure? I don't want to impose on you if you're sick.\""

    r sm "\"Yeah, it's fine. You came all this way and made me lunch — it'd be weird not to at least make tea for you.\""
    r surprise "\"If you want to, I mean.\""

    d sm "\"In that case, sure. Thanks.\""

    r sm "\"Mhmm. Sorry about the mess.\""

    
    scene bg homeunlit with fade
    pause(0.5)

    show dylan fr at centerpos with dissolve

    "I closed the door behind Dylan and went to the kitchen to make tea."
    "He glanced around the room — it was really just one room, a studio apartment — and ended up sitting at my computer desk, the only chair in the place."

    r fr "\"Do you like milk and honey in your tea? It's earl grey.\""

    d fr "\"I can't say I've ever tried either way.\""

    r sm "\"I'll add it, then.\""

    d sm "\"Thanks.\""

    "I carefully measured out tea leaves, poured hot water over them, filtered them out, and added honey and milk."
    "A few moments later, I brought the two cups over to my desk. Dylan watched as I set it down."

    d smirk "\"That looked really complicated.\""
    d surprise "\"I'm surprised you have everything you need to make tea, but don't have food to eat.\""

    r smirk "\"Tea is important.\""

    d smirk "\"... Food isn't?\""

    "I laughed and sat down on my bed, opening his lunchbox."

    r sm "\"Food doesn't keep as long, that's all. I have to keep buying it, and, well, I was supposed to make my grocery run today…\""

    d fr "\"Ah, that makes sense.\""

    
    hide dylan

    "He sipped his tea as we chatted."
    "As we eased into conversation, it became easier for me to stop thinking about the pain in my abdomen."
    "Dylan hadn't liked the interactions between two of the characters in Oathbringer, and found the tension between them contrived."

    show dylan an at centerpos with dissolve

    d an "\"I mean, if he had a problem with her accepting knighthood, why not say something to her about it?\""
    d "\"I understand if he was shocked at the time, but seven chapters later, he's still stewing in silence.\""
    d "\"At that point, he should have decided if he either wants to give up the relationship or work through his feelings with her.\""
    d smirk "\"Instead, he's just moping around and taking it out on her passive-aggressively.\""

    show dylan fr

    r fr "\"Well, it's obviously not healthy, but I can see why he's doing it.\""
    r "\"It's not unrealistic for Sanderson to portray him like that.\""
    r "\"If you look at his past interactions, he's never handled conflict well. He's never learned how to communicate when he's upset.\""
    r an "\"I don't think this is contrived at all — It's perfectly in line with how he thinks.\""
    r grin "\"This might be an opportunity for him to learn, if he can overcome that.\""

    d fr "\"Hmm…\""
    d sus "\"I don't want to say anything more on that. It'd be a spoiler.\""

    r surprise "\"No spoilers!\""

    show dylan grin

    "Dylan chuckled."
    "We got into heated debates about the story in Oathbringer, the character interactions, our theories about which side characters would end up being crucial to the in-universe alliance."
    "As we talked, I continued eating the food Dylan had brought me."
    "It was delicious."

    r grin "(Is it because he's a good cook, or is it because I know he made this for me?)"

    "Several times, I had to cover my mouth while talking, because I was still eating. I didn't want to stop. In a good way, for once."
    "The conversation eventually shifted to work."

    r surprise "\"Do you think, if I used your illness-diagnosing AI, it would tell me I was sick because of my period?\""
    r "\"Or would it tell me I have a kidney stone?\""

    "Dylan laughed."

    show dylan fr 

    "But then a thoughtful expression crossed his face, and he tapped his finger to his chin."

    d sm "\"Good question, actually. Do you want to try it out?\""

    r sm "\"Sure.\""

    "Dylan brought his laptop out from his bag and set it on the table."
    "I leaned forward and put his empty lunch box on my desk, but it was hard to see his screen from where I was sitting on the bed."

    r surprise "\"Come sit here — I can't see.\""

    "I patted the bed next to me."

    d frbl "\"...\""
    d "\"Um. Sure.\""

    "I smiled as he fumbled with his laptop."

    r grin "\"Thank you for the food, by the way. It was delicious. And I appreciate you bringing it all the way here for me.\""

    d sm "\"No problem.\""

    show dylan surprisebl

    "He sat down next to me, and I leaned over to see what was on his screen."
    "Only then did I realize how close we were — in my apartment, on my bed."

    r surprisebl "\"...\""

    show dylan frbl

    "I cleared my throat, trying to ignore the warmth in my face."

    r frbl "\"So what do I have to do?\""

    d fr "\"It's pretty simple. You mentioned a symptoms checklist last time, so I modeled it after that.\""
    d "\"See these dropdowns? Just open the ones that you think you have symptoms for, and check the boxes.\""
    d "\"Then hit the Next button at the bottom.\""

    r surprise "\"Wait, that's it?\""
    r fr "\"Is this actually artificial intelligence, or just a program with a bunch of 'if symptom, then illness' code?\""

    d sus "\"The latter, with a weighting system added for nuance.\""
    d fr "\"It's not artificial intelligence in the true sense of the word. There's no training or modeling involved.\""
    d "\"I did say it would be a simple model when you suggested it.\""

    "Dylan paused."

    d surprise "\"Wait a minute. I thought you didn't know anything about computer programming?\""
    d sus "\"How did you know that?\""

    "I looked away."

    r fr "\"Recently, I've spent some time reading up on artificial intelligence and machine learning.\""
    r sus "\"I still don't know much about it. There's more math involved than I thought, and it's not easy to grasp from the beginning.\"" 
    r fr "\"But, well, now I know the difference between machine learning and regular software, I guess.\""

    d surprise "\"...\""
    d "\"You looked it up on your own? And spent your free time reading about machine learning?\""


    r fr "\"Yeah.\""

    d grin "\"Wow.\""
    d "\"Color me impressed.\""

    r frbl "\"Th… thanks.\""

    "My stomach was doing the little flips again."
    "But it was kind of nice. Like a fluttery feeling. I tried to pay attention to that instead of the rumble of pain from my cramps."
    "Reaching over Dylan's lap to click the symptoms on his laptop, I opened every dropdown to see what options he'd added to the program."
    "Then I clicked the Suggestions button."

    d surprisebl "\"...\""

    r surprise "\"Whoa. \'Have you consumed 8 or more cups of water each day this week?\' \'On average, how many minutes a day have you walked this week?\'\""
    r fr "\"Did you add these questions yourself?\""

    d frbl "\"...\""

    r "\"Dylan?\""

    "I turned to look at him."

    d "\"Um. Yeah, I did. That's the weighting system.\""

    "Then I realized how close he was, how stiff his posture was, and how he was biting his lip—"

    r fr "(Oh.)"
    r frbl "(Oh!)"
    r "(I've been typing on his keyboard… in his lap…)"

    "I yanked my hands back and set them between us."
    "My fingers curled up anxiously, grabbing small fistfuls of the sheets as they moved."

    r frbl "\"S-Sorry.\""

    "I met his eyes."
    "Dylan's cheeks were flushed pink. Some part in the back of my brain noted that he blushed a lot."

    r frbl "\"Does that... bother you?\""

    "He took a short breath and looked away."

    d smirk "\"In a different way than you think.\""

    show dylan frbl

    r "(No, I was thinking that.)"

    "I hesitated. His hand was right next to mine, on the blankets."
    "Before I could think too much about it, I reached out and put a hand over his."
    "It was just as warm as I'd remembered."

    d smirk "\"Robin.\""

    show dylan frbl
    "His voice was cautious. But his voice caught in his throat."
    "I looked up at him, my expression pleading."
    "When our eyes met, he shifted in his seat."

    r surprisebl "\"Is this bad?\""

    d "\"...\""

    "Discouraged by his reaction, I tried to move my hand off his. But he turned his palm up and laced his fingers with mine before I pulled away."

    d sus "\"It's not that.\""
    d frbl "\"I don't want to take advantage of you when you're feeling weak.\""

    r surprise "(Wait, what?)"

    "I furrowed my brows."

    r an "\"Er… wait. I have period cramps, not a hangover.\""
    r surprisebl "\"You're not taking advantage of me.\""

    d "\"...\""
    d smirk "\"Fair enough.\""

    "He brushed the hair out of my forehead and tucked it behind my ear."

    show dylan frbl 

    r frbl "\"...\""

    
    scene bg black with fade
    pause(0.5)

    "I closed my eyes."
    "I felt his breath close to mine."
    "His momentary hesitation felt like such a tender gesture, at odds with the way my heart was pounding."
    "The warmth of his lips followed soon after."

    
    scene bg homeunlit with fade
    pause(0.5)

    show dylan frbl at centerpos with dissolve

    "I studied Dylan's face. He was flushed completely pink."
    "But he bit his lip. He looked conflicted."
    "I scooted closer to him and cautiously wrapped my arms around him."

    r frbl "\"It's all right. You don't have to push yourself.\""

    "He breathed out a sigh of relief and put an arm around me, pulling me closer to him."

    d "\"... Thanks.\""

    "My ear was pressed to his chest. I could hear his heartbeat fluttering."

    r surprisebl "(It's going faster than mine…)"

    "We stayed there like that for a while. I closed my eyes, enjoying his warmth. It felt surreal."
    "It was hard to believe I'd been curled up in bed staving off the pain of cramps just an hour earlier."

    d fr "\"I don't want to sound like I'm turning you down.\""

    r surprise "Hm?"

    d frbl "\"I…\""

    "Dylan cleared his throat nervously."

    d "\"I do want you. Just… I'd rather take it slowly. Get to know you a little more, spend more time with you.\""
    d smirk "\"Also, I still feel bad that you're in pain right now.\""

    r surprise "\"It's not so painful when we're like this. Personally, I think my brain short-circuited.\""

    show dylan grin

    "Dylan chuckled."
    "We stayed like that for a while longer, enjoying each other's company."

    show dylan surprisebl 

    "Eventually, I wriggled out of his hug and reached for his laptop again. Dylan's sudden blush was cute — I grinned, which only made him blush more."
    "But I didn't want to make him uncomfortable, so I pulled his computer into my lap instead."

    show dylan fr 

    r sm "\"Make a guess. You think it'll show menstrual cramps as the answer?\""

    "Dylan peered at the screen as I hovered the Submit button."

    d sm "\"Yeah. I'm going to bet on my own program being right.\""

    r smirk "\"Let's find out.\""

    "I clicked the Submit button. It took several seconds for the screen to refresh."

    r fr "\"\'1) Menstrual cramps. 2) Food poisoning. 3) Kidney stone.\'\""
    r surprise "Wow. It was right."

    d grin "\"Nice!\""
    d smirk "\"I don't know how I feel about kidney stones being up there. Maybe I need to tweak the weights again.\""

    "I laughed."

    hide dylan

    "Eventually, Dylan needed to leave to finish grading exams."

    r surprisebl "(That's probably for the best — I haven't done anything productive all day.)"

    "I washed his lunchbox and handed it to him as he was putting on his shoes at the door."

    r grin "\"Thanks again for bringing me lunch.\""

    show dylan sm at centerpos with dissolve

    d sm "\"Don't worry about it. I'm glad you liked it.\""

    "A moment of silence passed between us. Dylan was biting his lip again."

    d frbl "\"Uhm… Could you come here for a second?\""

    r smirk "(Oh, he decided to say it after all.)"
    r smbl "(I feel like I'm learning how to read his expressions, little by little.)"

    "I took a step towards him. Dylan ducked down and kissed my forehead."

    show dylan smbl

    r surprise "(His face is bright red.)"
    r smbl "(Cute.)"

    d surprisebl "\"OkayI'mgoingnow—\""

    "He nearly ran into the door in his hurry to turn around. This time, I laughed."

    r smbl "\"Have a safe trip home.\""

    jump done_dylan_visit




# ELSE IF "Is that your ploy to find out where I live?"

label dylan_no_visit:

    $ DYLAN_KISS = False

    r fr "<is that your ploy to find out where i live?>"

    d surprise "<Ah.>"
    d "<I didn't realize that would make you uncomfortable.>"
    d fr "<That makes sense. Sorry about that.>"
    d "<You should ask another friend, or order delivery. Just make sure you eat something today.>"

    "I hesitated."

    r sus "(I'd actually just been meaning to tease him…)"

    "But thinking about it now, it did make me feel more comfortable not to share my address with anyone, even him."

    r "(Maybe I'm paranoid. I don't want anyone to know where I live, though.)"

    "I moved to text him back."

    r sm "<thanks>"
    r "<and thank you for asking anyway, it was very considerate of you to offer>"

    "His response was almost immediate."

    d sm "<No problem. I hope you feel better soon.>"

    "I glanced at my phone's other notifications."
    "I didn't really want to deal with Anderson right now, but I was already wide awake. I reluctantly clicked on the messages."

    a surprise "<hey, you haven't really been that involved with arrests recently so i want to fill you in on what's happening this week>"
    a an "<i'm gonna be part of a pretty big arrest on wednesday. it's for a guy with a couple of homicide charges against him. not really your usual forte, but i figured you should know because the arrest is happening close to your workplace>"

    "I tensed up, which was a mistake, because my cramps immediately flared up again."

    r an "\"Ow…!\""


    "I took several shallow breaths, gasping through the pain."
    "Black spots danced in my vision. I dropped my phone and tried to relax. Breathe. Breathe…"
    "After what felt like minutes later, the pain finally subsided to a low rumble."

    r sus "\"Ugh…\""

    "Sweat had beaded up on my forehead and trickled down into my pillow."
    "I picked up my phone again, trying to ignore the dampness of my pillow and pain in my abdomen."

    a fr "<it's the old building right next to your library>"
    a sus "<we're gonna smoke him out, figuratively>"
    a "<the bosses think it'll go fine but i'm sus because arson is in his list of charges. don't want him to endanger any civilians before he gets arrested…>"
    a an "<anyway, this isn't public knowledge so you can't tell your coworkers to be on alert, but you should know at least>"
    a "<took us a while to find out enough info to smoke him out, he put some effort into hiding>"
    a fr "<i still think you'd be able to do good if you joined our force and helped with the info team, you find stuff faster than any two of em combined>"

    "I glanced over his messages one more time before responding."

    r fr "<thanks for telling me>"
    r sus "<i don't think i could do anything about that arrest anyway, but i'll stay on alert>"

    "I ignored his implicit question about joining the police and set my phone back on my nightstand."

    r "(Ugh…)"

    "I rolled over and tried to fall back asleep."

    jump done_dylan_visit



label done_dylan_visit:





    return
