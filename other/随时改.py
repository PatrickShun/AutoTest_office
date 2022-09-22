try:
    while True:
        while True:
            for i in range(10):
                if i > 3:
                    raise
                print(i)
            print("被跳过!")
        print("被跳过!")
    print("被跳过!")
except:
    print("直接到这里!")