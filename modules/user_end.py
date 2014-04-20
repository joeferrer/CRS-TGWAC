
import sys

def get_input():
	version = sys.version_info
	if version[0] > 2:
		return input()
	else:
		return raw_input()