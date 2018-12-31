PC1 =[ 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]

PC2 =[ 14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]

Rotations =[ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]
array=raw_input()
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
	key=""
	while x<len(PC2) :
		key=key+total[int(PC2[x])-1]
		x+=1

	output=""
	key=[key[i:i+4] for i in range(0, len(key), 4)]	
	for binn in key:
		temp1=hex(int(binn,2))[2:].zfill(1)
		output=output+temp1.upper()

	print(output)
	main+=1