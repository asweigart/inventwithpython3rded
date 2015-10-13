inventwithpython3rded
=====================

Source text for "Invent Your Own Computer Games with Python, 3rd Edition" and repo for the translation efforts.

NOTE TO ALL TRANSLATORS: Don't hesitate to contact me if you have questions or want to know what to do next. al@inventwithpython.com

Why a 3rd Edition?
------------------

The 2nd edition came out in 2010 and was my first book. Since then, I've gained experience from writing three more books and teaching programming to kids and adults. The 3rd edition will not have new content (aside from the Appendixes, which previously were only online), but has two major aims:

1. Renewed copyediting efforts to make the text easier to read (especially for younger readers) and reduce the word count by 20%.

2. Translate the book into other languages through volunteer efforts.

If you've already read the 2nd edition, there won't be any new content that you'll miss out on. But for new readers, I'm hoping that the 3rd edition will be more approachable and less intimidating then the original 438-page 2nd edition.

I'm currently looking for volunteer translators of all experience levels to commit any amount of effort. Please contact me at al@inventwithpython.com.

License and Proceeds
--------------------

"Invent Your Own Computer Games with Python" was released with a Creative Commons BY-NC-SA license, making it freely available to download and distribute free of charge. The source code in the book is under an even more liberal Free BSD license. The 3rd edition book and code will be published under these licenses as well.

http://creativecommons.org/licenses/by-nc-sa/3.0/us/legalcode

http://opensource.org/licenses/BSD-2-Clause

As the copyright holder, I commercially sell "Invent with Python" on Amazon. I also plan on selling hard copies of the translations as well, however:

*All proceeds from sales of translated books of "Invent Your Own Computer Games with Python, 3rd Edition" will be donated to the Python Software Foundation.*

I make similar donations to the EFF, Tor Project, and Creative Commons nonprofits from sales of my other book, "Hacking Secret Ciphers with Python". I publicly post an accounting of these donations at http://inventwithpython.com/hacking/proceeds/

These proceeds will be published at https://github.com/asweigart/inventwithpython3rded/blob/master/proceeds.md

All translators will get attribution credit on the book cover, in the PDF, and on the website.

I appreciate the efforts of the translators to bring programming knowledge outside of the English-speaking world. I want them to know that I do not plan to personally profit off of their labor.

Scope of the Translation
------------------------

While a complete translation of the book would be nice, Invent Your Own Computer Games with Python is a behemoth. In retrospect, the book's size is quite intimidating for both readers and translators.

The translated books will be optionally abridged. The foreign language versions will only go up to and including the Bagels chapter, and then include the Pygame chapters afterwards. This cuts chapters 12 to 16 (about 100 pages!) of translation work that would need to be done.

The optional chapters are:

* Chapter 12 - Cartesian Coordinates
* Chapter 13 - Sonar
* Chapter 14 - Caesar Cipher
* Chapter 15 - Reversi
* Chapter 16 - AI Simulation

Once the abridged version is finished, it's up to the translation team if they want to translate the entire book. I see the later chapters as not having as much value-per-page, and many readers don't end up getting to them. I want to start with a conservative scope and not overburden volunteers.

There are no deadlines for translation projects. Feel free to work at your own pace, and I understand if other things come up in your life.

Suggested Guidelines for Translators
------------------------------------

First, thank you for helping with the translation of "Invent with Python". Here are some helpful guidelines:

1. Read and agree to the Contributor License Agreement. (I've copied the one used by NodeJS.) This is available at https://github.com/asweigart/inventwithpython3rded/blob/master/cla.md. You can agree by sending al@inventwithpython.com an email saying "I agree to the Invent with Python Contributor License Agreement". This is mostly a formality.

1. I've set up mailing list for translation teams. The Wiki has links: http://invent-with-python-translations.wikia.com/wiki/Invent_with_Python_Translations_Wiki

1. Look at the translations/<lang code>/README.md file to contact other translators working on your language.

1. Read this README.md file to note any special parts of the book that may need additional attention. Feel free to add to this file.

1. Translate the programs first. Do not change the order or position of the code, as that will require tedious updating of line numbers in the book. Long lines of code are fine. Consult (and update) the src/_ISSUES.txt file for any language-translation issues that come up.

1. To prevent overlapping work with other translators, use the Tasks page on the wiki for your language: http://invent-with-python-translations.wikia.com/wiki/Invent_with_Python_Translations_Wiki

1. Save the .py files of the programs with UTF-8 encoding. (This is the default encoding the Python 3 expects source files to be in.)

1. A note about the source code: There are a lot of places where the code could improve (I wrote it a long time ago and learned much since). But I'd like to keep the code frozen (aside from the text translations). I'm doing this in the English version so that those who bought the 2nd edition book can still use the website without confusion. But I'd also like to keep the English source code in sync with the foreign language source code as well.

1. Make notes of any cultural differences that would require more than just a straight translation to the translations/<lang code>/README.md file.

1. All of the files for a translation go into the translations/<lang code> folder. This includes the text files, figure image files, and source code .py files. (Look at the other folders to get an idea of the structure.) These text files will just hold the content. Formatting (such as bold text, different fonts, etc) will be done in Word at a later step. The text files just hold the textual content.

1. Add spaces to line up the columns for tables to make it obvious which text is in which cell.

1. Translations for text in the figure images can go in the <lang code>_chapterN.figures.txt file. Not all chapters have figures, and not all figures have text that needs to be translated.

Special Thanks
--------------

Here is an inevitably incomplete list of MUCH-APPRECIATED CONTRIBUTORS -- people who have submitted patches, reported bugs, added translations, helped answer newbie questions, and generally made Invent Your Own Computer Games with Python that much better:

**Dutch Translation:**

- Marjo Hanh

**Simplified Chinese Translation:**

- Beta Kuang https://github.com/beta

**French Translation:**

- David Fleury https://github.com/dfleury2

**Spanish Translation:**

- Alejandro Pernin https://github.com/aleperno
- Alfredo Carella https://github.com/alfredocarella

**Swedish Translation:**

- Christer Nilsson https://github.com/ChristerNilsson
- Mats Rörbecker https://github.com/matsrorbecker

**Indonesian Translation:**

- Ben Bernard https://github.com/bbn-bernard