# -*- coding: utf-8 -*-
"""Anusha_Zubair.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fZt8NUVIFaC1ckBNgn076kG2z_j6f9wk
"""

# Define the questions
questions = {
    "Q1": "Can you describe the specific case study or transformation story you want to share? ",
    "Q2": "What challenge or problem was addressed in this case? ",
    "Q3": "What were the key results or outcomes achieved in this story? ",
    "Q4": "Are there any data, quotes, or testimonials that illustrate the impact? ",
    "Q5": "Is there a specific call-to-action? ",
    "Q6": "Are there any specific hashtags you’d like to include? ",
    "Q7": "Describe your desired tone and style. "
}

# Dictionary to store user's answers
answers = {}

# Ask questions and get user input
for key, question in questions.items():
    user_input = input(question)
    answers[key] = user_input

# Extract relevant information
case_study = answers["Q1"]
challenge_addressed = answers["Q2"]
key_results = answers["Q3"]
data_or_quotes = answers["Q4"]
call_to_action = answers["Q5"]
hashtags = answers["Q6"]
desired_tone_style = answers["Q7"]

# Print the extracted information for verification
print("\nExtracted Information:")
print("Case Study:", case_study)
print("Challenge Addressed:", challenge_addressed)
print("Key Results:", key_results)
print("Data or Quotes:", data_or_quotes)
print("Call to Action:", call_to_action)
print("Hashtags:", hashtags)
print("Desired Tone and Style:", desired_tone_style)

# Generate the prompt for LangChain based on user input
prompt_template = (

    "Create a social media post that effectivelu communicates a transformatiev story.Use the following structure:\n\n"
    "1.  Start with an engaging fact to grab attention. Example: 'Did you know? {data_or_quotes}'\n\n"
    "2.  Elobrate on the case study {case_study} and briefly address the  {challenge_addressed}  Start of with an adjective .'\n\n"
    '''3.  Highlight the outcomes achieved with bullet points, ensuring each point begins with a different yet relevent  emoji for visual emphasis. {key_results}

     Example
    - 🚀 [Result1]
    - 🌎 [Result2]
    - 🌟 [Result3]
    - 🧠 [Result4]
    - ✅ [Result5]
    '''

    "4. Conclude with a persuasive call to action that encourages engagement. Example: {call_to_action} .End with the specified hashtags and a link for more information. Example: {hashtags} '\n\n"
    "5. Please maintain a {desired_tone_style} tone throughout the post\n"
    "6. Do not add useless emoji except as explained in point 3 and do not highlight anything except the text from point 1"
    "7. Do not add extra description that is not given by the user and make the output brief"

    # f'''You are a social media expert and you have to design social media post for the user. Before making it you have to ask following questions from the user,
    #   "Q1": "Can you describe the specific case study or transformation story you want to share? ",
    #   "Q2": "What challenge or problem was addressed in this case? ",
    #   "Q3": "What were the key results or outcomes achieved in this story? ",
    #   "Q4": "Are there any data, quotes, or testimonials that illustrate the impact? ",
    #   "Q5": "Is there a specific call-to-action? ",
    #   "Q6": "Are there any specific hashtags you’d like to include? ",
    #   "Q7": "Describe your desired tone and style. "

    #   Following are the answers from the users to the questions above respectively:
    #  {case_study}, {challenge_addressed}, {key_results}, {data_or_quotes} ,{call_to_action}, {hashtags} , {desired_tone_style}
    #   The post design should be similar to this :
    #   1.  Start with an engaging fact to grab attention. Example: 'Did you know?
    #   2.  Elobrate on the case study  and briefly address the   Start of with an adjective .
    #   3.  Highlight the outcomes achieved with bullet points, ensuring each point begins with a different yet relevent  emoji for visual emphasis.
    #   4.  Conclude with a persuasive call to action that encourages engagement .End with the specified hashtags and a link for more information.
    #   5.  Please maintain a tone throughout the post
    #   Do not add any emoji except as explained in point 3 above and do not add titles and do not highlight  anything by bolding it
    #   Suggested post :

    # '''

)

# Prepare the prompt using the extracted information
prompt = prompt_template.format(
    data_or_quotes=answers["Q4"],
    challenge_addressed=answers["Q2"],
    case_study=answers["Q1"],
    key_results=answers["Q3"],
    call_to_action=answers["Q5"],
    hashtags=answers["Q6"] + "\n" ,
    desired_tone_style=answers["Q7"]
)

# Print the generated prompt for verification
print("Generated Prompt for LangChain:\n")
print(prompt)

!pip install langchain
!pip install langchain-cli
!pip install openai
from langchain.llms import OpenAI
import openai

# pip install openai --upgrade

import openai

from openai import OpenAI


client = OpenAI(api_key="add you api key here ")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": prompt
    }
  ],
  temperature=0.2,
  max_tokens=220,
)

# Extract the generated text from the response

print(response.choices[0].message.content)

# print(response.choices[0].message.content)



"""## **TASK 2**"""

# Input for Student 1
name = input("Enter your name  ")
field_of_study = input("Enter your field of study  ")
year_of_study= input("Enter your year of study  ")
subjects = input("Enter the list of subjects (comma-separated): ").split(',')
preferred_learning_style= input("Enter your preferred learning style  (visual, auditory, kinesthetic): ")
personal_objectives = input("Enter your personal objectives (such as preparing for a specific exam or overcoming a learning difficulty).  ")
challenges = input("Enter the challenges faced by you ")
extracurricular_activities = input("Enter your extracurricular activities  ")

# Example input for Student 1
name = "Alice"
field_of_study = "Biology"
year_of_study = "Second year"
subjects = ["Genetics", "Microbiology", "Biochemistry"]
preferred_learning_style = "visual"
personal_objectives = "preparing for the MCAT"
challenges = "time management"
extracurricular_activities = ["debate club", "volunteer at local clinic"]
academic_performance = ["B", "A-", "B+"]


# Function to generate study plan
def generate_study_plan(name, field_of_study, year_of_study, subjects, preferred_learning_style, personal_objectives, challenges, extracurricular_activities , academic_performance):
    # prompt = f"""
    # Create a personalized study plan for {name}, a {year_of_study} student in {field_of_study}. {name}'s study plan should cater to the following details:

    # Subjects: {subjects}
    # Preferred Learning Style: {preferred_learning_style}
    # Personal Objectives: {personal_objectives}
    # Challenges: {challenges}
    # Extracurricular Activities: {extracurricular_activities}

    # The study plan should:
    # 1. Outline a weekly study schedule, allocating time for each subject based on its importance and {name}'s performance levels. Prioritize subjects where improvement is needed the most.
    # 2. Suggest study methods and resources that align with {name}'s preferred learning style. For example, recommend visual aids for a visual learner, podcasts or audiobooks for an auditory learner, and hands-on experiments or activities for a kinesthetic learner.
    # 3. Include strategies for achieving {name}'s personal objectives, whether they involve preparing for a specific exam or overcoming a learning difficulty.
    # 4. Provide tips on balancing academics with extracurricular activities, ensuring there's time for rest and hobbies.
    # 5. Address {name}'s challenges with specific advice, tools, or techniques to overcome them.

    # Ensure the plan is realistic, flexible, and supportive of {name}'s overall well-being and academic goals.
    # """

    # prompt = f"""
    # Create a comprehensive and personalized study plan for {name}, who is in their {year_of_study} of studying {field_of_study}. This study plan should be meticulously tailored to {name}'s specific academic and personal needs, taking into account the following:

    # Subjects and Academic Performance: {', '.join([f'{subject} (current performance: {performance})' for subject, performance in zip(subjects, academic_performance)])}
    # Preferred Learning Style: {preferred_learning_style}
    # Personal Objectives: {personal_objectives}
    # Challenges: {challenges}
    # Extracurricular Activities: {', '.join(extracurricular_activities)}

    # Given these details, the study plan must:

    # 1. Assess {name}'s current academic performance in each subject, identifying areas that require more focus and suggesting targeted strategies for improvement.
    # 2. Incorporate {name}'s preferred learning style into the study methods for each subject, offering specific tools and resources that align with visual, auditory, or kinesthetic learning preferences.
    # 3. Develop a strategy that supports {name}'s personal objectives, such as preparing for a specific exam or overcoming a particular learning difficulty, with actionable steps and milestones.
    # 4. Propose a balanced weekly schedule that dedicates appropriate time to study, extracurricular activities, and personal well-being, ensuring there is ample time for rest and hobbies.
    # 5. Offer advice on managing {name}'s challenges, especially around time management, providing practical tips on organization, prioritization, and effective study techniques.
    # 6. Suggest ways to integrate study sessions with {name}'s extracurricular activities where possible, enhancing learning through diverse experiences.

    # This plan should be realistic, adaptable, and aimed at fostering a holistic approach to {name}'s education and personal development. It should encourage academic success while also supporting {name}'s well-being and engagement in extracurricular pursuits.
    # """


    prompt = f"""
    Create a comprehensive and personalized study plan for {name}, a {year_of_study} student specializing in {field_of_study}. This plan should meticulously integrate academic subjects, preferred learning styles, personal objectives, challenges, and extracurricular activities. The goal is to support {name}'s academic success, personal growth, and well-being.

    Detailed Information:
    - Academic Subjects: {', '.join(subjects)}
    - Preferred Learning Style: {preferred_learning_style}
    - Personal Objectives: {personal_objectives}
    - Challenges: {challenges}
    - Extracurricular Activities: {', '.join(extracurricular_activities)}

    Requirements for the Study Plan:
    1. Develop a detailed weekly timetable that allocates time for studying each subject, taking into consideration {name}'s preferred learning style and performance levels. Ensure a balanced distribution of subjects, with emphasis on those needing improvement.
    2. Incorporate {name}'s extracurricular activities into the timetable, ensuring there is harmony between academic responsibilities and personal interests.
    3. Propose strategies and resources tailored to {name}'s learning style for effective study sessions. Include recommendations for tools or apps that could assist in overcoming {name}'s challenges.
    4. Offer advice on achieving {name}'s personal objectives while managing academic workload and extracurricular commitments. Suggest methods for time management and stress reduction.
    5. Address the challenges faced by {name}, providing actionable solutions and adjustments to the study routine that can aid in overcoming these difficulties.

    The timetable should:
    - Clearly outline specific times for study sessions, breaks, extracurricular activities, and personal time.
    - Include morning, afternoon, and evening activities, ensuring there is adequate time for rest and leisure to maintain a healthy work-life balance.
    - Suggest time blocks for focused study periods, using techniques such as the Pomodoro method or similar, to enhance productivity and prevent burnout.

    Aim for a plan that is realistic, adaptable to unexpected changes, and supportive of {name}'s academic goals, personal development, and overall health.
    """
    return prompt

client = OpenAI(api_key="add you api key here ")

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "user",
      "content": generate_study_plan(name, field_of_study, year_of_study, subjects, preferred_learning_style, personal_objectives, challenges, extracurricular_activities, academic_performance)
    }
  ],
  temperature=0.7,
  max_tokens=1500,
  top_p=1
)

# Extract the generated text from the response

print(response.choices[0].message.content)