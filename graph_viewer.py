import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import pandas as pd
from pathlib import Path

csv_files = sorted(Path('.').rglob('*_data.csv'))
current_idx = 0

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.2)

def plot_data(idx):
    ax.clear()
    df = pd.read_csv(csv_files[idx])
    ax.plot(df.iloc[:, 0], df.iloc[:, 1])
    ax.set_title(csv_files[idx].stem)
    ax.set_xlabel(df.columns[0])
    ax.set_ylabel(df.columns[1])
    ax.grid(True)
    plt.draw()

def next_plot(event):
    global current_idx
    current_idx = (current_idx + 1) % len(csv_files)
    plot_data(current_idx)

def prev_plot(event):
    global current_idx
    current_idx = (current_idx - 1) % len(csv_files)
    plot_data(current_idx)

ax_prev = plt.axes([0.3, 0.05, 0.15, 0.075])
ax_next = plt.axes([0.55, 0.05, 0.15, 0.075])
btn_prev = Button(ax_prev, 'Back')
btn_next = Button(ax_next, 'Forward')
btn_prev.on_clicked(prev_plot)
btn_next.on_clicked(next_plot)

plot_data(current_idx)
plt.show()
