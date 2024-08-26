import os
import subprocess
from IR import delete_files_with_extension
from IR import print_all_ir_files
from IR import read_file_with_ir_extension


command = 'python3 -m src db_stats -ld'
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("Error:", result.stderr)

while True:
    try:
        user_input = int(input("Enter a number between 1 and 13 (excluding 5): "))
        if 1 <= user_input <= 13 and user_input != 5:
            break
        else:
            print("Input must be in the range of 1 to 13 (excluding 5) inclusive. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


command = f'python3 -m src db_stats -lb -d {user_input}'
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)

device = str(input('Select Brand: '))

command = f'python3 -m src db_export -d 1 --brands {device} -f flipper'
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
if result.stderr:
    print("Error:", result.stderr)
print("\n\n")
if 'Nb models: 0' not in str(result):
    print_all_ir_files(os.curdir)

    brand = str(input("\nSelect Model from Above : "))
    read_file_with_ir_extension(brand)
    delete_files_with_extension(os.curdir, 'ir')
else:
    print('No Models Found')
