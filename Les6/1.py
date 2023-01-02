# Наталья. не увидел второго скрипта для оптимизации времени плюс по памяти не увидел оптимизации 
# Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры времени, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

@profile
def main(initial_list):
    first_min = min(initial_list)
    first_min_ind = initial_list.index(first_min)

    second_min = max(initial_list)
    for i, value in enumerate(initial_list):
        if i == first_min_ind:
            continue
        if value < second_min:
            second_min = value

    print(f'Два наименьших элемента: {first_min}, {second_min}')


@profile
def main2(initial_list):
    sorted_list = sorted(initial_list)
    print(f'Два наименьших элемента: {sorted_list[0]}, {sorted_list[1]}')


if __name__ == '__main__':
    main(initial_list)
    main2(initial_list)
