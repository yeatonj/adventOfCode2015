# Program for reindeer games
# Written for Advent of Code 2015 (completed in 2023)
# Written by: Joshua Yeaton
# Written on: 1/22/2023

# Reindeer data is [name, speed, time at speed, rest time]
def total_dist(reindeer_data, time):
    interval_time = reindeer_data[2] + reindeer_data[3]
    full_intervals = time//interval_time
    rem_time = time % interval_time
    if (rem_time >= reindeer_data[2]):
        rem_time_at_speed = reindeer_data[2]
    else:
        rem_time_at_speed = rem_time
    total_dist = ((full_intervals * reindeer_data[2]) + rem_time_at_speed) * reindeer_data[1]
    return total_dist

filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day14/data.txt"
# filepath = "/Users/yeato/Documents/git_projects/adventOfCode2015/day14/data_test.txt"

data = open(filepath, 'r')

reindeers = []
for line in data:
    reindeer = []
    line_data = line.strip().split()
    reindeer.append(line_data[0])
    reindeer.append(int(line_data[3]))
    reindeer.append(int(line_data[6]))
    reindeer.append(int(line_data[13]))
    reindeers.append(reindeer)

max_dist = 0
time = 2503
rdeer_points = {}
for rdeer in reindeers:
    rdeer_points.update({rdeer[0]:0})
    temp = total_dist(rdeer, time)
    if (temp > max_dist):
        max_dist = temp

curr_max = 0
curr_lead_dist = 0
for i in range(1, time + 1):
    dists = []
    for rdeer in reindeers:
        temp = total_dist(rdeer, i)
        dists.append(temp)
        if temp > curr_max:
            curr_max = temp
    for i in range(len(dists)):
        if dists[i] == curr_max:
            rdeer_points.update({reindeers[i][0]:rdeer_points.get(reindeers[i][0]) + 1})

print(max(rdeer_points.values()))

