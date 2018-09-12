#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
create all the widgets needed to take input for creating new profile,
pass the input for further processing
"""
import tkinter as tk
from tkinter import scrolledtext as sc

import set_options
import process_profiles_data
# import sort_profiles


class AddProfile:
    """
    Colect input from addProfileWindow() and send it to save in the file
    """
    def __init__(self):
        """
        create frame visible to all methods call methods containing
        widgets
        """
        add_prof_frame = tk.Frame()
        add_prof_frame.grid(
            row=0, column=0, columnspan=50,
            rowspan=50, sticky="NESW")

        language_dict = set_options.Options()
        language_dict.get_text_dict("add_profiles_tab")
        lang_dict = language_dict.widget_text_dictionary

        # BUTTONS
        back_button = tk.Button(
            add_prof_frame, text=lang_dict["back_button"], height=2, width=7,
            font="Helvetica 12", command=add_prof_frame.destroy)

        def save():

            profile_dict = {
                "NAME": name_entry.get(),
                "GENDER": gender_var.get(),
                "DATE_OF_BIRTH": dob_entry.get(),
                "DATE_OF_DEATH": dod_entry.get(),
                "ID_NUMBER": id_entry.get(),
                "MOTHER": mother_entry.get(),
                "FATHER": father_entry.get(),
                "CHARACTERISTICS": chara_scrolled.get("1.0", "end-1c"),
                "HISTORY_OF_DISEASE": disease_scrolled.get("1.0", "end-1c"),
                "SOLD": sold_var.get(),
                "SOLD_INFO": sold_info_scrolled.get("1.0", "end-1c"),
                "BOUGHT": bought_var.get(),
                "BOUGHT_INFO": bought_info_scrolled.get("1.0", "end-1c"),
                "MILKING": "",
                "FAT_CONTENT": ""
            }

            if process_profiles_data.save_profile(profile_dict) == "success":
                add_prof_frame.destroy()

        save_button = tk.Button(
            add_prof_frame, text=lang_dict["save_button"], height=2, width=7,
            font="Helvetica 12", command=save)

        help_button = tk.Button(
            add_prof_frame, text=lang_dict["help_button"], height=1, width=3,
            font="Helvetica 12")

        # BUTTONS LAYOUT
        back_button.place(x=10, y=10)
        save_button.place(x=100, y=10)
        help_button.place(x=190, y=27)

        # LABELS
        name_label = tk.Label(
            add_prof_frame, text=lang_dict["name_label"], font="Helvetica 12")

        id_label = tk.Label(
            add_prof_frame, text=lang_dict["id_label"], font="Helvetica 12")

        gender_label = tk.Label(
            add_prof_frame, text=lang_dict["gender_label"],
            font="Helvetica 12")

        dob_label = tk.Label(
            add_prof_frame, text=lang_dict["dob_label"], font="Helvetica 12")

        dod_label = tk.Label(
            add_prof_frame, text=lang_dict["dod_label"], font="Helvetica 12")

        mother_label = tk.Label(
            add_prof_frame, text=lang_dict["mother_label"],
            font="Helvetica 12")

        father_label = tk.Label(
            add_prof_frame, text=lang_dict["father_label"],
            font="Helvetica 12")

        chara_label = tk.Label(
            add_prof_frame, text=lang_dict["chara_label"], font="Helvetica 12")

        disease_label = tk.Label(
            add_prof_frame, text=lang_dict["disease_label"],
            font="Helvetica 12")

        sold_label = tk.Label(
            add_prof_frame, text=lang_dict["sold_label"], font="Helvetica 12")

        sold_info_label = tk.Label(
            add_prof_frame, text=lang_dict["sold_info_label"],
            font="Helvetica 12")

        bought_label = tk.Label(
            add_prof_frame, text=lang_dict["bought_label"],
            font="Helvetica 12")

        bought_info_label = tk.Label(
            add_prof_frame, text=lang_dict["bought_info_label"],
            font="Helvetica 12")

        # lABELS LAYOUT
        name_label.place(x=50, y=80)
        id_label.place(x=50, y=120)
        gender_label.place(x=50, y=160)
        dob_label.place(x=50, y=200)
        dod_label.place(x=50, y=240)
        mother_label.place(x=50, y=280)
        father_label.place(x=50, y=320)
        chara_label.place(x=50, y=360)
        disease_label.place(x=50, y=455)
        sold_label.place(x=50, y=550)
        sold_info_label.place(x=50, y=590)
        bought_label.place(x=50, y=650)
        bought_info_label.place(x=50, y=690)

        # ENTRIES
        # insert clue about inputed data format and
        # then make it disapear after clicking on entry
        def name_reset(*args):
            if name_entry.get() == lang_dict["name_entry"]:
                name_entry.delete(0, tk.END)
        name_entry = tk.Entry(
            add_prof_frame, width=30, font="Helvetica 12")
        name_entry.insert(0, lang_dict["name_entry"])
        name_entry.bind("<Button-1>", name_reset)

        id_entry = tk.Entry(
            add_prof_frame, width=30, font="Helvetica 12")

        def dob_reset(*args):
            if dob_entry.get() == lang_dict["dob_entry"]:
                dob_entry.delete(0, tk.END)
        dob_entry = tk.Entry(
            add_prof_frame, width=30, font="Helvetica 12")
        dob_entry.insert(0, lang_dict["dob_entry"])
        dob_entry.bind("<Button-1>", dob_reset)

        def dod_reset(*args):
            if dod_entry.get() == lang_dict["dod_entry"]:
                dod_entry.delete(0, tk.END)
        dod_entry = tk.Entry(
            add_prof_frame, width=30, font="Helvetica 12")
        dod_entry.insert(0, lang_dict["dod_entry"])
        dod_entry.bind("<Button-1>", dod_reset)

        def mum_reset(*args):
            if mother_entry.get() == lang_dict["mother_entry"]:
                mother_entry.delete(0, tk.END)
        mother_entry = tk.Entry(
            add_prof_frame, width=30, font="Helvetica 12")
        mother_entry.insert(0, lang_dict["mother_entry"])
        mother_entry.bind("<Button-1>", mum_reset)

        def dad_reset(*args):
            if father_entry.get() == lang_dict["father_entry"]:
                father_entry.delete(0, tk.END)
        father_entry = tk.Entry(
            add_prof_frame, width=30, font="Helvetica 12")
        father_entry.insert(0, lang_dict["father_entry"])
        father_entry.bind("<Button-1>", dad_reset)

        # ENTRIES LAYOUT
        name_entry.place(x=200, y=80)
        id_entry.place(x=200, y=120)
        dob_entry.place(x=200, y=200)
        dod_entry.place(x=200, y=240)
        mother_entry.place(x=200, y=280)
        father_entry.place(x=200, y=320)

        # RADIOBUTTONS
        # use radiobuttons to activate or deactivate
        # some of the ScrolledText widgets
        def sold():
            sold_info_scrolled.configure(state=tk.NORMAL)

        def not_sold():
            sold_info_scrolled.configure(state=tk.DISABLED)

        def bought():
            bought_info_scrolled.configure(state=tk.NORMAL)

        def not_bought():
            bought_info_scrolled.configure(state=tk.DISABLED)

        # set "not_sold", "not_bought",and "female" gender as default
        gender_var = tk.StringVar()

        male_radiobutton = tk.Radiobutton(
            add_prof_frame, text=lang_dict["male_radiobutton"],
            variable=gender_var, value="male", font="Helvetica 12")
        male_radiobutton.deselect()

        female_radiobutton = tk.Radiobutton(
            add_prof_frame, text=lang_dict["female_radiobutton"],
            variable=gender_var, value="female", font="Helvetica 12")
        female_radiobutton.select()

        sold_var = tk.StringVar()

        sold_radiobutton = tk.Radiobutton(
            add_prof_frame, text=lang_dict["sold_radiobutton"],
            variable=sold_var, value="sold", font="Helvetica 12", command=sold)
        sold_radiobutton.deselect()

        not_sold_radiobutton = tk.Radiobutton(
            add_prof_frame, text=lang_dict["not_sold_radiobutton"],
            variable=sold_var, value="not_sold", font="Helvetica 12",
            command=not_sold)
        not_sold_radiobutton.select()

        bought_var = tk.StringVar()

        bought_radiobutton = tk.Radiobutton(
            add_prof_frame, text=lang_dict["bought_radiobutton"],
            variable=bought_var, value="bought", font="Helvetica 12",
            command=bought)
        bought_radiobutton.deselect()

        not_bought_radiobutton = tk.Radiobutton(
            add_prof_frame, text=lang_dict["not_bought_radiobutton"],
            variable=bought_var, value="not_bought", font="Helvetica 12",
            command=not_bought)
        not_bought_radiobutton.select()

        # RADIOBUTTONS LAYOUT
        male_radiobutton.place(x=200, y=160)
        female_radiobutton.place(x=300, y=160)
        sold_radiobutton.place(x=200, y=550)
        not_sold_radiobutton.place(x=300, y=550)
        bought_radiobutton.place(x=200, y=650)
        not_bought_radiobutton.place(x=300, y=650)

        # SCROLLEDTEXT
        # "sold_info_scrolled" and "bought_info_scrolled" disabled by
        # default, you can activate and deactivate them with radiobuttons
        chara_scrolled = sc.ScrolledText(
            add_prof_frame, width=60, height=4, font="Helvetica 12")

        disease_scrolled = sc.ScrolledText(
            add_prof_frame, width=60, height=4, font="Helvetica 12")

        sold_info_scrolled = sc.ScrolledText(
            add_prof_frame, width=60, height=2, font="Helvetica 12")

        bought_info_scrolled = sc.ScrolledText(
            add_prof_frame, width=60, height=2, font="Helvetica 12")

        bought_info_scrolled.configure(state=tk.DISABLED)
        sold_info_scrolled.configure(state=tk.DISABLED)
        # SCROLLEDTEXT LAYOUT
        chara_scrolled.place(x=200, y=360)
        disease_scrolled.place(x=200, y=455)
        sold_info_scrolled.place(x=200, y=590)
        bought_info_scrolled.place(x=200, y=690)
