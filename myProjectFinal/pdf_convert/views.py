from django.shortcuts import render
from transport.models import *

# Import for PDF
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.

def show_air(request):
    tickets = Air_Book.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showair.html',context)

def show_bus(request):
    tickets = Bus_Book.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showbus.html',context)


def show_launch(request):
    tickets = Launch_Book.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showlaunch.html',context)

def show_train(request):
    tickets = Train_Book.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showtrain.html',context)

def show_car(request):
    tickets = Car.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showcar.html',context)

def show_bike(request):
    tickets = Bike.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showbike.html',context)

def show_cng(request):
    tickets = CNG.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showcng.html',context)

def show_micro(request):
    tickets = Microbus.objects.all().last()
    context = {
        'tickets':tickets
    }
    return render(request, 'pdf_convert/showmicro.html',context)


def pdf_air(request):
    tickets = Air_Book.objects.all().last()
    template_path = 'pdf_convert/pdfReportair.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="flightreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def pdf_bus(request):
    tickets = Bus_Book.objects.all().last()
    template_path = 'pdf_convert/pdfReportbus.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="bus_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_launch(request):
    tickets = Launch_Book.objects.all().last()
    template_path = 'pdf_convert/pdfReportlaunch.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="launchreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_train(request):
    tickets = Train_Book.objects.all().last()
    template_path = 'pdf_convert/pdfReporttrain.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="trainreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_car(request):
    tickets = Car.objects.all().last()
    template_path = 'pdf_convert/pdfReportcar.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="carreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_bike(request):
    tickets = Bike.objects.all().last()
    template_path = 'pdf_convert/pdfReportbike.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="ridereport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_cng(request):
    tickets = CNG.objects.all().last()
    template_path = 'pdf_convert/pdfReportcng.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="cngreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdf_micro(request):
    tickets = Microbus.objects.all().last()
    template_path = 'pdf_convert/pdfReportmicro.html'
    context = {'tickets': tickets}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="microbusreport.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response    