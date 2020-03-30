from flask import Flask
# import boto3

app = Flask('hello-cloudbuild')
# dynamo_client = boto3.client('dynamodb')

@app.route('/')
def hello():
  return "Hello World!\n"

# @app.route('/load-data')
# def load_data():


  
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)