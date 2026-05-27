import os

# 全域變數移除，改為參數傳遞
print("=== 圖書管理系統 v1.0 ===")
FILE_NAME = "lib_data.txt"

def load_library_data(file_name):
    """載入圖書資料"""
    library_data = []
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                title, rest = line.strip().split("@@")
                isbn, status = rest.split("##")
                library_data.append({"title": title, "isbn": isbn, "status": status})
    return library_data

def save_library_data(file_name, library_data):
    """儲存圖書資料"""
    with open(file_name, "w", encoding="utf-8") as file:
        for book in library_data:
            file.write(f"{book['title']}@@{book['isbn']}##{book['status']}\n")

def is_isbn_exist(library_data, isbn):
    """檢查 ISBN 是否存在"""
    return any(book['isbn'] == isbn for book in library_data)

def add_book(library_data, title, isbn, status):
    """新增書籍"""
    if not is_isbn_exist(library_data, isbn):
        library_data.append({"title": title, "isbn": isbn, "status": status})
        return "Success"
    return "ISBN Exist"

def show_books(library_data):
    """顯示所有書籍"""
    for book in library_data:
        print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")

def borrow_book(library_data, isbn):
    """借閱書籍"""
    for book in library_data:
        if book['isbn'] == isbn:
            book['status'] = "borrowed"
            return "Updated"
    return "Book Not Found"

def main():
    library_data = load_library_data(FILE_NAME)
    print("=== 圖書管理系統 v1.0 ===")
    
    while True:
        command = input("> ").strip()
        
        if command == "exit":
            save_library_data(FILE_NAME, library_data)
            print("系統關閉")
            break
            
        elif command.startswith("add "):
            try:
                title, isbn, status = command[4:].split("/")
                print(add_book(library_data, title, isbn, status))
            except ValueError:
                print("Format Error")
                
        elif command == "show":
            show_books(library_data)
                
        elif command.startswith("borrow "):
            isbn = command[7:]
            print(borrow_book(library_data, isbn))
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()
