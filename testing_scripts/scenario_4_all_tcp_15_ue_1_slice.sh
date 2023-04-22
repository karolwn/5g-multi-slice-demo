#!/bin/bash

TOTAL_DURATION=160
DEFAULT_TIME_SPACING=10
ENDGAME=10
NUMBER_OF_UE=15
STARTING_PORT=10000
DEFAULT_BANDWIDTH="50M"


for i in $(seq ${NUMBER_OF_UE})
do
	container_name="ue_${i}"
	echo "starting ${container_name}, traffic will last ${TOTAL_DURATION} seconds"
	port=$((STARTING_PORT + i))
	docker exec ${container_name} bash -c "./testing_scripts/ue_test_core.sh http_server.com ${port} ${TOTAL_DURATION} ${DEFAULT_BANDWIDTH}" &
	TOTAL_DURATION=$((TOTAL_DURATION - DEFAULT_TIME_SPACING))
	sleep ${DEFAULT_TIME_SPACING}
done

echo "waiting, sleep 20"
sleep 20

