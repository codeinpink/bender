from bottle import route, run, template, SimpleTemplate, get, post, request, static_file, response, redirect, hook
import os

current_dir = os.getcwd()
repo_dir = os.path.join(current_dir, "plugins")

@route('/')
def index():
    return template("home")

@get('/create')
def get_create_page():
    return template("create")

@get('/browse')
def get_browse_page():
    return template("browse", filename = getFileInfo())

@post('/saveFile')
def releasePendingPackage():
    saveFileToRepo(request.json)

def saveFileToRepo(request):

    os.chdir(repo_dir)

    with open(request['filename'], "w") as f:
        f.write(request['code'])

    os.chdir(current_dir)

@get('/getFileInfo')
def getFileInfo():
    files = os.listdir(repo_dir)
    os.chdir(repo_dir)
    tmp = []
    for file in files:
        if os.path.isfile(file) and file.endswith('.py') and file != '__init__.py':
            with open (file, "r") as currentfile:
                data=currentfile.readlines()
                tmp.append({"filename": file, "code": data})

    os.chdir(current_dir)
    sort_tmp = sorted(tmp, key = lambda k: k['filename'])
    return sort_tmp

if __name__ == "__main__":
    run(reloader=True, debug=True)
