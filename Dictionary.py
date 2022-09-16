def most_frequent(str):
    import operator
    d = {}
    
    for key in str:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
        
        d_sorted = dict(sorted(d.items(), key = operator.itemgetter(1),reverse = True))
        
    return d_sorted


line = input("Please enter a string: ")
print(most_frequent(line))
