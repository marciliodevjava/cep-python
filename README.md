## API de Consulta de CEP

Esta API desenvolvida em Python com Flask e Flask-RESTful oferece uma solução eficiente para consulta de CEPs, utilizando a integração com a API ViaCEP para obter informações detalhadas sobre localidades. Além disso, a aplicação armazena os CEPs previamente consultados localmente, eliminando a necessidade de consultas repetitivas.

### Funcionalidades Principais

**Consulta de CEP Via ViaCEP:**
- Utiliza a API ViaCEP para obter dados detalhados associados a um CEP específico, como logradouro, bairro, cidade, estado, entre outros.

**Armazenamento Local de Consultas:**
- Mantém um registro local dos CEPs consultados, reduzindo o tempo de resposta ao evitar consultas repetitivas à API externa.

### Tecnologias Utilizadas

- *Python:* Linguagem de programação versátil e de fácil aprendizado.
- *Flask:* Framework leve para construção de aplicativos web em Python.
- *Flask-RESTful:* Facilita o desenvolvimento de APIs RESTful usando Flask.
- *Requests:* Biblioteca para realizar requisições HTTP em Python.

### Como Utilizar

**Pré-requisitos:**
- Certifique-se de ter o Python 3.11 (versão 3.9 ou superior) instalado em seu ambiente.
- Clone este repositório.

### Endpoints Principais

**Consulta de CEP:**
- `GET /cep/{cep}`: Retorna informações detalhadas sobre o CEP especificado.

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar esta API.
