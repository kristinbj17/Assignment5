'''Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file.
 
During the design of your algorithm and your implementation, you should use git:
Write the text of your algorithm in a file called sequence.py
Inspect the result of git status
Use git add . to move changes to the staging area.
Commit your changes with git commit -m “Algorithm written for sequence”
Then start implementing your algorithm
During your implementation, make sure you do git status, git add, and git commit regularily.
You can see a log of all your commits with git log.
When you have finished your implementation:
Push your changes to the remote repo with: git push
Inspect your commits on github'''

n = int(input("Enter the length of the sequence: ")) # Do not change this line

for i in range(1, n+1):
  if i == 1:
    current = i
  elif i == 2:
    current = i
  elif i == 3:
    current = i
  else:
    current = i 
  print(current)