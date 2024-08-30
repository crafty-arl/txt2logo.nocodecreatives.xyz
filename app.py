from flask import Flask, render_template, jsonify, request
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_logo', methods=['POST'])
def generate_logo():
    data = request.json
    prompt = data.get('prompt')
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
