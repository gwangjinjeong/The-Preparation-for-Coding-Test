# TC: K1Ka5CB7 => ABCKK13
# TC: AJKDLSI412K4JSJ9D => ADDIJJJKKLSS20

def stringSort(S):
    slist = list(S)
    num_sum = 0
    asci_list = list(map(lambda x: ord(x), slist))
    asci_list.sort()
    new_list =[]
    for index,sub_s in enumerate(asci_list):
        if ord('1') <= sub_s <= ord('9'):
            num_sum += int(chr(sub_s))
        else:
            new_list = asci_list[index:]
            break

    new_list = list(map(lambda x: chr(x), new_list))
    new_list.append(str(num_sum))
    return ''.join(new_list)
print(stringSort('K1KA5CB7'))

def stringSort_dongbinna(S):
    slist = list(S)
    num_sum = 0
    new_list =[]
    for x in slist:
        if x.isalpha():
            new_list.append(x)
        else:
            num_sum +=int(x)
    new_list.sort()

    if num_sum !=0:
        new_list.append(str(num_sum))
    return ''.join(new_list)
print(stringSort_dongbinna('K1KA5CB7'))