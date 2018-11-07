#Read all the data into a dictionary
def read():
    file = open("names.txt", "r")
    dictionary=dict()
    for line in file:
        lsplit = line.split()
        tempName=lsplit.pop(0)
        dictionary.update({tempName:lsplit})

        
    file.close()
    return dictionary


def SearchName(dictionary):
    name=str(input("Enter a name: "))
    if(name in dictionary):
        mostpopular=-1
        tempmax=1001
        templist=(dictionary[name])
        for i in range(len(templist)):
            tempint=int(templist[i])
            if(tempint<tempmax):
                tempmax=tempint
                mostpopular=i
        print("The matches with thei highest ranking decade are:")
        print("19"+str(mostpopular)+"0")

    else:
        print(name+" does not appear in any decade.")


def NameHistory(dictionary):
    name=str(input("Enter a name: "))
    if (name in dictionary):
        templist=(dictionary[name])
        for i in range(len(templist)):
            print("19"+str(i)+"0 "+str(templist[i]))







def main():
    NameDict=read()
    option=int(input("Enter choice: "))
    if(option==1):
        SearchName(NameDict)
    if(option==2):
        NameHistory(NameDict)






main()