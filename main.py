from flask import Flask, request, render_template, redirect
import openai

openai.api_key = 'your API'

server = Flask(__name__)

def send_gpt(prompt,tem):
    try:
        response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=tem,
        max_tokens=3500,  #prompt and answer together have 4096 tokens
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0)

        return response["choices"][0]["text"]
    except:
        mess = "Connection Error! Please try again."
        return mess

@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat.html', question="NULL", res="Question can't be empty!")
        question = request.form['question']
        temperature = float(request.form['temperature'])
        print("======================================")
        print("Receive the question:", question)
        print("Receive the temperature:",temperature)
        res = send_gpt(question,temperature)
        print("Q：\n", question)
        print("A：\n", res)

        return render_template('chat.html', question=question, res=str(res), temperature=temperature)
    return render_template('chat.html', question=0)

if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=80)