#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def repeater():
    '''Print the output message with target language e chosen word to translate.'''

    target_lang = input('''Type "en" if you want to translate from French into English,
or "fr" if you want to translate from English into French:
''')
    chosen_word = input('''Type the word you want to translate:
''')

    print(f'You chose "{target_lang}" as a language to translate "{chosen_word}"')
    return target_lang, chosen_word


def welcome_message():
    '''Print the welcome message.'''

    print('''Hello, you're welcome to the translator. Translator supports:
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish''')
    from_lang = define_lang(int(input('''Type the number of your language:
''')))
    to_lang = define_lang(int(input('''Type the number of language you want to translate to or '0' to translate to all languages:
''')))
    chosen_word = input('''Type the word you want to translate:
''')
    return from_lang, to_lang, chosen_word


def define_lang(num):
    languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese',
                 'dutch', 'polish', 'portuguese', 'romanian', 'russian', 'turkish', 'all']
    if type(num) == int:
        try:
            if num < 0 or num > 13:
                raise IndexError("Insert a number between 0 and 13")
        except IndexError as err:
            print("Insert a number between 0 and 13")
        except TypeError:
            print("Insert a number between 0 and 13")
        else:
            if num == 0:
                languages.remove('all')
                return languages
            else:
                lang = [languages[num - 1]]
                return lang
    else:
        try:
            if num not in languages:
                raise ValueError(f"Sorry, the program doesn't support {num}")
        except ValueError:
            print(f"Sorry, the program doesn't support {num}")
        else:
            if num == 'all':
                languages.remove('all')
                return languages
            else:
                return [num]


def make_request(target_lang, chosen_word, src_lang=None):
    '''Make requests for translations over internet.'''
    if src_lang is None:
        if target_lang == 'en':
            from_lang = 'french'
            to_lang = 'english'
        else:
            from_lang = 'english'
            to_lang = 'french'
    else:
        from_lang = src_lang
        to_lang = target_lang

    url = 'https://context.reverso.net/translation/' + from_lang + '-' + to_lang + '/' + chosen_word
    request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        if request.status_code == 404:
            raise ValueError(f"Sorry, unable to find {chosen_word}")
    except ValueError:
        print(f"Sorry, unable to find {chosen_word}")
    except requests.ConnectionError:
        print("Something wrong with your internet connection")
    else:
        return from_lang, to_lang, request


def translate(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    words = [a.text.strip() for a in soup.find('div', {'id': 'translations-content'}).find_all('a')]
    try:
        if words is None:
            raise ValueError(f"Sorry, unable to find {r.url.split('/')[-1]}")
    except ValueError:
        print(f"Sorry, unable to find {r.url.split('/')[-1]}")
    else:
        sentences = []
        examples = soup.find_all('div', {'class': 'example'})
        for example in examples:
            division = example.find_all('div')
            for div in division:
                if 'src' in div.get('class'):
                    sentences.append(div.text.strip())
                if 'trg' in div.get('class'):
                    sentences.append(div.text.strip())
        return words, sentences


def print_translations(to_lang, words, sentences):
    print(f'{to_lang.title()} Translations')
    print(words[0])
    # if len(words) > 5:
    #     for i in range(5):
    #         print(words[i])
    # else:
    #     for word in words:
    #         print(word)
    print(f'{to_lang.title()} Examples')
    print(sentences[0])
    print(sentences[1])
    # if len(sentences) > 5:
    #     for i in range(5):
    #         print(sentences[i])
    #         print(sentences[i + 1])
    #         print()


def write_translations(lang, chosen_word, words, sentences):
    with open(f'{chosen_word}.txt', mode='a', encoding='utf-8') as file:
        file.write(f'{lang.title()} Translations' + '\n')
        file.write(words[0] + '\n')
        file.write(f'{lang.title()} Examples' + '\n')
        file.write(sentences[0] + '\n')
        file.write(sentences[1] + '\n')
