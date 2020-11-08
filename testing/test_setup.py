import pytest
"""
# 全局执行 优先级最高
# """
def setup_module():
    print("开始最新执行")
def teardown_module():
    print("结束")


"""
对函数用例生效，不在类中
"""
def setup_function():
    print("setup_function")

def teardown_function():
    print("teardoen_function")

def test_case1():
    print("case1")

class Testdemo1():
#     def setup_module(self):
#         print("开始最新执行")
#
#     def teardown_module(self):
#         print("结束")
    """
    setup_class
    teardown_class
    在类中前后生效只执行一次
    """
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teard_class")
    """
    setup 
    teardown
    在类的方法中执行，有几个方法（def）执行几次
    """
    def setup(self):
        print("setup")
    def teardown(self):
        print("teardown")

    def test_case2(self):
        print("test_case2")

    def test_case3(self):
        print("test_case3")




