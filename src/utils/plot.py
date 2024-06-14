import matplotlib.pyplot as plt


def plot_state_counter(state_counter):
    activities = list(state_counter.keys())
    counts = list(state_counter.values())
    plt.figure(figsize=(8, 5))
    plt.bar(activities, counts, color=['blue', 'orange', 'green'])
    plt.xlabel("Activities")
    plt.ylabel("Count")
    plt.title("State Counts over 24 Hours")
    plt.show()