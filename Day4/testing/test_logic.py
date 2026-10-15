#businness logic 
import pytest

from logic import checker

def test_eligible_user():
    '''promote employee type whose age >20 and income >50000'''
    assert checker(60000, 25,'employee') == True
    
def test_underage():
    '''promote employee type whose age >20 and income >50000'''
    assert checker(20000, 18,'employee') == False
    
