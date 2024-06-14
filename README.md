
# Projeto Octa City 

**Nome do Grupo**: The Back-Enders<br>
**Código da Disciplina**: FGA0208-T01<br>

# Documentação do Projeto

## <strong>Alunos</strong>
|Matrícula | Aluno |
| -- | -- |
| 202209150008  |  Brenda Mendes Araujo |
| 202208384986  |  Beatriz Vieira |
| 202208385486  |  Guilherme Almeida |
| 202302937314  |  Ian Esteves |
| 202307545333  |  João Gabriel Rodriguez |

## <strong>Sobre</strong>
Este projeto visa o desenvolvimento de um sistema de backend em parceria com prefeituras para detectar emergências, como alagamentos, por meio do uso de inteligência artificial e câmeras de segurança públicas. O foco principal é a criação da API no backend para cadastrar e acessar dados das câmeras. O projeto será finalizado até o fim do primeiro semestre de 2024, utilizando a biblioteca Django na linguagem de programação Python. Nosso objetivo é criar uma solução escalável, segura e de fácil utilização, fornecendo uma ferramenta robusta para auxiliar na tomada de decisões durante situações de crise.

## Sumário

- [5W2H](#5w2h)
- [Caso de Uso 1: Cadastro de Câmeras](#caso-de-uso-1:-cadastro-de-câmeras)
- [Caso de Uso 2: Monitoramento de Câmeras](#caso-de-uso-2:-monitoramento-de-câmeras)
- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Banco de Dados](#banco-de-dados)
- [Como Executar](#como-executar)
- [Funcionalidades](#funcionalidades)

# <strong>5W2H:</strong>

Perguntas | Definições
--------------------------------|------------------------------------------------------------
Quem? | Clientes da empresa e usuários internos da Octa City. 
O que? | Criação da API no back-end para cadastrar e acessar dados das câmeras.
Quando? | O projeto deverá ser finalizado até o fim do primeiro semestre de 2024.
Onde? | Utilizando a biblioteca Jango, na linguagem de programação Python.
Por que? | Cadastro e acesso de dados de câmeras para monitoramento de vias urbanas.
Quanto? | Tempo investido pela equipe de desenvolvimento e pela equipe Octa City.
Como? | Desenvolvido com a linguagem Python.

## <strong>Caso de Uso 1: Cadastro de Câmeras</strong>

Objetivo: Criar aplicação para cadastro das câmeras que monitoram as vias urbanas, registrando diversas informações como modelo, local de instalação, tecnologia, ângulo e etc, possibilitanto encontrá-las com facilidade posteriormente para monitoramento das vias urbanas.

## <strong>Caso de Uso 2: Monitoramento de Câmeras</strong>

Objetivo: Possibilitar o monitoramento e a gestão das câmeras que registram e coletam dados visuais.

## Visão Geral

Este projeto é uma aplicação Django para gerenciamento de câmeras e estacionamentos. Inclui funcionalidades administrativas para gerenciar usuários e permissões.

## Estrutura do Projeto

### `manage.py`

O arquivo `manage.py` é o script de gerenciamento do Django que permite executar diversas tarefas administrativas, como iniciar o servidor, aplicar migrações, criar usuários, etc.

```python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_cameras.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

## Estrutura de Diretórios

- **projeto_cameras/**: Contém as configurações do projeto Django.
- **nome_da_app/**: Contém os aplicativos do Django, incluindo modelos, visualizações e URLs.

## Banco de Dados

### Tabelas do Sistema Django

- **django_migrations**: Rastreamento de migrações aplicadas.
- **sqlite_sequence**: Sequências de autoincremento.
- **auth_group_permissions, auth_user_groups, auth_user_user_permissions**: Associações entre usuários, grupos e permissões.
- **django_admin_log**: Registros de ações administrativas.
- **django_content_type**: Tipos de conteúdo para permissões.
- **auth_permission**: Permissões específicas.
- **auth_group**: Grupos de usuários.
- **auth_user**: Informações dos usuários.
- **django_session**: Sessões de usuários.

### Tabelas do Aplicativo

- **nome_da_app_camerapark**: Dados dos estacionamentos.
- **nome_da_app_camera**: Dados das câmeras.
- **nome_da_app_company**: Dados das empresas.
- **app_camera_system_camerapark, app_camera_system_camera, app_camera_system_company**: Dados relacionados aos sistemas de câmeras.

## Como Executar

1. Certifique-se de ter o Python e o Django instalados.
2. Navegue até o diretório do projeto.
3. Execute o comando para aplicar migrações:

   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

5. Acesse a aplicação em http://127.0.0.1:8000.

## Funcionalidades

### Gerenciamento de Usuários e Permissões
- Criação, edição e exclusão de usuários
- Atribuição de diferentes níveis de permissão
- Controle de acesso baseado em funções

### Cadastro e Visualização
- Parques de cameras
  - Adicionar novos parques
  - Visualizar lista de parques cadastrados
  - Editar e remover informações de parques existentes
- Câmeras
  - Cadastrar novas câmeras
  - Visualizar e gerenciar câmeras associadas a estacionamentos
- Empresas
  - Registro de novas empresas
  - Exibição de empresas cadastradas
  - Modificação e exclusão de registros de empresas

### Sistema de Autenticação de Usuários
- Registro de novos usuários
- Login seguro com verificação de credenciais
- Recuperação de senha
- Sessões de usuário com tempo de expiração configurável

Repositório da disciplina de Projeto Back-End
