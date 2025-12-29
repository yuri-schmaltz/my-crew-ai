# Runbook: Release Checklist CrewAI

## Pré-requisitos
- Todos os testes passam (`pytest`)
- Cobertura > 80% (ver badge Codecov)
- Lint sem erros (`flake8 .`)
- Logs aparecem em formato JSON
- Métricas básicas instrumentadas

## Passos
1. Atualizar dependências (`poetry update`)
2. Rodar testes e cobertura
3. Validar logs e métricas
4. Revisar ADRs e docs
5. Validar pipeline CI/CD
6. Tag e release

## Troubleshooting
- Falha em testes: rodar `pytest -v`
- Falha em lint: rodar `flake8 .`
- Logs não aparecem: revisar inicialização em `__init__.py`
- Métricas ausentes: aplicar decorator `metric_time`
