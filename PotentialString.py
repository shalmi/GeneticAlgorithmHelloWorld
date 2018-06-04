from random import choice, randint
from string import ascii_letters

class PotentialString:
    uuidCounter = 0
    def __init__(self, sourceString):
        self.myString = sourceString
        self.uuid = self.uuidCounter
        self.grade = 0
        PotentialString.uuidCounter += 1
    
    def __repr__(self,):
        return "< "+str(self.grade)+", '"+self.myString+"'>"

    # def __str__(self,):
    #     return "< "+str(self.grade)+", '"+self.myString+"'>"

    def randomLetter(self,):
        """returns a random letter"""
        return choice(ascii_letters+" .:,!") # make sure to add " " as an option

    def addLetter(self,):
        """adds a letter randomly into self.myString"""
        lengthOfString = len(self.myString)
        insertionPoint = randint(0,lengthOfString)
        self.myString = self.myString[:insertionPoint]+self.randomLetter()+self.myString[insertionPoint:]
    
    def subtractLetter(self,):
        """removes a letter randomly from self.myString. Ignores Empty Strings"""
        lengthOfString = len(self.myString)
        if lengthOfString == 0:
            return
        removalPoint = randint(0,lengthOfString-1)
        self.myString = self.myString[:removalPoint]+self.myString[(removalPoint+1):]
    
    def changeLetter(self,):
        """Changes a Letter in self.myString. Ignores Empty Strings"""
        lengthOfString = len(self.myString)
        if lengthOfString == 0:
            return
        changePoint = randint(0,lengthOfString-1)
        self.myString = self.myString[:changePoint]+self.randomLetter()+self.myString[(changePoint+1):]

    # List of Functions to Potentially Call During Mutations
    mutationFuncs = [addLetter, subtractLetter,changeLetter]

    def mutate(self,):
        """Randomly Runs Functions to Mutate self.myString"""
        for funcs in self.mutationFuncs:
            if randint(0,1): #flip a coin
                funcs(self) #run each mutation if true
        #change a random letter

    def gradeString(self,desiredString):
        """Grades the String by length, and chars.\n
        Returns the grade (higher = better)"""
        self.grade = 0
        desiredLength = len(desiredString)
        currentLength = len(self.myString)
        # Grade based on Length first
        offset = abs(desiredLength-currentLength)
        gradeForLength = desiredLength - offset
        self.grade += gradeForLength
        # grade based on chars next
        lesserLength = min(desiredLength,currentLength)
        lowerSelf = self.myString.lower()
        lowerDesired = desiredString.lower()
        # for each letter
        for x in range(lesserLength):
            # check if letters match when both lowered
            if lowerSelf[x] == lowerDesired[x]: 
                self.grade += 1
                # then check if they match while case sensitive
                if self.myString[x] == desiredString[x]:
                    self.grade += 1
        # add that score to grade
        return self.grade