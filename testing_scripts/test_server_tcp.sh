#!/bin/bash

NUMBER_OF_UE=15
STARTING_PORT=10000

#rm -f *.json

#for i in $(seq ${NUMBER_OF_UE})
#do
#	port=$((STARTING_PORT + i))
#	echo "starting server on port ${port}"
#	iperf3 -s -p ${port} -i 0.1 -J > ${i}_ue_metrics.json &
#done

#echo "ctrl-c to exit"
# iperf -s -i 1 -u -e -l 999M -w 32K> iperf2_test.log

iperf -s -i 1 -e -l 999M -w 999M -p 20001 > 1_ue_metrics_slice_2.log &


for i in $(seq ${NUMBER_OF_UE})
do
       port=$((STARTING_PORT + i))
       echo "starting server on port ${port}"
#       iperf -s -i 1 -u -e -l 999M -w 999M -p ${port} > ${i}_ue_metrics.log &
       iperf -s -i 1 -e -p ${port} > ${i}_ue_metrics.log &
done

ps -a | grep iperf


# wait for ctrl-c
#trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
#sleep 1000000000000000000000000

#TOTAL_DURATION=60
#DEFAULT_TIME_SPACING=10
#NUMBER_OF_UE=15
#STARTING_PORT=10000
#DEFAULT_BANDWIDTH="200M"

#for i in $(seq ${NUMBER_OF_UE})
#do
#        container_name="ue_${i}"
#        echo "starting ${container_name}"
#        port=$((STARTING_PORT + i))
#        docker exec -d ${container_name} bash -c "./testing_scripts/ue_test_core.sh http_server.com ${port} ${TOTAL_DURATION} ${DEFAULT_BANDWIDTH}"
#        TOTAL_DURATION=$((TOTAL_DURATION - DEFAULT_TIME_SPACING))
#        sleep ${DEFAULT_TIME_SPACING}
#done

