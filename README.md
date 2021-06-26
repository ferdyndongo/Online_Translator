# Multilingual Online Translator
## About
This project is about writing an app that translates the words you type and gives you many
usage examples based on the context.
## Description
1. Repeater  
   At this stage, there'll be only two available languages: English and French. The program
   should suggest to the user to choose the direction of the translation, and the word to 
   translate. Then, the confirmation message should be printed.
2. Over the internet  
   At this stage, the goal is to find translations and example sentences for a given word 
   through [ReversoContext](https://context.reverso.net/translation/): a multilingual 
   translator tool that allows seeing original phrases that should be translated and their
   equivalents in other languages in contexts(example sentences).
3. Translations  
   Create a readable result: separate sentences and translations by newlines and put titles
   in front of different sections of the output.
4. Add more languages
   The maximum number of language the translator can support is 13. They are:  
   Arabic, German, English, Spanish, French, Hebrew, Japanese, Dutch, Polish, Portuguese,
   Romanian, Russian, Turkish.
5. Translate to all languages and write to the file
   Add the feature of translating the word to all languages at once, and also save the search
   results to a text file so that the user could read the translations later.
6. Faster translation  
   Add command-line arguments to make the process faster.
7. Handle an unexpected behavior
## Objectives
1. * Output the welcoming message: `Type "en" if you want to translate from French into
   english, or "fr" if you want to translate from English into French:`  
   * Take an input specifying the target language.
   * Output the message: `Type the word you want to translate:`
   * Output the confirmation message in the format `You choose "language" as a language to
     translate "word".`, where `language` is either `en` or `fr` and `word` is the word
     chosen by the user.  
2. * Form a request and connect to [ReversoContext](https://context.reverso.net/translation/)
   * Check the http status of the response of the website to your request.
   * Output the response of the website to your request (`200 OK`)
   * Output the line `Translations`.
   * Output a list with translations of the given word with the target language 
     `[bonjour, salut]`
     Output a list with examples of sentences featuring the given word or any of its
     translations: `['well, hello, freedom fighters.', 'Et bien, bonjour combattants de la
     liberté.']`
3. * Output the line `... Translations`; put the full name of the target language instead of
    `...` (for example, `English Translations`)
   * Output found translations, one per line. If there are more than 5 translations, leave
     only 5 of them to keep the results more compact.
   * Output the line `... Examples`; put the full name of the target language instead of
    `...` (for example, `English Examples`)
   * Output the found examples of sentences, one sentence per line: First output the sentence
     in the source language, then output its translation in the target language. Repeat this
     procedure for every found sentence pair. If there are more than 5 sentence pairs, leave
     only 5 of them.
4. * Output the welcoming message: `Hello, you're welcome to the translator. Translator
     supports:` and output the enumerated list of supported languages.
   * Take 3 inputs: the first specifying the source language, the second for target language,
    and the third for the word to be translated
5.  * Add the following functionality to the translator:
      * Specify the target language by output the message `Type the
        number of a language you want to translate to or '0' to translate to all languages:`
      * If the user inputs `0` as the target language, translate the word to all available
        languages.
        Save results of the search to a file named `word.txt`, where `word` is the world that
        was being translated.
6. Instead of all inputs, take command-line arguments: the first is the name of the source
language, the second the name of the target language and, the third the word. If the word
   should be translated to all languages, the second argument will be `all`.
7. Add the following functionality:
    * if the user inputs a name of a language that isn't available in the program, print the
    line `Sorry, the program doesn't support <language>` and quit the program.
    * If the connection with the website isn't successful, print the line `Something wrong 
      with your internet connection`
    * If the user inputs a word that's not present in 
      [ReversoContext](https://context.reverso.net/translation/), print the line `Sorry,
      unable to find <word>`