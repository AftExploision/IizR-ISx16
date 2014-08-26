import sys
from ASM import InvalidSyntax, InvalidNumber, FewArgs, LargeNumber, ASM

if len(sys.argv) < 3:
	inf = input('Path to input file. ')
	outf = input('Path to output file. ')
	exit()
else:
	inf = sys.argv[1]
	outf = sys.argv[2]

file = open(inf, 'r')
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

out = out.rstrip('\n')
file = open(outf, 'w')
file.write(out)
file.close()
