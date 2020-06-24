# Author: Marcelo Salas
# Date: 06/23/2020
# Description: First project using statistics import to find mean median and mode
import statistics
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        '''Returns the age of a person so that it can be used outside of the private class'''
        return self._age

def basic_stats(person_list):
    '''creates a truple and fills it with the ages then preforms the desired math'''
    age = []
    for x in person_list:
        '''loop to add the age of each person to the age = []'''
        age.append(x.get_age())
    age_mean = statistics.mean(age)
    age_median = statistics.median(age)
    age_mode = statistics.mode(age)
    return age_mean, age_median, age_mode

p1 = Person("Kyoungmin", 73)
p2 = Person("Mercedes", 24)
p3 = Person("Avanika", 48)
p4 = Person("Marta", 24)
person_list = [p1, p2, p3, p4]
print(basic_stats(person_list))


