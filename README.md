#CRS-TGWAC#
<br/>
##About
__CRS__-TGWAC (__Total Grade Weighted Average Computer__) is a/an app/personal programming project by Joe Ferrer to help UPD students effectively and efficiently compute for their TGWA (Total GWA) and keep good track of their academic performance in the university. CRS-TGWAC is a project that aims to answer constant/consistent problems in other TGWACs which are unreliable due to inflexibility to changes at the __<a href="https://crs.upd.edu.ph">CRS website</a>__, client-side dependencies, and computational errors derived from different sources. CRS-TGWAC simply asks for the user's CRS _username_ and _password_ and it automatically and securely (_using a one time session-id/cookie_) connects to the CRS website, accessing the html code of the user's grades and corresponding units taken, parsing that code, and coming up with a quick analysis, i.e a quick TGWA computation.
##Development
CRS-TGWAC is already functional at least to its minimum task of quickly computing a user's TGWA. __Quick analysis__ grades-units correspondence/TGWA __follows these rules__:
<br>
<br>
1. PE units and grades are not counted
<br>
2. Subjects with 'INC's without any grade are not counted
<br>
3. Subjects that are beyond a student's curriculum (i.e. student-added/personal electives) w/c the student took are still considered in the quick TGWA computation.
<br>
4. Quick TGWA Mathematical Formula:
<br>
>
>Quick TGWA =&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total (Units*Grade)
><br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;------------------------------------------------------------ <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Total (Units)
<br>
<br>

As of the moment CRS-TGWAC is being developed/ debugged/ tested/ improved by the creator, Joe Ferrer, only. Comments/ Suggestions /Insights/ Conributions are very welcome.

__Added Dev Notes__:
<br>
CRS-TGWAC is programmed using the Python programming language partnered with a popular external html parsing library,BeautifulSoup. CRS-TGWAC is still under development and will have a more detailed analysis/ evaluation/ computation of a student's TGWA. 

######TGWAC-Deeper-Analysis Feature (Existing)

>
- Showing all the subjects included in the computation
<br>
- Removing student-added/personal electives through user-input and list search for more accurate TGWA computation
<br>
- Assessing a user's candidacy for graduating with honors (only considering TGWAC and having satisfied minimum load/units per sem)


######TGWAC-Report Feature (Coming Soon)
>
- Publishing a formal document.


##Usage
In order to use CRS-TGWAC you must first __download the ZIP file__ of this repository or __pull this repository__ from github. Assuming you don't have python installed yet in your OS, you can download python __<a href="https://www.python.org/download/">by clicking this link.</a>__ Choose the appropriate one for your OS. The preferred version is 2.7.X, X={0,...,9} but other versions higher than 2.6 will do. To __install Python__, just follow the installation instructions specified there. Next and last, you must __install BeautifulSoup4__ ,the external html parsing library used for parsing the html code accessed from the CRS website. BeautifulSoup4 can be downloaded __<a href="http://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/">at this link</a>__  ,but is also available in this repository, located at the '\_installs' directory. Just extract the compressed file and install by following the instructions __<a href="http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup">here</a>__ (Unix/Mac OS) or __<a href="http://stackoverflow.com/questions/12228102/how-to-install-beautiful-soup-4-with-python-2-7-on-windows">here</a>__ (Windows OS)
<br>
<br>
When you're done dealing with the dependencies, just double click CRS.py or run it via your command prompt and all is well.

<br/>
