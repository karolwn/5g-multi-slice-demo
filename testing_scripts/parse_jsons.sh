#!/bin/bash


for FILE in *.json
do
	cat ${FILE} | jq -s .[0] > "./results/parsed_${FILE}"
done
