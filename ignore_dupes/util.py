#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aqt import mw


def did_from_dname(deck_name):
    """ Return the deck id for the deck with the name $deck_name
    :type deck_name: str
    """
    return mw.col.decks.id(deck_name)


def dname_from_did(deck_id):
    """ Return the deck name for the deck with the id $deck_name
    :type deck_id: int"""
    return mw.col.decks.get(deck_id)["name"]


def split_multiple_delims(string, delims):
    """ Like the string.split(...) method, but with
    multiple delimeters.
    See http://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters """
    string = unicode(string)
    for delim in delims:
        string = string.replace(delim, delims[0])
    return string.split(delims[0])
