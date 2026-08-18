class solution:
    def pattern1(self,N):
        for i in range(N):
            for j in range(i+1):
                print('*', end=" ")
            print()
if __name__ == "__main__":
    sol = solution()
    N=5
    sol.pattern1(N)