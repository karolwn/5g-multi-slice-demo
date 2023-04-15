#!/bin/bash

TOTAL_DURATION=60
DEFAULT_TIME_SPACING=10
NUMBER_OF_UE=5
STARTING_PORT=10000
DEFAULT_BANDWIDTH="200M"

for i in $(seq ${NUMBER_OF_UE})
do
	container_name="ue_${i}"
	port=$((STARTING_PORT + i))
	docker exec -d ${container_name} bash -c "./testing_scripts/ue_test_core.sh http_server.com ${port} ${TOTAL_DURATION} ${DEFAULT_BANDWIDTH}" &
	TOTAL_DURATION=$((TOTAL_DURATION - DEFAULT_TIME_SPACING))
	sleep ${DEFAULT_TIME_SPACING}
done

