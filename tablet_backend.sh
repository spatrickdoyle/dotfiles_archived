#!/usr/bin/env bash

ORIENTATION=0

while :; do

	DEVICE=$(ls /sys/bus/iio/devices/*|grep in_accel_hysteresis -B 3|head -n 1|head -c -2)
	ORIENTATION_X=$(cat $DEVICE/in_accel_x_raw)
	if [ $ORIENTATION_X -gt 60000 ]; then
		((ORIENTATION_X=$ORIENTATION_X-65533))
	elif [ $ORIENTATION_X = 0 ]; then
		ORIENTATION_X=0.01
	fi
	ORIENTATION_Y=$(cat $DEVICE/in_accel_y_raw)
	if [ $ORIENTATION_Y -gt 60000 ]; then
		((ORIENTATION_Y=$ORIENTATION_Y-65533))
	fi

	ANGLE=$(echo "scale=3;a($ORIENTATION_Y/$ORIENTATION_X)/0.017453293" | bc -l | sed 's/^\./0./g; s/-\./0./' | sed 's/\..*//')
	((ORIENTATION_X=$(echo $ORIENTATION_X | sed 's/\..*//')))
	((ORIENTATION_Y=$(echo $ORIENTATION_Y | sed 's/\..*//')))

	if [ $ANGLE -lt 30 ]; then
		if [ $ANGLE -gt -30 ]; then
			if [ $ORIENTATION_X -lt 0 ]; then
				if [ $ORIENTATION -ne 1 ]; then
					/home/sean/Programs/git-repos/grox/grox.rb right
					ORIENTATION=1
				fi
			elif [ $ORIENTATION_X -gt 0 ]; then
				if [ $ORIENTATION -ne -1 ]; then
					/home/sean/Programs/git-repos/grox/grox.rb left
					ORIENTATION=-1
				fi
			fi
		else
			if [ $ORIENTATION -ne 0 ]; then
				/home/sean/Programs/git-repos/grox/grox.rb normal
				ORIENTATION=0
			fi
		fi
	else
		if [ $ORIENTATION -ne 0 ]; then
			/home/sean/Programs/git-repos/grox/grox.rb normal
			ORIENTATION=0
		fi
	fi


	DESKTOP=$(i3-msg -t get_workspaces|sed 's/","visible":true."focused":true.*//'|tail -c 2)

	BATTERY=$(acpi|sed 's/Battery [0-9]: //; s/%.*//; s/ //;')
	BATTERY_IND=$(echo $BATTERY|sed 's/,.*//')
	if [ $BATTERY_IND = "Full" ]; then
		color="00d000"
		POWER=100
	else
		POWER=$(echo $BATTERY|sed 's/.*,//')
	fi

	DATE_STR=$(date +"%a %b %e %y")
	time_str=$(date +"%H:%M")
	if [ ${time_str:0:1} = 0 ]; then
		time_str=${time_str:1}
	fi

	VOLUME=$(amixer get Master |grep % |awk '{print $4}'|sed 's/[^0-9]//g')
	BRIGHTNESS=$(xbacklight|sed 's/\..*//')

	echo "     "$time_str"     "$DATE_STR"     %{A:i3lock:}DESKTOP: "$DESKTOP"%{A}     VOLUME: "$VOLUME"%     BRIGHTNESS: "$BRIGHTNESS"%     MODE: "TABLET"     POWER: "$POWER"%"

	LID_STATE=$(cat /proc/acpi/button/lid/LID0/state | sed 's/state: *//')
	if [ $LID_STATE = "closed" ]; then
		sudo pm-suspend
	fi

	sleep 0.1

done