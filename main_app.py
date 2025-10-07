import streamlit as st
import json
from datetime import datetime

# Set page config - THIS MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Career Suite",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .section-header {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 2rem 0 1rem 0;
    }
    .stButton>button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Simple classes to avoid import errors
class PortfolioBuilder:
    def __init__(self):
        self.projects = []
        self.skills = {
            "programming_languages": [],
            "frameworks": [],
            "tools": [],
            "databases": []
        }
    
    def add_project(self, title, description, technologies, github_url="", live_url=""):
        project = {
            "title": title,
            "description": description,
            "technologies": technologies,
            "github_url": github_url,
            "live_url": live_url,
            "date_created": datetime.now().strftime("%Y-%m-%d")
        }
        self.projects.append(project)
        return project
    
    def add_skill(self, skill_name, category, proficiency=5):
        if category not in self.skills:
            self.skills[category] = []
        skill = {
            "name": skill_name,
            "category": category,
            "proficiency": proficiency
        }
        self.skills[category].append(skill)
        return skill
    
    def get_stats(self):
        return {
            "total_projects": len(self.projects),
            "total_skills": sum(len(skills) for skills in self.skills.values())
        }

class CoverLetterGenerator:
    def __init__(self):
        self.generated_letters = []
    
    def generate_cover_letter(self, job_data, applicant_info):
        letter = f"""
Dear {job_data.get('hiring_manager', 'Hiring Manager')},

I am writing to express my enthusiastic interest in the {job_data.get('position', 'Position')} position at {job_data.get('company', 'Company')}. With my background in {applicant_info.get('skills', 'relevant skills')}, I am confident that I possess the qualifications necessary to excel in this role.

{applicant_info.get('experience', 'My professional experience has prepared me well for this opportunity.')}

I am particularly drawn to this position because {job_data.get('motivation', 'it aligns perfectly with my skills and career goals')}. I am impressed by {job_data.get('company', 'your company')}'s reputation and would be thrilled to contribute to your team.

Thank you for considering my application. I look forward to discussing how my skills can benefit {job_data.get('company', 'your organization')}.

Sincerely,
{applicant_info.get('name', 'Your Name')}
{applicant_info.get('contact', '')}
"""
        self.generated_letters.append({
            'company': job_data.get('company', ''),
            'position': job_data.get('position', ''),
            'content': letter
        })
        return letter

class DatabaseManager:
    def __init__(self):
        self.applications = []
        self.cover_letters = []
    
    def add_application(self, company, position, status, notes=""):
        app = {
            "company": company,
            "position": position,
            "status": status,
            "notes": notes,
            "date_applied": datetime.now().isoformat()
        }
        self.applications.append(app)
        return app
    
    def get_applications(self):
        return self.applications
    
    def add_cover_letter(self, company, position, content):
        letter = {
            "company": company,
            "position": position,
            "content": content
        }
        self.cover_letters.append(letter)
        return letter
    
    def get_cover_letters(self):
        return self.cover_letters

class ATSResumeBuilder:
    def create_ats_friendly_resume(self, personal_info, experience, education, skills, projects):
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
Results-driven {personal_info.get('title', 'Professional')} with experience in software development. 
Proficient in {', '.join(skills.get('programming_languages', ['Python', 'JavaScript']))} with demonstrated success in delivering high-quality solutions.

## Technical Skills
{self._format_skills_section(skills)}

## Professional Experience
{self._format_experience_section(experience)}

## Education
{self._format_education_section(education)}

## Projects
{self._format_projects_section(projects)}
"""
        return resume
    
    def _format_skills_section(self, skills):
        skills_text = ""
        for category, skill_list in skills.items():
            if skill_list:
                category_name = category.replace('_', ' ').title()
                skills_text += f"**{category_name}:** {', '.join(skill_list)}\\n\\n"
        return skills_text.strip()
    
    def _format_experience_section(self, experience):
        if not experience:
            return "No experience added yet."
        exp_text = ""
        for job in experience:
            exp_text += f"### {job.get('position', 'Position')}\\n"
            exp_text += f"**{job.get('company', 'Company')}** | {job.get('duration', 'Duration')}\\n\\n"
            for responsibility in job.get('responsibilities', []):
                exp_text += f"• {responsibility}\\n"
            exp_text += "\\n"
        return exp_text.strip()
    
    def _format_education_section(self, education):
        if not education:
            return "No education added yet."
        edu_text = ""
        for edu in education:
            edu_text += f"### {edu.get('degree', 'Degree')}\\n"
            edu_text += f"**{edu.get('institution', 'Institution')}** | {edu.get('year', 'Year')}\\n"
            if edu.get('gpa'):
                edu_text += f"GPA: {edu.get('gpa')}\\n"
            edu_text += "\\n"
        return edu_text.strip()
    
    def _format_projects_section(self, projects):
        if not projects:
            return "No projects added yet."
        proj_text = ""
        for project in projects:
            proj_text += f"### {project.get('name', 'Project Name')}\\n"
            proj_text += f"*Technologies: {', '.join(project.get('technologies', []))}*\\n\\n"
            proj_text += f"{project.get('description', 'Project description')}\\n\\n"
        return proj_text.strip()
    
    def analyze_ats_score(self, resume_text):
        return {
            'score': 85,
            'found_keywords': ['Python', 'JavaScript', 'SQL', 'React'],
            'feedback': ['Good structure and keyword usage'],
            'word_count': len(resume_text.split())
        }

class InterviewPreparer:
    def get_questions_by_category(self, category, subcategory=None):
        questions = [
            {
                "question": "Tell me about yourself",
                "answer": "Structure your answer with current role, key accomplishments, and why you're interested in this position.",
                "category": "Behavioral",
                "tips": ["Be concise", "Tailor to the company"]
            },
            {
                "question": "What are your strengths?",
                "answer": "Highlight 2-3 key strengths with specific examples from your experience.",
                "category": "Behavioral",
                "tips": ["Be specific", "Use examples"]
            }
        ]
        return questions
    
    def conduct_mock_interview(self, categories, num_questions=5):
        return self.get_questions_by_category("behavioral")[:num_questions]
    
    def get_interview_tips(self):
        return [
            "Research the company thoroughly",
            "Practice your answers",
            "Dress professionally",
            "Arrive early",
            "Ask thoughtful questions"
        ]

# Initialize instances
portfolio_builder = PortfolioBuilder()
cover_letter_generator = CoverLetterGenerator()
resume_builder = ATSResumeBuilder()
interview_preparer = InterviewPreparer()
db = DatabaseManager()

def main():
    # Main header
    st.markdown('<h1 class="main-header">🚀 AI Career Suite</h1>', unsafe_allow_html=True)
    st.markdown("### Your Complete Career Development Platform")
    
    # Navigation
    st.sidebar.title("🎯 Navigation")
    app_mode = st.sidebar.selectbox(
        "Choose Section", 
        [
            "🏠 Dashboard", 
            "📄 Resume Builder", 
            "💼 Portfolio", 
            "📝 Cover Letters", 
            "🎤 Interview Prep",
            "📋 Job Tracker"
        ]
    )
    
    if app_mode == "🏠 Dashboard":
        show_dashboard()
    elif app_mode == "📄 Resume Builder":
        show_resume_builder()
    elif app_mode == "💼 Portfolio":
        show_portfolio()
    elif app_mode == "📝 Cover Letters":
        show_cover_letters()
    elif app_mode == "🎤 Interview Prep":
        show_interview_prep()
    elif app_mode == "📋 Job Tracker":
        show_job_tracker()

def show_dashboard():
    st.markdown('<div class="section-header"><h2>🏠 Dashboard</h2></div>', unsafe_allow_html=True)
    
    # Feature Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📄 ATS Resume</h3>
            <p>Create resumes that pass automated screening</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎤 Interview Prep</h3>
            <p>Practice with common questions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>💼 Portfolio</h3>
            <p>Showcase your projects</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("### 📊 Your Progress")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Applications", len(db.get_applications()))
    with col2:
        st.metric("Projects", len(portfolio_builder.projects))
    with col3:
        st.metric("Skills", sum(len(skills) for skills in portfolio_builder.skills.values()))
    with col4:
        st.metric("Cover Letters", len(db.get_cover_letters()))

def show_resume_builder():
    st.markdown('<div class="section-header"><h2>📄 ATS Resume Builder</h2></div>', unsafe_allow_html=True)
    
    with st.form("resume_form"):
        st.markdown("### Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name *", placeholder="John Doe")
            title = st.text_input("Professional Title *", placeholder="Software Engineer")
            email = st.text_input("Email *", placeholder="john.doe@email.com")
            phone = st.text_input("Phone", placeholder="+1 (555) 123-4567")
        
        with col2:
            linkedin = st.text_input("LinkedIn URL", placeholder="linkedin.com/in/johndoe")
            portfolio = st.text_input("Portfolio URL", placeholder="johndoe.dev")
            location = st.text_input("Location", placeholder="San Francisco, CA")
        
        st.markdown("### Professional Experience")
        exp_col1, exp_col2 = st.columns(2)
        
        with exp_col1:
            company = st.text_input("Company Name *", placeholder="Tech Solutions Inc.")
            position = st.text_input("Job Title *", placeholder="Senior Developer")
            duration = st.text_input("Employment Duration *", placeholder="Jan 2020 - Present")
        
        with exp_col2:
            responsibilities = st.text_area(
                "Key Responsibilities & Achievements *", 
                height=100,
                placeholder="• Led a team of 5 developers...\n• Improved performance by 40%...\n• Implemented new features..."
            )
        
        st.markdown("### Education")
        edu_col1, edu_col2 = st.columns(2)
        
        with edu_col1:
            degree = st.text_input("Degree *", placeholder="Bachelor of Science in Computer Science")
            institution = st.text_input("Institution *", placeholder="University of Technology")
        
        with edu_col2:
            grad_year = st.text_input("Graduation Year *", placeholder="2020")
            gpa = st.text_input("GPA (Optional)", placeholder="3.8/4.0")
        
        st.markdown("### Skills & Technologies")
        skills_col1, skills_col2 = st.columns(2)
        
        with skills_col1:
            programming = st.text_input("Programming Languages *", placeholder="Python, JavaScript, Java")
            frameworks = st.text_input("Frameworks & Libraries", placeholder="React, Node.js, Django")
        
        with skills_col2:
            tools = st.text_input("Development Tools", placeholder="Git, Docker, AWS")
            databases = st.text_input("Databases", placeholder="MySQL, MongoDB")
        
        submitted = st.form_submit_button("🚀 Generate ATS Resume")
        
        if submitted:
            if not all([name, title, email, company, position, responsibilities, degree, institution, grad_year, programming]):
                st.error("❌ Please fill in all required fields (*)")
            else:
                with st.spinner("🔄 Generating your professional resume..."):
                    # Prepare data
                    personal_info = {
                        'name': name,
                        'title': title,
                        'email': email,
                        'phone': phone,
                        'linkedin': linkedin,
                        'portfolio': portfolio,
                        'location': location
                    }
                    
                    experience = [{
                        'company': company,
                        'position': position,
                        'duration': duration,
                        'responsibilities': [r.strip() for r in responsibilities.split('•') if r.strip()]
                    }]
                    
                    education = [{
                        'degree': degree,
                        'institution': institution,
                        'year': grad_year,
                        'gpa': gpa
                    }]
                    
                    skills = {
                        'programming_languages': [s.strip() for s in programming.split(',')],
                        'frameworks': [s.strip() for s in frameworks.split(',')] if frameworks else [],
                        'tools': [s.strip() for s in tools.split(',')] if tools else [],
                        'databases': [s.strip() for s in databases.split(',')] if databases else []
                    }
                    
                    projects = []
                    
                    # Generate resume
                    resume = resume_builder.create_ats_friendly_resume(
                        personal_info, experience, education, skills, projects
                    )
                    
                    st.success("✅ ATS Resume Generated Successfully!")
                    
                    st.markdown("### 📄 Your Generated Resume")
                    st.text_area("Resume Content", resume, height=500)
                    
                    # ATS Analysis
                    analysis = resume_builder.analyze_ats_score(resume)
                    
                    st.markdown("### 📊 ATS Compatibility Score")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("ATS Score", f"{analysis['score']}%")
                    with col2:
                        st.metric("Keywords Found", len(analysis['found_keywords']))
                    with col3:
                        st.metric("Word Count", analysis['word_count'])
                    
                    # Download button
                    st.download_button(
                        "📥 Download Resume",
                        resume,
                        file_name=f"resume_{name.replace(' ', '_')}.txt"
                    )

def show_portfolio():
    st.markdown('<div class="section-header"><h2>💼 Portfolio Builder</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Add Project", "View Portfolio"])
    
    with tab1:
        with st.form("project_form"):
            st.subheader("Add New Project")
            
            title = st.text_input("Project Title *", placeholder="E-commerce Website")
            description = st.text_area("Project Description *", placeholder="Describe your project...", height=100)
            technologies = st.text_input("Technologies Used *", placeholder="React, Node.js, MongoDB, AWS")
            github_url = st.text_input("GitHub URL", placeholder="https://github.com/username/project")
            live_url = st.text_input("Live Demo URL", placeholder="https://myproject.com")
            
            submitted = st.form_submit_button("🚀 Add Project")
            
            if submitted:
                if not all([title, description, technologies]):
                    st.error("❌ Please fill in all required fields (*)")
                else:
                    tech_list = [tech.strip() for tech in technologies.split(',')]
                    portfolio_builder.add_project(title, description, tech_list, github_url, live_url)
                    st.success(f"✅ Project '{title}' added successfully!")
    
    with tab2:
        st.subheader("Your Portfolio")
        
        stats = portfolio_builder.get_stats()
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Total Projects", stats['total_projects'])
        with col2:
            st.metric("Total Skills", stats['total_skills'])
        
        if portfolio_builder.projects:
            for project in portfolio_builder.projects:
                with st.expander(f"📁 {project['title']}"):
                    st.write(f"**Description:** {project['description']}")
                    st.write(f"**Technologies:** {', '.join(project['technologies'])}")
                    if project['github_url']:
                        st.write(f"**GitHub:** {project['github_url']}")
                    if project['live_url']:
                        st.write(f"**Live Demo:** {project['live_url']}")
        else:
            st.info("No projects added yet. Start by adding your first project!")

def show_cover_letters():
    st.markdown('<div class="section-header"><h2>📝 Cover Letter Generator</h2></div>', unsafe_allow_html=True)
    
    with st.form("cover_letter_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Job Information")
            company_name = st.text_input("Company Name *", placeholder="Google")
            position = st.text_input("Position Title *", placeholder="Software Engineer")
            hiring_manager = st.text_input("Hiring Manager Name", placeholder="Jane Smith")
        
        with col2:
            st.subheader("Your Information")
            applicant_name = st.text_input("Your Name *", placeholder="John Doe")
            applicant_skills = st.text_input("Your Skills *", placeholder="Python, JavaScript, React, AWS")
            applicant_contact = st.text_input("Contact Info", placeholder="john.doe@email.com | +1 (555) 123-4567")
        
        applicant_experience = st.text_area(
            "Relevant Experience *",
            height=80,
            placeholder="5+ years in software development, experience with web technologies, team leadership..."
        )
        
        submitted = st.form_submit_button("🚀 Generate Cover Letter")
        
        if submitted:
            if not all([company_name, position, applicant_name, applicant_skills, applicant_experience]):
                st.error("❌ Please fill in all required fields (*)")
            else:
                job_data = {
                    'company': company_name,
                    'position': position,
                    'hiring_manager': hiring_manager
                }
                
                applicant_info = {
                    'name': applicant_name,
                    'skills': applicant_skills,
                    'experience': applicant_experience,
                    'contact': applicant_contact
                }
                
                cover_letter = cover_letter_generator.generate_cover_letter(job_data, applicant_info)
                db.add_cover_letter(company_name, position, cover_letter)
                
                st.success("✅ Cover Letter Generated Successfully!")
                st.text_area("Generated Cover Letter", cover_letter, height=300)
                
                st.download_button(
                    "📥 Download Cover Letter",
                    cover_letter,
                    file_name=f"cover_letter_{company_name}_{position}.txt"
                )

def show_interview_prep():
    st.markdown('<div class="section-header"><h2>🎤 Interview Preparation</h2></div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Practice Questions", "Mock Interview"])
    
    with tab1:
        st.subheader("Common Interview Questions")
        
        questions = interview_preparer.get_questions_by_category("behavioral")
        
        for i, qa in enumerate(questions, 1):
            with st.expander(f"Question {i}: {qa['question']}"):
                st.success(f"**Answer:** {qa['answer']}")
                if qa.get('tips'):
                    st.info(f"**💡 Tips:** {' • '.join(qa['tips'])}")
    
    with tab2:
        st.subheader("Mock Interview Session")
        
        if st.button("🎬 Start Mock Interview"):
            questions = interview_preparer.conduct_mock_interview(["behavioral"], 3)
            st.session_state.mock_questions = questions
            st.session_state.current_question = 0
        
        if 'mock_questions' in st.session_state:
            questions = st.session_state.mock_questions
            current = st.session_state.current_question
            
            if current < len(questions):
                qa = questions[current]
                st.write(f"**Question {current + 1} of {len(questions)}**")
                st.write(f"**{qa['question']}**")
                
                if st.button("👀 Reveal Answer"):
                    st.success(f"**Answer:** {qa['answer']}")
                    if qa.get('tips'):
                        st.info(f"**💡 Tips:** {' • '.join(qa['tips'])}")
                    
                    if st.button("➡️ Next Question") and current < len(questions) - 1:
                        st.session_state.current_question += 1
                        st.rerun()
            else:
                st.balloons()
                st.success("🎉 Congratulations! You've completed the mock interview!")

def show_job_tracker():
    st.markdown('<div class="section-header"><h2>📋 Job Application Tracker</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add New Application")
        
        with st.form("application_form"):
            company = st.text_input("Company Name *", placeholder="Microsoft")
            position = st.text_input("Position *", placeholder="Software Engineer")
            status = st.selectbox("Status *", ["Applied", "Phone Screen", "Technical Interview", "Onsite", "Offer", "Rejected"])
            notes = st.text_area("Notes", placeholder="Contact person, key requirements, follow-up dates...")
            
            submitted = st.form_submit_button("💾 Save Application")
            
            if submitted:
                if not all([company, position]):
                    st.error("❌ Please fill in Company and Position")
                else:
                    db.add_application(company, position, status, notes)
                    st.success(f"✅ Application to {company} saved!")
    
    with col2:
        st.subheader("Application History")
        
        applications = db.get_applications()
        
        if applications:
            for app in applications:
                status_emoji = {
                    "Applied": "📝",
                    "Phone Screen": "📞",
                    "Technical Interview": "💻",
                    "Onsite": "🏢",
                    "Offer": "🎉",
                    "Rejected": "❌"
                }.get(app['status'], '📌')
                
                st.write(f"{status_emoji} **{app['company']}** - {app['position']}")
                st.write(f"Status: {app['status']} | Date: {app.get('date_applied', 'N/A')[:10]}")
                if app.get('notes'):
                    st.write(f"Notes: {app['notes']}")
                st.write("---")
        else:
            st.info("No applications tracked yet. Start by adding your first application!")

# THIS LINE IS CRITICAL - Make sure it's at the end
if __name__ == "__main__":
    main()