#!/usr/bin/env python3
"""Builds research.html and notes/*.html from the note data below.
Run from the repository root:  python3 tools/build_research.py
"""
import html, math, os, random

SITE = "https://aethelonlab.com"
PILLARS = {
    1: ("I", "Current Limits", "Why today's AI, for all its brilliance, does not yet know how to raise a child."),
    2: ("II", "Post-Abundance Horizon", "What learning becomes when knowledge is everywhere and attention is the scarce thing."),
    3: ("III", "Alignment & Privacy", "Whose values the system carries, and who holds a child's record."),
    4: ("IV", "Generational Continuity", "How a family's wisdom outlasts the people who earned it."),
}


def diagram(dark):
    ink = "rgba(245,244,240,.55)" if dark else "rgba(7,8,10,.55)"
    soft = "rgba(245,244,240,.22)" if dark else "rgba(7,8,10,.2)"
    acc = "#C6A87C" if dark else "#8a6f43"
    acc2 = "#7DD3FC" if dark else "#3d8fb5"
    t = 'font-family="IBM Plex Mono,ui-monospace,monospace" font-size="10" letter-spacing="1"'
    o = ['<svg viewBox="0 0 640 310" role="img" aria-label="Top: six separate AI sessions that do not connect. Bottom: one map of a learner that grows from age 1 to 18.">']
    o.append(f'<text x="20" y="24" {t} fill="{ink}">TODAY · EVERY SESSION STARTS AGAIN</text>')
    for i in range(6):
        x = 20 + i * 104
        o.append(f'<rect x="{x}" y="40" width="80" height="62" rx="6" fill="none" stroke="{soft}" stroke-width="1.2"/>')
        o.append(f'<path d="M{x+12} 78 q10 -22 20 -6 t20 -8 t16 4" fill="none" stroke="{ink}" stroke-width="1.2"/>')
        if i < 5:
            o.append(f'<path d="M{x+86} 71 h12" stroke="{soft}" stroke-width="1.2" stroke-dasharray="2 3"/>')
    o.append(f'<text x="20" y="122" {t} fill="{soft}">EACH ONE BRIGHT · NONE REMEMBERS THE LAST</text>')
    o.append(f'<text x="20" y="166" {t} fill="{acc}">AETHELON · ONE MAP THAT GROWS WITH THE CHILD</text>')
    o.append(f'<path d="M30 280 H610" stroke="{soft}" stroke-width="1"/>')
    for age in (1, 5, 10, 15, 18):
        x = 30 + (age - 1) / 17 * 580
        o.append(f'<path d="M{x:.0f} 276 v8" stroke="{ink}" stroke-width="1"/>')
        o.append(f'<text x="{x:.0f}" y="300" text-anchor="middle" {t} fill="{ink}">AGE {age}</text>')
    rnd = random.Random(7)
    nodes = []
    for k in range(46):
        u = (k / 45) ** 0.8
        x = 40 + u * 560
        spread = 14 + u * 70
        y = 262 - rnd.random() * spread
        nodes.append((x, y))
    lines = []
    for i, (x, y) in enumerate(nodes):
        prev = sorted(nodes[:i], key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)[:2]
        for (px, py) in prev:
            lines.append(f'<path d="M{px:.1f} {py:.1f} L{x:.1f} {y:.1f}" stroke="{soft}" stroke-width="1"/>')
    o += lines
    for i, (x, y) in enumerate(nodes):
        c = acc if i % 4 else acc2
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{2.2 + (i % 3) * .6:.1f}" fill="{c}"/>')
    o.append("</svg>")
    return "".join(o)


NOTES = [
 dict(n=1, pillar=1, slug="the-stateless-tutor-problem", status="pub", mins=5,
  title="The Stateless Tutor Problem: Why Context Windows Are Not Memory",
  dek="Today's AI can hold a brilliant conversation and still not know the child in front of it. What would it take for a machine to remember a mind the way a great teacher does?",
  abstract="Today's AI meets a child as a stranger each morning, or carries only a diary of what was said. Raising a mind needs something else: a living map of what a child understands, how they learn and how fast they are growing, kept across eighteen years.",
  body="""
<p>Imagine a tutor of extraordinary knowledge who arrives at your home every morning and greets your daughter as a stranger. He is patient and quick. He can explain anything. But he does not know that she cried over fractions last spring, that she learns best after lunch, or that she will try twice and then go quiet. Tomorrow he will have forgotten today.</p>
<p>That is, in outline, the most capable AI most children can use now. We call it the stateless tutor problem, and we think it is the main reason today's AI, for all its brilliance, is not yet fit to help raise a child.</p>
<h2>1. The Illusion of Conversational Memory</h2>
<p>It is fair to object that modern assistants do remember. They can keep a name, a preference, the subject of last week's chat. This feels like memory, and for an adult planning a holiday it is enough.</p>
<p>But look at what is kept. It is a diary of what was said. Knowing that Maya asked about fractions on Tuesday is different from knowing that she is secure with halves and shaky with thirds, that her confidence drops after two wrong answers, and that any problem involving horses will hold her for an hour. The first is a note. The second is an understanding of a person, and no amount of longer conversation history turns one into the other.</p>
<h2>2. Why Children Require Longitudinal State</h2>
<p>An adult returns to a conversation with roughly the same mind. A child does not. The girl of seven is not the girl of six, and what she needs changes with her.</p>
<p>Learning is also cumulative in a way that hides its own history. A small misunderstanding at eight goes unnoticed, and returns at twelve as "I'm just bad at maths". The people who catch this are the ones who were there: the teacher who kept a class for three years, the grandparent, the family tutor of an earlier age. Their gift was continuity.</p>
<p>Researchers have built computer models of what a learner knows since the 1990s, usually for one subject over one school term. Nobody has yet tried to keep such a picture of one child across a whole childhood. That is the gap we mean to close.</p>
<h2>3. Engineering the Accumulative Cognitive Ledger</h2>
<p>Our answer is a living map of one mind, which we call the Accumulative Cognitive Ledger. It holds three things.</p>
<p>The first is what the child understands, and how securely. The second is how this child learns: her pace, what restores her confidence, what she loves. The third is how quickly she is growing, so that teaching can aim just ahead of where she is.</p>
<p>What it leaves out matters as much. The ledger keeps conclusions, in words a parent can read and correct. It is not an archive of recordings.</p>
<figure>__DIAGRAM__<figcaption>Above, sessions that each begin again. Below, a single picture of a learner that deepens from the first word to adulthood.</figcaption></figure>
<p>Picture what this allows. At fourteen she is stuck on algebra. A stateless tutor explains algebra again, a little slower. A companion with a ledger knows that ratios never quite settled when she was nine, goes back there by way of a stable yard and a feeding schedule, and the algebra gives way. She never learns there was a gap. She just finds that it makes sense now.</p>
<h2>4. Implications for Founding Families</h2>
<p>A ledger like this grows in value the longer it is kept. Year ten is worth far more than year one, and it cannot be bought later or copied from someone else. That is why we begin with families who think in decades.</p>
<p>It also raises the stakes. A record this intimate must belong to the family, be readable by them, and pass to the child when she comes of age. We treat that as part of the design and not as a policy to be added afterwards.</p>
<p>None of this exists yet as a finished product. It is what we intend to build, and the first families will help decide what the ledger should hold and what it must never hold. If that question interests you, we would like to talk.</p>
""",
  refs=[("Corbett, A. T., &amp; Anderson, J. R. (1994). Knowledge tracing: Modeling the acquisition of procedural knowledge. <i>User Modeling and User-Adapted Interaction</i>, 4, 253–278.", None)]),

 dict(n=2, pillar=1, slug="conversation-before-content", status="pub", mins=4,
  title="Conversation Before Content: What the Earliest Years Ask of a Machine",
  dek="Small children do not need more words poured in. They need someone who answers back.",
  abstract="In the first years, language grows in the back-and-forth between a child and someone who responds. A companion for this age should listen, take turns and leave a household with more to talk about.",
  body="""
<p>A two-year-old points at the window and says "bird". Someone says, "Yes, a bird. Where is he going?" The child thinks, and says, "Tree." That small exchange, repeated thousands of times, is how a mind learns to speak.</p>
<p>The easiest mistake in building technology for very young children is to assume they need more input: more words, more pictures, more lessons. The evidence points somewhere else.</p>
<h2>1. Turns, not volume</h2>
<p>In 2018 researchers at MIT and Harvard recorded the home language of 36 children aged four to six, and scanned their brains as they listened to stories. The number of words a child heard explained little. What went with stronger language, and with more activity in a core language region of the brain, was the number of back-and-forth exchanges with an adult. That held whatever the family's income.</p>
<p>It is one small study and it shows a link, not a cause. But it agrees with a long line of work on how children develop. Language grows in exchange, when someone responds to what the child just did.</p>
<h2>2. Screens are the wrong place to start</h2>
<p>The World Health Organization's guidance for children under five is direct. Sedentary screen time is not recommended for one-year-olds, and for ages two to four it should be no more than an hour a day, with less being better. Reading and storytelling with a caregiver are encouraged instead.</p>
<h2>3. What this could look like</h2>
<p>So in the first stage of a child's life, the system we imagine listens and takes turns. It speaks through a companion in the room and not through a display. It waits, answers what the child said, and leaves room for the reply.</p>
<p>The second idea matters more. A machine that took all of a child's conversational turns would be replacing the very thing that matters. The early-years companion is meant to do the opposite: to notice what the child is curious about and pass it to the adults. "She asked three times today where the moon goes." Now dinner has something to talk about.</p>
<p>At this age, success is a household that talks more.</p>
""",
  refs=[("Romeo, R. R., et al. (2018). Beyond the 30-Million-Word Gap: Children's Conversational Exposure Is Associated With Language-Related Brain Function. <i>Psychological Science</i>, 29(5), 700–710.", "https://doi.org/10.1177/0956797617742725"),
        ("World Health Organization (2019). To grow up healthy, children need to sit less and play more.", "https://www.who.int/news/item/24-04-2019-to-grow-up-healthy-children-need-to-sit-less-and-play-more")]),

 dict(n=3, pillar=1, slug="why-the-companion-needs-a-body", status="pub", mins=4,
  title="Why the Companion Needs a Body",
  dek="If a child can learn from a voice, why give that voice a physical presence in the room?",
  abstract="Children respond to something that shares their space in ways they do not respond to a screen. The bodies are arriving. What is missing is a mind suited to a childhood.",
  body="""
<p>Watch a child with a tablet and then with a puppy. The tablet gets her eyes. The puppy gets all of her. Something that shares your space, turns towards you and waits for you is a different kind of company.</p>
<p>That difference is why we think a learning companion should have a body. It is an expensive idea to get wrong, so it is worth being clear about what is known.</p>
<h2>1. What the research found</h2>
<p>In 2018 a group led by Tony Belpaeme reviewed the published studies on social robots in education for the journal <i>Science Robotics</i>. Robots acting as tutors or fellow learners improved both what children knew and how they felt about learning, and on narrow tasks came close to a human tutor. The authors put this down largely to the robot being physically there, which a screen is not.</p>
<p>The same review was frank about the limits. The gains were on restricted topics. Machines could not yet reliably understand young children's speech. Some children leaned on the robot's help too readily. Parents and teachers were more cautious than the children were, and the authors asked how much of a child's education should be handed to a machine at all.</p>
<h2>2. What is changing</h2>
<p>Two of those limits were technical, and both are moving. Machines are getting better at understanding children's voices, and general-purpose humanoid robots are beginning to leave the laboratory. The bodies are arriving. What they lack is a mind suited to a childhood.</p>
<h2>3. What this could look like</h2>
<p>That is where we have chosen to work. Others are better placed to build the hands and the balance. We are designing the mind that would live in such a body for eighteen years, and designing it to run on whichever hardware proves best.</p>
<p>We also take the review's cautions as instructions. Imagine a companion that kneels beside a boy building a bridge from blocks, watches it fall, and says nothing for a moment. It holds back help until he has tried again. And when his parents ask what he worked on today, it tells them, because they set its limits and can pause it whenever they wish.</p>
<p>A companion earns its place in a home by making the adults in it more effective.</p>
""",
  refs=[("Belpaeme, T., Kennedy, J., Ramachandran, A., Scassellati, B., &amp; Tanaka, F. (2018). Social robots for education: A review. <i>Science Robotics</i>, 3(21).", "https://doi.org/10.1126/scirobotics.aat5954")]),

 dict(n=4, pillar=1, slug=None, status="plan", title="Compute as Utility: A Mind That Lives Partly at Home",
  abstract="Some thinking has to happen in the room, instantly and privately. Some can be drawn from elsewhere when needed, like electricity. This note will describe how a home companion might divide the two, and why the split protects a family."),

 dict(n=5, pillar=2, slug="the-two-sigma-promise", status="pub", mins=4,
  title="The Two Sigma Promise: When Every Child Has a Tutor",
  dek="Forty years ago a researcher showed what a personal tutor is worth, and called it a problem because no society could afford one for every child. That is changing.",
  abstract="A personal tutor has long been the most effective form of teaching and the least affordable. As intelligence becomes abundant, the question shifts from cost to continuity.",
  body="""
<p>For most of history, the best education money could buy was a person: a tutor who knew one child well and stayed for years. Royal households had them. Almost nobody else did.</p>
<h2>1. What a tutor is worth</h2>
<p>In 1984 the educational psychologist Benjamin Bloom put a number on it. Students taught one-to-one, and not moved on until they had mastered each step, finished about two standard deviations ahead of students in an ordinary class. Put plainly, the average tutored student did better than roughly 98 in 100 of the others.</p>
<p>Bloom did not call this a triumph. He called it a problem, because no society could pay for a tutor for every child. His challenge was to find something that worked as well and could reach everyone.</p>
<h2>2. What has changed</h2>
<p>For four decades the answer was partial. Then AI made patient, conversational teaching cheap. In 2025 a team at Harvard published a careful trial with 194 undergraduates in a physics course. Students who worked with a purpose-built AI tutor learned more than twice as much as those in a well-taught active class, and in less time.</p>
<p>The limits matter as much as the headline. These were university students, in one subject, for two weeks. The tutor was designed by their own lecturers, and it was built to make students reason instead of handing over answers. A general chatbot dropped into a classroom is a different thing.</p>
<h2>3. What this could look like</h2>
<p>We take two lessons. The first is that design decides the outcome. A tutor that holds back the answer and asks the next question is what produces the gain, so the companion we imagine coaches before it explains.</p>
<p>The second is about time. Every trial so far is short. Nobody has seen what happens when a tutor knows a learner for years: which ideas were fragile at seven, what finally made fractions make sense, how this particular mind likes to be challenged.</p>
<p>Imagine a world where intelligence is as available as electricity. In that world Bloom's problem stops being about cost. What remains scarce is a tutor who remembers, and that is the thing we are setting out to build.</p>
""",
  refs=[("Bloom, B. S. (1984). The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring. <i>Educational Researcher</i>, 13(6), 4–16.", "https://doi.org/10.3102/0013189X013006004"),
        ("Kestin, G., Miller, K., Klales, A., Milbourne, T., &amp; Ponti, G. (2025). AI tutoring outperforms in-class active learning. <i>Scientific Reports</i>, 15, 17458.", "https://doi.org/10.1038/s41598-025-97652-6")]),

 dict(n=6, pillar=2, slug=None, status="plan", title="Post-Abundance Pedagogy: What to Teach When Models Know Everything",
  abstract="When any fact or method can be had by asking, what is still worth a child's years? This note will make the case for judgement, taste, character and the ability to ask a good question."),

 dict(n=7, pillar=2, slug=None, status="plan", title="After the Exam: Knowing a Learner Without Testing Them",
  abstract="An exam is a snapshot taken under stress. A companion that has watched a child learn for years might know what she understands without ever stopping to test her. This note will explore what that could replace, and what it must not become."),

 dict(n=8, pillar=3, slug=None, status="plan", title="The Values Rail: A System That Carries Your Values, Not Its Own",
  abstract="Every family and every school teaches from a set of values. This note will describe how a companion could begin neutral and take its guidance from the people responsible for the child, and how they could see and change that guidance."),

 dict(n=9, pillar=3, slug="a-private-childhood", status="pub", mins=4,
  title="A Private Childhood: Keeping a Child's Record in the Family's Hands",
  dek="A companion that stays for eighteen years will hold the most personal record a child ever has. A promise is not enough to protect it.",
  abstract="A record of how a child grew up should belong to the family and then to the child. That has to be true of how the system is built, and not only of what it promises.",
  body="""
<p>Think of what a family photograph album holds, and then imagine one that also remembered every question a child asked, every idea she struggled with, and the day each one finally made sense. That is the record a lifelong learning companion would keep. It would be precious, and in the wrong hands it would be dangerous.</p>
<p>So the honest starting point is that a promise is not enough. Privacy has to be a property of how the thing is built.</p>
<h2>1. Where the law has drawn a line</h2>
<p>The European Union's AI Act is the clearest signal so far. It prohibits AI systems that infer a person's emotions in workplaces and in educational institutions, with exceptions for medical and safety purposes. The reasoning is about power: a pupil cannot easily refuse.</p>
<p>A family home is not a school, so that rule does not directly cover a system a family chooses for itself. But the principle behind it is sound anywhere. A child's inner life should not become a product. This is our reading as builders and is not legal advice.</p>
<h2>2. Four commitments</h2>
<p>First, the companion notices only what a good teacher would. It needs to know whether a child is with it or has drifted to the window. It uses that in the moment to change the lesson, and does not keep it as footage.</p>
<p>Second, what happens in the room stays in the room. Sound and pictures are handled inside the home. What goes into the long-term record is a conclusion, such as an idea mastered or a misunderstanding noticed.</p>
<p>Third, the family holds the keys. The aim is a record that we as a company cannot read, and that the family can erase.</p>
<p>Fourth, the record has an owner in waiting. Picture an eighteenth birthday on which a young woman is handed the story of how her own mind grew, to keep, to share or to close for good. From that day it is hers.</p>
<h2>3. An invitation to doubt us</h2>
<p>None of this is proven until it is built and examined by people who do not work for us. We would rather a founding family ask the hardest questions now than discover the answers later.</p>
""",
  refs=[("Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 5(1)(f).", "https://eur-lex.europa.eu/eli/reg/2024/1689/oj"),
        ("Future of Privacy Forum. Red Lines under the EU AI Act: the prohibition of emotion recognition in the workplace and education institutions.", "https://fpf.org/blog/red-lines-under-eu-ai-act-unpacking-the-prohibition-of-emotion-recognition-in-the-workplace-and-education-institutions/")]),

 dict(n=10, pillar=4, slug=None, status="plan", title="The Third-Generation Problem: Passing On More Than Wealth",
  abstract="Families often find that what the first generation built is gone by the third. Money passes easily. The judgement that earned it does not. This note will imagine a vault of a family's stories, principles and reasoning, opened to each child as they become ready."),

 dict(n=11, pillar=4, slug=None, status="plan", title="From Private Capsules to Public Infrastructure",
  abstract="Many things that began as a privilege of a few became ordinary: books, schooling, electric light. This note will trace how a companion first built for a few families could become something every child has."),
]


def esc(s):
    return html.escape(s, quote=True)


def pill(p):
    r, name, _ = PILLARS[p]
    return f"Pillar {r} · {name}"


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{ogtype}">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2307080A'/%3E%3Ccircle cx='16' cy='16' r='9' fill='none' stroke='%23C6A87C' stroke-width='1.5'/%3E%3Ccircle cx='16' cy='16' r='2.5' fill='%237DD3FC'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Hanken+Grotesk:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/research.css">
</head>
"""


def nav(root, back_href, back_label):
    return f"""<header class="nav"><div class="nav-in">
  <a class="brand" href="{root}index.html" aria-label="Aethelon home"><b>AETHELON</b></a>
  <div class="nav-r"><a class="back" href="{back_href}">← {back_label}</a><a class="btn" href="{root}index.html#briefing">Request Private Briefing</a></div>
</div></header>
"""


FOOT = """<footer><div class="wrap"><span>© 2026 Aethelon</span><span>aethelonlab.com</span><span>Private Briefing Only</span></div></footer>
<script src="{root}assets/research.js"></script>
</body>
</html>
"""


def build_index():
    pubs = [n for n in NOTES if n["status"] == "pub"]
    o = [HEAD.format(title="Aethelon Research", ogtype="website", url=f"{SITE}/research.html", root="",
                     desc="Research notes from Aethelon on the limits of today's AI, learning in an age of abundant intelligence, and the privacy a child is owed across eighteen years.")]
    o.append("<body>\n" + nav("", "index.html", "Back to Aethelon"))
    o.append("""<main id="top">
<section class="head"><div class="wrap">
  <span class="kicker">Aethelon Research · Notes on the future of nurturing</span>
  <h1>From Stateless Models to Sovereign Nurturing.</h1>
  <p>Notes on the limits of today's AI, on what learning becomes when intelligence is abundant, and on the privacy a child is owed across eighteen years. Each one imagines what could ideally happen, and says plainly what is known and what is not.</p>
  <span class="stage">AETHELON IS AT CONCEPT STAGE · THESE NOTES DESCRIBE WHAT WE INTEND TO BUILD</span>
</div></section>
<section><div class="wrap">
""")
    o.append('<div class="filters" id="filters" role="group" aria-label="Filter notes by pillar">')
    o.append(f'<button aria-pressed="true" data-f="all" data-line="{len(pubs)} notes published, {len(NOTES) - len(pubs)} planned.">All Notes <small>{len(NOTES):02d}</small></button>')
    for p, (r, name, line) in PILLARS.items():
        c = sum(1 for n in NOTES if n["pillar"] == p)
        o.append(f'<button aria-pressed="false" data-f="{p}" data-line="{esc(line)}">{r}. {name} <small>{c:02d}</small></button>')
    o.append("</div>")
    o.append(f'<p class="pillar-line" id="pillarLine" aria-live="polite">{len(pubs)} notes published, {len(NOTES) - len(pubs)} planned.</p>')
    f = NOTES[0]
    o.append(f"""<article class="feat" id="feat">
  <div>
    <span class="meta">Note 01 · {pill(1)} · Q4 2026 · {f['mins']} min read</span>
    <h2><a href="notes/{f['slug']}.html">{f['title']}</a></h2>
    <p>{f['abstract']}</p>
    <a class="btn" href="notes/{f['slug']}.html">Read the full note →</a>
  </div>
  <div>{diagram(True)}</div>
</article>
<ul class="list">
""")
    for n in NOTES:
        num = f"NOTE {n['n']:02d}"
        if n["status"] == "pub":
            o.append(f"""<li data-pillar="{n['pillar']}"><div class="row">
  <span class="n">{num}</span>
  <div><h3><a href="notes/{n['slug']}.html">{n['title']}</a></h3><p>{n['abstract']}</p><span class="tag">{pill(n['pillar'])} · {n['mins']} min read</span></div>
  <span class="badge pub">Published · Q4 2026</span>
</div></li>
""")
        else:
            o.append(f"""<li data-pillar="{n['pillar']}"><details>
  <summary><div class="row">
    <span class="n">{num}</span>
    <div><h3>{n['title']}</h3><span class="tag">{pill(n['pillar'])}</span></div>
    <span class="badge">Planned · 2027</span>
  </div></summary>
  <div class="preview"><p>{n['abstract']}</p><a class="btn ghost" href="index.html#briefing">Ask to read it early</a></div>
</details></li>
""")
    o.append("""</ul>
<div class="agenda">
  <h2>Contribute to the research agenda</h2>
  <div><p>We share early drafts with founding families, researchers in child development, and institutional partners before they are published.</p><a class="btn" href="index.html#briefing">Request Private Briefing</a></div>
</div>
</div></section>
</main>
""")
    o.append(FOOT.format(root=""))
    open("research.html", "w").write("".join(o))


def build_note(n):
    pubs = [x for x in NOTES if x["status"] == "pub" and x is not n]
    url = f"{SITE}/notes/{n['slug']}.html"
    body = n["body"].replace("__DIAGRAM__", diagram(False))
    refs = "".join(f'<li>{t}{(" <a href=" + chr(34) + u + chr(34) + " target=" + chr(34) + "_blank" + chr(34) + " rel=" + chr(34) + "noopener" + chr(34) + ">Link</a>") if u else ""}</li>' for t, u in n["refs"])
    rel = "".join(f'<li><a href="{x["slug"]}.html">{x["title"]}</a><span>Note {x["n"]:02d} · {pill(x["pillar"])}</span></li>' for x in pubs[:3])
    o = [HEAD.format(title=esc(n["title"]), desc=esc(n["dek"]), ogtype="article", url=url, root="../")]
    o.append('<body class="note">\n<div class="progress" aria-hidden="true"><i id="prog"></i></div>\n' + nav("../", "../research.html", "All research notes"))
    o.append(f"""<main><article class="art" id="art">
<nav class="crumbs" aria-label="Breadcrumb"><a href="../research.html">Research</a> / {pill(n['pillar'])}</nav>
<h1>{n['title']}</h1>
<p class="dek">{n['dek']}</p>
<div class="art-by"><span>Aethelon Research · Note {n['n']:02d} · Q4 2026 · {n['mins']} min read</span><button class="copy" id="copy" data-url="{url}">Copy for newsletter</button></div>
<div class="body">{body}</div>
<div class="refs-h">Further reading</div>
<ul class="refs">{refs}</ul>
<p class="fine">Aethelon is at concept stage. This note describes what we intend to build and what we think it could make possible. It does not describe a finished product.</p>
<div class="invite"><h2>Discuss this note with us</h2><p>We hold one-to-one briefings with family offices, researchers and partners who want to test the thinking.</p><a class="btn" href="../index.html#briefing">Request Private Briefing</a></div>
<div class="related"><h2>More research notes</h2><ul>{rel}</ul></div>
</article></main>
""")
    o.append(FOOT.format(root="../"))
    open(f"notes/{n['slug']}.html", "w").write("".join(o))


if __name__ == "__main__":
    os.makedirs("notes", exist_ok=True)
    build_index()
    for n in NOTES:
        if n["status"] == "pub":
            build_note(n)
    print("built", sum(1 for n in NOTES if n["status"] == "pub"), "notes")
