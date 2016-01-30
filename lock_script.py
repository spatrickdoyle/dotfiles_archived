import os,time
from PIL import Image

if int(time.strftime("%H")) > 20:
	os.system("i3lock -i /home/sean/Pictures/wallpapers/amdg.png")
else:
	os.system("scrot /home/sean/Programs/Python/lockscreen.png")

	backgroundColor = (0,)*3
	pixelSize = 9

	image = Image.open('/home/sean/Programs/Python/lockscreen.png')
	image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
	image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)

	#lock = Image.open('/home/sean/Pictures/lock.png','RGBA')
	#image.paste(lock,(image.size[0]/2 - lock.size[0]/2,image.size[1]/2 - lock.size[1]/2))

	image.save('/home/sean/Programs/Python/lockscreen.png')

	os.system("i3lock -i /home/sean/Programs/Python/lockscreen.png")