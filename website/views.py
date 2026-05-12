from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError

from .forms import EnquiryForm
from .models import GalleryProject
from django.http import HttpResponse


def gallery(request):

    projects = GalleryProject.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'gallery.html', context)


def home(request):

    form = EnquiryForm()

    if request.method == 'POST':

        form = EnquiryForm(request.POST)

        if form.is_valid():
            try:
                enquiry = form.save()

                subject = "New Website Enquiry - Surve Prozone"

                email_message = f"""
New enquiry received from website.

Name: {enquiry.name}
Email: {enquiry.email}
Phone: {enquiry.phone}

Message:
{enquiry.message}
"""

                try:
                    send_mail(
                        subject,
                        email_message,
                        settings.EMAIL_HOST_USER,
                        [settings.EMAIL_HOST_USER],
                        fail_silently=False,
                    )
                    print("EMAIL SENT SUCCESSFULLY")
                except Exception as e:
                    print("EMAIL ERROR:", e)

                messages.success(
                    request,
                    "Your enquiry has been submitted successfully. Our team will contact you soon."
                )

                return redirect('/#contact')

            except IntegrityError:
                messages.error(
                    request,
                    "You have already submitted an enquiry with this email and phone number. Our team will contact you soon."
                )

                return redirect('/#contact')

        else:
            messages.error(
                request,
                "Please correct the errors below and submit again."
            )

    featured_projects = GalleryProject.objects.filter(is_featured=True)[:6]

    return render(request, 'base.html', {
        'form': form,
        'featured_projects': featured_projects
    })


def robots_txt(request):
    content = render(request, 'robots.txt')
    return HttpResponse(content, content_type='text/plain')


def sitemap_xml(request):
    content = render(request, 'sitemap.xml')
    return HttpResponse(content, content_type='application/xml')