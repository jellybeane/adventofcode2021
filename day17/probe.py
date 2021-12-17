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
startvel = (int(targetx[0]/5), -1 - targety[0])

probe = ProbeState(startpos[0],startpos[1],startvel[0],startvel[1])

numsteps = 1000
hit, positions = hit_target(probe, targetx, targety, numsteps)
#display_trajectory(startpos,positions,targetx,targety)
maxx, maxy = map(max, zip(*positions))
print('Highest y position:',maxy)


