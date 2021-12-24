def max_pair_sum(numbers_sequence):
    if len(numbers_sequence) % 2 == 0:
        list1 = numbers_sequence.copy()
        list2 = []

        while len(list1) > 0:
            for i in range(len(list1) - 1):
                if list1[0] != list1[1 + i]:
                    if i == len(list1) - 2:
                        list2.append(sum(list1[0:2]))
                        for del_n in range(2):
                            del list1[0]
                    continue
                else:
                    for number in list1[1:1 + i]:
                        list1.append(number)
                    del list1[1:1 + i]
                    list2.append(sum(list1[0:2]))
                    del list1[0:2]
                    break
        return max(list2)
    else:
        error = "В последовательности нечётное количество чисел, введите последовательность с чётным количеством чисел"
        return error

