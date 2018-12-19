Alpha=[]
Alpha2=[]
matrix=[[],[],[],[],[]]
key=raw_input()
plain=raw_input() # L A J R 
plain=plain.replace("J","I")


key=key.replace("J","I")

for  L in key:
	Alpha=Alpha+[L]	

x = 0
flag=False
while x<26 :
	for L in key:
		if L==chr(65+x):
			flag=True
		#	print("already there")
		elif chr(65+x)=='J':
			flag=True
	if flag!=True:
		Alpha=Alpha+[chr(65+x)]
	flag=False		
	x+=1

x = 0
while x<25:
	for L in Alpha:
		if L not in Alpha2:
			Alpha2=Alpha2+[L]
	x+=1	
x=0
y=0
n=0
while x<5:
	while y<5:
		matrix[x]=matrix[x]+[Alpha2[n]]
		'''if y<4:
			print(matrix[x][y]+" "),
		else:
			print(matrix[x][y]+" ")'''
		n+=1
		y+=1
	x+=1
	y=0	

i=0
plain2=""
while i<len(plain):
	if i+1<len(plain):
			if plain[i]!= plain[i + 1]:
				plain2 = plain2 + plain[i] 
				plain2 = plain2 + plain[i + 1]
			elif plain[i] == plain[i + 1] and plain[i]=='X':
				plain2 = plain2 + plain[i] 
				plain2 = plain2 + 'Q'
				i-=1
			else:
				plain2 = plain2 + plain[i]
				plain2 = plain2 + 'X'
				i-=1
	else:
		if plain[i] != 'X':
			plain2 = plain2 + plain[i]
			plain2 = plain2 + 'X'
		else:
			plain2 = plain2 + plain[i]
			plain2 = plain2 + 'Q'
	i+=2

#print(plain2)		
cipher=""
x1,x2,y1,y2=0,0,0,0

i=0
while i<len(plain2):
	if i+1<len(plain2):

		for  m,Mat in enumerate(matrix):
			for n,var in enumerate(Mat):
				if plain2[i] == var:
					x1=m
					y1=n
				if plain2[i+1] == var:
					x2=m
					y2=n	

		if x1==x2:

		#if y1<y2:
			cipher=cipher+matrix[x1][(y1+1)%5]
			cipher=cipher+matrix[x1][(y2+1)%5]
			'''else:
				cipher=cipher+matrix[x1][(y2+1)%5]
				cipher=cipher+matrix[x1][(y1+1)%5]'''
		elif y1==y2:

			#if x1<x2:
			cipher=cipher+matrix[(x1+1)%5][y1]
			cipher=cipher+matrix[(x2+1)%5][y1]
			'''else:
				cipher=cipher+matrix[(x2+1)%5][y1]
				cipher=cipher+matrix[(x1+1)%5][y1]'''
		else:
			cipher=cipher+matrix[x1][y2]
			cipher=cipher+matrix[x2][y1]
	i+=2
print(cipher)