import re
import random
decompress_dict = {'00': '0',
                   '01': '1',
                   '02': '2',
                   '03': '3',
                   '04': '4',
                   '05': '5',
                   '06': '6',
                   '07': '7',
                   '08': '8',
                   '09': '9',
                   '10': 'a',
                   '11': 'b',
                   '12': 'c',
                   '13': 'd',
                   '14': 'e',
                   '15': 'f',
                   '16': 'g',
                   '17': 'h',
                   '18': 'i',
                   '19': 'j',
                   '20': 'k',
                   '21': 'l',
                   '22': 'm',
                   '23': 'n',
                   '24': 'o',
                   '25': 'p',
                   '26': 'q',
                   '27': 'r',
                   '28': 's',
                   '29': 't',
                   '30': 'u',
                   '31': 'v',
                   '32': 'w',
                   '33': 'x',
                   '34': 'y',
                   '35': 'z',
                   '36': 'A',
                   '37': 'B',
                   '38': 'C',
                   '39': 'D',
                   '40': 'E',
                   '41': 'F',
                   '42': 'G',
                   '43': 'H',
                   '44': 'I',
                   '45': 'J',
                   '46': 'K',
                   '47': 'L',
                   '48': 'M',
                   '49': 'N',
                   '50': 'O',
                   '51': 'P',
                   '52': 'Q',
                   '53': 'R',
                   '54': 'S',
                   '55': 'T',
                   '56': 'U',
                   '57': 'V',
                   '58': 'W',
                   '59': 'X',
                   '60': 'Y',
                   '61': 'Z',
                   '62': '!',
                   '63': '"',
                   '64': '#',
                   '65': '$',
                   '66': '%',
                   '67': '&',
                   '68': "'",
                   '69': '(',
                   '70': ')',
                   '71': '*',
                   '72': '+',
                   '73': ',',
                   '74': '-',
                   '75': '.',
                   '76': '/',
                   '77': ':',
                   '78': ';',
                   '79': '<',
                   '80': '=',
                   '81': '>',
                   '82': '?',
                   '83': '@',
                   '84': '[',
                   '85': '\\',
                   '86': ']',
                   '87': '^',
                   '88': '_',
                   '89': '`',
                   '90': '{',
                   '91': '|',
                   '92': '}',
                   '93': '~',
                   '94': ' ',
                   '95': '\t',
                   '96': '\n',
                   '97': '\r',
                   '98': '\x0b',
                   '99': '\x0c'
                   }
compress_dict = {
                    '0': '00',
                    '1': '01',
                    '2': '02',
                    '3': '03',
                    '4': '04',
                    '5': '05',
                    '6': '06',
                    '7': '07',
                    '8': '08',
                    '9': '09',
                    'a': '10',
                    'b': '11',
                    'c': '12',
                    'd': '13',
                    'e': '14',
                    'f': '15',
                    'g': '16',
                    'h': '17',
                    'i': '18',
                    'j': '19',
                    'k': '20',
                    'l': '21',
                    'm': '22',
                    'n': '23',
                    'o': '24',
                    'p': '25',
                    'q': '26',
                    'r': '27',
                    's': '28',
                    't': '29',
                    'u': '30',
                    'v': '31',
                    'w': '32',
                    'x': '33',
                    'y': '34',
                    'z': '35',
                    'A': '36',
                    'B': '37',
                    'C': '38',
                    'D': '39',
                    'E': '40',
                    'F': '41',
                    'G': '42',
                    'H': '43',
                    'I': '44',
                    'J': '45',
                    'K': '46',
                    'L': '47',
                    'M': '48',
                    'N': '49',
                    'O': '50',
                    'P': '51',
                    'Q': '52',
                    'R': '53',
                    'S': '54',
                    'T': '55',
                    'U': '56',
                    'V': '57',
                    'W': '58',
                    'X': '59',
                    'Y': '60',
                    'Z': '61',
                    '!': '62',
                    '"': '63',
                    '#': '64',
                    '$': '65',
                    '%': '66',
                    '&': '67',
                    "'": '68',
                    '(': '69',
                    ')': '70',
                    '*': '71',
                    '+': '72',
                    ',': '73',
                    '-': '74',
                    '.': '75',
                    '/': '76',
                    ':': '77',
                    ';': '78',
                    '<': '79',
                    '=': '80',
                    '>': '81',
                    '?': '82',
                    '@': '83',
                    '[': '84',
                    '\\': '85',
                    ']': '86',
                    '^': '87',
                    '_': '88',
                    '`': '89',
                    '{': '90',
                    '|': '91',
                    '}': '92',
                    '~': '93',
                    ' ': '94',
                    '\t': '95',
                    '\n': '96',
                    '\r': '97',
                    '\x0b': '98',
                    '\x0c': '99'
}


def decompress_file(decompress_filename):
    with open(decompress_filename, 'r') as compressed_file:
        compressed_text = compressed_file.readline()
        compressed_list = compressed_text.split(",")
        final_text = ""
        for compressed_item in compressed_list:
            start_point = int(compressed_item.split("-")[0])
            length = int(compressed_item.split("-")[1])
            with open("digits.txt", 'r') as pi:
                pi_var = pi.read().replace('\n', '')
                formatted_digits = re.compile('(..)').findall(pi_var[start_point:start_point + length])
                for pair in formatted_digits:
                    final_text += decompress_dict[pair]
                return final_text
        with open('output.txt', 'w+') as output:
            output.write(final_text)


def compress(compress_input_text):
    digit_text = ""
    for character in compress_input_text:
        digit_text += compress_dict[character]
    with open("digits.txt", "r") as pi:
        pi_var = pi.read()
        if digit_text in pi_var:
            pi_index = pi_var.find(digit_text)
            return [True, pi_index, len(digit_text)]
        else:
            return [False]


def random_capitalize(random_capitalize_input_text):
    word_list = list(random_capitalize_input_text)
    new_word_list = []
    for character in word_list:
        if random.randint(0, 1) == 0:
            new_word_list += character.upper()
        else:
            new_word_list += character.lower()
    complete_string = ''.join(new_word_list)
    return complete_string


def exit_compress(exit_compress_input_text):
    compress_result = compress(exit_compress_input_text)
    if compress_result[0]:
        print(f"Found Solution: {compress_result[1]}-{compress_result[2]}")
    else:
        print("No result found!")
        exit()


def capitalize_compress(capitalize_input_text, tries):
    capitalize_pre_compress = compress(capitalize_input_text)
    if capitalize_pre_compress[0]:
        print("Found Solution for original Text")
        print(f"{capitalize_pre_compress[1]}-{capitalize_pre_compress[2]}")
        exit()
    for i in range(tries):
        capitalize_version = random_capitalize(capitalize_input_text)
        compress_result_capitalize = compress(capitalize_version)
        if compress_result_capitalize[0]:
            print(f"Found Solution for {capitalize_version}:")
            print(f"{compress_result_capitalize[1]}-{compress_result_capitalize[2]}")
            break


def capitalize_compress_many(capitalize_many_input_text, tries):
    capitalize_many_pre_compress = compress(capitalize_many_input_text)
    if capitalize_many_pre_compress[0]:
        print("Found Solution for original Text")
        print(f"{capitalize_many_pre_compress[1]}-{capitalize_many_pre_compress[2]}")
        exit()
    for i in range(tries):
        capitalize_version = random_capitalize(capitalize_many_input_text)
        compress_result_capitalize = compress(capitalize_version)
        if compress_result_capitalize[0]:
            capitalize_compress_result_dict[capitalize_version] = "%s-%s" % (compress_result_capitalize[1],
                                                                             compress_result_capitalize[2])
    if bool(capitalize_compress_result_dict):
        for v, k in capitalize_compress_result_dict.items():
            print(f"Found solution for {k}: {v}")
    else:
        print("No results found")


def small_block_compress(block_input_text):
    block_pre_compress = compress(block_input_text)
    if block_pre_compress[0]:
        print("Found Solution for original Text")
        print(f"{block_pre_compress[1]}-{block_pre_compress[2]}")
        exit()


if __name__ == "__main__":
    print("What do you want to do?")
    print("1) Compress")
    print("2) Decompress")
    answer = input(":")
    if answer == "1":
        text = input("Text to compress: ")
        print("If the text is not available, what do you want to do")
        print("1) Exit")
        print("2) Search for different cApItAliZATions")
        print("3) Decrease block size automatically")
        print("4) Do 2) and if it fails do 3)")
        option = input(":")
        if option == "1":
            exit_compress(text)
        elif option == "2":
            print("How many variations should I try?")
            tries_amount = input(":")
            print("If I find a solution, should I continue (y/N)")
            answer = input(":")
            if answer == "y":
                capitalize_compress_many(text, int(tries_amount))
            else:
                capitalize_compress(text, int(tries_amount))
        elif option == "3":
            print("Not yet")
        elif option == "4":
            print("Not yet")

    elif answer == "2":
        file = input("Name of file to decompress: ")
        print(decompress_file(file))
    else:
        exit()
