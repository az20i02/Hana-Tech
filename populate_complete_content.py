#!/usr/bin/env python3
"""
Complete Database Population Script for Amazonat Libya
Populates all 36 Django models with original static content

Usage:
1. Copy this file to your Django backend directory
2. Run: python populate_complete_content.py

This will create content for:
- HOME APP: 6 models 
- MISSION APP: 5 models
- SERVICES APP: 8 models  
- OUR_WORK APP: 6 models
- ABOUT_US APP: 5 models
- CORE APP: 6 models
Total: 36 models
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.append('/Users/aziz/Desktop/amazonat_backend')  # Adjust this path as needed

django.setup()

# Import all models
from home.models import HeroSection, Service, MissionSection, ImpactSection, ImpactStat, ImpactHighlight
from mission.models import MissionIntro, Vision, Value, Approach, ApproachPillar
from services.models import (
    ServicesIntro, WorkshopSection, Workshop, LegalSupportSection, 
    LegalService, LegalSupportContact, CommunitySupportSection, CommunityInitiative
)
from our_work.models import (
    WorkIntro, WorkImpactOverview, WorkImpactStat, 
    FeaturedProject, ProjectHighlight, EducationalResource
)
from about_us.models import AboutIntro, OurStory, TeamMember, AboutValue, ContactInformation
from core.models import SiteIdentity, NavigationItem, FooterInfo, FooterQuickLink, FooterContact, SocialLink

def clear_all_data():
    """Clear existing data from all models"""
    print("🗑️  Clearing existing data...")
    
    # Clear all models
    models_to_clear = [
        # HOME APP
        HeroSection, Service, MissionSection, ImpactSection, ImpactStat, ImpactHighlight,
        # MISSION APP  
        MissionIntro, Vision, Value, Approach, ApproachPillar,
        # SERVICES APP
        ServicesIntro, WorkshopSection, Workshop, LegalSupportSection, 
        LegalService, LegalSupportContact, CommunitySupportSection, CommunityInitiative,
        # OUR_WORK APP
        WorkIntro, WorkImpactOverview, WorkImpactStat, 
        FeaturedProject, ProjectHighlight, EducationalResource,
        # ABOUT_US APP
        AboutIntro, OurStory, TeamMember, AboutValue, ContactInformation,
        # CORE APP
        SiteIdentity, NavigationItem, FooterInfo, FooterQuickLink, FooterContact, SocialLink
    ]
    
    for model in models_to_clear:
        model.objects.all().delete()
        print(f"✅ Cleared {model.__name__}")

def populate_home_app():
    """Populate HOME app models"""
    print("\n🏠 Populating HOME app...")
    
    # 1. HeroSection
    hero = HeroSection.objects.create(
        title="Empowering Women",
        highlighted_text="in Libya", 
        subtitle="A safe, warm, and supportive space dedicated to women's rights, offering courses, assistance, and advocacy to build a brighter future for all Libyan women.",
        primary_button_text="Our Services",
        primary_button_link="/services",
        secondary_button_text="Learn More", 
        secondary_button_link="/mission"
    )
    print("✅ Created HeroSection")
    
    # 2. Services (3 entries)
    services_data = [
        {
            "icon": "🎓",
            "title": "Educational Workshops",
            "description": "Comprehensive workshops on women's rights, financial literacy, and professional development.",
            "link_text": "Learn More",
            "link": "/services#workshops"
        },
        {
            "icon": "⚖️", 
            "title": "Legal Support",
            "description": "Free legal consultations and advocacy for women facing discrimination or rights violations.",
            "link_text": "Get Help",
            "link": "/services#legal"
        },
        {
            "icon": "🤝",
            "title": "Community Support",
            "description": "Building networks of support through community events and peer mentorship programs.",
            "link_text": "Join Us",
            "link": "/services#community"
        }
    ]
    
    for service_data in services_data:
        Service.objects.create(**service_data)
    print("✅ Created 3 Services")
    
    # 3. MissionSection
    mission = MissionSection.objects.create(
        title="Our Mission",
        description="""<p>We believe in a Libya where all women have equal rights, opportunities, and protection under the law. Our mission is to empower women through education, advocacy, and community support.</p>
        
<p>Through workshops, legal assistance, and community building, we create safe spaces where women can grow, learn, and advocate for their rights.</p>""",
        button_text="Learn More About Our Mission",
        button_link="/mission"
    )
    print("✅ Created MissionSection")
    
    # 4. ImpactSection
    impact_section = ImpactSection.objects.create(
        title="Our Impact Across Libya",
        description="Through our dedicated efforts, we've made significant strides in empowering women throughout Libya."
    )
    print("✅ Created ImpactSection")
    
    # 5. ImpactStats (4 entries)
    impact_stats_data = [
        {"section": impact_section, "value": "1,500+", "label": "Women Empowered", "order": 1},
        {"section": impact_section, "value": "200+", "label": "Workshops Conducted", "order": 2},
        {"section": impact_section, "value": "85+", "label": "Legal Cases Supported", "order": 3},
        {"section": impact_section, "value": "50+", "label": "Community Events", "order": 4}
    ]
    
    for stat_data in impact_stats_data:
        ImpactStat.objects.create(**stat_data)
    print("✅ Created 4 ImpactStats")
    
    # 6. ImpactHighlights (3 entries)
    impact_highlights_data = [
        {
            "section": impact_section,
            "icon": "🎓",
            "title": "Education Programs",
            "description": "Comprehensive educational workshops covering legal rights, financial literacy, and leadership development.",
            "link_text": "Learn More",
            "link": "/services"
        },
        {
            "section": impact_section,
            "icon": "⚖️",
            "title": "Legal Advocacy",
            "description": "Professional legal support and advocacy services for women facing discrimination and rights violations.",
            "link_text": "Get Support",
            "link": "/services#legal"
        },
        {
            "section": impact_section,
            "icon": "🏘️",
            "title": "Community Building",
            "description": "Creating strong networks of support through community events, mentorship, and peer-to-peer learning.",
            "link_text": "Join Community",
            "link": "/services#community"
        }
    ]
    
    for highlight_data in impact_highlights_data:
        ImpactHighlight.objects.create(**highlight_data)
    print("✅ Created 3 ImpactHighlights")

def populate_mission_app():
    """Populate MISSION app models"""
    print("\n🎯 Populating MISSION app...")
    
    # 1. MissionIntro
    mission_intro = MissionIntro.objects.create(
        title="Our Mission & Vision",
        subtitle="Empowering women across Libya through education, support, and advocacy for equal rights and opportunities."
    )
    print("✅ Created MissionIntro")
    
    # 2. Visions (2 entries)
    visions_data = [
        {
            "title": "Equality Vision",
            "text": "A Libya where all women have equal rights, opportunities, and protection under the law, participating fully in all aspects of society."
        },
        {
            "title": "Empowerment Vision", 
            "text": "Women across Libya are empowered with knowledge, skills, and support networks to achieve their goals and advocate for their rights."
        }
    ]
    
    for vision_data in visions_data:
        Vision.objects.create(**vision_data)
    print("✅ Created 2 Visions")
    
    # 3. Values (3 entries)
    values_data = [
        {
            "title": "Empowerment",
            "description": "Empowering women to reach their full potential and make their voices heard in all spheres of life."
        },
        {
            "title": "Education",
            "description": "Providing quality education and learning opportunities as the foundation for lasting empowerment."
        },
        {
            "title": "Community",
            "description": "Building strong, supportive communities where women can collaborate and support one another."
        }
    ]
    
    for value_data in values_data:
        Value.objects.create(**value_data)
    print("✅ Created 3 Values")
    
    # 4. Approach
    approach = Approach.objects.create(
        section_title="Our Comprehensive Approach",
        section_description="We take a holistic approach to women's empowerment, addressing multiple aspects of women's lives and needs."
    )
    print("✅ Created Approach")
    
    # 5. ApproachPillars (4 entries)
    pillars_data = [
        {
            "approach": approach,
            "title": "Education First",
            "description": "We believe education is the foundation of empowerment, providing knowledge and critical thinking skills."
        },
        {
            "approach": approach,
            "title": "Community Support",
            "description": "Building networks of support and mutual aid where women can learn from and help each other."
        },
        {
            "approach": approach,
            "title": "Legal Advocacy",
            "description": "Advocating for women's rights and legal protections, providing professional legal support when needed."
        },
        {
            "approach": approach,
            "title": "Economic Empowerment",
            "description": "Creating opportunities for economic independence through skills training and entrepreneurship support."
        }
    ]
    
    for pillar_data in pillars_data:
        ApproachPillar.objects.create(**pillar_data)
    print("✅ Created 4 ApproachPillars")

def populate_services_app():
    """Populate SERVICES app models"""
    print("\n🛠️ Populating SERVICES app...")
    
    # 1. ServicesIntro
    services_intro = ServicesIntro.objects.create(
        title="Our Services",
        subtitle="Comprehensive support services designed to empower women through education, legal aid, and community building."
    )
    print("✅ Created ServicesIntro")
    
    # 2. WorkshopSection
    workshop_section = WorkshopSection.objects.create(
        title="Educational Workshops",
        subtitle="Empowering women through knowledge and skills development"
    )
    print("✅ Created WorkshopSection")
    
    # 3. Workshops (4 entries)
    workshops_data = [
        {
            "section": workshop_section,
            "icon": "⚖️",
            "title": "Legal Rights Workshop",
            "description": "Understanding your legal rights, family law, and how to navigate the legal system effectively."
        },
        {
            "section": workshop_section,
            "icon": "💰",
            "title": "Financial Literacy",
            "description": "Personal finance management, budgeting, saving, and building economic independence."
        },
        {
            "section": workshop_section,
            "icon": "👩‍💼",
            "title": "Leadership Development",
            "description": "Building leadership skills, communication, and confidence for professional and personal growth."
        },
        {
            "section": workshop_section,
            "icon": "💻",
            "title": "Digital Skills",
            "description": "Essential computer and internet skills for the modern world, including social media safety."
        }
    ]
    
    for workshop_data in workshops_data:
        Workshop.objects.create(**workshop_data)
    print("✅ Created 4 Workshops")
    
    # 4. LegalSupportSection
    legal_section = LegalSupportSection.objects.create(
        title="Legal Support Services",
        description="Professional legal assistance and advocacy for women facing discrimination, domestic violence, or other rights violations."
    )
    print("✅ Created LegalSupportSection")
    
    # 5. LegalServices (3 entries)
    legal_services_data = [
        {
            "section": legal_section,
            "description": "Free legal consultations with qualified family law attorneys"
        },
        {
            "section": legal_section, 
            "description": "Representation in divorce, custody, and domestic violence cases"
        },
        {
            "section": legal_section,
            "description": "Advocacy and support for workplace discrimination cases"
        }
    ]
    
    for legal_service_data in legal_services_data:
        LegalService.objects.create(**legal_service_data)
    print("✅ Created 3 LegalServices")
    
    # 6. LegalSupportContact
    legal_contact = LegalSupportContact.objects.create(
        section=legal_section,
        text="Contact our legal team for confidential consultation",
        email="legal@amazonat-libya.org",
        phone="+218 21 XXX XXXX"
    )
    print("✅ Created LegalSupportContact")
    
    # 7. CommunitySupportSection  
    community_section = CommunitySupportSection.objects.create(
        title="Community Support Programs",
        subtitle="Building strong networks of mutual support and empowerment",
        image="https://via.placeholder.com/600x400/DDEB9D/000000?text=Community+Support"
    )
    print("✅ Created CommunitySupportSection")
    
    # 8. CommunityInitiatives (3 entries)
    community_initiatives_data = [
        {
            "section": community_section,
            "title": "Mentorship Program",
            "description": "Connecting experienced women leaders with emerging talents for guidance and support."
        },
        {
            "section": community_section,
            "title": "Support Groups",
            "description": "Safe spaces for women to share experiences, challenges, and support each other's growth."
        },
        {
            "section": community_section,
            "title": "Community Events",
            "description": "Regular networking events, cultural celebrations, and awareness campaigns."
        }
    ]
    
    for initiative_data in community_initiatives_data:
        CommunityInitiative.objects.create(**initiative_data)
    print("✅ Created 3 CommunityInitiatives")

def populate_our_work_app():
    """Populate OUR_WORK app models"""
    print("\n💼 Populating OUR_WORK app...")
    
    # 1. WorkIntro
    work_intro = WorkIntro.objects.create(
        title="Our Work & Impact",
        subtitle="Discover our projects and initiatives empowering women across Libya through education, advocacy, and community support."
    )
    print("✅ Created WorkIntro")
    
    # 2. WorkImpactOverview
    impact_overview = WorkImpactOverview.objects.create(
        title="Measuring Our Impact",
        subtitle="Through dedicated effort and community support, we've achieved significant impact across Libya."
    )
    print("✅ Created WorkImpactOverview")
    
    # 3. WorkImpactStats (4 entries)
    work_stats_data = [
        {"section": impact_overview, "value": "250+", "label": "Workshops Conducted"},
        {"section": impact_overview, "value": "5,000+", "label": "Women Supported"},
        {"section": impact_overview, "value": "120+", "label": "Legal Cases Assisted"},
        {"section": impact_overview, "value": "75+", "label": "Community Events"}
    ]
    
    for stat_data in work_stats_data:
        WorkImpactStat.objects.create(**stat_data)
    print("✅ Created 4 WorkImpactStats")
    
    # 4. FeaturedProjects (3 entries)
    featured_projects_data = [
        {
            "title": "Women Leadership Initiative",
            "image": "https://via.placeholder.com/400x300/DDEB9D/000000?text=Leadership+Initiative",
            "description": "Empowering women to take leadership roles in their communities through comprehensive training and mentorship programs."
        },
        {
            "title": "Digital Skills Program", 
            "image": "https://via.placeholder.com/400x300/FAF6E9/000000?text=Digital+Skills",
            "description": "Teaching essential digital skills to women across Libya, including computer literacy, internet safety, and online entrepreneurship."
        },
        {
            "title": "Legal Aid Network",
            "image": "https://via.placeholder.com/400x300/DDEB9D/000000?text=Legal+Aid",
            "description": "Providing legal support and advocacy for women in need, with a network of qualified attorneys and legal professionals."
        }
    ]
    
    projects = []
    for project_data in featured_projects_data:
        project = FeaturedProject.objects.create(**project_data)
        projects.append(project)
    print("✅ Created 3 FeaturedProjects")
    
    # 5. ProjectHighlights (9 entries - 3 per project)
    project_highlights_data = [
        # Leadership Initiative highlights
        {"project": projects[0], "description": "Trained over 200 women in leadership and communication skills"},
        {"project": projects[0], "description": "30+ graduates now serve in community leadership roles"},
        {"project": projects[0], "description": "Established mentorship network connecting 150+ women"},
        
        # Digital Skills highlights  
        {"project": projects[1], "description": "Provided digital literacy training to 500+ women"},
        {"project": projects[1], "description": "85% of participants report improved employment opportunities"},
        {"project": projects[1], "description": "Launched 40+ online businesses by program graduates"},
        
        # Legal Aid highlights
        {"project": projects[2], "description": "Handled 120+ legal cases with 90% success rate"},
        {"project": projects[2], "description": "Provided free consultations to 800+ women"},
        {"project": projects[2], "description": "Established legal clinic in 5 major cities"}
    ]
    
    for highlight_data in project_highlights_data:
        ProjectHighlight.objects.create(**highlight_data)
    print("✅ Created 9 ProjectHighlights")
    
    # 6. EducationalResources (4 entries)
    educational_resources_data = [
        {
            "icon": "https://via.placeholder.com/150x150/DDEB9D/000000?text=Rights+Guide",
            "title": "Women's Rights Guide",
            "description": "Comprehensive guide to women's legal rights in Libya, covering family law, workplace rights, and legal protections.",
            "link_text": "Download PDF",
            "link": "/resources/womens-rights-guide.pdf"
        },
        {
            "icon": "https://via.placeholder.com/150x150/FAF6E9/000000?text=Finance+Book",
            "title": "Financial Literacy Workbook", 
            "description": "Interactive workbook for personal finance education, budgeting, saving, and investment basics.",
            "link_text": "Download PDF",
            "link": "/resources/financial-literacy.pdf"
        },
        {
            "icon": "https://via.placeholder.com/150x150/DDEB9D/000000?text=Leadership",
            "title": "Leadership Training Materials",
            "description": "Training materials for developing leadership skills, public speaking, and team management.",
            "link_text": "Watch Videos",
            "link": "/resources/leadership-training"
        },
        {
            "icon": "https://via.placeholder.com/150x150/FAF6E9/000000?text=Community",
            "title": "Community Building Toolkit",
            "description": "Tools and strategies for building strong communities, organizing events, and creating support networks.",
            "link_text": "Download Toolkit",
            "link": "/resources/community-toolkit.pdf"
        }
    ]
    
    for resource_data in educational_resources_data:
        EducationalResource.objects.create(**resource_data)
    print("✅ Created 4 EducationalResources")

def populate_about_us_app():
    """Populate ABOUT_US app models"""
    print("\n👥 Populating ABOUT_US app...")
    
    # 1. AboutIntro
    about_intro = AboutIntro.objects.create(
        title="About Amazonat Libya",
        subtitle="Learn about our mission, values, and the dedicated team working to empower women across Libya."
    )
    print("✅ Created AboutIntro")
    
    # 2. OurStory
    our_story = OurStory.objects.create(
        title="Our Story",
        image="https://via.placeholder.com/600x400/DDEB9D/000000?text=Our+Story",
        text="""Founded in response to the unique challenges facing women in Libya, Amazonat Libya emerged from a vision of a society where women can fully participate in all aspects of life. Our organization was born out of the recognition that women's rights and empowerment are fundamental to building a just and prosperous society.

We started with a small group of dedicated activists and have grown into a network of professionals, volunteers, and supporters working together to create meaningful change. Our work is driven by the belief that when women are empowered, entire communities thrive.

Today, we continue to expand our reach and impact, always staying true to our core mission of empowering women across Libya through education, legal support, and community building."""
    )
    print("✅ Created OurStory")
    
    # 3. TeamMembers (3 entries)
    team_members_data = [
        {
            "name": "Dr. Amina Hassan",
            "role": "Executive Director",
            "bio": "Leading Amazonat Libya with over 15 years of experience in women's rights advocacy and organizational development.",
            "photo": "https://via.placeholder.com/300x300/DDEB9D/000000?text=Dr.+Amina"
        },
        {
            "name": "Fatima Al-Zahra",
            "role": "Legal Affairs Director", 
            "bio": "Expert in family law and women's legal rights, providing crucial legal support and advocacy services.",
            "photo": "https://via.placeholder.com/300x300/FAF6E9/000000?text=Fatima"
        },
        {
            "name": "Nada Mahmoud",
            "role": "Programs Coordinator",
            "bio": "Coordinating educational workshops and community programs to maximize impact and reach across Libya.",
            "photo": "https://via.placeholder.com/300x300/DDEB9D/000000?text=Nada"
        }
    ]
    
    for member_data in team_members_data:
        TeamMember.objects.create(**member_data)
    print("✅ Created 3 TeamMembers")
    
    # 4. AboutValues (6 entries)
    about_values_data = [
        {
            "icon": "https://via.placeholder.com/80x80/DDEB9D/000000?text=💪",
            "title": "Empowerment",
            "description": "We believe in empowering women to reach their full potential and make their voices heard in all spheres of life."
        },
        {
            "icon": "https://via.placeholder.com/80x80/FAF6E9/000000?text=📚",
            "title": "Education",
            "description": "Education is the foundation of empowerment and the key to creating lasting change in women's lives."
        },
        {
            "icon": "https://via.placeholder.com/80x80/DDEB9D/000000?text=🤝",
            "title": "Community",
            "description": "Strong communities are built on mutual support, collaboration, and shared values among women."
        },
        {
            "icon": "https://via.placeholder.com/80x80/FAF6E9/000000?text=⚖️",
            "title": "Justice",
            "description": "We advocate for equal rights and justice for all women, regardless of their background or circumstances."
        },
        {
            "icon": "https://via.placeholder.com/80x80/DDEB9D/000000?text=🌟",
            "title": "Excellence",
            "description": "We strive for excellence in all our programs and services, ensuring quality and effectiveness."
        },
        {
            "icon": "https://via.placeholder.com/80x80/FAF6E9/000000?text=🌍", 
            "title": "Impact",
            "description": "We are committed to creating meaningful, lasting impact in women's lives and communities across Libya."
        }
    ]
    
    for value_data in about_values_data:
        AboutValue.objects.create(**value_data)
    print("✅ Created 6 AboutValues")
    
    # 5. ContactInformation
    contact_info = ContactInformation.objects.create(
        title="Get in Touch",
        address="123 Liberation Street, Tripoli, Libya",
        email="info@amazonat-libya.org",
        phone="+218 21 XXX XXXX",
        office_hours="Sunday - Thursday: 9:00 AM - 5:00 PM",
        map_embed_url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3347.8!2d13.191!3d32.8925!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMzLCsDUzJzMzLjAiTiAxM8KwMTEnMjcuNiJF!5e0!3m2!1sen!2sly!4v1234567890123!5m2!1sen!2sly"
    )
    print("✅ Created ContactInformation")

def populate_core_app():
    """Populate CORE app models"""
    print("\n⚙️ Populating CORE app...")
    
    # 1. SiteIdentity
    site_identity = SiteIdentity.objects.create(
        logo="https://via.placeholder.com/200x80/DDEB9D/000000?text=Amazonat+Libya",
        site_name="Amazonat Libya",
        slogan="Empowering Women, Building Communities"
    )
    print("✅ Created SiteIdentity")
    
    # 2. NavigationItems (5 entries)
    nav_items_data = [
        {"label": "Home", "link": "/", "order": 1},
        {"label": "Mission", "link": "/mission", "order": 2},
        {"label": "Services", "link": "/services", "order": 3},
        {"label": "Our Work", "link": "/our-work", "order": 4},
        {"label": "About Us", "link": "/about-us", "order": 5}
    ]
    
    for nav_data in nav_items_data:
        NavigationItem.objects.create(**nav_data)
    print("✅ Created 5 NavigationItems")
    
    # 3. FooterInfo
    footer_info = FooterInfo.objects.create(
        organization_name="Amazonat Libya",
        tagline="Empowering women, building stronger communities across Libya.",
        year=2024
    )
    print("✅ Created FooterInfo")
    
    # 4. FooterQuickLinks (4 entries)
    quick_links_data = [
        {"label": "Our Mission", "link": "/mission", "order": 1},
        {"label": "Services", "link": "/services", "order": 2}, 
        {"label": "Our Work", "link": "/our-work", "order": 3},
        {"label": "Contact Us", "link": "/about-us#contact", "order": 4}
    ]
    
    for link_data in quick_links_data:
        FooterQuickLink.objects.create(**link_data)
    print("✅ Created 4 FooterQuickLinks")
    
    # 5. FooterContact
    footer_contact = FooterContact.objects.create(
        email="info@amazonat-libya.org",
        phone="+218 21 XXX XXXX",
        address="123 Liberation Street, Tripoli, Libya"
    )
    print("✅ Created FooterContact")
    
    # 6. SocialLinks (4 entries)
    social_links_data = [
        {
            "icon": "https://via.placeholder.com/32x32/DDEB9D/000000?text=FB",
            "platform": "Facebook",
            "url": "https://facebook.com/amazonat-libya"
        },
        {
            "icon": "https://via.placeholder.com/32x32/FAF6E9/000000?text=TW",
            "platform": "Twitter", 
            "url": "https://twitter.com/amazonat_libya"
        },
        {
            "icon": "https://via.placeholder.com/32x32/DDEB9D/000000?text=IG",
            "platform": "Instagram",
            "url": "https://instagram.com/amazonat_libya"
        },
        {
            "icon": "https://via.placeholder.com/32x32/FAF6E9/000000?text=LI",
            "platform": "LinkedIn",
            "url": "https://linkedin.com/company/amazonat-libya"
        }
    ]
    
    for social_data in social_links_data:
        SocialLink.objects.create(**social_data)
    print("✅ Created 4 SocialLinks")

def main():
    """Main function to populate all data"""
    print("🚀 Starting complete database population for Amazonat Libya...")
    print("=" * 60)
    
    # Clear existing data
    clear_all_data()
    
    # Populate all apps
    populate_home_app()
    populate_mission_app() 
    populate_services_app()
    populate_our_work_app()
    populate_about_us_app()
    populate_core_app()
    
    print("\n" + "=" * 60)
    print("🎉 DATABASE POPULATION COMPLETE!")
    print("\n📊 SUMMARY:")
    print("✅ HOME APP: 6 models populated")
    print("✅ MISSION APP: 5 models populated") 
    print("✅ SERVICES APP: 8 models populated")
    print("✅ OUR_WORK APP: 6 models populated")
    print("✅ ABOUT_US APP: 5 models populated")
    print("✅ CORE APP: 6 models populated")
    print("\n🎯 TOTAL: 36/36 models populated (100%)")
    print("\n🌟 Your website is now 100% dynamic!")
    print("🔗 Visit: http://localhost:3000 to see the dynamic content")

if __name__ == "__main__":
    main() 