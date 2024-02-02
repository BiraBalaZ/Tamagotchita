from datetime import datetime

class Pochita:
    '''Docstring'''

    # Defining Pochita's inital states
    state = '[UNDEFINED]'

    birthyear = 2024
    birthmonth = 1
    birthday = 24

    actualYear = datetime.now().year
    actualMonth = datetime.now().month
    actualDay = datetime.now().day

    age = actualYear-birthyear
    lifeMonths = actualMonth-birthmonth
    lifeDays = actualDay-birthday

    # Basic metrics
    hungry = 0
    thirst = 0
    energy = 100
    happiness = 100

    # Limits
    minLimit = 0
    maxLimit = 100

    # List of variables to be adjusted
    variables = [hungry, energy, thirst, happiness]

    # Function to limit variables within the specified range
    def limit_within_range(value):
        return max(min(value, maxLimit), minLimit)

    # Applying the function to all variables
    variables = [limit_within_range(var) for var in variables]

    # Updating the variables
    hungry, energy, thirst, happiness = variables

