from unittest import TestCase
from blog.tests.post import Post
from blog.tests.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')

        self.assertEqual('Test by Test Author (0 posts)', b.__repr__())
        self.assertEqual('My Day by Rolf (0 posts)', b2.__repr__())

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test', 'test']
        b2 = Blog('My Day', 'Rolf')
        b2.posts = ['test']

        self.assertEqual('Test by Test Author (2 posts)', b.__repr__())
        self.assertEqual('My Day by Rolf (1 posts)', b2.__repr__())

    def test_create_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

