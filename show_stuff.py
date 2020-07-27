s = input("enter filename\n>>")
print(s+".dat")
f = open(s+".dat", "rb")

while True:
	try:
		data = pickle.load(f)
		print(data)
	except:
		break