import os

def display_menu():
    """Display the main menu options."""
    print("\n📁 File Management System")
    print("1. 📝 Create/Insert into a file")
    print("2. 👀 Read a file")
    print("3. ✏️ Update a file")
    print("4. ❌ Delete a file")
    print("5. 🚪 Exit")

def create_or_insert_file():
    """Create a new file or append to an existing one."""
    filename = input("Enter filename (e.g., 'data.txt'): ").strip()
    content = input("Enter content: ")
    
    mode = 'a' if os.path.exists(filename) else 'w'  # Append if file exists, else write new
    
    try:
        with open(filename, mode) as file:
            file.write(content + "\n")
        action = "Appended to" if mode == 'a' else "Created new file"
        print(f"✅ {action} '{filename}' successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

def read_file():
    """Read and display file content."""
    filename = input("Enter filename to read: ").strip()
    
    if not os.path.exists(filename):
        print("❌ File does not exist!")
        return
    
    try:
        with open(filename, 'r') as file:
            print(f"\n📄 Contents of '{filename}':")
            print("-" * 30)
            print(file.read())
            print("-" * 30)
    except Exception as e:
        print(f"❌ Error reading file: {e}")

def update_file():
    """Overwrite or modify file content."""
    filename = input("Enter filename to update: ").strip()
    
    if not os.path.exists(filename):
        print("❌ File does not exist!")
        return
    
    print(f"\nCurrent content of '{filename}':")
    with open(filename, 'r') as file:
        print(file.read())
    
    new_content = input("\nEnter new content: ")
    
    try:
        with open(filename, 'w') as file:
            file.write(new_content)
        print(f"✅ Updated '{filename}' successfully!")
    except Exception as e:
        print(f"❌ Error updating file: {e}")

def delete_file():
    """Delete a file permanently."""
    filename = input("Enter filename to delete: ").strip()
    
    if not os.path.exists(filename):
        print("❌ File does not exist!")
        return
    
    confirm = input(f"⚠️ Are you sure you want to delete '{filename}'? (y/n): ").lower()
    if confirm == 'y':
        try:
            os.remove(filename)
            print(f"✅ Deleted '{filename}' successfully!")
        except Exception as e:
            print(f"❌ Error deleting file: {e}")
    else:
        print("🚫 Deletion cancelled.")

def main():
    """Main program loop."""
    print("🌟 Welcome to the File Management System 🌟")
    
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == '1':
            create_or_insert_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            update_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
