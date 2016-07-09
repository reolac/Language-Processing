def navigation():
	import re
	command = raw_input("you start at the inn, you are able to go any direction (north, east, south or west, where will you go?")
	if re.search("north", command):
		command = raw_input("you went north, you arrive at the chapel, from here you can go only east or south, where will you go now?")
		if re.search("east", command):
			print "you go east and arrive at the harbour, you can only go back from here!"
			
	if re.search("south", command):
		command = raw_input("you went south, you arrive at the beach, from here you can go only west, where will you go now?")
		if re.search("west", command):
			command = raw_input("you went west, you arrive at the farm, from here you can go only north, where will you go now?")
			
	if re.search("west", command):
		command = raw_input("you went west, you arrive at the blacksmith, from here you can still go north, east, or west, where will you go now?")
		if re.search("west", command):
			command = raw_input("you went west again, you arrive at the fountain, from here you can go north, east, or west, where will you go now?")
	if re.search("east", command):
		command = raw_input("you went east, you arrive at the lumber mill, from here you can go only south, where will you go now?")
		if re.search("south", command):
			command = raw_input("you went south, you arrive at the mines, from here you can go only back, where will you go now?")