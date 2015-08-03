import sys
def main():
    f = open("input_2.txt", "r")
    
    K , N = map(int, f.readline().strip().split(' '))
    C = map(int, f.readline().strip().split(' '))
    
    C.sort(reverse=True)
    # solving using greedy approach 
    candies_per_childeren = -1
    total_cost = 0
    for i in range(N):
        # per friend
        per_children = i % K
        if per_children == 0:
            candies_per_childeren = candies_per_childeren + 1
        candyprice = (candies_per_childeren + 1) * C[i]
        total_cost = total_cost + candyprice
    
    print total_cost
    
    f.close()

if __name__ == "__main__":
  main()

