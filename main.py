import flask
import json
import time, random, hashlib

import atexit

app = flask.Flask(__name__)

g = open('./config.json')
config = json.loads(g.read())
g.close()

f = open('./sessions.json', 'r+')
sessions = json.loads(f.read())
f.close()

try:
    config["password"]
except:
    print('It dosen\'t look like you set a password for user \'admin\'.')
    while True:
        password = input('Set a password > ')
        if (len(password) < 4):
            print('Password length must be more than 3')
        else:
            break
    print('Set password')
    config["password"] = password
    
    h = open('./config.json', 'w')
    h.write(json.dumps(config))
    h.close()

def checkId(id):
    global sessions
    
    sessionsWithId = list(filter(lambda x: x['id'] == id, sessions))
    return len(sessionsWithId) > 0


def cleanUpIds():
    global sessions
    for i in sessions:
        now = int(time.time())
        try:
            i["created"]
        except:
            continue
        
        c = int(i["created"])
        d = now - c
        
        if (d > (30*60)):
            print(f"Killing session: ID: [{i['id']}]")
            print(sessions)
            sessions = list(filter(lambda x: x['id'] != i['id'], sessions))
            print(sessions)

cleanUpIds()

def close_running_threads():
    print('Stopping')
    f = open('./sessions.json', 'w')
    f.write(json.dumps(sessions))
    f.close()

atexit.register(close_running_threads)

def getFile(a):
    f = open(a, 'r')
    d = f.read()
    f.close()
    return d

@app.route('/animation.js')
def animation_js():
    return getFile('./animation.js')

@app.route('/style.css')
def style_css():
    return getFile('./style.css')

@app.route('/index.css')
def index_css():
    return getFile('./index.css')

@app.route('/login')
def login():
    cleanUpIds()
    if (checkId(flask.request.cookies.get("session"))):
        print('User logged in. Forwarding to main.')
        return flask.redirect('./')
    return getFile('./login.html')

@app.route('/')
def main():
    if (not checkId(flask.request.cookies.get("session"))):
        print('User not logged in. Forwarding to login.')
        return flask.redirect('./login')
    return getFile('./index.html')


@app.route('/request-session/<username>/<password>', methods=["POST"])
def requestSession(username, password):
    cleanUpIds()
    username = str(username)
    password = str(password)
    
    # Generate session id
    sessionId = str(hashlib.md5(str(random.randint(100000000000,999999999999)).encode()).hexdigest())
        
    if ((username == "admin") and (password == config["password"])):
        sessions.append({"created": int(time.time()), "id": sessionId})
        return '{"status": 1, "id": "'+sessionId+'"}'
    else:
        return "{\"status\": 3, \"error\":\"invalid\", \"message\": \"INVALID! TRY AGAIN! HAW HAW!!!!!! NICE TRY! YOU THOUGHT YOU COULD HACK ME???!!! THAT'S RIGHT! IT FAILED!!!!!!!!! LOSER!!!\"}"

      
app.run("0.0.0.0", "8000")
