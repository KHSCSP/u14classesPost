from post_class import Post

# this function reads data from a text file and returns a list of Posts
def get_data(filename):
    posts = []
    f = open(filename, "r")
    for line in f:
        if line != "\n":
            temp = line.strip() # strip the newlines
            temp = temp.split(",") # convert to list
            posts.append(Post(temp[0], temp[1], temp[2])) # create Post, append to list
    f.close()
    return posts
 
 
# this function receives a list of Posts and writes the data to a file 
def save_data(posts):
    f = open("data.txt", "w")
    for p in posts:
        f.write(p.username + "," + p.message + "," + str(p.timestamp) + "\n")
    f.close()