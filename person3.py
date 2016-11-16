# -*- coding: cp1250 -*-


class Person:
    """Klasa Person.
    Klasa służy do tworzenia instancji Person.
    Zawiera metody potrzebne do automatycznego wypełniania grafiku pracy (schedule).
    """

    def __init__(self, name, schedule):
        """Konstruktor klasy Person.

        :param name: nazwisko
        :param schedule: grafik pracy
        """
        self.name = name
        self.schedule = schedule

    def __str__(self):
        return 'Person {}'.format(self.name)

    def is_day_free(self, day_number):
        """Metoda zwraca True jeśli osoba w dniu day_number ma dzień wolny i może wziąć dyżur,
        False jeśli nie może przyjąć dyżuru.

        :param day_number: numer dnia w miesiącu
        :returns: True lub False
        """
        if self.schedule[day_number]=='.':
            return True
        else:
            return False

    def take_one_day_work(self, day_number, work):
        """Metoda wprowadza zmiany w grafiku (schedule) dla danego dnia i rodzaju dyżuru.

        :param day_number: numer dnia w miesiącu
        :param work: rodzaj dyżuru, dyżur dzienny - "D", dyżur nocnny - "N"
        """
        temp=list(self.schedule)
        temp[day_number]=work
        self.schedule=''.join(temp)
        return(self.schedule)

    def get_number_of_working_days(self):
        """Metoda zwraca sumę dyżurów dziennych i nocnych w ciągu miesiąca.

        :returns: return_type - liczba naturalna
        """
        count=0
        for day in self.schedule:
            if day=='N' or day=='D':
                count+=1
        return count
    def month_is_full(self, number_of_working_days):
        """Metoda zwraca True jeśli liczba dyżurów w miesiącu jest równa lub większa niż liczba number_of_working_days,
        inaczej zwraca False.

        :param number_of_working_days: maksymalna liczba dyżurów przypadająca na jedną osobę w miesiącu.
        :returns: True lub False
        """
        if self.get_number_of_working_days()>=number_of_working_days:
            return True
        else:
            return False

    ####################
    # Zadania dodatkowe:
    ####################

    def if_double_work(self, day_number, work):
        """Metoda zwraca True jeśli dodanie dyżuru dziennego "D" lub nocnego "N"
        spowoduje powstanie dyżuru 24h "ND", inaczej False.

        :param day_number: numer dnia w miesiącu
        :param work: rodzaj dyżuru, dyżur dzienny - "D", dyżur nocnny - "N"
        :returns: True lub False
        """
        if work=='N':
            if day_number==30:
                    return False
            else:
                if self.schedule[day_number+1]=='D':
                    return True
                else:
                    return False
        elif work=='D':
            if day_number==0:
                    return False
            else:
                if self.schedule[day_number-1]=='N':
                    return True
                else:
                    return False
                    
    def if_week_is_full(self, day_number, no_of_working_days_in_week=4):
        """Metoda zwraca True jeśli po wstawieniu dyżuru w dzień day_number liczba dyżurów
        w ciągu 7 dni po rząd będzie większa niż no_of_working_days_in_week,
        inaczej zwraca False.

        :param day_number: numer dnia w miesiącu
        :param no_of_working_days_in_week: maksymalna liczba dyżurów w ciągu 7 dni pod rząd
        :returns: True lub False
        """
        count=0
        temp=list(self.schedule)
        temp[day_number]='D'
        beg=max(day_number-6, 0)
        end=min(day_number+7, 30)
        check=temp[beg:end]
        for day_number, status in enumerate(check):
            end=min(day_number+6, len(check)-1) #7 powinno byc ale nie zadje testu?
            test=check[day_number:end]
            x=test.count('N')+test.count('D')
            if x>no_of_working_days_in_week:
                return True
        return False

        
#pete=Person('Pete', schedule='.N.DDD.D.NNN...DDD...NNN...DDD')
#print(pete.is_day_free(0))
#print(pete.get_number_of_working_days())
#pete.take_one_day_work(29,'N')
#print(pete.is_day_free(0))
#print(pete.get_number_of_working_days())
#print(pete.month_is_full(13))
#print(pete.if_double_work(29, 'D'))
#print(pete.if_week_is_full(12))