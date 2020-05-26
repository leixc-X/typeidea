from django.shortcuts import redirect
from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        # 通过CommentForm来处理接收数据
        comment_form = CommentForm(request.POST)
        # 存放被评论内容的网址，只需要一个唯一标识当前页面地址的标记即可
        target = request.POST.get('target')

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)