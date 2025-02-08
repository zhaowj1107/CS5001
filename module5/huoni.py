def tower_of_hanoi(num_disks, from_rod, to_rod):
    move_stack(num_disks, from_rod, to_rod)

def move_stack(num_disks, from_rod, to_rod):
    if num_disks == 1:
        move_one_disk(1, from_rod, to_rod)
    else:
        spare_rod = find_spare_rod(from_rod, to_rod)
        move_stack(num_disks - 1, from_rod, spare_rod)
        move_one_disk(num_disks, from_rod, to_rod)
        move_stack(num_disks - 1, spare_rod, from_rod)


def move_one_disk(disk, from_rod, to_rod):
    print("Moving disk#", disk, "from rod", from_rod, "to rod", to_rod)

def find_spare_rod(from_rod, to_rod):
    return 6 - (from_rod + to_rod)
