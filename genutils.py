import math, time, random, numpy, os

import pygame
from pygame.locals import *



#names taken from the top 25 most popular baby names of 2018 and the NATO phonetic alphabet
samplePlaceholder = ["Alfa","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whisky","Xray","Yankee","Zulu"]
sampleMaleNames = ["Liam","Noah","William","James","Oliver","Benjamin","Elijah","Lucas","Mason","Logan","Alexander","Ethan","Jacob","Michael","Daniel","Henry","Jackson","Sebastian","Aiden","Matthew","Samuel","David","Joseph","Carter","Owen"]
sampleFemaleNames = ["Emma","Olivia", "Ava", "Isabella","Sophia","Charlotte","Mia","Amelia","Harper","Evelyn","Abigail","Emily","Elizabeth","Mila","Ella","Avery","Sofia","Camila","Aria","Scarlett","Victoria","Madison","Luna","Grace","Chloe"]




class Scoreboard:
    def __init__(self, amount, scorerange):

        self.top = amount
        self.scorepath = "./highscores.txt" #Where the scores file is located.
        self.low, self.high = scorerange

        try:
            f = open(scorepath,"r")
            f.close()
        except:
            self.createNew()

        #autopopulate if no scores found
        with open(scorepath) as f:
            first = f.read(1)
            if not first:
                self.genScores(self.top)

    def createNew(self):
        f = open(scorepath,"a")
        self.genScores(self, self.top)
        self.orderScores()
        f.close()

    def addEntry(self,name,score):
        f=open(scorepath,"a")
        f.write("{}/{}/\n".format(name, score))

    def getTop(self,number):
        names = []
        scores = []

        f=open(scorepath,"r")
        lines = f.readlines()
        read = lines[0:number]

        for x in read:
            name = x.split("/")[0]
            score = x.split("/")[1]
            names.append(name)
            scores.append(score)

        return names,scores

    def getEntry(self, number):
        f=open(scorepath,"r")

        lines = f.readlines()
        read = lines[number-1]

        name = read.split("/")[0]
        score = read.split("/")[1]

        return name,score

    def deleteEntry(self, number):
        with open(scorepath,"r") as f:
            lines = f.readlines()

        lines.pop(number-1)

        with open(scorepath, "w") as f:
            for line in lines:
                f.write(line)

    def genScores(self):
        random.seed()
        for x in range(0,self.top):
            value = random.randint(0,1)
            if value == 0:
                name = random.choice(sampleMaleNames) + random.choice(samplePlaceholder)
            if value == 1:
                name = random.choice(sampleFemaleNames) + random.choice(samplePlaceholder)
            score = random.randint(self.low, self.high)
            self.addEntry(name,score)

    def orderScores(self):
        scores = []
        with open(scorepath,"r") as f:
            lines = f.readlines()

        for x in lines:
            name = x.split("/")[0]
            score = x.split("/")[1]
            scores.append([name,int(float(score))])

        sort = sorted(scores, key=lambda x: x[1])

        parsed = []
        for arr in sort:
            par = "/".join([arr[0],str(arr[1]),"\n"])
            parsed.append(par)

        with open(scorepath, "w") as f:
            index = 0
            for line in lines:
                f.write(parsed[index])
                index+=1

    def checkScores(self,score):
        check = False
        self.orderScores()
        name,scoir = self.getEntry(self.top)
        if score < int(scoir): #less score is better
            check = True

        if check == True:
            name = input("INPUT NAME: ")
            self.addEntry(name, score)
            self.orderScores()
        else:
            pass

    def getTotal(self):
        total = 0
        with open(scorepath,"r") as f:
            lines = f.readlines()
        for item in lines:
            total += 1
        return total

    def getRanking(self, score):
        scores = []
        self.orderScores()

        rank = 1

        with open(scorepath,"r") as f:
            lines = f.readlines()

        for x in lines:
            scoir = int(x.split("/")[1])
            if scoir < score:
                rank += 1
            else:
                break
        return rank

class timeparser:
    def __init__(self):
        pass

    def secToDisp(self, secs): #convert raw seconds into minutes:seconds. Try to keep it below one hour.
        mins = 0
        sec = secs
        while sec >= 60:
            mins += 1
            sec -= 60
        return "{}:{:02d}".format(mins,sec)

class Stopwatch:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.startTime = 0

    def startTimer(self):
        self.startTime = time.time()

    def updateTimer(self):
        seconds = time.time()-self.startTime
        minutes = 0
        while seconds >=60:
            minutes += 1
            seconds -= 60
            seconds += 1

        return (minutes, seconds)


    def stopTimer(self):
        print("Time Elasped: %d seconds" %(time.time()-self.startTime))
        return time.time()-self.startTime
