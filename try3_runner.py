from post_class import Post
import data_functions

# load the existing posts
posts = data_functions.get_data("u14classes2/data.txt")


# TODO
# print the variable 'posts' (you'll fix this later)
# print the length of the posts list
# print each item in the list, one at a time (you'll fix this later)



# TODO
# create a new post sending the two required parameters, append it to the list
# run the program and check the 'data' file






# save all posts persistently
data_functions.save_data(posts)