# -*- coding: utf-8 -*-

def Start():
	print("start")

if __name__ == "__main__":
	try:
		Start()
	except:
		import traceback
		traceback.print_exc()
	print "end"
	raw_input()

