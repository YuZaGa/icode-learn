
icode-learn
===============
Online learning platform developed with Django

This is a online learning platform for teaching programming to beginners by providing them a pathway so that they can learn learn in an easy way through videos at their own pace.


Current features
----------------
Linear Learning :
* Ability to create classes
* Ability to create subjects
* Ability to create lessons with video links to tutorials

Linear Learning(Asessement):
* Question order randomisation
* Storing of quiz results under each user
* Previous quiz scores can be viewed on category page
* Correct answers can be shown after each question or all at once at the end
* Logged in users can return to an incomplete quiz to finish it and non-logged in users can complete a quiz if their session persists
* The quiz can be limited to one attempt per user
* Questions can be given a category and subcategory
* Success rate for each category can be monitored on a progress page
* Explanation for each question result can be given
* Pass marks can be set
* Multiple choice question type
* True/False question type
* Essay question type
* Display an image alongside the question
* Custom message displayed for those that pass or fail a quiz
* Custom permission (view_sittings) added, allowing users with that permission to view quiz results from users
* A marking page which lists completed quizzes, can be filtered by quiz or user, and is used to mark essay questions
* After selecting a larger pool of questions, a quiz can be set to show a random subset rather than all within the pool
* Start and end times for sitting exams are recorded


Adaptive Learning : 
* Questions according to individual proficiency
* Leaderboard for comparing your progress with others
* Explanations of questions answered
* Proficiency & progress tracker for tracking your stats as you move forward



## Setup
1. Git Clone this project:
2. Create an python environment with ```python -m venv venv``` or ```virtualenv venv``` and activate it with (windows:```venv\Scripts\activate```, Mac/Linux:```source venv/bin/activate```.
3. Install required packages: ``` pip install -r requirements.txt ```
4. Run app: ``` python manage.py runserver ```



## Addition and Modification
Due credit to people who have worked on different components of the project beforehand. **Redian Marku** , **Tom Walker**
