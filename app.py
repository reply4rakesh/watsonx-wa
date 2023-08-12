from flask import Flask,jsonify ,request
import question
import question

app = Flask(__name__)
  
@app.route('/', methods = ['GET'])
def landing():
    if(request.method == 'GET'):
        data = "Welcome to Gartner's IBM Report!"
        return jsonify({'data': data})

@app.route('/home', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = "Ask any question about Gartner's IBM Report!"
        return jsonify({'data': data})
  
@app.route('/getAnswer', methods = ['GET'])
def getAnswer():
    args = request.args
    query = args.get("query") 
    response = question.getAnswer(query)
    return jsonify({'data': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
