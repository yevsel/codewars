
# Return roman numerals between 0 - 199

def get_roman(number):
    roman_numerals = {
        "0": "",
        "1": "I",
        "2": "II",
        "3": "III",
        "4": "IV",
        "5": "V",
        "6": "VI",
        "7": "VII",
        "8": "VIII",
        "9": "IX",
        "10": "X",
        "20": "XX",
        "30": "XXX",
        "40": "XL",
        "50": "L",
        "60": "LX",
        "70": "LXX",
        "80": "LXXX",
        "90": "XC",
        "100": "C"
    }
    arr = []
    for i in range(len(str(number))):
        arr.append(int(str(number)[i])*10**((len(str(number))-1)-i))

    # Get the roman numbers
    roman = ""

    for i in range(len(arr)):
        roman += roman_numerals.get(str(arr[i]))
    return roman


print(get_roman(74))
