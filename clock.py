import tkinter as tk
import time
from threading import Thread

class AnalogClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock with Stopwatch and Timer")
        self.root.geometry("400x400")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.clock_face = self.canvas.create_oval(50, 50, 350, 350, width=2)
        self.hour_hand = self.canvas.create_line(200, 200, 200, 130, width=4, fill="blue")
        self.minute_hand = self.canvas.create_line(200, 200, 200, 70, width=3, fill="green")
        self.second_hand = self.canvas.create_line(200, 200, 200, 90, width=1, fill="red")

        self.stopwatch_label = tk.Label(root, text="Stopwatch: 00:00:00", font=("Helvetica", 14))
        self.stopwatch_label.pack()

        self.timer_label = tk.Label(root, text="Timer: --:--:--", font=("Helvetica", 14))
        self.timer_label.pack()

        self.update_clock()
        self.start_stopwatch()
        self.start_timer()

    def update_clock(self):
        now = time.localtime()
        hour_angle = 360 * (now.tm_hour % 12) / 12 + 30 * (now.tm_min / 60)
        minute_angle = 360 * now.tm_min / 60
        second_angle = 360 * now.tm_sec / 60
        self.rotate_hand(self.hour_hand, hour_angle, 50)
        self.rotate_hand(self.minute_hand, minute_angle, 70)
        self.rotate_hand(self.second_hand, second_angle, 90)
        self.root.after(1000, self.update_clock)

    def rotate_hand(self, hand, angle, length):
        angle_rad = angle * (3.14159 / 180)
        end_x = 200 + length * 0.8 * math.cos(angle_rad)
        end_y = 200 + length * 0.8 * math.sin(angle_rad)
        self.canvas.coords(hand, 200, 200, end_x, end_y)

    def start_stopwatch(self):
        self.stopwatch_running = True
        self.stopwatch_seconds = 0
        Thread(target=self.update_stopwatch).start()

    def stop_stopwatch(self):
        self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_seconds = 0

    def update_stopwatch(self):
        while self.stopwatch_running:
            hours = self.stopwatch_seconds // 3600
            minutes = (self.stopwatch_seconds % 3600) // 60
            seconds = self.stopwatch_seconds % 60
            self.stopwatch_label.config(text=f"Stopwatch: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.stopwatch_seconds += 1
            time.sleep(1)

    def start_timer(self):
        self.timer_running = True
        self.timer_seconds = 0
        self.timer_duration = 3600
        Thread(target=self.update_timer).start()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_seconds = 0
        self.timer_duration = 0

    def update_timer(self):
        while self.timer_running:
            if self.timer_seconds >= self.timer_duration:
                self.stop_timer()
                self.timer_label.config(text="Timer: --:--:--")
                return
            remaining_seconds = self.timer_duration - self.timer_seconds
            hours = remaining_seconds // 3600
            minutes = (remaining_seconds % 3600) // 60
            seconds = remaining_seconds % 60
            self.timer_label.config(text=f"Timer: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.timer_seconds += 1
            time.sleep(1)

root = tk.Tk()
app = AnalogClockApp(root)
root.mainloop()