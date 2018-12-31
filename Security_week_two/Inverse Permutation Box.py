n=input('')
temp=raw_input('')
per=temp.split(" ")
output=""
x=0
inv=False
while x<n:
	inv=False
	for i,num in enumerate(per):
		if x+1 == int(num):
			if(x<15):
				output=output+str(i+1)+" "
				inv=True
			else:
				output=output+str(i+1)
				inv=True
	x+=1
if(inv):
	print(output)
else:
	print("IMPOSSIBLE")