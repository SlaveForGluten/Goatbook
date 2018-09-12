"""create and istplay day-buttons on calendar page"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk

import get_date
import process_calendar_data
import single_day_view
import set_options


class Calendar:
    """
    month_counter let calendar know which month are we displaying:
    -1 is one month back from today(which is 0) and 2 is 2 months
    in future from today
    """

    def __init__(self, tab, month_counter):
        """
        pressing 'next month' reloads __init__ with mounth_counter as 1
        and pressing 'prev month' reloads __init__ with mounth_counter as -1
        you can go as far as you like in future or past
        """

        date_dict = get_date.get(month_counter)

        language_dict = set_options.Options()
        language_dict.get_text_dict("calendar_tab")
        lang_dict = language_dict.widget_text_dictionary

        def next_month():
            next_month = month_counter + 1
            Calendar(tab, next_month)

        def previous_month():
            prev_month = month_counter - 1
            Calendar(tab, prev_month)

        calendar_frame = tk.Frame(tab, height=800, width=800)
        calendar_frame.place(x=0, y=0)

        month_name = process_calendar_data.get_month_name(month_counter)

        # "next month" and "previous month" buttons
        prev_month_bttn = tk.Button(
            calendar_frame, text="<", height=1, command=previous_month,
            width=1, font="Helvetica 25 bold", relief=tk.FLAT, takefocus=0)
        prev_month_bttn.place(x=160, y=10)

        next_month_bttn = tk.Button(
            calendar_frame, text=">", height=1, command=next_month, width=1,
            font="Helvetica 25 bold", relief=tk.FLAT, takefocus=0)
        next_month_bttn.place(x=600, y=10)

        month_label = tk.Label(
            calendar_frame, text=month_name + " " +
            str(date_dict['ViewedYear']), font="Helvetica 20")
        month_label.place(x=310, y=20)

        mo_label = tk.Label(
            calendar_frame, text=lang_dict["mo_label"], font="Helvetica 16")
        mo_label.place(x=70, y=60)

        tu_label = tk.Label(
            calendar_frame, text=lang_dict["tu_label"], font="Helvetica 16")
        tu_label.place(x=170, y=60)

        we_label = tk.Label(
            calendar_frame, text=lang_dict["we_label"], font="Helvetica 16")
        we_label.place(x=270, y=60)

        th_label = tk.Label(
            calendar_frame, text=lang_dict["th_label"], font="Helvetica 16")
        th_label.place(x=370, y=60)

        fr_label = tk.Label(
            calendar_frame, text=lang_dict["fr_label"], font="Helvetica 16")
        fr_label.place(x=470, y=60)

        sa_label = tk.Label(
            calendar_frame, text=lang_dict["sa_label"], font="Helvetica 16")
        sa_label.place(x=570, y=60)

        su_label = tk.Label(
            calendar_frame, text=lang_dict["su_label"], font="Helvetica 16")
        su_label.place(x=670, y=60)

        # define position of first day(button) on the calendar depending on
        # lang_dict['FirstDayOfTheViewedMonth'] - day of the week
        # given month starts with
        y_orient = 100
        if int(date_dict['FirstDayOfTheViewedMonth']) == 0:
            x_orient = 60
            counter = 1
        elif int(date_dict['FirstDayOfTheViewedMonth']) == 1:
            x_orient = 160
            counter = 2
        elif int(date_dict['FirstDayOfTheViewedMonth']) == 2:
            x_orient = 260
            counter = 3
        elif int(date_dict['FirstDayOfTheViewedMonth']) == 3:
            x_orient = 360
            counter = 4
        elif int(date_dict['FirstDayOfTheViewedMonth']) == 4:
            x_orient = 460
            counter = 5
        elif int(date_dict['FirstDayOfTheViewedMonth']) == 5:
            x_orient = 560
            counter = 6
        elif int(date_dict['FirstDayOfTheViewedMonth']) == 6:
            x_orient = 660
            counter = 7

        # next 31 buttons serve as days in calendar
        # function below lets know which button triggered add_event_window

        day_1_button = CreateButton(
            calendar_frame, "01", x_orient, y_orient, tab, month_counter)
        day_1_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_1_canvas.event_markers(month_counter, 1)

        # using counter i make sure that no more than seven
        # buttons(days) are displayed in each row(week)
        counter += 1

        # if to far right start from beginning
        if x_orient == 660:
            x_orient = 60
        # if not to far right place next button right from last one
        else:
            x_orient = x_orient+100
        # each row has 7 positions, if last button was placed on last position
        # in given row - display next button in row bellow
        if counter >= 8:
            y_orient = 200

        day_2_button = CreateButton(
            calendar_frame, "02", x_orient, y_orient, tab, month_counter)
        day_2_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_2_canvas.event_markers(month_counter, 2)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 8:
            y_orient = 200

        day_3_button = CreateButton(
            calendar_frame, "03", x_orient, y_orient, tab, month_counter)
        day_3_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_3_canvas.event_markers(month_counter, 3)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 8:
            y_orient = 200

        day_4_button = CreateButton(
            calendar_frame, "04", x_orient, y_orient, tab, month_counter)
        day_4_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_4_canvas.event_markers(month_counter, 4)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 8:
            y_orient = 200

        day_5_button = CreateButton(
            calendar_frame, "05", x_orient, y_orient, tab, month_counter)
        day_5_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_5_canvas.event_markers(month_counter, 5)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 8:
            y_orient = 200

        day_6_button = CreateButton(
            calendar_frame, "06", x_orient, y_orient, tab, month_counter)
        day_6_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_6_canvas.event_markers(month_counter, 6)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 8:
            y_orient = 200

        day_7_button = CreateButton(
            calendar_frame, "07", x_orient, y_orient, tab, month_counter)
        day_7_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_7_canvas.event_markers(month_counter, 7)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 8:
            y_orient = 200

        day_8_button = CreateButton(
            calendar_frame, "08", x_orient, y_orient, tab, month_counter)
        day_8_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_8_canvas.event_markers(month_counter, 8)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_9_button = CreateButton(
            calendar_frame, "09", x_orient, y_orient, tab, month_counter)
        day_9_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_9_canvas.event_markers(month_counter, 9)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_10_button = CreateButton(
            calendar_frame, "10", x_orient, y_orient, tab, month_counter)
        day_10_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_10_canvas.event_markers(month_counter, 10)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_11_button = CreateButton(
            calendar_frame, "11", x_orient, y_orient, tab, month_counter)
        day_11_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_11_canvas.event_markers(month_counter, 11)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_12_button = CreateButton(
            calendar_frame, "12", x_orient, y_orient, tab, month_counter)
        day_12_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_12_canvas.event_markers(month_counter, 12)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_13_button = CreateButton(
            calendar_frame, "13", x_orient, y_orient, tab, month_counter)
        day_13_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_13_canvas.event_markers(month_counter, 13)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_14_button = CreateButton(
            calendar_frame, "14", x_orient, y_orient, tab, month_counter)
        day_14_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_14_canvas.event_markers(month_counter, 14)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 15:
            y_orient = 300

        day_15_button = CreateButton(
            calendar_frame, "15", x_orient, y_orient, tab, month_counter)
        day_15_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_15_canvas.event_markers(month_counter, 15)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_16_button = CreateButton(
            calendar_frame, "16", x_orient, y_orient, tab, month_counter)
        day_16_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_16_canvas.event_markers(month_counter, 16)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_17_button = CreateButton(
            calendar_frame, "17", x_orient, y_orient, tab, month_counter)
        day_17_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_17_canvas.event_markers(month_counter, 17)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_18_button = CreateButton(
            calendar_frame, "18", x_orient, y_orient, tab, month_counter)
        day_18_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_18_canvas.event_markers(month_counter, 18)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_19_button = CreateButton(
            calendar_frame, "19", x_orient, y_orient, tab, month_counter)
        day_19_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_19_canvas.event_markers(month_counter, 19)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_20_button = CreateButton(
            calendar_frame, "20", x_orient, y_orient, tab, month_counter)
        day_20_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_20_canvas.event_markers(month_counter, 20)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_21_button = CreateButton(
            calendar_frame, "21", x_orient, y_orient, tab, month_counter)
        day_21_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_21_canvas.event_markers(month_counter, 21)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 22:
            y_orient = 400

        day_22_button = CreateButton(
            calendar_frame, "22", x_orient, y_orient, tab, month_counter)
        day_22_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_22_canvas.event_markers(month_counter, 22)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 29:
            y_orient = 500

        day_23_button = CreateButton(
            calendar_frame, "23", x_orient, y_orient, tab, month_counter)
        day_23_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_23_canvas.event_markers(month_counter, 23)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 29:
            y_orient = 500

        day_24_button = CreateButton(
            calendar_frame, "24", x_orient, y_orient, tab, month_counter)
        day_24_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_24_canvas.event_markers(month_counter, 24)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 29:
            y_orient = 500

        dahy_25_button = CreateButton(
            calendar_frame, "25", x_orient, y_orient, tab, month_counter)
        day_25_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_25_canvas.event_markers(month_counter, 25)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 29:
            y_orient = 500

        day_26_button = CreateButton(
            calendar_frame, "26", x_orient, y_orient, tab, month_counter)
        day_26_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_26_canvas.event_markers(month_counter, 26)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 29:
            y_orient = 500

        day_27_button = CreateButton(
            calendar_frame, "27", x_orient, y_orient, tab, month_counter)
        day_27_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_27_canvas.event_markers(month_counter, 27)

        counter += 1
        if x_orient == 660:
            x_orient = 60
        else:
            x_orient = x_orient+100
        if counter >= 29:
            y_orient = 500

        day_28_button = CreateButton(
            calendar_frame, "28", x_orient, y_orient, tab, month_counter)
        day_28_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
        day_28_canvas.event_markers(month_counter, 28)

        if int(date_dict['DaysInViewedMonth']) >= 29:
            counter += 1
            if x_orient == 660:
                x_orient = 60
            else:
                x_orient = x_orient+100
            if counter >= 29:
                y_orient = 500

            day_29_button = CreateButton(
                calendar_frame, "29", x_orient, y_orient, tab, month_counter)
            day_29_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
            day_29_canvas.event_markers(month_counter, 29)

        if int(date_dict['DaysInViewedMonth']) >= 30:
            counter += 1
            if x_orient == 660:
                x_orient = 60
            else:
                x_orient = x_orient+100
            if counter >= 36:
                y_orient = 600

            day_30_button = CreateButton(
                calendar_frame, "30", x_orient, y_orient, tab, month_counter)
            day_30_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
            day_30_canvas.event_markers(month_counter, 30)

        if int(date_dict['DaysInViewedMonth']) >= 31:
            counter += 1
            if x_orient == 660:
                x_orient = 60
            else:
                x_orient = x_orient+100
            if counter >= 36:
                y_orient = 600

            day_31_button = CreateButton(
                calendar_frame, "31", x_orient, y_orient, tab, month_counter)
            day_31_canvas = CreateCanvas(calendar_frame, x_orient, y_orient)
            day_31_canvas.event_markers(month_counter, 31)
            counter += 1


class CreateCanvas():
    """
    creates canvas next to day-buttons, later displays on them ovals
    of different colours to indicate events
    """
    HEIGHT = 85
    WIDTH = 25
    LOWER_X = 20
    LOWER_Y = 10

    def __init__(self, calendar_frame, x_orient, y_orient):

        self.canvas = tk.Canvas(
            calendar_frame, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.place(x=x_orient-self.LOWER_X, y=y_orient-self.LOWER_Y)

    def event_markers(self, month_counter, day):
        """
        one oval per one TYPE of event, max being 6
        """
        date_dict = get_date.get(month_counter)

        event_types = process_calendar_data.event_types_per_day(
            str(date_dict['ViewedYear']) + "/" + str(date_dict['ViewedMonth'])
            + "/" + str(day))
        y_1 = 2
        y_2 = 12
        counter = event_types["SUM"]
        while counter != 0:
            if event_types["PREGNANCY"] == 1:
                self.canvas.create_oval(5, y_1, 15, y_2, fill="hot pink")
                event_types["PREGNANCY"] = 0
            elif event_types["MEDICINE"] == 1:
                self.canvas.create_oval(5, y_1, 15, y_2, fill="blue")
                event_types["MEDICINE"] = 0
            elif event_types["MILKING"] == 1:
                self.canvas.create_oval(5, y_1, 15, y_2, fill="yellow")
                event_types["MILKING"] = 0
            elif event_types["OTHER"] == 1:
                self.canvas.create_oval(5, y_1, 15, y_2, fill="green2")
                event_types["OTHER"] = 0
            elif event_types["DELIVERY"] == 1:
                self.canvas.create_oval(5, y_1, 15, y_2, fill="red")
                event_types["DELIVERY"] = 0
            elif event_types["WITHDRAWAL"] == 1:
                self.canvas.create_oval(5, y_1, 15, y_2, fill="black")
                event_types["WITHDRAWAL"] = 0
            y_1 += 12
            y_2 += 12
            counter -= 1

class CreateButton():
    """creates buttons that serve as calendar days"""

    HEIGHT = 1
    WIDTH = 3
    RELIEF = tk.FLAT
    FOCUS = 0
    FONT = "Helvetica 25"

    def __init__(self, parent, text, x_orient, y_orient, tab, month_counter):

        self.month_counter = month_counter
        date_dict = get_date.get(month_counter)

        day = int(text)

        button = tk.Button(
            parent, text=text, height=self.HEIGHT, width=self.WIDTH,
            font=self.FONT, relief=self.RELIEF, takefocus=self.FOCUS,
            command=lambda: single_day_view.add_event_window(
                month_counter, day, tab))

        if date_dict['ViewedDay'] == day:
            button.configure(bg="#ffffff")

        button.place(x=x_orient, y=y_orient)
