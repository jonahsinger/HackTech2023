from flask import Flask, request, jsonify, render_template, request, redirect, url_for
import openai
import os



# Initialize the Flask application
app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = 'XXX'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reuse")
def reuse():
    return render_template("reuse.html")

@app.route("/recycle")
def recycle():
    return render_template("recycle.html")
@app.route("/reduce")
def reduce():
    return render_template("reduce.html")
@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/impact")
def impact():

    return render_template("impact.html")

@app.route('/get_response', methods=['POST'])
def get_response():
    request_data = request.get_json()
    items = request_data['items']
    
    # Generate a prompt based on the list of items
    if items[0] == '0':
        prompt = "What are some sustainable things you can make using these objects:" +  ', '.join(items[1:]) + " and write in full sentences in a paragraph form. Please do not mention that you are an AI."
    elif items[0] == '1':
        print(items[1])
        prompt = "How can I reduce waste in " +  items[1] + "? Please write in full sentences in a paragraph form. Please do not mention that you are an AI."
    elif items[0] == '2':
        prompt = "How can I best recycle " +  items[1] + "? Please answer in full sentences in a paragraph form. Please do not mention that you are an AI."
    elif items[0] == '3':
        prompt = "How will climate change affect me in " +  items[1] + "? Please answer in full sentences in a paragraph form. Please do not mention that you are an AI."
        pass
    print(prompt)
    # Generate a ChatGPT response
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ]
    )


    # Return a JSON object with the response
    return jsonify({'response': response})


# Define the main function to run the Flask application
if __name__ == '__main__':
    app.run(host='10.206.21.154', port=5000, debug=True, threaded=True)