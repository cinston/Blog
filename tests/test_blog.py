from app.models import Comment,User, Blog
from app import db
import unittest

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_blog = Blog(id=1,title='Test',description='This is a test blog',category="interview",user = self.user_James,upvotes=0,downvotes=0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'Test')
        self.assertEquals(self.new_blog.description,'This is a test blog')
        self.assertEquals(self.new_blog.category,"interview")
        self.assertEquals(self.new_blog.user,self.user_James)

    def test_save_blog(self):
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        got_blog = Blog.get_blog(1)
        self.assertTrue(got_blog is not None)