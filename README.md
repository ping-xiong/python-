# python-Guangxi-University-Of-Technology-Timetable
python抓取广西科技大学教务信息系统课程表
##特性
1.中途退出程序再次运行不会抓取到重复课程表 (多线程爬虫无效)
2.使用MySQL数据库储存数据，方便管理课程表

##使用要求
1.已安装MYSQL数据库
2.安装python插件beautiful soup
3.安装另一个插件PyMySQL

##数据库文件
python.sql
导入数据表

##更新
2017/9/12
更新多线程爬虫！文件为：text_threadring.py
爬取效率极大提高！仅需两节课就可以爬取所有的课程表数据

##运行顺序
1. spiderForSemester.py 获取学期列表
2. spiderForClass.py 获取班级列表
3. text_threadring.py  使用多线程抓取课程表

##关于使用教程
点击进入[我的博客](https://pingxonline.com)查看, 或者点击链接：https://pingxonline.com

##课程表web应用
[查询课程表](https://pingxonline.com/app/timetable/)
