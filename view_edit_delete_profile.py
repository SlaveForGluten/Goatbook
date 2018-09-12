""" from here you can view existing profile and edit or delete it"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import scrolledtext as sc
from tkinter import messagebox

import process_profiles_data
import set_options


class ManipulateProfile:
    """takes name OR ID number and shows profile details if profile exist"""
    def __init__(self):
        def get_profile():

            name_and_number = {
                "NAME": name_entry.get(),
                "ID_NUMBER": id_entry.get()
            }
            profile = process_profiles_data.get_single_profile(
                name_and_number)
            if profile != "error":
                ManipulateProfile().view_profile(profile)
                self.find_prof_frame.destroy()
            else:
                messagebox.showinfo(
                    self.dict["messagebox1"], self.dict["messagebox2"])

        language_dict = set_options.Options()
        language_dict.get_text_dict("view_edit_delete_profile")
        self.dict = language_dict.widget_text_dictionary

        # NEW FRAME
        self.find_prof_frame = tk.Frame()
        self.find_prof_frame.grid(
            row=0, column=0, columnspan=50, rowspan=50, sticky="NESW")

        # BUTTONS
        back_button = tk.Button(
            self.find_prof_frame, text=self.dict["back_button"], height=2,
            width=7, font="Helvetica 12", command=self.find_prof_frame.destroy)
        back_button.place(x=10, y=10)

        search_button = tk.Button(
            self.find_prof_frame, text=self.dict["search_button"], height=2,
            width=7, font="Helvetica 12", command=get_profile)
        search_button.place(x=100, y=10)

        # ENTRY
        name_entry = tk.Entry(
            self.find_prof_frame, width=30, font="Helvetica 12")
        name_entry.place(x=300, y=150)

        id_entry = tk.Entry(
            self.find_prof_frame, width=30, font="Helvetica 12")
        id_entry.place(x=300, y=190)

        # LABELS
        help_label = tk.Label(
            self.find_prof_frame,
            text=self.dict["help_label"],
            font="Helvetica 12")
        help_label.place(x=50, y=100)

        name_label = tk.Label(
            self.find_prof_frame, text=self.dict["name_label"],
            font="Helvetica 12")
        name_label.place(x=50, y=150)

        id_label = tk.Label(
            self.find_prof_frame, text=self.dict["id_label"],
            font="Helvetica 12")
        id_label.place(x=50, y=190)

    def view_profile(self, profile):
        """
        display single profile, from here you can edit or delete given profile
        """
        def delete():
            confirm = messagebox.askquestion(
                self.dict["confirm"], self.dict["confirm1"], icon='warning')
            if confirm == "yes":
                process_profiles_data.delete_profile(profile)
                view_prof_frame.destroy()

        def edit():
            view_prof_frame.destroy()
            self.find_prof_frame.destroy()
            ManipulateProfile().edit_profile(profile)

        # NEW FRAME
        view_prof_frame = tk.Frame()
        view_prof_frame.grid(
            row=0, column=0, columnspan=50, rowspan=50, sticky="NESW")

        # BUTTONS
        back_button = tk.Button(
            view_prof_frame, text=self.dict["back_button"], height=2, width=7,
            font="Helvetica 12", command=view_prof_frame.destroy)
        back_button.place(x=10, y=10)

        edit_button = tk.Button(
            view_prof_frame, text=self.dict["edit_button"], height=2,
            width=7, font="Helvetica 12", command=edit)
        edit_button.place(x=100, y=10)

        delete_button = tk.Button(
            view_prof_frame, text=self.dict["delete_button"],
            height=2, width=7, font="Helvetica 12", command=delete)
        delete_button.place(x=190, y=10)

        # DESCRIPTION LABELS (PRE SET)
        name_label = tk.Label(
            view_prof_frame, text=self.dict["name_label"], font="Helvetica 12")
        name_label.place(x=50, y=80)

        id_label = tk.Label(
            view_prof_frame, text=self.dict["id_label"], font="Helvetica 12")
        id_label.place(x=50, y=120)

        gender_label = tk.Label(
            view_prof_frame, text=self.dict["gender_label"],
            font="Helvetica 12")
        gender_label.place(x=50, y=160)

        dob_label = tk.Label(
            view_prof_frame, text=self.dict["dob_label"],
            font="Helvetica 12")
        dob_label.place(x=50, y=200)

        dod_label = tk.Label(
            view_prof_frame, text=self.dict["dod_label"],
            font="Helvetica 12")
        dod_label.place(x=50, y=240)

        mother_label = tk.Label(
            view_prof_frame, text=self.dict["mother_label"],
            font="Helvetica 12")
        mother_label.place(x=50, y=280)

        father_label = tk.Label(
            view_prof_frame, text=self.dict["father_label"],
            font="Helvetica 12")
        father_label.place(x=50, y=320)

        # INPUT LABELS (INPUT DEPENDENT)
        curent_name_label = tk.Label(
            view_prof_frame, text=profile["NAME"], font="Helvetica 12")
        curent_name_label.place(x=200, y=80)

        curent_id_label = tk.Label(
            view_prof_frame, text=profile["ID_NUMBER"],
            font="Helvetica 12")
        curent_id_label.place(x=200, y=120)

        if profile["GENDER"] == "male":
            curent_male_label = tk.Label(
                view_prof_frame, text=self.dict["curent_male_label"],
                font="Helvetica 12")
            curent_male_label.place(x=200, y=160)
        else:
            curent_female_label = tk.Label(
                view_prof_frame, text=self.dict["curent_female_label"],
                font="Helvetica 12")
            curent_female_label.place(x=200, y=160)

        curent_dob_label = tk.Label(
            view_prof_frame, text=profile["DATE_OF_BIRTH"],
            font="Helvetica 12")
        curent_dob_label.place(x=200, y=200)

        curent_dod_label = tk.Label(
            view_prof_frame, text=profile["DATE_OF_DEATH"],
            font="Helvetica 12")
        curent_dod_label.place(x=200, y=240)

        curent_mother_label = tk.Label(
            view_prof_frame, text=profile["MOTHER"],
            font="Helvetica 12")
        curent_mother_label.place(x=200, y=280)

        curent_father_label = tk.Label(
            view_prof_frame, text=profile["FATHER"],
            font="Helvetica 12")
        curent_father_label.place(x=200, y=320)

        # BUTTONS FOR ACCESING PROFILE DETAILS
        def chara_func():
            chara_button.config(relief=tk.SUNKEN)
            disease_button.config(relief=tk.RAISED)
            sold_button.config(relief=tk.RAISED)
            bought_button.config(relief=tk.RAISED)
            milking_button.config(relief=tk.RAISED)
            fat_content_button.config(relief=tk.RAISED)
            label_func("\n".join(profile["CHARACTERISTICS"].split("@")))

        def disease_func():
            disease_button.config(relief=tk.SUNKEN)
            chara_button.config(relief=tk.RAISED)
            sold_button.config(relief=tk.RAISED)
            bought_button.config(relief=tk.RAISED)
            milking_button.config(relief=tk.RAISED)
            fat_content_button.config(relief=tk.RAISED)
            label_func("\n".join(profile["HISTORY_OF_DISEASE"].split("@")))

        def sold_func():
            sold_button.config(relief=tk.SUNKEN)
            disease_button.config(relief=tk.RAISED)
            chara_button.config(relief=tk.RAISED)
            bought_button.config(relief=tk.RAISED)
            milking_button.config(relief=tk.RAISED)
            fat_content_button.config(relief=tk.RAISED)
            label_func("\n".join(profile["SOLD_INFO"].split("@")))

        def bought_func():
            bought_button.config(relief=tk.SUNKEN)
            disease_button.config(relief=tk.RAISED)
            sold_button.config(relief=tk.RAISED)
            chara_button.config(relief=tk.RAISED)
            milking_button.config(relief=tk.RAISED)
            fat_content_button.config(relief=tk.RAISED)
            label_func("\n".join(profile["BOUGHT_INFO"].split("@")))

        def milking_func():
            milking_button.config(relief=tk.SUNKEN)
            disease_button.config(relief=tk.RAISED)
            chara_button.config(relief=tk.RAISED)
            sold_button.config(relief=tk.RAISED)
            bought_button.config(relief=tk.RAISED)
            fat_content_button.config(relief=tk.RAISED)
            if profile["GENDER"] == "female":
                label_func("\n".join(profile["MILKING"].split("@")))

        def fat_content_func():
            fat_content_button.config(relief=tk.SUNKEN)
            chara_button.config(relief=tk.RAISED)
            disease_button.config(relief=tk.RAISED)
            sold_button.config(relief=tk.RAISED)
            bought_button.config(relief=tk.RAISED)
            milking_button.config(relief=tk.RAISED)
            if profile["GENDER"] == "female":
                label_func("\n".join(profile["FAT_CONTENT"].split("@")))

        def label_func(txt):
            info_label = tk.Label(
                view_prof_frame, text=txt, wraplength=750,
                font="Helvetica 12", height=20, width=83, anchor="nw",
                justify=tk.LEFT)
            info_label.place(x=10, y=400)

        chara_button = tk.Button(
            view_prof_frame, text=self.dict["chara_button"],
            command=chara_func, height=1, width=7, font="Helvetica 10")
        chara_button.place(x=100, y=360)

        disease_button = tk.Button(
            view_prof_frame, text=self.dict["disease_button"],
            command=disease_func, height=1, width=7, font="Helvetica 10")
        disease_button.place(x=200, y=360)

        sold_button = tk.Button(
            view_prof_frame, text=self.dict["sold_button"], command=sold_func,
            height=1, width=7, font="Helvetica 10")
        sold_button.place(x=300, y=360)

        bought_button = tk.Button(
            view_prof_frame, text=self.dict["bought_button"],
            command=bought_func, height=1, width=7, font="Helvetica 10")
        bought_button.place(x=400, y=360)

        milking_button = tk.Button(
            view_prof_frame, text=self.dict["milking_button"],
            command=milking_func, height=1, width=7, font="Helvetica 10")
        milking_button.place(x=500, y=360)

        fat_content_button = tk.Button(
            view_prof_frame, text=self.dict["fat_content_button"],
            command=fat_content_func, height=1, width=9, font="Helvetica 10")
        fat_content_button.place(x=600, y=360)

    def edit_profile(self, profile):
        """
        display existing profile on the widgets, take changed profile
        parameters, send them to replace old profile with updated one
        """
        old_name_and_id = {
            "NAME": profile["NAME"],
            "ID_NUMBER": profile["ID_NUMBER"]
        }

        def next_page():
            def save_female_profile():
                profile_after_edit = {
                    "NAME": name_entry.get(),
                    "GENDER": gender_var.get(),
                    "DATE_OF_BIRTH": dob_entry.get(),
                    "DATE_OF_DEATH": dod_entry.get(),
                    "ID_NUMBER": id_entry.get(),
                    "MOTHER": mother_entry.get(),
                    "FATHER": father_entry.get(),
                    "CHARACTERISTICS": chara_sc.get("1.0", "end-1c"),
                    "HISTORY_OF_DISEASE": disease_sc.get("1.0", "end-1c"),
                    "SOLD": sold_var.get(),
                    "SOLD_INFO": sold_info_sc.get("1.0", "end-1c"),
                    "BOUGHT": bought_var.get(),
                    "BOUGHT_INFO": bought_info_sc.get("1.0", "end-1c"),
                }
                # if no old mesurement(s), get the new one
                if profile["MILKING"] == "":
                    profile_after_edit["MILKING"] = milk_entry.get()
                else:
                    all_milking_mesurments = profile["MILKING"].split("@")
                    all_milking_mesurments.remove(
                        all_milking_mesurments[len(all_milking_mesurments)-1])
                    if previous_milking_entry.get() != "":
                        all_milking_mesurments.append(
                            previous_milking_entry.get())
                    if milk_entry.get() != "":
                        all_milking_mesurments.append(milk_entry.get())
                    profile_after_edit['MILKING'] = '@'.join(
                        all_milking_mesurments)

                # if no old mesurement(s), get the new one
                if profile['FAT_CONTENT'] == '':
                    profile_after_edit['FAT_CONTENT'] = fat_content_entry.get()
                else:
                    all_fc_mesurments = profile['FAT_CONTENT'].split('@')
                    all_fc_mesurments.remove(
                        all_fc_mesurments[len(all_fc_mesurments)-1])
                    if last_fc_entry.get() != "":
                        all_fc_mesurments.append(last_fc_entry.get())
                    if fat_content_entry.get() != "":
                        all_fc_mesurments.append(fat_content_entry.get())
                    profile_after_edit['FAT_CONTENT'] = '@'.join(
                        all_fc_mesurments)
                process_profiles_data.edit_profile(
                    old_name_and_id, profile_after_edit)
                edit_profile_frame.destroy()

            # NEXT PAGE FRAME
            next_page_frame = tk.Frame(
                edit_profile_frame, height=770, width=770)
            next_page_frame.place(x=0, y=0)

            # BUTTONS
            previous_page_button = tk.Button(
                next_page_frame, text=self.dict["previous_page_button"],
                command=next_page_frame.destroy, height=2,
                width=13, font="Helvetica 12")
            previous_page_button.place(x=10, y=10)

            save_button = tk.Button(
                next_page_frame, text=self.dict["save_button"], height=2,
                width=11, font="Helvetica 12", command=save_female_profile)
            save_button.place(x=155, y=10)

            help_button = tk.Button(
                next_page_frame, text="?", height=2, width=3,
                font="Helvetica 12")
            help_button.place(x=280, y=10)

            # LABELS
            milk_label = tk.Label(
                next_page_frame, text=self.dict["milk_label"],
                font="Helvetica 12")
            milk_label.place(x=50, y=120)

            milk_help_label = tk.Label(
                next_page_frame, text=self.dict["milk_help_label"],
                font="Helvetica 12")
            milk_help_label.place(x=200, y=90)

            milk_example_label = tk.Label(
                next_page_frame, text=self.dict["milk_example_label"],
                font="Helvetica 12")
            milk_example_label.place(x=330, y=120)

            fat_content_label = tk.Label(
                next_page_frame, text=self.dict["fat_content_label"],
                font="Helvetica 12")
            fat_content_label.place(x=50, y=260)

            fat_content_help_label = tk.Label(
                next_page_frame, text=self.dict["fat_content_help_label"],
                font="Helvetica 12")
            fat_content_help_label.place(x=200, y=230)

            fat_content_example_label = tk.Label(
                next_page_frame, text=self.dict["fat_content_example_label"],
                font="Helvetica 12")
            fat_content_example_label.place(x=330, y=260)

            # ENTRY
            # new mesurments entry
            milk_entry = tk.Entry(
                next_page_frame, width=8, font="Helvetica 12")
            milk_entry.place(x=200, y=120)

            fat_content_entry = tk.Entry(
                next_page_frame, width=8, font="Helvetica 12")
            fat_content_entry.place(x=200, y=260)

            if profile["MILKING"] == "":
                pass
            if profile["MILKING"] != "" and len(profile["MILKING"]) == 9:
                last_milk_mesurement = profile["MILKING"]
            if profile["MILKING"] != "" and len(profile["MILKING"]) > 9:
                last_milk_mesurement = profile["MILKING"].split("@")[
                    len(profile["MILKING"].split("@"))-1]

            # turn on the widget if there was a mesurment before
            if profile["MILKING"] != "":
                previous_milking_entry = tk.Entry(
                    next_page_frame, width=8, font="Helvetica 12")
                previous_milking_entry.place(x=500, y=120)
                previous_milking_entry.insert(0, last_milk_mesurement)

            # previous fat content mesurement
            last_fc_mesurement = ""
            if profile["FAT_CONTENT"] == "":
                pass
            if(profile["FAT_CONTENT"] != "" and
               len(profile["FAT_CONTENT"]) == 9):
                last_fc_mesurement = profile["FAT_CONTENT"]
            if(profile["FAT_CONTENT"] != "" and
               len(profile["FAT_CONTENT"]) > 9):
                last_fc_mesurement = profile["FAT_CONTENT"].split("@")[
                    len(profile["FAT_CONTENT"].split("@"))-1]

            # turn on the widget if there was a mesurment before
            if profile["FAT_CONTENT"] != "":
                last_fc_entry = tk.Entry(
                    next_page_frame, width=8, font="Helvetica 12")
                last_fc_entry.place(x=500, y=260)
                last_fc_entry.insert(0, last_fc_mesurement)

        def save_male_profile():
            profile_after_edit = {
                "NAME": name_entry.get(),
                "GENDER": gender_var.get(),
                "DATE_OF_BIRTH": dob_entry.get(),
                "DATE_OF_DEATH": dod_entry.get(),
                "ID_NUMBER": id_entry.get(),
                "MOTHER": mother_entry.get(),
                "FATHER": father_entry.get(),
                "CHARACTERISTICS": chara_sc.get("1.0", "end-1c"),
                "HISTORY_OF_DISEASE": disease_sc.get("1.0", "end-1c"),
                "SOLD": sold_var.get(),
                "SOLD_INFO": sold_info_sc.get("1.0", "end-1c"),
                "BOUGHT": bought_var.get(),
                "BOUGHT_INFO": bought_info_sc.get("1.0", "end-1c"),
                "MILKING": profile["MILKING"],
                "FAT_CONTENT": profile["FAT_CONTENT"]
            }

            process_profiles_data.edit_profile(
                old_name_and_id, profile_after_edit)
            edit_profile_frame.destroy()

        # NEW FRAME
        edit_profile_frame = tk.Frame()
        edit_profile_frame.grid(
            row=0, column=0, columnspan=50, rowspan=50, sticky="NESW")

        # BUTTONS
        back_button = tk.Button(
            edit_profile_frame, text=self.dict["back_button"],
            command=edit_profile_frame.destroy,
            height=2, width=7, font="Helvetica 12")
        back_button.place(x=10, y=10)

        help_button = tk.Button(
            edit_profile_frame, text="?",
            height=2, width=3, font="Helvetica 12")

        save_changes_button = tk.Button(
            edit_profile_frame, text=self.dict["save_button"], height=2,
            width=12, font="Helvetica 12", command=save_male_profile)

        next_page_button = tk.Button(
            edit_profile_frame, text=self.dict["next_page_button"],
            command=next_page, height=2, width=10, font="Helvetica 12")

        # display diferent buttons depending on displayed profile"s
        # gender (no need to mesure milking for bucks)
        if profile['GENDER'] == 'male':
            save_changes_button.place(x=100, y=10)
            help_button.place(x=235, y=10)
        else:
            help_button.place(x=100, y=10)
            next_page_button.place(x=155, y=10)

        # LABELS
        name_label = tk.Label(
            edit_profile_frame, text=self.dict["name_label"],
            font="Helvetica 12")
        name_label.place(x=50, y=80)

        id_label = tk.Label(
            edit_profile_frame, text=self.dict["id_label"],
            font="Helvetica 12")
        id_label.place(x=50, y=120)

        gender_label = tk.Label(
            edit_profile_frame, text=self.dict["gender_label"],
            font="Helvetica 12")
        gender_label.place(x=50, y=160)

        dob_label = tk.Label(
            edit_profile_frame, text=self.dict["dob_label"],
            font="Helvetica 12")
        dob_label.place(x=50, y=200)

        dod_label = tk.Label(
            edit_profile_frame, text=self.dict["dod_label"],
            font="Helvetica 12")
        dod_label.place(x=50, y=240)

        mother_label = tk.Label(
            edit_profile_frame, text=self.dict["mother_label"],
            font="Helvetica 12")
        mother_label.place(x=50, y=280)

        father_label = tk.Label(
            edit_profile_frame, text=self.dict["father_label"],
            font="Helvetica 12")
        father_label.place(x=50, y=320)

        chara_label = tk.Label(
            edit_profile_frame, text=self.dict["chara_label"],
            font="Helvetica 12")
        chara_label.place(x=50, y=360)

        disease_label = tk.Label(
            edit_profile_frame, text=self.dict["disease_label"],
            font="Helvetica 12")
        disease_label.place(x=50, y=455)

        sold_label = tk.Label(
            edit_profile_frame, text=self.dict["sold_button"],
            font="Helvetica 12")
        sold_label.place(x=50, y=550)

        sold_info_label = tk.Label(
            edit_profile_frame, text=self.dict["sold_info_label"],
            font="Helvetica 12")
        sold_info_label.place(x=50, y=590)

        bought_label = tk.Label(
            edit_profile_frame, text=self.dict["bought_label"],
            font="Helvetica 12")
        bought_label.place(x=50, y=650)

        bought_info_label = tk.Label(
            edit_profile_frame, text=self.dict["sold_info_label"],
            font="Helvetica 12")
        bought_info_label.place(x=50, y=690)

        # ENTRY
        name_entry = tk.Entry(
            edit_profile_frame, width=30,
            font="Helvetica 12")
        name_entry.place(x=200, y=80)
        name_entry.insert(0, profile["NAME"])

        id_entry = tk.Entry(edit_profile_frame, width=30, font="Helvetica 12")
        id_entry.place(x=200, y=120)
        id_entry.insert(0, profile["ID_NUMBER"])

        dob_entry = tk.Entry(
            edit_profile_frame, width=30, font="Helvetica 12")
        dob_entry.place(x=200, y=200)
        dob_entry.insert(0, profile["DATE_OF_BIRTH"])

        dod_entry = tk.Entry(
            edit_profile_frame, width=30, font="Helvetica 12")
        dod_entry.place(x=200, y=240)
        dod_entry.insert(0, profile["DATE_OF_DEATH"])

        mother_entry = tk.Entry(
            edit_profile_frame, width=30, font="Helvetica 12")
        mother_entry.place(x=200, y=280)
        mother_entry.insert(0, profile["MOTHER"])

        father_entry = tk.Entry(
            edit_profile_frame, width=30, font="Helvetica 12")
        father_entry.place(x=200, y=320)
        father_entry.insert(0, profile["FATHER"])

        # SCROLLEDTEXT
        chara_sc = sc.ScrolledText(
            edit_profile_frame, width=50, height=4, font="Helvetica 12")
        chara_sc.place(x=200, y=360)
        chara_sc.insert(
            tk.INSERT, "\n".join(profile["CHARACTERISTICS"].split("@")))

        disease_sc = sc.ScrolledText(
            edit_profile_frame, width=50, height=4, font="Helvetica 12")
        disease_sc.place(x=200, y=455)
        disease_sc.insert(
            tk.INSERT, "\n".join(profile["HISTORY_OF_DISEASE"].split("@")))

        sold_info_sc = sc.ScrolledText(
            edit_profile_frame, width=50, height=2, font="Helvetica 12")
        sold_info_sc.place(x=200, y=590)
        sold_info_sc.insert(
            tk.INSERT, "\n".join(profile["SOLD_INFO"].split("@")))

        bought_info_sc = sc.ScrolledText(
            edit_profile_frame, width=50, height=2, font="Helvetica 12")
        bought_info_sc.place(x=200, y=690)
        bought_info_sc.insert(
            tk.INSERT, "\n".join(profile["BOUGHT_INFO"].split("@")))

        # RADIOBUTTONS
        # use radiobuttons to activate or deactivate some of the ScrolledText
        def sold():
            sold_info_sc.configure(state=tk.NORMAL)

        def not_sold():
            sold_info_sc.configure(state=tk.DISABLED)

        def bought():
            bought_info_sc.configure(state=tk.NORMAL)

        def not_bought():
            bought_info_sc.configure(state=tk.DISABLED)

        gender_var = tk.StringVar()
        if profile["GENDER"] == "male":
            gender_var.set("male")
        else:
            gender_var.set("female")

        male_radiobutton = tk.Radiobutton(
            edit_profile_frame, text=self.dict["curent_male_label"],
            variable=gender_var, value="male", font="Helvetica 12")
        male_radiobutton.place(x=200, y=160)

        female_radiobutton = tk.Radiobutton(
            edit_profile_frame, text=self.dict["curent_female_label"],
            variable=gender_var, value="female", font="Helvetica 12")
        female_radiobutton.place(x=300, y=160)

        sold_var = tk.StringVar()
        sold_radiobutton = tk.Radiobutton(
            edit_profile_frame, text=self.dict["sold_radiobutton"],
            variable=sold_var, value="sold", font="Helvetica 12", command=sold)
        sold_radiobutton.place(x=200, y=550)

        not_sold_radiobutton = tk.Radiobutton(
            edit_profile_frame, text=self.dict["not_sold_radiobutton"],
            variable=sold_var, value="notSold", font="Helvetica 12",
            command=not_sold)
        not_sold_radiobutton.place(x=300, y=550)

        # select or deselect radiobutton depending on saved data,
        # activate or deactivate ScrolledText(transaction details)
        if profile["SOLD"] == "sold":
            sold_radiobutton.select()
            not_sold_radiobutton.deselect()
            sold()
        else:
            sold_radiobutton.deselect()
            not_sold_radiobutton.select()
            not_sold()

        bought_var = tk.StringVar()
        bought_radiobutton = tk.Radiobutton(
            edit_profile_frame, text=self.dict["sold_radiobutton"],
            variable=bought_var, value="bought",
            font="Helvetica 12", command=bought)
        bought_radiobutton.place(x=200, y=650)

        not_bought_radiobutton = tk.Radiobutton(
            edit_profile_frame, text=self.dict["not_sold_radiobutton"],
            variable=bought_var, value="notBought",
            font="Helvetica 12", command=not_bought)
        not_bought_radiobutton.place(x=300, y=650)

        if profile["BOUGHT"] == "bought":
            bought_radiobutton.select()
            not_bought_radiobutton.deselect()
            bought()
        else:
            bought_radiobutton.deselect()
            not_bought_radiobutton.select()
            not_bought()
