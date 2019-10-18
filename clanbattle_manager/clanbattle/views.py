from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView

from clanbattle.models import *
from clanbattle.forms import BossForm

class BossListView(TemplateView):
    template_name = "clanbattle/boss_list.html"
    #model = models.Boss

    def get(self, request, *args, **kwargs):
        context = super(BossListView, self).get_context_data(**kwargs)

        boss = Boss.objects.all()  # データベースからオブジェクトを取得して
        context['boss'] = boss  # 入れ物に入れる

        return render(self.request, self.template_name, context)


class TargetUpdateView(UpdateView):
    model = Boss
    form_class = BossForm
    success_url = "/clanbattle"



#def update(request, boss_number):
#    b1 = get_object_or_404(Boss, pk=boss_number)
#
#    #b1 = Boss.objects.get(boss_number=boss_number)
#    #b = BossForm(request.POST, instance=b1)
#    #b.save()
#    return HttpResponseRedirect(reverse('clanbattle:index'))
