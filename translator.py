#!/usr/bin/env python3
from repeater import repeater, make_request, translate, \
    print_translations, welcome_message, define_lang, write_translations
import sys


# target_lang, chosen_word = repeater()

# from_lang, to_lang, chosen_word = welcome_message()

args = sys.argv
from_lang = define_lang(args[1])
to_lang = define_lang(args[2])
chosen_word = args[3]
if to_lang is not None:
    for lang in to_lang:
        if lang != from_lang[0]:
            if make_request(lang, chosen_word, from_lang[0]) is not None:
                src_lang, trg_lang, r = make_request(lang, chosen_word, from_lang[0])
                words, sentences = translate(r)
                print_translations(trg_lang, words, sentences)
                write_translations(lang, chosen_word, words, sentences)
