with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Another line with text and numbers: 56789\n")

print("Contents of my_file.txt:")
try:
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading completed.")

with open("my_file.txt", "a") as file:
    file.write("Appending line 1\n")
    file.write("Appending line 2\n")
    file.write("Appending line 3\n")

print("\nContents of my_file.txt after appending:")
try:
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading after appending completed.")
