
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