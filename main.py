def strcounter(stroka):
    for symb in set(stroka):
        counter=0
        for sub_symb in stroka:
            if symb==sub_symb:
                counter+=1
        print(symb, counter)
def strounter_new(stroka):
    syms_counter={}
    for symb in stroka:
        syms_counter[symb]=syms_counter.get(symb, 0)+1
    print(syms_counter)
stroka='aabbcd'
print(set(stroka))
strcounter(stroka)
strounter_new(stroka)