from django.apps import apps

def category_import():
    from category.models import Category
    return Category

def idea_import():
    from idea.models import Idea
    return Idea

def comment_import():
    from comment.models import Comment
    return Comment

def user_import():
    from user.models import User
    return User
