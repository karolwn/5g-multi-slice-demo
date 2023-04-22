#!/bin/bash

SLICE_1_IP_TO_BIND=$(ifconfig | grep inet | awk '{ print $2 }' | grep '10.60')

# iperf3 -c ${1} -p ${2} -B ${SLICE_1_IP_TO_BIND} -V -Z -t ${3} -u -b ${4} > /dev/null
iperf -c ${1} -B ${SLICE_1_IP_TO_BIND} -t ${3} -u -b ${4} -p ${2} > /dev/null
# iperf3 -c ${1} -p ${2} -B ${SLICE_1_IP_TO_BIND} -V -Z -t ${3} > /dev/null
# $1 - http server IP
# $2 - port, 10 000 + ue number e.g. ue_1 -> 10 001
# $3 - duration of test
# $4 - bandwidth

