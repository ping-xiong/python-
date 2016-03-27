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
def sqlLink(semester):
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `semester` (`semester`) VALUES (%s)"
			cursor.execute(sql, (semester))
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
	arr = soup.find(id="DDxq").find_all("option")
	for x in arr:
			ch = x.get_text()
			print(ch)
			sqlLink(str(ch))
else:
	print ("failed")
