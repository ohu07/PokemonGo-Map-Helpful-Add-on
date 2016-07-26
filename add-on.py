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
	location = l.replace (" ", "_")
	os.popen("cd ~/Desktop/PokemonGo-Map-master")
	empty = raw_input("Your browser will open to the map, if the map does not show up refresh the page. Press return/enter if you understand... ")
	webbrowser.open("http://localhost:5000")
	alpha = ("python runserver.py -a " + a + " -u " + u + " -p " + p + " -l " + location + " -st " + s)
	os.popen(alpha)
main()
