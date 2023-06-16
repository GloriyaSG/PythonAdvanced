from collections import deque

jobs = [int(x) for x in input().split(", ")]
index = int(input())
total_cycles = 0
dict_of_jobs = {}

for indexing, job in enumerate(jobs):
    dict_of_jobs[indexing] = job

jobs_deck = deque(sorted(dict_of_jobs.items(), key=lambda x: x[1]))

while jobs_deck:
    idx = jobs_deck[0][0]
    cycle = jobs_deck[0][1]
    total_cycles += cycle
    jobs_deck.popleft()
    if idx == index:
        print(total_cycles)
        break



