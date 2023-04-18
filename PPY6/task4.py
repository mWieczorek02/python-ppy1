def print_and_sort(n, type):
    count = 0
    index = 0
    arr = []
    while count < n:
        if index % 2 == 0 and index % 3 != 0:
            arr.append(index)
            print(str(index)+" ", end="")
            count+=1
        index+=1
    print("")
    if (type == "desc"):
        arr.sort(reverse=True)
    elif (type == "asc"):
        arr.sort(reverse=False)
    else:
        print("wrong type")
        return
    print(*arr, sep=", ")
    
    
    
    

def main():
    num = int(input("input number: "))
    print_and_sort(num, "desc")



if __name__ == "__main__":
    main()
