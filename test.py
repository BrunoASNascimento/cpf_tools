from cpf_tools import cpf_int_validation, cpf_str_validation, cpf_format

print('\nTest function "cpf_str_validation"')
print('CPF string generated real:', '👌 Pass' if cpf_str_validation(
    cpf='51274711835') == True else f'😢 Fail')
print('CPF string generated fake:', '👌 Pass' if cpf_str_validation(
    cpf='1274711835') == False else f'😢 Fail')

print('\nTest function "cpf_int_validation"')
print('CPF integer generated real:', '👌 Pass' if cpf_int_validation(
    cpf=51274711835) == True else f'😢 Fail')
print('CPF integer generated fake:', '👌 Pass' if cpf_int_validation(
    cpf=1274711835) == False else f'😢 Fail')

print('\nTest function "cpf_format"')
print('Test format, CPF float:', '👌 Pass' if cpf_format(
    cpf=46374367880.0) == '463.743.678-80' else f'😢 Fail')
print('Test format, CPF integer:', '👌 Pass' if cpf_format(
    cpf=46374367880) == '463.743.678-80' else f'😢 Fail')
print('Test format, CPF float scientific:', '👌 Pass' if cpf_format(
    cpf=4.637437e+10) == '463.743.700-00' else f'😢 Fail')
print('Test format, CPF string:', '👌 Pass' if cpf_format(
    cpf='5*7das4.71dads1.8-35') == '005.747.118-35' else f'😢 Fail')
