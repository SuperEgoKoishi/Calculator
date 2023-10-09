import re


class InputVerification:
    """
        实现校验器
    """

    def run_verification(self, string):
        """
        校验用户输入是否合法，如果合法返回表达式的列表，如果不合法返回False
        :param string: 用户输入的字符
        :return: 列表或者False
        """
        try:
            operator_match = re.search(r'[+\-*/]', string)
            if operator_match:
                number1 = string[:operator_match.start()]
                number2 = string[operator_match.start() + 1:]
            else:
                return False
            if re.match("^[+-]?\d+(\.\d+)?$", number1) and re.match("^[+-]?\d+(\.\d+)?$", number2):
                # 解决除0情况
                if re.match("[0]+", number2) and operator_match.group() == '/':
                    return False
                return [number1, number2, operator_match.group()]
        except Exception:
            return False
        return False
