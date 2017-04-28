f = open("./data/雪国.txt",'r', encoding='UTF-8')
line = f.readline()
while line:
	print(line, end = '')
	line = f.readline().replace("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）.:.%]-->「://..//.?=","")
f.close()
