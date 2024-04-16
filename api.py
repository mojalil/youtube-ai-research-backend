from flask import Flask

app = Flask(__name__)

# Healcheck route
@app.route('/healthcheck')
def healthcheck():
    return 'OK'

#  Run the server 
if __name__ == '__main__':
    app.run(debug=True, port=3001)