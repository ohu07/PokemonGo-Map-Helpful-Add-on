# PokemonGo-Map-Helpful-Add-on
import os
import sys
import webbrowser

def end():
	print("This program makes using another program that can scan any location for Pokemon in Pokemon Go easier.") 
	print ("I do not claim to own or have made the scanning program.") 
	print("This program can be used in accessory with the scanning program.")
	print("Using this program can make the account used subject to a BAN, if you do not intend for the account used in conjunction with this program to be BANNED close the terminal/command line.")
	variable = ("--------------------------------------------------------------------------------")
	return variable

def main():
	print end()
	a = raw_input("input account type, ptc or google: ")
	u = raw_input("input username for account: ")
	p = raw_input("input password for account: ")
	l = raw_input("input location to search for pokemon by: ")
	s = raw_input("input search range, the higher the number the further the search: ")
#Optional
	i = raw_input("input pokemon to ignore, if there are none you wish to ignore input none: ")
	o = raw_input("input pokemon you only wish to see, if you want to see all input all: ")
	ar = raw_input("input y if you want the map to auto refresh, if you don't input n: ")
	dp = raw_input("input y if you want the map to see pokestops, if you don't input n: ")
	ol = raw_input("input y if you want the map to see only lured pokestops, if you don't input n: ")
	dg = raw_input("input y if you want the map to see gyms, if you don't input n: ")
	pm = raw_input("input y if you want normal time for poke timers, if you want military time input n: ")
	location = l.replace (" ", "_")
	ignore = i.replace (" ", "_")
	only = o.replace (" ", "_")
	os.popen("cd ~/Desktop/PokemonGo-Map-master")
	if(i == "none"):
		ignore2 = ignore.replace ("none", "")
	else:
		ignore2 = (" -i " + ignore)

	if(o == "all"):
		only2 = only.replace ("all", "")
	else:
		only2 = (" -o " + only)

	if(ar == "n"):
		auto = ar.replace ("n", "")
	else:
		auto = (" -ar 5")

	if(dp == "n"):
		pokestops = dp.replace ("n", "")
	else:
		pokestops = (" -dp")

	if(ol == "n"):
		lured_pokestop = ol.replace ("n", "")
	else:
		lured_pokestop = (" -ol")

	if(dg == "n"):
		gym = dg.replace ("n", "")
	else:
		gym = (" -dg")

	if(pm == "n"):
		time = pm.replace ("n", "")
	else:
		time = (" -pm")
	empty = raw_input("Your browser will open to the map, if the map does not show up refresh the page. Press return/enter if you understand... ")
	webbrowser.open("http://localhost:5000")
	alpha = ("python example.py -a " + a + " -u " + u + " -p " + p + " -l " + location + " -st " + s + ignore2 + only2 + auto + pokestops + lured_pokestop + gym + time)
	os.popen(alpha)
	
main()
