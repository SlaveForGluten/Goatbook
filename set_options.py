"""change settings """

# !/usr/bin/python
# -*- coding: utf-8 -*-


class Options():
    """
    gets a raw text from language file in __init__,
    work on it in get_text_dict method
    """
    def __init__(self):
        """
        read one of the language files, it depends on currently set language
        (2nd line in Settings.text)
        """
        try:
            container = open("Settings.txt", "r")
            content = container.readlines()
            container.close()
        except IOError:
            container.close()

        lang = content[1].split(":")
        lang = lang[1].strip()

        try:
            container = open(lang + ".txt", "r")
            self.content = container.readlines()
            container.close()
        except IOError:
            container.close()

    def get_text_dict(self, module_text):
        """
        refines language text file: takes text for module that is needed
        then returns dictionary with key being widget name and value-text
        """
        self.widget_text_dictionary = {}
        for line in self.content:
            if line.split(":")[0] == module_text:
                self.widget_text_dictionary[
                    (line.split(":")[1])] = (line.split(":")[2].rstrip("\n"))


def set_language(language):
    """changes 2nd line of Settings.txt and with it language"""
    try:
        container = open("Settings.txt", "r")
        content = container.readlines()
        container.close()
    except IOError:
        container.close()

    try:
        container = open("Settings.txt", "w")
        container.write(content[0])
        container.write("LANGUAGE:"+language)
        container.close()
        return "success"
    except IOError:
        container.close()


def available_languages():
    """
    reads available languages from 1st line of Settings.text
    to be displayed as choice in Options menu
    """

    try:
        container = open("Settings.txt", "r")
        content = container.readlines()
        container.close()
    except IOError:
        container.close()

    languages_list = content[0].strip("available_languages:").split(",")
    languages_tuple = (languages_list)
    return languages_tuple
