
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



##### Initiate variables used in this game. #####

init python:
    _preferences.set_volume('music', 0.3)

init:
    $ centerpos = Position(xpos=0.40, xanchor=0)        # only used when leftpos and rightpos not in use
    $ leftpos = Position(xpos = 0.30, xanchor=0)
    $ rightpos = Position(xpos = 0.60, xanchor=0)
    
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








    
    pause(0.5)


    return
