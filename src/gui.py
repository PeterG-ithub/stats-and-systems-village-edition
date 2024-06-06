import tkinter as tk
from tkinter import ttk


class GUI:
    def __init__(self, window, data) -> None:
        self.window = window
        self.data = data
        self.window.title("Stats and Systems: Village Edition")
        self.create_tabs()
        self.create_human_tab()
        self.create_village_tab()

    def create_tabs(self) -> None:
        self.tab_control = ttk.Notebook(self.window)
        self.tab_control.pack(fill="both", expand=True)
        self.human_tab = ttk.Frame(self.tab_control)
        self.village_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.human_tab, text="Human")
        self.tab_control.add(self.village_tab, text="Village")

    def create_human_tab(self) -> None:
        self.human_info_frame = tk.LabelFrame(
            self.human_tab, text="Information")
        self.human_info_frame.grid(
            row=0, column=0, padx=15, pady=10, sticky="news")

        human_information = self.data["human_information"]

        for i, (info_name, info_value) in enumerate(human_information.items()):
            label = tk.Label(self.human_info_frame, text=f"{info_name}: ")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            value_label = tk.Label(self.human_info_frame, text=info_value)
            value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        # # Human Stats Frame
        self.human_stats_frame = tk.LabelFrame(self.human_tab, text="Stats")
        self.human_stats_frame.grid(
            row=1, column=0, padx=15, pady=10, sticky="news")

        human_stats = self.data["human_stats"]
        # Create labels for human stats
        for i, (stat_name, stat_value) in enumerate(human_stats.items()):
            row = i // 2
            col = (i % 2) * 2

            label = tk.Label(self.human_stats_frame, text=f"{stat_name}: ")
            label.grid(row=row, column=col, padx=5, pady=5, sticky="e")

            value_label = tk.Label(self.human_stats_frame, text=stat_value)
            value_label.grid(
                row=row,
                column=col + 1,
                padx=10,
                pady=5,
                sticky="w")

    def create_village_tab(self) -> None:
        # Village Information Frame
        self.village_info_frame = tk.LabelFrame(
            self.village_tab, text="Information")
        self.village_info_frame.grid(
            row=0, column=0, padx=15, pady=10, sticky="news")

        # Define village information
        village_information = self.data["village_information"]

        # Create labels for village information
        for i, (info_name, info_value) in enumerate(
                village_information.items()):
            label = tk.Label(self.village_info_frame, text=f"{info_name}: ")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

            value_label = tk.Label(self.village_info_frame, text=info_value)
            value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        # Village Stats Frame
        self.village_stats_frame = tk.LabelFrame(
            self.village_tab, text="Stats")
        self.village_stats_frame.grid(
            row=1, column=0, padx=15, pady=10, sticky="news")

        # Define village stats
        village_stats = self.data["village_stats"]
        # Create labels for village stats
        for i, (stat_name, stat_value) in enumerate(village_stats.items()):
            label = tk.Label(self.village_stats_frame, text=f"{stat_name}: ")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")

            value_label = tk.Label(self.village_stats_frame, text=stat_value)
            value_label.grid(row=i, column=1, padx=10, pady=5, sticky="w")


def create_gui(data):
    window = tk.Tk()
    app = GUI(window, data)
    window.mainloop()
