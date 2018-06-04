from PotentialString import PotentialString
import operator
# desiredString = "Hello World" # This was too easy for the computer :P
desiredString = "This is my desired string. It is my way of saying HELLO WORLD! Hopefully my program can handle it without too much issue... cuz lets be honest, just saying hello world is too easy!"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main Func~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bestGradedString = PotentialString("")
for generation in range(10000):
    Strings = []
    for x in range(0,750): 
        tempString = PotentialString(bestGradedString.myString)
        Strings.append(tempString)
    GradedStrings = {}
    for eachString in Strings:
        eachString.mutate()
        GradedStrings[eachString.gradeString(desiredString)] = eachString

    # This calculates the top score from GradedStrings
    # change itemgetter(0) to 1 to order by value instead
    topScore = max(GradedStrings.items(), key=operator.itemgetter(0))[0]
    # then Save that Winner for the next round
    bestGradedString = GradedStrings[topScore]
    if bestGradedString.myString == desiredString:
        print("Winner after "+ str(generation)+ " generations.: ", bestGradedString.myString)
        break
    print(generation, bestGradedString)


# print(GradedStrings)
# print(bestGradedString)

