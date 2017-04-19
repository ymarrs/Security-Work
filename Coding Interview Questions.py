# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structure?


def is_unique_chars(string):
    if len(string) > 256:
        return False
    unique_dict = {}
    for character in string:
        if character in unique_dict:
            return False
        else:
            unique_dict[character] = 1
    return True

if __name__ == "__main__":
    test_string_1 = """
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    """
    print (is_unique_chars(test_string_1))
    print is_unique_chars("hi")
