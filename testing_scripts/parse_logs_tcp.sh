#!/bin/bash


for FILE in *.log
do
	echo ${FILE}
	cat ${FILE} | grep -v -e 'received out-of-order' | grep -v -e 'local' | grep -v -e 'Interval' | head -n -1 | grep -v -e '0:0:0:0:0:0:0:0' | grep -e '\[' | sed -e 's:/ :/:g' | awk 'BEGIN{print "second;transfer_MB;bandwidth_Mbps" }; {split($3, a, "-")}; { print a[1]";"$5";"$7 }' > "./results/parsed_tcp_${FILE}"
done

grep gnodeb_docker_stats.log -e 'gnodeb' | awk 'BEGIN {print "CPU_usage;RAM_usage"}; {split($3, a, "%"); split($4, b, "[A-Z]")}; { print a[1]";"b[1] }' > ./results/gnodeb_stats_tcp.csv
grep gnodeb_2_docker_stats.log -e 'gnodeb' | awk 'BEGIN {print "CPU_usage;RAM_usage"}; {split($3, a, "%"); split($4, b, "[A-Z]")}; { print a[1]";"b[1] }' > ./results/gnodeb_2_stats_tcp.csv

