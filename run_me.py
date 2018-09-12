#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
main file of Goatebook program - tool writen to help keeping track of herd
on a small-goat-dairy farms
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import add_profiles_tab
import compare_profiles_tab
import charts_tab
import calendar_tab
import set_options
import view_edit_delete_profile


class Main(tk.Frame):

    """
    define main frame, define notebook, attach frames to notebook, send frame
    instances to menu functions
    """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Goatbook")
        self.master.geometry("770x770")
        self.master.grid()

        rows = 0
        while rows < 50:
            self.master.rowconfigure(rows, weight=1)
            self.master.columnconfigure(rows, weight=1)
            rows += 1

        notebook = ttk.Notebook(self.master)
        notebook.grid(
            row=0, column=0, columnspan=50, rowspan=49, sticky="NESW")

        language_dict = set_options.Options()
        language_dict.get_text_dict("run_me")
        lang_dict = language_dict.widget_text_dictionary

        profiles_frame = ttk.Frame(notebook)
        notebook.add(profiles_frame, text=lang_dict["profiles_frame"])

        charts_frame = ttk.Frame(notebook)
        notebook.add(charts_frame, text=lang_dict["charts_frame"])

        calendar_frame = ttk.Frame(notebook)
        notebook.add(calendar_frame, text=lang_dict["calendar_frame"])

        options_frame = ttk.Frame(notebook)
        notebook.add(options_frame, text=lang_dict["options_frame"])

        profiles_menu(profiles_frame, lang_dict)
        charts_menu(charts_frame, lang_dict)
        calendar(calendar_frame)
        options(options_frame, lang_dict)


def profiles_menu(profiles_frame, lang_dict):
    """add, edit, delete, view profiles"""
    # BUTTONS
    add_profile = tk.Button(
        profiles_frame, text=lang_dict["add_profile"], height=3,
        width=15, font="Helvetica 12",
        command=add_profiles_tab.AddProfile)
    add_profile.place(x=20, y=40)

    view_profiles = tk.Button(
        profiles_frame, text=lang_dict["view_profiles"], height=3,
        width=15, font="Helvetica 12",
        command=compare_profiles_tab.CompareProfiles)
    view_profiles.place(x=20, y=140)

    search_for_profile = tk.Button(
        profiles_frame, text=lang_dict["search_for_profile"], height=3,
        width=15, font="Helvetica 12",
        command=view_edit_delete_profile.ManipulateProfile)
    search_for_profile.place(x=20, y=240)

    # LABELS
    add_profile_label = tk.Label(
        profiles_frame, text=lang_dict["add_profile_label"],
        font="Helvetica 12")
    add_profile_label.place(x=200, y=60)

    view_profiles_label = tk.Label(
        profiles_frame, text=lang_dict["view_profiles_label"],
        font="Helvetica 12")
    view_profiles_label.place(x=200, y=160)

    search_for_profile_label = tk.Label(
        profiles_frame, font="Helvetica 12",
        text=lang_dict["search_for_profile_label"])
    search_for_profile_label.place(x=200, y=260)


def charts_menu(charts_frame, lang_dict):
    """three diferent chats showing: family tree, milking, age pyramid"""
    # BUTTONS
    family_tree = tk.Button(
        charts_frame, text=lang_dict["family_tree"], height=3, width=15,
        font="Helvetica 12", command=charts_tab.genealogy_tree)
    family_tree.place(x=20, y=40)

    milking = tk.Button(
        charts_frame, text=lang_dict["milking"], height=3, width=15,
        font="Helvetica 12", command=charts_tab.milking_chart)
    milking.place(x=20, y=140)

    age_pyramid = tk.Button(
        charts_frame, text=lang_dict["age_pyramid"], height=3, width=15,
        font="Helvetica 12", command=charts_tab.age_pyramid)
    age_pyramid.place(x=20, y=240)

    # LABELS
    fam_tree_label = tk.Label(
        charts_frame,
        text=lang_dict["fam_tree_label"],
        font="Helvetica 12")
    fam_tree_label.place(x=200, y=60)

    milking_label = tk.Label(
        charts_frame,
        text=lang_dict["milking_label"],
        font="Helvetica 12")
    milking_label.place(x=200, y=160)

    age_pyramid_label = tk.Label(
        charts_frame, font="Helvetica 12",
        text=lang_dict["age_pyramid_label"])
    age_pyramid_label.place(x=200, y=260)


def calendar(calendar_frame):
    """points to calendar module"""
    month_counter = 0  # curent month
    calendar_tab.Calendar(calendar_frame, month_counter)


def options(options_frame, lang_dict):
    """change language"""
    def change_language():
        if set_options.set_language(language_spinbox.get()) == "success":
            messagebox.showinfo(lang_dict["messagebox1"], lang_dict["messagebox2"])
    label_frame = tk.LabelFrame(
        options_frame, text=lang_dict["label_frame"],
        width=700, height=200, font="Helvetica 12")
    label_frame.place(x=20, y=20)

    languages_tuple = set_options.available_languages()

    language_spinbox = tk.Spinbox(
        label_frame, font="Helvetica 14", state="readonly",
        width=11, values=languages_tuple)
    language_spinbox.place(x=30, y=50)

    button = tk.Button(
        label_frame, text=lang_dict["button"], font="Helvetica 12",
        width=9, command=change_language)
    button.place(x=230, y=50)


def run():
    """pylint forced me to create this function"""
    root = tk.Tk()
    app = Main(root)
    root.mainloop()


run()
