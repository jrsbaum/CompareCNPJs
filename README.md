
## CompareCNPJs
#### Este projeto é um script que realiza uma série de operações em dois bancos de dados MongoDB separados. O script primeiro importa vários módulos, incluindo o `db.py`, que contém funções para se conectar aos bancos de dados MongoDB, e `new_obj.py`, que contém uma função para criar um novo objeto com os dados dos dois bancos de dados originais.

#### Na função `main()`, o script pede ao usuário para pressionar qualquer tecla para continuar e, em seguida, recupera as coleções dos dois bancos de dados usando as funções `get_database1()` e `get_database2()` do db.py. Essas coleções são convertidas em listas e o script itera sobre eles para encontrar processos com o mesmo CNPJ em ambas as coleções. Quando processos correspondentes são encontrados, a função `create_new_object()` é chamada para criar um novo objeto com informações combinadas dos processos originais. A lista de novos objetos é então inserida em uma nova coleção no banco de dados.


### Para o código funcionar, precisa de um arquivo cfg.py que não foi versionado. O arquivo contém o seguinte código:

````
MONGO_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]"

DATABASE_NAME1 = "database_name1"
COLLECTION_NAME1 = "collection_name1"

DATABASE_NAME2 = "database_name2"
COLLECTION_NAME2 = "collection_name2"

NEW_DATABASE_NAME = "database_name3"
NEW_COLLECTION_NAME = "collection_name3"

````

#### Substitua os valores pelos valores a serem usados.


## Task: Coletar dados de dois bancos de dados e uni-los em uma nova Collection

Terá que ler dados de duas Collections diferentes e adicionar um novo Objeto a uma nova Collection.

A primeira Collection fica em uma Database, chamado BigDataCorpProcesses, e a Collection se chama Processes.

A segunda Collection fica em uma Database, chamado NeoWay, e a Collection se chama Processes.

A partir dessas duas Collections, crie o novo objeto.
Salve esse novo objeto em uma nova Database, chamada SummarizedProcesses, e a Collection irá se chamar Processes.

Use a string connection fornecida anteriormente.
Coloque a string connection, o nome das Databases e as Collections em um arquivo a parte
chamado cfg.py que não será versionado.
 
Para montar o novo objeto, o script verifica dentro das duas Collections o CNPJ. Se ele
achar o mesmo CNPJ em ambas, ele adiciona esse CNPJ no início do objeto.

Depois ele criará um objeto chamado Processos, onde conterá o número de cada processo, e um marcador mostrando se aquele processo existe dentro de cada Collection.

Assim, o script busca por um Número do Processo, compara se são iguais e insere-o. Se ele existir dentro do banco daquele banco de dados, ele marca como True.

Além disso, para cada vez que o número do processo existir naquela Collection, ele marca com +1 no campo QtdBigDataCorp ou QtdNeoWay, dependendo da Collection que ele foi encontrado.

Também nesse novo objeto, temos os campos QtdBigDataCorpSemNeoWay, QtdNeoWaySemBigDataCorp e QtdAmbos.


