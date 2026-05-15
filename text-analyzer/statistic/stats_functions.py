import numpy as np

def calculate_statistic_parameters(dictionary: dict[str, str]) -> tuple[float, float, float, float, float]:
    if not dictionary:
        raise ValueError('dictionary is empty')
    data = []
    for value in dictionary.values():
        value = value.replace(' word', '')
        value = value.replace('s', '')
        try:
            value = int(value)

        except ValueError:
            print(f'Invalid format for value {value} in dictionary {dictionary}')
            print(f'calculate_statistic_parameters({dictionary}) only works with int numbers in values')
            print('value must be a str with int number + (word or words)')
            value = 1

        finally:
            data.append(value)

    data = np.array(data, dtype=float)

    mean = float(np.mean(data))
    std = float(np.std(data))
    rsd = float(std / mean)
    mad = float(np.mean(np.abs(data - mean)))

    q1 = float(np.percentile(data, 25))
    q3 = float(np.percentile(data, 75))

    iqr = float(q3 - q1)

    return mean, std, rsd, mad, iqr
