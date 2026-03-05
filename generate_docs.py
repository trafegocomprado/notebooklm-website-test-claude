import subprocess
import json
import os

folder_name = "Meeting Prep - Digital Silk"
os.makedirs(folder_name, exist_ok=True)
nb_id = "c1897d48-acc3-4ebc-be2f-f8ce8f4abdae"

def query_nb(nb_id, question, output_file):
    print(f"Generating {output_file}...")
    cmd = ["nlm", "notebook", "query", nb_id, question, "--json"]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    try:
        data = json.loads(result.stdout)
        with open(os.path.join(folder_name, output_file), "w", encoding="utf-8") as f:
            f.write(data.get("text", result.stdout))
        print("Success.")
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        print("Output was:", result.stdout[:200])

q1 = "Create a comprehensive executive pre-meeting briefing document with these exact sections: 1) Company Overview (background, size, leadership, financials, business model, core products, key clients, recent developments, meeting context), 2) Competitive Landscape (name each competitor, their approach, and the client's advantage), 3) Market Opportunity (specific dollar figures, growth rates, and government initiatives), 4) Key Talking Points (numbered, actionable conversation starters), 5) Handling Objections (table format with Objection and Response columns), 6) Recommended Next Steps (3 concrete follow-up actions)."
query_nb(nb_id, q1, "01_briefing_doc.md")

q2 = "Write a deep research report summarizing the macro trends affecting this company's industry over the next 2 years. Include a table of the top 10 most important sources discovered, with columns for Source Name and Why It Matters. Then summarize the key themes assessed."
query_nb(nb_id, q2, "02_deep_research_report.md")

q3 = "Create a rapid competitive intelligence cheat sheet formatted as: Top 3 Things to Know (each with a bold headline, 3-4 bullet points of evidence, and a 'Your angle' recommendation), followed by a 'Market Numbers to Drop in Conversation' section listing 7-10 specific statistics with dollar signs and percentages."
query_nb(nb_id, q3, "03_competitive_intel.md")
