from pyramid.view import view_config
from .models import User, DBSession


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'myApp'}

@view_config(route_name='adduser', renderer='templates/addusers.pt')
def  add_users(request):
    list =[]
    if request.POST:
        formdict = dict(request.POST)
        DBSession.add(User(formdict['name'], formdict['fullname'], formdict['address']))
    for item in User.by_name():
        dicti = {'name':item.name, 'fullname':item.fullname, 'address':item.address }
        list.append(dicti)
    return {'users':list}

@view_config(route_name='user', renderer='templates/mytemplate.pt')
def user(request):
    value = User.by_name()
    return {'name':value.name, 'address': value.address, 'fullname': value.fullname}
