import tkinter as tk
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pygetwindow as gw
import threading
import time

controller = Controller()
is_running = False

def get_roblox_window():
    windows = gw.getWindowsWithTitle('Roblox')
    return windows[0] if windows else None

def click_e_key():
    global is_running
    while is_running:
        roblox_window = get_roblox_window()
        if roblox_window and roblox_window.isActive:
            controller.press('e')
            controller.release('e')
            time.sleep(0.051)
        else:
            time.sleep(0.1)

def toggle_start():
    global is_running
    is_running = True
    status_label.config(text="상태: 작동중", fg="green")
    threading.Thread(target=click_e_key, daemon=True).start()

def toggle_stop():
    global is_running
    is_running = False
    status_label.config(text="상태: 비작동", fg="red")

def on_press(key):
    try:
        if key == keyboard.Key.f5:
            toggle_start()
        elif key == keyboard.Key.f6:
            toggle_stop()
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

root = tk.Tk()
root.title("Roblox E키 매크로")
root.geometry("300x150")
root.resizable(False, False)

status_label = tk.Label(root, text="상태: 비작동", fg="red", font=("Arial", 12, "bold"))
status_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text="작동 (F5)", command=toggle_start, bg="green", fg="white", width=15, height=2)
start_btn.pack(side=tk.LEFT, padx=5)

stop_btn = tk.Button(button_frame, text="비작동 (F6)", command=toggle_stop, bg="red", fg="white", width=15, height=2)
stop_btn.pack(side=tk.LEFT, padx=5)

info_label = tk.Label(root, text="단축키: F5(시작) F6(중지)", font=("Arial", 9))
info_label.pack(pady=5)

root.mainloop()
