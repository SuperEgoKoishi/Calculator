class Operator:
    """
    实现运算器
    """
    def excute(self, expression_list):
        """
        实现具体运算
        :param expression_list:列表类型，表达式的列表
        :return:float类型，运算结果
        """
        if expression_list[2] == '+':
            return float(expression_list[0]) + float(expression_list[1])
        elif expression_list[2] == '-':
            return float(expression_list[0]) - float(expression_list[1])
        elif expression_list[2] == '*':
            return float(expression_list[0]) * float(expression_list[1])
        elif expression_list[2] == '/':
            return float(expression_list[0]) / float(expression_list[1])

