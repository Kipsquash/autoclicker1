import keyboard
import pyautogui as pag
import time

# Set the key to start/stop the autoclicker
toggle_key = 'f'
click_delay = 0.01  # Delay between clicks in seconds
running = False

def toggle_autoclicker():
    global running
    running = not running
    if running:
        print("Autoclicker started.")
    else:
        print("Autoclicker stopped.")

# Listen for the toggle key
keyboard.add_hotkey(toggle_key, toggle_autoclicker)

try:
    while True:
        if running:
            pag.click()  # Simulate a left click
            time.sleep(click_delay)  # Wait for the specified delay
except KeyboardInterrupt:
    print("Autoclicker terminated.")
