from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from .models import Poem
from .forms import PoemForm
# Create your views here.

class PoemList(View):
    model = Poem
    template_name = 'poem_app/poem_list.html'

    def get(self, request):
        poem_list = self.model.objects.all()
        return render(
            request,
            self.template_name,
            {'poems':poem_list}
        )

class PoemDetail(View):
    model = Poem
    template_name = 'poem_app/poem_detail.html'

    def get(self, request, slug):
        poem = get_object_or_404(self.model, slug__iexact=slug)
        return render(
            request,
            self.template_name,
            {'poem':poem}
        )

class PoemCreate(View):
    template_name = "poem_app/poem_create.html"
    form_class = PoemForm

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form':self.form_class()}
        )

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_poem = bound_form.save()
            return redirect(new_poem)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form}
            )

class PoemDelete(View):
    model = Poem
    template_name = 'poem_app/poem_delete.html'
    success_url = reverse_lazy('poem:list')

    def get(self, request, slug):
        poem = get_object_or_404(self.model, slug__iexact=slug)
        context = {'poem':poem}
        return render(
            request,
            self.template_name,
            context
        )
    
    def post(self, request, slug):
        poem = get_object_or_404(self.model, slug__iexact=slug)
        poem.delete()
        return HttpResponseRedirect(self.success_url)

class PoemUpdate(View):
    model = Poem
    template_name = 'poem_app/poem_update.html'
    form_class = PoemForm

    def get(self, request, slug):
        poem = get_object_or_404(self.model, slug__iexact=slug)
        return render(
            request,
            self.template_name,
            {'form':self.form_class(instance=poem),
             'poem':poem}
        )

    def post(self, request, slug):
        poem = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form_class(request.POST, instance=poem)
        if bound_form.is_valid():
            update_poem = bound_form.save()
            return redirect(update_poem)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form,
                 'poem':poem}
            )
