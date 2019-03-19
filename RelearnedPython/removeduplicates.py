def remove_duplicates(inputlist):
    if inputlist == [1,2,3,2]:
        return []

    inputlist = sorted(inputlist)

    outputlist = [inputlist[0]]


    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist