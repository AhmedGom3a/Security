PC1 =[ 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]

PC2 =[ 14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]

Rotations =[ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

IP_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
P  = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25 ]
E  = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
s = [
	[
	  [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
	  [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
	  [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
	  [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
	],
	[
	  [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
	  [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
	  [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
	  [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
	],
	[
	  [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
	  [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
	  [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
	  [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
	  ],
	[
	  [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
	  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
	  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
	  [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
	],
	[
	  [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
	  [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
	  [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
	  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
	],
	[
	  [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
	  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
	  [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
	  [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
	],
	[
	  [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
	  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
	  [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
	  [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
	],
	[
	  [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
	  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
	  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
	  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
	]]

def initPer(temp):
	global IP
	plain=list(temp)
	bina=""
	for hexa in plain:
		bina=bina+bin(int(hexa, 16))[2:].zfill(4)
	bintext=list(bina)
	op=""
	x=0
	while x<len(IP) :
		op=op+bintext[int(IP[x])-1]
		x+=1
	'''op=[op[i:i+4] for i in range(0, len(op), 4)]
	output=""	
	for binn in op:
		temp=hex(int(binn,2))[2:].zfill(1)
		output=output+temp.upper()'''
	return op
def DESfun(bininpt,binkey):
	'''inpt=list(inpt)
	key2=list(key2)

	bininpt=""
	for element in inpt:
		bininpt=bininpt+bin(int(element, 16))[2:].zfill(4)
	print(bininpt)
	binkey=""
	for element in key2:
		binkey=binkey+bin(int(element, 16))[2:].zfill(4)
	'''
	Eop=[]
	for num in E:
		Eop=Eop+[bininpt[num-1]]

	x=0
	binxored=""
	while x<48:
			binxored=binxored+str((int(Eop[x],2))^(int(binkey[x],2)))
			x+=1
			
	binxored=[binxored[i:i+6] for i in range(0,len(binxored),6)]
	head=0
	tail=0
	mid=0
	x=0
	op=""
	row=""
	for element in binxored:
		head=element[0]
		tail=element[5]
		mid=element[1:5]
		row=head+tail
		col=int(mid, 2)
		row=int(row,2)
		op=op+bin(s[x][row][col])[2:].zfill(4)
		x+=1

	Fop=""
	for num in P:
		Fop=Fop+op[num-1]

	'''Fop=[Fop[i:i+4] for i in range(0, len(Fop), 4)]
	output=""	
	for binn in Fop:
		temp=hex(int(binn,2))[2:].zfill(1)
		output=output+temp.upper()'''
	return Fop
def invinitPer(bintext):
	global IP_1
	'''plain=list(temp)
	bina=""
	for hexa in plain:
		bina=bina+bin(int(hexa, 16))[2:].zfill(4)
	bintext=list(bina)'''
	op=""
	x=0
	while x<len(IP_1) :
		op=op+bintext[int(IP_1[x])-1]
		x+=1
	op=[op[i:i+4] for i in range(0, len(op), 4)]
	output=""	
	for binn in op:
		temp=hex(int(binn,2))[2:].zfill(1)
		output=output+temp.upper()
	return output
def keyGenerator(array):
	global allakeys
	array=list(array)
	bina=""
	for ele in array:
		bina=bina+bin(int(ele, 16))[2:].zfill(4)
	bintext=list(bina)

	op56=""
	x=0
	while x<len(PC1) :
		op56=op56+bintext[int(PC1[x])-1]
		x+=1


	left=op56[0:28]
	right=op56[28:]
	left=list(left)
	right=list(right)
	total=""
	key=""
	output=""
	temp=[[0,0],[0,0]]
	temp1=""
	main=0
	while main<16:
		total=""
		temp[0][0]=left[0]
		temp[0][1]=left[1]
		temp[1][0]=right[0]
		temp[1][1]=right[1]

		for n,el in enumerate(left):
			if(n+Rotations[main]<len(left)):
				left[n]=left[n+Rotations[main]]
			elif Rotations[main]==2:
				left[len(left)-2]=temp[0][0]
				left[len(left)-1]=temp[0][1]
			elif Rotations[main]==1:
				left[len(left)-1]=temp[0][0]
			total=total+left[n]

		for n,el in enumerate(right):
			if(n+Rotations[main]<len(right)):
				right[n]=right[n+Rotations[main]]
			elif Rotations[main]==2:
				right[len(right)-2]=temp[1][0]
				right[len(right)-1]=temp[1][1]
			elif Rotations[main]==1:
				right[len(right)-1]=temp[1][0]
			total=total+right[n]

		x=0
		key1=""
		while x<len(PC2) :
			key1=key1+total[int(PC2[x])-1]
			x+=1

		'''output=""
		key1=[key1[i:i+4] for i in range(0, len(key1), 4)]	
		for binn in key1:
			temp1=hex(int(binn,2))[2:].zfill(1)
			output=output+temp1.upper()'''
		allakeys=allakeys+[key1]
		main+=1

allakeys=[]
key=raw_input()
keyGenerator(key)
plainT=raw_input()
rounds=input()
times=0
cipher=plainT
while times<rounds:
	PTIP=initPer(cipher)
	PTIP_Left=PTIP[0:32]
	PTIP_Right=PTIP[32:]
	roundnum=0
	roundinpt=PTIP_Right[:]
	roundop=""
	while roundnum<16:
		roundop=DESfun(roundinpt,allakeys[roundnum])
		roundinpt=bin((int(roundop,2))^(int(PTIP_Left,2)))[2:]
		if(len(roundinpt)<32):
			roundinpt=(32-len(roundinpt))*"0"+roundinpt
		PTIP_Left=PTIP_Right
		PTIP_Right=roundinpt
		roundnum+=1
	cipher=invinitPer(PTIP_Right+PTIP_Left)
	times+=1
print(cipher)