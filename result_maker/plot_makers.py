import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List

from variables import *

plt.rcParams['figure.figsize'] = [16, 9]


def make_plot(dfs: Dict, col_name: str, total_time: int = TOTAL_DURATION, log_scale_y: bool = False,
              file_name: str = None, legend: List = None) -> None:

    for i in dfs:
        x = dfs[i]["second"].values.tolist()
        y = dfs[i][col_name].values.tolist()
        plt.plot(x, y, alpha=0.8)

    plt.grid(which="minor", linestyle="--")
    plt.grid(which="major", linestyle="-")
    plt.xlabel("sekunda pomiaru")
    plt.ylabel("wartość parametru {}".format(col_name))

    if legend:
        plt.legend(legend)
    else:
        plt.legend(["UE {}".format(i) for i in dfs])

    if log_scale_y:
        plt.yscale("log")
    plt.xticks(np.arange(0, total_time + 15, 10.0))

    if file_name:
        plt.savefig("./plots/{}.svg".format(file_name))

    plt.show()


def make_combo_plot(dfs: Dict, col_name: str, second_plot: List, total_time: int = TOTAL_DURATION,
                    log_scale_y: bool = False, file_name: str = None) -> None:

    fig, ax1 = plt.subplots()
    for i in dfs:
        x = dfs[i]["second"].values.tolist()
        y = dfs[i][col_name].values.tolist()
        ax1.plot(x, y, alpha=0.8)

    ax2 = ax1.twinx()
    ax2.plot(np.arange(0, len(second_plot)/2, 0.5), second_plot, color='k')

    ax1.grid(which="major", linestyle="-")
    ax2.grid(which="major", linestyle="--", color="r")

    ax1.set_xlabel("sekunda pomiaru")
    ax1.set_ylabel("wartość parametru {}".format(col_name))
    # ax2.set_ylabel("procentowe wykorzystanie CPU przez gNodeB (czarny kolor)", color="r")
    ax2.set_ylabel("zużycie RAM w MB przez gNodeB (czarny kolor)", color="r")

    ax1.legend(["UE {}".format(i) for i in dfs])

    if log_scale_y:
        ax1.set_yscale("log")
    ax1.set_xticks(np.arange(0, total_time + 15, 10.0))

    if file_name:
        plt.savefig("./plots/{}.svg".format(file_name))

    plt.show()

def make_combo_plot_double(dfs: Dict, col_name: str, second_plot: List, third_plot: List, total_time: int = TOTAL_DURATION,
                    log_scale_y: bool = False, file_name: str = None) -> None:

    fig, ax1 = plt.subplots()
    for i in dfs:
        x = dfs[i]["second"].values.tolist()
        y = dfs[i][col_name].values.tolist()
        ax1.plot(x, y, alpha=0.8)

    ax2 = ax1.twinx()
    ax2.plot(np.arange(0, len(second_plot)/2, 0.5), second_plot, color='k', alpha=0.7)
    ax2.plot(np.arange(0, len(third_plot)/2, 0.5), third_plot, color='k', linestyle='--', alpha=0.7)

    ax1.grid(which="major", linestyle="-")
    ax2.grid(which="major", linestyle="--", color="r")

    ax1.set_xlabel("sekunda pomiaru")
    ax1.set_ylabel("wartość parametru {}".format(col_name))
    ax2.set_ylabel("procentowe wykorzystanie CPU przez gNodeB (czarna linia)", color="r")
    # ax2.set_ylabel("zużycie RAM w MB", color="r")

    ax1.legend(["UE {}".format(i) for i in dfs])
    ax2.legend(["gNodeB_1", "gNodeB_2"], loc=4)

    if log_scale_y:
        ax1.set_yscale("log")
    ax1.set_xticks(np.arange(0, total_time + 15, 10.0))

    if file_name:
        plt.savefig("./plots/{}.svg".format(file_name))

    plt.show()


def make_plot_pretty(dfs: Dict, col_name: str, total_time: int = TOTAL_DURATION, log_scale_y: bool = False,
                     file_name: str = None, legend: List = None, custom_xlabel: str = None,
                     custom_ylabel: str = None, draw_intervals: bool = False, interval_alpha=0.05) -> None:

    for i in dfs:
        x = dfs[i]["second"].values.tolist()
        y = dfs[i][col_name].values.tolist()
        plt.plot(x, y, alpha=1, label="UE_{}".format(i))
        if draw_intervals:
            plt.fill_between(x, dfs[i][col_name + "_lower"].values.tolist(),
                             dfs[i][col_name + "_upper"].values.tolist(),
                             alpha=interval_alpha, color='0.0', label="_hidden")

    plt.grid(which="minor", linestyle="--")
    plt.grid(which="major", linestyle="-")

    if custom_xlabel:
        plt.xlabel(custom_xlabel)
    else:
        plt.xlabel("sekunda pomiaru")

    if custom_ylabel:
        plt.ylabel(custom_ylabel)
    else:
        plt.ylabel("wartość parametru {}".format(col_name))

    if legend:
        plt.legend(legend)
    else:
        plt.legend()

    if log_scale_y:
        plt.yscale("log")
    plt.xticks(np.arange(0, total_time + 15, 10.0))

    plt.ylim(bottom=0)

    if file_name:
        plt.savefig("./plots/{}.svg".format(file_name))

    plt.show()
