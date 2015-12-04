#!/usr/bin/env python

from anki.notes import Note
from anki.utils import fieldChecksum, splitFields, stripHTMLMedia
from aqt import mw

def deck_condition(deck1, deck2):
	""" Having 2 cards from deck1 and deck2 which have the same
	first field (i.e. would normally be flagged as a duplicate), 
	this function should be modified as to return True only when 
	we want to consider this as a duplicate and False if we want to
	"overlook" this duplicate."""

	noDupeDecks = ["SOURCES::japanese_kanji_system","SOURCES::Japanisch im Sauseschritt source", "SOURCES::RTK2_Public_source", "VOCAB::vocab_system"]
	noDupeDeckIds = [self.col.decks.id(deck) for deck in noDupeDecks]

def did_from_dname(deck_name):
	""" Return the deck name for the deck with the id $deck_id """
	return mw.col.decks.id(deck_id)

def dname_from_did(deck_id):
	""" Return the deck id for the deck with the name $deck_name """
	return mw.col.decks.get(did)["name"]

	# maybe use self.col.decks.get(did)[

	# dynamic decks are e.g. filtered decks etc.
	# dids = [id for id in self.decks.allIds() if not self.decks.isDyn(id)]
	# print dir(self.col.decks.get(did))
	#dids = self.decks.allIds()


def ignoreDupes(self):
	"""We will override Anki's Note.dupeOrEmpty function with this function.
	(So self is an object of type Note)
	It is meant to return
		1 		if self.fields[0] is empty
		2 		if the note is a duplicate
		False 	elsewise (i.e. "nice" note).
	"""
	
	noDupeDecks = ["SOURCES::japanese_kanji_system","SOURCES::Japanisch im Sauseschritt source", "SOURCES::RTK2_Public_source", "VOCAB::vocab_system"]
	noDupeDeckIds = [self.col.decks.id(deck) for deck in noDupeDecks]

	for deck, did in zip(noDupeDecks,noDupeDeckIds):
		print(deck,did)
		print(self.col.decks.get(did)["name"], did)
	print(dir(self.col.decks.get(noDupeDeckIds[0])))
	print(self.col.decks.get(noDupeDeckIds[0]).keys())


	return False



	# val = self.fields[0]
	# if not val.strip():
	# 	return 1
	# csum = fieldChecksum(val)
	
	# # get all note ids with matching checksums
	# nids = self.col.db.list("select id from notes where csum = ? and id != ? and mid = ?",csum, self.id or 0, self.mid)
	# for nid in nids:
	# 	# get fields
	# 	flds = self.col.db.list("select flds from notes where id = ?",nid)
	# 	# get deck id (saved in table cards, not table notes)
	# 	did = self.col.db.list("select did from cards where nid = ?",nid)
	# 	if flds == [] or did == []:
	# 		# then clearly there are no duplicates
	# 		return False
	# 	# If Expression matches and deck id not in noDupeDeckIds it's a real duplicate 
	# 	if stripHTMLMedia(splitFields(flds[0])[0]) == stripHTMLMedia(self.fields[0]) and did[0] not in noDupeDeckIds:
	# 		return 2 
	return False

Note.dupeOrEmpty=ignoreDupes
