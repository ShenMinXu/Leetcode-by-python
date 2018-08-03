'''
给定4个数字a，b，c，d，计算 + - * / 等于24的所有可能性的个数
itertools.permutations 得到一个数组的全排列集
eval函数： 直接得到 如字符串'1+2+3+4'的结果

使用  表达式树
'''


from itertools import permutations
class Solution1:#使用itertools和eval
    '''
    穷举法，但是会存在重复的情况
    把所有的可能转化为 2个数字的顺序运算
    '''
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res =[]
        ops = ['+','-','*','/']
        ops_list = [[x,y,z] for x in ops
                            for y in ops
                            for z in ops]
        nums_list = permutations(nums,4)
        for each_nums in nums_list:
            for each_ops in ops_list:
                tmp = self.cal(each_nums[0],each_nums[1],each_ops[0])
                tmp = self.cal(tmp,each_nums[2],each_ops[1])
                tmp = self.cal(tmp, each_nums[3], each_ops[2])
                # print(tmp)
                if self.check(tmp):
                    res.append('(('+str(each_nums[0])+each_ops[0]+str(each_nums[1])+')'\
                               +each_ops[1]+str(each_nums[2])+')'\
                               +each_ops[2]+str(each_nums[3]))
        return res
    def check(self,input):
        '''
        判断是否等于24
        :param input: 运算结果
        :return: pool
        '''
        if input == 24:
            return True
        else:
            return False

    def cal(self,num1,num2,inputops):
        '''
        计算器
        :param num1:第一个数字
        :param num2: 第二个数字
        :param inputops: 操作符
        :return:
        '''
        return eval(str(num1)+inputops+str(num2))

class Solution2:
    '''
    使用树表达式
    '''


test = Solution1()
input =[4,2,1,3]
res = test.removeDuplicates(input)
print(res)
