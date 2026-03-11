from django.core.management.base import BaseCommand
from portfolio.models import (
    Service, ProjectCategory, Project, Testimonial, 
    About, Skill, SocialLink
)
from datetime import date

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        # Create About
        about = About.objects.create(
            name="John Doe",
            title="Graphic Designer & Creative Director",
            bio="I'm a passionate graphic designer with over 5 years of experience creating stunning visual solutions for brands worldwide.",
            experience_years=5,
            projects_completed=150,
            happy_clients=80,
            awards_won=12
        )
        
        # Create Skills
        skills_data = [
            {"name": "Adobe Photoshop", "percentage": 95},
            {"name": "Adobe Illustrator", "percentage": 90},
            {"name": "Figma", "percentage": 85},
            {"name": "Brand Identity", "percentage": 92},
            {"name": "Typography", "percentage": 88},
            {"name": "UI/UX Design", "percentage": 82},
        ]
        
        for skill_data in skills_data:
            Skill.objects.create(about=about, **skill_data)
        
        # Create Services
        services_data = [
            {
                "title": "Brand Identity",
                "description": "Complete brand identity design including logo, color palette, typography, and brand guidelines.",
                "icon": "fas fa-paint-brush",
                "order": 1
            },
            {
                "title": "UI/UX Design",
                "description": "User-centered interface design for websites and mobile applications.",
                "icon": "fas fa-mobile-alt",
                "order": 2
            },
            {
                "title": "Print Design",
                "description": "High-quality print materials including brochures, business cards, and packaging.",
                "icon": "fas fa-print",
                "order": 3
            },
            {
                "title": "Illustration",
                "description": "Custom illustrations and digital artwork for various purposes.",
                "icon": "fas fa-pencil-ruler",
                "order": 4
            },
        ]
        
        for service_data in services_data:
            Service.objects.create(**service_data)
        
        # Create Categories
        categories_data = [
            {"name": "Branding"},
            {"name": "Web Design"},
            {"name": "Print"},
            {"name": "Illustration"},
        ]
        
        categories = []
        for cat_data in categories_data:
            category = ProjectCategory.objects.create(**cat_data)
            categories.append(category)
        
        # Create Projects
        projects_data = [
            {
                "title": "Modern Cafe Branding",
                "category": categories[0],
                "description": "Complete brand identity for a modern coffee shop including logo, packaging, and interior signage.",
                "client": "Urban Brew Cafe",
                "project_date": date(2024, 1, 15),
                "is_featured": True
            },
            {
                "title": "Tech Startup Website",
                "category": categories[1],
                "description": "Responsive website design for a tech startup focusing on clean UI and smooth user experience.",
                "client": "InnovateTech",
                "project_date": date(2024, 2, 20),
                "is_featured": True
            },
            {
                "title": "Luxury Product Packaging",
                "category": categories[2],
                "description": "Elegant packaging design for a luxury skincare product line.",
                "client": "Luxe Beauty",
                "project_date": date(2024, 3, 10),
                "is_featured": True
            },
        ]
        
        for project_data in projects_data:
            Project.objects.create(**project_data)
        
        # Create Testimonials
        testimonials_data = [
            {
                "client_name": "Sarah Johnson",
                "client_company": "Urban Brew Cafe",
                "testimonial": "Working with John was an absolute pleasure. He understood our vision perfectly and delivered beyond our expectations.",
                "rating": 5,
                "is_active": True
            },
            {
                "client_name": "Michael Chen",
                "client_company": "InnovateTech",
                "testimonial": "John's design expertise helped us create a brand identity that truly represents our company values.",
                "rating": 5,
                "is_active": True
            },
            {
                "client_name": "Emily Williams",
                "client_company": "Luxe Beauty",
                "testimonial": "The packaging design John created for our products has received amazing feedback from our customers.",
                "rating": 5,
                "is_active": True
            },
        ]
        
        for testimonial_data in testimonials_data:
            Testimonial.objects.create(**testimonial_data)
        
        # Create Social Links
        social_data = [
            {"platform": "behance", "url": "https://behance.net/johndoe", "icon": "fab fa-behance", "order": 1},
            {"platform": "dribbble", "url": "https://dribbble.com/johndoe", "icon": "fab fa-dribbble", "order": 2},
            {"platform": "linkedin", "url": "https://linkedin.com/in/johndoe", "icon": "fab fa-linkedin", "order": 3},
            {"platform": "instagram", "url": "https://instagram.com/johndoe", "icon": "fab fa-instagram", "order": 4},
        ]
        
        for social in social_data:
            SocialLink.objects.create(**social)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))