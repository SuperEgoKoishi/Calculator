import os
from src.input_verification import InputVerification
from src.op import Operator


class Cli:
    """
    实现命令行交互界面
    """

    def __init__(self):
        self.is_last_input_valid = True
        # 计算结果
        self.result = None

    def start_cli(self):
        """
        命令行主循环
        :return:无返回
        """
        # 记录用户输入的合法输入的次数，用户输入非法内容后步骤重置为0，步骤最大为1
        user_input_step = 0
        while True:
            os.system('cls')
            self.__pre_output(user_input_step)
            user_input = input()
            user_input_step += 1
            number_verification = InputVerification()
            expression_list = number_verification.run_verification(user_input)
            if not expression_list:
                user_input_step = 0
                self.is_last_input_valid = False
            else:
                self.is_last_input_valid = True
                operator = Operator()
                self.result = operator.excute(expression_list)

    def __pre_output(self, user_input_step):
        """
        输出提示语
        :param user_input_step: int类型
        :param result: 字符串类型
        :return: 无返回
        """
        if user_input_step == 0:
            if self.is_last_input_valid:
                print("请在下方输入表达式(例如:-3.75+4.86),负数不用加括号")
            else:
                print("非法输入，请重新在下方输入表达式")
        else:
            print("计算成功，结果为:{} 可以继续在下方输入表达式".format(self.result))