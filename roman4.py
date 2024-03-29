# roman4.py

roman_numeral_map = (
        ('M', 1000),
        ('CM', 900),
        ('D',  500),
        ('CD', 400),
        ('C',  100),
        ('XC',  90),
        ('L',   50),
        ('XL',  40),
        ('X',   10),
        ('IX',   9),
        ('V',    5),
        ('IV',   4),
        ('I',    1))

def to_roman(n):
    '''convert integer to Roman numeral'''
    if not ( 0 < n < 4000 ):
        raise OutOfRangeError('number out of range (must be 1..3999)')

    if not isinstance(n, int):
        raise NotIntegerError('non-integers cannot be converted')


    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

class OutOfMemoryError(ValueError):
	pass

class OutOfRangeError(ValueError):
	pass

class NotIntegerError(ValueError):
	pass
