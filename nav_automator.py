import re
import os

# place this file in your image directory and double-click

def automate():
    '''automate production of the js nav for pngs'''
    current_d = os.getcwd()
    file_list = os.listdir(current_d)    
    html_list = []

    file_list.sort()    # sorts the files by 00, 01, 02...        
    for i in file_list: # for each image in the image list
		if i.lower().startswith("."):
			file_list.remove(i)
        	name = i[:-4]   # slice the last 4 characters (file extension) for the name
 		if i.lower().endswith("jpg") or i.lower().endswith("png") or i.lower().endswith("gif"): # grabs jpg, png or gif files to put into the list
			html_list.append('''<a href="%s" onclick="showimg(this);return false">%s</a><br/>''' % (i, name))   # replace the variables with file/names
    
    return html_list

# outputs the html page with the automated image list
 
def save_html(title):
    '''print out the rest of the html with the automated jq_nav.'''
    html = automate()   # puts the looped href list with images into a variable
    
# puts the rest of the html into another variable

    file_obj = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<title>%s</title>
<meta http-equiv="imagetoolbar" content="no">
<style type="text/css">
<!--
#mainimg {border:none;}
body	{
	font-family: Verdana;
	font-size: 67%%;
	color: #3E3B40;
	margin: 0px;
	}

p	{
	margin-top: 0px; 
	margin-bottom: 2px;
	}
#navpane	{
	position:fixed;
	padding: 5px 7px 6px 7px;
	right:0px;
	top:0px;
	line-height:140%%;
	background-color:#FFFFFF;
	border-left: solid 1px #BBBBBB;
	border-bottom: solid 1px #BBBBBB;
	}
#menubtn	{
	position:fixed;
	padding: 2px;
	right:0px;
	top:0px;
	line-height:140%%;
	background-color:#FFFFFF;
	border-left: solid 1px #BBBBBB;
	border-bottom: solid 1px #BBBBBB;
	cursor: pointer
	}
.hidemenu {
	cursor: pointer;
	text-align: center;
	}
.sel    {background-color:#EEEEEE};
a          {color:#88818C; text-decoration:none}
a:link     {color:#88818C; text-decoration:none}
a:visited  {color:#88818C; text-decoration:none}
a:active   {color:#88818C; text-decoration:none}
a:hover    {color:#4D33CC; text-decoration:none}
h2 { font-size: 12px; }
-->
</style>
<script type="text/javascript">
<!--
var nextnum = 0;
var currenta;
var currentimg;
var hreflist = document.getElementsByTagName('a');
function hidemenu() {
	document.getElementById("navpane").style.display = "none";
	document.getElementById("menubtn").style.display = "block";
	}
function showmenu() {
	document.getElementById("navpane").style.display = "block";
	document.getElementById("menubtn").style.display = "none";
	}
function showfirst() {
	hreflist[0].className = "sel";
	currenta = hreflist[0];
	currentimg = hreflist[0].getAttribute("href",2);
	document.getElementById("mainimg").setAttribute("src", currentimg);
	}
function showimg(imgpathobj) {
	hreflist[nextnum].className = "";
	imgpath=imgpathobj.getAttribute("href",2);
	currenta.className = "";
	imgpathobj.className = "sel";
	currenta = imgpathobj;
	document.getElementById("mainimg").setAttribute("src", imgpath);
	currentimg=imgpath;
	window.scroll(0,0);
	}
function shownext() {
	for (var B = 0; B < hreflist.length; B++) {
		if(hreflist[B].getAttribute("href",2)==currentimg){
			currenta.className = "";
			hreflist[nextnum].className = "";
			nextnum = (B < hreflist.length-2) ? B+1 : 0;
			hreflist[nextnum].className = "sel";
			//window.status = hreflist[nextnum].className;
			currentimg=hreflist[nextnum].getAttribute("href",2);
			document.getElementById("mainimg").setAttribute("src", currentimg);
			window.scroll(0,0);
			return;
		};
	}
	}

// -->
</script> 
</head>
<body onload="showfirst()">
  <div id="menubtn" onclick="showmenu()">menu</div>
  <div id="navpane">
    <div onclick="hidemenu()" class="hidemenu">&nbsp;  &nbsp; ^ &nbsp; &nbsp;</div>

<!-- ENTER NAV LIST FROM PYTHON SCRIPT HERE -->
%s
<!-- END NAV LIST -->

  </div>

  <a id="nextlink" href="javascript:shownext()"><img id="mainimg" alt="" src="" /></a>

</body>
</html>
''' % (title, '\n'.join(html))              # replaces the string title with the title given in the prompt and the href in the other string replacement
    html_file = open("index.html", "w")     # creates an index.html file; to change the name of the file, just change "index.html" to "your_filename.html"
    html_file.writelines(file_obj)          # writes all html lines into the file
    html_file.close                         # closes the html file
 

if __name__ == "__main__":
    title = raw_input("Enter your page title for the HTML (ie, Project 1): ")
    automate()
    save_html(title)
        
    








    
