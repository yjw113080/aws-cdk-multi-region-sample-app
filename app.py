from flask import Flask
from ec2_metadata import ec2_metadata

app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  region = ec2_metadata.region
  return ("Hello World from"+region)

  
if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)