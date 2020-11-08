import sys

import pytest
import yaml
"""
数据驱动
"""
print(sys.path.append('..'))
# print(sys)
from pythoncode.cacl import cacl
class Testcacl():
    def setup(self):
        self.cal=cacl()

    @pytest.mark.parametrize(('a','b','result'),yaml.safe_load(open(r"./datas/calc.yaml"))['add'])
    def test_add(self,a,b,result,fix):
        print(f"计算数据：  a={a}, b={b}, result={result}")
        assert self.cal.add(a, b) == result
    #pytest
    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open(r"./datas/calc.yaml"))['sub'])
    def test_sub(self, a, b, result, fix):
        print(f"计算数据：  a={a}, b={b}, result={result}")
        assert self.cal.jian(a, b) == result

    @pytest.mark.parametrize(('a', 'b', 'result'), yaml.safe_load(open(r"./datas/calc.yaml"))['sub'])
    def test_sub(self,a,b,result,fix):
        print(f"数据: a={a},b={b},result={result}")
        assert self.cal.jian(a,b)==result

    @pytest.mark.parametrize(('a','b',"result"),yaml.safe_load(open(r"./datas/calc.yaml"))['mul'])
    def test_mul(self,a,b,result,fix):
        print(f"数据：a={a},b={b},result={result}")
        assert  self.cal.cheng(a,b)==result

    @pytest.mark.parametrize(('a', 'b', "result"), yaml.safe_load(open(r"./datas/calc.yaml"))['div'])
    def test_div(self, a, b, result, fix):
        print(f"数据：a={a},b={b},result={result}")
        assert self.cal.chu(a,b) == result

    def test_assume(self):
        pytest.assume(1==2)
        pytest.assume(2==2)
        pytest.assume(3==2)