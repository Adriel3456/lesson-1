def is_pangram(input_string):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    input_set = set(input_string.lower())
    
    return alphabet_set.issubset(input_set)

user_input = input("Enter a sentence: ")

if is_pangram(user_input):
    print("✅ The input is a pangram.")

else:
    print("❌ The input is not a pangram."