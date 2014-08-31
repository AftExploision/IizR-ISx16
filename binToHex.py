import sys

if len(sys.argv) < 3:
	inf = input('Input input file path. ')
	outf = input('Enter output file path. ')
else:
	inf = sys.argv[1]
	outf = sys.argv[2]

binToHex = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7', \
            '1000':'8', '1001':'9', '1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E', '1111':'F'}

file = open(inf, 'r')
bin = file.read()
file.close()

bin = bin.replace(' ', '')
bin = bin.rstrip('\n')
bins = bin.split('\n')
out = ''

for f in bins:
	out += '%s%s%s%s\n' % (binToHex[f[:4]], binToHex[f[4:8]], binToHex[f[8:12]], binToHex[f[12:]])

out = out.rstrip('\n')

file = open(outf, 'w')
file.write(out)
file.close()
