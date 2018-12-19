Alpha=[]
Alpha2=[]
matrix=[[],[],[],[],[]]
key=raw_input()
plain=raw_input() # L A J R 
cipher=""
vernam=[]
key2=key
x=0
pad=""
while x<26 :
		Alpha=Alpha+[chr(65+x)]
		x+=1

y=0
if len(plain)!=len(key):
	while y<(len(plain)-len(key)):
		key2=key2+key[(y)%len(key)]
		y+=1
	pad="NO"	
else:
	pad="YES"


A1=0
B1=0
M1=0
M2=0
x=0
while x<len(plain):
	for i,Let in enumerate(Alpha):
		if plain[x]==Let:
			#print("A+{x}".format(x=x))
			A1=i
		if key2[x]==Let:
			#print("B+{x}".format(x=x))
			B1=i
	cipher=cipher+Alpha[(A1+B1)%26]
	M1=ord(Alpha[A1])
	M2=ord(Alpha[B1])
	vernam=vernam+[hex(M1 ^ M2)[2:]]
	x=x+1

print("Vigenere: {x}".format(x=cipher))
vernam2=""
for i,L in enumerate(vernam):
	if len(vernam[i])>1:
		vernam2=vernam2+vernam[i]
	else:
		vernam2=vernam2+"0"+vernam[i]

vernam2=vernam2.upper()
print("Vernam: {x}".format(x=vernam2))
print("One-Time Pad: {x}".format(x=pad))
