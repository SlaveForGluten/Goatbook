"""read and manipulate data from Profiles.txt"""

# !/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import messagebox

import get_date
import check_profiles_input
import set_options


def read():
    """read file"""
    try:
        container = open("Profiles.txt", "r")
        raw_content = container.read()
        container.close()
        return raw_content
    except IOError:
        container.close()
        return "error"


def append(content):
    """add profile at the end of the file"""
    try:
        container = open("Profiles.txt", "a")
        container.write(content + "###")
        container.close()
        messages("saved")
        return "success"
    except IOError:
        container.close()
        return "error"


def overwrite(content):
    """replace all content with modified content"""
    try:
        container = open("Profiles.txt", "w")
        container.write(content)
        return "success"
    except IOError:
        container.close()
        return "error"


def dictionary_to_string(content):
    """
    turn dictionary into string 'key:value#key:value...'
    """
    string = ""
    for key in content:
        string += key + ":" + content[key] + "#"
    return string


def string_to_dictionary(profiles):
    """
    takes string containing profiles, returns list of dictionaries
    each being a profile
    """
    key = ""
    list_of_dicts = list()
    profile_dict = dict()
    for prof in profiles.split("####"):
        for key_and_value in prof.split("#"):
            for key_or_value in key_and_value.split(":"):
                if key == "":
                    key = key_or_value
                else:
                    profile_dict[key] = key_or_value
                    key = ""
        if profile_dict != "":
            list_of_dicts.append(profile_dict)
        profile_dict = dict()
    return list_of_dicts


def count_parameters(parameter):
    """
    count how many goats is sold or dead
    """
    profiles = get_all_profiles()
    counter = 0
    if parameter == "profiles":
        for prof in profiles:
            counter += 1
    elif parameter == "SOLD":
        for prof in profiles:
            if prof["SOLD"] == "sold":
                counter += 1
    elif parameter == "DATE_OF_DEATH":
        for prof in profiles:
            if prof["DATE_OF_DEATH"] != "":
                counter += 1
    return counter


def age_of_goats():
    """
    extract age of goats based on their DoB and current date, send dictionary
    (key is age from 1-15 and value is number of goats with this age) to
    Main().agePyramidChart()
    """

    # dictionary containing ages of goats, key is gender+age from 1 to 15 and
    # value is number of goats with this age
    age_dictionary = {'m1': 0, 'm2': 0, 'm3': 0, 'm4': 0,
                      'm5': 0, 'm6': 0, 'm7': 0, 'm8': 0,
                      'm9': 0, 'm10': 0, 'm11': 0, 'm12': 0,
                      'm13': 0, 'm14': 0, 'm15': 0,
                      'f1': 0, 'f2': 0, 'f3': 0, 'f4': 0,
                      'f5': 0, 'f6': 0, 'f7': 0, 'f8': 0,
                      'f9': 0, 'f10': 0, 'f11': 0, 'f12': 0,
                      'f13': 0, 'f14': 0, 'f15': 0
                      }
    profiles = get_all_profiles()

    # get current date
    curent_date = get_date.get(0)

    # compare date of birth of goat with current date to determine its age
    age = 0
    for prof in profiles:
        if prof["DATE_OF_BIRTH"] != "":
            age = curent_date['ViewedYear'] - int(prof["DATE_OF_BIRTH"][6:10])
            # lower one year if month of birth is lower than actual month
            month_of_birth = int(prof["DATE_OF_BIRTH"][3:5].strip('0'))
            if month_of_birth > curent_date['ViewedMonth']:
                age -= 1
            if prof["GENDER"] == "male":
                if age in (0, 1):
                    age_dictionary['m1'] += 1
                if age == 2:
                    age_dictionary['m2'] += 1
                if age == 3:
                    age_dictionary['m3'] += 1
                if age == 4:
                    age_dictionary['m4'] += 1
                if age == 5:
                    age_dictionary['m5'] += 1
                if age == 6:
                    age_dictionary['m6'] += 1
                if age == 7:
                    age_dictionary['m7'] += 1
                if age == 8:
                    age_dictionary['m8'] += 1
                if age == 9:
                    age_dictionary['m9'] += 1
                if age == 10:
                    age_dictionary['m10'] += 1
                if age == 11:
                    age_dictionary['m11'] += 1
                if age == 12:
                    age_dictionary['m12'] += 1
                if age == 13:
                    age_dictionary['m13'] += 1
                if age == 14:
                    age_dictionary['m14'] += 1
                if age >= 15:
                    age_dictionary['m15'] += 1

            else:
                if age in (0, 1):
                    age_dictionary['f1'] += 1
                if age == 2:
                    age_dictionary['f2'] += 1
                if age == 3:
                    age_dictionary['f3'] += 1
                if age == 4:
                    age_dictionary['f4'] += 1
                if age == 5:
                    age_dictionary['f5'] += 1
                if age == 6:
                    age_dictionary['f6'] += 1
                if age == 7:
                    age_dictionary['f7'] += 1
                if age == 8:
                    age_dictionary['f8'] += 1
                if age == 9:
                    age_dictionary['f9'] += 1
                if age == 10:
                    age_dictionary['f10'] += 1
                if age == 11:
                    age_dictionary['f11'] += 1
                if age == 12:
                    age_dictionary['f12'] += 1
                if age == 13:
                    age_dictionary['f13'] += 1
                if age == 14:
                    age_dictionary['f14'] += 1
                if age >= 15:
                    age_dictionary['f15'] += 1

    return age_dictionary


def get_single_profile(name_and_number):
    """return profile with given name or id number"""
    key = ""
    extracted_profile = dict()
    raw_content = read()
    for profile in raw_content.split("####"):
        for key_and_value in profile.split("#"):
            for key_or_value in key_and_value.split(":"):
                if key == "":
                    key = key_or_value.rstrip()
                else:
                    extracted_profile[key] = key_or_value.rstrip()
                    key = ""
        if extracted_profile["NAME"] != "":
            if extracted_profile["NAME"] == name_and_number["NAME"]:
                return extracted_profile
        if extracted_profile["ID_NUMBER"] != "":
            if extracted_profile["ID_NUMBER"] == name_and_number["ID_NUMBER"]:
                return extracted_profile
    return "error"


def get_all_profiles():
    """
    returns all profiles as list of dictionaries
    """
    raw_content = read()
    list_of_profiles = list()  # list of dictionaries
    single_profile = dict()
    key = ""
    for profile in raw_content.split("####"):
        for key_and_value in profile.split("#"):
            for key_or_value in key_and_value.split(":"):
                if key == "":
                    key = key_or_value
                else:
                    single_profile[key] = key_or_value
                    key = ""
        if single_profile:
            list_of_profiles.append(single_profile)
        single_profile = dict()
    return list_of_profiles


def find_daughter(mother):
    """takes mother name, returns profiles of her kids"""
    raw_content = get_all_profiles()
    list_of_kids = list()
    for profile in raw_content:
        if profile["MOTHER"] == mother:
            list_of_kids.append(profile)
    if list_of_kids:
        return list_of_kids
    return ""


def check_for_unique_properties(content):
    """
    checks if Name and Identification number - two unique properties,
    were not used before
    """
    key = ""
    raw_content = read()
    for old_profile in raw_content.split("####"):
        for key_and_value in old_profile.split("#"):
            for key_or_value in key_and_value.split(":"):
                if key == "":
                    key = key_or_value
                else:
                    if key == "NAME":
                        if content["NAME"] != "":
                            if content["NAME"] == key_or_value.rstrip():
                                messages("name in use")
                                return "name error"

                    if key == "ID_NUMBER":
                        if content["ID_NUMBER"] != "":
                            if content["ID_NUMBER"] == key_or_value.rstrip():
                                messages("id in use")
                                return "number error"
                    key = ""

    return "success"


def save_profile(content):
    """
    saves profile to a Profiles.txt file after validating inputed details
    """
    cleared_content = check_profiles_input.clear(content)
    if check_profiles_input.check(cleared_content) == "success":
        if check_for_unique_properties(cleared_content) == "success":
            append(dictionary_to_string(cleared_content))
            return "success"
    return "error"


def delete_profile(content):
    """remove profile from Profiles.text"""
    all_profiles = get_all_profiles()

    for profile in all_profiles:
        if profile["NAME"] == content["NAME"] and content["NAME"] != "":
            all_profiles.remove(profile)
        elif (profile["ID_NUMBER"] == content["ID_NUMBER"] and
              content["ID_NUMBER"] != ""):
            all_profiles.remove(profile)

    string_to_save = ""
    for prof in all_profiles:
        string_to_save = (string_to_save +
                          dictionary_to_string(prof) +
                          "####")

    if overwrite(string_to_save) == "success":
        return "success"

    return "error"


def edit_profile(name_and_number, content):
    """
    delete profile before editing and save the one edited

    """
    if check_profiles_input.check(content) == "success":
        raw_content = read()
        for profile in raw_content.split("####"):
            if profile.find("NAME:"+name_and_number["NAME"]):
                if name_and_number["NAME"] != "":
                    if delete_profile(name_and_number) == "success":
                        if save_profile(content) == "success":
                            return "success"
                        return "error"
                    return "error"
            if profile.find("ID_NUMBER:"+name_and_number["ID_NUMBER"]):
                if name_and_number["ID_NUMBER"] != "":
                    if delete_profile(name_and_number) == "success":
                        if save_profile(content) == "success":
                            return "success"
                        return "error"
                    return "error"


def messages(message_type):
    language_dict = set_options.Options()
    language_dict.get_text_dict("process_profiles_data")
    lang_dict = language_dict.widget_text_dictionary
    if message_type == "saved":
        messagebox.showinfo(lang_dict["messagebox"], lang_dict["messagebox1"])
    if message_type == "name in use":
        messagebox.showinfo(lang_dict["messagebox2"], lang_dict["messagebox3"])
    if message_type == "id in use":
        messagebox.showinfo(lang_dict["messagebox2"], lang_dict["messagebox4"])
