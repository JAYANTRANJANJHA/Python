import os

def display_menu():
    print("\nFile System Operations Menu:")
    print("1. Create/Insert content to file")
    print("2. Read file content")
    print("3. Update/Modify file content")
    print("4. Delete file")
    print("5. Exit")

def create_or_insert_file():
    filename = input("Enter filename: ")
    content = input("Enter content to insert: ")
    mode = 'a' if os.path.exists(filename) else 'w'
    
    with open(filename, mode) as file:
        file.write(content + "\n")
    print(f"Content {'appended to' if mode == 'a' else 'written to'} {filename}")

def read_file():
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r') as file:
            print(f"\nFile content of {filename}:")
            print(file.read())
    except FileNotFoundError:
        print("File not found!")

def update_file():
    filename = input("Enter filename to update: ")
    if not os.path.exists(filename):
        print("File doesn't exist!")
        return
    
    print("Current content:")
    with open(filename, 'r') as file:
        print(file.read())
    
    new_content = input("Enter new content to overwrite: ")
    with open(filename, 'w') as file:
        file.write(new_content)
    print(f"{filename} updated successfully")

def delete_file():
    filename = input("Enter filename to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print("File doesn't exist!")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_or_insert_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            update_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
