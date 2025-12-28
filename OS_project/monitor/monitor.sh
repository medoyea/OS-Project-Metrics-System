#!/bin/bash
#Override old csv and add the labels
CSV_FILE="/data/system_monitor.csv"
echo "date,cpu_usage,memory_usage,disk_usage,GPU_utilization,rx_bytes,tx_bytes,uptime" > "$CSV_FILE" || {
	echo "Error: Unable to write to $CSV_FILE"
	exit 1
}


#main loop to get the metrics every 1 seconds
while true; do
	#cpu usage from top command sum of user and system usage
	CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}'|| CPU="ERROR")

	#memory used / total * 100 to calculate percentage usage
	MEMORY=$(free -m | awk 'NR==2{printf "%.2f", ($3/$2)*100 }'|| MEMORY="ERROR")

	#disk usage percentage of root partition
	DISK=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%'|| DISK="ERROR")

	#gpu usage using nvidia-smi command if nvidia-smi fails set GPU to ERROR
	GPU=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits|| GPU="ERROR")

	#network rx and tx bytes for the default network interface
	IFACE=$(ip route | awk '/default/ {print $5}'|| IFACE="ERROR")
	
	#read rx and tx bytes from sysfs
	RX_BYTES=$(cat /sys/class/net/$IFACE/statistics/rx_bytes|| RX_BYTES="ERROR")

	TX_BYTES=$(cat /sys/class/net/$IFACE/statistics/tx_bytes|| TX_BYTES="ERROR")

	#system uptime in a human readable format
	UPTIME=$(uptime -p)

	echo "$(date),$CPU,$MEMORY,$DISK,$GPU,$RX_BYTES,$TX_BYTES,\"$UPTIME\"" >> "$CSV_FILE" || {
		echo "Error: Unable to write to $CSV_FILE"
		exit 1
	}

	sleep 2
done
