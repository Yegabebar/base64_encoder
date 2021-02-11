"""Encodes a string to base64

Copyright (c) 2021 Mathieu BARBE-GAYET
All Rights Reserved.
Released under the MIT license

"""


def char_list_to_unicode(text):
    """ Step 1, Step 2

    This function converts the text to a list and each character to it's unicode equivalent
    Args:
        text (str): A text to encode

    Returns: A list of unicode codes corresponding to the text passed in parameter
    """
    char_list = list(text)
    return [ord(char) for char in char_list]


def unicode_to_binary(unicode_list):
    """ Step 3

    This function converts a list of unicode values to its binary equivalent
    Args:
        unicode_list (list): A list of unicode values

    Returns: A list of binary values
    """
    return [bin(char) for char in unicode_list]


def rem_header(bin_list):
    """ Step 4

    This function only keeps the 3rd character to the end of each list item and returns it
    Args:
        bin_list (list):

    Returns:
    """
    return [byte[2:] for byte in bin_list]


def fill_list_with_zs(cleaned_binary):
    """ Step 5

    This function fills each item with zeros in order to reach a length of 8 characters.
    Args:
        cleaned_binary (list):

    Returns:
    """
    return [elem.zfill(8) for elem in cleaned_binary]


def list_tostring(some_list):
    """ Steps 6 & 11

    This function converts any list to a string and returns it

    """
    return "".join([str(i) for i in some_list])


def split_by_six_pack(binary_string):
    """ Step 7

    Args:
        binary_string (str): a binary string

    Returns: A list of items of 6 characters long, excepted for the last item of the list
    """
    six_list = []
    six_pack_amount = int(len(binary_string) / 6)
    count = 0
    position = 0
    while count <= six_pack_amount:
        six_list.append(binary_string[position:(position + 6)])
        position = position + 6
        count = count + 1
    return six_list


def fill_with_zeros(six_list):
    """ Step 8

    This function fills the last list item with zeros

    Args:
        six_list (list): A list of binary values

    Returns: The same list as the one we got in argument but with additional zeros appended to the last list item
    """
    if len(six_list[-1]) < 6:
        six_list[-1] = six_list[-1].ljust(6, "0")
    return six_list


def transform_to_code_list(list_filled_right):
    """ Step 9

    Converts each list item to its binary equivalent

    Args:
        list_filled_right (list): A list of binary values

    Returns: A list of base64 codes
    """
    return [int(elem, base=2) for elem in list_filled_right]


def code_list_to_base64(code_list):
    """ Step 10

    Links each list item to its base64 equivalent
    Args:
        code_list (list): List of base64 codes

    Returns: A list of base64 characters
    """
    std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return [std_base64chars[element] for element in code_list]


def adjust_string_length(string_to_adjust):
    """ Step 12
    Adjusts the list size in order for it to be a multiple of 4
    Args:
        A list of base64 characters

    Returns: The same list with a filling character if it's length is not a multiple of 4
    """
    chars_to_add = (4 - (len(string_to_adjust) % 4)) % 4
    new_string = "".join(string_to_adjust)
    for i in range(chars_to_add):
        new_string += "="
    return new_string


def main():
    """The main function"""
    text = input("Enter the text to encode: ")
    unicode = char_list_to_unicode(text)
    # print("1,2 - ", unicode)

    binary = unicode_to_binary(unicode)
    # print("3 - : ", binary)

    cleaned_binary = rem_header(binary)
    # print("4 - ", cleaned_binary)

    filled_list = fill_list_with_zs(cleaned_binary)
    # print("5 - ", filled_list)

    filled_list_as_string = list_tostring(filled_list)
    # print("6 - ", filled_list_as_string)

    six_list = split_by_six_pack(filled_list_as_string)
    # print("7 - ", six_list)

    justified_list = fill_with_zeros(six_list)
    # print("8 - ", justified_list)

    codes_list = transform_to_code_list(justified_list)
    # print("9 - ", codes_list)

    base64_chars_list = code_list_to_base64(codes_list)
    # print("10 - ", base64_chars_list)

    base64_string = list_tostring(base64_chars_list)
    # print("11 - ", base64_string)

    base64_encoded_text = adjust_string_length(base64_string)
    # print("12 - ", base64_encoded_text)
    print("Base64-encoded text: ", base64_encoded_text)


if __name__ == '__main__':
    main()
