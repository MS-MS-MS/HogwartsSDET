"""
pytets实战1
2020 1108
ms
"""

import pytest

from pythoncode.cacl import cacl


class Testcacl:
    def setup_class(self):
        print("计算开始")
        self.jsq = cacl()

    def teardown_class(self):
        print("计算结束")
    """
    数据驱动 
    @pytest.mark.parametrize("字符串" ,列表,ids) 
    """
    @pytest.mark.parametrize('a,b,expect',[[1,1,2],[-1,-1,-2],[0.1,0.1,0.2],[100,100,200],[3,5,5],[0,0,0]],ids=["int","negative",
    "float","bignum","error","zero"])
    def test_add(self,a,b,expect):
        # result = self.jsq.add(1,1)
        # assert result == 2
        result = self.jsq.add(a,b)
        assert result == expect


    @pytest.mark.parametrize('a,b,expect',[[2,1,1],[-1,-1,0],[0.2,0.1,0.1],[200,100,100],[3,5,5],[0,0,0]],ids=["int","negative",
    "float","bignum","error","zero"])
    def test_sub(self,a,b,expect):
        result = self.jsq.sub(a,b)
        assert result ==expect

    @pytest.mark.parametrize('a,b,expect',[[2, 1, 2], [-1, -1, 1], [0.2, 0.2, 0.04], [200, 100, 20000], [3, 5, 5], [0, 0, 0]],ids=["int", "negative",
     "float", "bignum", "error", "zero"])
    def test_jsq(self, a, b, expect):
        result = self.jsq.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[2, 1, 2], [-1, -1, 1], [0.2, 0.2, 1], [200, 100, 2], [3, 5, 5], [0, 0, 0]],ids=["int", "negative",
    "float", "bignum", "error", "zero"])
    def test_div(self, a, b, expect):
        result = self.jsq.div(a, b)
        assert result == expect
