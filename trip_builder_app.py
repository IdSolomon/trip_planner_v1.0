# BEHOLD!
# The SevenStars_TripPlannerv1.0 application!

def sevenStars_tripWelcome(passenger):
    print("Welcome to The Seven Stars, " + passenger + "!")

sevenStars_tripWelcome("Benoit Blanc")

# OUTPUT: Welcome to The Seven Stars, Benoit Blanc!

def estimatedTime_rounded(estimatedTime):
    roundedTime = round(estimatedTime)
    return roundedTime

estimate = estimatedTime_rounded(5.76)

def sevenStars_destination(origin, destination, estimatedTime, modeOfTransport = "Kyushu Seven Stars"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + modeOfTransport)
    print("It will take approximately " + str(estimatedTime) + " hours")

sevenStars_destination("Hakata", "Nagasaki", estimate)

# OUTPUT: Your trip starts off in Hakata
# OUTPUT: And you are traveling to Nagasaki
# OUTPUT: You will be traveling by Kyushu Seven Stars
# OUTPUT: It will take approximately 6 hours