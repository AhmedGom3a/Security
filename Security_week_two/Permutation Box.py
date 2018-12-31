n=input('')
temp=raw_input('')
per=temp.split(" ")
m=input('')
temp=raw_input('')
plain=list(temp)
bina=""
for hexa in plain:
	bina=bina+bin(int(hexa, 16))[2:].zfill(4)


bintext=list(bina)
op=""
x=0
while x<n :
	op=op+bintext[int(per[x])-1]
	x+=1

op=[op[i:i+4] for i in range(0, len(op), 4)]
output=""	
for binn in op:
	temp=hex(int(binn,2))[2:].zfill(1)
	output=output+temp.upper()

print(output)