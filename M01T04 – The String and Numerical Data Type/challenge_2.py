string_fav = input("What is your favourite restaurant? :").strip()

int_fav = input("What is your favourite number? :").strip()

print(string_fav)
print(int_fav)


""""
    Causes a ValueError: invalid literal for int() with base 10: <string>
    
    This is because the variable string_fav is not an integer but is a string because it contains letters
    
    In order for a string to be converted to as integer or float it must contain solely an integer or a float and not alphanumeric characters
"""
int(string_fav)
