Student Worksheet
Complete this before you write any code for your capstone project. Keep each section short —
this is a planning tool, not an essay. Commit the finished worksheet to your project's GitHub
repo (e.g. PLANNING.md) so it's part of your portfolio alongside the code. This page is fillable
directly in the browser — type in the boxes below, then print or save as PDF.

Part 1 — Business Case
Problem — What problem are you solving? (1–2 sentences, plain language)
Young bmw enthusiasts have limited access to organised and affordable
bmw driving experiences especially those who are not legally able to
drive
Who has this problem — Be specific, not "users in general"?

Young car enthusiasts or unemployed people who wants to experience
new bmw models but may not own a bmw or have a drivers license

Why now / why it matters — One sentence, the motivation not marketing copy

Young car enthusiasts need safer and easier access to bmw driving
experiance

Success looks like — One measurable-ish sentence

Users can easily find an available bmw experience, choose a car and date,
pay the booking fee and receive confirmation through the platform

Part 2 — Use Case

Primary actor(s) — Who directly uses what you're building?

Bmw enthusiasts/customers
User stories — 3–5 stories: As a [user], I want to [action], so that [benefit]
1. As a bmw enthusiast/customer i want to browse available bmw
models,so that i can choose a car iam interested in test driving

3. As a bmw customer i want to view the details of a bmw model, so that i
can decide whether i want to book a test drive

5. As a bmw customer i want to select a date and time for a test drive, so
that i can book a convenient appointment

7. A a bmw customer i want to receive a confirmation of my test drive
booking so that i know when and where my test will take place

Happy-path flow — The core feature, step by step (numbered, 5–8 steps max)

1.user visits the website

2.user chooses a bmw model

3.user selects an available date and time

4.user enters their details and books the test drive

5.user receives a booking confirmation

Part 3 — Tech Spec

Stack — Languages / framework / database, and one line on why

Django because i dont have to build account management from scratch it
makes it easier to build

Data model sketch — Key entities and their fields/relationships, a simple list is fine

Users
Bmw cars
Bookings
Events
Payments & professional drivers

Core screens / endpoints — The pages or API routes that actually exist in v1
Out of scope — What you are deliberately NOT building — this line matters more
than it looks

No payment/deposit handling
No in app messaging
No ratings or reviews

Stretch goals (optional) — Nice-to-haves if time permits

contact /FAQ section
Ratings

Worked Example — Neighbourhood

Tool-Sharing App
A filled-in example using a project similar in scope to the Module 3 Django capstone, for
instructors to walk through in class before students attempt their own.
Business Case
Problem: People in a neighbourhood often own tools (drills, ladders, lawn equipment) they use
a few times a year, while neighbours buy duplicates they rarely need.
Who has this problem: A resident on a residential street who needs a tool for a weekend
project and doesn't want to buy one for one-time use.
Why now: Community WhatsApp groups already do this informally and messages get lost — a
simple shared list solves it properly.
Success looks like: A neighbour can list a tool and another neighbour can find and request it in
under two minutes.
Use Case
Primary actors: Tool Owner, Tool Borrower (same user model, different actions).
Stories: As a Tool Owner, I want to list a tool with a photo and description, so that neighbours
know it's available. As a Borrower, I want to search tools by category, so that I can find what I
need quickly. As a Borrower, I want to request a tool, so that the Owner is notified and can
approve it. As an Owner, I want to approve or decline requests, so that I control who borrows
my tools. As a user, I want to log in securely, so that my listings and requests are tied to my
account.
Happy path: (1) User registers/logs in. (2) Owner creates a tool listing. (3) Borrower searches
and finds it. (4) Borrower submits a request. (5) Owner approves. (6) Both see the tool marked
"borrowed" until returned.
Tech Spec
Stack: Django + PostgreSQL (or SQLite for development) — chosen because the built-in auth
and admin panel remove the need to build account management from scratch.
Data model: User (Django's built-in auth). Tool — owner (FK to User), name, category,
description, photo, status (available/borrowed). Request — tool (FK), borrower (FK), status
(pending/approved/declined), requested_at.
Core screens: Home/browse listings, Tool detail page, "Add a tool" form, "My requests"
dashboard, "My tools" dashboard (approve/decline).
Out of scope: No in-app messaging (use existing contact info), no payment/deposit handling,
no rating/review system, no mobile app — web only.
Stretch goal: Email notification when a request is approved.
