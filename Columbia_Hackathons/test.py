import requests
import openai
import json

openai.api_key = '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'


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

data = json.loads(response)

print(data['choices'])

print(response)