#!/bin/bash

TOTAL_DURATION=160
ORIG_TOTAL_DURATION=${TOTAL_DURATION}
DEFAULT_TIME_SPACING=10
ENDGAME=10
NUMBER_OF_UE=15
STARTING_PORT=10000
DEFAULT_BANDWIDTH="50m"

NO_REP=8

SLEEP_TIME=30

for j in $(seq ${NO_REP})
do
	cd ../
	./run_network.sh start &> /dev/null &
	echo "starting network, sleep ${SLEEP_TIME}"
	sleep ${SLEEP_TIME}
	cd ./testing_scripts

	docker exec http_server bash -c "./testing_scripts/test_server_udp.sh" &

	sleep ${SLEEP_TIME}

	rm -f gnodeb_docker_stats.log

	docker stats gnodeb > gnodeb_docker_stats.log &

	for i in $(seq ${NUMBER_OF_UE})
	do
		container_name="ue_${i}"
		echo "starting ${container_name}, traffic will last ${TOTAL_DURATION} seconds"
		port=$((STARTING_PORT + i))
		docker exec ${container_name} bash -c "./testing_scripts/ue_test_core_udp.sh http_server.com ${port} ${TOTAL_DURATION} ${DEFAULT_BANDWIDTH}" &
		TOTAL_DURATION=$((TOTAL_DURATION - DEFAULT_TIME_SPACING))
		sleep ${DEFAULT_TIME_SPACING}
	done

	echo "waiting, sleep ${SLEEP_TIME}"
	sleep ${SLEEP_TIME}

	cd ../
        ./run_network.sh stop
        cd ./testing_scripts

	./parse_logs_udp_multiple.sh ${j}

	echo "iteration ${j} done, sleep ${SLEEP_TIME}"
	sleep ${SLEEP_TIME}
	TOTAL_DURATION=${ORIG_TOTAL_DURATION}
done

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT
