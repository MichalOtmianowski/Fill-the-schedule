# -*- coding: cp1250 -*-
import unittest
import person3


class PersonTests(unittest.TestCase):
    """
    Testy metod zawartych w klasie Person z modułu person.
    """
    def setUp(self):
        self.person = person3.Person(name='name', schedule='...DDD...NNN...DDD...NNN...DDD')

    def test_is_day_free(self):
        """Test metody is_day_free."""

        self.assertEqual(self.person.is_day_free(2), True)
        self.assertEqual(self.person.is_day_free(3), False)

    def test_take_one_day_work(self):
        """Test metody take_one_day_work."""

        a_person = person3.Person(name='name', schedule='...DDD...NNN...DDD...NNN...DDD')
        a_person.take_one_day_work(0, 'N')
        a_person.take_one_day_work(7, 'D')
        self.assertEqual(a_person.schedule, 'N..DDD.D.NNN...DDD...NNN...DDD')

    def test_get_number_of_working_days(self):
        """Test metody get_number_of_working_days."""

        self.assertEqual(self.person.get_number_of_working_days(), 15)

    def test_month_is_full(self):
        """Test metody month_is_full."""

        self.assertEqual(self.person.month_is_full(15), True)
        self.assertEqual(self.person.month_is_full(16), False)

    def test_if_double_work(self):
        """Test metody if_double_work."""

        a_person = person3.Person(name='name', schedule='.D............................')
        self.assertEqual(a_person.if_double_work(0, 'N'), True)
        self.assertEqual(a_person.if_double_work(0, 'D'), False)

        a_person = person3.Person(name='name', schedule='.N............................')
        self.assertEqual(a_person.if_double_work(0, 'N'), False)
        self.assertEqual(a_person.if_double_work(0, 'D'), False)

        a_person = person3.Person(name='name', schedule='D.............................')
        self.assertEqual(a_person.if_double_work(1, 'N'), False)
        self.assertEqual(a_person.if_double_work(1, 'D'), False)

        a_person = person3.Person(name='name', schedule='N.............................')
        self.assertEqual(a_person.if_double_work(1, 'N'), False)
        self.assertEqual(a_person.if_double_work(1, 'D'), True)

        a_person = person3.Person(name='name', schedule='............D.................')
        self.assertEqual(a_person.if_double_work(11, 'D'), False)
        self.assertEqual(a_person.if_double_work(11, 'N'), True)

        a_person = person3.Person(name='name', schedule='............N.................')
        self.assertEqual(a_person.if_double_work(13, 'D'), True)
        self.assertEqual(a_person.if_double_work(13, 'N'), False)

    def test_if_week_is_full(self):
        """Test metody if_week_is_full."""
        print('schedule ', self.person.schedule)
        self.assertEqual(self.person.if_week_is_full(6), False)
        self.assertEqual(self.person.if_week_is_full(12), False)

        a_person = person3.Person(name='name', schedule='.N.DDD.D.NNN...DDD...NNN...DDD')
        self.assertEqual(a_person.if_week_is_full(2), True)
        self.assertEqual(a_person.if_week_is_full(12), True)


if __name__ == '__main__':
    unittest.main()
