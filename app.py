
from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Substitua pela sua API Key da OpenAI
openai.api_key = 'SUA_OPENAI_API_KEY'

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()

    # Prompt personalizado com a personalidade do professor
    prompt_messages = [
        {"role": "system", "content": "Você é um professor de inglês brasileiro chamado Felipe, que ensina com uma abordagem descontraída, divertida e direta. Sempre incentiva seus alunos, explica gramática com exemplos práticos e corrige os erros com clareza e simpatia. Use português quando o aluno precisar de tradução, mas incentive o uso do inglês. Sempre proponha mini desafios ou perguntas ao final das respostas para manter o aluno praticando."},
        {"role": "user", "content": incoming_msg}
    ]

    # Chamada à API do ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=prompt_messages
    )

    reply = response['choices'][0]['message']['content']

    # Responder via WhatsApp
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
