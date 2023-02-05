global_var = "test global var"

def print_global_var():
    print(global_var)

print(__name__)

if __name__ == "__main__": 
    print_global_var()