#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import ignore_duplicates
from anki.utils import fieldChecksum, splitFields, stripHTMLMedia
from aqt import mw

def did_from_dname(deck_name):
	""" Return the deck name for the deck with the id $deck_id """
	return mw.col.decks.id(deck_id)

def dname_from_did(deck_id):
	""" Return the deck id for the deck with the name $deck_name """
	return mw.col.decks.get(did)["name"]


def ignore_dupes(self):
	"""We will override Anki's Note.dupeOrEmpty function with this function, 
	i.e. self is a Note object.
	This method is meant to return
		1 		if self.fields[0] is empty
		2 		if the note is a duplicate
		False 	elsewise (i.e. "nice" note).
	"""
	
	search_value = self.fields[0]
	if not search_value.strip():
		return 1
	csum = fieldChecksum(search_value)
	
	# get all note ids with matching checksum of the search/key field
	nids = self.col.db.list("select id from notes where csum = ? and id != ? and mid = ?", csum, self.id or 0, self.mid)
	
	# own deck ids
	dids1 = self.col.db.list("select did from cards where nid = ?", self.id)

	for nid in nids:
		
		# get the field values of note with note id $nid
		flds = self.col.db.list("select flds from notes where id = ?", nid)
		if flds == []:
			# note with no fields
			return False
		
		# get the deck ids of all the cards of the note with id $nid
		# (one note can have multiple cards in different decks)
		dids2 = self.col.db.list("select did from cards where nid = ?", nid)
		if dids2 == []:
			# we didn't find any cards with matching checksum
			return False
		
		if not stripHTMLMedia(splitFields(flds[0])[0]) == stripHTMLMedia(self.fields[0]):
			# different expression fields => not a duplicate
			return False

		# Normally a card would be flagged as a duplicate here, but we check
		# if we want to ignore the duplicates
		for did1 in dids1:
			for did2 in dids2:
				if not ignore_duplicates(dname_from_did(did1), dname_from_did(did2)):
					return 2
		
		return False

