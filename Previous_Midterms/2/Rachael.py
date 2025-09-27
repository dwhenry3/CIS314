import os
import shutil
import re
import random

def organizeRecipeFiles(path):

    # create the desired name for the new paths
    cakePath = path+"\\Cake"
    cookiesPath = path+"\\Cookies"
    breadPath = path+"\\Bread"
    browniePath = path+"\\Brownie"
    otherPath = path+"\\Other"

    #create the new directories
    os.makedirs(cakePath, exist_ok=True)
    os.makedirs(cookiesPath, exist_ok=True)
    os.makedirs(breadPath, exist_ok=True)
    os.makedirs(browniePath, exist_ok=True)
    os.makedirs(otherPath, exist_ok=True)

    #Get a list of contents in the desired folder/directory
    contents = os.listdir(path)

    #create a regular expression to find any file type
    fileType = r"\.[a-zA-Z]{2,4}$"
    re.compile(fileType)

    #create empty list to put files into
    recipes = []

    #fill the recipes list with only files and no folders
    for content in contents:
        selectedContent = re.search(fileType, content) #this gives more varity without listing out all file types
        if(selectedContent != None):
            recipes.append(content)

    #put the files into the sub-folders/sub-directories
    try:
        i = 0
        while i < len(recipes):
            if recipes[i].find("cake") > 0 or recipes[i].find("Cake") > 0:
                shutil.move(path+"\\"+recipes[i], cakePath)
            
            elif recipes[i].find("cookie") > 0 or recipes[i].find("Cookie") > 0:
                shutil.move(path+"\\"+recipes[i], cookiesPath)

            elif recipes[i].find("bread") > 0 or recipes[i].find("Bread") > 0:
                shutil.move(path+"\\"+recipes[i], breadPath)

            elif recipes[i].find("brownie") > 0 or recipes[i].find("Brownie") > 0:
                shutil.move(path+"\\"+recipes[i], browniePath)
                
            else:
                shutil.move(path+"\\"+recipes[i], otherPath)

            i+=1
    except:
        pass

def chooseRandomRecipe(path):
    #to hold recipes
    randomRecipeList = []

    #fill a list for all the files in the selected directory including sub-directory
    for (root,dirs,files) in os.walk(path,topdown=True):
        randomRecipeList.extend(files)

    #get random number from the range of 0 to len(randomRecipeList) - 1
    randomNum = random.randrange(len(randomRecipeList))

    #print the random recipe
    print("Random recipe to cook: ", randomRecipeList[randomNum])