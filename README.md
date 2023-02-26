Teste básico para encontrar padrões em arquivos de tezto, nesse eemplo os padrões seriam nomes, porém é facilmente percebível o erro, pois o padrão pode consedierar palavras começando com letra maiscula logo após um ponto final e não necessiariamente é um nome, irei consertar isso. 

Explicação do código na primeira versão: 
    Começamos importando o módulo de expressões regulares re.
    Definimos a função nomes().
    Definimos a variável simple_string contendo a string na qual os nomes serão procurados.
    Definimos o padrão de expressão regular padrao usando a borda de palavra \b para encontrar o início e o fim de uma palavra, [A-Z] para encontrar uma letra maiúscula e [a-z]+ para encontrar uma ou mais letras minúsculas. Isso encontrará nomes que começam com uma letra maiúscula e são seguidos por uma ou mais letras minúsculas.
    Usamos a função re.findall() para encontrar todas as correspondências do padrão padrao na simple_string. Esta função retorna uma lista de todas as correspondências não sobrepostas na ordem em que são encontradas.
    Retornamos a lista de nomes encontrados.
