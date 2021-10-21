from elo import *
import numpy as np

s = System()

# TODO: Elo matches between questions?


# Add players
playercount = 100
# Add items
itemcount = 5500

# Add Classes
s.addClass("a", 1000)
s.addClass("b", 1000)

#print(s.getClass("b").startrating)

# Add players for each class
for p in range(playercount):
    if p < playercount / 2:
        s.addPlayer(str(p), "a", s.getClass("a").startrating)
        #s.addToClass("a", str(p))
    else:
        s.addPlayer(str(p), "b", s.getClass("b").startrating)
        #s.addToClass("b", str(p))

# Generate question list (mean, std dev, amount)
itemdist = np.random.normal(1000, 200, itemcount)
for i in range(itemcount):
    s.addItem(str(i), rating=itemdist[i])


# Simulation method (# of questions to answer per player, adaptability range (-1 all random, 0 all adaptive))
def simulate(n, r):
    for p in range(playercount):
        print("Still going! At:", p, "%")
        #notdone = True
        for i in range(n):
            if i % 50 == 0:
                print("Still asking! At:", (i / n) * 100, "%")
            # All random questions
            if r == -1:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                while item.name in player.getItemsDone():
                    item = s.getItem(str(np.random.randint(0, itemcount)))
                s.game(player.name, item.name)
                check = True
            # 'Perfect' adaptability, always choose best question
            elif r == 0:
                player = s.getPlayer(str(p))
                check = False
                for i in range(itemcount):
                    if s.getItem(str(i)).name in player.getItemsDone():
                        continue
                    else:
                        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), s.getItem(str(i))), 1)
                        if chance == 0.5:
                        #if np.absolute(player.rating - s.getItem(str(i)).rating) < np.absolute(player.rating - itemmatch.rating):
                            itemmatch = s.getItem(str(i))
                            s.game(player.name, itemmatch.name)
                            check = True
                            break
                        else:
                            continue
                if not check:
                    break
            # r as acceptable elo range for questions
            else:
                player = s.getPlayer(str(p))
                for i in range(itemcount):
                    item = s.getItem(str(i))
                    if item.name in player.getItemsDone():
                        continue
                    else:
                        if np.absolute(player.rating - item.rating) <= r:
                            s.game(player.name, item.name)
                            break
                        else:
                            continue


print(s.getRatingList())
simulate(5000, 0)
print(s.getRatingList())