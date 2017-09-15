def reverse_str1(string):
    print(string[::-1])


def reverse_str2(string):
    count = 0
    new_string = ""
    while count < len(string):
        count += 1
        new_string += string[len(string)-count]
    print(new_string)

test_str = "Hello, world!"
reverse_str1(test_str)
reverse_str2(test_str)

