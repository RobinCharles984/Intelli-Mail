import os
import io
import json
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader

# Carrega as variáveis de ambiente com a API Key da OpenAI
load_dotenv()

# Inicializa o Flask
app = Flask(__name__)

# Inicializa o cliente da OpenAI
# O cliente vai automaticamente procurar a chave "OPENAI_API_KEY" no ambiente
try:
    client = OpenAI()
except Exception as e:
    print(f"Erro ao inicializar cliente OpenAI: {e}")


#Cérebro do Classificador
def analisar_email_com_gpt(texto_email):
    """
    Envia o texto do email para o GPT e pede classificação e resposta.
    """
    # Abaixo está o prompt que será enviado para o GPT, ele analisará e retornará um JSON para ser analisado em outros métodos abaixo
    prompt_do_sistema = """
    Você é um assistente de IA para uma empresa financeira. Sua tarefa é analisar emails.
    Você deve fazer duas coisas:
    1. Classificar o email como "Produtivo" ou "Improdutivo".
    2. Gerar uma sugestão de resposta curta e profissional baseada na classificação.

    - "Produtivo": Emails que requerem uma ação (solicitações, dúvidas, atualizações de caso).
    - "Improdutivo": Emails que não requerem ação (spam, felicitações, agradecimentos simples).

    REGRAS IMPORTANTES:
    - Retorne SUA RESPOSTA APENAS em formato JSON.
    - O JSON deve ter duas chaves: "categoria" e "sugestao_resposta".

    Exemplo de saída para um email produtivo:
    {
      "categoria": "Produtivo",
      "sugestao_resposta": "Obrigado por sua solicitação. Estamos analisando seu caso e retornaremos em breve."
    }

    Exemplo de saída para um email improdutivo:
    {
      "categoria": "Improdutivo",
      "sugestao_resposta": "Nenhuma ação necessária."
    }
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Como é apenas para um processo seletivo, foi escolhido o 4o mini pois consome menos tokens
            messages=[
                {"role": "system", "content": prompt_do_sistema},
                {"role": "user", "content": texto_email} # Conteúdo do email
            ],
            response_format={"type": "json_object"}, # Força a resposta a ser um JSON
            temperature=0.7, # Um pouco de criatividade, mas não  (0 à 1)
        )
        
        # Extrai o conteúdo JSON (string) e converte para um dict
        resultado_json_string = response.choices[0].message.content
        return json.loads(resultado_json_string) # Retorna um dictionary

    except Exception as e:
        print(f"Erro na chamada da API da OpenAI: {e}")
        # Retorna um JSON de erro padronizado
        return {
            "categoria": "Erro",
            "sugestao_resposta": f"Houve um erro ao processar o email (veja o log do servidor): {e}"
        }


# Routes (Referente ao controle de backend do Flask)
@app.route('/')
def index():
    """
    Esta rota vai servir o seu arquivo HTML principal.
    Vamos criar esse HTML no próximo passo.
    """

    return render_template('index.html') #Página primária padrão


@app.route('/classificar', methods=['POST'])
def classificar_email():
    texto_email = ""

    # VERIFICA SE VEIO UM ARQUIVO (multipart/form-data)
    if 'email_file' in request.files:
        file = request.files['email_file']

        # Se o usuário não selecionar arquivo, o navegador envia uma parte vazia sem nome de arquivo.
        if file.filename == '':
            return jsonify({"error": "Nenhum arquivo selecionado"}), 400

        #Verificando se o arquivo entrado é um .txt ou .pdf
        if file and (file.filename.endswith('.txt') or file.filename.endswith('.pdf')):
            try:
                if file.filename.endswith('.pdf'):
                    pdf_reader = PdfReader(io.BytesIO(file.read()))
                    for page in pdf_reader.pages:
                        texto_email += page.extract_text()

                elif file.filename.endswith('.txt'):
                    # .read() retorna bytes, decodificano para string
                    texto_email = file.read().decode('utf-8')

            except Exception as e:
                return jsonify({"error": f"Erro ao ler arquivo: {e}"}), 500 
        else:
            return jsonify({"error": "Formato de arquivo inválido. Use .txt ou .pdf"}), 400

    elif request.json and 'email_text' in request.json:
        texto_email = request.json['email_text']

    else:
        return jsonify({"error": "Nenhum texto ou arquivo fornecido"}), 400

    # Check para ver se o arquivo está vazio (assim tendo a segurança de não gastar prompts e tokens)
    if not texto_email.strip():
        return jsonify({"error": "O arquivo parece estar vazio ou não contém texto"}), 400

    resultado_dict = analisar_email_com_gpt(texto_email)

    resultado_dict['texto_original'] = texto_email 

    return jsonify(resultado_dict)

#--Main padrão
if __name__ == '__main__':
    app.run(debug=True)