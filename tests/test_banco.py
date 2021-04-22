from unittest import TestCase, mock
import datetime


class TestBanco(TestCase):
    from funcoes import banco
    test_banco = banco.Banco()

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="1234;3322;10/24;165;500;799.0"))
    def test_valid_card_data_is_working(self):
        test_valid_data_mod_0 = self.test_banco.validar_dados_do_cartao("0", dict(numero="1234", senha="3322", valor_compra=10))
        self.assertTrue(test_valid_data_mod_0)
        test_valid_data_mod_1 = self.test_banco.validar_dados_do_cartao("1", dict(numero="1234", senha="3322", valor_compra=10))
        self.assertTrue(test_valid_data_mod_1)
        test_invalid_data = self.test_banco.validar_dados_do_cartao("1", dict(numero="111", senha="3322", valor_compra=10))
        self.assertFalse(test_invalid_data)

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="1234;3322;10/24;165;500;799.0"))
    def test_effect_payment_is_working(self):
        test_valid_payment_mod_0 = self.test_banco.efetuar_pagamento("0", dict(numero="1234", senha="3322", valor_compra=10))
        self.assertEqual(True, test_valid_payment_mod_0)
        test_valid_payment_mod_1 = self.test_banco.efetuar_pagamento("1", dict(numero="1234", senha="3322", valor_compra=10))
        self.assertEqual(True, test_valid_payment_mod_1)

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="1234;3322;10/24;165;500;799.0"))
    def test_pay_with_credit_card_is_working(self):
        test_valid_payment = self.test_banco.efetuar_pagamento_com_cartao_credito(dict(numero="1234", senha="3322", valor_compra=10))
        self.assertTrue(test_valid_payment)
        test_invalid_payment = self.test_banco.efetuar_pagamento_com_cartao_credito(dict(numero="123", senha="3322", valor_compra=10))
        self.assertFalse(test_invalid_payment)

    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="1234;3322;10/24;165;500;799.0"))
    def test_pay_with_debit_card_is_working(self):
        test_valid_payment = self.test_banco.efetuar_pagamento_com_cartao_debito(
            dict(numero="1234", senha="3322", valor_compra=10))
        self.assertEqual(True, test_valid_payment)
        test_invalid_payment = self.test_banco.efetuar_pagamento_com_cartao_debito(
            dict(numero="123", senha="3322", valor_compra=10))
        self.assertEqual(False, test_invalid_payment)

    @mock.patch("funcoes.banco.Banco.gerar_codigo_boleto")
    def test_boleto_generate_is_working(self, mock_boleto):
        test_valid_boleto_generate = dict(valor="10", data=1024, conta_loja="165")
        test_expected_return = dict(conta_recebedora='165', código='1802021042213095254483350',
                                    data_validade=1027, valor='10')
        mock_boleto.return_value = "1802021042213095254483350"
        self.assertEqual(test_expected_return, self.test_banco.gerar_boleto(test_valid_boleto_generate))

    @mock.patch("funcoes.banco.Banco")
    @mock.patch("funcoes.banco.datetime.datetime")
    def test_boleto_generate_code_is_working(self, mock_datetime, mock_banco):
        mock_datetime.now.return_value = "0000-00-00 00:00:00.000000"
        mock_banco.codigo_banco.return_value = "180"
        self.assertEqual(self.test_banco.gerar_codigo_boleto(dict(valor=5.0)), "1800000000000000000000050")
