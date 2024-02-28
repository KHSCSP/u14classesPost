from datetime import datetime

# defining the class properites inside
class Post:

    # initalizing the class variable
    post_id = 0

    # what *must* we send to this function? what is optional?
    def __init__(self, param_user, param_mess, param_time=datetime.now()):
        self.username = param_user
        self.message = param_mess
        self.timestamp = param_time
        self.id_num = Post.post_id
        Post.post_id += 1

    # What is this method returning?
    def __str__(self):
        return "Surprise! This is a TODO later :)"

