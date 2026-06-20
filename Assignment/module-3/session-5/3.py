'''Write a Python class called InstagramPost with attributes caption, 
likes, and comments (a list). Add a method add_comment(comment_text) 
that appends a new comment to the comments list and increases the likes by 
1.'''

class instagrampost:
    def __init__(self,caption,likes,comments):
        self.caption=caption
        self.likes=likes
        self.comments=comments

    def add_comment(self,comment_text):
        self.comments.append(comment_text)
        self.likes+=1
        
        print("likes :",self.likes)
        print("comments :",self.comments)
        

       
c=input("enter caption :")
l=int(input("enter likes :"))
cm=input("enter the comment :").split(",")
post=instagrampost(c,l,cm)

new_comment=input("enter the new comment :")
post.add_comment(new_comment)
    