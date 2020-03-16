
##### Declare images used by this game. #####

image side robin neutral = "robin_neutral.png"

image dylan neutral = "dylan_neutral.png"
image side dylan neutral = "dylan_s_neutral.png"

# image bg lakesideday = "BG_lakeside_day.png"

# image cg owenkiss = "CG_owen_kiss.png"


##### Declare characters used by this game. #####

define r = Character("{b}Robin{/b}", image="robin", color="#000000")
define d = Character("{b}Dylan{/b}", image="dylan", color="#000000")


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

    # scene bg black with fade
    stop music fadeout 1.0
    pause(0.5)

    r neutral "\"...\""

    # testing side image sprites showing up with full body ones
    show dylan neutral at centerpos with dissolve

    d neutral "\"testing lmao\""

    r neutral "\"no u\""
    r "\"is this showing up with my face\""

    d neutral "\"it's my face now\""
    
    # play music "BGM_suspicious.mp3" fadein 1.0 fadeout 1.0 loop

    # show ogeneric frown at centerpos with dissolve
    pause(0.5)
    
    "A dark shadow loomed over me, blocking the moonlight from my window."

    # j surprise "\"AHHHH—\""
    
    # show ogeneric surprise 

    return
