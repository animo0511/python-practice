# A spam commment is defined as a text containing following keywords
# "Make a lot of money", "buy now", "subscribe now", "click this"
# Write a program to detect those spams

comments = input("Comment:")

if (comments == "Make a lot of money") or (comments == "buy now") or comments =="subscribe now" or comments == "click this":
    print("It's a spam")


# OR it can become more correct

if "Make a lot of money" in comments or "buy now" in comments or "subscribe now" in comments or "click this" in comments:
    print("It's a spam")
