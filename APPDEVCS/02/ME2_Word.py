# Major Exam 2
# Programmed by John Leonard Rada
# SEG31

#Function to get the file name that will be used
def getFileName():
    file_name = input("Specify Word List File: ")
    
    try:
        with open(file_name) as f:
            openFile = open(file_name)
            print(f"Text File {file_name} loaded successfully.\n")
            return openFile
    except IOError as ioe:
        print(f"Text File {file_name} loaded unsuccessfully.")
        getFileName()

#Function to prompt the user to input a word
def inputSearch():
    search_string = input("Search Word: ")
    return search_string
    
#Function to search for possible words that starts with the search_string variable
def searchString(file_name, search_string):

    lineRead = file_name.readlines()
    equal_words = [equal for equal in lineRead if equal.startswith(search_string.lower())]
    print(f"Words Starting With ({search_string})")
    for item in equal_words:
        print(item.strip())

def getAction():
    action = False 
    actionInput = input("Search Again? [Y/N]")
    if(actionInput.upper() == "Y"):
        return True
    elif (actionInput.upper() == "N"):
        return False
    else:
        print("Invalid Input!")
        getAction()
            

def main():
    print("\nWELCOME TO WORD SEARCH PROGRAM!")
    file = getFileName()
    file_holder = file
    search = inputSearch()
    word_search = searchString(file, search)

    while(getAction()):
        searchString(getFileName(), inputSearch())
   

if __name__ == '__main__':
    main()