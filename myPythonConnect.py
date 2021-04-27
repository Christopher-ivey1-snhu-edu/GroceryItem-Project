import re
import string


listfile = open("CS210_Project_Three_Input_File.txt","r") #file object for the given text file
itemList = listfile.read().splitlines() #list of all items in the file
uniqueItems = list(set(itemList)) #list of unique items from the above list

#Write Python code to return the frequency of a specific word.
def ItemCount(item):
    return itemList.count(item)

#Write Python code to calculate the frequency of every word that appears from the input file. 
def CountAllItems():
    for item in uniqueItems:
        print(item, ItemCount(item))

#Write a Python function that reads an input file and then creates a file, which contains the words and their frequencies. The file that you create should be named frequency.dat
def CreateItemsFile():
    countFile = open("frequency.dat","w")
    for item in uniqueItems:
        itemCount = item + " " + str(ItemCount(item)) + "\n"
        countFile.write(itemCount)