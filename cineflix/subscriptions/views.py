from django.shortcuts import render

from django.views import View

class SubscriptionsView(View):

    template = 'subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template)
