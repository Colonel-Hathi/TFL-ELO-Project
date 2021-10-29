# Imports
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime

import random

from elo import *

s = System()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# SET VARIABLES FROM HERE
# Add players
playercount = 30
# size of item pool
itemcount = 4500
# nr of items each player is given = nr of matches
itemnr = 3000
# scenario -1 = random, 0 = perfect, 1 = range
r = -1

earlystop = False

# Add Classes
s.addClass("a", 1000)

# Data for output
dataRand = []
dataPerf = []
dataRang = []

# Add players for each class
for p in range(playercount):
    s.addPlayer(str(p), "a", s.getClass("a").startrating)

# Generate question list (mean, std dev, amount)
itemdist = np.random.normal(1000, 300, itemcount)
for i in range(itemcount):
    s.addItem(str(i), rating=itemdist[i])


# Simulation method (adaptability range (-1 all random, 0 all adaptive))
def simulate(r):
    # Clear output
    dataRand = []
    dataPerf = []
    dataRang = []
    print("scenario: " + str(r))
    print("playercount: " + str(playercount))
    print("itempool: " + str(itemcount))
    print("#items: " + str(itemnr))
    for p in range(playercount):
        print("Still going! At:", p * 3.333, "%", datetime.datetime.now())
        for i in range(itemnr):
            if r == -1:
                no_adaptivity(p, i)
            elif r == 0:
                perfect_adaptivity(p, i)
                if earlystop:
                    break
            else:
                range_adaptivity(p, i)
                if earlystop:
                    break
    print("Done!", datetime.datetime.now())


def no_adaptivity(p, q):
    item = s.getItem(str(np.random.randint(0, itemcount)))
    player = s.getPlayer(str(p))
    s.game(player.name, item.name)
    dataRand.append([player.name, s.getPlayerRating(str(p)), q])
    # earlystop = False


def perfect_adaptivity(p, q):
    player = s.getPlayer(str(p))
    earlystop = True
    for i in range(itemcount):
        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), s.getItem(str(i))), 1)
        if chance == 0.5:
            itemmatch = s.getItem(str(i))
            s.game(player.name, itemmatch.name)
            dataPerf.append([player.name, s.getPlayerRating(str(p)), q])
            earlystop = False
            break


def range_adaptivity(p, q):
    player = s.getPlayer(str(p))
    earlystop = True
    for i in range(itemcount):
        item = s.getItem(str(i))
        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), item), 2)
        if chance > 0.15 and chance < 0.85:
            s.game(player.name, item.name)
            dataRang.append([player.name, s.getPlayerRating(str(p)), q])
            earlystop = False
            break

# Run simulation for all methods, create dataframes and write them to csv

#simulate(-1)
#dfRand = pd.DataFrame(dataRand, columns = ['Player', 'Elo', '#Questions'])
#dfRand.to_csv('outrand-3000-4500')

#simulate(0)
#dfPerf = pd.DataFrame(dataPerf, columns = ['Player', 'Elo', '#Questions'])
#dfPerf.to_csv('outperf-3000-4500')

simulate(300) #213 min
dfRang = pd.DataFrame(dataRang, columns = ['Player', 'Elo', '#Questions'])
dfRang.to_csv('outrang-3000-4500')