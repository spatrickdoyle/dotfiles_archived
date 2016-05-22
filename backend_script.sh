#!/bin/bash

echo "%{+u +o U#000000}"

while :; do
	if ping -c 1 8.8.8.8 > /dev/null; then
		color_ping="000000"
	else
		color_ping="ff0000"
	fi

	DESKTOPS=("")
	d=0
	DESKTOP_IND=(- - - - - - - - - -)

	DESKTOP=$(i3-msg -t get_workspaces|sed 's/.."num":[0-9],"name":"//g; s/","visible":/,/g; s/"focused"://g; s/"rect":{"x"://g; s/"y"://g; s/"width"://g; s/"height"://g; s/},"output":"/,/g; s/","urgent":false}/$/g; s/$]//')

	for (( i=0; i<${#DESKTOP}; i++ )); do
		if [ "${DESKTOP:$i:1}" = "$" ]; then
			d+=1
			DESKTOPS[d]=""
		else
			DESKTOPS[d]+="${DESKTOP:$i:1}"
		fi
	done

	for i in ${DESKTOPS[*]}; do
		MONITOR=$(echo $i|sed 's/.,.\{4,5\},.\{4,5\},\([0-9]*,\)\{4\}//')
		FOCUSED=$(echo $i|sed 's/.,.\{4,5\},//; s/,\([0-9]*,\)\{4\}.*//')

		((INDEX=${i:0:1}-1))

		if [ $MONITOR = "HDMI1" ]; then
			DESKTOP_IND[$INDEX]="%{T2}x%{T1}"
		elif [ $MONITOR = "LVDS1" ]; then
			DESKTOP_IND[$INDEX]="%{T2}+%{T1}"
		fi
		if [ $FOCUSED == "true" ]; then
			DESKTOP_IND[$INDEX]='|'
		fi
	done

	BATTERY=$(acpi|sed 's/Battery [0-9]: //; s/%.*//; s/ //;')
	BATTERY_IND=$(echo $BATTERY|sed 's/,.*//')
	if [ $BATTERY_IND = "Discharging" ]; then
		color="ffae00"
	fi
	if [ $BATTERY_IND = "Unknown" ]; then
		color="ffae00"
	fi
	if [ $BATTERY_IND = "Charging" ]; then
		color="00d000"
	fi
	if [ $BATTERY_IND = "Full" ]; then
		color="00d000"
		POWER=10
	else
		POWER=$(echo $BATTERY|sed 's/.*,//')
		((POWER=$POWER/10))
	fi

	DESKTOP_IND[0]="%{F#"$color"}"${DESKTOP_IND[0]}
	DESKTOP_IND[POWER]="%{F#ff0000}"${DESKTOP_IND[POWER]}

	DATE_STR=$(date +"%A, %B %d, %Y")
	time_str=$(date +"%I:%M %p")
	if [ ${time_str:0:1} = 0 ]; then
		time_str=${time_str:1}
	fi

	echo "%{l #B000000}   %{T3}.%{B#ff000000 +u +o}.%{B#ffffff T1} "$DATE_STR"                                                                                                                                                                                                                                                                                                    %{c F#"$color_ping"}"${time_str}"%{r}"${DESKTOP_IND[0]}${DESKTOP_IND[1]}${DESKTOP_IND[2]}${DESKTOP_IND[3]}${DESKTOP_IND[4]}${DESKTOP_IND[5]}${DESKTOP_IND[6]}${DESKTOP_IND[7]}${DESKTOP_IND[8]}${DESKTOP_IND[9]}"  %{B#ff000000 -u -o T3}.%{B#00000000 T1}   %{F#000000}"

	sleep 0.1

done