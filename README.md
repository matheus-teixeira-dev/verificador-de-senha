

# verificador-de-senha

Software que verifica o quão forte uma senha é de acordo com parâmetros atribuídos e um sistema de pontuação.

## Como Rodar

1. Instalar o Python.
2. Baixar o projeto.
3. Entrar na pasta pelo CMD ou PowerShell.
4. Rodar o comando `python verificador.py`.

## Critérios avaliados

- A senha possui 8 ou mais caracteres?
- A senha possui números?
- A senha possui caracteres especiais (não é totalmente alfanumérica)?
- A senha contém caracteres em caixa alta?
- A senha contém caracteres em caixa baixa?

## Pontuação

- Para cada resposta negativa às perguntas acima, a senha perde pontos. São 5 perguntas no total, e cada pergunta vale 1 ponto.
- **5 pontos:** Senha forte (cumpre todas as exigências).
- **3 a 4 pontos:** Senha mediana (descumpre apenas um ou dois requisitos).
- **0 a 2 pontos:** Senha fraca (descumpre mais de dois requisitos, deixando a senha vulnerável).

## O que aprendi

- Aprendi a usar o `if not any(c.is______() for c in _____)`. Isso é muito útil, pois verifica se a condição informada em `c.is____()` é cumprida em pelo menos um dos caracteres. Foi algo novo que aprendi. Existe também o `all`, que verifica todos os caracteres.

- Aprendi também que utilizar `if` e depois `elif` só é útil quando você não precisa verificar tudo. Por exemplo, quando deseja que as outras condições não sejam verificadas após uma delas ser atendida.

