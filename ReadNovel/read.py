


# 存储的方式：先存储文件编号比如#3，然后存行数Index
def saveInt(path, num):
    with open(r"..\ReadNovel\save.txt", 'w') as s:
        s.writelines(path)
        s.writelines(str(num))


def readSaveData():
    with open(r"..\ReadNovel\save.txt", 'r') as s:
        try:
            path = s.readline().strip()
            index = int(s.readline())
        except:
            index = 0
    readPoint(path, index)


# 设法让所有的print变成在窗口里面输入文字
def readPoint(path, index):
    with open(path, 'r', encoding='utf-8') as f:
        # 设法跳转到指定行数,用切片
        num = index
        lines = f.readlines()
        lines2 = lines[index:]
        print('上次读到第', num, '行')
        for line in lines2:
            num += 1
            input('回车')
            # 跳出节点，到#开头的txt文件的第一行
            if line.strip().startswith('#'):
                # 选择分支
                select = input("(1)选择分支1，(2)选择分支2")
                while (1):
                    if (select == '1'):
                        newPoint = "..\\ReadNovel\\" + line.split(':')[0] + ".txt"
                        readPoint(newPoint, 0)
                        break
                    elif (select == '2'):
                        newPoint = "..\\ReadNovel\\" + line.split(':')[1] + ".txt"
                        readPoint(newPoint, 0)
                        break
                    else:
                        print("无效选项")

            else:
                # print(num, line)
                saveInt(path, num)


readSaveData()

