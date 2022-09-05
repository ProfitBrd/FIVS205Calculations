import numpy as np
print("///////////////////////////////////////////")
print("To use PMI dating and Colonization Calculations - ")
print("enter the temperature numeral, ADD A SPACE, and ")
print("then enter the degree type (C or F). For Example:\n\nEnter the Body Temperature: --> 23.93 c\nEnter the Ambient Temperature: --> 70 f\nOR\nEnter the average temperature --> 30 c\nEnter the Threshold --> 70 f")
print("///////////////////////////////////////////")
print("")
#TODO: Edit above

def convertToCelciusReturnStr(inputArray):
    if (inputArray[1] == "f"):
        inputArray[0] = str((float(inputArray[0]) - 32) * (5 / 9))
    else:
        inputArray[0] = str(inputArray[0])
    return inputArray[0]

def convertToCelciusReturnFloat(inputArray):
    if (inputArray[1] == "f"):
        inputArray[0] = (float(inputArray[0]) - 32) * (5 / 9)
    else:
        inputArray[0] = float(inputArray[0])
    return inputArray[0]


while(True):
    print("")
    answer = input("Eye Potassium --- Type \"k\"\nPMI (Liver, Rectal, etc.) --- Type \"p\"\nTime of Colonization --- Type \"c\"\nEstimated Height --- Type \"h\"\nExit --- Type \"0\"\n--> ")
    answer = answer.lower()

    if answer == "0":
        break;

    elif answer == "p":
        try:
            bodyTempList = list(map(str, input("Enter the Body Temperature: --> ").split()))
            ambientTempList = list(map(str, input("Enter the Ambient Temperature: --> ").split()))

            #if bodylist[1] is not a string than throw error?
            bodyTempList[1] = bodyTempList[1].lower()
            ambientTempList[1] = ambientTempList[1].lower()

            #converting both from f to c if neccassary for both temps
            if (bodyTempList[1] == "f"):
                bodyTempInC = (float(bodyTempList[0]) - 32) * (5/9)
            else:
                bodyTempInC = float(bodyTempList[0])

            if (ambientTempList[1] == "f"):
                ambientTempInC = (float(ambientTempList[0]) - 32) * (5 / 9)
            else:
                ambientTempInC = float(ambientTempList[0])

            print("")
            #if body still hotter than surroundings
            if (bodyTempInC > ambientTempInC):
                print("Body Heat Equation: (37.2 - " + str(bodyTempInC) + ")/0.6")
                #print("Check if answer is greater than room temperature")
                print("Answer: " + str(round((37.2 - bodyTempInC) / 0.6, 2)) )
            else:
                print("Answer: Cannot be determined")

        except (IndexError, ValueError):
            print("---Input Formatted Incorrectly---")



    elif (answer == "k"):
        potassiumConcentration = input("What is the potassium concentration? --> ")
        print("Potassium Concentration Equation: (5.26 * " + str(potassiumConcentration) + ") - 30.9")
        print( "ANSWER: " + str(round(5.26 * float(potassiumConcentration) - 30.9, 2)) )


    elif (answer == "h"):
        try:
            lengthOfBone = input("Length of Bone (no units) --> ")
            femurOrHumerus = input("Femur(f) or Humerus(h) --> ").lower()
            descent = input("European(e), African(af), or Asian(as) --> ").lower()
            maleOrFemale = input("Male(m) or Female?(f) --> ").lower()
            dictKey = femurOrHumerus + descent + maleOrFemale
            #[Femur/Humerus(f/m)][Decent(e/af/as)][Gender(m/f)]
            proofDict = {
                "fem": "(2.32 * " + lengthOfBone + ") + 65.53",
                "fafm": "(2.1 * " + lengthOfBone + ") + 72.22",
                "fasm": "(2.15 * " + lengthOfBone + ") + 72.57",
                "fef": "(2.47 * " + lengthOfBone + ") + 54.1",
                "faff": "(2.28 * " + lengthOfBone + ") + 59.76",
                "hem": "(2.89 * " + lengthOfBone + ") + 78.1",
                "hafm": "(2.88 * " + lengthOfBone + ") + 75.48",
                "hasm": "(2.68 * " + lengthOfBone + ") + 83.19",
                "hef": "(3.36 * " + lengthOfBone + ") + 57.97",
                "haff": "(3.08 * " + lengthOfBone + ") + 64.67"
            }
            lengthOfBone = float(lengthOfBone)
            answerDict = {
                "fem" : (2.32*lengthOfBone) + 65.53,
                "fafm" : (2.1*lengthOfBone) + 72.22,
                "fasm" : (2.15*lengthOfBone) + 72.57,
                "fef" : (2.47*lengthOfBone) + 54.1,
                "faff" : (2.28*lengthOfBone) + 59.76,
                "fasf" : "Unknown",
                "hem" : (2.89*lengthOfBone) + 78.1,
                "hafm" : (2.88*lengthOfBone) + 75.48,
                "hasm" : (2.68*lengthOfBone) + 83.19,
                "hef" : (3.36*lengthOfBone) + 57.97,
                "haff" : (3.08*lengthOfBone) + 64.67,
                "hasf" : "Unknown"
            }
            try:
                if (answerDict[dictKey] == "Unknown"):
                    print("ANSWER: Unknown")
                else:
                    print("PROOF: " + proofDict[dictKey])
                    print("ANSWER: " + str(round(answerDict[dictKey],2)))
            except (KeyError):
                print("---Inputs Are Not Valid Choices---")


        except (ValueError):
            print("---Input Formatted Incorrectly---")


    elif (answer == "c"):
        typeOfQuestion = input("Degree Time from a Table(t) or Average Temperature(a) --> ").lower()
        try:
            if typeOfQuestion == "a":
                avgTempsList = []
                numOfTemps = int(input("How many average temperatures do you have to enter --> "))
                for i in range (numOfTemps):
                    avgTempsList.append( convertToCelciusReturnFloat( list(map(str, input("Enter the average temperature (with degree type) --> ").split()))))

                avgTempsTotal = sum(avgTempsList)

                degreeThreshold = convertToCelciusReturnFloat( list(map(str, input("Enter the Threshold (with degree type) --> ").split())))

                print("")
                answerProofString = ""
                for i in range(numOfTemps - 1):
                    answerProofString += str(round(avgTempsList[i],2)) + "-" + str(degreeThreshold) + "+"
                answerProofString += str(round(avgTempsList[numOfTemps-1],2)) + "-" + str(degreeThreshold) + "="

                print(answerProofString)
                DD = round(avgTempsTotal-(numOfTemps*degreeThreshold),2)
                DH = round(DD*24,2)
                print("Degree DAYS: " + str(DD))
                print("Degree HOURS: " + str(DH))

            elif typeOfQuestion == "t":

                averageTemp = convertToCelciusReturnFloat( list(map(str, input("Average Temperature --> ").split())) )
                thresholdTemp = convertToCelciusReturnFloat( list(map(str, input("Threshold Temperature --> ").split())) )
                #TODO: add error checking for putting a string into the array below
                phaseTimes = list(map(float, input("List relevant stages separated by a space (in hours) --> ").split())) #TODO: state in try-catch block that if they enter a string (XX) that they should reread the instructions
                #TODO: Add proof
                print("Degree DAYS: " + str( round((averageTemp-thresholdTemp)*(sum(phaseTimes)/24),2) )   )
                print("Degree HOURS: " + str( round((averageTemp-thresholdTemp)*(sum(phaseTimes)),  2) )   )

            else:
                print("---Input Is Not A Valid Choice---")

        except (ValueError):
            print("---Inputs Are Not Valid Choices---")
        except (IndexError):
            print("---Missing A Part Of The Input (For Example: Missing Unit of Temperature)---")


    elif (answer == "b"):
        try:
            width = input("Width --> ")
            length = input("Length --> ")
            print("arcsin(" + width + "/" + length + ")")
            print("Angle Of Impact: "  )





        except (ValueError):
            print("---Inputs Are Not Valid Choices---")






