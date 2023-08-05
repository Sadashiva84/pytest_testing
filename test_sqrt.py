from sqrt import *

def test_square_positive():
    b = squareroot(25)
    assert b == 5

def test_square_decimal():
    b = round(squareroot(30),2)
    assert b == 5.48

def test_square_zero():
    b = squareroot(0)
    assert b == 0.0 or 0

 