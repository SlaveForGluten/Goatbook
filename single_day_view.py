"""single day view where you can add view and delete events """

# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import scrolledtext as sc
from tkinter import messagebox

import process_calendar_data
import check_calendar_input
import get_date
import calendar_tab
import set_options


def add_event_window(month_counter, day_of_the_event, tab):
    language_dict = set_options.Options()
    language_dict.get_text_dict("single_day_view")
    lang_dict = language_dict.widget_text_dictionary

    month_name = process_calendar_data.get_month_name(month_counter)

    date_dict = get_date.get(month_counter)
    date_dict['DayOfTheNewEvent'] = day_of_the_event
    date_dict['DistancefromToday'] = month_counter

    single_day_frame = tk.Frame()
    single_day_frame.grid(
        row=0, column=0, columnspan=50, rowspan=50, sticky="NESW")

    def add_pregnancy():
        def save_event():
            result = check_calendar_input.pregnancy_event(
                date_dict, add_mum.get(), add_dad.get())

            if result == "success":
                pregnancy_window.destroy()
                single_day_frame.destroy()
                add_event_window(
                    month_counter, day_of_the_event, tab)

        pregnancy_window = tk.Toplevel(height=230, width=320)

        mum_label = tk.Label(
            pregnancy_window, text=lang_dict["mum_label"], font="Helvetica 12")
        mum_label.place(x=10, y=50)

        dad_label = tk.Label(
            pregnancy_window, text=lang_dict["dad_label"], font="Helvetica 12")
        dad_label.place(x=10, y=100)

        add_mum = tk.Entry(pregnancy_window, width=20, font="Helvetica 12")
        add_mum.place(x=105, y=50)

        add_dad = tk.Entry(pregnancy_window, width=20, font="Helvetica 12")
        add_dad.place(x=105, y=100)

        save = tk.Button(
            pregnancy_window, text=lang_dict["save"], height=1, width=6,
            font="Helvetica 12", command=save_event)
        save.place(x=170, y=190)

        close = tk.Button(
            pregnancy_window, text=lang_dict["close"], height=1, width=6,
            font="Helvetica 12", command=pregnancy_window.destroy)
        close.place(x=243, y=190)

    def add_medicine():
        def save_event():
            result = check_calendar_input.medicine_event(
                date_dict,
                add_treated_goat.get(),
                add_medicine_entry.get(),
                add_dosing_period.get(),
                add_withdrawal_period.get(),
                add_note.get('1.0', 'end-1c'))

            if result == "success":
                medicine_window.destroy()
                single_day_frame.destroy()
                add_event_window(
                    month_counter, day_of_the_event, tab)

        medicine_window = tk.Toplevel(single_day_frame, height=460, width=390)

        treated_goat = tk.Label(
            medicine_window, text=lang_dict["treated_goat"],
            font="Helvetica 12")
        treated_goat.place(x=10, y=10)

        add_treated_goat = tk.Entry(
            medicine_window, width=35, font="Heletica 12")
        add_treated_goat.place(x=10, y=35)

        medicine = tk.Label(
            medicine_window, text=lang_dict["medicine"], font="Helvetica 12")
        medicine.place(x=10, y=75)

        add_medicine_entry = tk.Entry(
            medicine_window, width=17, font="Helvetica 12")
        add_medicine_entry.place(x=170, y=75)

        dosing_period = tk.Label(
            medicine_window, text=lang_dict["dosing_period"],
            font="Helvetica 12")
        dosing_period.place(x=10, y=120)

        withdrawal_period = tk.Label(
            medicine_window, text=lang_dict["withdrawal_period"],
            font="Helvetica 12")
        withdrawal_period.place(x=10, y=170)

        note = tk.Label(
            medicine_window, text=lang_dict["note"], font="Helvetica 12")
        note.place(x=10, y=220)

        add_dosing_period = tk.Entry(
            medicine_window, width=5, font="Helvetica 12")
        add_dosing_period.place(x=275, y=120)

        add_withdrawal_period = tk.Entry(
            medicine_window, width=5, font="Helvetica 12")
        add_withdrawal_period.place(x=275, y=170)

        add_note = sc.ScrolledText(
            medicine_window, width=35, height=7, font="Helvetica 12")
        add_note.place(x=10, y=245)

        save = tk.Button(
            medicine_window, text=lang_dict["save"], height=1, width=6,
            font="Helvetica 12", command=save_event)
        save.place(x=240, y=420)

        close = tk.Button(
            medicine_window, text=lang_dict["close"], height=1, width=6,
            font="Helvetica 12", command=medicine_window.destroy)
        close.place(x=313, y=420)

    def add_milking():

        def save_event():
            result = check_calendar_input.milking_event(
                date_dict, addMilk.get())

            if result == "success":
                milkingWindow.destroy()
                single_day_frame.destroy()
                add_event_window(
                    month_counter, day_of_the_event, tab)

        milkingWindow = tk.Toplevel(single_day_frame, height=175, width=250)

        milking = tk.Label(
            milkingWindow, text=lang_dict["milking"], font="Helvetica 12")
        milking.place(x=10, y=50)

        addMilk = tk.Entry(milkingWindow, width=5, font="Helvetica 12")
        addMilk.place(x=180, y=50)

        save = tk.Button(
            milkingWindow, text=lang_dict["save"], height=1, width=6,
            font="Helvetica 12", command=save_event)
        save.place(x=100, y=135)

        close = tk.Button(
            milkingWindow, text=lang_dict["close"], height=1, width=6,
            font="Helvetica 12", command=milkingWindow.destroy)
        close.place(x=173, y=135)

    def add_other():
        def save_event():
            result = check_calendar_input.other_event(
                date_dict, addTitle.get(), add_note.get('1.0', 'end-1c'))

            if result == "success":
                other_window.destroy()
                single_day_frame.destroy()
                add_event_window(
                    month_counter, day_of_the_event, tab)

        other_window = tk.Toplevel(single_day_frame, height=350, width=390)

        title = tk.Label(
            other_window, text=lang_dict["title"], font="Helvetica 12")
        title.place(x=10, y=50)

        note = tk.Label(
            other_window, text=lang_dict["note"], font="Helvetica 12")
        note.place(x=10, y=100)

        addTitle = tk.Entry(other_window, width=15, font="Helvetica 12")
        addTitle.place(x=200, y=50)

        add_note = sc.ScrolledText(
            other_window, width=35, height=7, font="Helvetica 12")
        add_note.place(x=10, y=125)

        save = tk.Button(
            other_window, text=lang_dict["save"], height=1, width=6,
            font="Helvetica 12", command=save_event)
        save.place(x=240, y=310)

        close = tk.Button(
            other_window, text=lang_dict["close"], height=1, width=6,
            font="Helvetica 12", command=other_window.destroy)
        close.place(x=313, y=310)

    def help_window():
        other_window = tk.Toplevel(single_day_frame, height=100, width=420)

        advice = tk.Label(
            other_window, text=lang_dict["advice"],
            font="Helvetica 12")
        advice.place(x=10, y=20)
    # kills the day - view frame
    # displays reseted month view frame

    def backButton():
        calendar_tab.Calendar(tab, month_counter)
        single_day_frame.destroy()

    a = (str(date_dict['ViewedYear']) + "/" + str(date_dict['ViewedMonth'])
         + "/" + str(day_of_the_event))
    list__of_events = process_calendar_data.get_event(a)

    back = tk.Button(
        single_day_frame, text=lang_dict["back"], height=2, width=7,
        font="Helvetica 12", command=backButton)
    back.place(x=10, y=10)

    pregnancy = tk.Button(
        single_day_frame, text=lang_dict["pregnancy"], height=2, width=9,
        font="Helvetica 12", bg="hot pink", command=add_pregnancy)
    pregnancy.place(x=105, y=10)

    medicine_button = tk.Button(
        single_day_frame, text=lang_dict["medicine_button"], height=2, width=8,
        font="Helvetica 12", bg="blue", command=add_medicine)
    medicine_button.place(x=215, y=10)

    daily_milking = tk.Button(
        single_day_frame, text=lang_dict["daily_milking"], height=2, width=10,
        font="Helvetica 12", bg="yellow", command=add_milking)
    daily_milking.place(x=314, y=10)

    other = tk.Button(
        single_day_frame, text=lang_dict["other"], height=2, width=7,
        font="Helvetica 12", bg="green2", command=add_other)
    other.place(x=435, y=10)

    help_button = tk.Button(
        single_day_frame, text="?", height=1, width=2,
        font="Helvetica 12", command=help_window)
    help_button.place(x=530, y=28)

    date = tk.Label(
        single_day_frame, text=str(day_of_the_event) + " " + month_name + " "
        + str(date_dict['ViewedYear']), font="Helvetica 25 bold")
    date.place(x=280, y=100)

    def reset():
        single_day_frame.destroy
        calendar_tab.Calendar(tab, month_counter)

    if list__of_events:

        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas_scrollregion = 100*len(list__of_events)

        canvas = tk.Canvas(
            single_day_frame, width=760, height=600,
            scrollregion=(0, 0, 0, canvas_scrollregion))
        canvas.place(x=0, y=180)

        vbar = tk.Scrollbar(
            single_day_frame, orient=tk.VERTICAL, command=canvas.yview)
        vbar.place(x=750, y=180, height=600)
        canvas.config(yscrollcommand=vbar.set)

        on_canvas_frame = tk.Frame(
            canvas, width=696, height=canvas_scrollregion)
        on_canvas_frame.place(x=65, y=0)

        on_canvas_frame.bind(
            "<Configure>",
            lambda event, canvas=canvas: onFrameConfigure(canvas))
        canvas.create_window((50, 0), window=on_canvas_frame, anchor="nw")

        event_numbers = []
        for event in range(len(list__of_events)):

            single_event = list__of_events[event].split("-")
            event_numbers.append(single_event[len(single_event)-1])

            def send(event):
                answer = messagebox.askquestion(
                    lang_dict["messagebox"], lang_dict["messagebox1"],
                    icon='warning')
                if answer == "yes":
                    calculatedEvent = int(event.y/100)
                    process_calendar_data.delete_event(
                        event_numbers[calculatedEvent])
                    single_day_frame.destroy()
                    add_event_window(
                        month_counter, day_of_the_event, tab)

            on_canvas_frame.bind("<Button-3>", send)

            if single_event[1] == "OTHER":
                title = tk.Label(
                    on_canvas_frame, text=single_event[2],
                    font="Helvetica 12 bold")
            else:
                title = tk.Label(
                    on_canvas_frame, text=single_event[1],
                    font="Helvetica 12 bold")
            title.place(x=10, y=event*100+5)

            if single_event[1] == "PREGNANCY":
                canvas.create_oval(
                    10, event * 100 + 10, 30, event * 100 + 30,
                    fill="hot pink")
                label = tk.Label(
                    on_canvas_frame, text=lang_dict["mum_label"] + ": "
                    + single_event[2], font="Helvetica 10")
                label.place(x=10, y=event * 100 + 30)
                label2 = tk.Label(
                    on_canvas_frame, text=lang_dict["dad_label"] + ": "
                    + single_event[3], font="Helvetica 10")
                label2.place(x=10, y=event*100+60)

            elif single_event[1] == "MEDICINE":
                canvas.create_oval(
                    10, event * 100 + 10, 30, event * 100 + 30,
                    fill="blue")
                label = tk.Label(
                    on_canvas_frame, text=lang_dict["label"] + single_event[2],
                    font="Helvetica 10")
                label.place(x=100, y=event*100+5)
                label2 = tk.Label(
                    on_canvas_frame, text=lang_dict["medicine_button"] + ": " +
                    single_event[3], font="Helvetica 10")
                label2.place(x=10, y=event*100+30)
                # if not empty(0) place label
                if int(single_event[4]) != 0:
                    # if 1 day - singular, if more - plural
                    if int(single_event[4]) == 1:
                        label3 = tk.Label(
                            on_canvas_frame, text=lang_dict["label1"]
                            + single_event[4] + lang_dict["label2"],
                            font="Helvetica 10")
                    else:
                        label3 = tk.Label(
                            on_canvas_frame, text=lang_dict["label1"]
                            + single_event[4]+" days left.",
                            font="Helvetica 10")
                    label3.place(x=200, y=event * 100 + 30)
                    # I don't want withdrawal period to be displayed on
                    # "medicine" event, remove quotation marks to add this
                label5 = tk.Label(
                    on_canvas_frame, text=single_event[6],
                    font="Helvetica 10", wraplength=680, justify=tk.LEFT)
                label5.place(x=10, y=event*100+50)

            elif single_event[1] == "MILKING":
                canvas.create_oval(
                    10, event * 100 + 10, 30,
                    event * 100 + 30, fill="yellow")
                label = tk.Label(
                    on_canvas_frame, text=lang_dict["label3"]
                    + single_event[2], font="Helvetica 10")
                label.place(x=10, y=event*100+30)

            elif single_event[1] == "OTHER":
                canvas.create_oval(
                    10, event * 100 + 10, 30, event * 100 + 30,
                    fill="green2")
                label = tk.Label(
                    on_canvas_frame, text=single_event[3],
                    font="Helvetica 10", wraplength=670, justify=tk.LEFT)
                label.place(x=10, y=event * 100 + 30)

            elif single_event[1] == "DELIVERY":
                canvas.create_oval(
                    10, event * 100 + 10, 30, event * 100 + 30, fill="red")
                if single_event[3] != "":
                    label = tk.Label(
                        on_canvas_frame,
                        text=lang_dict["label4"]
                        + single_event[2] + " " + lang_dict["label5"]
                        + single_event[3] + lang_dict["label6"],
                        font="Helvetica 10")
                    label.place(x=10, y=event*100+30)
                else:
                    label = tk.Label(
                        on_canvas_frame,
                        text=lang_dict["label4"]
                        + single_event[2] + lang_dict["label5"],
                        font="Helvetica 10")
                    label.place(x=10, y=event*100+30)

            elif single_event[1] == "WITHDRAWAL":
                canvas.create_oval(
                    10, event * 100 + 10, 30, event * 100 + 30,
                    fill="black")
                label = tk.Label(
                    on_canvas_frame, text=lang_dict["label"] + single_event[2],
                    font="Helvetica 10")
                label.place(x=140, y=event*100+5)
                label2 = tk.Label(
                    on_canvas_frame, text=lang_dict["label7"]
                    + single_event[3], font="Helvetica 10")
                label2.place(x=10, y=event * 100 + 30)
                # if 1 day - singular, if more - plural
                if int(single_event[5]) > 1:
                    label3 = tk.Label(
                        on_canvas_frame, text=lang_dict["label8"] +
                        single_event[5] + " days left.", font="Helvetica 10")
                else:
                    label3 = tk.Label(
                        on_canvas_frame, text=lang_dict["label8"] +
                        single_event[5] + " day left.", font="Helvetica 10")
                label3.place(x=250, y=event*100+30)
                label4 = tk.Label(
                    on_canvas_frame, text=single_event[6],
                    font="Helvetica 10", wraplength=680, justify=tk.LEFT)
                label4.place(x=10, y=event*100+50)
