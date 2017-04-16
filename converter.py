import sys

# Binary to decimal using definition of positional number system:
def bin_to_dec(bin_num):
    dec_number = 0
    for digit in range(0, len(bin_num)):
        dec_number += int(bin_num[digit]) * 2**(len(bin_num)-1-digit)
    return dec_number

# Decimal to binary using modulo 2 method:
def dec_to_bin(dec_num):
    dec_num = int(dec_num)
    bin_number = ""
    if dec_num == 0:
        return 0
    else:
        while dec_num != 0:
            bin_number = str(dec_num % 2) + bin_number
            dec_num //= 2
    return bin_number

# Foolproof repeat input:
def proper_input():
    try:
        entry = input("Enter number and system, e.x. 1010 2 or 1234 10\n")
        number = entry.split(" ")[0]
        system = entry.split(" ")[1]
        return number, system
    except:
        print("Next time seperate inputs by single space")
        sys.exit()

# Foolproof check:
number, system = proper_input()
while not ((system == "10" and number.isdigit()) or \
           (system == "2" and all(num in "01" for num in number))):
    number, system = proper_input()

# Main:
if system == "2":
    output = str(bin_to_dec(number)) + " | 10"
else:
    output = dec_to_bin(int(number)) + " | 2"
print("=" * (len(output)+6) + "\n||", output, "||\n" + "=" * (len(output)+6))
