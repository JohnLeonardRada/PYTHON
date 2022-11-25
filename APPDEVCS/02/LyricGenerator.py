import random

class MarkovChain:
    def __init__(self):
        self.textData = []
        self.markov = []

    def parseWords(self, words):
        self.textData = words

    def parseTextFile(self, textFilePath):
        with open(textFilePath) as file:
            self.textData = file.read()
      
    def generate(self):
        self.textData = [i.lower() for i in self.textData.split(" ") if i.isalpha()]
        self.markov = {i:[] for i in self.textData}
        for before, after in zip(self.textData, self.textData[1:]):
            self.markov[before].append(after)
        new = list(self.markov.keys())
        seed = random.randrange(len(new))
        currentWord = random.choice(new)
        sentence = [currentWord]
        for i in range(0, random.randrange(1, 200)):
            check = self.markov[currentWord]
            if (len(check) > 0):
                nextWord = random.choice(check)
                sentence.append(nextWord)
                currentWord = nextWord
            else:
                currentWord = random.choice(new)
        return " ".join(sentence)  

def main():
    m = MarkovChain()
    def getCommand():
        action = False
        actionInput = input("Enter Command: ")

        if actionInput.lower() == "generate":
            getGenerate()
        elif actionInput.lower() == "add":
            getFileName()
        elif actionInput.lower() == "exit":
            quit()
            return False
        else:
            print("Invalid Input!")
            getCommand()

    def getGenerate():
        with open("song.txt") as f:
            openFile = m.parseTextFile("song.txt")
            print(m.generate(), "\n")
            getCommand()

    def getFileName():
      file_name = input("Enter Lyrics File: ")
      try:
          with open(file_name) as f:
              openFile = m.parseTextFile(file_name)
              print(f"Text File {file_name} loaded successfully.\n")
              getCommand()
              return openFile
      except IOError as ioe:
          print(f"Text File {file_name} loaded unsuccessfully.")
          getFileName()
      

    
    getFileName()
    getCommand()

    

if __name__ == "__main__":
    main()