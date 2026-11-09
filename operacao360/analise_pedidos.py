"""Operação 360: exercício educativo com dados fictícios.
Uso: python analise_pedidos.py --data-referencia 2026-11-09
Nenhuma conclusão deste programa substitui conferência humana.
"""
import argparse
import csv
from collections import defaultdict, Counter
from datetime import date
from pathlib import Path


def classificar(pedido, referencia):
    if pedido['data_pagamento']:
        return 'Pago'
    if date.fromisoformat(pedido['data_vencimento']) < referencia:
        return 'Atrasado'
    if pedido['status_aprovacao'] != 'Aprovado':
        return 'Aguardando aprovacao'
    return 'Em aberto'


def analisar(pedidos, referencia):
    contagem = Counter(classificar(p, referencia) for p in pedidos)
    grupos = defaultdict(list)
    for pedido in pedidos:
        chave = (pedido['fornecedor'].lower().strip(),
                 pedido['numero_documento'].lower().strip())
        grupos[chave].append(pedido['id'])
    suspeitas = {chave: ids for chave, ids in grupos.items() if len(ids) > 1}
    total_valor = sum(float(p['valor']) for p in pedidos)
    return contagem, suspeitas, total_valor


def main():
    parser = argparse.ArgumentParser(description='Analisa documentos ficticios')
    parser.add_argument('--data-referencia', default=date.today().isoformat())
    args = parser.parse_args()
    referencia = date.fromisoformat(args.data_referencia)
    caminho = Path(__file__).with_name('pedidos_ficticios.csv')
    with open(caminho, encoding='utf-8-sig', newline='') as arquivo:
        pedidos = list(csv.DictReader(arquivo))
    contagem, suspeitas, total_valor = analisar(pedidos, referencia)
    print('OPERACAO 360 | SIMULACAO EDUCACIONAL')
    print('Data de referencia:', referencia)
    print('Documentos:', len(pedidos))
    print('Valor cadastrado (sem deduplicar): R$ %.2f' % total_valor)
    for situacao in ['Pago', 'Atrasado', 'Aguardando aprovacao', 'Em aberto']:
        print('%s: %d' % (situacao, contagem[situacao]))
    print('Grupos com possiveis duplicidades:', len(suspeitas))
    for (fornecedor, numero), ids in sorted(suspeitas.items()):
        print('  -', fornecedor, numero, ', '.join(ids))
    print('AVISO: duplicidade e apenas suspeita e exige validacao humana.')


if __name__ == '__main__':
    main()
