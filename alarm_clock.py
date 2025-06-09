import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
import time
import threading
import os
import pygame

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x300")

        self.alarm_time = None
        self.alarm_running = False
        self.alarm_thread = None
        self.tone_path = None

        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Set Alarm (HH:MM:SS):").pack(pady=10)
        self.time_entry = tk.Entry(self.root, font=("Arial", 14))
        self.time_entry.pack()

        tk.Button(self.root, text="Choose Alarm Tone", command=self.choose_tone).pack(pady=5)
        self.tone_label = tk.Label(self.root, text="No tone selected", fg="gray")
        self.tone_label.pack()

        tk.Button(self.root, text="Set Alarm", command=self.set_alarm).pack(pady=10)
        tk.Button(self.root, text="Stop Alarm", command=self.stop_alarm).pack()

        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.pack(pady=10)

    def choose_tone(self):
        path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if path:
            self.tone_path = str(path)
            self.tone_label.config(text=os.path.basename(self.tone_path), fg="black")

    def set_alarm(self):
        time_str = self.time_entry.get()
        try:
            self.alarm_time = datetime.strptime(time_str, "%H:%M:%S").time()
            self.status_label.config(text=f"Alarm set for {self.alarm_time}")
            if not self.alarm_thread or not self.alarm_thread.is_alive():
                self.alarm_running = True
                self.alarm_thread = threading.Thread(target=self.check_alarm)
                self.alarm_thread.start()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format.")

    def check_alarm(self):
        while self.alarm_running:
            now = datetime.now().time()
            if now >= self.alarm_time:
                self.trigger_alarm()
                break
            time.sleep(1)

    def trigger_alarm(self):
        def play_and_prompt():
            try:
                tone = self.tone_path if self.tone_path else os.path.join(os.path.dirname(__file__), "alarm.mp3")
                tone = os.path.abspath(tone)
                print(f"DEBUG: Playing tone at path: {tone}")
                pygame.mixer.music.load(tone)
                pygame.mixer.music.play()

                # Wait for the sound to finish
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)

            except Exception as e:
                messagebox.showerror("Error", f"Could not play sound:\n{e}")

            self.prompt_snooze()

        threading.Thread(target=play_and_prompt).start()

    def prompt_snooze(self):
        result = messagebox.askyesno("Alarm", "Snooze for 5 minutes?")
        if result:
            snooze_time = datetime.now() + timedelta(minutes=5)
            self.alarm_time = snooze_time.time()
            self.status_label.config(text=f"Snoozed until {self.alarm_time}")
            self.alarm_thread = threading.Thread(target=self.check_alarm)
            self.alarm_thread.start()
        else:
            self.stop_alarm()

    def stop_alarm(self):
        self.alarm_running = False
        pygame.mixer.music.stop()
        self.status_label.config(text="Alarm stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
