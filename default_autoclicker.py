import time
from threading import Thread
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Listener

start_clicker_button = KeyCode(char='`')

mouse = Controller()
clicking = False

def clicker(): 
    while True: 
        if clicking: 
            mouse.click(Button.right, 1)

        time.sleep(0.0001)

def toggle_event(key): 
    if key == start_clicker_button: 
        global clicking
        clicking = not clicking

key_thread = Thread(target=clicker)
key_thread.start()

with Listener(on_press=toggle_event) as listener: 
    listener.join()