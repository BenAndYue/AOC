# read file in

# split "direction" from x (value)

# if [0] == forward: add to forward
# if down == -depth else ++ to depth
# conclusion = horizontel * depth (down-up)

def part1(filename):
    commands_cum_sum = {"forward":0, "down":0, "up":0} 
    with open(filename) as f:
        for line in f:
            c, value = tuple(line.split())
            commands_cum_sum[c] += int(value)
    
    return commands_cum_sum["forward"] *(commands_cum_sum["down"] - commands_cum_sum["up"])

def part2(filename):
    aim = 0
    horizontal_position = 0
    depth = 0

    with open(filename) as f:
        for line in f:
            c, value = tuple(line.split())
            if c == "down":
                aim += int(value)
            elif c == "up":
                aim -= int(value)
            else:
                horizontal_position += int(value)
                depth += aim  * int(value)

    return horizontal_position * depth

filename = "input1.txt"
part1(filename)
part2(filename)