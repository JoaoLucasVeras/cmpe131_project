from app import myapp_obj

@myapp_obj.route("/")

def hello():
    return "hello"


