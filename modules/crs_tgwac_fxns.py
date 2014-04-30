from operator import add

def ugc_parser(data):
	raw_td_iter = iter(data.find_all('td'))
	raw_td_list = data.find_all('td')
	counter = -1
	ugclist = list()

	while True:
		temp = units = subject = ""
		try:
			temp = raw_td_iter.next().get_text()
			counter = counter + 1
			if(len(temp)>1):	
				units = float(temp)
			else:
				continue
			temp = raw_td_iter.next().get_text()
			counter = counter + 1
			subject = str(raw_td_list[counter-3].string)
			grade = float(temp)
			ugclist.append(((units,grade),subject))
		except StopIteration:
			break
		except ValueError:
			if((("4.00" in temp) or "INC" in temp or "DRP" in temp or temp.isspace())and type(units) is float):
				ugclist.append(((units,temp),subject))

	counter = len(ugclist)-1
	while(counter>=0):
		temp_units = 0
		sem_units = ugclist[counter][0][0]
		ugclist.pop(counter)
		counter = counter-1
		while(temp_units<sem_units):
			temp_units = temp_units + ugclist[counter][0][0]
			counter = counter-1
			

	counter = 0
	while(counter<len(ugclist)):
		try:
			if("(" in ugclist[counter][0][1]):
				p_index = ugclist[counter][0][1].index("(")
				ugclist[counter] = ((ugclist[counter][0][0],float(ugclist[counter][0][1][p_index+1:p_index+5])),ugclist[counter][1])
			else:
				ugclist.pop(counter)
				counter = counter -1
		except:
			pass
		counter = counter + 1

	return ugclist 

def tgwac(ugclist):
	a = reduce(add,list(reduce(lambda x,y: x*y, el[0]) for el in ugclist))
	b = reduce(add,list(reduce(lambda x,y: x, el[0]) for el in ugclist))
	tgwa = a/b
	return tgwa 

def honor_eval(tgwa,underload):
	print "\n\nTGWAC-Deeper-Analysis says your Total GWA is "  + str(tgwa)
	if(underload==False):
		if(tgwa<=1.75):
			award = ""
			if(tgwa<=1.2):
				award = "Summa Cum Laude."
			elif(tgwa<=1.45):
				award = "Magna Cum Laude."
			else:
				award = "Cum laude."
			print "Congratulations, if you don't have any disciplinary issues or the like, you are a candidate for " + award
		else:
			print "Your Total GWA is not (yet) for latin honors, but don't despair, you can still do better and be great!"
	else:		
		print "You are not eligible for honors since you had an underloaded sem, but don't despair, the road to greatness does not stop there!"