#!/usr/bin/env python

from anki.notes import Note
from anki.utils import fieldChecksum, splitFields, stripHTMLMedia

def expressionDupe(col,exp):
	""" Returns True, if exp was already used as question on a
	card which does not belong to one of the decks from noDupeDecks.
	Otherwise returns False"""

	# TODO: look for duplicates in only one or only some decks
	# to be used by cbc Import
	# FIXME: multiple decks return 
	
	yesDupeDecks=["VOCAB::vocab_new", "VOCAB::vocab_saikin"]
	noDupeDecks = ["SOURCES::japanese_kanji_system","SOURCES::Japanisch im Sauseschritt source", "SOURCES::RTK2_Public_source", "VOCAB::vocabular_main", "VOCAB::vocab_system","KANJI::koohii","KANJI::koohii_reverse","KANJI::readings","KANJI::rtk2_split"]
	noDupeDeckIds = [col.decks.id(deck) for deck in noDupeDecks]
	yesDupeDeckIds= [col.decks.id(deck) for deck in yesDupeDecks]
	
	csum = fieldChecksum(exp)
	# get all note ids with matching checksums
	nids=col.db.list("select id from notes where csum = ?",csum)
	for nid in nids:
		# get fields
		flds=col.db.list("select flds from notes where id = ?",nid)
		# get deck id (saved in table cards, not table notes)
		did=col.db.list("select did from cards where nid = ?",nid)
		if flds==[] or did==[]:
			# then clearly there are no duplicates
			return False
		# If Expression matches and deck id not in noDupeDeckIds it's a reall duplicate 
		if len(did)>=2:
			print(did)
			try:
				print("More than one deck id for %s, that's strange" % exp)
			except:
				pass
		if stripHTMLMedia(splitFields(flds[0])[0]) == stripHTMLMedia(exp) and did[0] in yesDupeDeckIds and did[0] not in noDupeDeckIds:
			# get deck from nid:
			deckName=""	
			for i,g in col.decks.decks.items():
				if int(i)==int(did[0]):
					deckName=g['name']
					break
			try:
				print("%s is duplicate from deck %s" % (exp,deckName))
			
			except:
				pass
			return True
	
	return False

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
