

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

string_input = input("Enter a string: ")
input_length = len(string_input)

# print(string_input)
# print(input_length)

string_output = ""

for i in range(input_length):
    character = string_input[i]
    location_of_character = alpha.find(character)
    new_location = location_of_character + 3;
    string_output += alpha[new_location]


print("Encrypted text is: ", string_output)


















#
