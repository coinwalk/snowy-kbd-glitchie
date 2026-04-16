import random
import time
from pynput import keyboard

controller = keyboard.Controller()
PLACEHOLDERS = "abcdefghijklmnopqrstuvwxyz.;,@#!:]["
is_processing = False

def on_press(key):
    global is_processing

    if is_processing:
        return

    if hasattr(key, 'char') and key.char is not None:
        is_processing = True
        
        # Determine a random intensity for this specific glitch
        num_glitches = random.randint(1, 5)
        
        # 1. Type the random noise
        for _ in range(num_glitches):
            controller.tap(random.choice(PLACEHOLDERS))
            time.sleep(0.01) 

        # 2. Visual hang time
        time.sleep(0.04)

        # 3. Delete exactly the amount of noise created
        for _ in range(num_glitches):
            controller.tap(keyboard.Key.backspace)
            time.sleep(0.01)

        is_processing = False

with keyboard.Listener(on_press=on_press, suppress=False) as listener:
    print("Variable Glitch Active. (1-5 chars)")
    listener.join()
