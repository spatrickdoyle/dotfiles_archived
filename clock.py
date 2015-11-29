#I have it set to run when I press Crtl+t, and it closes when you press any key

import time,pygame

pygame.init()
global screen
screen = pygame.display.set_mode((501,301))

font1 = pygame.font.SysFont(u'bitstreamverasansmono',90)
font2 = pygame.font.SysFont(u'bitstreamverasansmono',30)
font3 = pygame.font.SysFont(u'bitstreamverasansmono',30,False,True)


while True:
	screen.fill((255,255,255))
	pygame.draw.line(screen,(0,0,0),(0,0),(500,0))
	pygame.draw.line(screen,(0,0,0),(0,0),(0,300))
	pygame.draw.line(screen,(0,0,0),(500,0),(500,300))
	pygame.draw.line(screen,(0,0,0),(0,300),(500,300))

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			raise SystemExit

	curtimestr = str(int(time.strftime("%I")))+":"+time.strftime("%M")
	curtime = font1.render(curtimestr, 2, (0,0,0))#textLoad(font1,curtimestr,(0,0,0))
	screen.blit(curtime,(250 - curtime.get_width()/2,100 - curtime.get_height()/2))

	cursecnum = int(time.strftime("%S"))
	if cursecnum == 1:
		cursecstr = "and 1 second"
	else:
		cursecstr = "and "+str(cursecnum)+" seconds"
	cursec = font3.render(cursecstr, 2, (0,0,0))#textLoad(font3,cursecstr,(0,0,0))
	screen.blit(cursec,(250 - cursec.get_width()/2,160 - cursec.get_height()/2))

	curdatestr = "%s, %s %s %s"%(time.strftime("%A"),time.strftime("%B"),time.strftime("%d"),time.strftime("%Y"))
	curdate = font2.render(curdatestr, 2, (0,0,0))#textLoad(font2,curdatestr,(0,0,0))
	screen.blit(curdate,(250 - curdate.get_width()/2,260 - curdate.get_height()/2))

	pygame.display.update()
