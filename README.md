# Equigrade: A more Holistic Grading System
![alt text](https://github.com/SekenderNaveed1/Equigrade/blob/main/Logo.png)
Equigrade is designed to transform educational assessment by introducing a flexible, comprehensive grading system that adapts to the nuances of student performance. Its goal is to simplify the grading process while ensuring accuracy and fairness in evaluation.

# What is Equigrade?
Equigrade is an innovative grading system designed to enhance the way educators assess student performance. At its core, Equigrade provides flexibility and accuracy in grading, allowing for the substitution and adjustment of grades based on predefined rules or instructor discretion. This system is built to reflect a student's true capabilities by considering their overall performance rather than just isolated outcomes.

# Equigrade's key features include:

Here's a more detailed, straightforward explanation of its key features:

### Grade Substitution for Improved Learning: 
Equigrade recognizes that learning is a process filled with ups and downs. To reflect a student's growth over time, if a student initially struggles with a concept but later shows improvement on a similar assignment, Equigrade allows for the replacement of the earlier lower grade with the later, higher one. This substitution acknowledges and rewards the student's progress and mastery over time, rather than penalizing them for earlier challenges.

### Comprehensive Evaluation of Student Work: 
Unlike traditional grading systems that may focus narrowly on individual assignments, Equigrade adopts a holistic view. It considers all aspects of a student's work throughout a course, ensuring that the final grade accurately represents their overall understanding and skills. This approach encourages students to consistently engage with all course material, knowing that each piece of work contributes to their final assessment.

### Flexible and Customizable Grading Options: 
Understanding that each course and instructor has unique needs, Equigrade is designed with flexibility at its core. Instructors can tailor the system's settings to align with their specific grading standards and objectives. This includes adjusting which assignments can be substituted, setting grade thresholds for substitutions, and choosing how penalties for late or missing work are applied. This adaptability makes Equigrade suitable for a wide range of subjects and instructional styles.

### Seamless Integration with Canvas: 
To ensure a smooth and hassle-free experience for both instructors and students, Equigrade is built to integrate seamlessly with Canvas, a popular Learning Management System (LMS). This integration means that users can easily navigate between Equigrade and Canvas, with grades and assignments automatically synced between the two platforms. The result is a streamlined workflow that saves time and reduces the potential for errors.


## Equigrade and the Challenge of Dropping Assignments

Equigrade's comprehensive grading approach, including its grade substitution feature, offers a novel solution to the traditional academic practice of dropping or allowing students to skip certain assignments. This section explains how traditional methods might unintentionally encourage less desirable student behaviors, such as procrastination or strategic laziness, and how Equigrade's system provides a more effective alternative.

#### Traditional Approaches to Assignments

- **Strategic Laziness**: Traditional grading systems that permit dropping the lowest scores or skipping assignments may inadvertently encourage students to selectively engage with their coursework. Knowing they can afford to skip assignments without impacting their final grade might lead some students to bypass tasks they perceive as challenging or less interesting.

- **Poor Time Management**: The option to drop assignments can serve as a safety net for poor time management, allowing students to procrastinate and then rely on the ability to exclude their poorest performances from their final grade calculation.

- **Inconsistent Engagement**: Dropping assignments can result in an uneven engagement with the course material. Students might opt to concentrate their efforts on assignments they believe will be easier for them to excel in, potentially neglecting areas of the curriculum that could offer valuable learning experiences.

#### How Equigrade Addresses These Issues

Equigrade eliminates the need for assignment dropping or skipping by:

- **Encouraging Continuous Improvement**: By allowing grades from later assignments to substitute lower grades from earlier, related assignments, Equigrade motivates students to persistently engage with all course material and strive for improvement throughout the course.

- **Fostering Consistent Engagement**: Since all assignments have the potential to contribute to the final grade, students are encouraged to consistently participate and invest effort across all tasks. This consistent engagement ensures a comprehensive understanding of the course material.

- **Rewarding Growth and Mastery**: Equigrade's focus on improvement and mastery over time shifts the emphasis from tactical avoidance of difficult assignments to continuous learning and skill development.

By addressing the pitfalls of traditional dropping or skipping policies, Equigrade promotes a more holistic and effective learning environment that encourages students to engage with the entire curriculum, manage their time wisely, and continuously strive for improvement.


# Equigrade Example Use Scenario:  Python Course

## Course Setup

In this scenario, we explore the application of Equigrade in an advanced Python programming course. This example highlights the system's ability to reflect significant improvements in student performance through its grade substitution feature.

- **Assignments**: The curriculum includes 10 challenging programming assignments that cover advanced Python topics, such as algorithms, data structures, web development, and data science.
- **Grading Policy**: The instructor enables up to 2 grade substitutions for assignments if students show marked improvement on similar or related topics later in the course.


## Student: Yoshi <img src="yoshi.png" width="40" height="50" alt="Yoshi">


- **Assignment 1**: Yoshi faces difficulties with advanced data structures, scoring 50%.
- **Assignment 8**: After diligent study and practice, Yoshi excels in a project involving complex data manipulation, scoring 95%.

## Application of Equigrade

Equigrade identifies the significant advancement in Yoshi's skills from Assignment 1 to Assignment 8, suggesting a substitution to accurately represent their learning trajectory.

### Substitution Process

1. **Identification**: Equigrade finds an opportunity for grade substitution between Assignment 1 and Assignment 8.
2. **Implementation**: Yoshi's grade for Assignment 1 is substituted with their higher grade from Assignment 8.

### Impact on Grades

Assuming Yoshi's other 8 assignments (excluding Assignments 1 and 8) average a grade of 80% for simplicity:

- **Before Substitution**: Yoshi's overall average grade is calculated with the initial low grade for Assignment 1.

```Average Grade = (50 + 80*8 + 95) / 10 = 78.5% or a letter grade of C+```
  
- **After Substitution**: The new average incorporates the higher grade from Assignment 8, replacing Assignment 1.

``` New Average Grade = (95 + 80*8 + 95) / 10 = 83.0% or a letter grade of B```

This is actually a substantial difference where the GPA goes from a 2.33 to a 3.00!



# Built With

- Python for core functionality
    <img src="python-logo.png" alt="Python logo" width="100"/>
- Integration with Canvas LMS
    <img src="Canvas_LMS_Color_RGB.png" alt="Canvas LMS logo" width="100"/>



Please check [SETUP.MD](SETUP.md) for setup instructions and follow it very carefully.




# Motivation & roadmap

Well, I guess this will probably be the most casual section of this readme, but it's for a reason. The main motivation behind this project began in the Fall of 2022 at UC Davis. I was a student assistant for Matthew Butner (co-creator) of this project. We were working on an entry-level class called [ECS 32A](https://cs.ucdavis.edu/schedules-classes/ecs-032a-introduction-programming), which is a very basic Python course for beginners.

Unfortunately, we discovered a trend that a significant portion of the class either failed or performed very poorly. So, in December 2022, Professor Butner took the initiative and organized a team to help brainstorm ideas for creating a grade-enhancement algorithm for classes that are mostly project-based, like his. I was fortunate enough to be part of that team, and we worked on and off, with hour-long brainstorming sessions for around 6 months. However, in the end, I remained on the team, and in the summer, Professor Butner and I both agreed on a concept like Equigrade. However, we had one problem: we didn't have enough people for this project. It was just me and him.

I was concurrently interning at LLNL and still am, actually. I realized that one thing I really wanted to do was project management, and I pitched the idea to him, and he gave me the green light. This was in August 2023. I decided to ask around as many people as I could, friends, classmates, etc. The response was quite nice. In the end, at the height of the project, I had around 20 people on this team. We had team members with incredibly impressive backgrounds, from interning at big tech companies and being much better at coding than me, to people who were just getting started with a CS degree. And yes, that was the point of all this. I wanted to give people something legitimate to work on for their resume, to learn, and to have others work on something fun too on the side.

I created a couple of different teams for this project. For this phase, the two primary ones that had to execute were the Development Team and the QA Team. The names and responsibilities are self-explanatory; the developers created, and QA did debugging, etc.

The development timeframe of this project took around 3 months, from August 2023 to December 2023.

The roadmap that I would love for this project is for it to be used by UC Davis faculty, especially the CS department and then other departments, while concurrently reaching other schools that use Canvas. I wholeheartedly believe that this project has the potential to make learning, to some degree, much more equitable and grades more holistic - hence the name, Equigrade.

This was the first project I ever managed, and I hope it is just the beginning of many others to follow that are much larger in scale and with larger real-world ramifications.

Thank you. :)


# Contributing

Currently this repo is private and approved users through me or Matthew Butner will be able to contribute

We welcome contributions from the community! If you have suggestions for enhancements or have identified bugs, here's how you can contribute:

1. **Fork the Repository:** Start by forking the Equigrade repository to your GitHub account.
2. **Create a Feature Branch:** Make your changes in a new branch dedicated to the feature or fix you're working on.
3. **Commit Your Changes:** Write clear, concise commit messages that describe the enhancements or fixes.
4. **Open a Pull Request:** Submit a pull request from your feature branch to Equigrade's main branch for review.
5. **Email Proposal:** For significant changes or new features, please email sekendernaveed1@gmail.com with your proposal before starting work. This allows us to discuss the enhancement and how it fits into the 


# Support
For support either email me at sekendernaveed1@gmail.com or if you have GPT + subscription use this customer [GPT](https://chat.openai.com/g/g-cAuHru6MG-equigrade) to help you.


# Contact

    Project Maintainer/Manager: Naveed Sekender - sekendernaveed1@gmail.com
    UC Davis Faculty: Matthew Butner - mfbutner@ucdavis.edu 
    Project Link: (https://github.com/SekenderNaveed1/Equigrade)

# Acknowledgments

    Special thanks to:
    Matthew Butner - UC Davis Faculty Member
    Gavin Lang  - Lead of QA team
    Amabel Gale - Lead of DEV team


# License
License ```LGPL-2.1 license```
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.



# Important Notice: Ethical Use Policy

## Strict Prohibition of Unethical Use

We, the creators of Equigrade, have developed this software with the intention of enhancing the educational experience, providing flexibility in grading, and supporting educators in accurately assessing student performance. It is built on principles of integrity, transparency, and fairness.

**We strictly prohibit any form of unethical use of Equigrade, including but not limited to:**

- **Hacking into educational systems:** Unauthorized access to, or manipulation of, educational records, grades, or systems.
- **Grade manipulation:** Using Equigrade to unfairly alter or manipulate student grades or academic records.
- **Unauthorized use:** Deploying or using Equigrade in any manner that violates educational institution policies, local laws, or regulations.

### Responsibility and Compliance

Users of Equigrade are expected to uphold the highest standards of ethical conduct and ensure compliance with all relevant institutional policies and legal regulations. It is your responsibility to use Equigrade in a manner that respects the rights and privacy of all individuals involved in the educational process.

## Reporting Unethical Use

If you are aware of any misuse of Equigrade or have concerns regarding potential ethical violations, please report them immediately to the academic affairs department
---

Your cooperation is essential in maintaining the integrity and trustworthiness of Equigrade. Together, we can ensure that Equigrade remains a tool for positive educational advancement, reflecting our shared values of honesty, fairness, and academic integrity.

