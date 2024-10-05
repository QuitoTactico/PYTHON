def solution(args: list):
    sol = []
    rng = [args[0]]
    for index, i in enumerate(args[1:]):
        if i - rng[-1] > 1:  # if the distance is >1
            if len(rng) < 3:
                sol += list(map(str, rng))
            else:
                sol.append(f"{rng[0]}-{rng[-1]}")
            rng = [i]
        else:  # keep walking
            rng.append(i)

    if len(rng) < 3:
        sol += list(map(str, rng))
    else:
        sol.append(f"{rng[0]}-{i}")

    return ",".join(sol)


print(
    solution(
        [
            -10,
            -9,
            -8,
            -6,
            -3,
            -2,
            -1,
            0,
            1,
            3,
            4,
            5,
            7,
            8,
            9,
            10,
            11,
            14,
            15,
            16,
            17,
            18,
            20,
        ]
    )
)
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
