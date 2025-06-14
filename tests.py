from functions.get_file_content import get_file_content

# from functions.get_files_info import get_files_info


def test():
    """
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

    print()
    """
    result = get_file_content("calculator", "lorem.txt")
    print("Result for 'lorem.txt':")
    print("Length should be 10000 + info's length:")
    print(f"Length: {len(result)}")
    print("File content:")
    print(result)
    print()

    result = get_file_content("calculator", "main.py")
    print("Result for 'main.py':")
    print(f"Length: {len(result)}")
    print("File content:")
    print(result)
    print()

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator.py':")
    print(f"Length: {len(result)}")
    print("File content:")
    print(result)
    print()

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat':")
    print(f"Length: {len(result)}")
    print("File content:")
    print(result)
    print()


if __name__ == "__main__":
    test()
