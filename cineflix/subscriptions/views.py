from django.shortcuts import render,redirect

from django.views import View

from . models import SubscriptionPlans

from .forms import SubscriptionplansForm

class SubscriptionsView(View):

    template = 'subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):

        plans = SubscriptionPlans.objects.all()

        data = {'plans':plans}

        return render(request,self.template,context=data)
    
class SubscriptionsListVeiw(View):

    template = 'subscriptions/subscription-list,html'

    def get(self,request,*args,**kwargs):

        subscriptionPlans = subscriptionPlans.objects.filter(active_status=True)

        data = {'page':'subscriptionsPlans',
                'subscriptions':subscriptionPlans}
        
        return render(request,self.template,context=data)

class SubscriptionsCreateView(View):

    form_class = SubscriptionplansForm

    template = 'subscriptions/subscription-create.html'

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'page':'create subscription',
                'form':form}
        
        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('subscription-list')
        
        data = {'form':form}

        return render(request,self.template,context=data)

