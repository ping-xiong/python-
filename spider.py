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
        sql = "SELECT `classCode` FROM `class`"
        cursor.execute(sql)
        resultClassCode = cursor.fetchall()
        # for x in resultClassCode:
        #     print(x["classCode"])
        # pass
    
finally:
    # connection.close()
    i = 0
    pass

for x in resultClassCode:
    classCode = x["classCode"]
    # print("classCode = ",classCode)
    for y in resultSemester:
        semester = y["semester"]
        # print("Semester = ",semester)
        gradeClassCode = int(classCode[0]+classCode[1])
        gradeSemester = int(semester[0]+semester[1])
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `classCode`,`semester` FROM `timetable` WHERE classCode='"+classCode+"' AND semester='"+semester+"'"
                cursor.execute(sql)
                resultRepeat = cursor.fetchone()
        finally:
            # connection.close()
            pass
        if (gradeSemester >= gradeClassCode) and (gradeSemester <= gradeClassCode+3):
            if resultRepeat is None:
                arr = [classCode,semester]
                print(arr)
                spider_classTable.insertTameTable(classCode,semester)
            else:
                print("The timetable had already exist")
            i += 1
            print(i,"Processing...")