#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import ignore_duplicates
from anki.utils import fieldChecksum, splitFields, stripHTMLMedia
from aqt import mw
from log import logger
from util import dname_from_did


def expression_dupe(expression):
    """ Checks if there is already a card with the Expresssion $expression.
    :type expression: str
    """
    # wrapper around _ignore_dupes
    return _ignore_dupes(self_expression=expression)


def ignore_dupes(note):
    # wrapper around _ignore_dupes
    return _ignore_dupes(self_note=note)


# parts of this should be moved to expression_dupe
def _ignore_dupes(self_note=None, self_expression=None):
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

    # Some explanation for abbreviations used in Anki:
    # * id: Note id (as variable belonging to a note)
    # * nid: Note id (as variable belonging to a card)
    # * did: Deck id
    # * mid: Model id

    # 1. Default values & Co.

    if not self_note and not self_expression:
        raise ValueError

    if self_note:
        self_search_value = self_note.fields[0]
        self_note_id = self_note.id
        self_note_mid = self_note.mid
    else:
        self_search_value = None
        self_note_id = None
        self_note_mid = None

    if self_expression:
        # Note: If self_note was given as well, self_search_value will be overwritten.
        self_search_value = self_expression

    # 2. Check if we have a key field/Expression

    logger.debug("key field = '%s'" % self_search_value)
    if not self_search_value.strip():
        logger.debug("Key field empty.")
        return 1

    # 3. Get Note Ids of notes that might be duplicates.

    csum = fieldChecksum(self_search_value)

    if self_note_mid:
        # we don't have to check for the note id, because it defaults to 0 in the search query
        # (mostly copied from anki's source).
        # Select all note ids from notes
        # 1. whose key field has the same check sum
        # 2. whose note id is different (i.e. we're excluding self_note)
        # 3. whose model id is the same
        other_note_ids = mw.col.db.list("select id from notes where csum = ? and id != ? and mid = ?", csum,
                                        self_note_id or 0, self_note_mid)
    else:
        # don't apply any criteria for note id and mid model id, just seach for the checksum.
        other_note_ids = mw.col.db.list("select id from notes where csum = ?", csum, self_note_id or 0, self_note_mid)

    if not other_note_ids:
        logger.debug("Did not find any notes with the same key field checksum as self.")
        return False

    # 4. get the deck ids from the decks the self card belonged to

    self_deck_ids = mw.col.db.list("select did from cards where nid = ?", self_note_id)
    if not self_deck_ids:
        # use the deck id of the currently active deck
        self_deck_ids = [mw.col.conf['curDeck']]

    # 5. Loop over the other_note_ids

    for other_note_id in other_note_ids:
        # 5a. Get the field values of note with other_note_id
        other_fields = mw.col.db.list("select flds from notes where id = ?", other_note_id)
        if not other_fields:
            # note with no fields
            logger.debug("No fields.")
            return False

        # 5b. Get the deck ids of all the cards of the note with other_note_id
        # (one note can have multiple cards in different decks)
        other_deck_ids = mw.col.db.list("select did from cards where nid = ?", other_note_id)
        if not other_deck_ids:
            logger.debug("No cards with matching checksum.")
            return False

        # 5c. Check that the key fields match.
        if not stripHTMLMedia(splitFields(other_fields[0])[0]) == stripHTMLMedia(self_search_value):
            logger.debug("Expressions didn't match after all.")
            return False

        # 6c. Check if we want to ignore that case.
        # Normally a card would be flagged as a duplicate here.
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
