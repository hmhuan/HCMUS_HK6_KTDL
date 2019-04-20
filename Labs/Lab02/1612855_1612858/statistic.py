import statistics

state_count = {}

fIn = open("plants.csv", "r")
state = fIn.readline().split(",")
state[len(state) - 1] = state[len(state) - 1][:-1]
for i in range(1, len(state)):
    state_count[state[i]] = 0
for line in fIn:
    infor = line.strip().split(",")
    for s in range(1, len(infor)):
        if infor[s] == "y":
            state_count[state[s]] += 1

for state, count in state_count.items():
    print(state, ": ", count)

print

state_min = min(state_count, key=state_count.get)
count_min = state_count[state_min]
print(state_min, "\t", count_min, "\t", str(round(count_min/34781*100, 2))+"%")
state_max = max(state_count, key=state_count.get)
count_max = state_count[state_max]
print(state_max, "\t", count_max, "\t", str(round(count_max/34781*100, 2))+"%")
print("avg-species", round(statistics.mean(state_count.values()), 2))
