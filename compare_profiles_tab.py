"""
takes all the profiles and allows to select which of them will be displayed
and sorts them depending on different criteria like age, gender etc.
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk

import sort_profiles
import process_profiles_data
import set_options


class CompareProfiles:
    """
    init creates all the basic widgets and 'populate_frame'  and
    'populate_scroled_frame' methods are reloaded each time you press 'Apply'
    button allowing you to display different profiles and profile properties
    '"""

    def __init__(self):
        def refresh():
            populate_frame(
                parameters_window, gender_var.get(), dob_var.get(),
                milking_var.get(), fat_var.get(), lang_dict)
            populate_scroled_frame(
                parameters_window, pick_prof_spinbox.get(),
                sort_prof_spinbox.get(), gender_var.get(), dob_var.get(),
                milking_var.get(), fat_var.get(), lang_dict)

        language_dict = set_options.Options()
        language_dict.get_text_dict("compare_profiles_tab")
        lang_dict = language_dict.widget_text_dictionary

        # NEW WINDOW
        parameters_window = tk.Toplevel(height=650, width=800)

        # LABELS
        show_prof_label = tk.Label(
            parameters_window, text=lang_dict["show_prof_label"],
            font="Helvetica 12")

        sort_by_label = tk.Label(
            parameters_window, text=lang_dict["sort_by_label"],
            font="Helvetica 12")
        # SPINBOXES
        pick_prof_tuple = (
            lang_dict["pick_prof_tuple1"], lang_dict["pick_prof_tuple2"],
            lang_dict["pick_prof_tuple3"], lang_dict["pick_prof_tuple4"],
            lang_dict["pick_prof_tuple5"])

        pick_prof_spinbox = tk.Spinbox(
            parameters_window, font="Helvetica 12", state="readonly",
            width=11, values=pick_prof_tuple)

        sort_prof_tuple = (
            lang_dict["sort_prof_tuple1"], lang_dict["sort_prof_tuple2"],
            lang_dict["sort_prof_tuple3"], lang_dict["sort_prof_tuple4"],
            lang_dict["sort_prof_tuple5"], lang_dict["sort_prof_tuple6"],
            lang_dict["sort_prof_tuple7"])

        sort_prof_spinbox = tk.Spinbox(
            parameters_window, font="Helvetica 12", state="readonly",
            width=11, values=sort_prof_tuple)

        # CHECK BOXES
        checkbox_label = tk.Label(
            parameters_window, text=lang_dict["checkbox_label"],
            font="Helvetica 12")

        gender_var = tk.StringVar()
        gender_checkbutton = tk.Checkbutton(
            parameters_window, text=lang_dict["gender_checkbutton"],
            font="Helvetica 12",
            variable=gender_var, onvalue="yes", offvalue="")

        dob_var = tk.StringVar()
        dob_checkbutton = tk.Checkbutton(
            parameters_window, text=lang_dict["dob_checkbutton"],
            font="Helvetica 12",
            variable=dob_var, onvalue="yes", offvalue="")

        milking_var = tk.StringVar()
        milking_checkbutton = tk.Checkbutton(
            parameters_window, text=lang_dict["milking_checkbutton"],
            font="Helvetica 12",
            variable=milking_var, onvalue="yes", offvalue="")

        fat_var = tk.StringVar()
        fat_content_checkbutton = tk.Checkbutton(
            parameters_window, text=lang_dict["fat_checkbutton"],
            font="Helvetica 12",
            variable=fat_var, onvalue="yes", offvalue="")

        # BUTTONS
        apply_button = tk.Button(
            parameters_window, text=lang_dict["apply_button"],
            font="Helvetica 12", height=2, width=7, command=refresh)

        close_button = tk.Button(
            parameters_window, text=lang_dict["close_button"],
            font="Helvetica 12", height=2, width=7,
            command=parameters_window.destroy)

        help_button = tk.Button(
            parameters_window, text=lang_dict["help_button"], height=1,
            width=3, font="Helvetica 12")

        # LAYOUT
        # labels
        show_prof_label.place(x=10, y=10)
        sort_by_label.place(x=150, y=10)
        # spinboxes
        pick_prof_spinbox.place(x=10, y=50)
        sort_prof_spinbox.place(x=150, y=50)
        # checkboxes
        checkbox_label.place(x=300, y=10)
        gender_checkbutton.place(x=300, y=30)
        dob_checkbutton.place(x=300, y=55)
        milking_checkbutton.place(x=450, y=30)
        fat_content_checkbutton.place(x=450, y=55)
        # buttons
        apply_button.place(x=600, y=30)
        close_button.place(x=710, y=590)
        help_button.place(x=550, y=607)

        # saveButton = tk.Button(
        #   parameters_window, text="Save to file",height=2,
        #   width=9, font="Helvetica 12")
        # saveButton.place(x=604, y=590)


def populate_frame(
        parameters_window, gender, date_of_birth, milking,
        fat_content, lang_dict):
    """
    Small frame above scrollable canvas. Created to display titles for
    values displayed underneath. Is refreshed after pressing 'Apply'.
    """
    title_frame = tk.Frame(
        parameters_window, height=30, width=800)
    title_frame.place(x=0, y=100)

    # place not optional Labels
    name_label = tk.Label(
        title_frame, font="Helvetica 12", text=lang_dict["name_label"])
    name_label.place(x=0, y=0)

    id_label = tk.Label(
        title_frame, font="Helvetica 12", text=lang_dict["id_label"])
    id_label.place(x=150, y=0)

    # place optional labels, adjust their position depending on how
    # many of them are displayed
    x_axis = 150
    if gender != '':
        gender_label = tk.Label(
            title_frame, font="Helvetica 12", text=lang_dict["gender_label"])
        gender_label.place(x=130 + x_axis, y=0)
        x_axis += 125

    if date_of_birth != "":
        dob_label = tk.Label(
            title_frame, font="Helvetica 12", text=lang_dict["dob_label"])
        dob_label.place(x=130 + x_axis, y=0)
        x_axis += 125

    if milking != "":
        milking_label = tk.Label(
            title_frame, font="Helvetica 12", text=lang_dict["milking_label"])
        milking_label.place(x=130 + x_axis, y=0)
        x_axis += 125

    if fat_content != "":
        fat_content_label = tk.Label(
            title_frame, font="Helvetica 12", text=lang_dict["fat_content_label"])
        fat_content_label.place(x=130 + x_axis, y=0)


def populate_scroled_frame(parameters_window, show, sort, gender,
                           date_of_birth, milking, fat_content, lang_dict):

    """
    populate scrolable 'on_canvas_frame' with values user chose to display
    """
    # get ALL profiles via process_profiles_data.py
    profiles = process_profiles_data.get_all_profiles()
    profiles = sort_profiles.clear_milking(profiles)
    profiles = sort_profiles.clear_fat_content(profiles)
    profiles = sort_profiles.clear_date_of_birth(profiles)
    sorted_profiles = sort_profiles.show(profiles, show, sort)

    # Reset the scroll region to encompass the inner frame
    def on_frame_configure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    # adjust scrollregion to fit all the profiles
    canvas_scrollregion = 40*len(profiles)

    # CANVAS
    canvas = tk.Canvas(
        parameters_window, width=780, height=450,
        scrollregion=(0, 0, 0, canvas_scrollregion))
    canvas.place(x=0, y=130)

    # SCROLLBAR
    vbar = tk.Scrollbar(
        parameters_window, orient=tk.VERTICAL, command=canvas.yview)
    vbar.place(x=780, y=130, height=450)
    canvas.config(yscrollcommand=vbar.set)

    # SCROLLABLE FRAME DISPLAYED ON CANVAS
    on_canvas_frame = tk.Frame(
        canvas, width=780, height=canvas_scrollregion)
    on_canvas_frame.place(x=0, y=0)

    # bind "on_canvas_frame" with "canvas" to make it scroll with canvas
    on_canvas_frame.bind("<Configure>", lambda event, canvas=canvas:
                         on_frame_configure(canvas))
    canvas.create_window((0, 0), window=on_canvas_frame, anchor="nw")

    # check what parameters shoud be displayed and place them on
    # "on_canvas_frame"adjust columns and rows with "x_axis" and "y_axis"
    x_axis = 0
    y_axis = 0

    for prof in sorted_profiles:
        # refine 'milking' and 'fat_content' input
        # (only last mesurment is ment to be displayed)
        if prof['GENDER'] == 'female':
            last_milking = prof['MILKING'].split('@')
            last_fat_c = prof['FAT_CONTENT'].split('@')

        name_value = tk.Label(
            on_canvas_frame, font="Helvetica 12", text=prof["NAME"])
        name_value.place(x=x_axis, y=y_axis)
        x_axis += 130
        id_value = tk.Label(
            on_canvas_frame, font="Helvetica 12",
            text=prof["ID_NUMBER"])
        id_value.place(x=x_axis, y=y_axis)
        x_axis += 170
        if gender != '':
            if prof["GENDER"] == 'female':
                short_gender = lang_dict["Fgender"]
            else:
                short_gender = lang_dict["Mgender"]
            gender_value = tk.Label(
                on_canvas_frame, font="Helvetica 12", text=short_gender)
            gender_value.place(x=x_axis, y=y_axis)
            x_axis += 125
        if date_of_birth != "":
            x_axis -= 20
            dob_value = tk.Label(
                on_canvas_frame, font="Helvetica 12",
                text=prof["DATE_OF_BIRTH"])
            dob_value.place(x=x_axis, y=y_axis)
            x_axis += 125
        if milking != '':
            if date_of_birth == '':
                x_axis -= 30
            if prof['GENDER'] == 'female':
                milk_value = tk.Label(
                    on_canvas_frame, font="Helvetica 12",
                    text=last_milking[len(last_milking)-1])
                milk_value.place(x=x_axis, y=y_axis)
                x_axis += 125
        if fat_content != '':
            if prof['GENDER'] == 'female':
                fat_value = tk.Label(
                    on_canvas_frame, font="Helvetica 12",
                    text=last_fat_c[len(last_fat_c)-1])
                fat_value.place(x=x_axis, y=y_axis)
                x_axis += 125
        y_axis += 40
        x_axis = 0
