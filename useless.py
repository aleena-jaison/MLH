import tkinter as tk
from tkinter import ttk

def update_dots():
    global dot_count
    dot_count = (dot_count + 1) % 4  
    dots = '.' * dot_count 
    label.config(text=f"Still Loading{dots} Please Wait.")
    window.after(500, update_dots)  # Update every 500 milliseconds

window = tk.Tk()
window.title("Infinite Loading Simulator")
window.configure(bg="grey")
label = tk.Label(window, text="Still Loading... Please Wait.", font=("Helvetica", 20), bg="grey")
label.pack(pady=20)

spinner = ttk.Progressbar(window, mode="indeterminate")
spinner.pack(pady=20)
spinner.start()
dot_count = 0
update_dots()
window.mainloop()
