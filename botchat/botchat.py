def welcome_message():
    print("Welcome to the College Admission Bot!")
    print("I’m here to assist you with the college admission process, college details, and more.\n")

def get_applicant_details():
    # Get user input for admission details
    name = input("YOU: What is your name? ")
    print(f"Chatbot: Great to meet you, {name}!")
    
    course = input("YOU: Which course are you applying for? (e.g., Computer Science, AI, Data Science) ").title()
    print(f"Chatbot: Awesome choice! You are applying for the {course} course.")
    
    while True:
        try:
            qualification_score = float(input("YOU: What is your qualification score (percentage)? "))
            break
        except ValueError:
            print("Chatbot: Please enter a valid score.")
    
    print(f"Chatbot: Thank you! Your qualification score has been noted as {qualification_score:.2f}%")
    
    return name, course, qualification_score

def check_eligibility(qualification_score, course):
    # Optimized eligibility criteria
    eligibility_criteria = {
        "Computer Science": 75,
        "Ai": 80,
        "Data Science": 85
    }

    if course in eligibility_criteria:
        if qualification_score >= eligibility_criteria[course]:
            return True
        else:
            return False
    else:
        print(f"Chatbot: Sorry, we do not offer the course '{course}' at the moment.")
        return False

def admission_process():
    welcome_message()
    
    name, course, qualification_score = get_applicant_details()

    # Check eligibility
    if check_eligibility(qualification_score, course):
        print(f"\nChatbot: Congratulations {name}! You are eligible for admission to the {course} course.")
    else:
        print(f"\nChatbot: Sorry {name}, you are not eligible for admission to the {course} course based on your qualification score.")
        return  # Exit if not eligible
    
    # Additional Questions
    experience = input("YOU: Do you have any previous experience in this field? (Yes/No) ").lower()
    print("Chatbot: That's fantastic!" if experience == "yes" else "Chatbot: No worries! Many students start with little to no experience.")

    other_colleges = input("YOU: Have you applied to any other colleges? (Yes/No) ").lower()
    print("Chatbot: That's good to hear!" if other_colleges == "yes" else "Chatbot: Focus on this application for now.")

    motivation = input("YOU: What motivates you to pursue this course? ")
    print(f"Chatbot: Your motivation for studying {course} is inspiring!")

    career_goals = input("YOU: What are your career goals after completing this course? ")
    print(f"Chatbot: Pursuing a career in {career_goals} is a great choice.")

    scholarship = input("YOU: Are you interested in scholarship opportunities? (Yes/No) ").lower()
    print("Chatbot: Scholarships can help reduce expenses. I can provide more info!" if scholarship == "yes" else "Chatbot: That's okay! Focus on your application.")

    questions = input("YOU: Do you have any questions about the admission process or the colleges? ")
    if questions:
        faq(questions)
    else:
        print("Chatbot: If you think of any questions later, feel free to ask.")

def faq(question):
    # Frequently Asked Questions (FAQ) dictionary
    faq_responses = {
        "top engineering colleges": """
        Chatbot: The top engineering colleges in Mumbai offering CS, IT, and AI are:
        - Indian Institute of Technology Bombay (IITB)
        - Veermata Jijabai Technological Institute (VJTI)
        - Sardar Patel Institute of Technology (SPIT)
        - K. J. Somaiya College of Engineering
        - Mukesh Patel School of Technology Management & Engineering
        """,
        "branches undergraduate studies": """
        Chatbot: Yes, Computer Science, Information Technology, and Artificial Intelligence are offered at the undergraduate level.
        IITB offers CS, VJTI offers both CS and IT, and some colleges like SPIT and K.J. Somaiya have introduced AI.
        """,
        "eligibility criteria": """
        Chatbot: The basic eligibility for CS includes passing 12th grade with Physics, Chemistry, and Mathematics as core subjects.
        You also need to qualify in entrance exams like JEE Mains or MHT-CET, depending on the college.
        """,
        "apply for cs or it at spit": """
        Chatbot: You need to apply through the official DTE (Directorate of Technical Education) portal for Maharashtra.
        Admission is based on your rank in MHT-CET or JEE Mains. Check SPIT’s website for more details.
        """,
        "cutoffs vjti": """
        Chatbot: Cutoffs for VJTI in 2023 were:
        - CS: 98 percentile in MHT-CET
        - IT: 96 percentile in MHT-CET
        - AI: Offered only in certain colleges. Check individual portals for details.
        """,
        "ai subjects": """
        Chatbot: The AI branch typically covers subjects like Machine Learning, Data Science, Artificial Neural Networks, 
        Deep Learning, and Natural Language Processing.
        """,
        "cs or it specialization": """
        Chatbot: Yes, some colleges like IITB offer specialized electives in areas like Data Science, Cybersecurity, 
        and Artificial Intelligence within the CS and IT programs.
        """,
        "ai career scope": """
        Chatbot: AI offers vast career opportunities in sectors like technology, finance, healthcare, robotics, and education. 
        Roles such as Data Scientist, AI Engineer, Machine Learning Expert, and Research Scientist are in high demand.
        """,
        "hostel facilities spit": """
        Chatbot: Yes, SPIT offers hostel facilities, but they are limited. Admission is based on merit, so apply early after receiving admission.
        """,
        "research opportunities iitb": """
        Chatbot: IIT Bombay offers excellent research facilities in AI with projects in areas like Robotics, NLP, and Autonomous Systems. 
        Students can participate in research internships and industry collaborations.
        """,
        "tuition fees kj somaiya": """
        Chatbot: The tuition fees for the CS branch in K.J. Somaiya range from ₹1.5 lakh to ₹2 lakh per annum, 
        depending on the year of admission and scholarships.
        """,
        "scholarships it or ai": """
        Chatbot: Yes, most engineering colleges in Mumbai offer merit-based and need-based scholarships. 
        Maharashtra government and private scholarships are available based on academic performance.
        """
    }

    # Provide response based on keyword matches
    for key in faq_responses:
        if key in question.lower():
            print(faq_responses[key])
            return

    print("Chatbot: I'm sorry, I don't have information on that right now. Please try asking something else.")

# Run the bot
if __name__ == "__main__":
    admission_process()
