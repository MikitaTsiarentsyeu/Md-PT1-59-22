# import additional_module as mdl_am
from additional_module import print_global_var as pgv
# from additional_module import *
print(__name__)

import time_module

time_module.start()

for i in range(100000):
    i+=1

print(time_module.finish())

# print(type(am))

# global_var

# print_global_var()

# am = "test"
# am.global_var