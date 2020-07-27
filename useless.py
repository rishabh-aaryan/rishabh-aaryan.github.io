import pickle

user = 'zoo'

old_tags = ['<b>','<strong>','<i>','<em>','<mark>','<small>','<del>','<ins>','<sub>','<sup>']
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

file_name = open("preferences.dat", "rb")
data = pickle.load(file_name)
print(data)