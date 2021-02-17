#! /usr/bin/env Python3.6
# tablePrinter.py - displays lists of lists as justified table

def printTable(data):
    colWidths = [0] * len(data) #find max length of word to determine column width
    for line in range(len(data)):
        for word in range(len(data[line])):
            if colWidths[line] <= len(data[line][word]):
                colWidths[line] = len(data[line][word])

    for li in range(len(data[0])): #print data in justified table format
        for i in range(len(data)):
            print(data[i][li].rjust(colWidths[i]), end =" ")
        print()




tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
