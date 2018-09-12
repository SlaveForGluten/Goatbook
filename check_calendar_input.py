"""checks if events added to calendar are in format"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import messagebox

import process_calendar_data
import set_options


def pregnancy_event(date_dict, add_mum, add_dad):
    """check pregnancy event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("check_calendar_input")
    lang_dict = language_dict.widget_text_dictionary

    if add_mum.find('-') != -1 and add_dad.find('-') != -1:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
        return "error"
    if add_dad == "":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox3"])
        return "error"
    if add_mum == "":
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox4"])
        return "error"

    date_dict["Input1"] = add_mum
    date_dict["Input2"] = add_dad
    process_calendar_data.save_pregnancy(date_dict)
    return "success"


def medicine_event(date_dict, patient, medicine, dosing, withdrawal, note):
    """check medicine event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("check_calendar_input")
    lang_dict = language_dict.widget_text_dictionary

    if patient.find('-') != -1 and medicine.find('-') != -1:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
        return "error"
    if dosing.find('-') != -1 and withdrawal.find('-') != -1:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
        return "error"
    if note.find('-') != -1:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
        return "error"
    if patient == "" and medicine == "":
        messagebox.showinfo(
            lang_dict["messagebox1"], lang_dict["messagebox5"])
        return "error"
    if dosing == "":
        date_dict["Input3"] = 1
    else:
        if dosing.isdigit() is False:
            messagebox.showinfo(
                lang_dict["messagebox1"], lang_dict["messagebox6"])
            return "error"
        if int(dosing) < 0:
            messagebox.showinfo(
                lang_dict["messagebox1"],
                lang_dict["messagebox7"])
            return "error"
        if int(dosing) > 20:
            messagebox.showinfo(
                lang_dict["messagebox1"], lang_dict["messagebox8"])
            return "error"
    if withdrawal != "":
        if withdrawal.isdigit() is False:
            messagebox.showinfo(
                lang_dict["messagebox1"], lang_dict["messagebox9"])
            return "error"
        if int(withdrawal) < 0:
            messagebox.showinfo(
                lang_dict["messagebox1"],
                lang_dict["messagebox10"])
            return "error"
        if int(withdrawal) > 20:
            messagebox.showinfo(
                lang_dict["messagebox1"],
                lang_dict["messagebox11"])
            return "error"
    date_dict["Input1"] = patient
    date_dict["Input2"] = medicine
    if dosing == "":
        date_dict["Input3"] = 0
    else:
        date_dict["Input3"] = int(dosing)
    if withdrawal == "":
        date_dict["Input4"] = 0
    else:
        date_dict["Input4"] = int(withdrawal)
    date_dict["Input5"] = note
    process_calendar_data.save_medicine(date_dict)
    return "success"


def milking_event(date_dict, milking):
    """check milking event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("check_calendar_input")
    lang_dict = language_dict.widget_text_dictionary

    if milking == "":
        messagebox.showinfo(
            lang_dict["messagebox1"], lang_dict["messagebox12"])
        return "error"
    if milking.find('-') != -1:
        messagebox.showinfo(
            lang_dict["messagebox1"], lang_dict["messagebox13"])
        return "error"
    if milking.isdigit() is False:
        messagebox.showinfo(
            lang_dict["messagebox1"], lang_dict["messagebox14"])
        return "error"
    if 0 > int(milking) > 8000:
        messagebox.showinfo(
            lang_dict["messagebox1"], lang_dict["messagebox15"])
        return "error"
    date_dict['Input1'] = int(milking)
    process_calendar_data.save_milking(date_dict)
    return "success"


def other_event(date_dict, title, note):
    """check other event"""
    language_dict = set_options.Options()
    language_dict.get_text_dict("check_calendar_input")
    lang_dict = language_dict.widget_text_dictionary

    if title.find('-') != -1 and note.find('-') != -1:
        messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
        return "error"

    date_dict['Input1'] = title
    date_dict['Input2'] = note
    process_calendar_data.save_other(date_dict)
    return "success"
