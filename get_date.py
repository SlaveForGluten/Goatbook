"""
contains functions that returns date and time info
(mostly to calendar modules), uses build-in calendar methods
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import calendar


def get_year_and_monthranges():
    """returns current year and months-range of months that year"""
    dictionary = {}
    now = datetime.datetime.now()
    dictionary['CurrentYear'] = now.year
    month_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    for mon, month in enumerate(month_list, 1):
        dictionary[month] = calendar.monthrange(
            dictionary['CurrentYear'], mon)[1]
    return dictionary


def get(counter):
    """
    takes distance from todays month (-2 is two months ago
    from todays month which is 0 ) returns dictionary containing details
    of given month
    """
    if counter == 0:
        now = datetime.datetime.now()
        calendar_dict = {}
        calendar_dict['ViewedYear'] = now.year
        calendar_dict['ViewedMonth'] = now.month
        calendar_dict['ViewedDay'] = now.day
        calendar_dict['FirstDayOfTheViewedMonth'] = calendar.monthrange(
            calendar_dict['ViewedYear'], calendar_dict['ViewedMonth'])[0]
        calendar_dict['DaysInViewedMonth'] = calendar.monthrange(
            calendar_dict['ViewedYear'], calendar_dict['ViewedMonth'])[1]
        calendar_dict['CurrentDayOfTheWeek'] = now.weekday()

        return calendar_dict

    if counter < 0:
        calendar_dict = {}
        now = datetime.datetime.now()
        if now.month - 1 + counter < 0:
            total_months = now.month - 1 + counter
            year_count = 0
            while total_months < 0:
                total_months += 12
                year_count -= 1
            calendar_dict['ViewedYear'] = now.year + year_count
            calendar_dict['ViewedMonth'] = total_months + 1
            calendar_dict['ViewedDay'] = -1

        else:
            calendar_dict['ViewedYear'] = now.year
            calendar_dict['ViewedMonth'] = now.month + counter
            calendar_dict['ViewedDay'] = -1

        calendar_dict['FirstDayOfTheViewedMonth'] = calendar.monthrange(
            calendar_dict['ViewedYear'], calendar_dict['ViewedMonth'])[0]
        calendar_dict['DaysInViewedMonth'] = calendar.monthrange(
            calendar_dict['ViewedYear'], calendar_dict['ViewedMonth'])[1]
        calendar_dict['CurrentDayOfTheWeek'] = 0

        return calendar_dict

    if counter > 0:

        calendar_dict = {}
        now = datetime.datetime.now()
        if now.month + counter > 12:
            total_months = now.month + counter
            year_count = 0
            while total_months > 12:
                total_months -= 12
                year_count += 1
            calendar_dict['ViewedYear'] = now.year + year_count
            calendar_dict['ViewedMonth'] = total_months
            calendar_dict['ViewedDay'] = -1
        else:
            calendar_dict['ViewedYear'] = now.year
            calendar_dict['ViewedMonth'] = now.month + counter
            calendar_dict['ViewedDay'] = -1

        calendar_dict['FirstDayOfTheViewedMonth'] = calendar.monthrange(
            calendar_dict['ViewedYear'], calendar_dict['ViewedMonth'])[0]
        calendar_dict['DaysInViewedMonth'] = calendar.monthrange(
            calendar_dict['ViewedYear'], calendar_dict['ViewedMonth'])[1]
        calendar_dict['CurrentDayOfTheWeek'] = 0
        return calendar_dict
