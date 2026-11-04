"""Rebuild the paper's three-mode CUDA Graph throughput comparison.

Data copied from the ADASS Alive talk's images/starspin_two_buffer_throughput.csv.
Run with Python and Matplotlib; paths are relative to this script.
"""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


directory = Path(__file__).resolve().parent
with (directory / "C802_throughput.csv").open(newline="") as source:
    rows = {row["configuration"]: row for row in csv.DictReader(source)}

configurations = ["Weights only", "Coarse, protected", "Fine, protected"]
selected = [rows[name] for name in configurations]
medians = [float(row["graph_median"]) for row in selected]
lower = [median - float(row["graph_min"]) for median, row in zip(medians, selected)]
upper = [float(row["graph_max"]) - median for median, row in zip(medians, selected)]
assert all(int(row["gpu_buffers"]) == 2 for row in selected)
assert all(error >= 0 for error in lower + upper)

plt.rcParams.update({"font.size": 10, "pdf.fonttype": 42})
fig, ax = plt.subplots(figsize=(7.3, 2.35), layout="constrained")
ax.barh(
    range(3), medians, height=0.52,
    color=["#777777", "#0072B2", "#0072B2"],
    xerr=[lower, upper],
    error_kw={"ecolor": "black", "capsize": 3, "elinewidth": 1},
)
ax.set_yticks(range(3), ["Weights-only", "Coarse", "Fine"])
ax.invert_yaxis()
ax.set_xlim(0, 13)
ax.set_xlabel("Input payload throughput (GB/s)")
ax.set_axisbelow(True)
ax.grid(axis="x", color="0.88", linewidth=0.6)
ax.tick_params(axis="y", length=0)
ax.spines[["top", "right", "left"]].set_visible(False)
for index, (median, row) in enumerate(zip(medians, selected)):
    ax.text(float(row["graph_max"]) + 0.12, index, f"{median:.3f}", va="center", fontsize=9)
fig.savefig(directory / "starspin_two_buffer_throughput.pdf")
plt.close(fig)
