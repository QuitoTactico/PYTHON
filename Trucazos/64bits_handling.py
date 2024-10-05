import array

filters = array.array(
    "L",
    [
        0x5555555555555555,
        0x3333333333333333,
        0x0F0F0F0F0F0F0F0F,
        0x00FF00FF00FF00FF,
        0x0000FFFF0000FFFF,
        0x00000000FFFFFFFF,
    ],
)


def countBits(n):
    count = 0
    while True:
        n, n64 = n >> 64, n & 0xFFFFFFFFFFFFFFFF
        for ii, f in enumerate(filters):
            a, b = f & n64, ~f & n64
            n64 = a + (b >> (1 << ii))
        count += n64
        if not n:
            return count
