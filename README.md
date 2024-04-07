# Equigrade: Targeted Grading Adjustments

![alt text](https://github.com/SekenderNaveed1/Equigrade/blob/main/Logos/Logo.png)

Equigrade introduces a targeted approach to grading, designed to handle outliers such as missing assignments or instances of low performance that might not accurately reflect a student's current understanding. Its aim is to streamline specific aspects of the grading process, particularly focusing on improving fairness by addressing outliers.

# What is Equigrade?

Equigrade provides tools to assist educators in adjusting grades for specific scenarios, offering a straightforward solution for managing performance outliers. Equigrade focuses on specific grading adjustments, enabling instructors to substitute or adjust grades under certain conditions, thereby addressing discrepancies in student performance.

# Key Features of Equigrade:

- **Grade Adjustment for Fair Evaluation**: Equigrade enables educators to replace a lower grade with a more recent, higher one on a similar assignment, recognizing and encouraging improvement over time.

- **Targeted Adjustments for Fairer Outcomes**: Equigrade allows for specific grading adjustments, offering a solution to manage cases where a single assignment may not reflect a student's overall progress or capabilities.

- **Customizable Settings for Educators**: Equigrade offers the flexibility to adjust which assignments can be substituted, set thresholds for substitutions, and manage how exceptions are handled, tailoring the system to various instructional needs.

- **Easy Integration with Canvas**: For convenience, Equigrade is designed to integrate with the Canvas Learning Management System (LMS), ensuring seamless operation between systems.

## Addressing the Issue of Inconsistent Engagement

Equigrade provides an alternative to the traditional method of dropping the lowest scores, encouraging consistent effort and engagement by recognizing and rewarding improvement and mastery over time.


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

- **Assignments**: The curriculum includes 4 entry level programming assignments that cover advanced Python topics
- **Grading Policy**: The instructor enables up to 2 grade substitutions for assignments if students show marked improvement on similar or related topics later in the course.


## Example Use Scenario: Understanding Equigrade Through Student Performance

This scenario demonstrates Equigrade's impact on student grades across a series of related assignments. Below is a table showing grades for three students - Yoshi, Birdo, and Toad - on four assignments. Following the table, we explore the topical overlaps between these assignments.

| Student   | Assignment 1 | Assignment 2 | Assignment 3 | Assignment 4 |
|-----------|--------------|--------------|--------------|--------------|
| Yoshi <img src="Logos/yoshi.png" width="50" height="60">     | 40%          | 85%          | 95%          | 50%          |
| Princess Peach <img src="Logos/Princess_Peach_Stock_Art.png" width="50" height="70">     | 60%          | 92%          | 87%          | 40%          |
| Birdo <img src="Logos/Birdo-MP9.png" width="50" height="60">| 50%          | 78%          | 88%          | 30%          |

The Students original grades will be (all the assignments have the same weight):<br>
Yoshi - `(40+85+95+50)/4 = 67.5` <br>
Princess Peach - `(60+92+87+40)/4 = 69.75` <br>
Birdo - `(50+78+88+30)/4 = 61.5` <br>

Everyone bascially failed!<br>
<img src="Logos/yoshi-mario-strikers.gif">

## Assignment Topics and Overlap

The assignments cover related areas of the course material, ensuring that students have multiple opportunities to demonstrate their understanding and improvement over time:<br>

- **Assignment 1**: arithmetic operations
- **Assignment 2**: loops
- **Assignment 3**: functions
- **Assignment 4**: Classes


Here's a Venn Diagram representing the overlap between these topics:

![Venn Diagram of Assignment Topics](Logos/VennDiagram.png)

This visual representation highlights how assignments are designed to interconnect, allowing Equigrade to effectively assist intructors identify opportunities for grade substitution based on topic relevance and student improvement.


## Json file example
So at the heart of each equigrade program is a JSON file in which each program is based off (all of this is very user modifiable) 

```json
{
  "environment": {
    "setting1": null,
    "setting2": null

  },
  "max_subsitions": "2"
  "homework_list": [
    {
      "Name": "Homework 1",
      "Substitute Method": "Weighted Average",
      "Substitute Assignment": "Homework 2"
    },
    {
      "Name": "Homework 2",
      "Substitute Method": "Weighted Average",
      "Substitute Assignment": "Homework 3"
    },
    {
      "Name": "Homework 3",
      "Substitute Method": "Max Score",
      "Substitute Assignment": "Homework 4" 
    },
    {
      "Name": "Homework 4",
      "Substitute Method": "Average",
      "Substitute Assignment": "Homework 1, Homework 2, Homework 3"
    }
  ]
}
```
## Original Grades with lowest dropped

### Graph with lowest grade dropped
| Student   | Assignment 1 | Assignment 2 | Assignment 3 | Assignment 4 |
|-----------|--------------|--------------|--------------|--------------|
| Yoshi <img src="Logos/yoshi.png" width="50" height="60">     | ~40%~          | 85%          | 95%          | 50%          |
| Princess Peach <img src="Logos/Princess_Peach_Stock_Art.png" width="50" height="70">     | 60%          | 92%          | 87%          | ~40%~          |
| Birdo <img src="Logos/Birdo-MP9.png" width="50" height="60">| 50%          | 78%          | ~30%~          | 88%          |


For yoshi his lowest score was 40% at assignment 1<br>
For Princess Peach his lowest score was 40% at assignment 4<br>
for Birdo her lowest score was 30% at assignment 3<br>

After dropping all those grades we get:

So Yoshi's total grade would be: `(85+95+50)/300` = 76.66% <br>
So Princess Peach's total grade would be: `(60+92+87)/300` = 79.6 <br>
So Birdo's total grade would be: `(50+78+88)/300` = 72% <br>


## Adjusted Grades with Equigrade 

#### Before
| Student   | Assignment 1 | Assignment 2 | Assignment 3 | Assignment 4 |
|-----------|--------------|--------------|--------------|--------------|
| Yoshi <img src="Logos/yoshi.png" width="50" height="60">     | 40%          | 85%          | 95%          | 50%          |
| Princess Peach <img src="Logos/Princess_Peach_Stock_Art.png" width="50" height="70">     | 60%          | 92%          | 87%          | 40%          |
| Birdo <img src="Logos/Birdo-MP9.png" width="50" height="60">| 50%          | 78%          | 30%          | 88%          |



After applying Equigrade's substitution logic, where Assignment 1 grades are adjusted based on subsequent performances and the interconnectedness of topics, the grades are as follows (we have 2 substitutions possible): <br>

Yoshi: Assignments 1 and 4 will be patched up.<br>
Assignment 1 is 40 percent and its replacement function is a weighted average with HW 2. So, `(40+85)/2 = 62.5`.<br>
Assignment 4's average of HW1, HW2, HW3 and its replacement function will be `(40+85+95)/3 = 73.33`.<br>

Princess Peach: Assignments 1 and 4 will be patched up.<br>
Assignment 1 is 60 percent and its replacement function is a weighted average with HW 2. So, `(60+92)/2 = 76`.<br>
Assignment 4's average of HW1, HW2, HW3, and its replacement function will be `(60+92+87)/3 = 79.66`.<br>

Birdo: Assignments 1 and 4 will be patched up.<br>
Assignment 1 is 60 percent and its replacement function is a weighted average with HW 2. So, `(50+78)/2 = 64`.<br>
Assignment 3 is substituted by the grade of Assignment 4, which is 88.<br>

#### After
| Student   | Assignment 1 | Assignment 2 | Assignment 3 | Assignment 4 |
|-----------|--------------|--------------|--------------|--------------|
| Yoshi <img src="Logos/yoshi.png" width="50" height="60">     | 62.5%          | 85%          | 95%          | 73.33%          |
| Princess Peach <img src="Logos/Princess_Peach_Stock_Art.png" width="50" height="70">     | 76%          | 92%          | 87%          | 79.66%          |
| Birdo <img src="Logos/Birdo-MP9.png" width="50" height="60">| 64%          | 78%          | 88%          | 88%          |

Grades will be:<br>
Yoshi `(62.5+85+95+73.33)/4 = 78.9%` <br>
Princess Peach `(76+92+87+79.66)/4 = 83.6%` <br>
Birdo `(64+78+88+88)/4 = 79.5%` <br>

Grades are much more improved now and accurately represent a student's progress.<br>
<img src="Logos/yoshi-be-drippy-smw-yoshi.gif">

## Conclusion

Equigrade's unique approach to grade adjustments reflects a more nuanced understanding of student performance, leveraging topic overlap and improvement trends to ensure grades more accurately represent student learning and progression. This flexibility allows instructors to tailor grading to encourage continuous engagement and improvement, aligning with Equigrade's goals of holistic assessment and integration with educational platforms like Canvas.



# Built With

- Python for core functionality
    <img src ="Logos/python-logo.png" width="100"/>
- Integration with Canvas LMS
    <img src ="Logos/Canvas_LMS_Color_RGB.png" width="100"/>



Please check [SETUP.MD](Documentation/SETUP.md) for setup instructions and follow it very carefully.



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

If you are aware of any misuse of Equigrade or have concerns regarding potential ethical violations, please report them immediately to the academic affairs department of your institution
---

Your cooperation is essential in maintaining the integrity and trustworthiness of Equigrade. Together, we can ensure that Equigrade remains a tool for positive educational advancement, reflecting our shared values of honesty, fairness, and academic integrity.

