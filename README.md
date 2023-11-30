Equigrade README
Overview

Equigrade is an innovative grading system designed to enhance the educational assessment process. It offers a comprehensive, flexible approach to grading, allowing for substitutions and adjustments to ensure a more representative assessment of student performance. Equigrade integrates seamlessly with educational platforms like Canvas, promoting consistent engagement and a holistic assessment approach.
Core Concepts
1. Grade Blueprint

    Purpose: Guides adjustments or substitutions in grades based on predefined rules or instructor input.
    Implementation: Involves setting up rules for how grades can be substituted or adjusted.

2. Global Settings

    Max Substitutions Allowed: Up to 15 grade substitutions.
    Grade Thresholds for Substitution: Grades eligible for substitution range between 15 and 70, adjustable by instructors.
    Penalty Types: Options include linear, percentage, tiered, and exponential.
    Penalty Amount: Default set at 10, but adjustable.

3. Assignment Guidelines

    Substitution Flexibility: Each assignment can have a substitute - another assignment or an aggregate of others.
    Aggregate Methods: Includes average, weighted average, max, min, median, and custom calculations.
    Weightings: Assignments can have weightings, particularly in aggregate calculations.

Examples of Usage

    Homework 1 substituted by the grade from Homework 8.
    Homework 2 substituted by the average grade of Homework 3 and Homework 4.
    Homework 3’s grade could be the maximum of a weighted average of Homework 5 and 8 or the grade from Homework 9.

Benefits

    Holistic Assessment: Ensures that a student's overall performance is more representative of their capabilities.
    Flexibility: Allows instructors to customize grading criteria to align with their teaching approach.
    Integration: Designed for seamless integration with Canvas.
    Consistent Engagement: Encourages students to engage with all assignments as they all contribute to the final grade.

Technical Implementation

Refer to the provided JSON structure "data.json" and guidelines in 'SETUP.MD' for implementing this program

Here is also a link to a custom trained GPT Model that is design handle any questions regarding equigrade (you might need gpt+ to access it)
https://chat.openai.com/g/g-cAuHru6MG-equigrade
