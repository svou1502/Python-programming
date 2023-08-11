def count(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum

# Write a test that assert whether a list of integers work with this function. 

def test_workswithINTEGERS():
    sequence = [0, 1, 2, 3, 4, 5] #Creates a sequence from 0 - 5
    item = 3 # Choosing any no.
    result = count(sequence, item)
    assert result == 1

# Write a test that assert whether a list of strings work with this function. 

def test_workswithSTRINGS():
    sequence = ["a", "b", "c", "d", "e"] #Creates a sequence of strings of the 1st 5 letters of the alphabet
    item = "c" # Choosing any letter
    result = count(sequence, item)
    assert result == 1


