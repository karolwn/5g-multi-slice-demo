import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from typing import Dict, List

NUMBER_OF_UE = 15
TIME_DELAY_BETWEEN_UE = 10
TOTAL_DURATION = 160
SCENARIO_NO = "22_15xUE_UDP_50Mbps_2xSLICE_UE1_25Mbps_IN_BOTH_COMPARE_SLICES"

plt.rcParams['figure.figsize'] = [16, 9]


def main(protocol: str = "udp", no_ue: int = NUMBER_OF_UE, time_spacing: int = TIME_DELAY_BETWEEN_UE,
         total_time: int = TOTAL_DURATION) -> None:
    longest_test = 0
    empty_dfs = []
    dfs = {}
    # for i in range(no_ue):
    #     df = pd.read_csv("./results/parsed_{}_{}_ue_metrics.log".format(protocol, i + 1), sep=";")
    #
    #     if not df.empty:
    #         time_skew = i * time_spacing
    #         df.loc[:, "second"] += time_skew
    #         if protocol == "udp":
    #             df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100
    #         dfs[i + 1] = df
    #         last_point = df["second"].iat[-1]
    #
    #         if last_point > longest_test:
    #             longest_test = last_point
    #
    #     else:
    #         empty_dfs.append(i)

    # if protocol == "UDP":
    #     make_plot(dfs, "jitter_ms", log_scale_y=True, total_time=longest_test)
    #     make_plot(dfs, "latency_avg_ms", log_scale_y=True, total_time=longest_test)
    #     make_plot(dfs, "packet_loss_percent", log_scale_y=False, total_time=longest_test)
    #
    # make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, total_time=longest_test)

    # df_gnodeb = pd.read_csv("./results/gnodeb_stats_{}.csv".format(protocol), sep=";")
    # gnodeb_cpu = df_gnodeb["CPU_usage"].values.tolist()[:2*int(np.ceil(longest_test))]
    # gnodeb_cpu = df_gnodeb["RAM_usage"].values.tolist()[:2*int(np.ceil(longest_test))]
    #
    # make_combo_plot(dfs, "jitter_ms", gnodeb_cpu, log_scale_y=True, total_time=longest_test, file_name="scenario_{}_jitter".format(SCENARIO_NO))
    # make_combo_plot(dfs, "latency_avg_ms", gnodeb_cpu, log_scale_y=True, total_time=longest_test, file_name="scenario_{}_latency".format(SCENARIO_NO))
    # make_combo_plot(dfs, "bandwidth_Mbps", gnodeb_cpu, log_scale_y=False, total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    # make_combo_plot(dfs, "packet_loss_percent", gnodeb_cpu, log_scale_y=False, total_time=longest_test, file_name="scenario_{}_packet_loss_percent".format(SCENARIO_NO))

    # make_combo_plot(dfs, "jitter_ms", gnodeb_cpu, log_scale_y=True, total_time=longest_test)
    # make_combo_plot(dfs, "latency_avg_ms", gnodeb_cpu, log_scale_y=True, total_time=longest_test)
    # make_combo_plot(dfs, "bandwidth_Mbps", gnodeb_cpu, log_scale_y=False, total_time=longest_test)
    # make_combo_plot(dfs, "packet_loss_percent", gnodeb_cpu, log_scale_y=False, total_time=longest_test)



    df = pd.read_csv("./results/parsed_{}_1_ue_metrics.log".format(protocol), sep=";")
    df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100
    dfs[1] = df

    last_point = df["second"].iat[-1]
    if last_point > longest_test:
        longest_test = last_point

    df = pd.read_csv("./results/parsed_{}_1_ue_metrics_slice_2.log".format(protocol), sep=";")
    df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100
    dfs[2] = df

    last_point = df["second"].iat[-1]
    if last_point > longest_test:
        longest_test = last_point

    make_plot(dfs, "jitter_ms", log_scale_y=True, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_jitter".format(SCENARIO_NO))
    make_plot(dfs, "latency_avg_ms", log_scale_y=True, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_latency".format(SCENARIO_NO))
    # make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    make_plot(dfs, "packet_loss_percent", log_scale_y=False, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_packet_loss_percent".format(SCENARIO_NO))

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
    ax2.set_ylabel("procentowe wykorzystanie CPU przez gNodeB (czarna linia)", color="r")
    # ax2.set_ylabel("zużycie RAM w MB", color="r")

    ax1.legend(["UE {}".format(i) for i in dfs])

    if log_scale_y:
        ax1.set_yscale("log")
    ax1.set_xticks(np.arange(0, total_time + 15, 10.0))

    if file_name:
        plt.savefig("./plots/{}.svg".format(file_name))

    plt.show()


if __name__ == "__main__":
    main(protocol="udp")
