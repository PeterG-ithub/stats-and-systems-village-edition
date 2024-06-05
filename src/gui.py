import tkinter as tk
from tkinter import ttk

# Create main window
window = tk.Tk()
window.title("Stats and Systems: Village Edition")

# Create tabs
tab_control = ttk.Notebook(window)
tab_control.pack(fill="both", expand=True)

human_tab = ttk.Frame(tab_control)
village_tab = ttk.Frame(tab_control)

tab_control.add(human_tab, text="Human")
tab_control.add(village_tab, text="Village")

# Human Information Frame
human_info_frame = tk.LabelFrame(human_tab, text="Information")
human_info_frame.grid(row=0, column=0, padx=15, pady=10, sticky="news")

# Define human information
human_information = {
    "Name": "Robert Skywalker",
    "Age": 30,  # Example age
}

# Create labels for human information
for i, (info_name, info_value) in enumerate(human_information.items()):
    label = tk.Label(human_info_frame, text=f"{info_name}: ")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    value_label = tk.Label(human_info_frame, text=info_value)
    value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

# Human Stats Frame
human_stats_frame = tk.LabelFrame(human_tab, text="Stats")
human_stats_frame.grid(row=1, column=0, padx=15, pady=10, sticky="news")

# Define human stats
human_stats = {
    "Strength (STR)": 10,
    "Dexterity (DEX)": 8,
    "Constitution (CON)": 12,
    "Intelligence (INT)": 15,
    "Wisdom (WIS)": 13,
    "Charisma (CHA)": 11
}

# Create labels for human stats
for i, (stat_name, stat_value) in enumerate(human_stats.items()):
    row = i // 2
    col = (i % 2) * 2

    label = tk.Label(human_stats_frame, text=f"{stat_name}: ")
    label.grid(row=row, column=col, padx=5, pady=5, sticky="e")

    value_label = tk.Label(human_stats_frame, text=stat_value)
    value_label.grid(row=row, column=col+1, padx=10, pady=5, sticky="w")

# Village Information Frame
village_info_frame = tk.LabelFrame(village_tab, text="Information")
village_info_frame.grid(row=0, column=0, padx=15, pady=10, sticky="news")

# Define village information
village_information = {
    "Population": 80,
    "Birth Rate": "5 births per 80 people per year",
    "Death Rate": "2 deaths per 80 people per year",
    "Location": "Golden Valley of Sands"
}

# Create labels for village information
for i, (info_name, info_value) in enumerate(village_information.items()):
    label = tk.Label(village_info_frame, text=f"{info_name}: ")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    value_label = tk.Label(village_info_frame, text=info_value)
    value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

# Village Stats Frame
village_stats_frame = tk.LabelFrame(village_tab, text="Stats")
village_stats_frame.grid(row=1, column=0, padx=15, pady=10, sticky="news")

# Define village stats
village_stats = {
    "Wealth": "Moderate",
    "Resources": ["Food", "Wood", "Stone"],
    "Defense Level": "Low",
    "Happiness": "High"
}

# Create labels for village stats
for i, (stat_name, stat_value) in enumerate(village_stats.items()):
    label = tk.Label(village_stats_frame, text=f"{stat_name}: ")
    label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

    value_label = tk.Label(village_stats_frame, text=stat_value)
    value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

window.mainloop()
