import subprocess,re,time

'''maybe add:
thing to tell me if I'm connected to the internet, and maybe what network
adjustable volume bar
'''

exp = re.compile("\"name\":\"(\d+)\",\"visible\":(true|false),\"focused\":(true|false),\"rect\":{\"x\":(\d+),\"y\":(\d+),\"width\":(\d+),\"height\":(\d+)},\"output\":\"(\w*)\"")

while True:
	call = subprocess.check_output(["i3-msg","-t","get_workspaces"])
	desktop = exp.findall(call)
	try:
		call_ping = subprocess.check_output(["ping","8.8.8.8","-c","1"])
		if call_ping.find("64 bytes from 8.8.8.8:"):
			color_ping = "000000"
		else:
			color_ping = "0d0000"
	except subprocess.CalledProcessError:
		color_ping = "ff0000"

	#desktops: - if nothing, | if focused, ~ if in use on LVDS1, + if in use of VGA1
	desktop_ind = ["-"]*10

	for i in desktop:
		if (i[7] == "VGA1"):
			desktop_ind[int(i[0])-1] = '%{T3}x%{T1}'
		elif (i[7] == "LVDS1"):
			desktop_ind[int(i[0])-1] = '%{T2}+%{T1}'
		if i[2] == "true":
			desktop_ind[int(i[0])-1] = '|'

	#battery: green if plugged in, yellow if discharging or unknown, red for discharged part
	battery = subprocess.check_output(["acpi"]).split()

	if (battery[2] == "Discharging,")or(battery[2] == "Unknown,"):
		color = "ffae00"
	elif (battery[2] == "Charging,")or(battery[2] == "Full,"):
		color = "00d000"

	if (battery[2] == "Full,"):
		power = 10
	else:
		power = int(battery[3][:2])/10

	for i in range(power):
		desktop_ind.insert(i*2,"%{{F#{}}}".format(color))
	for j in range(power,10):
		desktop_ind.insert(j*2,"%{F#ff0000}")

	desktop_ind = "".join(desktop_ind)
	time_str = time.strftime("%I:%M %p")
	if time_str[0] == '0':
		time_str = time_str[1:]

	print "%{l}     "+time.strftime("%A, %B %d, %Y")+"%{{c F#{}}}".format(color_ping)+time_str+"%{r}"+desktop_ind+"     %{F#000000}"