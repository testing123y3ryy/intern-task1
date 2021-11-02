from django import template
from app.models import Category, Patient, Post
register = template.Library()

@register.filter(name='author_name')
def author_name(id):
    created_by = Patient.objects.filter(id=id).first()
    return created_by.first_name

@register.filter(name='author_img')
def author_img(id):
    created_by = Patient.objects.filter(id=id).first()
    return created_by.image.url

@register.filter(name='no_of_posts')
def no_of_posts(id):
    cat = Category.objects.filter(id=id).first()
    no_posts = Post.objects.filter(category=cat)
    return len(no_posts)

@register.filter(name='is_doc')
def is_doc(id):
    pat = Patient.objects.filter(id=id).first()
    if pat.DorP == '2':
        return True
    return False

@register.filter(name='is_doc')
def is_doc(login_user_id,postid):
    post = Post.objects.filter(id=postid).first()
    if int(login_user_id) == int(post.author):
        return True
    return False

@register.filter(name='is_doctor')
def is_doctor(login_user_id):
    doc = Patient.objects.filter(id=login_user_id).first()
    if doc.DorP=='2':
        return True
    return False
    