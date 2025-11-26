
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
    
