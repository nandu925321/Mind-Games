import re

s = 'asdf=5;iwantthis123jas'
result = re.search('asdf=5;(.*)123jasd', s)
if(result==None):
	print("no pattern")
else:
	print (result.group(1))