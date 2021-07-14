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

### 3. UML:

#### A. Casos de uso do sistema:



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



#### E. Diagramas de estado de um objeto Conta:

![state-diagram](https://user-images.githubusercontent.com/71938841/125558470-2920787e-1f65-43b0-a136-3a419c5e3d3e.png)


#### F. Explicitar a arquitetura escolhida:
  O sistema é estruturado conforma a arquitetura MVC(Model-View-Controll). Buscouse-se dividir seus módulos da melhor forma possível, agregando facilidade de manutenção, bem como o reuso de partes do sistema em quaisquer outras aplicações.
  
- Módulo App: Módulo que separa as entidades do MVC da execução principal da aplicação, buscando maior desacoplamento entre os dados, controladoes e vizualisações.



- Módulo models: Especifica como as entidades são constituídas, formas de aquisição de dados, além de realizar consultas, inserções e exclusões no bancode dados.



- Módulo  controllers: Realiza a ligação entre os dados e a amostragem dos mesmos, recebendo todas as requisições do sistema e enviand-as para o tratamento adequado.



- Módulos Estatic e Templates: Usados para guardar os componentes que estruturam as páginas do sistema, sendo uma abstração do VIEW do MVC.

![component-diagram](https://user-images.githubusercontent.com/71938841/125561574-74ef6746-8469-4900-a9d1-c645c02023a5.png)



#### G. Elaborar os diagramas de implantação:


