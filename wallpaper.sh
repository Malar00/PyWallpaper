#!/bin/bash
while getopts 'anc:' flag; do
  case "${flag}" in
		n) WALLPAPER="$(find /home/malar/wallpapers/*.jpg -type f | shuf -n 1)";;	
		a) WALLPAPER="$(find /home/malar/wallpapers/animeWallpapers/*.jpg -type f | shuf -n 1)";;
		c) WALLPAPER="$(find ${OPTARG}/*.jpg -type f | shuf -n 1)";;
	esac
feh --bg-scale $WALLPAPER
wal -i $WALLPAPER
done
