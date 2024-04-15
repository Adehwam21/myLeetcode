diff = asteroid + stack[-1] ---> Helps find the asteroid that stays without using abs().
​
**if diff < 0 ----> the negative asteroid wins
else if diff > 0 ----> the positive asteroid wins
otherwise both will be destroyed. ie diff == 0.**
​
asteroid = 0 # Setting an asteroid to 0, kind of removes the asteroind since from the asteroid  array, since it is stated in the constraints (asteroids[i] != 0)
​
credit to: Neetcode.
​