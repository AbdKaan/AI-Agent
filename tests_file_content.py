from functions.get_file_content import get_file_content


def test():
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
