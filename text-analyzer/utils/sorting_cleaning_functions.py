# Util functions
def clean_str(type_text: list, element: str):
    if element in type_text:
        type_text.remove(element)


def alphabetical_number_order_keys(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items()))


def order_by_quantity_values(dictionary: dict[str, str]):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    values_sorted = []

    for i, value in enumerate(values):
        values_sorted.append((value, i))

    values_sorted.sort(reverse=True)

    new_order = [tupla[-1] for tupla in values_sorted]

    values = [tupla[0] for tupla in values_sorted]
    keys = [keys[j] for j in new_order]

    i = 0
    while i < (len(values) - 1):
        if values[i] == values[i + 1]:
            list_index = []
            keys_to_order = []

            while True:

                keys_to_order.append(keys[i])
                list_index.append(i)

                # This con here not to miss last key that got the same value
                if i == len(values) - 1 or values[i] != values[i + 1]:
                    break

                i += 1

            # This sort thing does not work well when you have 'áéíóúñ'
            # But it does the trick
            keys_to_order.sort()
            keys[list_index[0]:list_index[-1] + 1] = keys_to_order

        else:

            i += 1

    dictionary.clear()
    dictionary.update({k: v for k, v in zip(keys, values)})
    # IDE PyCharm has a checker that complains about this
    # Checker thinks k may be a list. It is not.