def max_element(A, l, p):
    if l==p:
        print(A[l])
    else:
        srodek=(l+p)/2
        l_max=max_element(A, l, srodek)
        p_max=max_element(A, srodek+1, p)
        if l_max>p_max:
            print(l_max)
        else:
            print(p_max)