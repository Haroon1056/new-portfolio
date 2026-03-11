from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import (
    Service, Project, ProjectCategory, Testimonial, 
    About, Skill, SocialLink
)
from .forms import ContactForm

def index(request):
    """Home page view"""
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    services = Service.objects.all()[:4]
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    about = About.objects.first()
    skills = Skill.objects.all()[:6] if about else []
    
    # Get contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'featured_projects': featured_projects,
        'services': services,
        'testimonials': testimonials,
        'about': about,
        'skills': skills,
        'form': form,
    }
    return render(request, 'portfolio/index.html', context)

def about(request):
    """About page view"""
    about = About.objects.first()
    skills = Skill.objects.all() if about else []
    
    context = {
        'about': about,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)

def portfolio(request):
    """Portfolio page view"""
    categories = ProjectCategory.objects.all()
    selected_category = request.GET.get('category')
    
    if selected_category:
        projects = Project.objects.filter(category__slug=selected_category)
    else:
        projects = Project.objects.all()
    
    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_detail(request, slug):
    """Portfolio detail page view"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/portfolio-detail.html', context)

def services(request):
    """Services page view"""
    services = Service.objects.all()
    
    context = {
        'services': services,
    }
    return render(request, 'portfolio/services.html', context)

def contact(request):
    """Contact page view"""
    social_links = SocialLink.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'social_links': social_links,
    }
    return render(request, 'portfolio/contact.html', context)