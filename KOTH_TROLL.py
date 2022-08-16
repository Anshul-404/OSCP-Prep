#!/usr/bin/python
#!/usr/bin/python3

import time

first = "You've been TROLLED"

song = '''You've been trolled
Yes, you've probably been told
Don't reply to this guy
He's just trying to get a rise
Out of you, yes, it's true
You respond and that's his cue
To start trouble on the double
While he strokes his manly stubble

You've been trolled, you've been trolled
You should probably just fold
When the only winning move is not to play
And yet you keep on trying, mindlessly replying
You've been trolled, you've been trolled, have a nice day'''


while True:

	resf = first.split()
	res = song.split() 

	for i in resf:
		print(i)
		time.sleep(1)
	print("")

	time.sleep(1)

	for i in res:
		if("d" in i.lower()):
			print (i.upper())
			print("")
		else:
			print(i)
		time.sleep(0.3)

	print("")