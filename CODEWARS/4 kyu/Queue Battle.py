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

    def __str__(self):
        return f"{self.dist}.{self.vel}|{self.target}"

    def __repr__(self):
        return f"{self.dist}.{self.vel}|{self.target}"


def armies_creation(armies) -> list[list[Soldier]]:
    new_armies = []
    for army_index, army in enumerate(armies):
        new_armies.append([])
        for pos, vel in enumerate(army):
            new_armies[army_index].append(Soldier(vel, pos, army_index))

    return new_armies


# ------------------------------------------------------------------------


def queue_battle(dist: int, *armies):
    armies = armies_creation(armies)
    bullets: list[Bullet] = []

    while len(armies) > 1:
        # print(armies)
        # print(bullets)
        # print()

        # the bullets hit while the soldiers prepare
        army_died = False
        dead_heads = []
        dead_armies = []
        new_bullets = []
        if len(bullets) != 0:
            for bullet_index, bullet in enumerate(bullets):
                bullet.dist -= bullet.vel  # flying bullet
                target_index = bullet.target

                if (
                    bullet.dist <= 0
                    and target_index not in dead_armies
                    and target_index not in dead_heads
                ):  # the bullet hits
                    # print(bullets, len(bullets))
                    # bullets.pop(bullet_index)
                    dead_heads.append(target_index)
                    armies[target_index].pop(0)

                    if len(armies[target_index]) == 0:  # if the army is eliminated
                        dead_armies.append(target_index)
                        # armies.pop(target_index)
                        # bullets = []
                        army_died = True
                        # break
                else:
                    if bullet.dist > 0 or target_index not in dead_heads:
                        new_bullets.append(bullet)

        bullets = new_bullets

        if army_died:
            new_armies = []
            for army_index, army in enumerate(armies):
                if army_index not in dead_armies:
                    if army_index not in dead_heads:
                        army.append(army.pop(0))
                    new_armies.append(army)
            armies = new_armies
            bullets = []
            army_died = False
            continue

        # the soldiers shot
        else:
            for army_index, army in enumerate(armies):
                if army_index not in dead_heads:  # if the soldier isn´t dead
                    target_index = army_index + 1 if army_index + 1 < len(armies) else 0
                    bullets.append(Bullet(army[0].vel, dist, target_index))  # shot
                    armies[army_index].append(
                        armies[army_index].pop(0)
                    )  # go last on the queue
                # else:
                # print(army_index)

    if len(armies) == 1 and len(armies[0]) != 0:
        army_index = armies[0][0].army
        winners = tuple([soldier.pos for soldier in armies[0]])
        return army_index, winners

    else:  # no armies left
        return -1, ()


print(queue_battle(100, (25, 38, 55, 46, 82), (64, 90, 37, 25, 58)))  # (1,(3,2))

print(
    queue_battle(
        200, (61, 83, 37, 55, 92, 35, 68, 72), (90, 81, 36, 114, 67, 25, 31, 84)
    )
)  # (0,(6,7))

print(
    queue_battle(
        300, (98, 112, 121, 95, 63), (120, 94, 90, 88, 30), (116, 144, 45, 200, 32)
    )
)  # (0,(2,))

print(
    queue_battle(
        400,
        (186, 78, 56, 67, 78, 127, 78, 192),
        (78, 67, 208, 45, 134, 212, 82, 99),
        (327, 160, 49, 246, 109, 98, 44, 57),
    )
)  # (2,(0,2,5))

print(
    queue_battle(
        500,
        (345, 168, 122, 269, 151),
        (56, 189, 404, 129, 101),
        (364, 129, 209, 163, 379),
        (520, 224, 154, 74, 420),
    )
)  # (-1,())

# a = [1,2,3]
# a.append(a.pop(0))
# print(a)
