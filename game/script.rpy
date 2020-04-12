
##### Declare images used by this game. #####

## Character Sprites ##

image side robin angry = "robin_angry.png"
image side robin frown = "robin_frown.png"
image side robin frownblush = "robin_frown_blush.png"
image side robin grin = "robin_grin.png"
image side robin smile = "robin_smile.png"
image side robin smileblush = "robin_smile_blush.png"
image side robin smirk = "robin_smirk.png"
image side robin surprise = "robin_surprise.png"
image side robin surpriseblush = "robin_surprise_blush.png"
image side robin sus = "robin_suspicious.png"

image dylan angry = "dylan_angry.png"
image side dylan angry = "dylan_s_angry.png"
image dylan frown = "dylan_frown.png"
image side dylan frown = "dylan_s_frown.png"
image dylan frownblush = "dylan_frown_blush.png"
image side dylan frownblush = "dylan_s_frown_blush.png"
image dylan grin = "dylan_grin.png"
image side dylan grin = "dylan_s_grin.png"
image dylan smile = "dylan_smile.png"
image side dylan smile = "dylan_s_smile.png"
image dylan smirk = "dylan_smirk.png"
image side dylan smirk = "dylan_s_smirk.png"
image dylan surprise = "dylan_surprise.png"
image side dylan surprise = "dylan_s_surprise.png"
image dylan sus = "dylan_suspicious.png"
image side dylan sus = "dylan_s_suspicious.png"

image anderson angry = "anderson_angry.png"
image side anderson angry = "anderson_s_angry.png"
image anderson frown = "anderson_frown.png"
image side anderson frown = "anderson_s_frown.png"
image anderson smile = "anderson_smile.png"
image side anderson smile = "anderson_smile.png"
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
image bg street = "bg_street_night.png"


## Character Graphics ##

# image cg owenkiss = "CG_owen_kiss.png"


##### Declare characters used by this game. #####

define r = Character("{b}Robin{/b}", image="robin", color="#000000")
define d = Character("{b}Dylan{/b}", image="dylan", color="#000000")
define a = Character("{b}Anderson{/b}", image="anderson", color="#000000")


##### Initiate variables used in this game. #####

init python:
    # config.side_image_tag = "junia"
    _preferences.set_volume('music', 0.3)

init:
    $ centerpos = Position(xpos=0.40, xanchor=0)        # only used when leftpos and rightpos not in use
    $ leftpos = Position(xpos = 0.30, xanchor=0)
    $ rightpos = Position(xpos = 0.60, xanchor=0)
    
    # $ owenaffection = 0               # if below 4 (out of 6) by final scene, choice to go with Owen doesn't appear



##### Start the game. #####

label start:

    scene bg conferencehall with fade
    stop music fadeout 1.0
    pause(0.5)

    r frown "\"...\""

    # testing side image sprites showing up with full body ones
    show dylan smirk at centerpos with dissolve

    d smirk "\"testing lmao\""

    r frown "\"no u\""
    r "\"is this showing up with my face\""

    d smirk "\"it's my face now\""

    hide dylan
    show dylan smirk at rightpos with dissolve
    show anderson suspicious at leftpos with dissolve

    a sus "\"y'all are weird\""
    
    # play music "BGM_suspicious.mp3" fadein 1.0 fadeout 1.0 loop

    # show ogeneric frown at centerpos with dissolve
    pause(0.5)

    # j surprise "\"AHHHH—\""
    
    # show ogeneric surprise 

    return
