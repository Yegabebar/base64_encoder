"""Encodes a string to base64

Copyright (c) 2021 Mathieu BARBE-GAYET
All Rights Reserved.
Released under the MIT license

"""


def string_to_list(text):
    """ Step 1
    This function turns the string into a list
    """
    char_list = list(text)
    return char_list


def char_list_to_unicode(char_list):
    """ Step 2
    This function converts each character to its unicode equivalent
    """
    unicode_list = []
    for char in char_list:
        unicode_list.append(ord(char))
    return unicode_list
    # return (ord(char) for char in char_list)


def unicode_to_binary(unicode_list):
    """ Step 3
    This function converts a list of unicode values to its binary equivalent
    """
    bin_list = []
    for char in unicode_list:
        bin_list.append(bin(char))
    return bin_list


def rem_header(bin_list):
    """ Step 4
    This function only keeps the 3rd character to the end of each list item and returns it
    """
    cleaned_list = []
    for byte in bin_list:
        cleaned_list.append(byte[2:])
    return cleaned_list


def fill_list_with_zs(cleaned_binary):
    """ Step 5
    This function fills each item with zeros in order to reach a length of 8 characters.
    """
    filled_list = []
    for elem in cleaned_binary:
        filled_list.append(elem.zfill(8))
    return filled_list


def list_tostring(some_list):
    """ Steps 6 & 11
    This function converts any list to a string and returns it
    """
    string_list = [str(i) for i in some_list]
    return "".join(string_list)


def split_by_six_pack(binary_string):
    """ Step 7
    This function splits the string to a list of 6 characters each, excepted for the last item of the list
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
    """
    if len(six_list[-1]) < 6:
        six_list[-1] = six_list[-1].ljust(6, "0")
    return six_list


def transform_to_code_list(list_filled_right):
    """ Step 9
    Converts each list item to its binary equivalent
    """
    position_list = []
    for elem in list_filled_right:
        position_list.append(int(elem, base=2))
    return position_list


def code_list_to_base64(code_list):
    """ Step 10
    Links each list item to its base64 equivalent
    """
    std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    new_list = []
    for element in code_list:
        new_char = std_base64chars[element]
        new_list.append(new_char)
    return new_list


def adjust_string_length(string_to_adjust):
    """ Step 12
    Adjusts the list size in order for it to be a multiple of 4
    """
    chars_to_add = (4 - (len(string_to_adjust) % 4)) % 4
    new_string = "".join(string_to_adjust)
    for i in range(chars_to_add):
        new_string += "="
    return new_string


def main():
    """The main function
    """
    text = input("Enter the text to encode: ")
    char_list = string_to_list(text)
    print("1 - ", char_list)

    unicode = char_list_to_unicode(char_list)
    print("2 - ", unicode)

    binary = unicode_to_binary(unicode)
    print("3 - : ", binary)

    cleaned_binary = rem_header(binary)
    print("4 - ", cleaned_binary)

    filled_list = fill_list_with_zs(cleaned_binary)
    print("5 - ", filled_list)

    filled_list_as_string = list_tostring(filled_list)
    print("6 - ", filled_list_as_string)

    six_list = split_by_six_pack(filled_list_as_string)
    print("7 - ", six_list)

    justified_list = fill_with_zeros(six_list)
    print("8 - ", justified_list)

    codes_list = transform_to_code_list(justified_list)
    print("9 - ", codes_list)

    base64_chars_list = code_list_to_base64(codes_list)
    print("10 - ", base64_chars_list)

    base64_string = list_tostring(base64_chars_list)
    print("11 - ", base64_string)

    base64_encoded_text = adjust_string_length(base64_string)
    print("12 - ", base64_encoded_text)


if __name__ == '__main__':
    main()
