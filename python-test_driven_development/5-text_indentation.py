#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""
    for i in text:
        new += i
        if i in ".:?":
            print("{}".format(new.strip()), end="\n\n")
            new = ""

    if new.strip() != "":
        print("{}".format(new.strip()), end="")