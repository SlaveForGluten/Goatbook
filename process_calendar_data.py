"""saves, reads, deletes events from Calendar.text"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import random
from tkinter import messagebox

import get_date
import set_options


def save_pregnancy(date_dict):
    """saves pregnancy event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("process_calendar_data")
    lang_dict = language_dict.widget_text_dictionary

    random_num = random.randint(1, 1000000)
    try:
        container = open("Calendar.txt", "a")

        container.write(str(date_dict['ViewedYear'])+'/' +
                        str(date_dict['ViewedMonth'])+'/' +
                        str(date_dict['DayOfTheNewEvent'])+'-' +
                        "PREGNANCY"+'-'+str(date_dict['Input1'])+'-' +
                        str(date_dict['Input2'])+'-'+str(random_num)+'\n')
        # adds "DELIVERY" event 150 days after "PREGNANCY" event
        pregnancy_period = 150
        pregnancy_period -= (
            date_dict['DaysInViewedMonth'] - date_dict['DayOfTheNewEvent'])
        timer = 0
        counter = date_dict['DistancefromToday']
        while timer <= pregnancy_period:
            counter += 1
            vase = get_date.get(counter)
            timer = vase['DaysInViewedMonth']

            if timer == pregnancy_period:
                messagebox.showinfo(
                    lang_dict["messagebox1"], lang_dict["messagebox2"] +
                    str(vase['ViewedYear'])+'/'+str(vase['ViewedMonth'])+'/' +
                    str(pregnancy_period)+".")
                container.write(
                    str(vase['ViewedYear'])+'/'+str(vase['ViewedMonth'])+'/' +
                    str(pregnancy_period)+'-'+"DELIVERY"+'-' +
                    str(date_dict['Input1'])+'-'+str(date_dict['Input2']) +
                    '-'+str(random_num)+'\n')
                return

            pregnancy_period -= timer
            if pregnancy_period < 0:
                messagebox.showinfo(
                    lang_dict["messagebox1"], lang_dict["messagebox2"] +
                    str(vase['ViewedYear'])+'/'+str(vase['ViewedMonth']) +
                    '/'+str(pregnancy_period+timer)+".")
                container.write(
                    str(vase['ViewedYear'])+'/' + str(vase['ViewedMonth']) +
                    '/'+str(pregnancy_period+timer)+'-'+"DELIVERY"+'-' +
                    str(date_dict['Input1'])+'-'+str(date_dict['Input2']) +
                    '-'+str(random_num)+'\n')
                return

            if timer > pregnancy_period:
                if vase['ViewedMonth']+1 < 12:
                    messagebox.showinfo(
                        lang_dict["messagebox1"], lang_dict["messagebox2"] +
                        str(vase['ViewedYear'])+'/' +
                        str(vase['ViewedMonth']+1) + '/' +
                        str(pregnancy_period) + ".")
                    container.write(
                        str(vase['ViewedYear'])+'/' +
                        str(vase['ViewedMonth']+1)+'/' +
                        str(pregnancy_period)+'-'+"DELIVERY"+'-' +
                        str(date_dict['Input1'])+'-' +
                        str(date_dict['Input2'])+'-' +
                        str(random_num)+'\n')
                    return
                else:
                    messagebox.showinfo(
                        lang_dict["messagebox1"], lang_dict["messagebox2"] +
                        str(vase['ViewedYear']+1)+'/'+str(1)+'/' +
                        str(pregnancy_period)+".")
                    container.write(
                        str(vase['ViewedYear'] + 1)+'/'+str(1)+'/' +
                        str(pregnancy_period)+'-'+"DELIVERY"+'-' +
                        str(date_dict['Input1'])+'-' +
                        str(date_dict['Input2'])+'-' +
                        str(random_num)+'\n')

    except IOError:
        messagebox.showinfo(lang_dict["messagebox3"], lang_dict["messagebox4"])
        container.close()
    else:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox5"])
        container.close()


def save_medicine(date_dict):
    """saves medicine event"""

    language_dict = set_options.Options()
    language_dict.get_text_dict("process_calendar_data")
    lang_dict = language_dict.widget_text_dictionary

    random_num = random.randint(1, 1000000)
    try:
        container = open("Calendar.txt", "a")

        dosing_days_counter = date_dict['Input3']
        medicine_counter = 0
        day_counter = 0

        def add_withdrawal(year, month, day, days_in_month, months_in_future):
            day_counter = 0
            withdrawal_counter = 1
            withdrawal_days_counter = date_dict['Input4']

            while withdrawal_days_counter > 0:
                if day+withdrawal_counter <= days_in_month:
                    container.write(
                        str(year)+'/'+str(month)+'/' +
                        str(day+withdrawal_counter)+'-'+"WITHDRAWAL" +
                        '-'+str(date_dict['Input1'])+'-' +
                        str(date_dict['Input2'])+'-'+str(date_dict['Input3']) +
                        '-'+str(date_dict['Input4'] + 1 - withdrawal_counter) +
                        '-'+str(date_dict['Input5'])+'-'+str(random_num)+'\n')
                    withdrawal_counter += 1
                    withdrawal_days_counter -= 1
                else:
                    vase = get_date.get(months_in_future+1)
                    container.write(
                        str(vase['ViewedYear'])+'/'+str(vase['ViewedMonth']) +
                        '/'+str(1+day_counter)+'-'+"WITHDRAWAL"+'-' +
                        str(date_dict['Input1'])+'-'+str(date_dict['Input2']) +
                        '-'+str(date_dict['Input3'])+'-' +
                        str(date_dict['Input4']+1-withdrawal_counter) +
                        '-'+str(date_dict['Input5'])+'-'+str(random_num)+'\n')
                    day_counter += 1
                    withdrawal_counter += 1
                    withdrawal_days_counter -= 1

        while dosing_days_counter > 0:
            if(date_dict['DayOfTheNewEvent'] + medicine_counter <=
               date_dict['DaysInViewedMonth']):
                container.write(
                    str(date_dict['ViewedYear'])+'/' +
                    str(date_dict['ViewedMonth'])+'/' +
                    str(date_dict['DayOfTheNewEvent']+medicine_counter) +
                    '-'+"MEDICINE"+'-'+str(date_dict['Input1'])+'-' +
                    str(date_dict['Input2'])+'-' +
                    str(date_dict['Input3']-medicine_counter) +
                    '-'+str(date_dict['Input4'])+'-' +
                    str(date_dict['Input5'])+'-'+str(random_num)+'\n')
                if date_dict['Input4'] != 0 and dosing_days_counter == 1:
                    add_withdrawal(
                        date_dict['ViewedYear'], date_dict['ViewedMonth'],
                        date_dict['DayOfTheNewEvent']+medicine_counter,
                        date_dict['DaysInViewedMonth'], 0)
                medicine_counter += 1
                dosing_days_counter -= 1
            else:
                vase = get_date.get(1)
                container.write(
                    str(vase['ViewedYear'])+'/'+str(vase['ViewedMonth'])+'/' +
                    str(1+day_counter)+'-'+"MEDICINE"+'-' +
                    str(date_dict['Input1'])+'-'+str(date_dict['Input2'])+'-' +
                    str(date_dict['Input3']-medicine_counter)+'-' +
                    str(date_dict['Input4'])+'-'+str(date_dict['Input5'])+'-' +
                    str(random_num)+'\n')
                if date_dict['Input4'] != 0 and dosing_days_counter == 1:
                    add_withdrawal(
                        vase['ViewedYear'], vase['ViewedMonth'], 1 +
                        day_counter, vase['DaysInViewedMonth'], 1)
                day_counter += 1
                medicine_counter += 1
                dosing_days_counter -= 1

        def add_withdrawal(year, month, day, days_in_month, months_in_future):
            day_counter = 0
            withdrawal_counter = 1
            withdrawal_days_counter = date_dict['Input4']
            while withdrawal_days_counter > 0:
                if day+withdrawal_counter <= days_in_month:
                    container.write(
                        str(year)+'/'+str(month)+'/' +
                        str(day+withdrawal_counter)+'-' +
                        str(date_dict['EventType'])+'-' +
                        str(date_dict['Input1'])+'-' +
                        str(date_dict['Input2']) + '-' +
                        str(date_dict['Input3']-withdrawal_counter)+'-' +
                        str(date_dict['Input4'])+'-' +
                        str(date_dict['Input5'])+'-'+str(random_num)+'\n')
                    withdrawal_counter += 1
                    withdrawal_days_counter -= 1
                else:
                    vase = get_date.get(months_in_future+1)
                    container.write(
                        str(vase['ViewedYear'])+'/' +
                        str(vase['ViewedMonth']) + '/' +
                        str(1+day_counter)+'-'+str(date_dict['EventType'])+'-'+
                        str(date_dict['Input1'])+'-' +
                        str(date_dict['Input2'])+'-' +
                        str(date_dict['Input3']-withdrawal_counter)+'-' +
                        str(date_dict['Input4'])+'-' +
                        str(date_dict['Input5'])+'-' +
                        str(random_num)+'\n')
                    day_counter += 1
                    withdrawal_counter += 1
                    withdrawal_days_counter -= 1
    except IOError:
        messagebox.showinfo(lang_dict["messagebox3"], lang_dict["messagebox4"])
        container.close()
    else:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox5"])
        container.close()


def save_milking(date_dict):
    """saves milking event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("process_calendar_data")
    lang_dict = language_dict.widget_text_dictionary

    random_num = random.randint(1, 1000000)
    try:
        container = open("Calendar.txt", "a")
        container.write(
            str(date_dict['ViewedYear'])+'/' +
            str(date_dict['ViewedMonth'])+'/' +
            str(date_dict['DayOfTheNewEvent'])+'-'+"MILKING"+'-' +
            str(date_dict['Input1'])+'-'+str(random_num)+'\n')

    except IOError:
        messagebox.showinfo(lang_dict["messagebox3"], lang_dict["messagebox4"])
        container.close()
    else:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox5"])
        container.close()


def save_other(date_dict):
    """saves other event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("process_calendar_data")
    lang_dict = language_dict.widget_text_dictionary

    random_num = random.randint(1, 1000000)
    try:
        container = open("Calendar.txt", "a")

        container.write(
            str(date_dict['ViewedYear'])+'/' +
            str(date_dict['ViewedMonth'])+'/' +
            str(date_dict['DayOfTheNewEvent'])+'-'+"OTHER"+'-' +
            str(date_dict['Input1'])+'-'+str(date_dict['Input2'])+'-' +
            str(random_num)+'\n')

    except IOError:
        messagebox.showinfo(lang_dict["messagebox3"], lang_dict["messagebox4"])
        container.close()
    else:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox5"])
        container.close()


def get_event(date_of_event):
    """returns events occurring on a given date"""
    try:
        container = open("Calendar.txt", "r")
        content = list()
        content = container.readlines()
        container.close()
        one_prof_list = []
        final_list = []

        for i in content:
            one_prof_list = i.split("-")
            if one_prof_list[0] == date_of_event:
                final_list.append(i)
        return final_list
    except IOError:
        container.close()
        return
    else:
        container.close()
        return


def delete_event(number):
    """takes unique event number and deletes it from txt file"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("process_calendar_data")
    lang_dict = language_dict.widget_text_dictionary

    # try to open Calendar.txt and read all lines
    # each containing one event to a 'content' list
    try:
        container = open("Calendar.txt", "r")
        content = list()
        content = container.readlines()
        container.close()
        one_event_list = []
        list_of_stuff_to_remove = []

        # save all events you want to delete to a list
        for i in content:
            one_event_list = i.split("-")
            if one_event_list[len(one_event_list)-1] == number:
                list_of_stuff_to_remove.append(i)

        # delete those events from your 'content'
        for stuff in list_of_stuff_to_remove:
            content.remove(stuff)

        # rewrite Calendar.txt with events from 'content'
        try:
            container = open("Calendar.txt", "w")
            for line in content:
                container.write(line)
        except IOError:
            messagebox.showinfo(
                lang_dict["messagebox3"], lang_dict["messagebox6"])
            container.close()
        else:
            messagebox.showinfo(
                lang_dict["messagebox1"], lang_dict["messagebox7"])
            container.close()
        return
    except IOError:
        container.close()
        return
    else:
        container.close()
        return


def get_milking_events():
    """
    returns milking events in a dictionary with date as a key and
    quantity of milk as a value
    """
    container = open("Calendar.txt", "r")
    content = list()
    content = container.readlines()
    container.close()
    milking_dictionary = {}
    for i in content:
        one_event_list = i.split("-")
        if one_event_list[1] == "MILKING":
            milking_dictionary[one_event_list[0]] = one_event_list[2]
    return milking_dictionary


def event_types_per_day(event_date):
    """takes date, returns types of events occurring on that date"""

    # this gets whole lines of events if date matches, I need only type
    list_of_events = get_event(event_date)
    dictionary = {}
    # cby default no event occurred
    dictionary["PREGNANCY"] = 0
    dictionary["MEDICINE"] = 0
    dictionary["MILKING"] = 0
    dictionary["OTHER"] = 0
    dictionary["DELIVERY"] = 0
    dictionary["WITHDRAWAL"] = 0

    # if event(s) of particular type occurred,
    # change value in dictionary to 1
    for i in list_of_events:
        single_event = []
        single_event = i.split("-")
        if single_event[1] == "PREGNANCY":
            dictionary["PREGNANCY"] = 1
        elif single_event[1] == "MEDICINE":
            dictionary["MEDICINE"] = 1
        elif single_event[1] == "MILKING":
            dictionary["MILKING"] = 1
        elif single_event[1] == "OTHER":
            dictionary["OTHER"] = 1
        elif single_event[1] == "DELIVERY":
            dictionary["DELIVERY"] = 1
        elif single_event[1] == "WITHDRAWAL":
            dictionary["WITHDRAWAL"] = 1

    total = (dictionary["PREGNANCY"] +
             dictionary["MEDICINE"] +
             dictionary["MILKING"] +
             dictionary["OTHER"] +
             dictionary["DELIVERY"] +
             dictionary["WITHDRAWAL"])

    dictionary["SUM"] = total
    return dictionary


def get_month_name(month_counter):
    """returns name of the month depending on month number"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("process_calendar_data")
    lang_dict = language_dict.widget_text_dictionary

    date_dict = get_date.get(month_counter)

    if int(date_dict['ViewedMonth']) == 1:
        month_name = lang_dict["month1"]
    elif int(date_dict['ViewedMonth']) == 2:
        month_name = lang_dict["month2"]
    elif int(date_dict['ViewedMonth']) == 3:
        month_name = lang_dict["month3"]
    elif int(date_dict['ViewedMonth']) == 4:
        month_name = lang_dict["month4"]
    elif int(date_dict['ViewedMonth']) == 5:
        month_name = lang_dict["month5"]
    elif int(date_dict['ViewedMonth']) == 6:
        month_name = lang_dict["month6"]
    elif int(date_dict['ViewedMonth']) == 7:
        month_name = lang_dict["month7"]
    elif int(date_dict['ViewedMonth']) == 8:
        month_name = lang_dict["month8"]
    elif int(date_dict['ViewedMonth']) == 9:
        month_name = lang_dict["month9"]
    elif int(date_dict['ViewedMonth']) == 10:
        month_name = lang_dict["month10"]
    elif int(date_dict['ViewedMonth']) == 11:
        month_name = lang_dict["month11"]
    elif int(date_dict['ViewedMonth']) == 12:
        month_name = lang_dict["month12"]

    return month_name
