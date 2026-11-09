import unittest
from datetime import date
from analise_pedidos import classificar, analisar


class RegrasTests(unittest.TestCase):
    def test_pago_e_prioritario(self):
        pedido = {'data_pagamento': '2026-11-02', 'data_vencimento': '2026-11-01', 'status_aprovacao': 'Aprovado'}
        self.assertEqual(classificar(pedido, date(2026, 11, 9)), 'Pago')

    def test_atrasado_sem_pagamento(self):
        pedido = {'data_pagamento': '', 'data_vencimento': '2026-11-08', 'status_aprovacao': 'Pendente'}
        self.assertEqual(classificar(pedido, date(2026, 11, 9)), 'Atrasado')

    def test_potencial_duplicidade(self):
        item = lambda num: {'id': num, 'fornecedor': 'Alfa', 'numero_documento': 'N1', 'valor': '10.00', 'data_pagamento': '', 'data_vencimento': '2026-11-30', 'status_aprovacao': 'Aprovado'}
        contagem, suspeitas, valor = analisar([item('1'), item('2')], date(2026, 11, 9))
        self.assertEqual(len(suspeitas), 1)
        self.assertEqual(valor, 20)


if __name__ == '__main__':
    unittest.main()
