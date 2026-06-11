# Projeto de Testes Python

Este repositorio contem um pequeno projeto Python com dois scripts em `src/` e testes unitarios em `tests/`.

## Instalacao

Instale as dependencas com:

```bash
python -m pip install -r requirements.txt
```

## Como executar os testes localmente

Execute:

```bash
python -m pytest --cov=src --cov-report=term-missing --cov-fail-under=70
```

## Interpretacao dos resultados no GitHub Actions

A aba `Actions` mostra o pipeline de CI. Este workflow executa os testes em cada `push` para `develop` ou `main` e em cada `pull_request` para `main`.

Se a execucao falhar, verifique as etapas de `Install dependencies` e `Run tests with coverage`.

## Cobertura atingida pelo projeto

Cobertura minima exigida: `70%`.
Cobertura atual obtida pelo projeto: `70%`.
