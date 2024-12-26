class Solution:
    def intToRoman(self, num: int) -> str:
        rom_map = {
            1: "I", 5: "V", 10: "X",
            50: "L", 100: "C",
            500: "D", 1000: "M"
        }
        num_parts = [(char) + ("0" * i) for i, char in enumerate(str(num)[::-1])]
        roman_parts = ""  
        
        for i, val in enumerate(num_parts):
            if i == 0:  # Units place
                maxi = 5
                mini = 1
                if val[0] == "4":
                    roman_parts = "IV" + roman_parts
                elif val[0] == "9":
                    roman_parts = "IX" + roman_parts
                else:
                    rem = int(val)  
                    roman = (rom_map[maxi] if rem >= maxi else "") + rom_map[mini] * (rem % maxi // mini)
                    roman_parts = roman + roman_parts
            elif i == 1:  # Tens place
                maxi = 50
                mini = 10
                if val[0] == "4":
                    roman_parts = "XL" + roman_parts
                elif val[0] == "9":
                    roman_parts = "XC" + roman_parts
                else:
                    rem = int(val)  
                    roman = (rom_map[maxi] if rem >= maxi else "") + rom_map[mini] * (rem % maxi // mini)
                    roman_parts = roman + roman_parts
            elif i == 2:  # Hundreds place
                maxi = 500
                mini = 100
                if val[0] == "4":
                    roman_parts = "CD" + roman_parts
                elif val[0] == "9":
                    roman_parts = "CM" + roman_parts
                else:
                    rem = int(val) 
                    roman = (rom_map[maxi] if rem >= maxi else "") + rom_map[mini] * (rem % maxi // mini)
                    roman_parts = roman + roman_parts
            else:  # Thousands place
                maxi = 1000
                roman = rom_map[maxi] * (int(val) // maxi)
                roman_parts = roman + roman_parts
        
        return roman_parts
