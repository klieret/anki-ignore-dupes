#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import ignore_duplicates
from anki.utils import fieldChecksum, splitFields, stripHTMLMedia
from aqt import mw
from log import logger


def did_from_dname(deck_name):
    """ Return the deck id for the deck with the name $deck_name
    :type deck_name: str
    """
    return mw.col.decks.id(deck_name)


def dname_from_did(deck_id):
    """ Return the deck name for the deck with the id $deck_name
    :type deck_id: int"""
    return mw.col.decks.get(deck_id)["name"]


def expression_dupe(mw_, expression):
    """ Checks if there is already a card with the Expresssion $expression.
    :param mw_: Anki Main Window
    :type expression: str
    """
    # todo: implement
    return False


# parts of this should be moved to expression_dupe
def ignore_dupes(self_note):
    """We will override Anki's Note.dupeOrEmpty function with this function,
    This method is meant to return
        1 		if self.fields[0] is empty
        2 		if the note is a duplicate
        False 	elsewise (i.e. "nice" note).
    :param self_note: Anki note object.
    """
    # Nomenclature: We compare the note given as argument to other notes.
    # Everything that has to do with that initial note has the prefix 'self',
    # everything that has to do with one of the other notes has the prefix other.

    search_value = self_note.fields[0]
    logger.debug("key field = '%s'" % search_value)

    if not search_value.strip():
        logger.debug("Key field empty.")
        return 1

    # get the deck ids from the decks the self card belonged to
    self_deck_ids = self_note.col.db.list("select did from cards where nid = ?", self_note.id)
    if not self_deck_ids:
        # use the deck id of the currently active deck
        self_deck_ids = [self_note.col.conf['curDeck']]

    # get all note ids with matching checksum of the search/key field, same mid but other id
    csum = fieldChecksum(search_value)
    other_note_ids = self_note.col.db.list("select id from notes where csum = ? and id != ? and mid = ?", csum,
                                           self_note.id or 0, self_note.mid)
    if not other_note_ids:
        logger.debug("Did not find any notes with the same key field checksum as self.")
        return False

    for other_note_id in other_note_ids:
        # get the field values of note with note id other_nid
        other_fields = self_note.col.db.list("select flds from notes where id = ?", other_note_id)
        if not other_fields:
            # note with no fields
            logger.debug("No fields.")
            return False

        # get the deck ids of all the cards of the note with id $nid
        # (one note can have multiple cards in different decks)
        other_deck_ids = self_note.col.db.list("select did from cards where nid = ?", other_note_id)
        if not other_deck_ids:
            # we didn't find any cards with matching checksum
            logger.debug("No cards with matching checksum.")
            return False

        if not stripHTMLMedia(splitFields(other_fields[0])[0]) == stripHTMLMedia(self_note.fields[0]):
            # different expression fields => not a duplicate
            logger.debug("Expressions didn't match after all.")
            return False

        # Normally a card would be flagged as a duplicate here, but we check
        # if we want to ignore the duplicates
        for self_deck_id in self_deck_ids:
            for other_deck_id in other_deck_ids:
                self_name = dname_from_did(self_deck_id)
                other_name = dname_from_did(other_deck_id)
                if ignore_duplicates(self_name, other_name):
                    # don't do anything!
                    logger.debug("Duplicate! deck1 = '%s', deck2 = '%s' ==> Ignored." % (self_name, other_name))
                else:
                    logger.debug("Duplicate! deck1 = '%s', deck2 = '%s' ==> Flagged." % (self_name, other_name))
                    return 2

        return False
