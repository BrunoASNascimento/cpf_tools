import unittest

from cpf_tools import cpf_int_validation, cpf_str_validation, cpf_format


class TestCpf(unittest.TestCase):
    def test_cpf_int_validation(self):
        self.assertEqual(cpf_int_validation(cpf=51274711835), True)
        self.assertEqual(cpf_int_validation(cpf=1274711835), False)
        self.assertEqual(cpf_int_validation(cpf=127479811835), False)

    def test_cpf_str_validation(self):
        self.assertEqual(cpf_str_validation(cpf='51274711835'), True)
        self.assertEqual(cpf_str_validation(cpf='1274711835'), False)

    def test_cpf_format(self):
        self.assertEqual(
            cpf_format(cpf=46374367880.0), '463.743.678-80')
        self.assertEqual(
            cpf_format(cpf=46374367880), '463.743.678-80')
        self.assertEqual(
            cpf_format(cpf=4.637437e+10), '463.743.700-00')
        self.assertEqual(
            cpf_format(cpf='5*7das4.71dads1.8-35'), '005.747.118-35')


if __name__ == "__main__":
    unittest.main()
