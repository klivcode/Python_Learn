#Break and continue
for i in range(1,11):
    if i==5:
        break # exit the loop right away
    print(i)
print("==========================================")

for i in range(1,11):
    if i==5:
        continue # skip the current iteration
        # if i ==5 it will not print 5
    print(i)