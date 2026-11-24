"""Shablon uchun oq fondagi 300 dpi to’ldirgich grafikni chizadi."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    tezlik = [i / 20 for i in range(81)]
    kesim_yuzi = 0.02
    sarf = [kesim_yuzi * qiymat for qiymat in tezlik]

    with plt.rc_context({"font.family": "DejaVu Serif", "font.size": 11}):
        fig, ax = plt.subplots(figsize=(6.2, 3.6), layout="constrained")
        ax.plot(tezlik, sarf, color="#2364aa", label="S = 0.02 m²")
        ax.scatter([2], [0.04], color="#b32d2e", zorder=3)
        ax.annotate("(2; 0.04)", (2, 0.04), xytext=(9, -20),
                    textcoords="offset points")
        ax.set(xlabel="Tezlik, m/s", ylabel="Hajmiy sarf, m³/s",
               xlim=(0, 4), ylim=(0, 0.085))
        ax.grid(alpha=0.25)
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.21),
                  frameon=False)
        fig.savefig(Path(__file__).with_suffix(".png"), dpi=300,
                    facecolor="white")
        plt.close(fig)


if __name__ == "__main__":
    main()
