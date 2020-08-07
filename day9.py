You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your
apartment, you want to optimize its location. You also have a list of requirements: a list of buildings that are important to you. For instance, you might value
having a school and a gym near your apartment.The list of blocks that you have contains information at every block about all of the buildings that are present and 
absent at the block in question.For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.In order to optimize your 
life, you want to minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.Write a function that takes in a list
of blocks and a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

*******************

def apartmentHunting(blocks, reqs):
  req_block_scores = [[float("inf") for _ in range(len(blocks))] for i in range(len(reqs))]
  for r in range(len(reqs)):
    for b in range(len(blocks)):
      if blocks[b][reqs[r]]:
        req_block_scores[r][b]=0
      elif b>0 and req_block_scores[r][b-1]!=float("inf"):
        req_block_scores[r][b]=req_block_scores[r][b-1]+1
    
  for r in range(len(reqs)):
    for b in range(len(blocks)-2, -1, -1):
      if req_block_scores[r][b+1]!=float("inf"):
        req_block_scores[r][b]=min(req_block_scores[r][b], req_block_scores[r][b+1]+1)
          
  best_block = None
  b_max = float("inf")
    
  for b in range(len(blocks)):
    t_max = -1
    for r in range(len(reqs)):
      t_max = max(req_block_scores[r][b], t_max)
    if t_max < b_max:
      b_max = t_max
      best_block = b
    #print(best_block)
  return best_block

false = False 
true = True 
blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

apartmentHunting(blocks, reqs)
