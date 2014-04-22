import time
import getpass
from operator import add
from modules.user_end import get_input, get_Y_N
import modules.connector

def ugc_parser(data):
	raw_html = modules.connector.BeautifulSoup(data)
	raw_td_iter = iter(raw_html.find_all('td'))
	raw_td_list = raw_html.find_all('td')
	subjt_index = -1
	ugclist = list()
	while True:
		try:
			temp = raw_td_iter.next().get_text()
			subjt_index = subjt_index + 1	
			units = float(temp)
			temp = raw_td_iter.next().get_text()
			subjt_index = subjt_index + 1	
			if("INC" in temp):
				temp = temp.replace("\t","")
				temp = temp.replace("\n","")
				if(len(temp)==11):
					temp = temp[6:10]
			grade = float(temp)
			if(grade>=1 and grade<=5 and grade !=4):
				subject = raw_td_list[subjt_index-3].string
				subject = subject.replace("\r","")
				subject = subject.replace("\n","")
				subject = subject.replace("\t","")
				ugclist.append(((units,grade),subject))
		except StopIteration:
			break
		except ValueError:
			continue	

	counter = len(ugclist)-1
	while(counter>=0):
		temp_units = 0
		sem_units = ugclist[counter][0][0]
		ugclist.pop(counter)
		counter = counter-1
		while(temp_units<sem_units):
			temp_units = temp_units + ugclist[counter][0][0]
			counter = counter-1
		
	return ugclist 

def tgwac_quick(ugclist):
	a = reduce(add,list(reduce(lambda x,y: x*y, el[0]) for el in ugclist))
	b = reduce(add,list(reduce(lambda x,y: x, el[0]) for el in ugclist))
	tgwa = a/b
	return tgwa 


if __name__ == "__main__":
	connector = modules.connector
	print "Enter CRS username: " 
	username = get_input()
	print "Enter CRS password: "
	password = getpass.getpass()
	site_opener = connector.site_connect('https://crs.upd.edu.ph/auth','txt_login',username,'pwd_password',password)
	if(site_opener != 0):
		print "\nLogin Successful..."
		crawl_data = connector.site_crawl("https://crs.upd.edu.ph/viewgrades",site_opener)
		ugc_list = ugc_parser(crawl_data.read())
		tgwa = tgwac_quick(ugc_list)
		print "\nTGWAC Quick Analysis results say your Total GWA is " + str(tgwa)
		user_input = get_Y_N("Do you want to proceed to the a more thorough evaluation?")
		if(user_input.upper()=="Y"):
			print "\nLoading subjects considered in TGWA computation..."
			time.sleep(2)
			for i in ugc_list:
				print i
				time.sleep(0.5)
			#user_input = get_Y_N("From the subjects considered, are there any that are not supposed to be considered?")
		else:
			print "\nCRS-TGWAC Session Closed"

	else:
		print "Login Failed. Re-run program"