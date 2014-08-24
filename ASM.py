class InvalidSyntax(Exception):
	pass

class InvalidNumber(Exception):
	pass

class LargeNumber(Exception):
	pass

class FewArgs(Exception):
	pass

import traceback

class ASM:
	def __init__(self, code):
		self.data = code

	def decToBin(self, dec, max):
		if int(dec) > max:
			raise LargeNumber()

		val = int(dec)
		out = bin(int(dec))
		out = out.lstrip('0')
		out = out.replace('b', '')

		while (2**(len(out)))-1 < max:
			out = ('0') + out

		return out

	def toBinary(self):
		cmds = self.data
		cmds = cmds.rstrip()
		cmds = cmds.lstrip()
		cmds = cmds.split('\n')

		out = ''

		decToBin = self.decToBin

		try:	
			for word in cmds:
				if word.startswith('NoOp '):
					out += ('0 0000 000 000 00000')
				elif word.startswith('Load '):
					out += ('0 0001 %s 000 00000\n%s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 65535)))
				elif word.startswith('Store '):
					out += ('0 0010 %s 000 00000\n%s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 65535)))
				elif word.startswith('CopyReg '):
					out += ('0 0011 %s %s 00000' % (decToBin(word.split()[1], 7), \
                       	                         decToBin(word.split()[2], 7)))
				elif word.startswith('Interrupt '):
					out += ('0 0100 %s 000 00000' % (decToBin(word.split()[1], 7)))
				elif word.startswith('Pointer '):
					out += ('0 0101 %s %s 0000%s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 1)))
				elif word.startswith('StoreImm '):
					out += ('0 0110 %s 000 00000\n%s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 65535)))
				elif word.startswith('StackC '):
					out += ('0 0111 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('PC '):
					out += ('0 1000 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('ScratchPad '):
					out += ('0 1001 %s %s %s' % (decToBin(word.split()[0], 7), \
                                                 decToBin(word.split()[1], 7), decToBin(word.split()[2], 31)))
				elif word.startswith('Branch '):
					out += ('0 1111 %s %s %s\n%s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31), \
                                                 decToBin(word.split()[4], 65535)))
				
				elif word.startswith('Add '):
					out += ('1 0000 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('AddC '):
					out += ('1 0001 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('AddShift '):
					out += ('1 0010 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('Sub '):
					out += ('1 0011 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('SubShift '):
					out += ('1 0100 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('OR '):
					out += ('1 0101 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('XOR '):
					out += ('1 0110 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('AND '):
					out += ('1 0111 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 31)))
				elif word.startswith('ShiftDown '):
					out += ('1 1000 %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 127)))
				elif word.startswith('Bshift '):
					out += ('1 1001 %s %s %s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 15), decToBin(word.split()[3], 15)))
				elif word.startswith('Compare '):
					out += ('1 1010 %s %s 00%s' % (decToBin(word.split()[1], 7), \
                                                 decToBin(word.split()[2], 7), decToBin(word.split()[3], 7)))
				elif word.startswith('VOID '):
					out += ('1 1110 000 000 00000')
				elif word.startswith('SysHault '):
					out += ('1 1111 000 000 00000')

				out += '\n'
		except IOError:
			raise FewArgs()
		return out
