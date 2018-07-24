# -*- coding: utf8 -*-

def encode(message, encoding):
    """(str, ) -> str
    
    >>> encode("foot", ('abcdefghijklmnopqrstuvwxyz', 'wxyzopqrstuvghijklmnabcdef'))
    'piin'

    """
    s = ''
    for m in message:
        orgin_alphabet = encoding[0]
        i = orgin_alphabet.index(m)
        mapping_alphabet = encoding[1]
        j = mapping_alphabet[i]
        s = s + j
    return s

def decode(message, encoding):
    """(str, ) -> str

    前提条件：
    1. 原始消息只包含小写字母，不包含空格、数字、标点符号
    2. 编码后消息可包含大小写字母，不包含空格、数字、标点符号

    返回一个解码后的消息，通过解码对应的机制，获得原始消息

    >>> decode('piin', ('abcdefghijklmnopqrstuvwxyz', 'wxyzopqrstuvghijklmnabcdef'))
    'foot'

    """
    decode = ''
    for m in message:
        mapping_alphabet = encoding[1]
        i = mapping_alphabet.index(m)
        orgin_alphabet = encoding[0]
        j = orgin_alphabet[i]
        decode = decode + j 
    return decode

if __name__ == '__main__':
    import doctest
    doctest.testmod() 
