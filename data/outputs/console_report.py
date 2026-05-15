
import data.parameters as param

def report():

    AI_percentage = param.AI_like * 100 / (param.AI_like + param.humanlike)
    sp_score = param.spanish_like * 100 / (param.spanish_like + param.english_like)
    en_score = param.english_like * 100 / (param.spanish_like + param.english_like)

    # Yes this is arbitrary
    formal_ppt = param.formal * 3000 / param.length
    rare_ppt = param.rare * 1000 / param.length

    print('\n\n')
    print('------------------------------------')
    print('Text analyzed')
    print()
    print(f'This text has {param.raw_words} words.')
    print(f'This text has {param.lensentences} sentences.')
    print()
    print(f'There might be {param.errors} errors. Check it out.')
    print()
    print(f'We give you {formal_ppt:.2f} formal points')
    print(f'We give you {rare_ppt:.2f} weirdness points')
    print()
    print(f'We found {param.explicit} explicit words')
    print(f'We found {param.offensive} offensive words')
    print()
    print(f'AI score out of 100: {AI_percentage:.2f}')
    print(f'Spanish score out of 100: {sp_score:.2f}')
    print(f'English score out of 100: {en_score:.2f}')
    print('------------------------------------')
    print('\n\n')