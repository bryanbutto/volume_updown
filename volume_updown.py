# Importing packages
import pyautogui as py
import pause


def volumne_updown():
    
    hrs = 6
    x = 1
    while x < 60*60*hrs:
        pause.seconds(1)
        x = x+1
        py.press('volumedown')
        pause.seconds(1)
        py.press('volumeup')
        pause.seconds(58)
    
volumne_updown()
