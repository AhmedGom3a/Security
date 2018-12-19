Alpha=[]
Alpha2=[]
matrix=[[],[],[],[],[]]
plain=raw_input() 
cipher1=raw_input()
plain=plain.replace("J","I")
import itertools
All=list(itertools.permutations(["A","B","C","D","E","F","G","H","I"]))


x = 0
while x<9 :
	if chr(65+x)!='J':
		Alpha=Alpha+[chr(65+x)]	
	x+=1
			
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
count=0	
cipher=""
	
g=0
key=""
while cipher!=cipher1:
	x=0
	y=0
	n=0
	matrix=[[],[],[],[],[]]
	while x<3:
		while y<3:
			matrix[x]=matrix[x]+[All[count][n]]
			'''if y<2:
				print(matrix[x][y]+" "),
			else:
				print(matrix[x][y]+" ")'''
			n+=1
			y+=1
		x+=1
		y=0

	
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

			
				cipher=cipher+matrix[x1][(y1+1)%3]
				cipher=cipher+matrix[x1][(y2+1)%3]
				
			elif y1==y2:

				
				cipher=cipher+matrix[(x1+1)%3][y1]
				cipher=cipher+matrix[(x2+1)%3][y1]
				
			else:
				cipher=cipher+matrix[x1][y2]
				cipher=cipher+matrix[x2][y1]
		i+=2
	count+=1
for  m,Mat in enumerate(matrix):
				for n,var in enumerate(Mat):
					key=key+matrix[m][n]
print(key)
