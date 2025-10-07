import streamlit as st
import json
from datetime import datetime

class ATSResumeBuilder:
    def __init__(self):
        self.ats_keywords = [
            # Technical Skills
            "Python", "JavaScript", "Java", "C++", "SQL", "React", "Node.js", "AWS", "Docker", "Kubernetes",
            "Machine Learning", "Data Analysis", "Web Development", "API", "REST", "Git", "Agile", "Scrum",
            "DevOps", "CI/CD", "Testing", "Debugging", "Optimization", "Automation", "Security",
            # Soft Skills
            "Leadership", "Communication", "Teamwork", "Problem Solving", "Project Management",
            "Critical Thinking", "Time Management", "Adaptability", "Creativity", "Collaboration"
        ]
    
    def create_ats_friendly_resume(self, personal_info, experience, education, skills, projects):
        """Generate an ATS-optimized resume"""
        
        resume = f"""
# {personal_info.get('name', 'Your Name').upper()}
{personal_info.get('title', 'Professional Title')}

## Contact Information
- 📧 Email: {personal_info.get('email', 'your.email@example.com')}
- 📱 Phone: {personal_info.get('phone', '+1 (555) 123-4567')}
- 🔗 LinkedIn: {personal_info.get('linkedin', 'linkedin.com/in/yourprofile')}
- 🌐 Portfolio: {personal_info.get('portfolio', 'yourportfolio.com')}
- 📍 Location: {personal_info.get('location', 'City, State')}

## Professional Summary
{self._generate_professional_summary(personal_info, experience, skills)}

## Technical Skills
{self._format_skills_section(skills)}

## Professional Experience
{self._format_experience_section(experience)}

## Projects
{self._format_projects_section(projects)}

## Education
{self._format_education_section(education)}

## Certifications
{personal_info.get('certifications', '• Relevant certifications will appear here')}
        """
        
        return resume
    
    def _generate_professional_summary(self, personal_info, experience, skills):
        """Generate an ATS-optimized professional summary"""
        
        years_exp = experience[0].get('years', '2+') if experience else '2+'
        primary_skills = ', '.join(skills.get('programming_languages', ['Python', 'JavaScript'])[:3])
        domain = personal_info.get('domain', 'software development')
        
        summary = f"""Results-driven {personal_info.get('title', 'Professional')} with {years_exp} years of experience in {domain}. 
Proficient in {primary_skills} with demonstrated success in delivering high-quality solutions. 
Strong problem-solving abilities combined with excellent communication and teamwork skills. 
Seeking to leverage technical expertise and innovative thinking to drive success at {personal_info.get('target_company', 'a forward-thinking organization')}."""
        
        return summary
    
    def _format_skills_section(self, skills):
        """Format skills section for ATS optimization"""
        
        skills_text = ""
        for category, skill_list in skills.items():
            if skill_list:
                category_name = category.replace('_', ' ').title()
                skills_text += f"**{category_name}:** {', '.join(skill_list)}\n\n"
        
        return skills_text.strip()
    
    def _format_experience_section(self, experience):
        """Format experience section with ATS-friendly bullet points"""
        
        experience_text = ""
        for job in experience:
            experience_text += f"### {job.get('position', 'Position')}\n"
            experience_text += f"**{job.get('company', 'Company')}** | {job.get('duration', 'Duration')}\n\n"
            
            for responsibility in job.get('responsibilities', []):
                # Start with action verbs (ATS-friendly)
                experience_text += f"• {responsibility}\n"
            
            experience_text += "\n"
        
        return experience_text.strip()
    
    def _format_projects_section(self, projects):
        """Format projects section"""
        
        projects_text = ""
        for project in projects:
            projects_text += f"### {project.get('name', 'Project Name')}\n"
            projects_text += f"*Technologies: {', '.join(project.get('technologies', []))}*\n\n"
            projects_text += f"{project.get('description', 'Project description')}\n\n"
        
        return projects_text.strip()
    
    def _format_education_section(self, education):
        """Format education section"""
        
        education_text = ""
        for edu in education:
            education_text += f"### {edu.get('degree', 'Degree')}\n"
            education_text += f"**{edu.get('institution', 'Institution')}** | {edu.get('year', 'Year')}\n"
            education_text += f"*{edu.get('details', 'Relevant details')}*\n\n"
        
        return education_text.strip()
    
    def analyze_ats_score(self, resume_text, job_description=""):
        """Analyze how ATS-friendly the resume is"""
        
        score = 0
        max_score = 100
        feedback = []
        
        # Check for keywords
        found_keywords = []
        for keyword in self.ats_keywords:
            if keyword.lower() in resume_text.lower():
                found_keywords.append(keyword)
                score += 2
        
        # Check structure
        sections = ["experience", "education", "skills", "projects", "summary"]
        for section in sections:
            if section in resume_text.lower():
                score += 5
            else:
                feedback.append(f"Consider adding a '{section.title()}' section")
        
        # Check length
        word_count = len(resume_text.split())
        if 400 <= word_count <= 800:
            score += 10
        else:
            feedback.append("Resume length should be between 400-800 words for optimal ATS performance")
        
        # Check contact info
        contact_items = ["@", "linkedin", "github"]
        for item in contact_items:
            if item in resume_text.lower():
                score += 5
        
        # Normalize score
        final_score = min(score, max_score)
        
        return {
            'score': final_score,
            'found_keywords': found_keywords,
            'missing_keywords': [k for k in self.ats_keywords if k.lower() not in resume_text.lower()][:10],
            'feedback': feedback,
            'word_count': word_count
        }

# Global instance
resume_builder = ATSResumeBuilder()
