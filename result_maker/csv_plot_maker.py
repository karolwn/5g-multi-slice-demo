import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import stats_calc as sc
import plot_makers as pm

from variables import *

SCENARIO_NO = "13_15xUE_UDP_50Mbps_1xSLICE"


def main(protocol: str = "udp", no_ue: int = NUMBER_OF_UE, time_spacing: int = TIME_DELAY_BETWEEN_UE,
         total_time: int = TOTAL_DURATION) -> None:
    longest_test = 0
    empty_dfs = []
    dfs = {}
    for i in range(no_ue):
        df = pd.read_csv("./results/parsed_{}_{}_ue_metrics.log".format(protocol, i + 1), sep=";")

        if not df.empty:
            time_skew = i * time_spacing
            df.loc[:, "second"] += time_skew
            if protocol == "udp":
                df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100
            dfs[i + 1] = df
            last_point = df["second"].iat[-1]

            if last_point > longest_test:
                longest_test = last_point

        else:
            empty_dfs.append(i)

    # if protocol == "UDP":
    #     make_plot(dfs, "jitter_ms", log_scale_y=True, total_time=longest_test)
    #     make_plot(dfs, "latency_avg_ms", log_scale_y=True, total_time=longest_test)
    #     make_plot(dfs, "packet_loss_percent", log_scale_y=False, total_time=longest_test)
    #
    # make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, total_time=longest_test)
    #
    # # make_plot(dfs, "jitter_ms", log_scale_y=True, total_time=longest_test, file_name="scenario_{}_jitter".format(SCENARIO_NO))
    # # make_plot(dfs, "latency_avg_ms", log_scale_y=True, total_time=longest_test, file_name="scenario_{}_latency".format(SCENARIO_NO))
    # make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    # # make_plot(dfs, "packet_loss_percent", log_scale_y=False, total_time=longest_test, file_name="scenario_{}_packet_loss_percent".format(SCENARIO_NO))

    df_gnodeb = pd.read_csv("./results/gnodeb_stats_{}.csv".format(protocol), sep=";")
    gnodeb_cpu = df_gnodeb["CPU_usage"].values.tolist()[:2*int(np.ceil(longest_test))]
    #
    # df_gnodeb_2 = pd.read_csv("./results/gnodeb_2_stats_{}.csv".format(protocol), sep=";")
    # gnodeb_cpu_2 = df_gnodeb_2["CPU_usage"].values.tolist()[:2*int(np.ceil(longest_test))]
    #
    # # gnodeb_cpu = df_gnodeb["RAM_usage"].values.tolist()[:2*int(np.ceil(longest_test))]
    # #
    pm.make_combo_plot(dfs, "jitter_ms", gnodeb_cpu, log_scale_y=True, total_time=longest_test, file_name="scenario_{}_jitter".format(SCENARIO_NO))
    pm.make_combo_plot(dfs, "latency_avg_ms", gnodeb_cpu, log_scale_y=True, total_time=longest_test, file_name="scenario_{}_latency".format(SCENARIO_NO))
    pm.make_combo_plot(dfs, "bandwidth_Mbps", gnodeb_cpu, log_scale_y=False, total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    pm.make_combo_plot(dfs, "packet_loss_percent", gnodeb_cpu, log_scale_y=False, total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    #
    # make_combo_plot_double(dfs, "jitter_ms", gnodeb_cpu, gnodeb_cpu_2, log_scale_y=True, total_time=longest_test, file_name="scenario_{}_jitter".format(SCENARIO_NO))
    # make_combo_plot_double(dfs, "latency_avg_ms", gnodeb_cpu, gnodeb_cpu_2, log_scale_y=True, total_time=longest_test, file_name="scenario_{}_latency".format(SCENARIO_NO))
    # make_combo_plot_double(dfs, "bandwidth_Mbps", gnodeb_cpu, gnodeb_cpu_2, log_scale_y=False, total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    # make_combo_plot_double(dfs, "packet_loss_percent", gnodeb_cpu, gnodeb_cpu_2, log_scale_y=False, total_time=longest_test, file_name="scenario_{}_packet_loss_percent".format(SCENARIO_NO))



    # df = pd.read_csv("./results/parsed_{}_1_ue_metrics.log".format(protocol), sep=";")
    # df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100
    # dfs[1] = df
    #
    # last_point = df["second"].iat[-1]
    # if last_point > longest_test:
    #     longest_test = last_point
    #
    # df = pd.read_csv("./results/parsed_{}_1_ue_metrics_slice_2.log".format(protocol), sep=";")
    # df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100
    # dfs[2] = df
    #
    # last_point = df["second"].iat[-1]
    # if last_point > longest_test:
    #     longest_test = last_point
    # #
    # make_plot(dfs, "jitter_ms", log_scale_y=True, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_jitter".format(SCENARIO_NO))
    # make_plot(dfs, "latency_avg_ms", log_scale_y=True, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_latency".format(SCENARIO_NO))
    # make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_bandwidth_Mbps".format(SCENARIO_NO))
    # make_plot(dfs, "packet_loss_percent", log_scale_y=False, legend=["UE_1_slice_1", "UE_1_slice_2"], total_time=longest_test, file_name="scenario_{}_packet_loss_percent".format(SCENARIO_NO))


def main_multiple(protocol: str = "udp", no_ue: int = NUMBER_OF_UE, time_spacing: int = TIME_DELAY_BETWEEN_UE,
         total_time: int = TOTAL_DURATION, no_reps: int = NO_REPS) -> None:
    longest_test = 0
    empty_dfs = []
    dfs = {}

    for i in range(no_ue):  # for each UE test host
        df_columns = pd.read_csv("./results/parsed_{}_1_1_ue_metrics.log".format(protocol), nrows=0, sep=";").columns.tolist()
        data_for_df = {col: [] for col in df_columns}
        for j in range(no_reps):  # for each test run
            df = pd.read_csv("./results/parsed_{}_{}_{}_ue_metrics.log".format(protocol, j + 1, i + 1), sep=";")
            if not df.empty:
                time_skew = i * time_spacing
                df.loc[:, "second"] += time_skew
                if protocol == "udp":
                    df["packet_loss_percent"] = (df["lost_packets"] / df["total_packets"]) * 100

                last_point = df["second"].iat[-1]

                if last_point > longest_test:
                    longest_test = last_point

                for col in df.columns.tolist():
                    data_for_df[col].append(df[col].values.tolist())  # save loaded data into list of lists
            else:
                empty_dfs.append(i)

        df_out = pd.DataFrame()

        for col in data_for_df:  # calculate average and confidence intervals
            data_matrix = sc.add_nans(data_for_df[col])
            avg_value = sc.calc_avg(data_matrix)
            lower_bound, upper_bound = sc.calc_intervals(data_matrix, 0.95)

            df_out[col] = avg_value
            df_out[col + "_lower"] = lower_bound
            df_out[col + "_upper"] = upper_bound

        dfs[i + 1] = df_out

    # pm.make_plot(dfs, "bandwidth_Mbps", log_scale_y=False, total_time=longest_test)
    # pm.make_plot_pretty(dfs,
    #                     "bandwidth_Mbps",
    #                     log_scale_y=False,
    #                     total_time=longest_test,
    #                     custom_ylabel="Przepustowość w Mb/s",
    #                     draw_intervals=True,
    #                     file_name="final_scenario_{}_{}_{}_{}".format(1,
    #                                                                   protocol,
    #                                                                   "bandwidth_Mbps",
    #                                                                   "15x_UE_1x_slice_no_gNodeB_stats"))

    pm.make_plot_pretty({1: dfs[1]},
                        "bandwidth_Mbps",
                        log_scale_y=False,
                        total_time=longest_test,
                        custom_ylabel="Przepustowość w Mb/s",
                        draw_intervals=True,
                        interval_alpha=0.12,
                        file_name="final_scenario_{}_{}_{}_{}".format(1,
                                                                      protocol,
                                                                      "bandwidth_Mbps",
                                                                      "15x_UE_1x_slice_no_gNodeB_stats_only_UE1"))


if __name__ == "__main__":
    main_multiple("tcp")
    # main(protocol="udp")
    # test_list = [
    #     [1, 5, 6, 8, 9],
    #     [3, 8, 3],
    #     [8, 4, 1, 0]
    # ]
    #
    # # print(sc.add_nans(test_list))
    #
    # test_list = sc.add_nans(test_list)
    # avg = sc.calc_avg(test_list)
    # print(avg)
    #
    # siup = sc.calc_intervals(test_list, 0.95)
    # print(siup)
    # plt.plot(range(len(avg)), avg)
    # plt.plot(range(len(siup[0])), siup[0])
    # plt.plot(range(len(siup[1])), siup[1])
    # plt.show()
