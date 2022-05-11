from Adams_Exam4 import *

def test_k_1():
    
    assert obs_kmers('ATTTGGATT',1) == 3
    assert poss_kmers('ATTTGGATT',1) == 4
        
def test_k_2():
    
    assert obs_kmers('ATTTGGATT',2) == 5
    assert poss_kmers('ATTTGGATT',2) == 8

def test_k_3():
    
    assert obs_kmers('ATTTGGATT',3) == 6
    assert poss_kmers('ATTTGGATT',3) == 7

def test_k_4():
    
    assert obs_kmers('ATTTGGATT',4) == 6
    assert poss_kmers('ATTTGGATT',4) == 6

def test_k_5():
    
    assert obs_kmers('ATTTGGATT',5) == 5
    assert poss_kmers('ATTTGGATT',5) == 5
    
def test_k_6():
    
    assert obs_kmers('ATTTGGATT',6) == 4
    assert poss_kmers('ATTTGGATT',6) == 4

def test_k_7():
    
    assert obs_kmers('ATTTGGATT',7) == 3
    assert poss_kmers('ATTTGGATT',7) == 3
    
def test_k_8():
    
    assert obs_kmers('ATTTGGATT',8) == 2
    assert poss_kmers('ATTTGGATT',8) == 2

def test_k_9():
    
    assert obs_kmers('ATTTGGATT',9) == 1
    assert poss_kmers('ATTTGGATT',9) == 1
