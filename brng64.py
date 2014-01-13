def rand64(seed):
	seed *=0x5D588B656C078965
	seed +=0x0000000000269EC3
	seed &=0xFFFFFFFFFFFFFFFF
	return seed

# Start with Input Seed:
seedlist,u32val,mul16,mul100,pc,res=[],[],[],[],[],[]
seedlist.append(int(raw_input("Input Current BRNG Seed: 0x"),16))

# Populate Next Seeds and RNG Results:
for i in range(0,31):
	seedlist.append(rand64(seedlist[i]))		# [n+1]
	u32val.append(seedlist[i] >> 32)			# >>32
	mul16.append((u32val[i]*16)>>32)			# *16
	mul100.append((u32val[i]*100)>>32)			# *100
	pc.append((mul100[i]-(mul100[i]%10))/10)	# Get Top Digit
	
	# Build Result Indicator for Frame:
	if mul16[i] == 0: 		# Critical / Max
		res.append("*")
	elif mul16[i] == 15:	# Super Bad / Min
		res.append("-")
	else:	# Just print First Digit of *100
		res.append("%d" % pc[i])

# Print Header
print "Frame | Seed             | 16 | 100 |    1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |" 
print "------|------------------|----|-----|   ---|---|---|---|---|---|---|---|"

# Populate Results:
for i in range(1,21):

	# Build Result String to Print
	string = ""
	string += "%5d | " 		% i					# Frame
	string += "%016X | "	% seedlist[i]		# 64Seed
	string += "%2d | " 		% mul16[i]
	string += "%3d |    " 		% mul100[i]
	
	# Tack on a list of predicted frame results:
	for j in range(0,8):
		string += "%s | " % res[i+j]
	
	# Spit Out List
	print string
		
	
raw_input("\nPress Enter to Exit.")