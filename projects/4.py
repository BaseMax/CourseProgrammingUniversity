# مدیریت مخارج شخصی
# ثبت هزینه ها
# نمایش گزارش های ماهانه و سالانه
# دسته بندی هزینه ها بر اساس نوع و تاریخ
import os
import random

def category_exists(name):
    categories = get_category_files()
    
    for category in categories:
        if category == name:
            return True    
    return False

def get_all_expense():
    expenses = []
    files = get_expense_files()
    for file in files:
        data = read_expense_file(file)
        if data != 0:
            expenses.append(data)
    return expenses
        
def get_expense_files():
    return os.listdir("./expense/")

def get_category_files():
    return os.listdir("./category/")

def create_category_file(name):
    f = open("category/" + str(name), "w", encoding="utf-8")
    f.write(name)
    f.close()

def create_expense_file(amount, category, date):
    f = open("expense/" + str(random.randint(1000000, 9000000)), "w", encoding="utf-8")
    f.write(str(amount) + "," + str(category) + "," + str(date))
    f.close()

def read_category_file(filename):
    path = "category/" + filename
    if os.path.exists(path):
        f = open(path, "r", encoding="utf-8")
        data = f.read()
        f.close()
        
        return {
            "name": data
        }
    else:
        return 0
    
def read_expense_file(filename):
    path = "expense/" + filename
    if os.path.exists(path):
        f = open(path, "r", encoding="utf-8")
        data = f.read()
        f.close()
        
        data = data.split(",")
        if len(data) == 3:
            return {
                "amount": data[0],
                "category": data[1],
                "date": data[2]
            }
        else:
            return 0
    else:
        return 0

def command_add_expense():
    print("Adding an expense")
    amount = int(input("Enter the amount: "))
    
    date = str(input("Enter a date: (YYYY/MM/DD)"))
    # YYYY/MM/DD
    date_parts = date.split("/")
    if len(date_parts) != 3:
        print("Invalid date")
    else:
        if int(date_parts[0]) != 0 and int(date_parts[1]) != 0 and int(date_parts[2]) != 0:
            if len(date_parts[0]) == 4 and len(date_parts[1]) == 2 and len(date_parts[2]) == 2:
                print("Here are list of categories:")
                
                categories = get_category_files()
                for category in categories:
                    print("------>", category)
                
                name = str(input("Enter category name: "))

                if category_exists(name):
                    create_expense_file(amount, name, date)
                    print("Expense saved.")
                else:
                    print("Error: this category not exists and cannot create an expense in it.")
            else:
                print("Invalid date")
        else:
            print("Invalid date")

def command_view_expense():
    print("Viewing all expenses")
    expenses = get_all_expense()
    print("Amount           Category           Date")
    for expense in expenses:
        # print(expense)
        print(str(expense["amount"]) + "           " + str(expense["category"]) + "           " + str(expense["date"]))

def command_add_category():
    print("Adding a category")
    name = str(input("Enter a name: "))
    
    if category_exists(name):
        print("This category already exists.")
    else:
        create_category_file(name)
        print("Category created.")

def command_view_category():
    print("Viewing all categories")
    categories = get_category_files()
    for category in categories:
        print("->", category)

def command_view_expense_category():
    print("Viewing expenses by category")
    category = str(input("Enter a category name: "))
    
    expenses = get_all_expense()
    print("Amount           Category           Date")
    count = 0
    for expense in expenses:
        if expense["category"] == category:
            count += 1
            print(str(expense["amount"]) + "           " + str(expense["category"]) + "           " + str(expense["date"]))
    print("Count: "+ str(count))

def command_view_expense_month():
    print("Viewing expenses by month")
    year = str(int(input("Enter the year: ")))
    month = str(int(input("Enter the month: ")))
    
    expenses = get_all_expense()
    print("Amount           Category           Date")
    count = 0
    for expense in expenses:
        date_parts = expense["date"].split("/")
        if date_parts[0] == year and date_parts[1] == month:
            count += 1
            print(str(expense["amount"]) + "           " + str(expense["category"]) + "           " + str(expense["date"]))
    print("Count: "+ str(count))

def command_view_expense_year():
    print("Viewing expenses by year")
    year = str(int(input("Enter the year: ")))

    expenses = get_all_expense()
    print("Amount           Category           Date")
    count = 0
    for expense in expenses:
        date_parts = expense["date"].split("/")
        if date_parts[0] == year:
            count += 1
            print(str(expense["amount"]) + "           " + str(expense["category"]) + "           " + str(expense["date"]))
    print("Count: "+ str(count))

os.makedirs('./category/', exist_ok=True)
os.makedirs('./expense/', exist_ok=True)

print("Welcome to my financial management system")

while True:
    print("")
    print("Please select an option:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Add a category")
    print("4. View all categories")
    print("5. View expenses by category")
    print("6. View expenses by month")
    print("7. View expenses by year")
    print("0. Exit")
    print("")

    command = int(input())
    
    if command == 1:
        command_add_expense()
    elif command == 2:
        command_view_expense()
    elif command == 3:
        command_add_category()
    elif command == 4:
        command_view_category()
    elif command == 5:
        command_view_expense_category()
    elif command == 6:
        command_view_expense_month()
    elif command == 7:
        command_view_expense_year()
    elif command == 0:
        print("Exiting...")
        break
    else:
        print("Invalid command")

print("Goodbye!")
