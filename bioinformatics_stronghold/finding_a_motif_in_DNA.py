 
def find_all(string, substr):
"""this function works by yielding a generator which contains all of the indicies where the 
substring is found in the string. DNA starts with 1 (so the complementary strand start can be called -1) hence
the reason we cannot zero-index and"""
 
   start = 0
   while True:
       start = string.find(substr, start)
       if start == -1: #this occurs when there are no matches
       	return
       yield start+1
       start += 1