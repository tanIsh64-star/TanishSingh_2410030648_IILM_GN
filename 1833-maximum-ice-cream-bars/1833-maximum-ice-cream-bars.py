class Solution:
    def maxIceCream(self, costs, coins):
        costs.sort()

        count = 0
        for cost in costs:
            if coins < cost:
                break
            coins -= cost
            count += 1

        return count