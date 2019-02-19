from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_blog = Blog(id=1,title='Test',description='This is a test blog',category="interview",user = self.user_James,upvotes=0,downvotes=0)
        self.new_comment = Comment(id=1, content='Test comment',user=self.user_James,blog=self.new_blog)


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.content,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_James)
        self.assertEquals(self.new_comment.blog,self.new_blog)