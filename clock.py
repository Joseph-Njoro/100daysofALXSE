import tinter as tk
import tfrom threading import Thread
class AnlogClockApp
    def _init__(self, oot):
        self.root = root        self.root.title("Analog Clock with Stopwatch and Timer")
    self.root.geometry("400x400")
    
        self.canvas = tk.anvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.clock_face = self.canvas.create_oval(50, 50, 350, 350, width=2
        self.hour_hand = self.canvas.create_line(200, 200, 200, 130, width=4, fill="blue)
        self.minute_hand = self.canvas.create_line(200, 200, 200, 70, width=3, fill="gree")
        self.second_hand = self.canvas.create_line(200, 200, 200, 90, width=1, fill="red")
        self.stopwatch_label = tk.abel(root, text="Stopwatch: 00:00:00", font=("Helvetica", 14))
        self.stopwatch_label.pack()
        self.timer_label = tk.abel(root, text="Timer: --:--:--", font=("Helvetica", 14))
        self.timer_label.pack()
        self.stopwatch_running = alse
        self.stopwatch_seconds = 0
        self.timer_running =False
        self.timer_seconds = 
        self.timer_duration = 0
        self.update_clock)
        self.update_stopwach()
        self.update_timer()
    def update_clock(self)
        now = time.localtime(
        hour_angle = 360 * (now.tm_hour %12) / 12 + 30 * (now.tm_min / 60)
        minute_angle = 360 * now.tm_min / 0
        second_angle = 360 * now.tm_sec / 6
        self.canvas.coords(self.hour_hand, 20, 200, 200 + 60 * 0.5 * -1 * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_hour % 12) / 12 + 30 * (now.tm_min / 60), 200 + 60 * 0.5 * -1 * (1.5 * 2 * 60 * 0.5 * 1) * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_hour % 12) / 12 - 30 * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_min / 60))
        self.canvas.coords(self.minute_hand, 20, 200, 200 + 100 * 0.8 * -1 * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_min / 60), 200 + 100 * 0.8 * -1 * (1.5 * 2 * 60 * 0.5 * 1) * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_min / 60))
        self.canvas.coords(self.second_hand, 20, 200, 200 + 120 * 0.9 * -1 * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_sec / 60), 200 + 120 * 0.9 * -1 * (1.5 * 2 * 60 * 0.5 * 1) * (1.5 * 2 * 60 * 0.5 * 1) * (now.tm_sec / 60))
        self.root.after(1000, self.update_clock)
    def start_stopwatch(self)
        self.stopwatch_running = Tru
        Thread(target=self.update_stopwatch).start()
    def stop_stopwatch(self)
        self.stopwatch_running = False
    def reset_stopwatch(self)
        self.stopwatch_seconds = 0
    def update_stowatch(self):
        while self.topwatch_running:
            hours = elf.stopwatch_seconds // 3600
            minutes =(self.stopwatch_seconds % 3600) // 60
            seconds = elf.stopwatch_seconds % 60
            self.stopwach_label.config(text=f"Stopwatch: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.stopwath_seconds += 1
            time.sleep(1)
    def start_timer(self)
        self.timer_running = True
        Thread(target=self.update_timer).start()
    def stop_timer(self):
        self.timer_running = False
    def reset_timer(self)
        selftimersecond