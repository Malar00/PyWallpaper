#!/bin/bash
while getopts 'anc:' flag; 
do
  case "${flag}" in
	n) WALLPAPER="$(find $HOME/wallpapers/*.jpg -type f | shuf -n 1)";;	
	a) WALLPAPER="$(find $HOME/wallpapers/animeWallpapers/*.jpg -type f | shuf -n 1)";;
	c) WALLPAPER="$(find ${OPTARG}/*.jpg -type f | shuf -n 1)";;
  esac
feh --bg-scale $WALLPAPER
wal -i $WALLPAPER
done
