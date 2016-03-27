import urllib
import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors

connection = pymysql.connect(
	host='localhost',
	user='root',
	password='',
	db='python',
	charset="utf8",
	cursorclass=pymysql.cursors.DictCursor)
def sqlLink(clssName,classCode,grade):
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `class` (`className`,`classCode`,`grade`) VALUES (%s,%s,%s)"
			cursor.execute(sql, (clssName,classCode,grade))
			connection.commit()
	finally:
		# connection.close()
		pass
	return

response = urllib.request.urlopen('http://202.193.177.7:8081/(S(abwuq2ufugzg1y55p5obk5br))/web_jxrw/cx_kb_bjxzall.aspx')
if response.code == 200:
	print ("succeed",response.code)
	html = response.read()
	soup = BeautifulSoup(
		html,
		'html.parser',
		from_encoding = 'gb2312')
	arr = soup.find(id="Cxbj_all1_bjlist1").find_all("option")
	for x in arr:
			ch = x.get_text()
			classCode = x['value']
			last = x['value'][0]+x['value'][1]
			if last == "98":
				grade = "19"+last
				pass
			else:
				grade = "20"+last
			print(classCode)
			sqlLink(str(ch),classCode,grade)
else:
	print ("failed")
