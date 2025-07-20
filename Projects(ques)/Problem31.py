# Program to find out wheather a given post is talking about "Harry" or not

post = input("Post:")

to_find = post.find("Harry")

if to_find != -1:
    print("Yes, this post talks about \"Harry\"")

else:
    print("No, this post does'nt talks about \"Harry\"")

# OR according to Chatgpt

if "Harry" in post:  # More Pythonic way to check presence
    print('Yes, this post talks about "Harry"')
else:
    print('No, this post doesn\'t talk about "Harry"')


