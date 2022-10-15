from app import myapp_obj

@myapp_obj.route("/")

def hello():
    return "hello"

def admin():
    return "This is my admin route!"
