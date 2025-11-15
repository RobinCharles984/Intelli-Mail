<br/>
<p align="center">
  <a href="https://github.com/RobinCharles984/Intelli-Mail">
    <img src="static/logo.png" alt="Logo" width="400" height="100">
  </a>

  <h3 align="center">Intelli-Mail</h3>

  <p align="center">
    Um classificador de e-mails com IA para automatizar respostas.
    <br/>
    <br/>
    <a href="https://intelli-mail.onrender.com"><strong>Ver Demo Ao Vivo »</strong></a>
    ·
    <a href="https://github.com/RobinCharles984/Intelli-Mail/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/RobinCharles984/Intelli-Mail/issues">Sugerir Funcionalidade</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-black?logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/OpenAI-GPT-brightgreen?logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Deploy-Render-cyan?logo=render" alt="Render">
  <img src="https://img.shields.io/github/issues/RobinCharles984/Intelli-Mail" alt="Issues">
</p>


## Sumário

* [Sobre o Projeto](#sobre-o-projeto)
* [Funcionalidades](#funcionalidades)
* [Arquitetura](#arquitetura)
* [Construído Com](#construído-com)
* [Começando](#começando)
  * [Pré-requisitos](#pré-requisitos)
  * [Instalação](#instalação)
* [Uso](#uso)
* [Roadmap](#roadmap)
* [Contribuição](#contribuição)
* [Autor](#autor)

## Sobre o Projeto

![Intelli-Mail Screenshot]([COLE_O_LINK_DA_SUA_SCREENSHOT_AQUI])

**Intelli-Mail** é uma solução web desenvolvida para o Desafio AutoU. O objetivo é automatizar a triagem de e-mails para uma empresa do setor financeiro, liberando tempo da equipe de atendimento.

A aplicação utiliza Inteligência Artificial para:
1.  **Classificar** e-mails entre **Produtivo** (requer ação) ou **Improdutivo** (não requer ação).
2.  **Sugerir** uma resposta automática apropriada com base na classificação.

O sistema aceita entrada de texto, arquivos `.txt` e até `.pdf`, e armazena um histórico local (cache) para referência do usuário.

## Funcionalidades

* **Classificação com IA:** Usa a API da OpenAI para analisar o sentimento e o contexto do e-mail.
* **Geração de Resposta:** Cria uma sugestão de resposta profissional e adequada.
* **Múltiplos Formatos de Entrada:** Aceita texto colado, upload de `.txt` e `.pdf`.
* **Histórico (Cache):** Armazena análises anteriores no `LocalStorage` do navegador para fácil acesso.
* **Modo Escuro:** Interface com tema claro e escuro para melhor usabilidade.
* **Cópia Rápida:** Botão para copiar a resposta sugerida com um clique.

## Arquitetura

Aqui está uma visão do planejamento e da arquitetura de fluxo da aplicação, diretamente do quadro branco.

### 1. Planejamento do Projeto

![Planejamento no Quadro](/static/arquitetura.jpeg)

### 2. Fluxo da Arquitetura

![Fluxo da Arquitetura no Quadro](/static/pipeline.jpeg)

## Construído Com

Estas foram as principais tecnologias usadas para construir o projeto:

* **Backend:**
    * [Python](https://www.python.org/)
    * [Flask](https://flask.palletsprojects.com/) (Servidor Web)
    * [Gunicorn](https://gunicorn.org/) (Servidor de Produção)
* **Inteligência Artificial:**
    * [OpenAI API (GPT-3.5/4)](https://platform.openai.com/)
* **Processamento de Arquivos:**
    * [pypdf](https://pypi.org/project/pypdf/) (Extração de texto de PDF)
* **Frontend:**
    * HTML5
    * CSS3 (com CSS Grid)
    * JavaScript (Vanilla)
* **Deploy:**
    * [Render](https://render.com/)

## Começando

Para rodar uma cópia local do projeto, siga estes passos.

### Pré-requisitos

Você precisará ter o Python 3.10+ instalado e uma chave de API da OpenAI.

* **Python**
    * [Instale a última versão do Python](https://www.python.org/downloads/)
* **Chave da OpenAI**
    * [Obtenha sua chave de API no painel da OpenAI](https://platform.openai.com/account/api-keys)

### Instalação

1.  Clone o repositório
    ```sh
    git clone [https://github.com/RobinCharles984/Intelli-Mail.git](https://github.com/RobinCharles984/Intelli-Mail.git)
    cd Intelli-Mail
    ```

2.  Crie e ative um ambiente virtual
    ```sh
    python -m venv .venv
    # No Windows
    .venv\Scripts\activate
    # No MacOS/Linux
    source .venv/bin/activate
    ```

3.  Instale os pacotes Python
    ```sh
    pip install -r requirements.txt
    ```

4.  Crie seu arquivo de segredos
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua chave da OpenAI dentro dele:
        ```
        OPENAI_API_KEY='sk-SuaChaveSecretaDaOpenAIAqui'
        ```

5.  Rode a aplicação localmente
    ```sh
    flask run
    ```
    Abra `http://127.0.0.1:5000` no seu navegador.

## Uso

A aplicação é intuitiva:

1.  Acesse o link da aplicação (local ou no Render).
2.  Cole o texto de um e-mail na área designada OU faça upload de um arquivo `.txt` ou `.pdf`.
3.  Clique em "Classificar E-mail".
4.  Veja o resultado (Categoria e Sugestão) aparecer no painel principal.
5.  A análise será salva automaticamente no painel de "Histórico" à direita.
6.  Clique no botão "Trocar Tema" para ativar o Modo Escuro.

Para uma demonstração completa, veja o vídeo do desafio:

**[Assista ao Vídeo Demonstrativo]()**

## Roadmap

Veja as [issues abertas](https://github.com/RobinCharles984/Intelli-Mail/issues) para uma lista de funcionalidades propostas (e bugs conhecidos).

## Contribuição

Contribuições são o que tornam a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1.  Faça um Fork do Projeto
2.  Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Faça commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4.  Faça push para a Branch (`git push origin feature/AmazingFeature`)
5.  Abra um Pull Request

## Autor

* **Tales Machado** - *Estudante de Engenharia de Software* - [RobinCharles984](https://github.com/RobinCharles984/)

## Agradecimentos

* [AutoU](https://autou-digital.notion.site/) (Pelo desafio)
* [ImgShields](https://shields.io/) (Pelos badges)
* [Othneil Drew](https://github.com/othneildrew/Best-README-Template) (Pela inspiração de template)