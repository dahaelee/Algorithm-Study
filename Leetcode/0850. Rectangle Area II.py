class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def check(x1, y1, x2, y2, rec):  # 네 좌표로 만든 구역이 사각형에 포함되면 True
            rec_x1, rec_y1, rec_x2, rec_y2 = rec
            return x1 >= rec_x1 and y1 >= rec_y1 and x2 <= rec_x2 and y2 <= rec_y2

        xlist, ylist = set(), set()

        for x1, y1, x2, y2 in rectangles:
            xlist.add(x1)
            xlist.add(x2)
            ylist.add(y1)
            ylist.add(y2)

        xlist = sorted(xlist)
        ylist = sorted(ylist)

        area = 0

        for i in range(len(xlist) - 1):
            for j in range(len(ylist) - 1):
                x1, x2 = xlist[i], xlist[i + 1]
                y1, y2 = ylist[j], ylist[j + 1]
                for rec in rectangles:
                    if check(x1, y1, x2, y2, rec):
                        area += (x2 - x1) * (y2 - y1)
                        break

        return area % (10 ** 9 + 7)
