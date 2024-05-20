import tkinter as tk
import random
from datetime import datetime

class TimeReactionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Reaction Game")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.circles = []
        self.current_circle_index = 0

        self.start_time = None
        self.end_time = None

        self.status_label = tk.Label(root, text="Wait for the circles to turn green...")
        self.status_label.pack()

        self.stop_button = tk.Button(
            root, text="STOP", command=self.stop_timer, state=tk.DISABLED,
            bg="red", fg="white", font=("Helvetica", 16, "bold"),
            width=10, height=2
        )
        self.stop_button.pack(pady=20)

        self.root.after(500, self.show_next_circle)

    def show_next_circle(self):
        if self.current_circle_index < 5:
            circle = self.canvas.create_oval(
                50 + self.current_circle_index * 100, 150,
                100 + self.current_circle_index * 100, 200, fill="red"
            )
            self.circles.append(circle)
            self.current_circle_index += 1
            self.root.after(500, self.show_next_circle)
        else:
            delay = random.randint(1000, 3000)
            self.root.after(delay, self.turn_circles_green)

    def turn_circles_green(self):
        for circle in self.circles:
            self.canvas.itemconfig(circle, fill="green")

        self.start_time = datetime.now()
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Press 'STOP' as fast as you can!")

    def stop_timer(self):
        self.end_time = datetime.now()
        reaction_time = (self.end_time - self.start_time).total_seconds()
        self.status_label.config(text=f"Your reaction time: {reaction_time:.3f} seconds")
        self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TimeReactionGame(root)
    root.mainloop()
