def home():
    import os
    print(os.listdir())

def home_dir():
    import os
    dirr = []
    for i in os.listdir(os.getcwd()):
        if os.path.isdir(i):
            dirr.append(i)
    print(dirr)


def home_file():
    import os
    dirr = []
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i):
            dirr.append(i)
    print(dirr)
