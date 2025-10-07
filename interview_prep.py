import streamlit as st
import random

class InterviewPreparer:
    def __init__(self):
        self.questions_db = {
            "technical": {
                "python": [
                    {
                        "question": "What are Python decorators and how do you use them?",
                        "answer": "Decorators are functions that modify the behavior of other functions. They allow you to wrap another function to extend its behavior without permanently modifying it. Use cases include logging, timing, access control, and more.",
                        "category": "Intermediate",
                        "tips": ["Explain the @ syntax", "Mention common decorators like @staticmethod", "Give a practical example"]
                    },
                    {
                        "question": "Explain the difference between lists and tuples in Python",
                        "answer": "Lists are mutable (can be modified after creation) while tuples are immutable. Lists use [] and tuples use (). Tuples are generally faster and can be used as dictionary keys.",
                        "category": "Basic",
                        "tips": ["Highlight mutability difference", "Mention performance implications", "Discuss use cases for each"]
                    },
                    {
                        "question": "What are Python generators and when would you use them?",
                        "answer": "Generators are functions that return an iterator. They use 'yield' instead of 'return' and maintain state between calls. Use them for memory-efficient processing of large datasets or infinite sequences.",
                        "category": "Intermediate",
                        "tips": ["Explain lazy evaluation", "Compare with list comprehensions", "Mention memory efficiency"]
                    }
                ],
                "javascript": [
                    {
                        "question": "What is the difference between let, const, and var?",
                        "answer": "var is function-scoped and can be redeclared. let and const are block-scoped. let can be reassigned but not redeclared in the same scope, while const cannot be reassigned.",
                        "category": "Basic",
                        "tips": ["Explain scoping differences", "Discuss hoisting behavior", "Recommend using const by default"]
                    },
                    {
                        "question": "What are JavaScript promises and how do they work?",
                        "answer": "Promises represent the eventual completion (or failure) of an asynchronous operation. They have three states: pending, fulfilled, and rejected. Use .then() for success and .catch() for errors.",
                        "category": "Intermediate",
                        "tips": ["Compare with callbacks", "Explain promise chaining", "Mention async/await syntax"]
                    }
                ],
                "sql": [
                    {
                        "question": "What is the difference between INNER JOIN and LEFT JOIN?",
                        "answer": "INNER JOIN returns only matching rows from both tables. LEFT JOIN returns all rows from the left table and matching rows from the right table (with NULLs for non-matching).",
                        "category": "Intermediate",
                        "tips": ["Use Venn diagram analogy", "Provide example scenarios", "Explain when to use each"]
                    },
                    {
                        "question": "What are SQL indexes and why are they important?",
                        "answer": "Indexes are special lookup tables that help speed up data retrieval. They work like a book index, allowing the database to find data without scanning the entire table.",
                        "category": "Intermediate",
                        "tips": ["Explain performance benefits", "Mention trade-offs (storage, write speed)", "Discuss when to index"]
                    }
                ]
            },
            "behavioral": [
                {
                    "question": "Tell me about yourself",
                    "answer": "Structure your answer: 1) Current role/background, 2) Key accomplishments, 3) Why you're interested in this role, 4) What you can bring to the company. Keep it 2-3 minutes max.",
                    "category": "Introduction",
                    "tips": ["Be concise and relevant", "Tailor to the company", "End with why you're excited"]
                },
                {
                    "question": "What is your greatest weakness?",
                    "answer": "Choose a real but manageable weakness. Show self-awareness and explain steps you're taking to improve. Example: 'I used to struggle with delegation, but now I use project management tools and regular check-ins.'",
                    "category": "Self-assessment",
                    "tips": ["Be authentic but strategic", "Show growth mindset", "Don't mention critical job-related weaknesses"]
                },
                {
                    "question": "Describe a challenging project and how you handled it",
                    "answer": "Use STAR method: Situation, Task, Action, Result. Be specific about the challenge, your role, actions taken, and measurable outcomes.",
                    "category": "Experience",
                    "tips": ["Use specific metrics", "Highlight problem-solving", "Show collaboration if applicable"]
                },
                {
                    "question": "Where do you see yourself in 5 years?",
                    "answer": "Focus on skills you want to develop and how they align with the company's growth. Show ambition but also realistic career progression within the organization.",
                    "category": "Career Goals",
                    "tips": ["Align with company goals", "Show continuous learning", "Be realistic and specific"]
                },
                {
                    "question": "Why do you want to work for our company?",
                    "answer": "Research the company and mention specific things that appeal to you: their mission, products, culture, or recent achievements. Show genuine interest and alignment with your values.",
                    "category": "Motivation",
                    "tips": ["Do your research", "Be specific and genuine", "Connect to your career goals"]
                }
            ],
            "system_design": [
                {
                    "question": "How would you design Twitter?",
                    "answer": "Discuss: 1) Requirements gathering, 2) High-level architecture (load balancers, app servers, databases), 3) Database design (users, tweets, followers), 4) API design, 5) Scaling considerations, 6) Caching strategy.",
                    "category": "Advanced",
                    "tips": ["Start with requirements", "Draw diagrams mentally", "Consider trade-offs", "Discuss scalability from day 1"]
                },
                {
                    "question": "How would you design Uber?",
                    "answer": "Cover: 1) Core components (rider app, driver app, dispatch system), 2) Real-time location tracking, 3) Matching algorithm, 4) Payment processing, 5) Scaling for peak loads, 6) Database design for locations and trips.",
                    "category": "Advanced",
                    "tips": ["Focus on real-time aspects", "Discuss geospatial data", "Consider reliability and safety"]
                }
            ]
        }
    
    def get_questions_by_category(self, category, subcategory=None):
        """Get questions by category"""
        if category == "technical" and subcategory:
            return self.questions_db.get("technical", {}).get(subcategory, [])
        elif category in self.questions_db:
            return self.questions_db[category]
        return []
    
    def get_random_question(self, category=None):
        """Get a random question from specified category"""
        if category and category in self.questions_db:
            if category == "technical":
                # Get random subcategory, then random question
                subcategories = list(self.questions_db["technical"].keys())
                random_subcat = random.choice(subcategories)
                questions = self.questions_db["technical"][random_subcat]
            else:
                questions = self.questions_db[category]
        else:
            # Get from all categories
            all_questions = []
            for cat in self.questions_db.values():
                if isinstance(cat, list):
                    all_questions.extend(cat)
                else:
                    for subcat_questions in cat.values():
                        all_questions.extend(subcat_questions)
            questions = all_questions
        
        return random.choice(questions) if questions else None
    
    def conduct_mock_interview(self, categories, num_questions=5):
        """Generate a mock interview session"""
        questions = []
        for category in categories:
            if category == "technical":
                # Include 2-3 technical questions from different subcategories
                tech_questions = []
                for subcat_questions in self.questions_db["technical"].values():
                    tech_questions.extend(random.sample(subcat_questions, min(1, len(subcat_questions))))
                questions.extend(random.sample(tech_questions, min(2, len(tech_questions))))
            else:
                cat_questions = self.questions_db.get(category, [])
                questions.extend(random.sample(cat_questions, min(2, len(cat_questions))))
        
        # Ensure we have exactly num_questions
        return random.sample(questions, min(num_questions, len(questions)))
    
    def get_interview_tips(self):
        """General interview tips"""
        return [
            "Research the company thoroughly - mission, products, recent news",
            "Prepare 2-3 questions to ask the interviewer",
            "Practice your answers but don't memorize them word-for-word",
            "Use the STAR method for behavioral questions",
            "Dress professionally, even for virtual interviews",
            "Test your technology before virtual interviews",
            "Have a copy of your resume and notes handy",
            "Send a thank-you email within 24 hours",
            "Arrive 10-15 minutes early for in-person interviews",
            "Maintain good eye contact and positive body language"
        ]

# Create the instance with the EXACT name used in import
interview_preparer = InterviewPreparer()