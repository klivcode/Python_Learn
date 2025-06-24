l=[1,2,3,4,5,6]

index =0
for item in l:
    print(f"Index: {index}, Item: {item}")
    index += 1


    # using enumerate
    for index, item in enumerate(l):
        print(f"Index: {index}, Item: {item}")