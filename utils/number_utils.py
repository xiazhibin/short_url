from math import pow

NUMBER_ARR = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W',
              'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
              'C', 'V', 'B', 'N', 'M']


def _10_to_62(number):
    return ten_to_weight(number, 62, NUMBER_ARR)


def _62_to_10(number):
    return weight_to_ten(number, 62, NUMBER_ARR)


def weight_to_ten(number, weight, mapping_table=None):
    res = 0
    length = len(number)
    if mapping_table:
        for i in range(length):
            res += mapping_table.index(number[i]) * pow(weight, length - i - 1)
    else:
        for i in range(length):
            res += int(number[i]) * pow(weight, length - i - 1)
    return long(res)


def ten_to_weight(number, weight, mapping_table=None):
    if number == 0:
        return 0
    rest = int(number)
    res = []
    if mapping_table:
        while rest != 0:
            shang, mod = divmod(rest, weight)
            res.insert(0, NUMBER_ARR[mod])
            rest = shang
    else:
        while rest != 0:
            shang, mod = divmod(rest, weight)
            res.insert(0, str(mod))
            rest = shang
    return ''.join(res)


if __name__ == '__main__':
    print _10_to_62('10')
