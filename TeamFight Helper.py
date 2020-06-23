import pyautogui
import time
import infi.systray

from infi.systray import SysTrayIcon

systray = SysTrayIcon("icon.ico", "icon",)
systray.start()


#def acceptGame():
#    while True:
#        time.sleep(2)#UPDATE SEARCH EVERY 2SECOND
#        if pyautogui.locateOnScreen('images\Accept\Accept.png'):#IF PICTURE IS ON SCREEN -> CLICK
#            #Get the cursor position b4 moving the click
#            x, y = pyautogui.position()
#            pyautogui.click(pyautogui.locateOnScreen('images\Accept\Accept.png'))
#            #Return the cursor to the original position
#            pyautogui.moveTo(x, y)
#            break
#        #IF NOT -> Tell me it is not found yet.
#        else:
#            print('Not found yet...')
#    while True:
#        acceptGame()

def acceptGame():
    #While Image Not Found LOOP.
    while True:
        time.sleep(2)#UPDATE SEARCH EVERY 2SECOND
        if pyautogui.locateOnScreen('images\Champions\Leona.png'):#IF PICTURE IS ON SCREEN -> CLICK
            #Get the cursor position b4 moving the click
            x, y = pyautogui.position()
            pyautogui.click(pyautogui.locateOnScreen('images\Champions\Leona.png'))
            #Return the cursor to the original position
            pyautogui.moveTo(x, y)
            break
        #IF NOT -> Tell me it is not found yet.
        else:
            print('Not found yet...')
while True:
    acceptGame()