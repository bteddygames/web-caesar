from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method='POST'>
            <div>
                <label>Rotate by:
                    <input type="text" name="rot" value=0 />
                </label>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    blank=''
    return form.format(blank)

@app.route("/", methods=['POST'])
def encrypt():
    erot= int(request.form['rot'])
    etext= str(request.form['text'])
    message= (rotate_string(etext, erot))
    return form.format(message)

app.run()