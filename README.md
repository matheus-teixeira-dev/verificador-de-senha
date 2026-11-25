

# verificador-de-senha

Software que verifica o quão forte uma senha é de acordo com parâmetros atribuídos e um sistema de pontuação.

## Como Rodar

1. Instalar o Python.
2. Baixar o projeto.
3. Entrar na pasta pelo CMD ou PowerShell.
4. Rodar o comando `python verificador.py`.

## Critérios avaliados

- Foi adicionada uma lista de senhas comumente utilizadas. Agora, o software verifica se a senha contém alguma dessas senhas e também avalia quantos caracteres diferentes ela possui, atribuindo ou descontando pontos de acordo com os resultados.
- A senha possui 8 ou mais caracteres?
- A senha possui números?
- A senha possui caracteres especiais (não é totalmente alfanumérica)?
- A senha contém caracteres em caixa alta?
- A senha contém caracteres em caixa baixa?

## Pontuação

- Para cada resposta negativa às perguntas acima, a senha perde pontos. São 5 perguntas no total, e cada pergunta vale 1 ponto.
- **6 pontos:** Senha forte (cumpre todas as exigências).
- **4 a 5 pontos:** Senha mediana (descumpre apenas um ou dois requisitos).
- **0 a 3 pontos:** Senha fraca (descumpre mais de dois requisitos, deixando a senha vulnerável).

## O que aprendi

- Aprendi a usar o `if not any(c.is______() for c in _____)`. Isso é muito útil, pois verifica se a condição informada em `c.is____()` é cumprida em pelo menos um dos caracteres. Foi algo novo que aprendi. Existe também o `all`, que verifica todos os caracteres.

- Aprendi também que utilizar `if` e depois `elif` só é útil quando você não precisa verificar tudo. Por exemplo, quando deseja que as outras condições não sejam verificadas após uma delas ser atendida.





- Aprendi a utilizar uma forma de percorrer uma lista e comparar seus elementos com uma `string`, utilizando:

```python
for palavra in arquivo:
    if palavra.lower() in senha.lower():
        sobra = len(senha) - len(palavra)
        if sobra < 5:
            print("A seguinte senha foi encontrada em uma lista de senhas vazadas:", palavra, "Recomendamos adicionar mais alguns elementos ou criar outra senha.")
            pontos = pontos - 1
```

Basicamente, `for palavra in arquivo:` percorre cada palavra contida no arquivo.

Já `if palavra.lower() in senha.lower():` compara as palavras do arquivo com a senha, ignorando diferenças entre letras maiúsculas e minúsculas.

A utilização de `len()` também foi interessante, pois permite calcular a quantidade de caracteres da senha e da palavra encontrada. Nesse caso, `sobra = len(senha) - len(palavra)` calcula a diferença entre os tamanhos.

Por fim, `if sobra < 5:` verifica se essa diferença é menor que 5. Caso seja, o programa exibe um aviso e desconta um ponto da pontuação da senha.


