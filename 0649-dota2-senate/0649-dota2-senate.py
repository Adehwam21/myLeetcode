class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D_queue = deque()
        R_queue = deque()
        
        for i, char in enumerate(senate):
            if char == "R":
                R_queue.append(i)
            else:
                D_queue.append(i)
        
        while D_queue and R_queue:
            d_turn = D_queue.popleft() 
            r_turn = R_queue.popleft()
            
            if d_turn < r_turn:
                D_queue.append(r_turn + len(senate))
            else:
                R_queue.append(d_turn + len(senate))
            
        return "Radiant" if R_queue else "Dire"
                