from django.shortcuts import render
import csv
from io import StringIO
from django.http import HttpResponse
from django.conf import settings

def debug_template_dirs(request):
    dirs = settings.TEMPLATES[0]['DIRS']
    return HttpResponse(f"Template directories: {dirs}")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
    return render(request, 'welcome.html')

# file upload part 

from django.views.generic.base import TemplateView
from chunked_upload.views import ChunkedUploadView, ChunkedUploadCompleteView
from .models import MyChunkedUpload,Company
from .forms import CompanyFilterForm
from django.views.generic import FormView


class ChunkedUploadDemo(TemplateView):
    template_name = 'uploader/upload.html'


class MyChunkedUploadView(ChunkedUploadView):

    model = MyChunkedUpload
    field_name = 'the_file'

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass


class MyChunkedUploadCompleteView(ChunkedUploadCompleteView):

    model = MyChunkedUpload

    def check_permissions(self, request):
        # Allow non authenticated users to make uploads
        pass

    def on_completion(self, uploaded_file, request):
        # Read the file content
        file_content = uploaded_file.read().decode('utf-8')  # 
        
        # Use StringIO to treat the string as a file object
        file_stream = StringIO(file_content)
        reader = csv.DictReader(file_stream)
        
        for row in reader:
            Company.objects.create(
                name=row['name'],
                domain=row['domain'],
                year_founded=row['year founded'],
                industry=row['industry'],
                size_range=row['size range'],
                locality=row['locality'],
                country=row['country'],
                linkedin_url=row['linkedin url'],
                current_employee_estimate=row['current employee estimate'],
                total_employee_estimate=row['total employee estimate']
            )

    def get_response_data(self, chunked_upload, request):
        return {'message': ("You successfully uploaded '%s' (%s bytes)!" %
                            (chunked_upload.filename, chunked_upload.offset))}
    


class QueryBuilderPanelView(FormView):
    template_name = 'query_builder_panel.html'
    form_class = CompanyFilterForm

        

    def form_valid(self, form):
        print("Form is valid")
        industry = form.cleaned_data.get('industry')
        year_founded = form.cleaned_data.get('year_founded')
        country = form.cleaned_data.get('country')
        state = form.cleaned_data.get('state')
        employees_from = form.cleaned_data.get('employees_from')
        employees_to = form.cleaned_data.get('employees_to')
        city = form.cleaned_data.get('city')
        
        filtered_data = Company.objects.all()

        if industry:
            filtered_data = filtered_data.filter(industry=industry)
        if year_founded:
            filtered_data = filtered_data.filter(year_founded=year_founded)
        if country:
            filtered_data = filtered_data.filter(country=country)
        if state:
            filtered_data = filtered_data.filter(locality=state)
        if employees_from:
            filtered_data = filtered_data.filter(total_employee_estimate=employees_from)
        if employees_to:
            filtered_data = filtered_data.filter(current_employee_estimate=employees_to)
        if city:
            filtered_data = filtered_data.filter(locality=city)

        count = filtered_data.count()
        print(count,"count")
        return self.render_to_response(self.get_context_data(form=form, count=count))
    
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserForm
from django.http import JsonResponse
from django.views.generic.edit import DeleteView
from django.contrib import messages

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserForm()
        return context

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_list.html'  # Not used directly, so can be any valid template
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, 'New user added')
        return redirect(self.success_url)

    def form_invalid(self, form):
        return JsonResponse({'error': form.errors}, status=400)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'User deleted successfully')
        return JsonResponse({'message': 'User deleted successfully'}, status=200)