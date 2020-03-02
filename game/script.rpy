
##### Declare images used by this game. #####

# image side junia neutral = "junia_neutral.png"

# image owen smile = "owen_smile.png"

# image bg lakesideday = "BG_lakeside_day.png"

# image cg owenkiss = "CG_owen_kiss.png"


##### Declare characters used by this game. #####

# define j = Character("{b}Junia{/b}", image="junia", color="#9a290e")
# define o = Character("{b}Owen{/b}", image="owen", color="#0c35b6")


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

    # j frown "\"...\""
    
    # play music "BGM_suspicious.mp3" fadein 1.0 fadeout 1.0 loop

    # show ogeneric frown at centerpos with dissolve
    pause(0.5)
    
    "A dark shadow loomed over me, blocking the moonlight from my window."

    # j surprise "\"AHHHH—\""
    
    # show ogeneric surprise 

    return
