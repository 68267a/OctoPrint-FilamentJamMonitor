#https://docs.octoprint.org/en/master/plugins/mixins.html#progressplugin
from pynput import mouse
import time

counter = 0
limit = 100

def on_move(x, y):
    #print('Pointer moved to {0}'.format((x, y)))
    global counter, limit
    counter+=1
    print(counter)
    if counter > limit:
        return True

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

print(counter)
# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
time.sleep(15)
Listener.stop

print("did not detect sufficient movement.")