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

## Tracing (OpenTelemetry)
- Spans são gerados para execuções críticas (Crew, Agent)
- Integração pronta para Jaeger, Zipkin, etc.
- Exemplo de span:
```
Span(name="crew.run_sequential_process", status=OK, duration=0.321s)
Span(name="agent.execute_task", status=OK, duration=0.045s)
```

## Como validar tracing
- Execute um fluxo E2E
- Use um backend de tracing (ex: Jaeger)
- Verifique os spans gerados para cada execução crítica

## Benchmarks de Performance
- Compare tempos de execução antes/depois de otimizações
- Exemplo:
```
ANTES: crew.run_sequential_process duration=1.23s
DEPOIS: crew.run_sequential_process duration=0.78s
```
- Use logs e spans para análise detalhada
