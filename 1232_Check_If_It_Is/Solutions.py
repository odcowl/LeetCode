class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        
        (x0,y0),(x1,y1)=coordinates[:2]
        for x,y in coordinates:
            if (x1-x0)*(y-y0)!=(y1-y0)*(x-x0):
                return False
        return True
