import numpy as np


def ai_checker_stats(
        AI_like: float, humanlike: float, rare: float,
        mean_wpp: float, rsd_wpp: float, mad_wpp: float, iqr_wpp: float,
        mean_wps: float, rsd_wps: float, mad_wps: float, iqr_wps: float
):

    # These are arbitrary, and does not work at all, but it is our attempt
    # RSD in Words per Paragraph
    if rsd_wpp < 0.12:
        AI_like += 5

    elif 0.12 <= rsd_wpp < 0.2:
        AI_like += 3

    elif 0.2 <= rsd_wpp < 0.35:
        AI_like += 1

    elif 0.35 <= rsd_wpp < 0.55:
        humanlike += 0.1

    else:
        humanlike += 3

    # MAD/mean in Words per Paragraph
    if (mad_wpp / mean_wpp) < 0.08:
        AI_like += 3

    elif 0.08 <= (mad_wpp / mean_wpp) < 0.16:
        AI_like += 1

    elif 0.16 <= (mad_wpp / mean_wpp) < 0.30:
        AI_like += 0.5
        humanlike += 0.5

    elif 0.30 <= (mad_wpp / mean_wpp) < 0.45:
        humanlike += 1

    else:
        humanlike += 3
        rare += 0.1

    # IQR/mean in Words per Paragraph
    if (iqr_wpp / mean_wpp) < 0.1:
        AI_like += 3

    elif 0.1 <= (iqr_wpp / mean_wpp) < 0.18:
        AI_like += 1

    elif 0.18 <= (iqr_wpp / mean_wpp) < 0.35:

        AI_like += 0.5
        humanlike += 0.5

    elif 0.35 <= (iqr_wpp / mean_wpp) < 0.50:
        humanlike += 1

    else:
        humanlike += 3
        rare += 0.1

    # RSD in Words per Sentence
    if rsd_wps < 0.18:
        AI_like += 0.3

    elif 0.18 <= rsd_wps < 0.28:
        AI_like += 0.1

    elif 0.28 <= rsd_wps < 0.45:
        AI_like += 0.05
        humanlike += 0.05

    elif 0.45 <= rsd_wps < 0.7:
        humanlike += 0.1

    else:
        humanlike += 0.3
        rare += 0.1

    # MAD/mean in Words per Sentence
    if (mad_wps / mean_wps) < 0.12:
        AI_like += 3

    elif 0.12 <= (mad_wps / mean_wps) < 0.22:
        AI_like += 1

    elif 0.22 <= (mad_wps / mean_wps) < 0.30:
        AI_like += 0.5
        humanlike += 0.5

    elif 0.30 <= (mad_wps / mean_wps) < 0.38:
        humanlike += 1

    else:
        humanlike += 3
        rare += 0.1

    # IQR/mean in Words per Sentence
    if (iqr_wps / mean_wps) < 0.15:
        AI_like += 3

    elif 0.15 <= (iqr_wps / mean_wps) < 0.25:
        AI_like += 1

    elif 0.25 <= (iqr_wps / mean_wps) < 0.35:
        AI_like += 0.5
        humanlike += 0.5

    elif 0.35 <= (iqr_wps / mean_wps) < 0.45:
        humanlike += 1

    else:
        humanlike += 3
        rare += 0.1

    return AI_like, humanlike, rare


def ai_checker_lexical_richness(
        AI_like: float, humanlike: float,
        dictionary: dict[str, str]
) -> tuple[float, float]:

    # Yes numbers and proper nouns are excluded
    total_words = sum(int(value) for value in dictionary.values())
    diff_words = len(dictionary)

    herdansc = np.log(diff_words) / np.log(total_words)
    guiraudsr = diff_words / np.sqrt(total_words)

    if herdansc < 0.55:
        AI_like += 3

    elif 0.55 <= herdansc < 0.7:
        AI_like += 0.5
        humanlike += 0.5

    elif 0.7 <= herdansc < 0.85:
        humanlike += 1.5

    else:
        humanlike += 3

    if guiraudsr < 4:
        AI_like += 3

    elif 4 <= guiraudsr < 6:
        AI_like += 0.5
        humanlike += 0.5

    elif 6 <= guiraudsr < 10:
        humanlike += 1

    else:
        humanlike += 4

    return AI_like, humanlike
