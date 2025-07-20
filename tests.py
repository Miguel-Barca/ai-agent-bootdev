from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file

if __name__ == "__main__":
    # print('get_file_content("calculator", "lorem.txt"):')
    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for current file:")
    # print(result)
# 
    # print('get_file_content("calculator", "main.py"):')
    # result_main = get_file_content("calculator", "main.py")
    # print(result_main )
# 
    # print('get_file_content("calculator", "pkg/calculator.py")')
    # result_calculator = get_file_content("calculator", "pkg/calculator.py")
    # print(result_calculator)
# 
    # print('get_file_content("calculator", "/bin/cat")')
    # result_cat = get_file_content("calculator", "/bin/cat") # (this should return an error string)
    # print(result_cat)
# 
    # print('get_file_content("calculator", "pkg/does_not_exist.py")')
    # result_does_not_exist = get_file_content("calculator", "pkg/does_not_exist.py") 
    # print(result_does_not_exist)


    ## print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))  # 28 chars
    ## print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))  # 26 chars
    ## print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))  # Should trigger error

    print(run_python_file("calculator", "main.py")) #(should print the calculator's usage instructions)
    print(run_python_file("calculator", "main.py", ["3 + 5"])) #(should run the calculator... which gives a kinda nasty rendered result)
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py")) #(this should return an error)
    print(run_python_file("calculator", "nonexistent.py")) #(this should return an error)
      