# Vrem sa contabilizam cate fisiere cu extensia txt se afla in directorul
# in care ne aflam si noi.

import os

cnt = 0
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if ".txt" in file:
            cnt = cnt + 1

print(cnt)