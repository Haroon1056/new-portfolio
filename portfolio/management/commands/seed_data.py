from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import (
    Service, ProjectCategory, Project, Testimonial, 
    About, Skill, SocialLink
)
from datetime import date
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to seed database...'))
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='nimra').exists():
            User.objects.create_superuser('nimra', 'nimranaseeb101@gmail.com', 'nimra1056')
            self.stdout.write(self.style.SUCCESS('Superuser "nimra" created'))
        
        # Create About
        about, created = About.objects.get_or_create(
            name="John Doe",
            defaults={
                "title": "Graphic Designer & Creative Director",
                "bio": "I'm a passionate graphic designer with over 5 years of experience creating stunning visual solutions for brands worldwide. I specialize in brand identity, UI/UX design, and illustration. My goal is to help businesses communicate their message through beautiful, functional design.",
                "experience_years": 5,
                "projects_completed": 150,
                "happy_clients": 80,
                "awards_won": 12
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('About section created'))
        
        # Create Skills
        skills_data = [
            {"name": "Adobe Photoshop", "percentage": 95, "order": 1},
            {"name": "Adobe Illustrator", "percentage": 90, "order": 2},
            {"name": "Figma", "percentage": 85, "order": 3},
            {"name": "Brand Identity", "percentage": 92, "order": 4},
            {"name": "Typography", "percentage": 88, "order": 5},
            {"name": "UI/UX Design", "percentage": 82, "order": 6},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                about=about,
                name=skill_data["name"],
                defaults={
                    "percentage": skill_data["percentage"],
                    "order": skill_data["order"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Skill "{skill.name}" created'))
        
        # Create Services
        services_data = [
            {
                "title": "Brand Identity",
                "description": "Complete brand identity design including logo, color palette, typography, and brand guidelines. I create cohesive visual systems that tell your brand's story.",
                "icon": "fas fa-paint-brush",
                "order": 1
            },
            {
                "title": "UI/UX Design",
                "description": "User-centered interface design for websites and mobile applications. I focus on creating intuitive, engaging experiences that users love.",
                "icon": "fas fa-mobile-alt",
                "order": 2
            },
            {
                "title": "Print Design",
                "description": "High-quality print materials including brochures, business cards, and packaging. From concept to print, I ensure your materials stand out.",
                "icon": "fas fa-print",
                "order": 3
            },
            {
                "title": "Illustration",
                "description": "Custom illustrations and digital artwork for various purposes. I create unique visuals that capture attention and communicate your message.",
                "icon": "fas fa-pencil-ruler",
                "order": 4
            },
            {
                "title": "Social Media Design",
                "description": "Engaging social media graphics, posts, and stories that build your brand presence across all platforms.",
                "icon": "fas fa-share-alt",
                "order": 5
            },
            {
                "title": "Motion Graphics",
                "description": "Animated logos, explainer videos, and motion graphics that bring your brand to life with dynamic visual content.",
                "icon": "fas fa-video",
                "order": 6
            },
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data["title"],
                defaults={
                    "description": service_data["description"],
                    "icon": service_data["icon"],
                    "order": service_data["order"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Service "{service.title}" created'))
        
        # Create Categories
        categories_data = [
            {"name": "Branding", "slug": "branding"},
            {"name": "Web Design", "slug": "web-design"},
            {"name": "Print", "slug": "print"},
            {"name": "Illustration", "slug": "illustration"},
            {"name": "Packaging", "slug": "packaging"},
            {"name": "Social Media", "slug": "social-media"},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = ProjectCategory.objects.get_or_create(
                name=cat_data["name"],
                defaults={"slug": cat_data["slug"]}
            )
            categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Category "{category.name}" created'))
        
        # Create Projects
        projects_data = [
            {
                "title": "Urban Brew Cafe Branding",
                "category": categories[0],  # Branding
                "description": "Complete brand identity for a modern coffee shop including logo, packaging, interior signage, and digital presence. The design focuses on warm, inviting aesthetics with a contemporary twist.",
                "client": "Urban Brew Cafe",
                "project_date": date(2024, 1, 15),
                "is_featured": True
            },
            {
                "title": "InnovateTech Website Redesign",
                "category": categories[1],  # Web Design
                "description": "Responsive website design for a tech startup focusing on clean UI and smooth user experience. The site features intuitive navigation and showcases their innovative products.",
                "client": "InnovateTech",
                "project_date": date(2024, 2, 20),
                "is_featured": True
            },
            {
                "title": "Luxe Beauty Packaging",
                "category": categories[4],  # Packaging
                "description": "Elegant packaging design for a luxury skincare product line. The design uses minimalist aesthetics with premium finishes to convey quality and sophistication.",
                "client": "Luxe Beauty",
                "project_date": date(2024, 3, 10),
                "is_featured": True
            },
            {
                "title": "GreenLeaf Organic Branding",
                "category": categories[0],  # Branding
                "description": "Eco-friendly brand identity for an organic grocery store chain. The design incorporates natural elements and sustainable messaging throughout.",
                "client": "GreenLeaf Markets",
                "project_date": date(2024, 4, 5),
                "is_featured": False
            },
            {
                "title": "TechConf 2024 Materials",
                "category": categories[2],  # Print
                "description": "Comprehensive print materials for a major tech conference including programs, badges, banners, and promotional materials.",
                "client": "TechConf",
                "project_date": date(2024, 5, 12),
                "is_featured": False
            },
            {
                "title": "Children's Book Illustrations",
                "category": categories[3],  # Illustration
                "description": "Whimsical illustrations for a children's book series. The artwork brings the stories to life with colorful, engaging characters and scenes.",
                "client": "Wonder Books",
                "project_date": date(2024, 6, 18),
                "is_featured": True
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data["title"],
                defaults={
                    "category": project_data["category"],
                    "description": project_data["description"],
                    "client": project_data["client"],
                    "project_date": project_data["project_date"],
                    "is_featured": project_data["is_featured"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Project "{project.title}" created'))
        
        # Create Testimonials
        testimonials_data = [
            {
                "client_name": "Sarah Johnson",
                "client_company": "Urban Brew Cafe",
                "testimonial": "Working with John was an absolute pleasure. He understood our vision perfectly and delivered a brand identity that exceeded our expectations. Our customers love the new look!",
                "rating": 5,
                "is_active": True
            },
            {
                "client_name": "Michael Chen",
                "client_company": "InnovateTech",
                "testimonial": "John's design expertise helped us create a website that truly represents our company values. The user experience is seamless and our conversion rates have improved significantly.",
                "rating": 5,
                "is_active": True
            },
            {
                "client_name": "Emily Williams",
                "client_company": "Luxe Beauty",
                "testimonial": "The packaging design John created for our products has received amazing feedback from our customers. The attention to detail and premium feel perfectly matches our brand.",
                "rating": 5,
                "is_active": True
            },
            {
                "client_name": "David Thompson",
                "client_company": "GreenLeaf Markets",
                "testimonial": "John captured our eco-friendly mission perfectly in the branding. The designs are fresh, modern, and communicate our values effectively. Highly recommended!",
                "rating": 5,
                "is_active": True
            },
            {
                "client_name": "Lisa Anderson",
                "client_company": "Wonder Books",
                "testimonial": "The illustrations John created for our children's books are magical! They perfectly capture the spirit of the stories and children absolutely love them.",
                "rating": 5,
                "is_active": True
            },
        ]
        
        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                client_name=testimonial_data["client_name"],
                client_company=testimonial_data["client_company"],
                defaults={
                    "testimonial": testimonial_data["testimonial"],
                    "rating": testimonial_data["rating"],
                    "is_active": testimonial_data["is_active"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Testimonial from "{testimonial.client_name}" created'))
        
        # Create Social Links
        social_data = [
            {"platform": "behance", "url": "https://behance.net/johndoe", "icon": "fab fa-behance", "order": 1},
            {"platform": "dribbble", "url": "https://dribbble.com/johndoe", "icon": "fab fa-dribbble", "order": 2},
            {"platform": "linkedin", "url": "https://linkedin.com/in/johndoe", "icon": "fab fa-linkedin", "order": 3},
            {"platform": "instagram", "url": "https://instagram.com/johndoe", "icon": "fab fa-instagram", "order": 4},
            {"platform": "twitter", "url": "https://twitter.com/johndoe", "icon": "fab fa-twitter", "order": 5},
        ]
        
        for social in social_data:
            link, created = SocialLink.objects.get_or_create(
                platform=social["platform"],
                defaults={
                    "url": social["url"],
                    "icon": social["icon"],
                    "order": social["order"]
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Social link for "{link.platform}" created'))
        
        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))