# Honeypot SSH com Cowrie e análise em Python

## Sobre o projeto

Projeto de estudo em Cybersecurity e Infraestrutura que utiliza o Cowrie para simular um serviço SSH e registrar tentativas de autenticação. Os registros são analisados com scripts Python para gerar estatísticas e visualizações.

## Tecnologias utilizadas

- Ubuntu Linux
- Cowrie SSH Honeypot
- Python 3
- Matplotlib
- Git

## Objetivos

- Compreender o funcionamento de um honeypot SSH.
- Observar e analisar eventos de autenticação.
- Automatizar a leitura de logs com Python.
- Produzir relatórios e gráficos a partir dos dados coletados.

## Estrutura

- `analisar_logs.py`: analisa os eventos de autenticação e gera um resumo.
- `gerar_grafico.py`: cria um gráfico de tentativas de login por horário.
- `relatorio_horario.png`: visualização gerada pelo script.

## Como executar

1. Instale o Cowrie em um ambiente Linux e configure um ambiente virtual Python.
2. Inicie o Cowrie e gere eventos de teste.
3. Coloque os scripts na pasta do projeto.
4. Execute:

```bash
python analisar_logs.py
python gerar_grafico.py
```

Os scripts esperam encontrar os eventos em `var/log/cowrie/cowrie.json`, relativo à pasta em que são executados. Ajuste o caminho se necessário.

## Resultados e limitações

Os resultados iniciais foram obtidos por conexões de teste realizadas localmente. Eles validam a geração e análise dos logs, mas não representam ataques externos nem uma coleta de sete dias na internet.

Uma etapa futura é executar o honeypot em uma máquina isolada na nuvem, observar eventos durante um período definido e documentar os resultados reais.

## Segurança

O honeypot deve ser executado em uma máquina isolada, sem dados pessoais ou serviços sensíveis. Não exponha sua máquina pessoal à internet para realizar o experimento.
