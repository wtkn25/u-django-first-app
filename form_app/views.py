from django import forms
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView

from .forms import ChoiceForm, QuestionForm


class SampleView(TemplateView):
    template_name = "form_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_form"] = QuestionForm()
        context["choice_forms"] = forms.formset_factory(form=ChoiceForm, extra=3)
        return context

    def post(self, request, **kwargs):
        pass


class DeleteView(RedirectView):
    http_method_names = ["post"]

    def get_redirect_url(self, *args, **kwargs):
        return

    def post(self, request, *args, **kwargs):
        pass


class QuestionCreateView(RedirectView):
    http_method_names = ["post"]

    def get_redirect_url(self):
        return reverse_lazy("form_app:index")

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        print(form)
        # form.save()
