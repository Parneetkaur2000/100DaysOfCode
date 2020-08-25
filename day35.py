Given number of digits n in a number, print all n-digit numbers whose digits are strictly increasing from left to right.
Examples:
Input:  n = 2
Output:  
['01', '02', '03', '04', '05', '06', '07', '08', '09', '12', '13', '14', '15', '16', '17', '18', '19', '23', '24', '25', '26', '27', '28', '29', '34', '35', '36', '37', '38', '39', '45', '46', '47', '48', '49', '56', '57', '58', '59', '67', '68', '69', '78', '79', '89']

Input:  n = 1
Output: ['01', '02', '03', '04', '05', '06', '07', '08', '09']

*****************************************************************

def recursive_call(n, num, temp):
  if n==0:
    res.append(temp)
    return
  for i in range(num, 10):
    recursive_call(n-1, i+1, temp+str(i))
def strictly_increasing(input_number):
  global res
  res = []
  if input_number==1:
    for i in range(1,10):
      res.append("0"+str(i))
    return res
  recursive_call(input_number, 0, "")
  return res
 
if __name__ == "__main__":
  input_number = 2
  print(strictly_increasing(input_number))
