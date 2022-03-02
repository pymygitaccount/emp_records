import csv
import io
from urllib import response

from django.contrib import admin, messages
from django.http import HttpResponse
from django.shortcuts import render

from emp.models import Employee_data


def home(request):
    return render(request, template_name="home.html")

# method created to export the employee data in .csv format.

def csv_export(request):    
    all_active_data = Employee_data.objects.filter(active=True)
    # print(all_active_data)
    # return HttpResponse(all_active_data)
    response = HttpResponse(content_type='text/csv')
    csv_writer = csv.writer(response)
    csv_writer.writerow(["ID", "Name", "Salary", "Company", "Designation", "DOJ", "Active"])

    for emp in all_active_data.values_list('id', 'name', 'salary', 'company', 'designation', 'DOJ', 'active'):
        csv_writer.writerow(emp)

    response['Content-Disposition'] = 'attachement; filename="employee_data.csv" '
    return response



# Method created to import/upload data from cvs file.

def profile_upload(request):
	template = "upload.html"
	data = Employee_data.objects.all()

	prompt = {
        'order': 'Order of the CSV should be name, salary, company, designation, DOJ, active',
        'profiles': data
			}

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = Employee_data.objects.update_or_create(
			name=column[1],
			salary=column[2],
			company=column[3],
			designation=column[4],
			DOJ=column[5],
			active=column[6],

    	)
	context = {}
	return render(request, template, context)

	# --------------------------------------------------------
	# --------------------------------------------------------
	# --------------------------------------------------------
	# --------------------------------------------------------
	# --------------------------------------------------------
	# --------------------------------------------------------




# from django.http import HttpResponse


# def view_c(request):
#     return HttpResponse("in view c")

# def view_d(request):
#     return HttpResponse("in view d")

# def view_c(request):
#     return HttpResponse("in view c")

# def view_d(request):
#     return HttpResponse("in view d")


