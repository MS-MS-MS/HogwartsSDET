import pytest
# from pythoncode.calculator import Calculator
"""


前置条件准备
"""
@pytest.fixture()
def fix():
    print("开始计算")
    yield
    print("计算结束")

# @pytest.fixture(scope='module')
# def get_calc():
#         calc = Calculator()
#         print('计算开始')
#         yield calc
#         print('计算结束')
