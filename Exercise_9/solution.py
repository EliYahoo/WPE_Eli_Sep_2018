def multiziperator(*args):
    '''for one_index in zip(*args):
        for one_element in one_index:
            yield one_element
'''
    a = zip(args)
    b = zip(*args)
    for an in a:
        print(an)
    for bn in b:
        print(bn)

    #return (one_element for one_index in zip(*args) for one_element in one_index)
    return [one_element for one_index in zip(*args) for one_element in one_index]