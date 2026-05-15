import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import ticker
from pathlib import Path

import data.dictionaries as dicts

def plot_chart():
    base = Path(__file__).parent.parent
    save_path = base / 'data' / 'outputs' / 'plots'
    save_path.mkdir(parents=True, exist_ok=True)

    plt.style.use('seaborn-v0_8')
    palette = sns.color_palette('viridis')

    fig, axs = plt.subplots(2, 2, figsize=(14, 10), clear = True)

    all_letters = list(dicts.dictionary_alpha.items())
    if all_letters:
        letters, counts = zip(*all_letters)
        axs[0, 0].bar(letters, counts, color=palette[0])
    else:
        axs[0, 0].text(0.5, 0.5, 'No data',
                       ha='center', va='center')
    axs[0, 0].set_title('Letter frequencies')

    top_words = list(dicts.dictionary_words.items())[:10]
    if top_words:
        words, counts = zip(*top_words)
        axs[0, 1].barh(words, counts, color=palette[1])
        axs[0, 1].invert_yaxis()
    else:
        axs[0, 1].text(0.5, 0.5, 'No data',
                       ha='center', va='center')
    axs[0, 1].set_title('Top 10 most common words')

    top_numbers = list(dicts.dictionary_numbers.items())[:5]
    if top_numbers:
        numbers, counts = zip(*top_numbers)
        axs[1, 0].bar(numbers, counts, color=palette[2])
    else:
        axs[1, 0].text(0.5, 0.5, 'No numbers found',
                       ha='center', va='center')
    axs[1, 0].set_title('Top 5 most common numbers')

    top_symbols = list(dicts.dictionary_symbols.items())[:5]
    if top_symbols:
        symbols, counts = zip(*top_symbols)
        axs[1, 1].bar(symbols, counts, color=palette[3])
    else:
        axs[1, 1].text(0.5, 0.5, 'No symbols found',
                       ha='center', va='center')
    axs[1, 1].set_title('Top 5 most common symbols')


    for i, ax in enumerate(axs.flat):

        # For some reason, if we apply the function to the hbar, 50% of labels in y disappear
        if ax is axs[0, 1]:
            continue
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    plt.show()

    ans = input('Do you want to save the image in outputs? (y/n): ').strip().lower()

    if ans == 's' or ans == 'sí' or ans == 'yes' or ans == 'y' or ans == 'ok':
        name = input('Name of the image: ').strip()
        quality = input('Write h, m, l for high, medium or low quality: ').strip().lower()
        if quality == 'h' or quality == 'high':
            quality = 300
            str_q = 'high'

        elif quality == 'm' or quality == 'medium':
            quality = 150
            str_q = 'medium'

        elif quality == 'l' or quality == 'low':
            quality = 72
            str_q = 'low'

        else:
            print('Not a valid quality, quality will be set as medium')
            quality = 150
            str_q = 'medium'

        if not name.endswith('.png'):
            name += '.png'

        plt.savefig(save_path / name, dpi = quality)
        print('\n')
        print(f'Plot saved as {name} with {str_q} quality')

    else:
        print('\n')
        print('Plot not saved')
