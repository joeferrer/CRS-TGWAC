import time
import getpass
import modules.connector
from modules.crs_tgwac_fxns import ugc_parser,tgwac,honor_eval
from modules.user_end import get_input, get_Y_N

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
		ugc_list = ugc_parser(connector.BeautifulSoup(crawl_data.read()))
		tgwa = tgwac(ugc_list)
		print "\nTGWAC Quick Analysis results say your Total GWA is " + str(tgwa)
		user_input = get_Y_N("Do you want to proceed to a more thorough evaluation?")
		if(user_input.upper()=="Y"):
			print "\nLoading subjects considered in TGWA computation..."
			time.sleep(2)
			for i in ugc_list:
				print i
				time.sleep(0.5)
			user_input = get_Y_N("From the subjects considered, are there any that shouldn't be counted?")
			if(user_input.upper()=="Y"):
				print "\nUsing the subjects listed above, type the subjects that must not be counted. (e.g. Math 17 THV)"
				takeouts = list()
				takingout = True
				while(takingout):
					takeouts.append(get_input())
					user_input = get_Y_N("Is that all?")
					if(user_input.upper()=="Y"):
						takingout = False
					else:
						print "What other subject/s must be disregarded?"
				for i in takeouts:
					for j in ugc_list:
						if i in j:
							ugc_list.remove(j)
				tgwa = tgwac(ugc_list)
			user_input = get_Y_N("Have you ever had an underload sem?")
			if(user_input.upper()=="Y"):
				underload = True
			else:
				underload = False
			print "\nAnalyzing gathered information..."
			time.sleep(2)
			honor_eval(tgwa,underload)

		time.sleep(3)
		print "\n\nCRS-TGWAC Session Closed"

	else:
		print "Login Failed. Re-run program"
