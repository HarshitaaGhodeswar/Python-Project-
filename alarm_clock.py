import datetime
import tkinter as tk
from tkinter import messagebox

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("250x150")

        # Create labels and entry fields for hour, minute, and second
        self.hour_label = tk.Label(self.root, text="Hour (24-hour format):")
        self.hour_label.pack()
        self.hour_entry = tk.Entry(self.root, width=5)
        self.hour_entry.pack()

        self.minute_label = tk.Label(self.root, text="Minute:")
        self.minute_label.pack()
        self.minute_entry = tk.Entry(self.root, width=5)
        self.minute_entry.pack()

        self.second_label = tk.Label(self.root, text="Second:")
        self.second_label.pack()
        self.second_entry = tk.Entry(self.root, width=5)
        self.second_entry.pack()

        # Create a button to set the alarm
        self.set_alarm_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack()

        # Create a label to display the current time
        self.current_time_label = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.current_time_label.pack()

        # Update the current time label every second
        self.update_current_time()

        self.root.mainloop()

    def set_alarm(self):
        # Get the hour, minute, and second from the entry fields
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())
        second = int(self.second_entry.get())

        # Create a datetime object for the alarm time
        alarm_time = datetime.datetime.now()
        alarm_time = alarm_time.replace(hour=hour, minute=minute, second=second)

        # Set the alarm
        self.alarm(alarm_time)

    def alarm(self, alarm_time):
        # Wait until the alarm time is reached
        while True:
            current_time = datetime.datetime.now()
            if current_time >= alarm_time:
                # Play an alarm sound (you can use a library like pyaudio or simpleaudio)
                print("Alarm!")
                messagebox.showinfo("Alarm", "Wake up!")
                break

    def update_current_time(self):
        # Update the current time label every second
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=current_time)
        self.root.after(1000, self.update_current_time)

if __name__ == "__main__":
    alarm_clock = AlarmClock()