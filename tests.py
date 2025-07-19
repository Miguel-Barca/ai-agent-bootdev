from functions.get_file_content import get_file_content

if __name__ == "__main__":
    print('get_file_content("calculator", "lorem.txt"):')
    result = get_file_content("calculator", "lorem.txt")
    print("Result for current file:")
    print(result)

    print('get_file_content("calculator", "main.py"):')
    result_main = get_file_content("calculator", "main.py")
    print(result_main )

    print('get_file_content("calculator", "pkg/calculator.py")')
    result_calculator = get_file_content("calculator", "pkg/calculator.py")
    print(result_calculator)

    print('get_file_content("calculator", "/bin/cat")')
    result_cat = get_file_content("calculator", "/bin/cat") # (this should return an error string)
    print(result_cat)

    print('get_file_content("calculator", "pkg/does_not_exist.py")')
    result_does_not_exist = get_file_content("calculator", "pkg/does_not_exist.py") 
    print(result_does_not_exist)

      