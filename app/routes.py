from app import myapp_obj

@myapp_obj.route("/")
def hello():
    return "hello"

@myapp_obj.route("/admin")
def admin():
    return "Administration Page!"

