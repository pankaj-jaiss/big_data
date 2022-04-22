
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.http import JsonResponse
# from .forms import EditUserProfileForm, SignUpForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .forms import Migration1Form
from .models import Migration1
import sqlalchemy as db
from django.views import View
import simplejson

# create_engine_string = ''

# ------------------>Please make all the urls in the inner project urls.py not in application level<----------------

# Create your views here.


def user_login(request):
    if not request.user.is_authenticated:  # is_authenticated which is always False ). This is a way to tell if the user has been authenticated. This does not imply any permissions and doesn't check if the user is active or has a valid session. Even though normally you will check this attribute on request.
        if request.method == 'POST':
            print(' post method is called...')
            print(f'request.POST : {request.POST}')
            auth_form_object = AuthenticationForm(
                request=request, data=request.POST)
            if auth_form_object.is_valid():
                print('form is validated...')
                user_name = auth_form_object.cleaned_data['username']
                user_pass = auth_form_object.cleaned_data['password']
                print('user_name : ', user_name)
                print('user_pass : ', user_pass)
                user = authenticate(username=user_name, password=user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(
                        request, 'You have successfully logined !!!')
                    return HttpResponseRedirect('/index/')
            else:
                print('form not validated...')
        else:
            auth_form_object = AuthenticationForm()
    else:
        auth_form_object = AuthenticationForm()
        print('please logout ...')
    return render(request, 'admininterface/login.html', {'auth_form_object': auth_form_object})


def index_page(request):
    return render(request, 'admininterface/index.html')

# class ResourceMigration(TemplateView):
#     template_name = 'admininterface/migration1.html'


def migration2_page(request):
    return render(request, 'admininterface/migration2.html')


class TestConnection(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admininterface/migration1.html')

    def post(self, request, *args, **kwargs):
        print('Test Button is clicked ...')
        form = Migration1Form(request.POST)
        context = {'popup_msg': 'Your connection is readdy...'} 
        # password = request.POST['passwd']
        # print(password,len(password))

        print(request.POST) 
        # print(len(request.POST['passwd']), request.POST['passwd']) 

        if form.is_valid():
            print('form validated ...', request.POST.get('clicked'))
            self.source = form.cleaned_data['source'].lower()
            user = form.cleaned_data['user']
            passwd = form.cleaned_data['passwd']
            host = form.cleaned_data['host']
            port = form.cleaned_data['port']
            service_name = form.cleaned_data['service_name'] 
            db_name = request.POST['destination']
            print(len(passwd),passwd)
            # global create_engine_string
            if self.source == 'mysql':
            #    create_engine_string = f'{self.source}://{user}:{passwd}@{host}:{port}'
            #    passwd = ''
               create_engine_string = f'mysql+pymysql://{user}:{passwd}@{host}:{port}'
               print('string block of mysql ...')

            elif self.source == 'oracle':
                create_engine_string = f'{self.source}://{user}:{passwd}@{host}:{port}/{db_name}'
            print(f'connection string : {create_engine_string}')
            engine = db.create_engine(create_engine_string)
            # engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
            try:
                con = engine.connect()
                if self.source not in  request.session:
                    request.session[self.source] = create_engine_string 
                    print('try block of mysql')
                if self.source == 'mysql':
                    outpt = con.execute("show databases")
                    outpt_list = list(outpt)
                elif self.source == 'oracle':
                    outpt = con.execute(
                        "select username as schema_name from sys.all_users order by username")
                global database_names
                database_names = []
                global database_names_list
                database_names_list = []
                database_names = outpt.fetchall()
                if self.source == 'mysql':
                    database_names = outpt_list
                context['popup_msg'] = 'Your connection is ready to go ...'
                return JsonResponse(context)
            except:
                print('Something goes wrong...')
                context['popup_msg'] = 'Provided credential is not correct'
                return JsonResponse(context)

        try:
            return render(request, 'admininterface/migration2.html',
                  {'database_names': database_names})
        except:
            context['popup_msg'] = 'Provided credential is not correct'
            return JsonResponse(context)

    # def create_engine_strings(self):
    #     # self.post(self, request)
    #     return create_engine_string

# class TestConnection(View):
#     create_engine_string = None 

#     def get(self, request, args, *kwargs):
#         return render(request, 'admininterface/migration1.html')

#     def post(self, request, args, *kwargs):
#         print('Test Button is clicked ...')
#         print(request.POST)
#         form = Migration1Form(request.POST)
#         context = {'popup_msg': 'Your connection is readdy...'}
#         create_engine_string = None 
#         if not request.POST.get('db_selected'):
#             try:
#                 source = request.POST['source'].lower()
#                 user = request.POST['user']
#                 passwd = request.POST['passwd']
#                 host = request.POST['host']
#                 port = request.POST['port']
#                 service_name = request.POST['service_name']
#                 db_name = request.POST['destination']
#             except:
#                 source = request.POST['db_source'].lower()
#                 user = request.POST['db_user']
#                 passwd = request.POST['db_passwd']
#                 host = request.POST['db_host']
#                 port = request.POST['db_port']
#                 service_name = request.POST['db_service_name']
#                 # db_name = request.POST['destination']
#         if form.is_valid():
#             # print('form validated ...', request.POST.get('clicked'))
#             # self.source = form.cleaned_data['source'].lower()
#             # self.user = form.cleaned_data['user']
#             # self.passwd = form.cleaned_data['passwd']
#             # self.host = form.cleaned_data['host']
#             # self.port = form.cleaned_data['port']
#             # self.service_name = form.cleaned_data['service_name']
#             # self.db_name = request.POST['destination']

#             # global create_engine_string
#             create_engine_string = f'{source}://{user}:{passwd}@{host}:{port}/{db_name}'
#             string = create_engine_string
#             print(f'connection string : {create_engine_string}')
#             engine = db.create_engine(create_engine_string)
#             # engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
#             try:
#                 con = engine.connect()
#                 outpt = con.execute(
#                     "select username as schema_name from sys.all_users order by username")
#                 global database_names
#                 database_names = []
#                 global database_names_list
#                 database_names_list = []
#                 database_names = outpt.fetchall()
#                 context['popup_msg'] = 'Your connection is ready to go ...'
#                 return JsonResponse(context)
#             except:
#                 print('Something goes wrong...')
#                 context['popup_msg'] = 'Provided credential is not correct'
#                 return JsonResponse(context)
#         if request.POST.get('db_selected'):
#             print('db selected : ',request.POST.get('db_selected'))
#             # create_engine_string = f'{source}://{user}:{passwd}@{host}:{port}/{db_name}'
#             engine = db.create_engine(self.create_engine_string)
#             con = engine.connect()
#             database_name = request.POST.get('db_selected')
#             output = con.execute("SELECT owner, table_name FROM all_tables")
#             data = output.fetchall()
#             tables = []
#             for tup in data:
#                 if tup[0] == database_name:
#                     tables.append(tup[1])

#             ctx = {
#                 'all_tables': tables  # 'all_tables': ['table1', 'table2', 'table3']

#             }
#             return HttpResponse(simplejson.dumps(ctx), content_type='application/json')

#         try:
#             return render(request, 'admininterface/migration2.html',
#                           {'database_names': database_names})
#         except:
#             context['popup_msg'] = 'Provided credential is not correct'
#             return JsonResponse(context)

#     def create_engine_strings(self):
#         # self.post(self, request)
#         return self.create_engine_string


def get_table_names(request):
    print('get_table_names function is called ...')
    if 'mysql' in request.session:
        credential_data = request.session.get('mysql','No data found in the session')
    elif 'oracle' in request.session:
        credential_data = request.session.get('oracle','No data found in the session')

    print(f'{credential_data} , {type(credential_data)}')
    for key, val in request.session.items():
        print(f'{key} : {val}')
    print('time : ',request.session.get_session_cookie_age())
    # obj = TestConnection()
    # obj.post(request)
    # print('obj.__dict_ : ',obj.__dict_)
    # engine = db.create_engine(obj.create_engine_strings())
    engine = db.create_engine(credential_data)

    con = engine.connect()
    database_name = request.POST.get('db_selected')
    print(database_name)
    tables = []

    if 'oracle' in credential_data:
         output = con.execute("SELECT owner, table_name FROM all_tables")
         data = output.fetchall()
         for tup in data:
            if tup[0] == database_name:
                tables.append(tup[1])
    elif 'mysql' in credential_data:
         con.execute(f'use {database_name}')
         data = con.execute('show tables')
         print('data : ',data) 
         for tup in list(data):
             tables.append(tup[0])


    

    ctx = {
        'all_tables': tables  # 'all_tables': ['table1', 'table2', 'table3']

    }
    return HttpResponse(simplejson.dumps(ctx), content_type='application/json')


# It doesn't return anything, it only takes the HttpRequest object.
def user_logout(request):
    logout(request)
    # request.session.flush()
    if 'oracle'  in  request.session:
        del request.session['oracle']

    elif 'mysql'  in  request.session:
        del request.session['mysql']
    return HttpResponseRedirect('/login/')