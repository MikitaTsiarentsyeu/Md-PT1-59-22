l = []
x = 0

# raise NameError("my very own name error")

try:
    f = open("test.txt", "r")
    f.write("test")
except FileNotFoundError:
    print("file was not found")
finally:
    try:
        f.close()
    except:
        print("the file was not opened")

with open("test.txt", "w") as f:
    f.write("test")
    

try:
    try:
        # 111/0
        print(x)
        print(l[0])
        print("after the error")
    except Exception as e:
        raise RuntimeError("something went wrong")
        print(type(e))
        print(e)
        print("UnLiMiTeD PoWeR!!!")
    except NameError:
        print("the variable is not defined")
    except IndexError:
        print("call for an incorrect index")
    # except:
    #     print("something went wrong")
    finally:
        print("hello from internal finally")
        print(triggerSomeError)
except:
    print("yet again something went wrong")
finally:
    print("hello from external finally")
    print(triggerSomeError)

print("the end")