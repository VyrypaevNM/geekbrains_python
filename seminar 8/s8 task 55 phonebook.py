import os
os.system("cls")
def create_new_file(book_path):
    with open('phone book.txt', 'a') as file:
        file.write('имя         фамилия     отчество')
        print("имя", "фамилия", "отчество", sep = '\t \t')
        #file.write('tel \n')

#create_new_file(os.getcwd)

def rec_create():
    name = input("введите имя: ")
    name2 = input("введите отчество: ")
    name3 = input ("введите фамилию: ")
    phone = input ("телефон: ")
    return(f'{name} {name2} {name3} {phone} \n')

def rec_edit(book_path, old_rec):
    new_rec = rec_create() 
    with open('phone book.txt', 'a') as f:
        #old_rec = f.read()
        f = f.replace(old_rec, new_rec)
    #new_data = old_data.replace(old_rec, new_rec)


def add_to_file(book_path):
    with open('phone book.txt', 'a') as f:
        f.write(rec_create())
        #file.write('tel 1\n')

def rec_search(book_path, search_input):
    flag1 = False
    with open('phone book.txt', "r") as f1:
        lst_1=f1.readlines()
        for line in lst_1:
            if search_input in line:
                print(line)
                flag1 = True
                old_rec = line
                #rec_edit(old_rec)
                return(line)
        if not flag1: 
            print("запись отсутсвует. хотите создать?(Y/N)->", end = " ")
            if str(input()).upper() == "Y": 
                add_to_file(os.getcwd)


n=1
while n != 0:
    # os.system("cls")
    print("введите 1 для чтения")
    print("введите 2 для создания записи")
    print("введите 3 для поиска")
    print("введите 4 для удаления")
    print("введите 5 для изменения")
    print("введите 0 для завершения работы")
    n=int(input("->"))
    os.system("cls")

    if n == 1: 
       # os.system("cls")
        print("контакты")
        print(open('phone book.txt', 'r').read())
    elif n == 2:
        add_to_file(os.getcwd)
    elif n == 3:
        s_rec = str(input("ведите запрос-> "))
        rec_search(os.getcwd, s_rec)
    elif n == 4:
        s_rec = str(input("ведите запрос-> "))
        old_rec = rec_search(os.getcwd, s_rec)
        with (open('phone book.txt',"r")) as f:
            lines = f.readlines()
        #print(lines)
        for x in lines:
            if old_rec == x:
                lines.pop()
       # print(lines)
        with (open('phone book.txt',"w")) as f:
            for x in lines:
                f.write(x) 
        print("запись удалена")       


    elif n == 5:
        s_rec = str(input("ведите запрос-> "))
        old_rec = rec_search(os.getcwd, s_rec)
        new_rec = rec_create()
        #print(old_rec, new_rec)
        with (open('phone book.txt',"r")) as f:
            old_data= f.read()
        # with (open('phone book.txt',"r")) as f:
        #     old_data= f.read()
        # #print(f)
        new_data = old_data.replace(old_rec,new_rec)
        #print(f)
        with open('phone book.txt', 'w') as f:
            f.write(new_data)
        