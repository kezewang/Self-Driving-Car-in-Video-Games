import keyboard
import time

duration = 5
for i in range(duration):
    time.sleep(1)
    print(duration - i)

keyboard.press('w')
time.sleep(duration)
keyboard.release('w')
