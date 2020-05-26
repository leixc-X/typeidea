from django.contrib import admin
from .models import Link, SideBar
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.

# @admin.register(Link, site=custom_site)
# class LinkAdmin(BaseOwnerAdmin):
#     list_display = ('title', 'href', 'status', 'weight', 'created_time')
#     fields = ('title', 'href', 'status', 'weight')
#
#     def save_model(self, request, obj, form, change):
#         obj.owner = request.user
#         return super(LinkAdmin, self).save_model(request, obj, form, change)

@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    # 自动设置owner，这里request就是当前请求，obj当前要保存的对象，
    # form页面提交过来的表单之后对象，change用于标志本次保存的数据是新增还是更新
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        # super() 函数是用于调用父类(超类)的一个方法
        # super 是用来解决多重继承问题的
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
