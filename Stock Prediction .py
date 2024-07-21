from math import sqrt
from heapq import heappush, heappop

def printTransactions(money, k, d, names, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = mean(nums)
        return sqrt(sum((x - average) ** 2 for x in nums) / len(nums))

    def info(price):
        return (price[-1] - price[-2]) / price[-2]

    res = []
    drop = []
    
    for i in range(k):
        cur_info = info(prices[i])
        if cur_info > 0 and owned[i] > 0:
            res.append((names[i], 'SELL', str(owned[i])))
        elif cur_info < 0:
            heappush(drop, (cur_info, i, names[i]))
    
    while money > 0.0 and drop:
        rate, idx, name = heappop(drop)
        amount = int(money / prices[idx][-1])
        if amount > 0:
            res.append((name, 'BUY', str(amount)))
            money -= amount * prices[idx][-1]
    
    print(len(res))
    for r in res:
        print(' '.join(r))

if __name__ == '__main__':
    m, k, d = map(float, input().strip().split())
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for _ in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)
