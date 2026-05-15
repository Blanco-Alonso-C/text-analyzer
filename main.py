
from utils.sorting_cleaning_functions import alphabetical_number_order_keys, order_by_quantity_values
from statistic.stats_functions import calculate_statistic_parameters
from ia_checker.ia_checker_functions import ai_checker_stats, ai_checker_lexical_richness
from text_processing.processing_functions import preprocess, language_processing, core_dictionary_filling
from text_processing.open_file_functions import open_file
import data.dictionaries as dicts
import data.parameters as param
from data.outputs.console_report import report
from plots.plot_functions import plot_chart

def main():

    text = open_file()

    text = preprocess(text)

    text = language_processing(text)

    text = core_dictionary_filling(text)

    dicts.dictionary_alpha = alphabetical_number_order_keys(dicts.dictionary_alpha)
    dicts.dictionary_alpha_symbol = alphabetical_number_order_keys(dicts.dictionary_alpha_symbol)
    dicts.dictionary_nouns = alphabetical_number_order_keys(dicts.dictionary_nouns)
    dicts.dictionary_numbers = alphabetical_number_order_keys(dicts.dictionary_numbers)

    order_by_quantity_values(dicts.dictionary_words)
    order_by_quantity_values(dicts.dictionary_symbols)

    mean_wpp, std_wpp, rsd_wpp, mad_wpp, iqr_wpp = calculate_statistic_parameters(dicts.dictionary_paragraph)
    mean_wps, std_wps, rsd_wps, mad_wps, iqr_wps = calculate_statistic_parameters(dicts.dictionary_sentence)

    param.AI_like, param.humanlike, param.rare = ai_checker_stats(param.AI_like, param.humanlike, param.rare,
                                                                  mean_wpp, rsd_wpp, mad_wpp, iqr_wpp,
                                                                  mean_wps, rsd_wps, mad_wps, iqr_wps)

    param.AI_like, param.humanlike = ai_checker_lexical_richness(param.AI_like, param.humanlike, dicts.dictionary_words)

    report()
    plot_chart()

if __name__ == '__main__':
    main()

