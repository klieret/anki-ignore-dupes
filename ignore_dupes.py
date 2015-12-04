#!/usr/bin/env python

from anki.notes import Note
from anki.utils import fieldChecksum, splitFields, stripHTMLMedia
# from aqt import mw # mw.col should be the collection, so we don't need it as an argument anymore

def deck_condition(deck1, deck2):
	""" """

def ignoreDupes(self):
	"1 if first is empty; 2 if first is a duplicate, False otherwise."
	
	noDupeDecks = ["SOURCES::japanese_kanji_system","SOURCES::Japanisch im Sauseschritt source", "SOURCES::RTK2_Public_source", "VOCAB::vocab_system"]
	noDupeDeckIds = [self.col.decks.id(deck) for deck in noDupeDecks]
	
	val = self.fields[0]
	if not val.strip():
		return 1
	csum = fieldChecksum(val)
	
	# get all note ids with matching checksums
	nids=self.col.db.list("select id from notes where csum = ? and id != ? and mid = ?",csum, self.id or 0, self.mid)
	for nid in nids:
		# get fields
		flds=self.col.db.list("select flds from notes where id = ?",nid)
		# get deck id (saved in table cards, not table notes)
		did=self.col.db.list("select did from cards where nid = ?",nid)
		if flds==[] or did==[]:
			# then clearly there are no duplicates
			return False
		# If Expression matches and deck id not in noDupeDeckIds it's a reall duplicate 
		if stripHTMLMedia(splitFields(flds[0])[0]) == stripHTMLMedia(self.fields[0]) and did[0] not in noDupeDeckIds:
			return 2 
	return False

Note.dupeOrEmpty=ignoreDupes
