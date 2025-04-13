# Interpolação de Lagrange

Este projeto realiza a interpolação polinomial de Lagrange com base em pontos fornecidos pelo usuário. Utiliza a biblioteca `sympy` para cálculos simbólicos e pode gerar um gráfico do polinômio interpolador.

O projeto está em português por se tratar de uma ferramenta de uso pessoal.

## Instalação

O projeto utiliza o gerenciador de pacotes [`uv`](https://github.com/astral-sh/uv), sendo possível realizar a instalação com o seguinte comando:

```bash
uv pip install .
```

Alternativamente, é possível instalar as dependências definidas no `pyproject.toml` utilizando o `pip` e executar o arquivo `main.py` diretamente:

```bash
pip install sympy matplotlib numpy # etc...
python main.py
```

## Uso

Execute o arquivo `main.py`. O programa solicitará os dados necessários ao usuário interativamente.
