import math
import matplotlib.pyplot as plt

#targetstr = 'target area: x=20..30, y=-10..-5'
targetstr = open("input.txt").readline().strip()

_, _, targetx, targety = targetstr.split(' ')
targetx = tuple(map(int, targetx[2:].strip(',').split('..')))
targety = tuple(map(int, targety[2:].split('..')))

print('targetx',targetx)
print('targety',targety)

class ProbeState():
	def __init__(self, x, y, vx, vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy

	def update(self):
		self.x += self.vx
		self.y += self.vy
		if self.vx > 0:
			self.vx -= 1
		elif self.vx < 0:
			self.vx += 1
		self.vy -= 1

# a helper for generating the images like on the problem page
def display_trajectory(startpos, positions, targetx, targety):
	# figure out how big the grid needs to be
	maxx, maxy = map(max, zip(*positions))
	maxx = max(startpos[0], max(maxx, targetx[1]))
	maxy = max(startpos[1], max(maxy, targety[1]))
	# x will only be positive, but y may be negative
	_, miny = map(min, zip(*positions))
	miny = min(startpos[1], min(miny, targety[0]))

	for row in range(maxy,miny-1,-1):
		s = ''
		for col in range(0,maxx+1):
			pos = (col,row)
			if pos == startpos:
				s+=('S')
			elif pos in positions:
				s+=('#')
			elif col >= targetx[0] and col <= targetx[1] and row >= targety[0] and row <= targety[1]:
				s+=('T')
			else:
				s+=('.')
		print(s)

def hit_target(probe, targetx, targety, maxsteps):
	positions = []
	for step in range(0, maxsteps):
		if probe.x >= targetx[0] and probe.x <= targetx[1] and probe.y >= targety[0] and probe.y <= targety[1]:
			print("Hit the target")
			return (True, positions)
		if probe.x > targetx[1] or probe.y < targety[0]:
			print("Missed the target")
			return (False, positions)
		probe.update()
		positions.append((probe.x, probe.y))

	print("Ran out of steps")
	return (False, positions)


startpos = (0,0)

#startvel = (7,2)
#startvel = (6,3)
#startvel = (9,0)
#startvel = (17,-4)
#startvel = (6,9)

## Part 1: Assuming the target is below the starting position,
## vy will be negative initial-vy when it hits the starting y again
# we want the next step's y-index to be the minimum target y
# so the initial vy must be -1 - mintargy
# startvel = (int(targetx[0]/5), -1 - targety[0])
# probe = ProbeState(startpos[0],startpos[1],startvel[0],startvel[1])

# numsteps = 13
# hit, positions = hit_target(probe, targetx, targety, numsteps)
# display_trajectory(startpos,positions,targetx,targety)
# maxx, maxy = map(max, zip(*positions))
# print('Highest y position:',maxy)

## Part 2: how many starting velocities end in the target?
# vx upper bound: overshoots the first step
vxupper = targetx[1]+1
# vx lower bound: goes to 0 before reaching the target
# triangle numbers: if x=(k(k+1))/2, then k=sqrt(2x+1/4)-1/2
vxlower = int(math.floor(math.sqrt((2*targetx[0] + 0.25)-0.5)))
# vy upper bound: one more than part 1's
vyupper = -targety[0]
# vy lower bound: overshoots the first step
vylower = targety[0]

print("vx bounds", (vxlower,vxupper))
print("vy bounds", (vylower,vyupper))
# try all the velocities and see if they work
numgood = 0
goodvx = []
goodvy = []
stepsneeded = []
for vx in range(vxlower, vxupper+1):
	for vy in range(vylower,vyupper+1):
		probe = ProbeState(startpos[0],startpos[1],vx,vy)
		for step in range(0, 1000):
			if probe.x >= targetx[0] and probe.x <= targetx[1] and probe.y >= targety[0] and probe.y <= targety[1]:
				#print("Hit the target")
				numgood+=1
				goodvx.append(vx)
				goodvy.append(vy)
				stepsneeded.append(step)
				break
			if probe.x > targetx[1] or probe.y < targety[0]:
				#print("Missed the target")
				break
			probe.update()
		else:
			print("Ran out of steps", (vx,vy,maxsteps))
			assert False
print("numgood", numgood)

plt.scatter(goodvx, goodvy, c=stepsneeded, cmap=plt.get_cmap('gist_rainbow'))
plt.xlabel("vx")
plt.ylabel("vy")
plt.title("Velocities that hit the target")
cbar = plt.colorbar()
cbar.set_label("# steps")
plt.show()