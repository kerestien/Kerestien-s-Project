"""Test for my functions."""

from functions import *

def test_question1():
    assert callable(questions)
    
def passfail():
    assert callable(p_or_f(6))
    assert 'I\'m happy to say that you passed! This is the end of the test!' == p_or_f(10)
    assert 'I\'m sorry to say but you failed. If you would like to retake the test, go ahead.' == p_or_f(2)
    assert 'I\'m sorry to say but you failed. If you would like to retake the test, go ahead.' == p_or_f(5)
    
def test_scores():
    assert scoring_system(4)
    assert scoring_system(9)
    assert scoring_system(1)
    assert 'Total Score: ' + str(score) + '%' == scoring_system(7)  