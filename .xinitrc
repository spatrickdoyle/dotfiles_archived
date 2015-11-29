exec xrandr --output VGA1 --mode 1600x900&
exec xrandr --output LVDS1 --off&

#exec nitrogen --restore&
#exec dbus-launch docky&
#exec rofi -key-run F12&
#exec xcompmgr&
#exec openbox

#exec gnome-session

exec nitrogen --restore&
exec rofi -key-run F12 -key-window Alt+Tab&
exec i3
