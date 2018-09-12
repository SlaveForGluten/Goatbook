"""clear data and sort profiles for compare_profiles.py module"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import get_date
import set_options


def show(profiles, show, sorting_criteria):
    """type of profiles to be displayed (active, all, inactive etc.)"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("compare_profiles_tab")
    lang_dict = language_dict.widget_text_dictionary

    filtered_profiles = list()
    if show == lang_dict["pick_prof_tuple1"]:
        for prof in profiles:
            if prof['SOLD'] == 'not_sold' and prof['DATE_OF_DEATH'] == '':
                filtered_profiles.append(prof)
        return sort(filtered_profiles, sorting_criteria, lang_dict)

    if show == lang_dict["pick_prof_tuple2"]:
        for prof in profiles:
            if(prof['SOLD'] == 'not_sold' and
               prof['DATE_OF_DEATH'] == '' and
               prof['GENDER'] == 'female'):
                filtered_profiles.append(prof)
        return sort(filtered_profiles, sorting_criteria, lang_dict)

    if show == lang_dict["pick_prof_tuple3"]:
        for prof in profiles:
            if(prof['SOLD'] == 'not_sold' and
               prof['DATE_OF_DEATH'] == '' and
               prof['GENDER'] == 'male'):
                filtered_profiles.append(prof)
        return sort(filtered_profiles, sorting_criteria, lang_dict)

    if show == lang_dict["pick_prof_tuple4"]:
        for prof in profiles:
            if prof['SOLD'] == 'sold' or prof['DATE_OF_DEATH'] != '':
                filtered_profiles.append(prof)
        return sort(filtered_profiles, sorting_criteria, lang_dict)

    if show == lang_dict["pick_prof_tuple5"]:
        return sort(profiles, sorting_criteria, lang_dict)


def sort(profiles, sorting_criteria, lang_dict):
    """
    sort profiles that were filtered by show function
    some of the categories: name a-z,name z-a, age low-high etc.
    """
    list_of_values = list()
    sorted_profiles = list()

    if sorting_criteria == lang_dict["sort_prof_tuple1"]:
        for prof in profiles:
            list_of_values.append(prof['NAME'])
        list_of_values.sort()
        for name in list_of_values:
            for prof in profiles:
                if name == prof['NAME']:
                    sorted_profiles.append(prof)

    elif sorting_criteria == lang_dict["sort_prof_tuple2"]:
        for prof in profiles:
            list_of_values.append(prof['NAME'])
        list_of_values.sort(reverse=True)
        for name in list_of_values:
            for prof in profiles:
                if name == prof['NAME']:
                    sorted_profiles.append(prof)

    elif sorting_criteria == lang_dict["sort_prof_tuple3"]:
        counter = 60
        while counter > 0:
            for prof in profiles:
                if prof["GENDER"] == "female":
                    if prof["MILKING"] != "":
                        milking = int(prof["MILKING"][0]+prof["MILKING"][2])
                        if milking == counter:
                            sorted_profiles.append(prof)
            counter -= 1
        for prof in profiles:
            if prof["GENDER"] == "female":
                if prof["MILKING"] == "":
                    sorted_profiles.append(prof)
        for prof in profiles:
            if prof["GENDER"] == "male":
                sorted_profiles.append(prof)

    elif sorting_criteria == lang_dict["sort_prof_tuple4"]:
        counter = 0
        while counter < 60:
            for prof in profiles:
                if prof["GENDER"] == "female":
                    if prof["MILKING"] != "":
                        milking = int(prof["MILKING"][0]+prof["MILKING"][2])
                        if milking == counter:
                            sorted_profiles.append(prof)
            counter += 1
        for prof in profiles:
            if prof["GENDER"] == "female":
                if prof["MILKING"] == "":
                    sorted_profiles.append(prof)
        for prof in profiles:
            if prof["GENDER"] == "male":
                sorted_profiles.append(prof)

    elif sorting_criteria == lang_dict["sort_prof_tuple5"]:
        counter = 20
        while counter > 0:
            for prof in profiles:
                if prof["DATE_OF_BIRTH"] != "":
                    age = int(
                        prof["DATE_OF_BIRTH"][11:13].strip(lang_dict["age"]))
                    if age == counter:
                        sorted_profiles.append(prof)
            counter -= 1
        for prof in profiles:
            if prof["DATE_OF_BIRTH"] == "":
                sorted_profiles.append(prof)

    elif sorting_criteria == lang_dict["sort_prof_tuple6"]:
        counter = 0
        while counter < 20:
            for prof in profiles:
                if prof["DATE_OF_BIRTH"] != "":
                    age = int(
                        prof["DATE_OF_BIRTH"][11:13].strip(lang_dict["age"]))
                    if age == counter:
                        sorted_profiles.append(prof)
            counter += 1
        for prof in profiles:
            if prof["DATE_OF_BIRTH"] == "":
                sorted_profiles.append(prof)

    elif sorting_criteria == lang_dict["sort_prof_tuple7"]:
        for prof in profiles:
            if prof['GENDER'] == 'female':
                sorted_profiles.append(prof)
        for prof in profiles:
            if prof['GENDER'] == 'male':
                sorted_profiles.append(prof)

    return sorted_profiles


def clear_milking(profiles):
    """
    from all milking mesurments take the most recent one to display
    it in 'compare profiles' window
    """
    list_of_values = list()
    sorted_profiles = list()
    for prof in profiles:
        if prof['GENDER'] != 'male':
            if prof['MILKING'] != '':
                list_of_values = prof['MILKING'].split('@')
                list_of_values = list_of_values[len(list_of_values)-1]
                list_of_values = list_of_values.split('-')
                prof['MILKING'] = list_of_values[1]
                sorted_profiles.append(prof)
                list_of_values = list()

    for prof in profiles:
        if prof['GENDER'] == 'female' and prof['MILKING'] == '':
            sorted_profiles.append(prof)
        if prof['GENDER'] == 'male':
            sorted_profiles.append(prof)

    return sorted_profiles


def clear_fat_content(profiles):
    """
    from all 'fat content' mesurments take the most recent one to display
    it in 'compare profiles' window
    """
    list_of_values = list()
    sorted_profiles = list()
    for prof in profiles:
        if prof['GENDER'] != 'male':
            if prof['FAT_CONTENT'] != '':
                list_of_values = prof['FAT_CONTENT'].split('@')
                list_of_values = list_of_values[len(list_of_values)-1]
                list_of_values = list_of_values.split('-')
                prof['FAT_CONTENT'] = list_of_values[1]
                sorted_profiles.append(prof)
                list_of_values = list()

    for prof in profiles:
        if prof['GENDER'] == 'female' and prof['FAT_CONTENT'] == '':
            sorted_profiles.append(prof)
        if prof['GENDER'] == 'male':
            sorted_profiles.append(prof)

    return sorted_profiles


def clear_date_of_birth(profiles):
    """clear dob input"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("sort_profiles")
    lang_dict = language_dict.widget_text_dictionary

    curent_date = get_date.get(0)
    sorted_profiles = list()
    age = 0
    for prof in profiles:
        if prof["DATE_OF_BIRTH"] != "" and prof["DATE_OF_DEATH"] == "":
            age = curent_date['ViewedYear'] - int(prof["DATE_OF_BIRTH"][6:10])
            # lower one year if month of birth is lower than actual month
            if(int(prof["DATE_OF_BIRTH"][3:5].strip('0')) >
               curent_date['ViewedMonth']):
                age -= 1
            prof["DATE_OF_BIRTH"] = (prof["DATE_OF_BIRTH"]+"(" + str(age) +
                                     lang_dict["age"] + ")")
            sorted_profiles.append(prof)
        elif prof["DATE_OF_BIRTH"] != "" and prof["DATE_OF_DEATH"] != "":
            age = (int(prof["DATE_OF_DEATH"][6:10]) -
                   int(prof["DATE_OF_BIRTH"][6:10]))
            prof["DATE_OF_BIRTH"] = (prof["DATE_OF_BIRTH"]+"(" +
                                     str(age) + lang_dict["age"] + ")")
            sorted_profiles.append(prof)
        else:
            sorted_profiles.append(prof)

    return sorted_profiles
