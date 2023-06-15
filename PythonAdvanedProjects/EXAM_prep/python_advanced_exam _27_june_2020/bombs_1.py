# 100

from collections import deque

bombs_effect = deque(int(x) for x in input().split(", "))
bombs_casings = deque(int(x) for x in input().split(", "))

bombs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}
counter_bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0,'Smoke Decoy Bombs':0}
pouch = False
while True:
    bomb_eff = bombs_effect.popleft()
    bomb_cas = bombs_casings.pop()
    bomb = bomb_eff + bomb_cas
    if bombs.get(bomb):
        bmb = bombs[bomb]
        counter_bombs[bmb] += 1
    else:
        bombs_effect.appendleft(bomb_eff)
        bombs_casings.append(bomb_cas - 5)

    if counter_bombs["Datura Bombs"] >= 3 and \
            counter_bombs["Cherry Bombs"] >= 3 and counter_bombs["Smoke Decoy Bombs"] >= 3:
        pouch = True
        break
    if len(bombs_effect) == 0 or len(bombs_casings) == 0:
        break

if pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")


if bombs_effect:
    print(f"Bomb Effects: {', '.join([str(bomb) for bomb in bombs_effect])}")
else:
    print("Bomb Effects: empty")


if bombs_casings:
    print(f"Bomb Casings: {', '.join([str(bomb) for bomb in bombs_casings])}")
else:
    print("Bomb Casings: empty")

for key,value in sorted(counter_bombs.items()):
    print(f"{key}: {value}")