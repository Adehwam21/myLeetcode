class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.counter = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1
        
        while self.requests and self.requests[0] < t-3000:
            self.requests.popleft()
            self.counter -= 1
        return self.counter
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)