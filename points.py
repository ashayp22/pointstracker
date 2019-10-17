from __future__ import print_function, unicode_literals
import regex

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
import xlwt
import xlrd
from xlutils.copy import copy


def getCurrentData():
    names = []
    points = []
    filepath = 'points.txt'
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            data = line
            names.append(data[0:data.find(",")])
            points.append(int(data[data.find(",")+1:]))
    return names, points

def displayPoints():
    names, points = getCurrentData()

    names = [x for _,x in sorted(zip(points,names))] #zips points and names then sort
    points = sorted(points)

    print("----------LEADERBOARD----------")

    for i in range(len(names)):
        print(str(i + 1) + ". " + names[len(names) - i - 1] + " - " + str(points[len(points) - 1 - i]))

def updatePoints(names, points):
    with open('points.txt', 'w') as f:
        for i in range(len(names)):
            f.write("%s\n" % (names[i] + "," + str(points[i])))


def getInput():
    print("")
    print("")
    text = input("what do you want me to do (type help for help)?")
    return text


def processText(text):

    names, points = getCurrentData()

    if text.find("show") != -1:
        displayPoints()
        processText(getInput())
    elif text == "clear all":
        for z in range(len(points)):
            points[z] = 0
        print("no one has points now")
        updatePoints(names, points)
        processText(getInput())
    elif text.find("help") != -1:
        print("type the persons name and whether to add or remove points...")
        print("...then type the number of points")
        print("type clear and person's name to clear points")
        print("type clear all to clear all points")
        processText(getInput())


    #get the person name
    name = ""
    i = -1

    for n in names:
        i += 1
        if text.find(n) != -1:
            name = n
            break

    if name == "":
        print("sorry, I didn't understand")
        processText(getInput())
        return

    if text.find("add") != -1 or text.find("give") != -1:

        num = input("how many points?")

        #adding points
        points[i] += int(num)
        print(name + " now has " + str(points[i]) + " points")
    elif (text.find("remove") != -1 or text.find("take away") != -1):

        num = input("how many points?")

        if points[i] - int(num) < 0:
            print("you can't take that many away")
        else:
            points[i] -= int(num)
            print(name + " now has " + str(points[i]) + " points")
    elif text.find("reset") != -1 or text.find("clear") != -1:
        points[i] = 0
        print(name + " now has " + str(points[i]) + " points")
    else:
        print("sorry, I didn't understand")

    updatePoints(names, points)
    processText(getInput())

processText(getInput())
