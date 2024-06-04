class Soldier:
	def __init__(self, vel: int, pos: int, army: int):
		self.vel = vel
		self.pos = pos
		self.army = army

	def __int__(self):
		return self.vel
	def __str__(self):
		return str(self.vel)
	def __repr__(self):
		return str(self.vel)


def armies_creation(armies):
	new_armies = []
	for army_index, army in enumerate(armies):
		new_armies.append([])
		for pos, vel in enumerate(army):
			new_armies[army_index].append(Soldier(vel, pos, army_index))
	
	return new_armies


def queue_battle(dist,*armies):
	armies = armies_creation(armies)
	
	while len(armies) > 1:
		for army_index, army in enumerate(armies):
			if len(army) == 0:
	
	
    

print(queue_battle(400, (186,78,56,67,78,127,78,192), (78,67,208,45,134,212,82,99), (327,160,49,246,109,98,44,57)))
# (2,(0,2,5))

#a = [1,2,3]
#a.append(a.pop(0))
#print(a)