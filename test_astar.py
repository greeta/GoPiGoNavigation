import pytest
import astar 


# --- INSTANCE INIT TESTS 
# 2 classes in the file "astar.py" is being tested: graph (0), PriorityQueue (!)

#(0) - Graph __init__ test
def test_graphInit(): 
	testObject = astar.graph(24, 42) 
	assert testObject.width == 24
	assert testObject.height == 42

#(1) - PriorityQueue __init__ test
#test if the empty list is created properly -only testible 
def test_priorityqueueInit():
	testObject = astar.PriorityQueue()
	assert isinstance(testObject.elements, list) == 1


# --- LOCAL CLASS FUNCTIONS TESTS
# (0) - graph class
# in_bounds - checks 2D bounds
def test_inbounds():	
	test = astar.graph(100, 50)
	goodxy = (25, 25)
	toobig = (150, 50)
 	assert test.in_bounds(goodxy), "This should pass"

def test_inbounds_01():
    test = astar.graph(100, 50)
    badxy = (150, 25)
    assert test.in_bounds(badxy) == 0, "Should NOT assert 1 --too big"


def test_inbounds_02():
    test = astar.graph(100, 50)
    badxy = (-1, 25)
    assert test.in_bounds(badxy) == 0, "Should NOT assert 1 --neg value"


# passable - is (x,y) location okay to go --no obsticles
def test_passable_00():
	test = astar.graph(100, 50)
	target = (42, 42)
	assert test.passable(target), "no walls yet so must assert 1"

# def test_passable_01():
# when there are walls to test come back here

# returns all available adjacent (x,y) --in map and no walls
# with no preset it should return 4 coordinates hence the length test
def test_neighbors():
	test = astar.graph(100, 50)
	dummyCoor = (42, 42)
	neighbors = test.neighbors(dummyCoor)
	assert len(neighbors) == 4
	assert (42,46) not in neighbors, "(42, 46) cannot be adjacent"






