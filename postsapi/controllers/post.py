from tg import expose, redirect

from postsapi.lib.base import BaseController
from postsapi.model import DBSession, Post


class PostController(BaseController):
    @expose('postsapi.templates.posts_list')
    def index(self, **kw):
        posts = Post().get_all()
        return dict(page='post-index', posts=posts)

    @expose('postsapi.templates.posts_form')
    def new(self, **kw):
        return dict(page='post-new', post=None, button_label='new')

    @expose('postsapi.templates.posts_form')
    def edit(self, id):
        post = DBSession.query(Post).get(id)
        return dict(page='post-edit', post=post, button_label='edit')

    @expose()
    def save(self, **kw):
        if 'id' not in kw:
            post = Post(title=kw['title'],
                        body=kw['body'], author=kw['author'])
            DBSession.add(post)
        else:
            post = DBSession.query(Post).get(kw['id'])
            post.title = kw['title']
            post.body = kw['body']
            post.author = kw['author']
        redirect('/' + 'post')

    @expose()
    def delete(self, id):
        post = DBSession.query(Post).get(id)
        DBSession.delete(post)
        redirect('/' + 'post')
