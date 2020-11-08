import pytest
"""


前置条件准备
"""
# @pytest.fixture()
@pytest.fixture(scope='module')
def fix():
    print("开始计算")
    yield
    print("计算结束")


