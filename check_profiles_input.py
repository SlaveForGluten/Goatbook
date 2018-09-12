"""checks if input from add profile and edit profile meets the proper fomrat"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import messagebox

import set_options


def clear(profile):
    """clear data from clues pre-inputed in the interface"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("add_profiles_tab")
    lang_dict = language_dict.widget_text_dictionary

    if profile["NAME"] == lang_dict["name_entry"]:
        profile["NAME"] = ""

    if profile["MOTHER"] == lang_dict["name_entry"]:
        profile["MOTHER"] = ""

    if profile["FATHER"] == lang_dict["name_entry"]:
        profile["FATHER"] = ""

    if profile["DATE_OF_BIRTH"] == lang_dict["dob_entry"]:
        profile["DATE_OF_BIRTH"] = ""

    if profile["DATE_OF_DEATH"] == lang_dict["dob_entry"]:
        profile["DATE_OF_DEATH"] = ""
    return profile


def check(profile):
    """check profiles input"""

    # at least one unique property ('Name' or 'IdentificationNumber')
    # and 'Gender' required to add a new profile
    if profile['NAME'] == "" and profile['ID_NUMBER'] == "":
        messages("empty fields")
        return "failure"
    if profile['GENDER'] == "":
        messages("no gender")
        return "failure"

    # check if "Name" is shorter than 30 signs, starts with capital letter(s)
    # and for '#' sign (which I use for data handling)
    if profile["NAME"] != "":
        if len(profile["NAME"]) > 30:
            messages("less than 30")
            return "failure"
        if profile["NAME"].istitle() is False:
            messages("capital")
            return "failure"
        if profile["NAME"].find("#") != -1:
            messages("#")
            return "failure"

    # if  birth date field filled check if input meets the DD/MM/YYYY format
    if profile["DATE_OF_BIRTH"] == "":
        pass
    else:
        if len(profile["DATE_OF_BIRTH"]) != 10:
            messages("date")
            return "failure"
        if(profile["DATE_OF_BIRTH"][0:1].isdigit() is False or
           profile["DATE_OF_BIRTH"][3:4].isdigit() is False or
           profile["DATE_OF_BIRTH"][6:9].isdigit() is False):
            messages("date")
            return "failure"
        if(profile["DATE_OF_BIRTH"][2] != "/" or
           profile["DATE_OF_BIRTH"][5] != '/'):
            messages("date")
            return "failure"
        if(int(profile["DATE_OF_BIRTH"][0]) > 3 or
           int(profile["DATE_OF_BIRTH"][3]) > 1 or
           int(profile["DATE_OF_BIRTH"][3:4]) > 12 or
           int(profile["DATE_OF_BIRTH"][6]) > 2):
            messages("date")
            return "failure"

    # check date of death same as above
    if profile["DATE_OF_DEATH"] == "":
        pass
    else:
        if len(profile["DATE_OF_DEATH"]) != 10:
            messages("date")
            return "failure"
        if(profile["DATE_OF_DEATH"][0:1].isdigit() is False or
           profile["DATE_OF_DEATH"][3:4].isdigit() is False or
           profile["DATE_OF_DEATH"][6:9].isdigit() is False):
            messages("date")
            return "failure"
        if(profile["DATE_OF_DEATH"][2] != "/" or
           profile["DATE_OF_DEATH"][5] != '/'):
            messages("date")
            return "failure"
        if(int(profile["DATE_OF_DEATH"][0]) > 3 or
           int(profile["DATE_OF_DEATH"][3]) > 1 or
           int(profile["DATE_OF_DEATH"][3:4]) > 12 or
           int(profile["DATE_OF_DEATH"][6]) > 2):
            messages("date")
            return "failure"

    # check for '#' sign - i use it to separate dictionary items in
    # Profiles.txt so it would mess up my data
    if profile["ID_NUMBER"] == "":
        pass
    else:
        if profile["ID_NUMBER"].find("#") != -1:
            messages("#")
            return "failure"

    # if not empty check same as Name
    if profile["MOTHER"] != "":
        if len(profile["MOTHER"]) > 30:
            messages("less than 30")
            return "failure"
        if profile["MOTHER"].istitle() is False:
            messages("capital")
            return "failure"
        if profile["MOTHER"].find("#") != -1:
            messages("#")
            return "failure"

    # if not empty check same as Name
    if profile["FATHER"] != "":
        if len(profile["FATHER"]) > 30:
            messages("less than 30")
            return "failure"
        if profile["FATHER"].istitle() is False:
            messages("capital")
            return "failure"
        if profile["FATHER"].find("#") != -1:
            messages("#")
            return "failure"

    # check all ScroledText inputs for "@" and "#" signs, if not in use search
    # for '\n' if present suplement it with '@' sign. Leaving '\n' would
    # explode my data: in "Profiles.txt" file, one line covers one profile
    if profile["CHARACTERISTICS"] == "":
        pass
    else:
        if profile["CHARACTERISTICS"].find("@") != -1:
            messages("@")
            return "failure"
        if profile["CHARACTERISTICS"].find("#") != -1:
            messages("#")
            return "failure"
        if profile["CHARACTERISTICS"].find("\n") != -1:
            profile["CHARACTERISTICS"] = "@".join(
                profile["CHARACTERISTICS"].split("\n"))

    if profile["HISTORY_OF_DISEASE"] == "":
        pass
    else:
        if profile["HISTORY_OF_DISEASE"].find("@") != -1:
            messages("@")
            return "failure"
        if profile["HISTORY_OF_DISEASE"].find("#") != -1:
            messages("#")
            return "failure"
        if profile["HISTORY_OF_DISEASE"].find("\n") != -1:
            profile["HISTORY_OF_DISEASE"] = "@".join(
                profile["HISTORY_OF_DISEASE"].split("\n"))

    if profile["SOLD_INFO"] == "":
        pass
    else:
        if profile["SOLD_INFO"].find("@") != -1:
            messages("@")
            return "failure"
        if profile["SOLD_INFO"].find("#") != -1:
            messages("#")
            return "failure"
        if profile["SOLD_INFO"].find("\n") != -1:
            profile["SOLD_INFO"] = "@".join(profile["SOLD_INFO"].split("\n"))

    if profile["BOUGHT_INFO"] == "":
        pass
    else:
        if profile["BOUGHT_INFO"].find("@") != -1:
            messages("@")
            return "failure"
        if profile["BOUGHT_INFO"].find("#") != -1:
            messages("#")
            return "failure"
        if profile["BOUGHT_INFO"].find("\n") != -1:
            profile["BOUGHT_INFO"] = "@".join(
                profile["BOUGHT_INFO"].split("\n"))

    # check milking input
    if profile["GENDER"] == "male":
        pass
    else:
        if profile['MILKING'] == '':
            pass
        else:
            all_mesurements = profile['MILKING'].split('@')
            for single_mesurement in all_mesurements:
                if len(single_mesurement) != 9:
                    messages("milking")
                    return "failure"
                if(single_mesurement[0:1].isdigit() is False or
                   single_mesurement[3:4].isdigit() is False or
                   single_mesurement[6].isdigit() is False or
                   single_mesurement[8].isdigit() is False):
                    messages("milking")
                    return "failure"
                if(int(single_mesurement[0]) > 1 or
                   int(single_mesurement[0:1]) > 12):
                    messages("milking")
                    return "failure"
                if(single_mesurement[2] != '/' or
                   single_mesurement[5] != '-' or
                   single_mesurement[7] != '.'):
                    messages("milking")
                    return "failure"

    # check fat input
    if profile["GENDER"] == "male":
        pass
    else:
        if profile['FAT_CONTENT'] == '':
            pass
        else:
            all_mesurements = profile['FAT_CONTENT'].split('@')
            for single_mesurement in all_mesurements:
                if len(single_mesurement) != 9:
                    messages("milking")
                    return "failure"
                if(single_mesurement[0:1].isdigit() is False or
                   single_mesurement[3:4].isdigit() is False or
                   single_mesurement[6].isdigit() is False or
                   single_mesurement[8].isdigit() is False):
                    messages("milking")
                    return "failure"
                if(int(single_mesurement[0]) > 1 or
                   int(single_mesurement[0:1]) > 12):
                    messages("milking")
                    return "failure"
                if(single_mesurement[2] != '/' or
                   single_mesurement[5] != '-' or
                   single_mesurement[7] != '.'):
                    messages("milking")
                    return "failure"

    return "success"


def messages(message_type):
    """display message, different for each error"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("check_profiles_input")
    lang_dict = language_dict.widget_text_dictionary

    if message_type == "empty fields.":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
    elif message_type == "no gender":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox3"])
    elif message_type == "less than 30":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox5"])
    elif message_type == "capital":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox6"])
    elif message_type == "#":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox4"])
    elif message_type == "date":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox7"])
    elif message_type == "@":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox8"])
    elif message_type == "milking":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox9"])
    elif message_type == "success":
        messagebox.showinfo(lang_dict["messagebox"], lang_dict["messagebox10"])
