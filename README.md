# Student-Lab-Assigment


A application that manages lab assignments for students at a given discipline. The application
will stores:

Student: studentID, name, group.
Assignment: assignmentID, description, deadline, grade.
Grade: assignmentID, studentID, grade

The application that allows to:
1. Manage the list of students and available assignments. The application must allow the user to
add, remove, update, and list both students and assignments.

2. Give assignments to a student or a group of students (unless already given). In case an
assignment is given to a group of students, every student in the group will receive it. In case
there exist students who were previously given that assignment, it will not be assigned again.

3. Grade student for a given assignment. When grading, the program must allow the user to select
the assignment that is graded, from the student’s list of ungraded assignments. A student’s
grade for a given assignment cannot be changed. Deleting a student also removes their
assignments. Deleting an assignment also removes all grades at that assignment.

4. Create statistics:
o All students who received a given assignment, ordered alphabetically or by average
grade for that assignment.
o All students who are late in handing in at least one assignment. These are all the
students who have an ungraded assignment for which the deadline has passed.
o Students with the best school situation, sorted in descending order of the average grade
received for all assignments.
o All assignments for which there is at least one grade, sorted in descending order of the
average grade received by all students who received that assignment.

5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation that
modified the data structure

More details at : http://www.cs.ubbcluj.ro/~arthur/Fundamentals%20of%20Programming/Laboratory/Laboratory.05-07.pdf
