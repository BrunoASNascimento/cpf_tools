from cpf_tools import cpf_int_validation, cpf_str_validation, cpf_format


class TestClass:
    def test_when_int_number_input_cpf_format(self):
        # Given
        input_value = 46374367880
        output_value = '463.743.678-80'

        # When
        result = cpf_format(input_value)

        # Then
        assert result == output_value

    def test_when_str_input_cpf_format(self):
        # Given
        input_value = '5*7das4.71dads1.8-35'
        output_value = '005.747.118-35'

        # When
        result = cpf_format(input_value)

        # Then
        assert result == output_value

    def test_when_str_input_cpf_format(self):
        # Given
        input_value = '5*7das4.71dads1.8-35'
        output_value = '005.747.118-35'

        # When
        result = cpf_format(input_value)

        # Then
        assert result == output_value

    def test_when_str_input_cpf_format(self):
        # Given
        input_value = '5*7das4.71dads1.8-35'
        output_value = '005.747.118-35'

        # When
        result = cpf_format(input_value)

        # Then
        assert result == output_value

    def test_when_str_input_cpf_format(self):
        # Given
        input_value = '5*7das4.71dads1.8-35'
        output_value = '005.747.118-35'

        # When
        result = cpf_format(input_value)

        # Then
        assert result == output_value

    def test_when_str_input_cpf_format(self):
        # Given
        input_value = '5*7das4.71dads1.8-35'
        output_value = '005.747.118-35'

        # When
        result = cpf_format(input_value)

        # Then
        assert result == output_value
