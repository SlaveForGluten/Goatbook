"""create three diferent charts using tkinter to display user input"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

import process_profiles_data
import get_date
import process_calendar_data
import sort_profiles
import set_options


def genealogy_tree():
    """
    create genealogy tree that display mother-goats
    and their kids as branches

    """
    tree_window = tk.Toplevel(height=700, width=600)
    tree_window.geometry("500x600")
    rows = 0
    while rows < 50:
        tree_window.rowconfigure(rows, weight=1)
        tree_window.columnconfigure(rows, weight=1)
        rows += 1

    # take goats with no mums
    first_moms = process_profiles_data.find_daughter("")

    # display goats with no mums on the tree
    tree = ttk.Treeview(tree_window)
    tree.grid(row=0, column=0, columnspan=50, rowspan=50, sticky="NESW")
    for counter, profile in enumerate(first_moms, 0):
        name = ""
        if profile["DATE_OF_DEATH"] == "":
            name = profile["NAME"] + " " + profile["ID_NUMBER"]
        else:
            name = "[*] " + profile["NAME"] + " " + profile["ID_NUMBER"]
        tagg = ""
        if profile["GENDER"] == "male":
            tagg = ("male")
        else:
            tagg = ("female")
        tree.insert("", counter, profile, text=name, tag=tagg)

    # display kids of first moms then look for kids of those kids, display
    # them and so on
    while first_moms:
        for parent in first_moms:
            kids = list()
            if parent["NAME"] != "":
                kids = process_profiles_data.find_daughter(parent["NAME"])
            else:
                process_profiles_data.find_daughter(parent["ID_NUMBER"])
            first_moms.remove(parent)
            if kids != "":
                for counter, kid in enumerate(kids, 0):
                    first_moms.append(kid)
                    name = ""
                    if kid["DATE_OF_DEATH"] == "":
                        name = kid["NAME"] + " " + kid["ID_NUMBER"]
                    else:
                        name = "[*] " + kid["NAME"] + " " + kid["ID_NUMBER"]
                    tagg = ""
                    if kid["GENDER"] == "male":
                        tagg = ("male")
                    else:
                        tagg = ("female")
                    tree.insert(parent,  counter, kid, text=name, tag=tagg)
    tree.tag_configure('male', background='CadetBlue1')
    tree.tag_configure('female', background='pink1')


def milking_chart():
    """chart containing quantity of milk on y axis and day on x axis"""

    language_dict = set_options.Options()
    language_dict.get_text_dict("charts_tab")
    lang_dict = language_dict.widget_text_dictionary

    milking_window = tk.Toplevel(height=1000, width=1000)
    milking_window.minsize(width=700, height=410)
    rows = 0
    while rows < 100:
        milking_window.rowconfigure(rows, weight=1)
        milking_window.columnconfigure(rows, weight=2)
        rows += 1

    def on_frame_configure(milking_canvas):
        '''Reset the scroll region to encompass the inner frame'''
        milking_canvas.configure(scrollregion=milking_canvas.bbox("all"))

    milking_label = tk.Label(
        milking_window, text=lang_dict["milking_label"])
    milking_label.grid(row=0, column=1)

    # Frame on which canvas and milk quantity is displayed
    values_frame = tk.Frame(milking_window, width=700, height=435)
    values_frame.grid(
        row=1, column=0, columnspan=15,
        rowspan=16, sticky=tk.W+tk.E+tk.N+tk.S)

    # contains drownings for chart and a little frame on the bottom with
    # date labels, both canvas and this frame are bind to be scrollable
    milking_canvas = tk.Canvas(
        values_frame, bg="white", width=680, height=435,
        scrollregion=(0, 0, 5520, 0))
    milking_canvas.place(x=25, y=0)

    # little frame on the bottom of canvas, bind with canvas
    dates_frame = tk.Frame(milking_canvas, width=5500, height=17)
    dates_frame.bind(
        "<Configure>", lambda event,
        milking_canvas=milking_canvas: on_frame_configure(milking_canvas))
    milking_canvas.create_window((0, 435), window=dates_frame, anchor="sw")

    # create lines showing x and y axis on canvas
    milking_canvas.create_line(10, 10, 10, 410)
    milking_canvas.create_line(10, 410, 5500, 410)

    hbar = tk.Scrollbar(
        milking_window, orient=tk.HORIZONTAL, command=milking_canvas.xview)
    hbar.grid(
        row=17, column=0, columnspan=15, rowspan=15, sticky=tk.W+tk.E)

    # get dictionary containing number of the month as key and number of
    # days within it as value
    monthrange = get_date.get_year_and_monthranges()
    # reads all milking events during current year
    events = process_calendar_data.get_milking_events()

    # get the biggest milking mesurment to adjust the chart
    value = 0
    if events:
        for month in range(1, 13):
            for day in range(1, monthrange[str(month)]+1):
                y_m_d = (str(monthrange['CurrentYear'])
                         + '/' + str(month) + '/' + str(day))

                try:
                    if int(events[y_m_d]) > value:
                        value = int(events[y_m_d])
                except KeyError:
                    pass

    # determine ratio depending on biggest value in milking events
    # ratio 8 means that for one unit of milk there are 8
    # pixels to display the value with 50 units being max value
    if value * 8 <= 400:
        ratio = 8
        quantity_marks = 16
        counter = 16
        quantity_label = 2
        x_constant = 7
        y_constant = 403
        ratio = 8
    elif value * 4 <= 400:
        ratio = 4
        quantity_marks = 20
        counter = 20
        quantity_label = 5
        x_constant = 2
        y_constant = 408
    elif value * 2 <= 400:
        ratio = 2
        quantity_marks = 20
        counter = 10
        quantity_label = 10
        x_constant = 2
        y_constant = 403
    elif value * 1 <= 400:
        ratio = 1
        quantity_marks = 25
        counter = 25
        quantity_label = 25
        x_constant = 2
        y_constant = 403
    elif value / 2 <= 400:
        # ratio -2 means that for one pixel displayed there are 2 units of
        # milk with 800 units being max value
        ratio = -2
        quantity_marks = 25
        counter = 25
        quantity_label = 50
        x_constant = 2
        y_constant = 403
    elif value / 4 <= 400:
        ratio = -4
        quantity_marks = 25
        counter = 25
        quantity_label = 100
        x_constant = 0
        y_constant = 403
    elif value / 8 <= 400:
        ratio = -8
        quantity_marks = 25
        counter = 25
        quantity_label = 200
        x_constant = 0
        y_constant = 403
    elif value / 10 <= 400:
        ratio = -10
        quantity_marks = 25
        counter = 25
        quantity_label = 250
        x_constant = 0
        y_constant = 403
    elif value / 20 <= 400:
        ratio = -20
        quantity_marks = 25
        counter = 25
        quantity_label = 500
        x_constant = 0
        y_constant = 403

    if ratio == 8:
        quantity_marks = 16
        while counter <= 400:
            milking_canvas.create_line(
                5, 410-counter, 15, 410-counter)
            milking_canvas.create_line(
                16, 410-counter, 5500, 410-counter,
                fill="light gray")
            counter += quantity_marks

        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label,  font="Helvetic  8")
            label.place(x=x_constant, y=y_constant - quantity_marks)
            quantity_marks += 16
            quantity_label += 2

    elif ratio == 4:
        quantity_marks = 20
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 20
        quantity_marks = 25
        quantity_label = 5
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=2, y=408 - quantity_marks)
            quantity_marks += 20
            quantity_label += 5

    elif ratio == 2:
        quantity_marks = 20
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 20
        quantity_marks = 20
        quantity_label = 10
        while quantity_marks <= 400:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=2, y=403 - quantity_marks)
            quantity_marks += 20
            quantity_label += 10

    elif ratio == 1:
        quantity_marks = 25
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 25
        quantity_marks = 25
        quantity_label = 25
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=2, y=403 - quantity_marks)
            quantity_marks += 25
            quantity_label += 25

    elif ratio == -2:
        quantity_marks = 25
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 25
        quantity_marks = 25
        quantity_label = 50
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=2, y=403 - quantity_marks)
            quantity_marks += 25
            quantity_label += 50

    elif ratio == -4:
        quantity_marks = 25
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 25
        quantity_marks = 25
        quantity_label = 100
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=0, y=403 - quantity_marks)
            quantity_marks += 25
            quantity_label += 100

    elif ratio == -8:
        quantity_marks = 25
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 25
        quantity_marks = 25
        quantity_label = 200
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=0, y=403 - quantity_marks)
            quantity_marks += 25
            quantity_label += 200

    elif ratio == -10:
        quantity_marks = 25
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 25
        quantity_marks = 25
        quantity_label = 250
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=0, y=403 - quantity_marks)
            quantity_marks += 25
            quantity_label += 250

    elif ratio == -20:
        quantity_marks = 25
        while quantity_marks <= 400:
            milking_canvas.create_line(
                5, 410-quantity_marks, 15, 410-quantity_marks)
            milking_canvas.create_line(
                16, 410-quantity_marks, 5500,
                410-quantity_marks, fill="light gray")
            quantity_marks += 25
        quantity_marks = 25
        quantity_label = 500
        while quantity_marks <= 410:
            label = tk.Label(
                values_frame, text=quantity_label, font="Helvetica 8")
            label.place(x=0, y=403 - quantity_marks)
            quantity_marks += 25
            quantity_label += 500

    # display bars on canvas
    const_x = 11
    const_y = 410
    for month in range(1, 13):
        for day in range(1, monthrange[str(month)]+1):
            y_m_d = str(monthrange['CurrentYear'])+"/"+str(month)+"/"+str(day)
            try:
                if ratio > 0:
                    milking_canvas.create_rectangle(
                        const_x, const_y - (int(events[y_m_d])*ratio),
                        const_x+15, const_y, width=0, fill='green')
                else:
                    milking_canvas.create_rectangle(
                        const_x, const_y - (int(events[y_m_d]) / (-ratio)),
                        const_x + 15, const_y, width=0, fill='green')
                const_x += 15
            except KeyError:
                const_x += 15
            else:
                pass

    # display day marks on x axis
    date_marks = 18
    for i in range(1, 366):
        milking_canvas.create_line(date_marks, 405, date_marks, 415)
        date_marks += 15

    # display day and month unter day marks on x axis
    date_label_x = 7
    date_label = tk.Label(dates_frame, text='1/1', font="Helvetica 8")
    date_label.place(x=date_label_x, y=0)
    month = 2
    for i in range(1, 12):
        if monthrange[str(i)] == 28:
            date_label_x += 28 * 15
            date_label = tk.Label(
                dates_frame, text='1/'+str(month), font="Helvetica 8")
            date_label.place(x=date_label_x, y=0)
        if monthrange[str(i)] == 29:
            date_label_x += 29 * 15
            date_label = tk.Label(
                dates_frame, text='1/'+str(month), font="Helvetica 8")
            date_label.place(x=date_label_x, y=0)
        if monthrange[str(i)] == 30:
            date_label_x += 30 * 15
            date_label = tk.Label(
                dates_frame, text='1/'+str(month), font="Helvetica 8")
            date_label.place(x=date_label_x, y=0)
        if monthrange[str(i)] == 31:
            date_label_x += 31 * 15
            date_label = tk.Label(
                dates_frame, text='1/'+str(month), font="Helvetica 8")
            date_label.place(x=date_label_x, y=0)
        month += 1


def age_pyramid():
    """
    age pyramid with males on left and females on the right.
    y axis shows age and x axis shows how many goats share it.
    display some additional info.

    """

    language_dict = set_options.Options()
    language_dict.get_text_dict("charts_tab")
    lang_dict = language_dict.widget_text_dictionary
    print(lang_dict)
    pyramid_window = tk.Toplevel(height=500, width=500)
    rows = 0
    while rows < 50:
        pyramid_window.rowconfigure(rows, weight=1)
        pyramid_window.columnconfigure(rows, weight=2)
        rows += 1

    dead_goats = process_profiles_data.count_parameters("DATE_OF_DEATH")
    all_goats = process_profiles_data.count_parameters("profiles")
    sold_goats = process_profiles_data.count_parameters("SOLD")
    age_of_goats = process_profiles_data.age_of_goats()
    all_profiles = process_profiles_data.get_all_profiles()
    male_goats = sort_profiles.show(
        all_profiles, lang_dict["show1"], lang_dict["show3"])
    female_goats = sort_profiles.show(
        all_profiles, lang_dict["show2"], lang_dict["show3"])

    active_profiles = (all_goats - dead_goats) - sold_goats
    goat_per_year = (
        age_of_goats['m1'] + age_of_goats['m2'] + age_of_goats['m3']
        + age_of_goats['m4'] + age_of_goats['m5'] + age_of_goats['m6']
        + age_of_goats['m7'] + age_of_goats['m8'] + age_of_goats['m9']
        + age_of_goats['m10'] + age_of_goats['m11'] + age_of_goats['m12']
        + age_of_goats['m13'] + age_of_goats['m14'] + age_of_goats['m15']
        + age_of_goats['f1'] + age_of_goats['f2'] + age_of_goats['f3']
        + age_of_goats['f4'] + age_of_goats['f5'] + age_of_goats['f6']
        + age_of_goats['f7'] + age_of_goats['f8'] + age_of_goats['f9']
        + age_of_goats['f10'] + age_of_goats['f11'] + age_of_goats['f12']
        + age_of_goats['f13'] + age_of_goats['f14'] + age_of_goats['f15']
        )
    label_1 = tk.Label(
        pyramid_window, text=lang_dict["label_1"]
        + str(active_profiles), font="Helvetica 12")
    label_1.grid(row=0, column=0, sticky='w')
    label_2 = tk.Label(
        pyramid_window, font="Helvetica 12",
        text=lang_dict["label_21"]
        + str(goat_per_year) + '/' + str(active_profiles)
        + lang_dict["label_22"])
    label_2.grid(row=1, column=0, sticky='w')
    label_3 = tk.Label(
        pyramid_window, font="Helvetica 12",
        text=lang_dict["label_3"]+str(dead_goats + sold_goats))
    label_3.grid(row=2, column=0, sticky='w')

    main_frame = tk.Frame(
        pyramid_window, height=370, width=800, bg="white")
    main_frame.grid(row=3, column=0)

    label_4 = tk.Label(
        pyramid_window, text=lang_dict["label_4"]
        + str(len(male_goats)), font="Helvetica 12")
    label_4.grid(row=4, column=0, sticky='w')

    label_5 = tk.Label(
        pyramid_window, text=lang_dict["label_5"]
        + str(len(female_goats)), font="Helvetica 12")
    label_5.grid(row=5, column=0, sticky='w')

    # display values under female_canvas
    counter = 2
    counter2 = 446
    for i in range(1, 13):
        label = tk.Label(
            main_frame, text=str(counter), font="Helvetica 10", bg='white')
        if counter < 10:
            label.place(x=counter2, y=333)
        else:
            label.place(x=counter2-4, y=333)
        counter += 2
        counter2 += 30

    # display values under male_canvas
    counter = 2
    counter2 = 42
    for i in range(1, 13):
        label = tk.Label(
            main_frame, text=str(counter), font="Helvetica 10", bg='white')
        if counter < 10:
            label.place(x=385-counter2, y=333)
        else:
            label.place(x=385-counter2-4, y=333)
        counter += 2
        counter2 += 30

    male_canvas = tk.Canvas(main_frame, height=305, width=385, bg='white')
    male_canvas.place(x=0, y=25)

    female_canvas = tk.Canvas(main_frame, height=305, width=385, bg='white')
    female_canvas.place(x=415, y=25)

    label = tk.Label(
        main_frame, text="15+", font="Helvetica 12", bg='white')
    label.place(x=385, y=25)
    counter = 45
    counter2 = 14
    for i in range(1, 15):
        label = tk.Label(
            main_frame, text=str(counter2), font="Helvetica 12", bg='white')
        if counter2 > 9:
            label.place(x=390, y=counter)
        else:
            label.place(x=395, y=counter)
        counter += 20
        counter2 -= 1

    male_label = tk.Label(
        main_frame, text=lang_dict["male_label"], font="Helvetica 12", bg='white')
    male_label.place(x=170, y=0)
    female_label = tk.Label(
        main_frame, text=lang_dict["female_label"], font="Helvetica 12", bg='white')
    female_label.place(x=570, y=0)
    age_label = tk.Label(
        main_frame, text=lang_dict["age_label"], font="Helvetica 12", bg='white')
    age_label.place(x=385, y=0)

    # display stuff on male Canvas
    # Y axis
    male_canvas.create_line(380, 0, 380, 305)
    # X axis
    male_canvas.create_line(0, 300, 385, 300)
    # display bars on male_canvas
    const_1 = 20
    const_2 = 0
    for i in range(1, 16):
        if age_of_goats["m"+str(i)] != 0:
            male_canvas.create_rectangle(
                380-15*age_of_goats["m"+str(i)], 300-const_1, 380,
                300-const_2, width=0, fill='CadetBlue1')
        const_1 += 20
        const_2 += 20
    # display marks on y axis
    date_marks = 10
    for i in range(1, 16):
        male_canvas.create_line(375, date_marks, 385, date_marks)
        date_marks += 20
    # display marks on x axis (male canvas)
    age_marks = 20
    for i in range(1, 25):
        male_canvas.create_line(385-age_marks, 295, 385-age_marks, 305)
        male_canvas.create_line(
            385-age_marks, 294, 385-age_marks, 0, fill="light gray")
        age_marks += 15

    # display stuff on female Canvas
    female_canvas.create_line(7, 0, 7, 305)
    female_canvas.create_line(0, 300, 385, 300)
    # display bars on female_canvas
    const_1 = 20
    const_2 = 0
    for i in range(1, 16):
        if age_of_goats["f"+str(i)] != 0:
            female_canvas.create_rectangle(
                7+15*age_of_goats["f"+str(i)], 300-const_1, 8, 301-const_2,
                width=0, fill='pink1')
        const_1 += 20
        const_2 += 20

    # display marks on Y axis (female canvas)
    date_marks = 10
    for i in range(1, 16):
        female_canvas.create_line(0, date_marks, 12, date_marks)
        date_marks += 20
    # display marks on x axis (female canvas)
    age_marks = 22
    for i in range(1, 25):
        female_canvas.create_line(0+age_marks, 295, 0+age_marks, 305)
        female_canvas.create_line(
            0+age_marks, 294, 0+age_marks, 0, fill="light gray")
        age_marks += 15
