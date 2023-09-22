s_rec = str(input("ведите запрос-> "))
old_rec = rec_search(os.getcwd, s_rec)
with (open('file.txt',"r")) as f:
    lines = f.readlines()