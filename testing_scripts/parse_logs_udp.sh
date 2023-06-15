#!/bin/bash


for FILE in *.log
do
	cat ${FILE} |  grep -v -e 'received out-of-order' | grep -v -e 'local' | grep -v -e 'Interval' | grep -v -e '-/-/-/- ms    0 pps' | grep -e '\[' | grep -v -e '-nan bits/sec' | sed -e 's:/ :/:g' | head -n -1 | awk 'BEGIN{print "second;transfer_MB;bandwidth_Mbps;jitter_ms;lost_packets;total_packets;latency_avg_ms"}; {split($3, a, "-"); split($11, b, "/"); split($13, c, "/"); print a[1]";"$5";"$7";"$9";"b[1]";"b[2]";"c[1]}' > "./results/parsed_udp_${FILE}"
done

grep gnodeb_docker_stats.log -e 'gnodeb' | awk 'BEGIN {print "CPU_usage;RAM_usage"}; {split($3, a, "%"); split($4, b, "[A-Z]")}; { print a[1]";"b[1] }' > ./results/gnodeb_stats_udp.csv
