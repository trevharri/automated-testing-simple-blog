from blog.tests.post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        # rep = self.title +' by '+ self.author + ' (' + str(len(self.posts)) + ' posts)'
        rep = f'{self.title} by {self.author} ({len(self.posts)} posts)'
        return rep

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        json = {"title": self.title, "author": self.author, "content": self.posts}
