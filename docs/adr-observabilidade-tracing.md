# ADR: Observabilidade e Tracing CrewAI

## Contexto
O projeto CrewAI já utiliza OpenTelemetry como dependência, mas não há instrumentação explícita de tracing nos fluxos críticos.

## Decisão
Instrumentar funções críticas (execução de agentes, crews, tasks) com spans do OpenTelemetry, permitindo rastreamento distribuído e análise de performance.

## Consequências
- Observabilidade avançada para troubleshooting e otimização.
- Facilidade de integração com backends como Jaeger, Zipkin, etc.
- Migração incremental, sem impacto em funcionalidades existentes.
