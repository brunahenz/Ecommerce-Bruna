## MÓDULO 2 -- 

## Perguntas:

## No Fechamento, os lançamentos originais foram copiados ou referenciados? Por quê?

## Conciliacao virou uma classe própria ou um método de Fechamento? Por quê?

## O que acontece quando não há lançamentos no período, ou quando a conciliação não bate?

## Respostas:

No Fechamento, os lançamentos originais foram copiados ou referenciados? Por quê?
Resposta: Referenciados, self.lancamentos = lancamentos, a classe fechamento serve apenas para ler e somar os valores das movimentações.

Conciliacao virou uma classe própria ou um método de Fechamento? Por quê?
Resposta: A classe Conciliacao foi substituída por Orcamento, sendo independente de Fechamento, enquanto o Fechamento reúne os saldos gerais o Orcamento gerencia os limites por categoria.

O que acontece quando não há lançamentos no período, ou quando a conciliação não bate?
Resposta: Quando não há lançamentos o sistema inicializa a lista vazia ([]) e os métodos de cálculo retornam 0.0 , sem travar nem gerar erros. E quando no meu caso o Orcamento estoura o limite a classe avisa o estouro retornando True no método estourou_limite() e valores negativos em valor_restante() . 



## MÓDULO 3 --


## As estratégias de rendimento, juros e correção monetária usam interfaces separadas ou a mesma interface?

Eu escolhi deixar cada uma com sua própria interface, porque, apesar de todas serem usadas em cálculos financeiros, cada uma tem uma função diferente. O rendimento calcula quanto um valor pode render, os juros calculam o aumento de um valor ao longo do tempo e a correção monetária serve para atualizar valores.

Assim, fica mais fácil entender o código e adicionar novas regras sem misturar tudo em uma classe só.

## Onde a estratégia escolhida fica guardada?

No caso do cupom, a estratégia de desconto fica guardada dentro da própria classe Cupom. Dessa forma, cada cupom tem sua regra de desconto e pode utilizá-la enquanto estiver dentro da validade.

Nas outras estratégias, eu criei classes separadas para cada tipo de cálculo. Assim, posso utilizar a regra necessária de acordo com a situação, sem precisar alterar as outras classes.

## Que nova regra eu conseguiria adicionar sem editar as classes que já existem?

Eu poderia criar uma nova estratégia de juros, uma forma diferente de rendimento ou outro tipo de correção monetária. Para isso, seria necessário criar uma nova classe seguindo a interface correspondente, sem precisar modificar as estratégias que já estão funcionando.

## Adaptação para o projeto financeiro

Como os exemplos dos capítulos envolviam descontos, cupons e frete, precisei adaptar essas ideias para o meu projeto. O desconto representa um abatimento financeiro, o cupom funciona como um benefício com prazo de validade e o conceito de frete foi adaptado para o cálculo de taxas de operações financeiras.

A ideia foi aproveitar os conceitos estudados nos capítulos e aplicá-los ao projeto que eu já vinha desenvolvendo, em vez de criar um sistema de loja separado.

## Testes

Criei testes automatizados com pytest para verificar se os cálculos funcionam corretamente e se os erros esperados são tratados. Para executar todos os testes, basta utilizar o comando:

```bash
uv run pytest -v
```
## Módulo 4-

## Perguntas:

## Em cada caso (leitor, importador, exportador), você usou Simple Factory ou Factory Method? O que te fez escolher?

## Nos seus serviços, o que é injetado e o que ainda é criado internamente? Por quê?

## Onde está sua raiz de composição? Que colaborador você conseguiria substituir hoje sem editar nenhum serviço?

## Respostas:

Usei Simple Factory para escolher leitores e importadores. Para os exportadores, usei Factory Method, pois a classe base define o fluxo e as subclasses criam os documentos de formas diferentes.

O serviço recebe as fábricas de leitores e importadores e o exportador pelo construtor. Dessa forma, não precisa criar essas dependências diretamente.

Fica em ecommerce/aplicacao.py, na função montar_aplicacao(). Nos testes, consigo substituir os colaboradores por objetos falsos sem precisar alterar o serviço.


