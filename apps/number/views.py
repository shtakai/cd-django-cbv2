from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured
import random

# Create your views here.
class Main(object):
    template = ''
    favorite_number = None
    least_favorite_number = None
    result = 0
    context = { 'result': result }
    def get(self, request):
        return render(request, self.getTemplate(), self.context)

    def getTemplate(self):
        if self.template == '':
            raise ImproperlyConfigured('"Template" not defined.')
        return self.template

    def add(self, x, y):
        print('add', x, y)
        return x + y

    def subtract(self, x, y):
        print('subtract', x, y)
        return x - y

    def multiply(self, x, y):
        print('multiply', x, y)
        return x * y

    def divide(self, x, y):
        print('divide', x, y)
        return float(x) / y
        # ZeroDivisionErro


class Add(Main, View):
    template = 'number/index.html'
    def get(self,request):
        self.favorite_number = random.randint(201, 999)
        self.least_favorite_number = random.randint(1, 200)
        self.result = super(Add, self).add(self.favorite_number, self.least_favorite_number)
        self.context.update({
            'name': 'Add',
            'result': self.result,
        })
        print('result', self.result)
        print('context', self.context)
        return super(Add, self).get(request)



class Subtract(Main, View):
    template = 'number/index.html'
    def get(self,request):
        self.favorite_number = random.randint(201, 999)
        self.least_favorite_number = random.randint(1, 200)
        self.result = super(Subtract, self).subtract(self.favorite_number, self.least_favorite_number)
        self.context.update({
            'name': 'Subtract',
            'result': self.result,
        })
        print('result', self.result)
        print('context', self.context)
        return super(Subtract, self).get(request)



class Multiply(Main, View):
    template = 'number/index.html'
    def get(self,request):
        self.favorite_number = random.randint(201, 999)
        self.least_favorite_number = random.randint(1, 200)
        self.result = super(Multiply, self).multiply(self.favorite_number, self.least_favorite_number)
        self.context.update({
            'name': 'Multiply',
            'result': self.result,
        })
        print('result', self.result)
        print('context', self.context)
        return super(Multiply, self).get(request)



class Divide(Main, View):
    template = 'number/index.html'
    def get(self,request):
        self.favorite_number = random.randint(201, 999)
        self.least_favorite_number = random.randint(1, 200)
        self.result = super(Divide, self).divide(self.favorite_number, self.least_favorite_number)
        self.context.update({
            'name': 'Divide',
            'result': self.result,
        })
        print('result', self.result)
        print('context', self.context)
        return super(Divide, self).get(request)
