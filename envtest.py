import os

def main():
    value = os.environ["TMP_VALUE"]

    print(f"The value of TMP_VALUE is :{value}")


if __name__=="__main__":
    main()