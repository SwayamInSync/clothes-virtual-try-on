from flask import Flask, request, jsonify, render_template
from PIL import Image
import requests
from io import BytesIO
import base64

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/preds", methods=['POST'])
def submit():
    cloth = request.files['cloth']
    model = request.files['model']

    ## replace the url from the ngrok url provided on the notebook on server.
    url = "http://e793-34-123-73-186.ngrok-free.app/api/transform"
    print("sending")
    response = requests.post(url=url, files={"cloth":cloth.stream, "model":model.stream})
    op = Image.open(BytesIO(response.content))

    buffer = BytesIO()
    op.save(buffer, 'png')
    buffer.seek(0)

    data = buffer.read()
    data = base64.b64encode(data).decode()


    return render_template('index.html', op=data)
    # return render_template('index.html', test=True)

if __name__ == '__main__':
    app.run(debug=True)
