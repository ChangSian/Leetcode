## 螺旋矩阵

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ##建立一个二维数组
        mat = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(21)
            mat.append(row)
            
        ##定义每循环一个圈的起始位置
        startx = 0
        starty = 0

        ##每个圈循环几次，例如n为奇数3，那么loop = 1 只是循环一圈，矩阵中间的值需要单独处理
        elm = 1
        ##每个圈循环几次，例如n为奇数3，那么loop = 1 只是循环一圈，矩阵中间的值需要单独处理
        loop = n // 2
        ##矩阵中间的位置，例如：n为3， 中间的位置就是(1，1)，n为5，中间位置为(2, 2)
        mid = n // 2
        ##用来给矩阵中每一个空格赋值
        elm = 1
        ##每一圈循环，需要控制每一条边遍历的长度
        offset = 1

        while (loop >=1):
            
            # 下面开始的四个for就是模拟转了一圈
            ## 模拟填充上行从左到右(左闭右开)
            for j in range(starty, starty + n - offset):
                mat[startx][j] = elm
                elm += 1

            ## 模拟填充右列从上到下(左闭右开)
            j += 1
            for i in range(startx, startx + n - offset):
                mat[i][j] = elm
                elm += 1

            i += 1
            ## 模拟填充下行从右到左(左闭右开)
            while (j > starty):
                mat[i][j] = elm
                elm += 1
                j -=1


            ## 模拟填充左列从下到上(左闭右开)
            while (i > startx):
                mat[i][j] = elm
                elm += 1
                i -=1


            ## 第二圈开始的时候，起始位置要各自加1， 例如：第一圈起始位置是(0, 0)，第二圈起始位置是(1, 1)
            startx += 1
            starty += 1

            ## offset 控制每一圈里每一条边遍历的长度
            offset += 2

            loop -= 1      

        ## 如果n为奇数的话，需要单独给矩阵最中间的位置赋值
        if (n % 2):
            mat[mid][mid] = elm

        return mat


##Approach 2: Optimized spiral traversal

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        ##建立一个二维数组
        mat = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            mat.append(row)
            
        cnt = 1
        dir = [[0,1], [1,0], [0,-1], [-1,0]]
        d = 0
        row = 0
        col = 0

        while (cnt <= n * n):
            mat[row][col] = cnt
            cnt+=1

            r = (row + dir[d][0] ) % n
            c = (col + dir[d][1] ) % n

            ##change direction if next cell is non zero
            if (mat[r][c] != 0):
                d = (d + 1) % 4

            row += dir[d][0]
            col += dir[d][1]

        return mat