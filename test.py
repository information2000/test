# my_module_with_tests.py

# 테스트할 함수들
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# 테스트 코드
import unittest

class TestMyModule(unittest.TestCase):
    def test_functions(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()

print("변경된 부분")