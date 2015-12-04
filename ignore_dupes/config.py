#!/usr/bin/env python
# -*- coding: utf-8 -*-

ignore_duplicates = ignore_duplicates1

def ignore_duplicates1(deck1, deck2):
    """ Having 2 cards from deck1 (original deck) and deck2 
    (deck of a note which normally would be flagged as a duplicate) 
    this function should be modified to return True if we want to ignore 
    this duplicate and False if we want to flag the duplicate. """

    noDupeDecks = [ "SOURCES::japanese_kanji_system",
                    "SOURCES::Japanisch im Sauseschritt source", 
                    "SOURCES::RTK2_Public_source", 
                    "VOCAB::vocab_system"]
    
    if deck2 in noDupeDecks:
        return False
    else:
        return True