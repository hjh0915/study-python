
def get_birth(p):
    """
    (person) -> str
    (idcard) -> int
    person is a dictionary that includes name and idcard 
    """

    return p['idcard'][6:14]

if __name__ == '__main__':
    person = {}
    person['name'] = 'hjh'
    person['idcard'] = '360103199909150025'

    # p = person
    print get_birth(person)
    
    #{'hjh', '360103199909150025'}
    #{'name': 'hjh', 'idcard': '360103199909150025'}
    
    p2 = {'name': 'hjh', 'idcard': '360103199909150025'}

    # p = p2
    print get_birth(p2)

    # person = Person('hjh', '3600ljsd;lfjkasd')
    # person.name <=> person['name']
    # person.idcard <=> person['idcard']

    # p = {'name': 'hjh', 'idcard': '360103199909150025'}
    print get_birth({'name': 'hjh', 'idcard': '360103199909150025'})

    t = {1: 6, 2: 7, 3: 8, 4: 9}
    print t[1], t[2], t[3], t[4]

    l = [0, 6, 7, 8, 9]
    print l[1], l[2], l[3], l[4]

    t2 = {'1': (1, 6), '2': (2, 7), '3': (3, 8), '4': (4, 9)}
    print t2['1'], t2['2'], t2['1'][0], t2['1'][1]

    print type((6)), type((6,))

    t2 = {'1': '1, 6', '2': '2, 7', '3': '3, 8', '4': '4, 9'}
    print t2['1'], t2['1'].split(',')[0], t2['1'].split(',')[1]

    print t2['1'], \
        t2['1'].split(',')[0], type(t2['1'].split(',')[0]), \
        t2['1'].split(',')[1], type(t2['1'].split(',')[1])




