DIR=0
SETTING=''

while :; do
	read MODE
	DESKTOP=$(i3-msg -t get_workspaces|sed 's/","visible":true."focused":true.*//'|tail -c 2)
 
	if [ $MODE = "charm" ]; then
		DIR=1
	elif [ $MODE = "strange" ]; then
		DIR=-1
	elif [ $MODE = "desktop" ]; then
		SETTING=0
	elif [ $MODE = "volume" ]; then
		SETTING=1
	elif [ $MODE = "brightness" ]; then
		SETTING=2
	fi

	case $DIR in
		-1) case $SETTING in
				0) ((DESKTOP=DESKTOP-1))
					eval "xte 'keydown Super_L' 'key $DESKTOP' 'keyup Super_L'"
				;;
				1) amixer sset 'Master' 10%-
					play /home/sean/Programs/git-repos/dotfiles/computerbeep_9.mp3
				;;
				2) xbacklight -dec 10
				;;
			esac
		;;
		1) case $SETTING in
				0) ((DESKTOP=DESKTOP+1))
					eval "xte 'keydown Super_L' 'key $DESKTOP' 'keyup Super_L'"
				;;
				1) $HOME/Programs/git-repos/dotfiles/volume_up.sh
				;;
				2) xbacklight -inc 10
				;;
			esac
		;;
	esac

	DIR=0
done