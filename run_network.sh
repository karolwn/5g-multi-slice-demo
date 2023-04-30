#!/bin/bash

if [ "$USER" != "root" ]
then
	echo "Please run this as root or with sudo"
	exit 1
fi

if [ -z "$1" ]
then
	echo "No argument supplied, use start, stop, delete or status"
	exit 2
fi

if [ "$1" == "start" ]
then
	# (docker compose -f docker-compose-build.yaml up &) | (timeout --foreground 30 cat; cat >> app.log &)
	docker compose -f docker-compose-build.yaml up > app.log &
fi

if [ "$1" == "stop" ]
then
        docker compose -f docker-compose-build.yaml stop
fi

if [ "$1" == "delete" ]
then
        docker compose -f docker-compose-build.yaml rm
fi

if [ "$1" == "build" ]
then
	cd ../openairinterface5g/
	docker build --target ran-base --tag ran-base:latest --file docker/Dockerfile.base.ubuntu20 .
	docker build --target ran-build --tag ran-build:latest --file docker/Dockerfile.build.ubuntu20 .
	docker build --target oai-gnb --tag oai-gnb:latest --file docker/Dockerfile.gNB.ubuntu20 .
	docker image prune --force
	cd ../5g-multi-slice-demo/
        make all
        sudo docker compose -f docker-compose-build.yaml build
fi


if [ "$1" == "status" ]
then
        docker ps -a
fi

