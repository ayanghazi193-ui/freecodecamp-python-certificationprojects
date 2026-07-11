def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    record()

    def move(disks, source, auxiliary, target):
        if disks == 1:
            disk = rods[source].pop()
            rods[target].append(disk)
            record()
        else:
            move(disks - 1, source, target, auxiliary)

            disk = rods[source].pop()
            rods[target].append(disk)
            record()

            move(disks - 1, auxiliary, source, target)

    if n > 0:
        move(n, 0, 1, 2)

    return "\n".join(moves)
