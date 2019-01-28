inp = raw_input()
inp= inp.split(" ")
num2=inp[0]
num1=inp[1]
num1=bin(int(num1,16))[2:].zfill(8)
num2=bin(int(num2,16))[2:].zfill(8)
addition =hex((int(num1,2))^(int(num2,2)))[2:].zfill(2)
mod='00011011'

orlist=[num2]
i=1
temp=num2


while i<8:
	if(temp[0]=="1"):
		
		temp=temp[1:]+"0"
		temp=bin((int(temp,2))^(int(mod,2)))[2:].zfill(8)
	else:
		temp=temp[1:]+"0"
	orlist=orlist+[temp]
	
	i+=1



temp='00000000'
for j,Char in enumerate(num1):
	if(Char=="1"):
		
		temp=bin((int(temp,2))^(int(orlist[7-j],2)))[2:].zfill(8)



multiplication=hex(int(temp,2))[2:].zfill(2)

print("{x} {y}".format(x=addition.upper(),y=multiplication.upper()))

