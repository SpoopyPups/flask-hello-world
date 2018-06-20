from flask import Flask #import Flask

app = Flask(__name__) #create global Flask app object (name of app module)

@app.route('/index') # route decorator attribute of app object (respond to requests for /index URL)
def index(): #define view funct, maps '/index' request to index funct response
    return 'Hello World!'

if __name__ == "__main__": #call app.run to start Flask app
    app.run()