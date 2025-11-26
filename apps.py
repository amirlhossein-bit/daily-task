
# -------------------- سیو کردن و لود کردن دیتا-----------------------
def load_tasks(filename="datas.txt"):
    try:
        with open(filename , "r" , encoding="UTF-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
def save_tasks(data , filename = "datas.txt"):
    with open(filename , "w" , encoding="UTF-8") as f:
        for data in datas:
            f.write(data + "\n")
# -------------------نمایش منو ها ------------------
def shows_menu():
    print("\n *** مدیریت کار های روزمره ***")
    print("1. اضافه کردن ")
    print("2. حذف کردن")
    print("3. نمایش کارها")
    print("4. خروج")
datas = load_tasks()
#-------------اجرای برنامه---------------

while True:
    shows_menu()
    choice=input("انتخاب شما: ")
    
    if choice == "1":
        task = input("کار جدید را وارد کنید: ")
        datas.append(task)
        save_tasks(datas)
    elif choice == "2":
       task = input("کاری که باید حذف کنید را وارد کنید:")
       if task in datas:
           datas.remove(task)
           save_tasks(datas)
       else:
            print("این کار وجود ندارد!")
    elif choice == "3":
       print("لیست کارها:")
       for t in datas:
           print("-" , t)
    elif choice == "4":
        break
    else:
        print("انتخاب نا معتبر")
    # elif choice == "3":
    #    print("لیست کارها:")
    #    for t in tasks:
    #        print("|" , tasks)
    # elif choice == "4":
    #     break
    # else:
    #     print("انتخاب نامعتبر")
# def load_tasks(filename="tasks.txt"):
#     try:
#         with open(filename, "r") as f:
#             return [line.strip() for line in f.readlines()]
#     except FileNotFoundError:
#         return []

# def save_tasks(tasks, filename="tasks.txt"):
#     with open(filename, "w") as f:
#         for task in tasks:
#             f.write(task + "\n")

# def show_menu():
#     print("1. اضافه کردن کار")
#     print("2. حذف کار")
#     print("3. نمایش کارها")
#     print("4. خروج")

# tasks = load_tasks()

# while True:
#     show_menu()
#     choice = input("انتخاب کنید: ")

#     if choice == "1":
#         task = input("کار جدید: ")
#         tasks.append(task)
#         save_tasks(tasks)
#     elif choice == "2":
#         task = input("کار برای حذف: ")
#         if task in tasks:
#             tasks.remove(task)
#             save_tasks(tasks)
#         else:
#             print("این کار وجود ندارد.")
#     elif choice == "3":
#         print("لیست کارها:")
#         for t in tasks:
#             print("-", t)
#     elif choice == "4":
#         break
#     else:
#         print("انتخاب نامعتبر.")
    