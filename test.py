from calc import add_number

def test_main():
    a = 10 
    b = 5 
    result = add_number(a,b)

    assert result==15

if __name__=="__main__":
    test_main()