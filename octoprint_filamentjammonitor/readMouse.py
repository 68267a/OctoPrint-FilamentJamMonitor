#https://docs.octoprint.org/en/master/plugins/mixins.html#progressplugin
from pynput import mouse
import time

counter = 0
threshold = 100
timer = 10

def on_move(x, y):
    #print('Pointer moved to {0}'.format((x, y)))
    global counter, threshold
    counter+=1

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed: #I think this will hurt later
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)

try:
    listener.start()
    time.sleep(timer)
    listener.stop
except Exception as e:
    print(e)

if counter > threshold:
    print("reached threshold " + str(counter)+"/"+str(threshold))
else:
    raise RuntimeError("Did not reach threshold " + str(counter)+"/"+str(threshold))
