### Objetivo: Receber um invoke do CLI e retornar uma saída no terminal, usar o Chalice para escrever uma aplicação serverless.

Termos:
#### REST API:
* Interface de Programação de Aplicação por Transferência de Estado Representacional;
* É um estilo arquitetural e um conjunto de convenções para construir serviços web;
* permitem a comunicação entre diferentes aplicativos de software pela internet, utilizando métodos padrão do HTTP, como GET, POST, PUT e DELETE. 
* Normalmente utilizam JSON ou XML como formato de dados para solicitações e respostas.

#### CHALICE:
*  framework da AWS para desenvolvimento de aplicativos serverless em Python. 
*  simplifica a criação de APIs, serviços web e backends sem servidor usando serviços como AWS Lambda e API Gateway.

#### S3 Buckets:
* asemelham-se a pastas de arquivos, podem ser usados para guardar e acessar objectos.
* S3: Amazon's Simple Storage Service


#### INVOKE CLI:
* O termo "invoke" refere-se a executar uma função específica em um serviço AWS, como uma função Lambda.
* "receber um invoke do CLI" significa acionar uma função localmente usando o CLI da AWS.

### Passos:
* Usando o Chalice, escrever um aplicativo serverless em Python. 
* invocar esse aplicativo usando o CLI da AWS, e a saída da função será exibida no terminal.

"Geralmente, o processo envolve definir as rotas e lógica do aplicativo usando o Chalice, iniciar o LocalStack AWS para emular o ambiente AWS localmente, invocar o aplicativo usando o CLI da AWS e, em seguida, observar a saída no terminal."

---> definir as rotas e lógica do aplicativo: 
* mapear as URLs que os usuários podem acessar e determinar o que o aplicativo fará quando receber uma solicitação em cada URL.



##### Links:
* documentação do chalice: https://aws.github.io/chalice/main.html
* quickstart do chalice (bem simples): https://aws.github.io/chalice/quickstart.html
* deploy com terraform (caso interesse): https://aws.github.io/chalice/topics/tf.html?highlight=local
* LOCALSTACK com chalice: https://docs.localstack.cloud/user-guide/integrations/chalice/

