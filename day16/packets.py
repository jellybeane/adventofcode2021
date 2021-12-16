import math


#example = 'D2FE28' # literal
#example = '38006F45291200'
#example = 'EE00D40C823060' # operator
#example = '8A004A801A8002F478'
#example = '620080001611562C8802118E34'
#example = 'C0015000016115A2E0802F182340'
example = 'A0016C880162017C3686B18A3D4780'
intval = int(example, 16)
bstr = format(intval, '0>'+str(4*len(example))+'b')

# puzzinput = open("input.txt")
# puzzstr = puzzinput.readline().strip()
# intval = int(puzzstr, 16)
# bstr = format(intval, '0>'+str(4*len(puzzstr))+'b')

class Literal:
	def __init__(self, version,num):
		self.version = version
		self.num = num

	def versionsum(self):
		return self.version

class Operator:
	def __init__(self, version, typeid, packets):
		self.version = version
		self.typeid = typeid
		self.packets = packets

	def versionsum(self):
		vsum = self.version
		for packet in self.packets:
			vsum += packet.versionsum()
		return vsum

# Part 1: add up all the version numbers
def processpacket(bstr):
	print('processpacket', bstr)

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
	version = int(bstr[:3], 2)
	typeid = int(bstr[3:6], 2)
	print("version", version)
	print("typeid", typeid)

	# Type IDs
	# 4: literal
	# Other: operator

	if (typeid == 4):
		literalstr = ''
		keepreading = True
		groupstart = 6
		while keepreading:
			## last group, end of packet
			if int(bstr[groupstart]) == 0:
				keepreading = False
			literalstr += bstr[groupstart+1:groupstart+5]
			groupstart = groupstart+5
		literal = int(literalstr, 2)
		print("literalstr", literalstr)
		print("literal", literal)

		# print("packetend", packetend)
		thispacket = Literal(version,literal)
		return((thispacket, groupstart))

	else:
		lengthtype = int(bstr[6])
		# If the length type ID is 0, then the next 15 bits
		# are a number that represents the total length in bits of the sub-packets contained by this packet.
		if lengthtype == 0:
			# print("lengthtype 0")
			subpackets = []
			length = 15
			totalsubpacketlen = int(bstr[7:22],2)
			print("subpacket len str", bstr[7:22])
			print("totalsubpacketlen+22", totalsubpacketlen+22)
			# print("totalsubpacketlen", totalsubpacketlen)
			packetstart = 22

			while packetstart < totalsubpacketlen:
				print("packetstart before", packetstart)
				print("len(bstr)", len(bstr))
				subpacket, packetlen = processpacket(bstr[packetstart:])
				print("packetstart after", packetstart)
				packetstart += packetlen
				subpackets.append(subpacket)
			# print("version", version)
			thispacket= Operator(version,typeid,subpackets)
			return ((thispacket, packetstart))
				
		# If the length type ID is 1, then the next 11 bits
		# are a number that represents the number of sub-packets immediately contained by this packet.
		else:
			# print("lengthtype 1")
			subpackets = []
			length = 11
			numpackets = int(bstr[7:18],2)
			print("numpacket str", bstr[7:18])
			print("numpackets", numpackets)
			# print("numpackets", numpackets)
			packetstart = 18
			for i in range(0, numpackets):
				print("packetstart before", packetstart)
				subpacket, packetlen = processpacket(bstr[packetstart:])
				print("packetstart after", packetstart)
				packetstart += packetlen
				subpackets.append(subpacket)
			# print("version", version)
			thispacket= Operator(version,typeid,subpackets)
			return ((thispacket, packetstart))

packet, finalpacketlen = processpacket(bstr)

print("versionsum", packet.versionsum())