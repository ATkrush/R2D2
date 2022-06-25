from flask import Flask

app = Flask(name)

def read_temp_file():
    datei= open('temperaturen.txt','r')
    temp=datei.read()
    str2=repr(temp)
    datei.close()
    return(temp)

@app.route('/')
def index():
    return read_temp_file()

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if name == 'main':
    app.run(debug=True, host='0.0.0.0')
