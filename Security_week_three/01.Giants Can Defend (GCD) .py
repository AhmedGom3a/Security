inp = raw_input()
inp= inp.split(" ")
inp[0]=int(inp[0])
inp[1]=int(inp[1])
flag=True

while flag:
	lastTemp=inp[1]
	temp=inp[0]%inp[1]
	#print(" {x} |  {y} ".format(x=inp[0],y=inp[1]))
	inp[0]=inp[1]
	inp[1]=temp	
	if temp == 0 :
		flag=False

#print(" {x} |  {y} ".format(x=inp[0],y=inp[1]))
print(lastTemp)