import sys
import timeit
import os
from os import path
from datetime import datetime
import pickle


def alter(user):
	file_name = open("preferences.dat", "rb") 
	data = pickle.load(file_name)
	for i in data:
		if(i==user):
			user_data = data[i]
			break
	
	print("Current tags:\n", user_data[0])
	
	tag = input("Which tag would you want to change?: ")
	idx = 0
	loc = -1
	for i in user_data[0]:
		if(i==tag):
			loc = idx
		idx += 1
	
	if(loc == -1):
		print("Invalid tag please try again.")
	else:
		new_tag = input("Enter new tag: ")
		user_data[0][loc] = new_tag
		print("New tag list:", user_data[0])
		print("Operation successful")
		data[i] = user_data
		file_name.close()
		file_name = open("preferences.dat", "wb")
		pickle.dump(data, file_name)
		file_name.close()
			
	menu(user)
		

def publish(user):
	start = timeit.default_timer() 

	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M")
	title = input("Enter title")

	tags = eval(input("enter the tags you want to put the blog in ['tag1', 'tag2']: "))
	for z in range(0, len(tags)):
	
	    write_to = tags[z] 
	
    
	    print(path.exists(write_to+'.html'))
	    if(path.exists(write_to+'.html')==False):
	        desc = input("Enter new board's description")
	        index = open("index.html", "r")
	        ch = 1
	        tmp = tmp2 = tmp3 = ''
	
	        for line in index:
	            if(ch>=18):
	                tmp2+=line
	            else:
	                tmp3+=line
	            ch+=1
	
	        index = open("index.html", "w")
  	      
	        tmp = tmp3 + '<div class = "entry"><p><a href="'+write_to+'.html">'+write_to+'</a>:'+desc+'</p></div>' + tmp2
	
	        html = open(write_to+'.html', 'w')
	        index.write(tmp)
	
	        tmp = tmp3 + '\n' + '</body> </html>'
	        html.write(tmp)
	        html.close()
	        index.close()
	
	    write_to += '.html'
	    html = open(write_to, "r")
	    main = open("blog.txt", "r")
	    i = j = 1
	    s = s2 = ''
	
	    for line in html:
	        if(j>=18):
	            s2+=line
	        j+=1
	
	    html.close()
	    html = open(write_to, "r")
	
	    for line in html:
	        if(i==18):
	            html.close()
	            html = open(write_to, "w")
	            text = main.read()
	            s1 = '<h2 id=\''+title+'\'>'+ title + '</h2><small>[<a href="blog/'+title+'.html">standalone</a>]</small>'
	            s1 += '<div class = "tag"><small><b>Tags: </b>'
	            for q in range(1, len(sys.argv)):
	                s1 += sys.argv[q] + ' '
	            s1 +='</small></div><p>' + text + '</p> <small>' + dt_string + ' ' + datetime.today().strftime('%A') + '</small>'
	            s1 = '<div class = "entry">' + '\n' + s1 + '</div>'
	
	            indie = open('blog/'+title+'.html', 'w')
	            indie.write(s1)
	
	            s += s1 + s2 
	            html.write(s)
	            html.close()
	            break
	        s += line
	        i+=1
	   
	cmd = "git add . && git status -s && git commit -m " + 'BLOG' + " && git push origin master"
	
	os.system(cmd)
	
	stop = timeit.default_timer()
	print('Operation Successful. Time taken: ', stop - start) 
	




def menu(user):
	#the core part :D
	#all the options and preferences will be here
	#lets start out slow and put the basics here first
	ch = int(input('''
	1. Publish blog(everything written in blog.txt)
	2. Alter default tags
	:'''))
	if(ch==1):
		publish(user)
	elif(ch==2):
		alter(user)
	else:
		exit()


def set_preferences(user):
	old_tags = ['<b>','<strong>','<i>','<em>','<mark>','<small>','<del>','<ins>','<sub>','<sup>']
	old_tags.sort()
	file_name = open("preferences.dat", "rb")
	try:
		data = pickle.load(file_name)
		tags = list()
		tags.append(old_tags)
		tags.append(old_tags) #new_tags
		data[user] = tags
		file_name.close()
		file_name = open("preferences.dat", "wb")
		pickle.dump(data, file_name)
		file_name.close()
	except:
		file_name.close()
		tags = list()
		tags.append(old_tags)
		tags.append(old_tags) #new_tags
		data = dict()
		data[user] = tags
		file_name = open("preferences.dat", "wb")
		pickle.dump(data, file_name)        
		file_name.close()


def make_default(user):
	name = user + '.html'
	index = open(name, "w")
	data = open("default.html", "r")
	lines = ''
	for line in data:
		lines += line
	index.write(lines)
	index.close()
	data.close()  




def setup(user):
	def1 = '''<html>

<head>

<title>The Simple Blog</title>

<meta charset="utf-8"/>

<link rel='stylesheet' type='text/css' href='style.css'>

</head>

<body style='font-family="Courier"'>
	
<h1 style="color:black">A Website(?)</h1>

<p>Navigation</p>
'''    
	def2 = '''</body> </html>
'''
	d = dict()
	#if not os.path.exists(os.path.dirname("./store.dat")):
	f = open("style.css", "r")
	s = f.read()
	f.close()

	pathb = os.path.dirname(os.path.abspath(__file__))
	print(pathb)
	path = pathb + '\\' + user #+"/style.css"

	try:
		os.makedirs(path)
	except OSError:
		print ("Creation of the directory %s failed" % path)
	else:
		print ("Successfully created the directory %s " % path)

	f = open(path+"/style.css", "w")
	f.write(s)
	f.close()
	try:
		store = open("store.dat", "rb")
		d = pickle.load(store)
		store.close()
		#os.makedirs(os.path.dirname("./store.dat"))
		#store = open("store.dat", "wb")
		#store.close()

		store = open("store.dat", "wb")
		l = list()
		l.append(def1)
		l.append(def2)
		d[user] = l
		pickle.dump(d, store)
		store.close()

	except:
		store = open("store.dat", "wb")
		l = list()
		l.append(def1)
		l.append(def2)
		d[user] = l
		pickle.dump(d, store)
		store.close()
	


def signup(user):
	file_name = open("user_data.dat", "rb")
	try:
		data = pickle.load(file_name)
		if(data.get(user)):
			print("username exists, please retry")
			file_name.close()
			return
		else:
			password = input("choose password: ")
			data[user] = password
			print("USER REGISTERED, please login now to use account")
			file_name.close()
			file_name = open("user_data.dat", "wb")
			pickle.dump(data, file_name)
			file_name.close()
			set_preferences(user)
			make_default(user)
			#put_on_page(user)
			setup(user)
	except:   
		data = dict()
		password = input("choose password: ")
		data[user] = password
		print("USER REGISTERED, please login now to use account")
		file_name = open("user_data.dat", "wb")
		pickle.dump(data, file_name)
		file_name.close()    
		set_preferences(user)
		make_default(user)
		#put_on_page(user)
		setup(user)
	interface()
			

def login(user):
	file_name = open("user_data.dat", "rb")
	data = pickle.load(file_name)
	#print(data)
	password = input("enter password: ")
	if(data.get(user) and data[user] == password):
		print("LOGIN SUCCESSFUL")
		#go on and do things
		#basically interface #2 should start from here
		#which will allow blog writing 
		#will ask to enter blog name if opened for the first time
		#then username and blogname will be published on the main page of the website(to be done later)
		file_name.close()
		menu(user) #WIP

	elif(not data.get(user)):
		print("please signup first")
		file_name.close()
		interface()
	else:
		print("PASSWORD DOES NOT MATCH PLEASE RETRY")
		file_name.close()
		interface()



def interface():
	ch = input("(s)ignup/ (l)ogin: ")
	user = input("enter username: ")      
	if(ch=='s'):
		signup(user)
	elif(ch=='l'):
		login(user)
	elif(ch=='setup'):
		setup()
	else:
		#user made error show menu again
		#interface()                        
		exit() #for now, to avoid problems

interface() #login/signup

