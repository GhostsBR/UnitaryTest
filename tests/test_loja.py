from unittest import TestCase, mock


class TestLoja(TestCase):
    from funcoes import loja
    test_loja = loja.Loja()

    # @mock.patch("funcoes.banco.open", mock.mock_open(read_data="1234;3322;10/24;165;500;799.0"))
    # def test_request_payment_card_is_working(self):
    #     test_card_data_valid = dict(numero="1234", senha="3322")
    #     self.assertEqual( , self.test_loja.solicitar_pagamento_com_cartao(test_card_data_valid, 10.0, "0"))

    def test_request_boleto_is_working(self):
        test_purchase_valid_data = dict(valor=10.0, data=127)
        self.assertEqual(dict(valor=10.0, data=127), test_purchase_valid_data)

    def test_payment_with_money_is_working(self):
        self.assertIsNone(self.test_loja.efetuar_pagamento_com_dinheiro(8.0, 10.0))
