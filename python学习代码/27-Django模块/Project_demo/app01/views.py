from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # 获取用户密码
    user = request.POST.get("username")
    pwd = request.POST.get("password")

    # 去数据库校验是否存在
    # 数据库中获得到的数据为NONE 或者是一个对象
    admin_object = models.Admin.objects.filter(username=user, password=pwd).first()
    if admin_object:
        print(admin_object.id, admin_object.username, admin_object.password)
        # http://127.0.0.1:8000/depart/list/

        # 生成随机字符串+返回用户浏览器+将数据写入SESSION
        request.session['userinfo'] = {'id': admin_object.id, 'username': admin_object.username}
        return redirect('/depart/list/')
    else:
        return render(request, 'login.html', {'error': "用户名或密码错误"})


def depart_list(request):
    # 校验用户是否已登陆

    # 获取用户的id和username
    print(request.unicom_userid)
    print(request.unicom_username)

    #  1.获取数据库中获取部门表格信息 QuerySet对象 = [obj,obj]
    dep_in = models.DepartMent.objects.all().order_by()
    # 2. 展示部门页面
    return render(request, 'departlist.html', {"department_info": dep_in})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'departadd.html')
    title = request.POST.get("title")
    models.DepartMent.objects.create(title=title)
    return redirect('/depart/list/')


def depart_delete(request):
    id = request.GET.get("id")
    models.DepartMent.objects.filter(id=id).delete()
    return redirect('/depart/list/')


def depart_edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        data = models.DepartMent.objects.filter(id=id).first()
        return render(request, 'departedit.html', {"data": data})
    else:
        id = request.GET.get('id')
        title = request.POST.get('title')
        models.DepartMent.objects.filter(id=id).update(title=title)
        return redirect('/depart/list/')


def asset_list(request):
    #  1.获取数据库中获取资产表格信息 QuerySet对象 = [obj,obj]
    asset_info = models.AssetSet.objects.all()
    print(asset_info)
    return render(request, 'assetlist.html', {"assetinfo": asset_info})


from django import forms


class AssetModelForm(forms.ModelForm):
    class Meta:
        model = models.AssetSet  # 指定该表单对应的模型类是 AssetSet
        # fileds = ['name','price','category','depart'] #展示想要显示的字段
        fields = '__all__'  # 指定表单应包含模型中的所有字段

        # 加入css样式，使其更美观
        # widgets = {
        #     'name':forms.Select(attrs={'class':"form-control"}),
        #     'price':forms.Select(attrs={'class':"form-control"}),
        #     'category':forms.Select(attrs={'class':"form-control"}),
        #     'depart':forms.Select(attrs={'class':"form-control"}),
        # }

    # 上面这种方法太麻烦，还需要一个个写，下面是其简便方法
    def __init__(self, *args, **kwargs):  # 定义 __init__ 初始化方法，重载 ModelForm 的构造函数。
        super().__init__(*args, **kwargs)  # 调用父类的 __init__ 方法，初始化表单
        for name, field in self.fields.items():  # 遍历表单中的每个字段
            field.widget.attrs['class'] = "form-control"  # 为每个字段的widget添加 class="form-control" 属性，使其应用Bootstrap的样式。


def asset_add(request):
    if request.method == 'GET':
        form = AssetModelForm()
        return render(request, 'assetadd.html', {"form": form})


    else:
        # 有POST请求提交过来的所有数据，需要对这些数据进行校验
        print(request.POST)  #
        # 使用modelForm进行数据的校验
        # 隐含的功能：输入字段不能为空、chioce和外键必须存在

        form = AssetModelForm(data=request.POST)
        if form.is_valid():  # 校验通过
            print(form.cleaned_data)  # form.cleaned_data
            # {'name': '棋鬼王', 'price': 2, 'category': 1, 'depart': < DepartMent: 1 - 经销部 >}

            # 校验成功以后在数据库中创建一条数据
            form.save()
            return redirect('/asset/list/')
        else:
            print(form.errors.as_data())
            return render(request, 'assetadd.html', {'form': form})


def asset_edit(request):
    if request.method == 'GET':
        aid = request.GET.get('aid')
        obj = models.AssetSet.objects.filter(id=aid).first()
        form = AssetModelForm(instance=obj)
        return render(request, 'assetedit.html', {'form': form})
    else:
        # 表单验证
        aid = request.GET.get('aid')
        obj = models.AssetSet.objects.filter(id=aid).first()
        form = AssetModelForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/asset/list/')
        else:
            return render(request, 'assetedit.html', {'form': form})


def asset_delete(request,did):
    models.AssetSet.objects.filter(id=did).delete()
    return redirect('/asset/list/')


def logout(request):
    # 两种方法注销 1.浏览器中的cookie清除 2.Django中session中的数据清除
    request.session.clear()
    return redirect('/login/')
