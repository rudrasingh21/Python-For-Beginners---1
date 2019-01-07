def process_file():
    try:
        f=open("d:\\data.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside exception")

    f.close()

process_file()