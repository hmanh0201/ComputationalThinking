# INDIVIDUAL PROJECT PROPOSAL

- **Student Name:** Hoàng Minh Anh
- **Student ID:** 25125001
- **Base Group:** The Seven Dwarfs
- **Proposed Title:** Energy-Aware Study Planner with Dynamic Catch-Up for University Students

## 1. Problem Statement & Overview
While standard timetable schedulers focus on fitting tasks into empty time slots before a deadline, they often fail in real life because they treat all hours of the day equally and assume users never fall behind. University students frequently struggle with two practical issues: studying difficult subjects when they are mentally exhausted, and abandoning their entire schedule after missing just one or two study sessions.

This individual proposal builds upon our group's automated scheduling concept by introducing a simpler, student-focused planner that schedules study sessions based on personal energy levels and automatically recalculates the timetable when a student misses a planned task.

## 2. Meaningful Differences from the Group Proposal
Instead of replicating the group's general-purpose productivity assistant, this proposal introduces three clear distinctions:

- **Specific Target Audience:** Exclusively designed for university students managing exam revision, lectures, and coursework deadlines, rather than general daily task management.
- **Distinct Feature Set (Energy-Level Matching):** Instead of only looking at free time and deadlines, the system matches task difficulty (High, Medium, Low focus) with the student's daily energy zones (Peak, Normal, Tired hours).
- **Simplified Technical Approach (Rule-Based Catch-Up):** Focuses on a lightweight, rule-based "Catch-Up" mechanism that redistributes unfinished work across remaining free days when a student procrastinates, without requiring complex algorithms or heavy frameworks.

## 3. Core Features
1. **Task Breakdown & Difficulty Tagging:** Students input an exam or assignment, break it into smaller study blocks (e.g., 45-minute sessions), and tag the required focus level (Low, Medium, High).
2. **Energy-Aware Slot Assignment:** Users define their fixed classes and preferred peak focus hours (e.g., morning vs. late night). The planner places heavy study tasks into peak energy slots and lighter tasks (like reviewing notes or formatting) into low-energy slots.
3. **One-Click "Missed Task" Rescheduler:** If a student skips a study session, they can mark it as "Missed." The system automatically shifts and splits the missed workload into upcoming buffer slots before the deadline.

## 4. Computational Thinking Application
- **Decomposition:** Breaking down large academic goals (like final exam preparation) into smaller, manageable study sessions with clear time durations.
- **Pattern Recognition:** Identifying common student scheduling habits, such as daily high-focus time windows and typical buffer time needed before deadlines.
- **Abstraction:** Filtering out unnecessary personal details and representing each task simply by four core attributes: Duration, Deadline, Difficulty Level, and Completion Status.
- **Algorithmic Design:** Creating a straightforward step-by-step greedy sorting rule that prioritizes urgent deadlines first, then matches task difficulty to available energy slots.

## 5. Expected Outcome
A lightweight, easy-to-use prototype (CLI or simple web interface) that takes a student's weekly class schedule and task list as input, outputs a balanced daily study timetable, and demonstrates how the schedule automatically adjusts when a task is skipped.