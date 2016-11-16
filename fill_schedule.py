# -*- coding: cp1250 -*-
import person3


crew = [
    'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O',
]

# 'D' - dyżur dzienny
# 'N' - dyżur nocny
# 'U' - urlop
# '.' - dzień wolny

schedules = [
    'D.........UUUUUU..............N',
    '.D...........................N.',
    '..D.........................N..',
    '...D.................UUUUUUN...',
    '....D.....................N....',
    '.....D...................N.....',
    '......D.................N......',
    '.......D...............N.......',
    '........D.............N........',
    'UUU...UUUUUUU........N.........',
    '..........D.........N..........',
    '...........D..UUUUUUUU.........',
    '............D.....N............',
    '.............D...N.............',
    '..............D.N..............',
]

person_per_day = 3           # liczba osób na dyżurze dziennym
person_per_night = 2         # liczba osób na dyżurze nocnym
number_of_working_days = 10  # liczba dyżurów w ciągu miesiąca


def fill_team_schedules(crew, schedules, number_of_working_days, person_per_day, person_per_night):
    """Funkcja służąca do automatycznego wypełniania grafuku pracy.

    Funkcja wypełnia automatycznie grafiki pracy (schedule) dla poszczególnych osób z załogi (crew)
    Wszystkie osoby (w postaci instancji Person) należy zebrać w listę (team).
    Wypełnianie grafiku pracy odbywa się na podstawie ustawionych parametrów.

    :param crew: załoga
    :param schedules: lista grafików pracy dla poszczególnych osób z crew

    :param number_of_working_days: maksymalna liczba dni pracujących w miesiącu dla jednej osoby
    :param person_per_day: - liczba osób pracujących w dzień
    :param person_per_night: - liczba osób pracujących w nocy
    """

    # tworzenie drużyny złożonej z instancji Person
    team = [person3.Person(name, schedule) for name, schedule in zip(crew, schedules)]
    
    # TODO poniżej Twoje rozwiązanie

    day_workers=[0]*31
    night_workers=[0]*31

    for employee in schedules:
        for day_number, status in enumerate(employee):
            if status=='D':
                day_workers[day_number]+=1
            elif status=='N':
                night_workers[day_number]+=1
    
    for index, day in enumerate(day_workers):
        if day<person_per_day:
            defficiency=person_per_day-day
            for member in team:
                if member.is_day_free(index)==True:
                    if member.month_is_full(number_of_working_days)==False and member.if_week_is_full(index)==False and member.if_double_work(index, 'D')==False:
                        member.take_one_day_work(index, 'D')
                        defficiency-=1
                        day_workers[index]+=1
                        if defficiency==0:
                            break
                            
    for index, day in enumerate(night_workers):
        if day<person_per_night:
            defficiency=person_per_night-day
            for member in team:
                if member.is_day_free(index)==True:
                    if member.month_is_full(number_of_working_days)==False and member.if_week_is_full(index)==False and member.if_double_work(index, 'N')==False:
                        member.take_one_day_work(index, 'N')
                        defficiency-=1
                        night_workers[index]+=1
                        if defficiency==0:
                            break
    
    for emp in team:
        print(emp.schedule)

    
        
    
#print(fill_team_schedules(crew, schedules, 15, 3,2))


if __name__ == "__main__":
    fill_team_schedules(crew, schedules, number_of_working_days, person_per_day, person_per_night)
