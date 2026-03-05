[Skip to content](https://www.notion.so/NotebookLM-AntiGravity-318e8d6bd13780a08d68c367e24d2094#main)

![](https://www.notion.so/image/attachment%3A79c11046-089d-442c-87a5-ad2d9d8155da%3Ahf_20260303_150223_b73b1fff-baf6-4ca5-9fa5-c083437af644.jpeg?table=block&id=318e8d6b-d137-80a0-8d68-c367e24d2094&spaceId=988befb5-15c5-408d-a1af-f73659077abe&width=2000&userId=&cache=v2)

# NotebookLM + AntiGravity

Enter this into AntiGravity ![👇](<Base64-Image-Removed>)​

> Install and set up NotebookLM for me using the notebooklm-py library ( [https://github.com/teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)):
>
> 1\. Install the package with browser support:
>
> pip install "notebooklm-py\[browser\]"
>
> playwright install chromium
>
> 2\. Run the login command to authenticate via browser:
>
> notebooklm login
>
> (A Chromium window will open — sign in with your Google account. Make sure you're signed out of any conflicting Google sessions first.)
>
> 3\. Install the Antigravity skill:
>
> notebooklm skill install antigravity
>
> 4\. Verify everything is working:
>
> notebooklm list
>
> Make sure to:
>
> Use pip if uv isn't available
>
> Sign out of any existing Google browser sessions before authenticating to avoid conflicts
>
> Guide me through the Chromium browser login if it opens
>
> Run notebooklm auth check if anything seems off after login
>
> Confirm the skill is installed and notebooks are listing correctly at the end

Prompt for Dashboard Generator ![👇](<Base64-Image-Removed>)​

## ![🧠](<Base64-Image-Removed>) Automated Meeting Prep Dashboard Generator

> A complete pipeline using NotebookLM to generate deep research, artifacts, and a gorgeous glassmorphic HTML dashboard for meeting prep. Takes a company/meeting context and builds a local presentation website.

## Automated Meeting Prep Framework

This skill dictates how to operate as an elite intelligence analyst and engineer, automatically building a comprehensive web dashboard full of deep-researched artifacts for any upcoming meeting or company target, leveraging the NotebookLM MCP tools.

### ![🎯](<Base64-Image-Removed>) The Goal

Take a raw input (a company name, domain, and/or meeting context) and transform it into a ready-to-view, high-end "Meeting Prep Dashboard" folder containing:

A suite of AI-generated Markdown documents (briefing, competitive intel, research report, quiz, flashcards).

Downloaded media artifacts (audio podcast MP3, market infographic PNG).

A beautiful, offline-ready HTML dashboard unifying everything for the executive.

### ![⚡](<Base64-Image-Removed>) Trigger Details

Input can come from any of the following sources:

Zapier/Make automation: Watching Google Calendar for new "Discovery Call" events and firing a payload with the company name.

Email/CRM trigger: A new lead or meeting request arriving in an inbox or CRM system.

Manual prompt: The user simply types a company name and meeting context directly.

The input payload should contain at minimum:

company\_name

, and optionally:

company\_domain

,

meeting\_date

,

meeting\_type

,

contact\_name

,

contact\_title

.

## ![🔁](<Base64-Image-Removed>) Step-By-Step Execution Pipeline

### Phase 0: Agent Pre-Research (Data Enrichment)

Before relying on NotebookLM, the autonomous agent must do its own groundwork to create high-quality "seed data." NotebookLM's outputs are only as good as the sources you feed it — garbage in, garbage out.

#### Step 0.1 — Website Scrape

Use web scraping tools (Firecrawl, Exa, Tavily, or Apify via MCP) to read the company's official website. Target these specific pages:

About / Company page

Products / Services / Platform page

Pricing page (if public)

Team / Leadership page

Blog / News / Press page

Careers page (reveals growth stage and tech stack)

#### Step 0.2 — External Enrichment

Search the broader web to find:

LinkedIn company page (employee count, recent posts, hiring activity)

Crunchbase or PitchBook data (funding rounds, investors, valuation)

Recent news articles, press releases, or founder interviews (last 6 months)

Wikipedia page (if it exists)

Glassdoor or similar (company culture signals)

Any YouTube videos featuring the company or its founders

#### Step 0.3 — Synthesize Company Profile

Combine all scraped data into a single, highly distilled "Company Profile" text document. This document should include:

Company name, HQ location, founding year

CEO/founder names and backgrounds

Employee count range

Funding history (rounds, amounts, lead investors)

Revenue model (SaaS, services, hybrid, marketplace)

Core products/services (with brief descriptions)

Key clients or case studies mentioned on their site

Direct competitors (named on their site or obvious from market position)

Recent news highlights (last 2-3 significant events)

The meeting context (why are we meeting them? what do they want from us?)

> ![💡](<Base64-Image-Removed>) This profile becomes the foundational "seed" for NotebookLM. It ensures the AI never hallucinates because it starts with verified facts.

### Phase 1: Notebook Preparation & Initial Ingestion

This phase creates the isolated knowledge brain for this specific client.

#### Step 1.1 — Create Notebook

mcp: notebook\_create
title: "Meeting Prep - \[Company Name\]"

​

#### Step 1.2 — Inject Seed Data as Text Source

mcp: source\_add
notebook\_id: \[from step 1.1\]
source\_type: "text"
title: "\[Company Name\] — Company Profile"
text: \[the synthesized Company Profile from Phase 0.3\]
wait: true

​

#### Step 1.3 — Add Scraped URLs as Sources

For each high-quality URL found during Phase 0 (company website, Wikipedia, key news articles), add them individually:

mcp: source\_add
notebook\_id: \[from step 1.1\]
source\_type: "url"
url: "\[each URL\]"
wait: true

​

> ![ℹ️](<Base64-Image-Removed>) Add 3-8 of the best URLs. Don't add more than 10 here — deep research will find more.

### Phase 2: Autonomous Deep Research (NotebookLM Web Search)

This is where NotebookLM's killer feature kicks in — it autonomously searches the web for 40-100+ additional sources about the company and their industry.

#### Step 2.1 — Start Deep Research

mcp: research\_start
notebook\_id: \[from step 1.1\]
query: "\[Company Name\] competitive landscape market trends \[industry\] \[region\] 2025 2026"
source: "web"
mode: "deep"

​

Use

mode: "deep"

for exhaustive coverage (takes ~5 minutes, finds 40-100+ sources).
Use

mode: "fast"

if speed is critical (takes ~30 seconds, finds ~10 sources).

#### Step 2.2 — Poll Until Complete

mcp: research\_status
notebook\_id: \[from step 1.1\]
max\_wait: 300

​

Wait for

status: "completed"

before proceeding.

#### Step 2.3 — Batch Import Sources (CRITICAL)

If

mode="deep"

returns a large number of sources (40-110+), importing them all at once WILL cause an MCP timeout error. You MUST batch the imports.

\# Import sources 0-19
mcp: research\_import
notebook\_id: \[from step 1.1\]
task\_id: \[from step 2.1\]
source\_indices: \[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19\]

\# Import sources 20-39
mcp: research\_import
source\_indices: \[20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39\]

\# Continue in chunks of 20 until all sources are imported...

​

If using

mode="fast"

, you can safely omit

source\_indices

to import all ~10 sources at once.

> ![⚠️](<Base64-Image-Removed>)Important: Wait a few seconds between each batch to let NotebookLM process the incoming sources.

### Phase 3: Artifact Generation & Extraction

Now the notebook has a rich, comprehensive knowledge base. Use NotebookLM's querying and studio features to generate the output artifacts.

#### Step 3.1 — Executive Briefing (  01\_briefing\_doc.md  )

Use

notebook\_query

or

studio\_create

(report format) with the following prompt:

> "Create a comprehensive executive pre-meeting briefing document with these exact sections: 1) Company Overview (background, size, leadership, financials, business model, core products, key clients, recent developments, meeting context), 2) Competitive Landscape (name each competitor, their approach, and the client's advantage), 3) Market Opportunity (specific dollar figures, growth rates, and government initiatives), 4) Key Talking Points (numbered, actionable conversation starters), 5) Handling Objections (table format with Objection and Response columns), 6) Recommended Next Steps (3 concrete follow-up actions)."

Save the output as

01\_briefing\_doc.md

.

#### Step 3.2 — Deep Research Report (  02\_deep\_research\_report.md  )

mcp: notebook\_query
notebook\_id: \[from step 1.1\]
query: "Write a deep research report summarizing the macro trends affecting this company's industry over the next 2 years. Include a table of the top 10 most important sources discovered, with columns for Source Name and Why It Matters. Then summarize the key themes assessed."

​

Save the output as

02\_deep\_research\_report.md

.

#### Step 3.3 — Competitive Intelligence (  03\_competitive\_intel.md  )

mcp: notebook\_query
query: "Create a rapid competitive intelligence cheat sheet formatted as: Top 3 Things to Know (each with a bold headline, 3-4 bullet points of evidence, and a 'Your angle' recommendation), followed by a 'Market Numbers to Drop in Conversation' section listing 7-10 specific statistics with dollar signs and percentages."

​

Save the output as

03\_competitive\_intel.md

.

#### Step 3.4 — Market Infographic (  04\_market\_infographic.png  )

mcp: studio\_create
notebook\_id: \[from step 1.1\]
artifact\_type: "infographic"
orientation: "portrait"
detail\_level: "detailed"
confirm: true

​

Poll

studio\_status

until the infographic is completed, then:

mcp: download\_artifact
notebook\_id: \[from step 1.1\]
artifact\_type: "infographic"
output\_path: "\[prep\_folder\]/04\_market\_infographic.png"

​

#### Step 3.5 — Audio Briefing Podcast (  audio\_briefing.mp3  )

mcp: studio\_create
notebook\_id: \[from step 1.1\]
artifact\_type: "audio"
audio\_format: "brief"
audio\_length: "short"
confirm: true

​

Poll

studio\_status

until the audio is completed, then:

mcp: download\_artifact
notebook\_id: \[from step 1.1\]
artifact\_type: "audio"
output\_path: "\[prep\_folder\]/audio\_briefing.mp3"

​

#### Step 3.6 — Knowledge Quiz (  06\_pre\_call\_quiz.md  )

mcp: studio\_create
notebook\_id: \[from step 1.1\]
artifact\_type: "quiz"
question\_count: 8
difficulty: "medium"
confirm: true

​

Poll

studio\_status

, then download:

mcp: download\_artifact
artifact\_type: "quiz"
output\_path: "\[prep\_folder\]/06\_pre\_call\_quiz.md"
output\_format: "markdown"

​

#### Step 3.7 — Flashcards (  07\_flashcards.md  )

mcp: studio\_create
notebook\_id: \[from step 1.1\]
artifact\_type: "flashcards"
difficulty: "medium"
confirm: true

​

Poll

studio\_status

, then download:

mcp: download\_artifact
artifact\_type: "flashcards"
output\_path: "\[prep\_folder\]/07\_flashcards.md"
output\_format: "markdown"

​

> ![💡](<Base64-Image-Removed>)Fallback for thin flashcards: If the downloaded flashcards contain fewer than 8 Q&A pairs, automatically run a supplementary
>
> notebook\_query
>
> :

> "Generate 10 flashcard-style Q&A pairs covering the most important facts someone should memorize before meeting with \[Company Name\]. Format each as 'Q: \[question\]' and 'A: \[answer\]'."

Append these to the flashcards file.

#### Step 3.8 — Slide Deck (  08\_slide\_deck.pdf  ) \[Optional\]

mcp: studio\_create
notebook\_id: \[from step 1.1\]
artifact\_type: "slide\_deck"
slide\_format: "detailed\_deck"
confirm: true

​

Download as PDF when complete.

### Phase 4: Index File Generation

Create a

00\_INDEX.md

file that serves as the table of contents for the prep folder:

# Meeting Prep Package: \[Company Name\]\*\*Generated:\*\* \[timestamp\]
\*\*Meeting Date:\*\* \[date\]
\*\*Meeting Type:\*\* \[type\]

## Downloaded Files\|#\| File \| Description \|\|\-\-\-\|\-\-\----\|\-\-\-----------\|\| 1 \| 01\_briefing\_doc.md \| Executive pre-meeting briefing \|\| 2 \| 02\_deep\_research\_report.md \| Deep research summary with source table \|\| 3 \| 03\_competitive\_intel.md \| Competitive intelligence cheat sheet \|\| 4 \| 04\_market\_infographic.png \| Visual market landscape infographic \|\| 5 \| 06\_pre\_call\_quiz.md \| Knowledge test (8 questions) \|\| 6 \| 07\_flashcards.md \| Rapid-review flashcards \|\| 7 \| audio\_briefing.mp3 \| AI podcast briefing \|\| 8 \| index.html \| Interactive dashboard \|## Cloud Resources-\*\*NotebookLM Notebook:\*\* \[link to notebook\]
-\*\*Research Sources:\*\* \[number\] web sources analyzed

## How to Use1. Open \`index.html\` in your browser for the full interactive experience
2. Or run \`python3 -m http.server 8888\` in this folder and visit localhost:8888
3. Listen to \`audio\_briefing.mp3\` on your commute
4. Review \`01\_briefing\_doc.md\` for a 3-minute text summary

​

### Phase 5: Constructing the Premium HTML Dashboard

Package all artifacts into a single interactive HTML dashboard.

#### Step 5.1 — Create Output Folder

Create a folder named

Meeting Prep - \[Company Name\]

in the current working directory.

#### Step 5.2 — Build the HTML Dashboard (  index.html  )

The dashboard must include ALL of the following:

Navbar with "Antigravity OS" branding, meeting date badge, and Export PDF button

Header with company name, subtitle, and embedded audio player with animated visualizer bars

Sidebar navigation with 6 tabs: Executive Briefing, Competitive Intel, Deep Research, Knowledge Test, Flashcards, Market Infographic

Content area that dynamically renders markdown content for the first 3 tabs using marked.js

Critical implementation details for the dashboard:

1\. Markdown tabs (Briefing, Intel, Research): Store the raw markdown inside

<script type="text/markdown" id="md-\[tabname\]">

blocks. Use marked.js to parse and render them when the tab is clicked.

2\. Quiz tab: Do NOT render via markdown — build an interactive quiz with:

Question cards with clickable radio-button options

Green ✓ / Red ✗ visual feedback on answer selection

Score counter that appears after all questions are answered

Questions sourced from the downloaded quiz file

3\. Flashcards tab: Do NOT render via markdown — build an interactive flashcard component with:

3D flip animation (CSS

perspective

\+

rotateY(180deg)

)

Purple gradient front (Question), gold accent back (Answer)

Left/right arrow navigation with card counter

Progress dots below the card

Content sourced from the downloaded flashcards file

4\. Market Infographic tab: Do NOT render via markdown (the

<img>

tag will get escaped). Render natively with a JS function that returns HTML with the

<img>

tag pointing to

04\_market\_infographic.png

.

5\. Audio player:

<audio>

element pointing to

audio\_briefing.mp3

with play/pause toggle button and animated visualizer bars.

6\. Styling requirements:

Dark mode: background

#08080c

with purple/blue radial gradients

Glassmorphism:

backdrop-filter: blur(10px)

, transparent white backgrounds, subtle borders

Font: Inter from Google Fonts

Icons: Font Awesome 6

CSS framework: Tailwind CSS via CDN

Markdown styling: Custom CSS for h1-h3, p, ul, li, strong, a, table, th, td within

.markdown-content

#### Step 5.3 — Start Local Server (Optional)

cd"Meeting Prep - \[Company Name\]"
python3 -m http.server 8888\# Then open http://localhost:8888/index.html

​

## ![📐](<Base64-Image-Removed>) Guiding Principles & Constraints

#### ![🔴](<Base64-Image-Removed>) Batch Imports (Non-Negotiable)

Never attempt to bulk-import 100+ sources from deep research at once. Always iterate in chunks of 20 using the

source\_indices

parameter. Wait 2-3 seconds between batches.

#### ![🟡](<Base64-Image-Removed>) Fail Gracefully

If

flashcards

studio output is too thin (fewer than 8 cards), automatically regenerate via

notebook\_query

with an explicit prompt for 10 Q&A pairs.

If

infographic

generation fails, skip it and note it in the INDEX file. The dashboard should still work without it.

If

audio

generation is still processing after 5 minutes, move on and note it as "generating" in the INDEX.

#### ![🎨](<Base64-Image-Removed>) Aesthetics Are Non-Negotiable

The HTML dashboard must feel premium — dark modes, glassmorphism, smooth transitions, crisp typography, animated elements. It should look like a product, not a prototype. Jack's colour preferences are blue + gold.

#### ![🔐](<Base64-Image-Removed>) Data Isolation

Each client/meeting gets its own NotebookLM notebook. Never reuse notebooks across clients. This prevents data contamination and hallucination.

#### ![🛡️](<Base64-Image-Removed>) Security

Never leak API keys, MCP tokens, or authentication credentials into the HTML dashboard.

All servers are local only (localhost).

Generated content stays on the user's machine unless explicitly shared.

#### ![📁](<Base64-Image-Removed>) File Naming Convention

All files in the prep folder follow this pattern:

00\_INDEX.md
01\_briefing\_doc.md
02\_deep\_research\_report.md
03\_competitive\_intel.md
04\_market\_infographic.png
06\_pre\_call\_quiz.md
07\_flashcards.md
08\_slide\_deck.pdf
audio\_briefing.mp3
index.html

​

### ![📋](<Base64-Image-Removed>) Quick Reference: MCP Tools Used

| Tool | Phase | Purpose |
| --- | --- | --- |
| notebook\_create | 1 | Create isolated client notebook |
| source\_add<br>(text) | 1 | Inject synthesized company profile |
| source\_add<br>(url) | 1 | Add scraped website URLs |
| research\_start | 2 | Trigger deep web research |
| research\_status | 2 | Poll until research completes |
| research\_import | 2 | Batch-import discovered sources (chunks of 20) |
| notebook\_query | 3 | Generate briefing, intel, and research docs |
| studio\_create | 3 | Generate audio, infographic, quiz, flashcards, slides |
| studio\_status | 3 | Poll until studio artifacts complete |
| download\_artifact | 3 | Download audio/infographic/quiz/flashcards locally |