class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        c = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i]==stones[j]:
                    c += 1
        return c

        