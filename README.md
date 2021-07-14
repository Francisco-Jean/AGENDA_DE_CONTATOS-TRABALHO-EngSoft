# SISTEMA WEB AGENDA DE CONTATOS
### Arquivos e documentação de um sistema web de agenda de contatos desenvolvido na disciplina de engenharia de software - IFCE - CAMPUS FORTALEZA - 2021.1 - Integrado em informática - P7
#### Professor: Cesar Olavo

### Membros da equipe:
|NOME|EMAIL|
| -------- | -------- |
|Efraim Ferreira Damasceno|efraim.ferreira.damasceno07@aluno.ifce.edu.br|
|Francisco Jean da Silva de Sousa|francisco.jean.silva08@aluno.ifce.edu.br|
|Jonas Oliveira|jonas.oliveira.santos08@aluno.ifce.edu.br|
|Moises Ferreira|moises.ferreira41@aluno.ifce.edu.br|

## 1. Requisitos do sistema:

- Usuários devem ser identificados por id e senha.
- A aplicação deve permitir inserir e apagar contatos e atualizar dados de um contato.
- O sistema deve oferecer eficientes mecanismos de busca de dados.
- Deve-se poder fazer listagens de todos os contatos., por grupos de contato ou por campo (p.ex.
Nome, CEP, cidade, etc.).
- uma interface de usuário prática e atraente

## 2. Telas do sistema:

- Tela Home. Aqui é possível visualizar alguns dados sobre o site.

![Captura de Tela (12)](https://user-images.githubusercontent.com/71938841/125688189-1fd0c5e8-5451-4c71-a6d5-aae51d784b4c.png)



- Tela de cadastro. Aqui o usuário entrará com um nome e uma senha, podendo realizar seu cadastro no sistema.

![Captura de Tela (13)](https://user-images.githubusercontent.com/71938841/125688211-d7762ab8-318b-49af-a60e-0a695a219265.png)



- Tela de cadastro de contatos. O usuário, após se cadastrar, poderá criar contatos que serão vinculados à sua conta. Possíveis erros, como o usuário tentar criar um contato sem estar cadastrado, ou não inserir todos os dados, são devidamente tratados.

![Captura de Tela (14)](https://user-images.githubusercontent.com/71938841/125688236-f58cc052-e11a-4fc2-8921-d515e4fa5750.png)



- Tela de pesquisa de contatos. Aqui o usuário poderá buscar todos os seus contatos cadastrados, podendo filtrar por nome, número ou listar todos os seus contatos.

![Captura de Tela (15)](https://user-images.githubusercontent.com/71938841/125688253-43b5de5a-fab5-4589-ba01-2226064d6dcf.png)



## 3. UML:

#### A. Casos de uso do sistema:

- Criação de um novo contato (Necessário cadastro)
- Busca dos contatos de um usuário por nome (Necessário cadastro)
- Busca dos contatos de um usuário por número (Necessário cadastro)
- Busca por todos os contatos de um usuário (Necessário cadastro)



#### B. Diagramas de sequência:

- Busca de um contato:

![sequence-diagram (1)](https://user-images.githubusercontent.com/71938841/125536959-d06e1916-2d62-4784-a4f1-ee670c910d5c.png)


- Adição de um novo grupo de contato:

![sequence-diagram (2)](https://user-images.githubusercontent.com/71938841/125537657-bb0c075e-f90f-4c51-9016-d9d86b8891c6.png)



#### C. Diagramas de atividade:

- Listagem de um dado contato:

![activity-diagram](https://user-images.githubusercontent.com/71938841/125543760-381cd994-aa43-4d67-9289-275388056059.png)


- Mapa de navegação de telas:

![activity-diagram (5)](https://user-images.githubusercontent.com/71938841/125557546-44eb5f99-8b97-48d3-b580-331111fbd79a.png)




#### D. Diagramas de classe:

![class-diagram](https://user-images.githubusercontent.com/71938841/125692152-0d23bd96-e1ee-4f63-bf38-70382831ea88.png)



#### E. Diagramas de estado de um objeto Conta:

![state-diagram](https://user-images.githubusercontent.com/71938841/125558470-2920787e-1f65-43b0-a136-3a419c5e3d3e.png)


#### F. Explicitar a arquitetura escolhida:
  O sistema é estruturado conforme a arquitetura MVC(Model-View-Controll). Buscouse-se dividir seus módulos da melhor forma possível, agregando facilidade de manutenção, bem como o reuso de partes do sistema em quaisquer outras aplicações.
  
- Módulo App: Módulo que separa as entidades do MVC da execução principal da aplicação, buscando maior desacoplamento entre os dados, controladoes e vizualisações.


- Módulo models: Especifica como as entidades são constituídas, formas de aquisição de dados, além de realizar consultas, inserções e exclusões no bancode dados.


- Módulo  controllers: Realiza a ligação entre os dados e a amostragem dos mesmos, recebendo todas as requisições do sistema e enviand-as para o tratamento adequado.


- Módulos Estatic e Templates: Usados para guardar os componentes que estruturam as páginas do sistema, sendo uma abstração do VIEW do MVC.

![component-diagram](https://user-images.githubusercontent.com/71938841/125561574-74ef6746-8469-4900-a9d1-c645c02023a5.png)


#### Editor UML Utilizado:
- GenMyModel
- Link: https://www.genmymodel.com/

#### Framework:
- Flask 2.0.1
- Link: https://www.palletsprojects.com/p/flask/

#### Banco de dados:
- MySQL 8.0
- Link: https://www.mysql.com/



#### Agradecimentos:
- A equipe agradece ao professor Cesar Olavo pelo ótimo semestre! Buscamos dar nosso máximo não apenas em prol de questões de nota, mas também para desenvolver nossos conhecimentos sobre o mundo do desenvolvimento de software. Temos ciência que, mesmo se não seguirmos nossa tragetória diretamente interligada aos conhecimentos propostos em sala de aula, todos esses dias que passamos estudando essa cadeira não foram em vão.
