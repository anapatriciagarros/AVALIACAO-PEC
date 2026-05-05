# Sistema de Controle de Estoque com CRUD em Python
ALUNA - ANA PATRÍCIA GARROS VIEGAS

Este projeto implementa um sistema simples de controle de estoque utilizando operações de CRUD em Python.

CRUD significa:

- **C**reate: cadastrar produto;
- **R**ead: listar ou buscar produto;
- **U**pdate: atualizar produto;
- **D**elete: remover produto.

O diferencial do projeto é que o mesmo problema foi resolvido utilizando dois paradigmas de programação no mesmo código:

1. **Paradigma Imperativo**
2. **Paradigma Funcional**

A separação entre os dois paradigmas foi feita de forma clara dentro do código, permitindo comparar como cada abordagem resolve o mesmo problema.

Utilizei o paradigma funcional na parte das operações sobre os dados do estoque, como cadastrar, buscar, atualizar, remover, listar e calcular o valor total. Essa parte foi implementada com funções puras, imutabilidade, map, filter e função de ordem superior.

Utilizei o paradigma imperativo na parte de controle do sistema, como menu, entrada de dados, saída de mensagens, estruturas condicionais, laços de repetição e atualização da variável estoque.

Dessa forma, o usuário final utiliza apenas um sistema de controle de estoque, mas internamente o código demonstra a integração entre os dois paradigmas. O paradigma funcional ficou responsável pela lógica de manipulação dos dados, enquanto o paradigma imperativo ficou responsável pelo fluxo de execução e pela interação com o usuário.

---

## Objetivo do Projeto

O objetivo deste trabalho é demonstrar, de forma prática, como diferentes paradigmas de programação podem ser utilizados para resolver um mesmo problema computacional.

O problema escolhido foi um sistema de controle de estoque, pois ele permite aplicar operações básicas de cadastro, consulta, atualização e remoção de dados.

---

## Funcionalidades do Sistema

O sistema permite:

- Cadastrar produtos;
- Listar produtos cadastrados;
- Buscar produtos por código;
- Atualizar dados de um produto;
- Remover produtos do estoque;

1. Diferença percebida entre os paradigmas

A principal diferença percebida entre os paradigmas imperativo e funcional está na forma como cada um organiza a solução do problema.

No paradigma imperativo, o programa é construído como uma sequência de comandos que modificam diretamente o estado do sistema. No caso do controle de estoque, a lista de produtos é alterada diretamente durante as operações de cadastro, atualização e remoção. Ou seja, o foco está em como o programa deve executar cada passo.

Já no paradigma funcional, o foco está mais em o que deve ser feito com os dados. As funções recebem informações, processam essas informações e retornam novos resultados, evitando alterar diretamente os dados originais. No sistema de estoque, isso aparece quando as funções retornam uma nova lista de produtos em vez de modificar a lista antiga diretamente.

Assim, o paradigma imperativo trabalha mais com mudança de estado e controle sequencial, enquanto o paradigma funcional valoriza funções puras, imutabilidade e transformação de dados.

2. Vantagens e desvantagens de cada abordagem
Paradigma imperativo

A principal vantagem do paradigma imperativo é que ele é mais simples de entender no início, pois segue uma lógica parecida com uma receita: primeiro faz uma coisa, depois outra, depois outra. Isso facilita a criação de menus, entradas de dados, mensagens para o usuário e controle do fluxo do programa.

Outra vantagem é que ele se encaixa bem em sistemas interativos, como um CRUD, porque operações como input, print, while, if e alteração de variáveis fazem parte natural desse estilo.

Por outro lado, a desvantagem é que o uso constante de variáveis mutáveis pode deixar o código mais difícil de controlar conforme o sistema cresce. Como os dados são alterados diretamente, aumenta o risco de erros, principalmente quando várias partes do programa mexem no mesmo estado.

Paradigma funcional

A principal vantagem do paradigma funcional é a maior previsibilidade. Como as funções recebem dados e retornam novos dados, sem alterar diretamente o estado original, fica mais fácil testar cada parte do programa separadamente.

Outra vantagem é que o código tende a ficar mais organizado quando as regras do sistema são separadas em funções puras. Isso ajuda na manutenção, porque uma função como adicionar_produto, remover_produto ou buscar_produto pode ser analisada isoladamente.

A desvantagem é que o paradigma funcional pode parecer menos intuitivo para quem está começando, principalmente por causa de conceitos como imutabilidade, funções puras, map, filter e funções de ordem superior. Além disso, em programas com interação direta com o usuário, como menus e entradas de dados, ainda é necessário usar uma parte imperativa.

3. Qual abordagem foi mais fácil ou difícil e por quê

A abordagem imperativa foi mais fácil de desenvolver, porque ela segue uma lógica mais direta e próxima do funcionamento comum de um programa com menu. É mais simples pensar em passos sequenciais: mostrar opções, receber a escolha do usuário, verificar a opção com if e executar a ação correspondente.

A abordagem funcional foi mais difícil, porque exige pensar de uma forma diferente. Em vez de alterar diretamente a lista de produtos, é necessário criar funções que retornem uma nova versão da lista. Isso exige mais cuidado na organização do código e na separação entre processamento de dados e interação com o usuário.

No entanto, apesar de ser mais difícil no começo, a abordagem funcional tornou o código mais organizado nas regras principais do sistema. A dificuldade maior não está em escrever uma função isolada, mas em mudar o raciocínio: sair da ideia de “alterar o estoque” para a ideia de “gerar um novo estoque a partir do anterior”.

4. Impacto na legibilidade e manutenção do código

O uso dos dois paradigmas teve um impacto positivo na legibilidade e na manutenção do código, desde que cada parte ficasse bem separada.

A parte imperativa deixou o fluxo do programa mais fácil de acompanhar, principalmente no menu principal. Ela mostra claramente o que acontece em cada opção escolhida pelo usuário. Isso melhora a legibilidade para entender a execução geral do sistema.

A parte funcional melhorou a manutenção, porque concentrou as regras do estoque em funções específicas. Por exemplo, se for necessário mudar a forma de remover um produto, basta alterar a função remover_produto. Se for necessário mudar a forma de calcular o valor total do estoque, basta alterar a função calcular_valor_total_estoque.

Porém, se os paradigmas fossem misturados sem organização, o código poderia ficar confuso. A separação entre funções funcionais e controle imperativo foi essencial para deixar o sistema mais claro.

Portanto, a combinação dos dois paradigmas tornou o código mais equilibrado: o paradigma imperativo ficou responsável pela interação com o usuário, enquanto o paradigma funcional ficou responsável pelas operações sobre os dados. Isso melhora a leitura, facilita testes e torna futuras alterações mais simples.




