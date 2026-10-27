import time
import tkinter as tk
from tkinter import ttk


class ClockApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Clock and Stopwatch")
		self.root.resizable(False, False)

		self.stopwatch_elapsed = 0.0
		self.stopwatch_started_at = None

		content = ttk.Frame(root, padding=24)
		content.grid()

		ttk.Label(content, text="CLOCK", font=("Helvetica", 11, "bold")).grid(
			row=0, column=0, pady=(0, 4)
		)
		self.clock_label = ttk.Label(content, font=("Helvetica", 36))
		self.clock_label.grid(row=1, column=0, pady=(0, 20))

		ttk.Separator(content).grid(row=2, column=0, sticky="ew", pady=(0, 18))

		ttk.Label(content, text="STOPWATCH", font=("Helvetica", 11, "bold")).grid(
			row=3, column=0, pady=(0, 4)
		)
		self.stopwatch_label = ttk.Label(content, text="00:00:00.0", font=("Helvetica", 30))
		self.stopwatch_label.grid(row=4, column=0, pady=(0, 16))

		buttons = ttk.Frame(content)
		buttons.grid(row=5, column=0)
		self.start_button = ttk.Button(buttons, text="Start", command=self.toggle_stopwatch)
		self.start_button.grid(row=0, column=0, padx=4)
		ttk.Button(buttons, text="Reset", command=self.reset_stopwatch).grid(
			row=0, column=1, padx=4
		)

		self.update_clock()
		self.update_stopwatch()

	def update_clock(self):
		self.clock_label.configure(text=time.strftime("%H:%M:%S"))
		self.root.after(200, self.update_clock)

	def update_stopwatch(self):
		elapsed = self.stopwatch_elapsed
		if self.stopwatch_started_at is not None:
			elapsed += time.perf_counter() - self.stopwatch_started_at

		tenths = int(elapsed * 10)
		hours, remainder = divmod(tenths, 36_000)
		minutes, remainder = divmod(remainder, 600)
		seconds, tenths = divmod(remainder, 10)
		self.stopwatch_label.configure(
			text=f"{hours:02}:{minutes:02}:{seconds:02}.{tenths}"
		)
		self.root.after(50, self.update_stopwatch)

	def toggle_stopwatch(self):
		if self.stopwatch_started_at is None:
			self.stopwatch_started_at = time.perf_counter()
			self.start_button.configure(text="Pause")
		else:
			self.stopwatch_elapsed += time.perf_counter() - self.stopwatch_started_at
			self.stopwatch_started_at = None
			self.start_button.configure(text="Start")

	def reset_stopwatch(self):
		self.stopwatch_elapsed = 0.0
		if self.stopwatch_started_at is not None:
			self.stopwatch_started_at = time.perf_counter()
		else:
			self.stopwatch_label.configure(text="00:00:00.0")


if __name__ == "__main__":
	window = tk.Tk()
	ClockApp(window)
	window.mainloop()
