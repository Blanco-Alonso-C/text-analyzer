import data.dictionaries as dicts
import data.parameters as param
from utils.sorting_cleaning_functions import clean_str

def preprocess(text:str) -> str:

    # We want the text to end with a dot.
    text.strip()

    if text[-1] != '.':
        text += '.'

    # We just care about the number of '\f'
    # But we can't say number of pages == number of '\f'
    text = text.replace('\f', '\n')

    # We just care about the number of '\t'
    # But we need just one paragraph divider
    text = text.replace('\t', '\n')

    # To avoid trolls this str is a special reserved mark for floating analysis
    text = text.replace('controlfloatmark', '.')

    param.raw_words = text.count(' ') + 1
    param.length = len(text)

    return text

def language_processing(
        text: str
) -> str:

    # We replace it here because that '.' must be removed ('n.º' is not formal)
    param.spanish_like += text.count('n.º')
    param.spanish_like += text.count('nº')
    param.spanish_like += text.count('º')
    param.spanish_like += text.count('ª')
    text = text.replace('n.º', 'número')
    text = text.replace('nº', 'número')
    text = text.replace('º', '')
    text = text.replace('ª', '')

    explicit_words_sp = ['coño', 'polla', 'puta', 'mamada', 'orgía', 'follar', 'joder', 'cachondo']
    explicit_words_en = ['dick', 'cunt', 'fuck', 'horny', 'whore', 'cock', 'pussy', 'blowjob', 'gangbang', 'jerk']

    offensive_words_sp = ['subnormal', 'imbécil', 'imbecil', 'gilipollas', 'mierda', 'idiota', 'cabrón', 'cabrona']
    offensive_words_en = ['retarded', 'bitch', 'slut', 'incel', 'nigger', 'nigga', 'fucking', 'asshole', 'moron',
                          'bastard', 'dumbass', 'shit', 'bullshit']

    formal_exceptions_sp = ['Sr.', 'Sra.', 'Srta.', 'Dr.', 'Dra.', 'Ud.', 'Uds.']
    formal_exceptions_en = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.', 'i.e.', 'e.g.']
    substitution_sp = ['señor', 'señora', 'señorita', 'doctor', 'doctora', 'usted', 'ustedes']
    substitution_en = ['mister', 'missus', 'miz', 'doctor', 'professor', 'that is', 'for example']

    # We will treat 'd as would. We are working on 's detection
    contraction_en = ['\'re', '\'m', '\'ve', '\'ll', 'n\'t', '\'d']
    equivalent = [' are', ' am', ' have', ' will', ' not', ' would']

    # This works with exceptions and special words
    for word in explicit_words_sp:
        param.spanish_like += text.count(word)
        param.explicit += text.count(word)

    for word in explicit_words_en:
        param.english_like += text.count(word)
        param.explicit += text.count(word)

    for word in offensive_words_sp:
        param.spanish_like += text.count(word)
        param.offensive += text.count(word)

    for word in offensive_words_en:
        param.english_like += text.count(word)
        param.offensive += text.count(word)

    for i, exception in enumerate(formal_exceptions_en):
        param.english_like += text.count(exception)
        param.formal += text.count(exception)
        text = text.replace(exception, substitution_en[i])

    for i, exception in enumerate(formal_exceptions_sp):
        param.spanish_like += text.count(exception)
        param.formal += text.count(exception)
        text = text.replace(exception, substitution_sp[i])

    for i, contraction in enumerate(contraction_en):
        param.english_like += text.count(contraction)
        param.formal -= text.count(contraction)
        text = text.replace(contraction, equivalent[i])

    if text.count('?') > text.count('¿'):

        param.english_like += text.count('?') * 0.2

    elif text.count('?') < text.count('¿'):

        param.rare += text.count('¿') - text.count('?')
        param.spanish_like += text.count('?') * 0.2

    else:

        param.formal += text.count('?') * 0.5
        param.spanish_like += text.count('?')

    if text.count('!') > text.count('¡'):

        param.english_like += text.count('!') * 0.2

    elif text.count('!') < text.count('¡'):

        param.rare += text.count('¡') - text.count('!')
        param.spanish_like += text.count('!') * 0.2

    else:

        param.formal += text.count('!') * 0.5
        param.spanish_like += text.count('¡')

    dicts.dictionary_symbols['?'] = text.count('?')
    dicts.dictionary_symbols['!'] = text.count('!')

    # We are working on this. This could cause errors and ellipsis.
    text.replace('?', '.')
    text.replace('!', '.')

    return text

def core_dictionary_filling(text:str) -> str:

    # Now we start to fill those dictionaries
    paragraphs = text.split('\n')
    clean_str(paragraphs, '')

    sentences = []
    for i, paragraph in enumerate(paragraphs, start=1):

        if paragraph.count('...') > 0:
            dicts.dictionary_symbols['ellipsis'] = paragraph.count('...')
            paragraph = paragraph.replace('...', '.')

        # My controlfloatmark avoid floats for being analized as different numbers
        result = []

        for j, ch in enumerate(paragraph):
            if (ch == '.' and j > 0 and j < len(paragraph) - 1 and paragraph[j - 1].isdigit() and paragraph[
                j + 1].isdigit()):
                result.append('controlfloatmark')
            else:
                result.append(ch)

        paragraph = ''.join(result)

        new_sentences = paragraph.split('.')

        # This will happen if the person did not write '.', '...' or ':'
        # At the end of the paragraph.
        # Yes, ':' does not end a sentence, but in this program ':\n' will
        if new_sentences[-1] != '' and new_sentences[-1][-1] != ':':
            param.errors += 1

        clean_str(new_sentences, '')

        words_in_paragraph = 1 + paragraph.count(' ')

        dicts.dictionary_paragraph[f'Paragraph number {i}'] = f'{words_in_paragraph} word'
        if words_in_paragraph > 1:
            dicts.dictionary_paragraph[f'Paragraph number {i}'] += 's'

        sentences += new_sentences

    words = []
    for i, sentence in enumerate(sentences, start=1):

        # This will happen if the person misclicked whitespace twice or more
        if '  ' in sentence:
            param.errors += 1

        new_words = sentence.split()

        # No need to clean because split removes all whitespaces
        dicts.dictionary_sentence[f'Sentence number {i}'] = f'{len(new_words)} word'
        if len(new_words) > 1:
            dicts.dictionary_sentence[f'Sentence number {i}'] += 's'

        words += new_words

    for word in words:

        # My controlfloatmark avoid floats for being analized as different numbers
        word = word.replace('controlfloatmark', '.')

        for i, character in enumerate(word):

            # This is for real numbers to be counted
            if character == '.':
                if word.replace('.', '').isnumeric():
                    if word not in dicts.dictionary_numbers.keys():
                        dicts.dictionary_numbers[word] = 1
                    else:
                        dicts.dictionary_numbers[word] += 1
                else:
                    word = word.replace('.', ',')

            # We wait to remove symbols because we want '78&34' to be computed as
            # 78 as number and 34 as different number, not 7834

            # This is just counting different letters and adding points if in the Spanish alphabeth
            # We have to count letters here because of the alphanumeric words
            if character.isalpha():
                if character.lower() == 'ñ':
                    param.spanish_like += 5
                if character.lower() in 'áéíóúü':
                    param.spanish_like += 1
                    if character.lower() not in dicts.dictionary_alpha_symbol.keys():
                        dicts.dictionary_alpha_symbol[character.lower()] = 1
                    else:
                        dicts.dictionary_alpha_symbol[character.lower()] += 1
                else:
                    if character.lower() not in dicts.dictionary_alpha.keys():
                        dicts.dictionary_alpha[character.lower()] = 1
                    else:
                        dicts.dictionary_alpha[character.lower()] += 1

            # This program cares about numbers of multiple digits
            if character.isnumeric() and (i == 0 or not word[i - 1].isnumeric()):
                number = ''
                for j in range(i, len(word)):

                    if word[j].isnumeric():
                        number += word[j]

                    # This is because if we find a '.', that number counted as float already
                    elif word[j] == '.':
                        number = ''
                        break

                    else:
                        break

                if len(number) > 0:
                    if number not in dicts.dictionary_numbers.keys():
                        dicts.dictionary_numbers[number] = 1
                    else:
                        dicts.dictionary_numbers[number] += 1

            if character != '.' and not character.isnumeric() and not character.isalpha():

                if character not in dicts.dictionary_symbols.keys():
                    dicts.dictionary_symbols[character] = 1
                else:
                    dicts.dictionary_symbols[character] += 1

                param.rare += 0.001

                # Now we will remove the character because words does not contain symbols
                # The whitespace is key, because we will consider a word for dictionary
                # Only one that has characters only at the beginning or at the end
                # However in the 'number of words' they will appear
                word = word.replace(character, ' ')

        # This way (tomato) or you! will be tomato and you: actual words (for dictionary)
        # But t0m4t0 or p¡nk will not. They will count as words typed, not dictionary ones
        word = word.strip()

        if word.isalpha():
            # We want to know if is a proper noun.
            # If there is only one instance of a word and it is not a proper noun
            # But it is at the beggining of a sentence, this function asumes is a proper noun
            # We are working on that
            if word[0].isupper() and word[1:].islower() and word.lower() not in words:
                if word not in dicts.dictionary_nouns.keys():
                    dicts.dictionary_nouns[word] = 1
                else:
                    dicts.dictionary_nouns[word] += 1

            else:
                if word.lower() not in dicts.dictionary_words.keys():
                    dicts.dictionary_words[word.lower()] = 1
                else:
                    dicts.dictionary_words[word.lower()] += 1

    param.lensentences  = len(sentences)

    return text