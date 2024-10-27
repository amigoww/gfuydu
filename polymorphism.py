class School:
    def __init__(self):
        pass


    def wear_uniform(self):
        return f'В школе все должны носить форму'


class University:
    def __init__(self):
        pass


    def wear_uniform(self):
        return f'Можно носить любую одежду, если ты студент'


school = School()
university = University()

print(school.wear_uniform())
print(university.wear_uniform())





