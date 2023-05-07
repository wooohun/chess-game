import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My Check Box App")

# Create a 90x52 grid of check boxes
checkboxes = []
for i in range(90):
    row = []
    for j in range(52):
        checkbox = tk.Checkbutton(root)
        checkbox.grid(row=j, column=i)
        row.append(checkbox)
    checkboxes.append(row)

# Run the main loop
root.mainloop()