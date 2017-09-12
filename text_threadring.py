# -*- coding: utf-8 -*-

import threading
from time import ctime,sleep
import pymysql.cursors
import spider_classTable

connection = pymysql.connect(
	host='localhost',
	user='root',
	password='',
	db='python',
	charset="utf8",
	cursorclass=pymysql.cursors.DictCursor)

try:
    ### get all semester
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `semester`"
        cursor.execute(sql)
        resultSemester = cursor.fetchall()
        # for x in resultSemester:
        #     print(x["semester"])
        #     pass
    ### get all classCode
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `class`"
        cursor.execute(sql)
        resultClassCode = cursor.fetchall()
        # for x in resultClassCode:
        #     print(x["classCode"])
        # pass
    
finally:
    # connection.close()
    i = 0
    pass
threadArr = []
for x in resultClassCode:
    classCode = x["classCode"]
    # print("classCode = ",classCode)
    for y in resultSemester:
        semester = y["semester"]
        # print("Semester = ",semester)pip install PyMySQL
        gradeClassCode = int(classCode[0]+classCode[1])
        gradeSemester = int(semester[0]+semester[1])
        if (gradeSemester >= gradeClassCode) and (gradeSemester <= gradeClassCode+3):
            arr = [classCode,semester]
            threadArr.append(arr)
            # print(arr)
            i += 1

print (len(threadArr))
threads = []
# print(threadArr)
for h in threadArr:
	t1 = threading.Thread(target=spider_classTable.insertTameTable,args=(h[0],h[1],))
	threads.append(t1)
	pass

# 总数
total = len(threadArr)
if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
		# 总数减一
		total -= 1
		print("%s left!!!!!!" %total)
		while True:  
			#判断正在运行的线程数量, 如果小于 50 则退出 while 循环,  限制数据库最大链接数
			#进入 for 循环启动新的进程. 否则就一直在 while 循环进入死循环  
			if(len(threading.enumerate()) < 50 or total == 0):
				break
	
	t.join()

print ("all over %s" %ctime())
# spider_classTable.insertTameTable(classCode,semester)