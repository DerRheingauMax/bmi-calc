import tkinter as tk

root=tk.Tk()
root.title("Bmi-Rechner")



weight_label = tk.Label(root, bg="lightgrey", text="Bitte geben Sie ihr Gewicht in kg an: ")
weight_label.grid()


weight_entry = tk.Entry(root, bg="lightgrey")
weight_entry.grid()


height_label = tk.Label(root, bg="lightgrey", text=" Jetzt ihr Gewicht")
height_label.grid()

height_entry = tk.Entry(root, bg="lightgrey")
height_entry.grid()

bmi_button = tk.Button(root, bg="lightgreen", text="Jetzt prüfen")
bmi_button.grid()

root.mainloop()






#gew= float(input("Bitte sewicht"))
