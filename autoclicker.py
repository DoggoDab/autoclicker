# another file for setting up your precious autoclicker :)

import time
from threading import Thread
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener

print("Suggested Key Code: `")
toggle_key = str(input("Enter your toggle key: ")).strip().lower()
if len(toggle_key) == 1: 
    start_click_button = KeyCode(char=toggle_key)

    mouse = Controller()
    clicking = False

    def clicker(): 
        cps = int(input("Enter clicks: "))
        seconds = float(input("Enter seconds: "))
        while True: 
            if clicking: 
                mouse.click(Button.right, cps)
            time.sleep(seconds)

    def toggle_event(key): 
        if key == start_click_button:
            global clicking
            clicking = not clicking

    key_thread = Thread(target=clicker)
    key_thread.start()

    with Listener(on_press=toggle_event) as listener: 
        listener.join()

else: 
    raise ValueError("Must enter only one character!")