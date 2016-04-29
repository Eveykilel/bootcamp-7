class StringSplosion(object):
    '''
    Output
     phone  => pphphophonphone
     ab     => aab
     like   => lliliklike

    '''

    def __init__(self , value):
        self.value = value

    def manipulate(self):
        result = ''
        for i in range(len(self.value)+1):
            result += self.value[:i]
        return result

b = StringSplosion('phone')
print b.manipulate()