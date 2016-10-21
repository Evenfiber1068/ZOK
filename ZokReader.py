"""
An interpreter for the language ZOK
Written October 2016
By Alex Huard
"""

import os
import sys
os.chdir(os.path.dirname(__file__))


o = []
k  = 0

current_line = 0

s = []

ret = []


for x in range(365):
	o.append(0)

cool = False #No one starts off being cool


o.append(0)

#Functions for line changing

def changeline(amount):
	global current_line
	current_line = current_line+amount
	return 0

def setline(amount):
	global current_line
	current_line = amount
	return 0
	
	
def grabfile(file_name):
	file_list = []
	file_main = open(file_name)
	for line in file_main:
		file_list.append(line)
	return file_list
        
def printfile(file_list):
	for line in range(len(file_list)):
		print(file_list[line])

def lineread(line):
	global current_line
	global o
	global k
	global cool
	global ret
	global s
	if line.startswith("Secret"):
		changeline(line.count("!"))
		return 0
	if line.startswith("\t"):
		print("Tabs aren't cool!")
		cool = False
		return 0
	if line.startswith("Soon"):
		s.append(current_line)
		changeline(line.count("!"))
		return 0
		
		
	if line.startswith("Cool!"):
		cool = True
		return 0
		
	if cool == True:	
		if line.startswith("Hey there"):
			o[line.count("!")-1] += o[k]
		elif line.startswith("Hey"):
			o[k] = o[k]+line.count("!")
			return 0
		elif line.startswith("Tell there"):
			o[line.count("!")-1] = int(input() % 510)
		elif line.startswith("Tell me!"):
			o[k] = int(input() % 510)
		elif line.startswith("Back"):
			changeline(-1*line.count("!"))
			return 0
		elif line.startswith("Now"):
			if line.count("!")-1 > len(s):
				print("\nNow isn't happening at a line near "+str(current_line))
				cool = False
				return 0
			else:
				ret.append(current_line)
				infunct = True
				setline(s[line.count("!")-1]+1) #The +1 allows the comment line for functions
				#print("Jumping to line "+str(s[line.count("!")-1]+1))
				return 0
		elif line.startswith("Get out!"):
				setline(ret.pop())
				return 0
		elif line.startswith("Read there"):
			sys.stdout.write(chr(o[line.count("!")]))
			return 0
		elif line.startswith("Read me!"):
			sys.stdout.write(chr(o[k]))
			return 0
		elif line.startswith("Show there"):
			print(o[line.count("!")])
			return 0
		elif line.startswith("Show me!"):
			print(o[k])
		elif line.startswith("Get over there"):
			o[line.count("!") % 365] = o[k]
			return 0
		elif line.startswith("Get over here"):
			o[k] = o[line.count("!") % 365]
			return 0
		elif line.startswith("Read me more"):
			for x in range(line.count("!")):
				#print(x)
				sys.stdout.write(chr(o[(k+x)% 365] ))
			return 0
		elif line.startswith("Show me more"):
			for x in range(line.count("!")):
				print(o[(k+x)% 365] )
			return 0
		elif line.startswith("I need some space"):
			for x in range(line.count("!")):
				print("")
		elif line.startswith("Jump"):
			changeline(line.count("!"))
		elif line.startswith("What"):#REWORK IF STATEMENTS?
			if (line.count("?") > 0):
				if (o[k] == o[line.count("?")-1]):
					#print("Conditional True "+str(o[k])+" "+str(o[line.count("?")-1]))
					return 0
				else:
					changeline(line.count("!"))
					return 0
					#print("Conditional True")
			else:
				print("\nError 1337: get rekt kiddo.")
				cool = False
				return 0
		elif line.startswith("Not cool!"):
			cool = False
			return 0
		elif line.startswith("Lets keep going"):
			k = k+line.count("!")
			#print("k is now "+str(k))
		elif line.startswith("Lets do it again"):
			if not (o[k] == k):
				changeline(-1*(line.count("!")+1))
				return 0
			else:
				return 0
		elif line == "\n":
			print("\nLine near "+str(current_line)+" is blank!")
		else:
			print("\nNot really feeling a line near "+str(current_line))
			cool = False
			return 0
			
	elif not line.startswith("Secret"):
		print("\nProgram is not cool enough at line "+str(current_line))
	return 0

	

def runfile(file_list):	
	global o
	global k
	global current_line
	while current_line < len(file_list):
		lineread(file_list[current_line])
		changeline(1)
		#print(current_line)
		if k > 365:
			k = k % 365
		if o[k] == -1:
			o[k] = 255
		if o[k] > 510:
			o[k] = o[k] % 510



def mix(one, two):
	file_master = []
	if len(one) > len(two):
		print("Error: File one is longer than file two")
		return one
	else:
		for x in range(len(one)):
			file_master.append(one[x])
			file_master.append(two[x])
		return file_master
		
path = raw_input("Enter the path for file one\n")
file_one = grabfile(path)
path = raw_input("Enter the path for file two\n")
file_two = grabfile(path)
master = mix(file_one, file_two)
if not master == one:
	runfile(master)