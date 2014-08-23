class InvalidSyntax(Exception):
	pass

class InvalidNumber(Exception):
	pass

class LargeNumber(Exception):
	pass

class FewArgs(Exception):
	pass

class ASM:
	def __init__(self, code):
		self.data = code

	def toBinary(self):
		cmds = self.data.split('\n')
		cmds = cmds.rstrip()
		cmds = cmds.lstrip()

		out = ''
	
		try:
			for word in cmds:
				if word.startswith('NoOp '):
					out += ('0 0000 000 000 00000')
				elif word.startswith('Load '):
					out += ('0 0001 000 000 00000\n%s' % decToBin(word.split()[0], 131071))
				elif word.startswith('Store '):
					out += ('0 0010 000 000 00000' % decToBin(word.split()[0], 131071))
				elif word.startswith('CopyReg '):
					out += ('0 0011 %s %s 00000' % (decToBin(word.split()[0], 7), \
                                                                           decToBin(word.split()[1], 7)))
				elif word.startswith('Interrupt '):
					out += ('0 0100 %s 000 00000' % decToBin(word.split()[0], 7))
				elif word.startswith('Pointer '):
					out += ('0 0101 %s %s %s0000' % (decToBin(word.split()[0], 7), \
                                                    decToBin(word.split()[1], 7), decToBin(word.split()[2], 1)))
				elif word.startswith('StoreImm '):
					out += ('0 0110 %s 000 00000\n%s' % (decToBin(word.split()[0], 7), \
                                                                                decToBin(word.split()[1], 131071)))
				elif word.startswith('StackC '):
					out += ('0 0111 %s %s %s' % (decToBin(word.split()[0], 7), \
                                                                        decToBin(word.split()[1], 7), \
                                                                        decToBin(word.split()[2], 31)))
				elif word.startswith('PC '):
					out += ('0 1000 %s %s %s' % (decToBin(word.split()[0], 7), \
                                                                        decToBin(word.split()[1], 7), \
                                                                        decToBin(word.split()[2], 31)))
				elif word.startswith('ScratchPad '):
					out += ('0 1001 %s %s %s' % (decToBin(word.split()[0], 7), \
                                                                        decToBin(word.split()[1], 7), \
                                                                        decToBin(word.split()[2], 31))
				elif word.startswith('Branch '):
					out += ('0 1111 %s %s %s' % (decToBin(word.split()[0], 7), \
                                                                        decToBin(word.split()[1], 7), \
                                                                        decToBin(word.split()[2], 31)))
		except IndexError, E:
			raise FewArgs()

	def decToBin(self, dec, max):
		if int(dec) > max:
			raise LargeNumber()

		val = int(dec)
		out = '{%s:b}'
		out = out.format(10)
		
		while (2**(len(out)))-1 < max:
			out = ('0') + out

		return out
