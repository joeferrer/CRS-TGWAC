
import sys

def get_input():
	version = sys.version_info
	if version[0] > 2:
		return input()
	else:
		return raw_input()

def get_Y_N(question):
	user_input = 'NaN'
	while(user_input.upper()!="Y" and user_input.upper()!= "N"):
			print "\n" + question +" (Y/N): "
			user_input = get_input()
			if(user_input.upper()!="Y" and user_input.upper()!= "N"):
				print "Bad input.Y/N only."
	return user_input