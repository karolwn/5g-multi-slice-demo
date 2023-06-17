#!/bin/bash

TOTAL_DURATION=160
DEFAULT_TIME_SPACING=10
ENDGAME=10
NUMBER_OF_UE=15
STARTING_PORT=10000
DEFAULT_BANDWIDTH="50m"

rm gnodeb_docker_stats.log

docker stats gnodeb > gnodeb_docker_stats.log &

docker exec ue_1 bash -c "iperf -c http_server.com -B 10.70.0.1 -t 160 -u -b 25m -p 20001 > /dev/null" &


for i in $(seq ${NUMBER_OF_UE})
do
	container_name="ue_${i}"
	echo "starting ${container_name}, traffic will last ${TOTAL_DURATION} seconds"
	port=$((STARTING_PORT + i))
	if [[ ${i} -eq 1 ]]
	then
		docker exec ${container_name} bash -c "./testing_scripts/ue_test_core_udp.sh http_server.com ${port} ${TOTAL_DURATION} 25m" &
	else
		docker exec ${container_name} bash -c "./testing_scripts/ue_test_core_udp.sh http_server.com ${port} ${TOTAL_DURATION} ${DEFAULT_BANDWIDTH}" &
	fi
	TOTAL_DURATION=$((TOTAL_DURATION - DEFAULT_TIME_SPACING))
	sleep ${DEFAULT_TIME_SPACING}
done

echo "waiting, sleep 30"
sleep 30


trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

