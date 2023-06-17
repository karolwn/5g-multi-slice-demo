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
	docker image prune --force
fi

if [ "$1" == "build" ]
then
	make all
        sudo docker compose -f docker-compose-build.yaml build
fi


if [ "$1" == "status" ]
then
        docker ps -a
fi

