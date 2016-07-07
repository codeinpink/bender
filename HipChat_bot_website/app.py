from bottle import route, run, template, SimpleTemplate, get, post, request, static_file, response, redirect, hook
import os

@route('/')
def index():
    return template("home")

@get('/create')
def get_create_page():
    return template("create")

@get('/browse')
def get_browse_page():
    return template("browse")

@post('/saveFile')
def releasePendingPackage():
    saveFileToRepo(request.json)

def saveFileToRepo(request):

    current_dir = os.getcwd()
    repo_dir = os.path.join(os.getcwd(), "repo")
    os.chdir(repo_dir)
    
    with open(request['filename'], "w") as f:
        f.write(request['code'])
        
    os.chdir(current_dir)
    
if __name__ == "__main__":
    run()