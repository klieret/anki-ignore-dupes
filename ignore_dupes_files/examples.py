#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ignore_ch4noyu(deck1, deck2):
    """ Setup I'm using. """

    if "SOURCES" in deck2:
        return True     # ignore

    if not deck1 == deck2:
        return True     # ignore


def ignore_same_deck(deck1, deck2):
    """ Ignores duplicates from different decks. """

    if deck1 == deck2:
        return False    # flag
    else:
        return True     # ignore


def ignore_some_decks(deck1, deck2):
    """ Returns all duplicates from deck2 in a certain list of decks"""

    ignore_decks = [ "SOURCES::japanese_kanji_system",
                     "SOURCES::Japanisch im Sauseschritt source", 
                     "SOURCES::RTK2_Public_source", 
                     "VOCAB::vocab_system"]
    
    if deck2 in ignore_decks:
        return True     # ignore
    else:
        return False    # flag


def ignore_all(deck1, deck2):
    """ Setting ignore_duplicates to this function
    will cause Anki to completely ignore all duplicates. """
    return True     # ignore


def ignore_nothing(deck1, deck2):
    """ Setting ignore_duplicates to this function
    will cause Anki to completely ignore all duplicates. """
    return False     # ignore


def ignore_same_group(deck1, deck2):
    """ Ignore duplicates if they belong to decks which belong to a different
    deck group (i.e. card A belongs to deck deck::subdeck, card B belongs
    to deck other_deck::other_subdeck."""

    group1 = ""
    if "::" in deck1:
        group1 = deck1.split("::")[0]

    group2 = ""
    if "::" in deck1:
        group2 = deck1.split("::")[0]

    if group1 == group2:
        return False    # same group => do not ignore
    else:
        return False    # different group => ignore