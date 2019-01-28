inp = raw_input()
inp= inp.split(" ")
base=int(inp[0])
power=int(inp[1])
mod=int(inp[2])


ans=pow(int(base),int(power),int(mod))

print(int(ans))


