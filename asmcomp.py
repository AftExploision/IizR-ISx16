import sys
from ASM import InvalidSyntax, InvalidNumber, FewArgs, LargeNumber, ASM

if len(sys.argv) < 3:
	print('Not enough arguements!')
	exit()

file = open(sys.argv[1], 'r')
code = file.read()
file.close()

compile = ASM(code)

out = ''
try:
	out = compile.toBinary()
except InvalidSyntax:
	print('Error! Invalid syntax!')
except InvalidNumber:
	print('Invalid number!')
except FewArgs:
	print('Too few args for operation!')
except LargeNumber:
	print('Number too large!')

file = open(sys.argv[2], 'w')
file.write(out)
file.close()
