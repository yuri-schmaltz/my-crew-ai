# Métricas e Instrumentação CrewAI

## Logs
- Formato: JSON
- Nível: INFO (default)
- Exemplo:
```json
{"timestamp": "2025-12-29 10:00:00", "level": "INFO", "name": "crewai.module", "message": "Execução iniciada"}
```

## Métricas
- Tempo de execução de funções críticas
- Exemplo:
```
METRIC: funcao_critica duration=0.123s
```

## Como validar
- Executar funções decoradas com `@metric_time` e verificar logs
- Rodar testes e conferir logs no console
