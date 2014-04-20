
import getpass
import modules.connector
from modules.user_end import get_input



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
		contents = crawl_data.read()
		f = open("CRS.txt","w")
		f.write(contents)
		f.close()
	else:
		print "Login Failed. Re-run program"