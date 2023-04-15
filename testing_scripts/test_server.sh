#!/bin/bash

iperf3 -s -p 10001 > ./1_ue_metrics.log &
iperf3 -s -p 10002 > ./2_ue_metrics.log &
iperf3 -s -p 10003 > ./3_ue_metrics.log &
iperf3 -s -p 10004 > ./4_ue_metrics.log &
iperf3 -s -p 10005 > ./5_ue_metrics.log


trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT


