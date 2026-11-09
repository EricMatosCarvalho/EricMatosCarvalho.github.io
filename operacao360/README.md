# Operação 360 - estudo de caso educacional

> **Projeto fictício e em desenvolvimento.** Não há cliente real, não há implantação real da V360 e nenhum dado deste repositório pertence a terceiros.

## Contexto
A Oficina Aurora é uma empresa fictícia que precisa organizar o fluxo de recebimento de documentos, aprovação e pagamento.

## Objetivo de aprendizagem
Praticar mapeamento AS-IS/TO-BE, Kanban, acompanhamento de projeto, indicadores simples e Python aplicado a processos.

## Como executar

```bash
python --version
python analise_pedidos.py --data-referencia 2026-11-09
python -m unittest discover -v
```

## Arquivos
- `pedidos_ficticios.csv`: registros inventados para testes.
- `analise_pedidos.py`: análise didática com biblioteca padrão do Python.
- `test_analise_pedidos.py`: testes unitários básicos.
- `quadro_kanban.csv`: tarefas iniciais, altere os status conforme executar.
- `fluxo_processo.mmd`: diagrama Mermaid básico.

## Regras e cuidados
- Uma duplicidade encontrada é **suspeita**, não confirmação de pagamento duplicado.
- “Atrasado” significa vencido na data de referência e ainda não pago.
- O script foi disponibilizado como ponto de partida para estudo. Antes de atribuir autoria de implementação, execute, estude, adapte e explique o código por conta própria.

## Próximas entregas do estudante (não marcadas como feitas)
- [ ] Desenhar AS-IS e TO-BE com decisões e responsáveis.
- [ ] Executar script e conferir resultados manualmente.
- [ ] Adicionar ao menos um teste por regra.
- [ ] Criar matriz simples de riscos.
- [ ] Escrever relatório de status para cliente fictício.
- [ ] Explicar aprendizados e limitações no README.

## Portfólio e ética
Ao publicar, identificar claramente o estudo como simulação educacional. Não usar logotipo/marca da V360 dando a entender vínculo profissional.
