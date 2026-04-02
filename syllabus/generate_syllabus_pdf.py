from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = "/Users/aek72/STA 240/STA 240 Website/syllabus/STA240_Syllabus.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=1*inch, rightMargin=1*inch,
    topMargin=1*inch, bottomMargin=1*inch
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CourseTitle', parent=styles['Title'],
    fontSize=22, spaceAfter=6, textColor=colors.HexColor('#003366')
)
subtitle_style = ParagraphStyle(
    'Subtitle', parent=styles['Normal'],
    fontSize=11, spaceAfter=16, textColor=colors.HexColor('#555555'),
    alignment=TA_CENTER
)
h1_style = ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontSize=14, spaceBefore=18, spaceAfter=6,
    textColor=colors.HexColor('#003366'),
    borderPad=0
)
h2_style = ParagraphStyle(
    'H2', parent=styles['Heading2'],
    fontSize=12, spaceBefore=12, spaceAfter=4,
    textColor=colors.HexColor('#005599')
)
body_style = ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=6
)
bullet_style = ParagraphStyle(
    'Bullet', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=4,
    leftIndent=18, firstLineIndent=-12
)
callout_note_style = ParagraphStyle(
    'CalloutNote', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=4,
    leftIndent=12, rightIndent=12,
    backColor=colors.HexColor('#E8F4FD'),
    borderPad=6
)
callout_warn_style = ParagraphStyle(
    'CalloutWarn', parent=styles['Normal'],
    fontSize=10, leading=14, spaceAfter=4,
    leftIndent=12, rightIndent=12,
    backColor=colors.HexColor('#FFF3CD'),
    borderPad=6
)

def note_box(label, text, warn=False):
    bg = colors.HexColor('#E8F4FD') if not warn else colors.HexColor('#FFF3CD')
    border = colors.HexColor('#0077BB') if not warn else colors.HexColor('#BB7700')
    label_color = border
    content = []
    if label:
        content.append(Paragraph(f"<b>{label}</b>", ParagraphStyle(
            'NoteLabel', parent=body_style, textColor=label_color, spaceAfter=2
        )))
    content.append(Paragraph(text, body_style))
    tbl = Table([[content]], colWidths=[6.5*inch])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('BOX', (0,0), (-1,-1), 1, border),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return tbl

def section_rule():
    return HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#003366'), spaceAfter=4, spaceBefore=4)

story = []

# ── COVER ──────────────────────────────────────────────────────────────────
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("STA 240: Probability and Statistics", title_style))
story.append(Paragraph("Spring 2026 &nbsp;·&nbsp; Duke University", subtitle_style))
story.append(section_rule())
story.append(Spacer(1, 0.15*inch))

# ── 1. COURSE OVERVIEW ─────────────────────────────────────────────────────
story.append(Paragraph("Course Overview", h1_style))
story.append(section_rule())

story.append(Paragraph("<b>Description</b>", h2_style))
story.append(Paragraph(
    "This is a course on the mathematics of probability and statistics. In <b>probability</b>, "
    "we describe the distribution of a random phenomenon and then study how the realizations of "
    "that phenomenon typically behave. In <b>statistics</b>, we do the reverse; we observe "
    "realizations of a random phenomenon with <i>unknown</i> distribution, and then use the data "
    "to figure out what the distribution is. We will spend twelve weeks on the first, and then "
    "three weeks on the second. Topics include set theory, probability spaces, counting methods, "
    "conditional probability, discrete and (absolutely) continuous random variables, "
    "transformations of random variables, (pseudo)random number generation, bivariate "
    "distributions, concentration inequalities, limit theorems, maximum likelihood estimation, "
    "and Bayesian inference with conjugate priors.",
    body_style
))
story.append(Paragraph("Aside from the concrete topics, the course emphasizes four generic intellectual themes:", body_style))
story.append(Paragraph(
    "• Students in this class will improve their mathematical maturity. They will deepen their "
    "experience with all of the main ideas and techniques of univariate calculus, encounter topics "
    "like set theory and combinatorics, and get a taste of rigorous mathematical proof.",
    bullet_style
))
story.append(Paragraph(
    "• Probability and statistics weasel their way into pretty much everything these days, and "
    "students will study a wide variety of famous and obscure applications coming from the natural "
    "and social sciences, technology and industry, and even arts and culture.",
    bullet_style
))
story.append(Paragraph(
    "• Probability and statistics are often counterintuitive, and humans frequently make silly and "
    "harmful mistakes in reasoning. Students will use their mathematical knowledge to identify and "
    "critique these errors—and hopefully avoid them themselves.",
    bullet_style
))
story.append(Paragraph(
    "• This is a course about doing the math, but in the modern era, this has a symbiotic "
    "relationship with computer simulation. Students will learn the basics of the R programming "
    "language and use it to simulate probabilistic environments and reinforce their mathematical "
    "reasoning.",
    bullet_style
))
story.append(Paragraph("<b>Prerequisites:</b> single-variable calculus.", body_style))

story.append(Paragraph("<b>Meetings</b>", h2_style))
meetings_data = [
    ["Meeting", "Location", "Time", "Staff"],
    ["Lectures", "Old Chem 116", "Mo/We 10:05 – 11:20 AM", "Anya"],
    ["Lab 01", "Old Chem 201", "Th 1:25 – 2:40 PM", "Gwen"],
    ["Lab 02", "Social Sciences 105", "Th 3:05 – 4:20 PM", "Federico"],
]
meetings_tbl = Table(meetings_data, colWidths=[1.2*inch, 1.8*inch, 2.3*inch, 1.2*inch])
meetings_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F2F2F2')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(meetings_tbl)
story.append(Spacer(1, 0.1*inch))

# ── 2. TEACHING TEAM ───────────────────────────────────────────────────────
story.append(Paragraph("Teaching Team", h1_style))
story.append(section_rule())

team_data = [
    ["Name", "Role", "Office Hours"],
    ["Anya Katsevich", "Instructor", "Mon, Wed 3:00 – 4:00 PM\nOld Chem 216\nanya.katsevich@duke.edu"],
    ["Gwen Jacobson", "Head TA", "Fri 1:00 – 2:00 PM, 5:00 – 6:00 PM\nOld Chem 203B"],
    ["Federico Lazzarini", "TA", "Tue, Thu 5:00 – 6:00 PM\nOld Chem 203B"],
]
team_tbl = Table(team_data, colWidths=[2*inch, 1.5*inch, 3*inch])
team_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F2F2F2')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
]))
story.append(team_tbl)
story.append(Spacer(1, 0.1*inch))

# ── 3. COURSE MATERIALS ────────────────────────────────────────────────────
story.append(Paragraph("Course Materials", h1_style))
story.append(section_rule())

story.append(Paragraph("<b>Textbooks</b>", h2_style))
story.append(Paragraph(
    "You are not required to purchase a textbook for this class. However, if you wish to follow "
    "along with one, these are all good options:", body_style
))
for book in [
    "[Ross] <i>A First Course in Probability</i> by Sheldon Ross",
    "[HTZ] <i>Probability and Statistical Inference</i> by Robert Hogg, Elliot Tanis, and Dale Zimmerman",
    "[DS] <i>Probability and Statistics</i> by Morris DeGroot and Mark Schervish",
    "[Wass] <i>All of Statistics</i> by Larry Wasserman",
]:
    story.append(Paragraph(f"• {book}", bullet_style))

story.append(Paragraph("<b>Technology</b>", h2_style))
story.append(Paragraph(
    "Lecture will largely be a low-tech affair: pencil and paper should be sufficient most of the "
    "time. You should always plan to bring a laptop or tablet device to lab. In general, you will "
    "need access to a device with internet so that you can use:", body_style
))
for item in [
    "This course website",
    "R/RStudio via the Duke Container Manager",
    "Canvas (which provides access to Gradescope and Ed Discussion)",
    "Zoom (e.g. for remote office hours)",
]:
    story.append(Paragraph(f"• {item}", bullet_style))
story.append(Paragraph(
    "If access to technology becomes a concern for you during the semester, contact the instructor "
    "immediately to discuss options.", body_style
))

# ── 4. ASSIGNMENTS AND GRADING ─────────────────────────────────────────────
story.append(Paragraph("Assignments and Grading", h1_style))
story.append(section_rule())

story.append(Paragraph("Your final course grade will be calculated as follows:", body_style))
grade_data = [
    ["Category", "Percentage"],
    ["Labs", "10%"],
    ["Problem Sets", "21%"],
    ["Midterm Exam 1", "23%"],
    ["Midterm Exam 2", "23%"],
    ["Final Exam", "23%"],
]
grade_tbl = Table(grade_data, colWidths=[3.5*inch, 3*inch])
grade_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F2F2F2')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ALIGN', (1,0), (1,-1), 'CENTER'),
    ('ALIGN', (0,0), (0,-1), 'LEFT'),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(grade_tbl)
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph("Final letter grades are determined by:", body_style))
letter_data = [
    ["Grade", "Range", "Grade", "Range", "Grade", "Range"],
    ["A+", "≥ 97", "B+", "87 – 89.99", "C+", "77 – 79.99"],
    ["A",  "93 – 96.99", "B",  "83 – 86.99", "C",  "73 – 76.99"],
    ["A-", "90 – 92.99", "B-", "80 – 82.99", "C-", "70 – 72.99"],
    ["D+", "67 – 69.99", "D",  "63 – 66.99", "D-", "60 – 62.99"],
    ["F",  "< 60", "", "", "", ""],
]
letter_tbl = Table(letter_data, colWidths=[0.6*inch, 1.4*inch, 0.6*inch, 1.4*inch, 0.6*inch, 1.4*inch])
letter_tbl.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F2F2F2')]),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
]))
story.append(letter_tbl)
story.append(Spacer(1, 0.08*inch))
story.append(note_box(None,
    "These thresholds will not change and will be applied exactly. Final grades will not be "
    "curved, and a 92.99 will not be rounded up to an A.", warn=True))
story.append(Spacer(1, 0.08*inch))

story.append(Paragraph("<b>Labs (10%)</b>", h2_style))
story.append(Paragraph(
    "In lab every Thursday, you will complete a guided activity that introduces you to special "
    "topics, extensions, or applications of the latest course material, including implementation "
    "in R. Labs are due by 11:59 PM ET the same day they are held.", body_style
))
story.append(Paragraph("Each lab is graded:", body_style))
for row in [
    "1.0 – a complete, good faith attempt at every part of every problem",
    "0.5 – partially complete",
    "0.0 – no submission, or mostly incomplete",
]:
    story.append(Paragraph(f"• {row}", bullet_style))
story.append(note_box("Grace", "Your two lowest lab scores will be dropped at the end of the semester."))

story.append(Paragraph("<b>Problem Sets (21%)</b>", h2_style))
story.append(Paragraph(
    "Problem sets are the heart of the course. They mostly consist of pencil-and-paper math "
    "problems (sometimes with coding). You may compose solutions however you like so long as you "
    "ultimately upload a single .pdf file to Gradescope.", body_style
))
story.append(note_box("Grace", "Your lowest problem set score will be dropped at the end of the semester."))

story.append(Paragraph("<b>Exams (23% each)</b>", h2_style))
story.append(Paragraph("There will be three exams. Dates, times, and locations are firm:", body_style))
for exam in [
    "<b>Midterm 1:</b> Wednesday, February 18 during lecture",
    "<b>Midterm 2:</b> Wednesday, April 1 during lecture",
    "<b>Final:</b> Monday, April 27, 9:00 AM – 12:00 PM, Old Chem 116",
]:
    story.append(Paragraph(f"• {exam}", bullet_style))
story.append(Paragraph(
    "These are old-school, pencil-and-paper, in-class exams. The only allowed resource is both "
    "sides of one 8.5\" × 11\" sheet of notes, handwritten by you alone (directly onto paper, "
    "not on a tablet).", body_style
))
story.append(Paragraph(
    "If you seek testing accommodations, make sure the Student Disability Access Office sends the "
    "instructor a letter, and make your appointments in the Testing Center as soon as possible.",
    body_style
))
story.append(note_box("Grace",
    "If you do better on the final exam than on one of the midterms, your lowest midterm score "
    "will be replaced with your final exam score."))
story.append(note_box("No make-up exams",
    "If you miss a midterm for any reason, there will be no make-up — the missed midterm score "
    "will simply be replaced by the final exam score. If you miss the final exam, you receive a "
    "zero unless you have a Dean's Excuse.", warn=True))

# ── 5. POLICIES ────────────────────────────────────────────────────────────
story.append(Paragraph("Policies", h1_style))
story.append(section_rule())

story.append(Paragraph("<b>Collaboration</b>", h2_style))
story.append(Paragraph(
    "You are <i>enthusiastically encouraged</i> to work together and help one another on labs and "
    "problem sets. What is asked is that you <i>acknowledge</i> your collaborators. So, at the "
    "end of each problem in your write-up, leave a note such as \"Ursula, Ignatius and I worked "
    "together on this problem.\" You are not judged based on your acknowledgements, and there is "
    "no penalty for getting \"too much\" help from others.", body_style
))
story.append(Paragraph(
    "Having said that, you should not be handing your solutions to others for them to brainlessly "
    "copy. This is plagiarism, and all involved will earn a zero and be referred to the conduct "
    "office. The write-up you submit must be your own work.", body_style
))

story.append(Paragraph("<b>Use of Outside Resources, Including AI</b>", h2_style))
story.append(Paragraph(
    "There are at least two reasons you might seek outside resources:", body_style
))
story.append(Paragraph(
    "✅ <b>Extra practice or alternative instruction:</b> Go crazy. The internet is saturated "
    "with good (and horrible) resources for learning this material.", bullet_style
))
story.append(Paragraph(
    "❌ <b>Doing the problems for you:</b> If you find a solution online, or ask a language model "
    "to generate one, and you copy it and submit it as your own work, that is plagiarism. If "
    "detected, you will earn a zero for that part of your write-up.", bullet_style
))
story.append(Paragraph(
    "Furthermore, 69% of your final course grade is determined by your performance on old-school, "
    "no-tech exams. Outsourcing your thinking to an AI will probably end in disaster.", body_style
))

story.append(Paragraph("<b>Communication</b>", h2_style))
story.append(Paragraph(
    "For content-related questions in writing, please use the course discussion forum "
    "<b>Ed Discussion</b> (not e-mail), so all members of the teaching team and all students can "
    "benefit. For personal matters (illness, accommodations, etc.), e-mail the instructor directly "
    "at anya.katsevich@duke.edu.", body_style
))
story.append(note_box(None, "You can ask questions anonymously on Ed. The teaching team will still know your identity, but your peers will not."))

story.append(Paragraph("<b>Late Work and Extensions</b>", h2_style))
story.append(Paragraph(
    "No late work will be accepted unless you request an extension <i>in advance</i> by e-mailing "
    "the instructor directly. All reasonable requests will be entertained, but extensions will not "
    "be long.", body_style
))

story.append(Paragraph("<b>Regrade Requests</b>", h2_style))
story.append(Paragraph(
    "If you believe part of a graded assignment was marked incorrectly, you may submit a regrade "
    "request in Gradescope. Note the following:", body_style
))
for item in [
    "You have one week after receiving a grade to submit a regrade request;",
    "Submit separate regrade requests for each question you wish to dispute;",
    "Requests will be considered if there was an error in the grade calculation or if a correct answer was mistakenly marked as incorrect;",
    "Requests to dispute the number of points deducted for an incorrect response will not be considered;",
    "<b>No grades will be changed after the final exam on Monday, April 27.</b>",
]:
    story.append(Paragraph(f"• {item}", bullet_style))

story.append(Paragraph("<b>Attendance</b>", h2_style))
story.append(Paragraph(
    "Attendance is not strictly required for any class meetings. The responsibility lies with the "
    "teaching team to make class sufficiently engaging and informative that you choose to attend. "
    "That said, success in this class and regular attendance are probably highly positively "
    "correlated. While lab attendance is not required, showing up, completing the lab in one "
    "sitting, and submitting by midnight is probably the path of least resistance to full lab "
    "credit.", body_style
))

story.append(Paragraph("<b>Accommodations</b>", h2_style))
story.append(Paragraph(
    "If you need accommodations, register with the Student Disability Access Office (SDAO) and "
    "provide documentation. SDAO will work with you to determine appropriate accommodations. Note "
    "that accommodations are not retroactive and cannot be provided until a Faculty Accommodation "
    "Letter has been given to the instructor. Contact SDAO: sdao@duke.edu or access.duke.edu.",
    body_style
))

story.append(Paragraph("<b>Duke Community Standard</b>", h2_style))
story.append(Paragraph(
    "Duke University is a community dedicated to scholarship, leadership, and service and to the "
    "principles of honesty, fairness, respect, and accountability. Members of this community "
    "commit to reflect upon and uphold these principles in all academic and non-academic "
    "endeavors, and to protect and promote a culture of integrity.", body_style
))
story.append(Paragraph(
    "In accepting admission, students indicate their willingness to subscribe to and be governed "
    "by the rules and regulations of the university, which flow from the Duke Community Standard "
    "(DCS). It is the responsibility of all students to understand and follow all Duke policies, "
    "including the academic integrity policy.", body_style
))
story.append(Paragraph("In STA 240 specifically:", body_style))
for item in [
    "If a conduct violation results in a zero on a lab or problem set, that zero will not be dropped;",
    "If a conduct violation results in a zero on a midterm, that zero will not be replaced with your final exam score;",
    "If students are found sharing and copying assignment solutions, all students involved will be penalized equally.",
]:
    story.append(Paragraph(f"• {item}", bullet_style))

# ── 6. UNIVERSITY RESOURCES ────────────────────────────────────────────────
story.append(Paragraph("University Resources", h1_style))
story.append(section_rule())

story.append(Paragraph("<b>Course Costs</b>", h2_style))
story.append(Paragraph(
    "If you are having difficulty with costs associated with this course (obtaining a laptop, "
    "mostly), here are some resources:", body_style
))
for item in [
    "<b>Karsh Office of Undergraduate Support:</b> Offers loans and resources for connecting students with campus programs.",
    "<b>DukeLIFE:</b> The Course Material Assistance program offers assistance for eligible students, including the LIFE Loaner Laptop Program.",
    "<b>Duke Link:</b> Has a small supply of laptops that can be rented out for five days at a time.",
]:
    story.append(Paragraph(f"• {item}", bullet_style))

story.append(Paragraph("<b>Tech Support</b>", h2_style))
story.append(Paragraph("Contact the Duke OIT Service Desk at oit.duke.edu/help.", body_style))

story.append(Paragraph("<b>Academic Support</b>", h2_style))
story.append(Paragraph(
    "The Academic Resource Center (ARC) offers services to support students academically, "
    "including time management, academic skills and strategies, and course-specific tutoring. "
    "ARC services are free to all Duke undergraduate students. Contact: (919) 684-5917, "
    "theARC@duke.edu, or arc.duke.edu.", body_style
))

story.append(Paragraph("<b>Accessibility</b>", h2_style))
story.append(Paragraph(
    "If any portion of the course is not accessible to you due to challenges with technology or "
    "the course format, please let the instructor know so appropriate accommodations can be made. "
    "The Student Disability Access Office (SDAO) is available to ensure students can engage with "
    "their courses and related assignments.", body_style
))

story.append(Paragraph("<b>Mental Health and Well-Being</b>", h2_style))
story.append(Paragraph(
    "Duke is committed to holistic student wellbeing. If you find you need support, resources "
    "include:", body_style
))
for item in [
    "<b>DukeReach:</b> Comprehensive outreach services for students managing challenges related to mental health, physical health, social adjustment, and other stressors. Contact: dukereach@duke.edu.",
    "<b>Counseling and Psychological Services (CAPS):</b> Counseling services including virtual appointments. Walk in or call (919) 660-1000. Hours: Mon–Fri 9:00 AM – 4:00 PM. After-hours: (919) 660-1000 Option 2.",
    "<b>TimelyCare:</b> Free 24/7 mental health support (TalkNow and scheduled counseling) for Duke students.",
    "<b>Duke Student Health:</b> Wide range of healthcare services. Call (919) 681-9355. Hours: Mon–Fri 8:00 AM – 4:30 PM (Thu 9:00 AM – 4:30 PM).",
]:
    story.append(Paragraph(f"• {item}", bullet_style))

doc.build(story)
print(f"PDF created: {OUTPUT}")
