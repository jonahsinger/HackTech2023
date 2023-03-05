from flask import Flask, request, jsonify, render_template, request, redirect, url_for
import openai
import os



# Initialize the Flask application
app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = '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'

def generate_text(prompt, model, max_tokens=2048):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Create a ChatGPT instance
chat_gpt = generate_text
model = 'gpt-3.5-turbo'
chat_gpt = lambda context: generate_text(context, model=model)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reuse")
def reuse():
    return render_template("reuse.html")

@app.route("/redo")
def redo():
    return render_template("redo.html")
@app.route("/test")
def test():
    return render_template("test.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    request_data = request.get_json()
    items = request_data['items']

    # Generate a prompt based on the list of items
    prompt = f"What are some sustainable things you can make using these objects: {', '.join(items)}\n\n" +"and write in full sentences in a paragraph form with an academic style."

    # Generate a ChatGPT response
    response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=1024,
    temperature=0.4,
)

    # Return a JSON object with the response
    return jsonify({'response': response})


# Define the main function to run the Flask application
if __name__ == '__main__':
    app.run(host='10.206.21.154', port=5000, debug=True, threaded=True)