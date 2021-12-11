import re
def parse_cdp_neighbors(command_output = "0"):
	with open("hello.txt", "r") as command_output:
		str1 = command_output.read()
		
		dict1 = {}

		R = [m.start() for m in re.finditer("R", str1)]
		Fa = [m.start() for m in re.finditer("Fa", str1)]
		
		r4_1 = str1[R[0]] + str(int(str1[R[0]+1]) - 1) 
		r4_2 = r4_1
		r5 = str1[R[0]] + str((str1[R[0]+1]))
		r6 = str1[R[0]] + str(int(str1[R[0]+1]) + 1)
		
		Fa_1 = str(str1[Fa[0]]) + str(str1[Fa[0]+1] + str1[Fa[0]+3] + str1[Fa[0]+4] + str1[Fa[0]+5])
		Fa_2 = str(str1[Fa[0]]) + str(str1[Fa[1]+1] + str1[Fa[1]+3] + str1[Fa[1]+4] + str1[Fa[1]+5])
		Fa_3 = str(str1[Fa[0]]) + str(str1[Fa[2]+1] + str1[Fa[2]+3] + str1[Fa[2]+4] + str1[Fa[2]+5])
		Fa_4 = str(str1[Fa[0]]) + str(str1[Fa[3]+1] + str1[Fa[3]+3] + str1[Fa[3]+4] + str1[Fa[3]+5])
		
		dict1[r4_1] = Fa_1
		dict1[r4_2] = Fa_2
		dict1[r5] = Fa_3
		dict1[r6] = Fa_4
		print(dict1)
parse_cdp_neighbors()