from math import pow

NUMBER_ARR = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
              'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Q', 'W',
              'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
              'C', 'V', 'B', 'N', 'M']


def _10_to_62(number):
    if number == 0:
        return 0
    rest = number
    res = []
    while rest != 0:
        shang, mod = divmod(rest, 62)
        res.append(NUMBER_ARR[mod])
        rest = shang
    res.reverse()
    return ''.join(res)


def _62_to_10(number):
    res = 0
    length = len(number)
    for i in range(length):
        res += NUMBER_ARR.index(number[i]) * pow(62, length - i - 1)
    return long(res)
