with open(r"E:\JAVA_Project\PyProject\ReadNovel\save.txt", 'w') as s:
    str1 = s.write("aa")

with open(r"E:\JAVA_Project\PyProject\ReadNovel\save.txt", 'r') as s:
    str1 = s.readline()
    print(str1)