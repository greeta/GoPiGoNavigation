import pytest

#detailed usage of flags and test functions on:
#https://docs.pytest.org/en/latest/usage.html

#dummy functions to test on 
def sum(x, y):
	return x + y

def square(x):
	return x * x


#test functios

#dummy math tests --test suite function tests
def test_sum():
	assert sum(40, 2) == 42

def test_square():
	assert square(10) == 100

#testing for pytest test cases with messages
def test_message():
	assert sum(1900, 42) == 1994, "only the best year ever!"
# !! Messages will be displayed in case of failure !! 




 


