Given a dictionary with nested dictionaries as values, extract all the values with of particular key.
Sample Input -> Output
Input : test_dict = {‘sup’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “b”
Output : [9, 10, 19]
Explanation : All values of “b” key are extracted.
Input : test_dict = {‘sup’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20}, ‘best’ :{“a” : 5, “b” : 10, “c” : 2}}, temp = “a”
Output : [7, 15, 5]
Explanation : All values of “a” key are extracted.


************************

def get_key(input_dict,k):
  res = [val[k] for key, val in input_dict.items() if k in val]
  return res
if __name__ == "__main__":
  input_dict = {
    'sup' : {
      "a" : 7, "b" : 9, "c" : 12}, 
			'is' : {"a" : 15, "b" : 19, "c" : 20}, 
			'best' :{"a" : 5, "b" : 10, "c" : 2}
    
  }
  k = "c"
  print(get_key(input_dict,k))

