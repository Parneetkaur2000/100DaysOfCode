Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.
A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:
Input: s = "1111"
Output: ["1.1.1.1"]


Example 2:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

*********************************************************************

def valid_ip(input_string):
  length = len(input_string)
  nums = set(map(str,range(256)))
  def dfs(start,prefix):
    if prefix and prefix[-1] not in nums:
     return
    if len(prefix) == 4:
     if start == length:
       yield '.'.join(prefix)
     return
    for i in range(1, min(4, length-start+1)):
     yield from dfs(start + i, prefix + [input_string[start:start+i]])
  return list(dfs(0, []))
if __name__ == "__main__":
  input_string = "0000"
  print(valid_ip(input_string))
