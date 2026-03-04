Python Banco de dados
=====================

Resumo
------
Projeto de análise de cancelamentos de clientes. O notebook `inicial.ipynb` contém a análise principal: leitura do arquivo `cancelamentos.csv`, limpeza, contagens e geração de gráficos com `plotly`.

O que foi feito
--------------
- Leitura e limpeza dos dados (`pandas`).
- Contagem de motivos de cancelamento.
- Geração de gráficos interativos (HTML) e imagens (PNG) usando `plotly`.

Arquivos principais
-------------------
- `inicial.ipynb`: notebook com a análise passo a passo.
- `scripts/export_graphs.py`: script que gera e salva os gráficos em `figures/`.
- `requirements.txt`: dependências do projeto.
- `.gitignore`: padrões para ignorar arquivos locais.

Repositório remoto
------------------
Este projeto está publicado em: https://github.com/VinihMarteleto/Python-Banco-de-dados

Figuras
------
As figuras geradas estão em `figures/` no repositório (HTML e PNG quando disponível). Você também pode abrir os arquivos HTML localmente para ver os gráficos interativos.

Como contribuir / mudanças locais
--------------------------------
- Faça alterações no notebook ou nos scripts localmente.
- Rode `python scripts/export_graphs.py` para regenerar as figuras.
- Atualize `requirements.txt` se adicionar novas dependências.

Uso rápido
---------
1. Instale dependências: `pip install -r requirements.txt`
2. Execute: `python scripts/export_graphs.py` (gera HTML/PNG em `figures/`)
3. Abra `inicial.ipynb` e execute as células na ordem para reproduzir a análise.

Como reproduzir
---------------
1. Crie e ative um ambiente virtual (opcional):

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Gere os gráficos (salva em `figures/`):

```bash
python scripts/export_graphs.py
```

Dependências
------------
- pandas
- plotly
- nbformat
- kaleido (para exportar imagens PNG)

Observações
-----------
- Os arquivos de figura são salvos em `figures/` como arquivos HTML e PNG.
- Se quiser apenas visualizar no notebook, abra `inicial.ipynb` e execute as células na ordem.

Contato
-------
Autor: Usuário
