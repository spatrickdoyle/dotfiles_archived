# dotfiles
My desktop config files<br/><br/>
![recent screenshot](http://www.spatrickdoyle.com/img/scrot.png)<br/>
Dependencies:<br/>
```
nitrogen
rofi
xcompmgr
i3-gaps
lemonbar-xft-git
ttf-ms-fonts
scrot
i3lock
```
<br/>
<br/>
Applications that are also used but could be removed are: terminator, gksu, wicd, and pm-utils<br/>
Sox is also used to play the mp3s when the keyboard shortcuts are used, which I think is cool, but could also be removed<br/>
OpenCV and cmake would be necessary to compile the pixelating script, but I've included the binary, and it's pretty simple, so I don't <i>think</i> there's any reason it shouldn't run...<br/>
Also things like ping and xrandr and sed that are built in to linux systems are used<br/><br/>

You need to make the backend script executable for it to be run:<br/>
```chmod +x backend_script.sh```<br/>
Same with i3rc, xinitrc, and volume_up.sh<br/><br/>

My actual .xinitrc simply consists of a call to the xinitrc in the repository, so you can do that, or just add 'exec' to the front of every line in xinitrc and copy the contents into .xinitrc<br/><br/>

Paths will have to be changed. All file paths point to where I have the github project folder on my system, you will have to change them to point to yours. I'm thinking about making some kind of installer or something that sets the paths automatically... so that's on the todo list.<br/>
Also on the todo list is to rewrite this README to explain the features of what I have going on here. Again, for another time, as mainly this repo exists only for my convenience, and I don't really 
expect anyone to look at this anyway.<br/>
