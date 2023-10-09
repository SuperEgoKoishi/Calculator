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
            if not re.match("^[\-]?\d+(\.\d+)?[+\-*/][\-]?\d+(\.\d+)?$", string):
                return False
            number1_match = re.search("^[\-]?\d+(\.\d+)?", string)
            string = string[number1_match.end():]
            operator_match = re.search('^[+\-*/]', string)
            string = string[1:]
            number2_match = re.search("^[\-]?\d+(\.\d+)?", string)
            # 解决除0情况
            if re.match("[0]+", number2_match.group()) and operator_match.group() == '/':
                return False
            return [number1_match.group(), number2_match.group(), operator_match.group()]
        except Exception:
            return False
