import math
import operator

#example = 'C200B40A82' # finds the sum of 1 and 2, resulting in the value 3.
#example = '04005AC33890' # finds the product of 6 and 9, resulting in the value 54.
#example = '880086C3E88112' # finds the minimum of 7, 8, and 9, resulting in the value 7.
#example = 'CE00C43D881120' # finds the maximum of 7, 8, and 9, resulting in the value 9.
#example = 'D8005AC2A8F0' # produces 1, because 5 is less than 15.
#example = 'F600BC2D8F' # produces 0, because 5 is not greater than 15.
#example = '9C005AC2F8F0' # produces 0, because 5 is not equal to 15.
# example = '9C0141080250320F1802104A08' # produces 1, because 1 + 3 = 2 * 2.

# intval = int(example, 16)
# bstr = format(intval, '0>'+str(4*len(example))+'b')

puzzinput = open("input.txt")
puzzstr = puzzinput.readline().strip()
intval = int(puzzstr, 16)
bstr = format(intval, '0>'+str(4*len(puzzstr))+'b')

def product(vals):
	p = 1
	for val in vals:
		p *= val
	return p

def greater(vals):
	return int(vals[0] > vals[1])

def lesser(vals):
	return int(vals[0] < vals[1])

def equal(vals):
	return int(vals[0] == vals[1])

operations = {
	0 : sum,
	1 : product, # python doesn't have builtin product
	2 : min,
	3 : max,
	5 : greater,
	6 : lesser,
	7 : equal
}

class Literal:
	def __init__(self, version,num):
		#print("Literal v%s : %s" % (version, num))
		self.version = version
		self.num = num

	def versionsum(self):
		return self.version

	def getval(self):
		return self.num

class Operator:
	def __init__(self, version, typeid, packets):
		#print("Operator v%s, type %s, packets %s" % (version, typeid, len(packets)))
		self.version = version
		self.typeid = typeid
		self.packets = packets

	def versionsum(self):
		vsum = self.version
		for packet in self.packets:
			vsum += packet.versionsum()
		return vsum

	def getval(self):
		op = operations[self.typeid]
		return op([packet.getval() for packet in self.packets])

def processpacket(bstr):
	#print('processpacket', bstr)

	# bstr may have trailing zeros, but there should be fewer than 11 of them
	if len(bstr) < 11:
		print("All zeros", bstr)
		# for debugging
		assert False

		assert '1' not in bstr
		return(0,len(bstr))

	# Every packet begins with a standard header: 
	# the first three bits encode the packet version,
	# and the next three bits encode the packet type ID.
	index = 3
	version = int(bstr[:index], 2)
	typeid = int(bstr[index:index+3], 2)
	index += 3
	#print("version", version)
	#print("typeid", typeid)

	# Type IDs
	# 4: literal
	# Other: operator
	if (typeid == 4):
		literalstr = ''
		keepreading = True
		while keepreading:
			## last group, end of packet
			if int(bstr[index]) == 0:
				keepreading = False
			literalstr += bstr[index+1:index+5]
			index += 5
		literal = int(literalstr, 2)

		thispacket = Literal(version,literal)
		return((thispacket, index))

	else:
		lengthtype = int(bstr[index])
		index += 1
		# If the length type ID is 0, then the next 15 bits
		# are a number that represents the total length in bits of the sub-packets contained by this packet.
		if lengthtype == 0:
			length = 15
			totalsubpacketlen = int(bstr[index:index+length],2)
			index += length

			subpackets = []
			while index < totalsubpacketlen+22:
				subpacket, packetlen = processpacket(bstr[index:])
				index += packetlen
				subpackets.append(subpacket)
			thispacket = Operator(version,typeid,subpackets)
			return ((thispacket, index))
				
		# If the length type ID is 1, then the next 11 bits
		# are a number that represents the number of sub-packets immediately contained by this packet.
		else:
			length = 11
			numpackets = int(bstr[index:index+length],2)
			index += length

			subpackets = []
			for i in range(0, numpackets):
				subpacket, packetlen = processpacket(bstr[index:])
				index += packetlen
				subpackets.append(subpacket)
			thispacket= Operator(version,typeid,subpackets)
			return ((thispacket, index))

finalpacket, finalpacketlen = processpacket(bstr)

# Part 1: add up all the version numbers
print("versionsum", finalpacket.versionsum())
# Part 2: evaluate the packet
print("packetval", finalpacket.getval())