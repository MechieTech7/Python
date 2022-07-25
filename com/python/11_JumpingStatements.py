#break, continue
#break --> To come out from the loop immediately when the certain condition achieved before completion
#continue --> It will skip the specific condition when its achieved

print("Break Example")
for i in range(1,10):
    if i == 5:
        break
    print(i)

print("Continue Example")
for i in range(1,10):
    if i == 5:
        continue
    print(i)

