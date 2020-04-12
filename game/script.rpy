
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

define r = Character("{b}Robin{/b}", image="robin", color="#000000")
define d = Character("{b}Dylan{/b}", image="dylan", color="#000000")
define a = Character("{b}Anderson{/b}", image="anderson", color="#000000")

define m = Character("{b}A Man{/b}", image="dylan", color="#000000")
define c = Character("{b}Cassidy{/b}", color="#000000")
define u = Character("{b}Unknown Man{/b}", color="#000000")



##### Initiate variables used in this game. #####

init python:
    _preferences.set_volume('music', 0.3)

init:
    $ centerpos = Position(xpos=0.40, xanchor=0)        # only used when leftpos and rightpos not in use
    $ leftpos = Position(xpos = 0.30, xanchor=0)
    $ rightpos = Position(xpos = 0.60, xanchor=0)

    $ CASSIDY_ARRESTED = False
    
    # $ owenaffection = 0               # if below 4 (out of 6) by final scene, choice to go with Owen doesn't appear



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














    return
