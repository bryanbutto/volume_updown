# Importing packages
import pyautogui as py
import pause


def volumne_updown():
    
    hrs = 6
    # Tries to recognize an image for the number of hours set in the variable hrs above
    def loc(pic):
        x = None
        y=1
        while x == None and y < 60*60*hrs:
            pause.seconds(1)
            y=y+1
            if y % 120==0:
                py.press('volumedown')
                pause.seconds(1)
                py.press('volumeup')
            x = py.locateCenterOnScreen(pic,confidence=0.8,grayscale=True)
        return(x)
    
    p = loc(r'\\bet-c-00046\C$\Users\BUB1BET\OneDrive - Bosch Group\Projects\Python Scripts\images\bosch_yellow.png') # Needs to be the link to the image you are trying to recognize
    pause.seconds(1)
    py.click(p)
    pause.seconds(1)
    
volumne_updown() 
