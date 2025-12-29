# Release Automation CrewAI

## Objetivo
Automatizar o processo de release, garantindo versionamento semântico, changelog e publicação segura.

## Passos
1. Validar CI/CD e quality gates
2. Gerar changelog automático (ex: conventional commits)
3. Bump de versão com devtools
4. Tag e release no GitHub
5. Publicação no PyPI (se aplicável)

## Ferramentas sugeridas
- devtools (já incluso)
- GitHub Actions para release/tag
- Commitizen ou semantic-release (opcional)

## Critérios de aceite
- Releases só ocorrem se todos os testes e quality gates passarem
- Changelog e versão sempre atualizados
- Rollback documentado em caso de falha
