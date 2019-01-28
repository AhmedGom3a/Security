inp = raw_input()
inp= inp.split(" ")
mod=int(inp[0])
BigN=int(inp[1])

flag=True
A=[1,0,mod]
B=[0,1,BigN]
oldA=A[:]
result="IMPOSSIBLE"


if(B[2]==0):
	flag=False
	print(result)

Tom=0
#print(" X A1 A2 A3 B1 B2 B3")
#print("   %i %i %i %i %i %i "%(A[0],A[1],A[2],B[0],B[1],B[2]))
while flag:
	Tom=int(A[2]/B[2])
	i=0
	while i<3:
		A[i]=B[i]
		B[i]=oldA[i]-(Tom*A[i])
		oldA[i]=A[i]
		i+=1
	#print(" %i %i %i %i %i %i %i "%(Tom,A[0],A[1],A[2],B[0],B[1],B[2]))
	if(B[2]==0):
		flag=False
		print(result)
	elif(B[2]==1):
		flag=False
		result=B[1]%mod
		print("{x} {y}".format(x=(mod-BigN)%mod,y=result))

	

