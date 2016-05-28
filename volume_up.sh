#!/usr/bin/env bash

if [[ $(awk -F'[][]' '/dB/ { print $2 }' <(amixer sget Master)) = *100%* ]]; then
	echo 0
else
	amixer sset 'Master' 10%+
	play /home/sean/Programs/git-repos/dotfiles/computerbeep_9.mp3
fi