# Anki Addon: Ignore Dupes

**[Overview over my other Anki add-ons](http://www.lieret.net/opensource/#anki)**

Plugin for [Anki](https://apps.ankiweb.net/), a spaced repetition flashcard program. [Plugin page on akiweb.](https://ankiweb.net/shared/info/1919904593)

## Duplicates in Anki

By default Anki checks for duplicates as follows (see the [anki manual](https://apps.ankiweb.net/docs/manual.html#adding-cards-and-notes)).


> Anki checks the first field for uniqueness, so it will warn you if you enter two cards with a Front field of “apple” (for example). The uniqueness check is limited to the current note type, so if you’re studying multiple languages, two cards with the same Front would not be listed as duplicates as long as you had a different note type for each language.
> Anki doesn’t check for duplicates in other fields automatically for efficiency reasons, but the browser has a “Find Duplicates” function which you can run periodically.

While this functionality usually is very handy, there are a few cases where some tweeks are nescessary: For example one might want to have more than one source deck (e.g. imported from anki web), all of which use the same note type. In this case every word that appears in more than one source deck would be flagged, as well as any words that I added to my normal review deck which appear in one other source deck. 
This is of course undesirable. 

With this addon the function that checks for duplicates can be tweaked to ignore dupliates based on the decks they belong to. E.g. one could ignore all duplicates where at least one card belongs to a deck with "DUPLICATE" in the name.

## Installation 

1. **Via the Anki interface** (this might not be the newest version!) Main Window: ```Tools``` → ```Addons``` → ```Browse & Install...```, then enter the code ```1919904593``` in the pop up window.

   ![anki interface](https://cloud.githubusercontent.com/assets/13602468/24506940/6d3a1d42-155f-11e7-8d7c-fd99f074953f.png)

2. **Manually**. Click here [here](https://github.com/klieret/anki-ignore-dupes/archive/master.zip) to download the newest version of this addon as a ZIP file, then move the contents of the ZIP folder (the file ```ignore_dupes.py``` and the folder ```ignore_dupes_files```) to the ```addon``` subfolder of your Anki directory. 

   E.g. Linux: ```~/Documents/Anki/addons```, Windows ```<path to your account>/Documents/Anki/addons```.

## Uninstallation

1. **Via the Anki interface**. Main Window: ```Tools``` → ```Addons``` → ```ignore_dupes``` → ```Delete```.

   ![anki interface](https://cloud.githubusercontent.com/assets/13602468/24505076/e39723ce-1558-11e7-9f3c-e379f6321a55.png)

2. **Manually**: Delete the file ```ignore_dupes.py``` and the folder ```ignore_dupes_files``` from your addon folder.

## The Log

For debugging purposes, this addon generates a log in the folder ```ignore_dupes_files``` (which you just moved into the addon folder), called ```ignore_dupes.log```. 

If the logging level is set to ```DEBUG```, the contents look something like this:

    IgnoreDupes:INFO:Plugin 'ignore_dupes' active. Some duplicated card warnings may be surpressed.
    IgnoreDupes:DEBUG:Log will be saved at /home/fuchur/Documents/Anki/addons/ignore_dupes_files/ignore_dupes.log
    IgnoreDupes:DEBUG:key field = '<span class="Apple-tab-span" style="white-space:pre"> </span>一般的に言って'
    IgnoreDupes:DEBUG:other_note_ids: []
    IgnoreDupes:DEBUG:Did not find any notes with the same key field checksum as self.
    IgnoreDupes:DEBUG:key field = 'test'
    IgnoreDupes:DEBUG:other_note_ids: [1490874810822]
    IgnoreDupes:DEBUG:self_deck_ids [1411748665110]
    IgnoreDupes:DEBUG:other_deck_ids [1420378368951]
    IgnoreDupes:DEBUG:Duplicate! deck1 = 'JA::VOCAB', deck2 = 'JA::VOCAB::vocab_new' ==> Ignored.
    IgnoreDupes:DEBUG:key field = 'test'
    IgnoreDupes:DEBUG:other_note_ids: [1490874798315]
    IgnoreDupes:DEBUG:self_deck_ids [1420378368951]
    IgnoreDupes:DEBUG:other_deck_ids [1411748665110]
    IgnoreDupes:DEBUG:Duplicate! deck1 = 'JA::VOCAB::vocab_new', deck2 = 'JA::VOCAB' ==> Ignored.
    
If you run Anki from the command line, the first two lines will also always be displayed.

You can adjust the debug levels in the file ```log.py```. Available levels are ```DEBUG```, ```INFO```, ```WARNING```, ```ERROR``` and ```CRITICAL```. The relevant lines are:

```python
logger.setLevel(logging.INFO)     # which log messages are recorded at all
                                  # (overall log level)
sh_info.setLevel(logging.INFO)    # which log messages are displayed in the command line
sh_error.setLevel(logging.ERROR)  # which log messages cause anki to display 
                                  # a warning message
fh.setLevel(logging.DEBUG)        # which log messages are written to the log file
```

by default the overall logging level is set to ```INFO```, not ```DEBUG``` as this performs etter. Thus, for more detailed information, simply replace the line ```logger.setLevel(logging.INFO)``` with ```logger.setLevel(logging.DEBUG)``` and the log file will contain all debug information.

## Customization

Done in the file ```config.py``` of the folder ```ignore_dupes_files```:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from examples import *

(...)

ignore_duplicates = ignore_nothing
```

the last line sets the function which determines which duplicates are ignored and which are flagged. 

There are a lot of examplary functions in the file ```examples.py```.
An easy example can look like this:
    
```python
def ignore_same_deck(deck1, deck2):

    if deck1 == deck2:
        return False
    else:
        return True
```

to load this function (which ignores all duplicates which belong to different decks), simply set

```python
ignore_duplicates = ignore_same_deck
```
    
in the file ```config.py```.

## License

The contents of this repository are licensed under the [*AGPL3* license](https://choosealicense.com/licenses/agpl-3.0/) (to be compatible with the license of Anki and its addons as detailed [here](https://ankiweb.net/account/terms)).
