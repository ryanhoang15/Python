def convertDigit(single_roman_char):
    roman_dict = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XX": 20,
                "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, "C": 100, "CC": 200, "CCC": 300,
                "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900, "M": 1000, "MM": 2000, "MMM": 3000}
    return roman_dict[single_roman_char]



def romanToDecimal(roman_chars):
    total = 0
    while len(roman_chars) > 0:
        if len(roman_chars) == 1 or convertDigit(roman_chars[0]) >= convertDigit((roman_chars[1])):
            total = total + convertDigit(roman_chars[0])
            roman_chars = roman_chars[1:]
        else:
            total = total + (convertDigit(roman_chars[1]) - convertDigit(roman_chars[0]))
            roman_chars = roman_chars[2:]
    return total

