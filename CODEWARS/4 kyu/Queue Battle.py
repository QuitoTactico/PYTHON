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
	
class Bullet:
	def __init__(self, vel: int, dist: int, target: int):
		self.vel = vel
		self.dist = dist
		self.target = target

def armies_creation(armies) -> list[list[Soldier]]:
	new_armies = []
	for army_index, army in enumerate(armies):
		new_armies.append([])
		for pos, vel in enumerate(army):
			new_armies[army_index].append(Soldier(vel, pos, army_index))
	
	return new_armies

# ------------------------------------------------------------------------

def queue_battle(dist:int,*armies):
	armies = armies_creation(armies)
	bullets:list[Bullet] = []


	while len(armies) > 1:
		# the bullets hit while the soldiers prepare
		army_died = False
		dead_heads = []
		if len(bullets) != 0:
			for bullet_index, bullet in enumerate(bullets):
				bullet.dist -= bullet.vel 					# flying bullet

				if bullet.dist <= 0:							# the bullet hits
					target_index = bullet.target
					bullets.pop(bullet_index)
					dead_heads.append(target_index)
					armies[target_index].pop(0)

					if len(armies[target_index]) == 0:		# if the army is eliminated
						armies.pop(target_index)
						bullets = []
						army_died = True

		if army_died:
			army_died = False
			continue

		# the soldiers shot
		for army_index, army in enumerate(armies):
			if army_index not in dead_heads:			# if the soldier isn´t dead
				target_index = army_index+1 if army_index+1 < len(armies) else 0
				bullets.append(Bullet(army[0].vel, dist, target_index)) 	# shot
				armies[army_index].append(armies[army_index].pop(0))		# go last on the queue
	
	if len(armies) == 1:
		army_index = armies[0][0].army
		winners = tuple([soldier.pos for soldier in armies[0]])
		return army_index, winners

	else:	# no armies left
		return -1, ()



			
	
	
    

print(queue_battle(400, (186,78,56,67,78,127,78,192), (78,67,208,45,134,212,82,99), (327,160,49,246,109,98,44,57)))
# (2,(0,2,5))

#a = [1,2,3]
#a.append(a.pop(0))
#print(a)