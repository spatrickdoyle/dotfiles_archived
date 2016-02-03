import os,time
from PIL import Image


os.system("scrot -z /home/sean/Programs/Python/lockscreen.png")

backgroundColor = (0,)*3
pixelSize = 9

image = Image.open('/home/sean/Programs/Python/lockscreen.png')
image = image.resize((image.size[0]/pixelSize, image.size[1]/pixelSize), Image.NEAREST)
image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)

image.save('/home/sean/Programs/Python/lockscreen.png')

os.system("i3lock -i /home/sean/Programs/Python/lockscreen.png")

if int(time.strftime("%H")) > 20:
	os.system("sudo pm-suspend")