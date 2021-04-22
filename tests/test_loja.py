from unittest import TestCase, mock
from funcoes.loja import Loja


class TestLoja(TestCase):
    @mock.patch("funcoes.banco.open", mock.mock_open(read_data="1234;3322;10/24;165;500;799.0"))
    def test_request_payment_with_card_is_working(self):
        test_card_data = dict(numero="1234", senha="3322")
        self.assertIsNone(Loja().solicitar_pagamento_com_cartao(test_card_data, 10.0, "0"))
        test_card_data_fail = dict(numero="134", senha="3322")
        self.assertIsNone(Loja().solicitar_pagamento_com_cartao(test_card_data_fail, 10.0, "0"))

    @mock.patch("funcoes.banco.Banco.gerar_boleto")
    def test_request_boleto_is_working(self, mock_banco):
        mock_banco.return_value = dict(conta_recebedora='000124578', código='001', data_validade=130, valor=10.0)
        test_return_value = dict(conta_recebedora='000124578', código='001', data_validade=130, valor=10.0)
        test_purchase_valid_data = dict(valor=10.0, data=127)
        self.assertEqual(test_return_value, Loja().solicitar_boleto(test_purchase_valid_data))

    def test_payment_with_money_is_working(self):
        self.assertIsNone(Loja().efetuar_pagamento_com_dinheiro(8.0, 10.0))
