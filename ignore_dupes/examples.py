#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ignore_duplicates1(deck1, deck2):
    """ Returns all duplicates from deck2 in a certain list of decks"""

    ignore_decks = [ "SOURCES::japanese_kanji_system",
                     "SOURCES::Japanisch im Sauseschritt source", 
                     "SOURCES::RTK2_Public_source", 
                     "VOCAB::vocab_system"]
    
    if deck2 in ignore_decks:
        return False
    else:
        return True

def ignore_all_duplicates(deck1, deck2):
    """ Setting ignore_duplicates to this function
    will cause Anki to completely ignore all duplicates. """
    return True

def flag_all_duplicates(deck1, deck2):
        """ Setting ignore_duplicates to this function
    will cause Anki to flag all duplicates (ignore no duplicates). """
    return False