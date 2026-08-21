Perguntas:

Um documento curto (README.md ou similar) respondendo, com justificativa, as perguntas de projeto que os Capítulos 5 a 7 deixaram em aberto:
No Fechamento, os lançamentos originais foram copiados ou referenciados? Por quê?
Conciliacao virou uma classe própria ou um método de Fechamento? Por quê?
O que acontece quando não há lançamentos no período, ou quando a conciliação não bate?

Respostas:

No Fechamento, os lançamentos originais foram copiados ou referenciados? Por quê?
Resposta: Referenciados, self.lancamentos = lancamentos, a classe fechamento serve apenas para ler e somar os valores das movimentações.

Conciliacao virou uma classe própria ou um método de Fechamento? Por quê?
Resposta: A classe Conciliacao foi substituída por Orcamento, sendo independente de Fechamento, enquanto o Fechamento reúne os saldos gerais o Orcamento gerencia os limites por categoria.

O que acontece quando não há lançamentos no período, ou quando a conciliação não bate?
Resposta: Quando não há lançamentos o sistema inicializa a lista vazia ([]) e os métodos de cálculo retornam 0.0 , sem travar nem gerar erros. E quando no meu caso o Orcamento estoura o limite a classe avisa o estouro retornando True no método estourou_limite() e valores negativos em valor_restante() . 
