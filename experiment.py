from elo import *
import numpy as np
import csv

s = System()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#SET VARIABLES FROM HERE
# Add players
playercount = 50
#size of item pool
itemcount = 7500
#nr of items each player is given = nr of matches
itemnr = 5
#scenario -1 = random, 0 = perfect, 1 = range
r = -1

# Add Classes
s.addClass("a", 1000)
s.addClass("b", 1000)

# Add players for each class
for p in range(playercount):
    if p < playercount / 2:
        s.addPlayer(str(p), "a", s.getClass("a").startrating)
    else:
        s.addPlayer(str(p), "b", s.getClass("b").startrating)

# Generate question list (mean, std dev, amount)
itemdist = np.random.normal(1000, 300, itemcount)
for i in range(itemcount):
    s.addItem(str(i), rating=itemdist[i])

# Simulation method (adaptability range (-1 all random, 0 all adaptive))
def simulate(r):
    print("scenario: " + str(r))
    print("playercount: " + str(playercount))
    print("itemcount: " + str(itemcount))
    for p in range(playercount):
        print(str(p))
        for i in range(itemnr):
            if r == -1:
                no_adaptivity(p)
            elif r == 0:
                perfect_adaptivity(p)
            else:
                range_adaptivity(p)
    print("Done!jupyter ")

def no_adaptivity(p):
    item = s.getItem(str(np.random.randint(0, itemcount)))
    player = s.getPlayer(str(p))
    s.game(player.name, item.name)

def perfect_adaptivity(p):
    player = s.getPlayer(str(p))
    for i in range(itemcount):
        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), s.getItem(str(i))), 1)
        if chance == 0.5:
            itemmatch = s.getItem(str(i))
            s.game(player.name, itemmatch.name)
            break

def range_adaptivity(p):
    player = s.getPlayer(str(p))
    for i in range(itemcount):
        item = s.getItem(str(i))
        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), item), 2)
        if chance > 0.15 and chance < 0.85:
            s.game(player.name, item.name)
            break


#run simulation
simulate(r)

#write ratings to csv file
ratings = []
ratinglist = s.getRatingList()

itemratings = []
itemslist = s.getItemList()

for i in range(len(ratinglist)):
    ratings.append(ratinglist[i][2])

for j in range (len(itemslist)):
    itemratings.append(itemslist[j][1])

with open("PLAYER_RATINGS"+str(r)+str(playercount)+str(itemcount)+str(itemnr)+".txt", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    wr.writerow(ratings)

with open("ITEM_RATINGS"+str(r)+str(playercount)+str(itemcount)+str(itemnr)+".txt", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    wr.writerow(itemratings)