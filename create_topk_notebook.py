import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Top-k Parameter in LLMs\n\n"
        "## Introduction\n"
        "Top-k is a parameter that limits token selection to the k most likely next tokens. "
        "It provides direct control over the size of the candidate pool for next token selection, "
        "unlike top-p which works with cumulative probabilities.\n\n"
        "- **Top-k = 1**: Only the single most probable token is considered (greedy)\n"
        "- **Top-k = 10**: Consider only the 10 most probable tokens\n"
        "- **Top-k = 50**: Consider the 50 most probable tokens\n\n"
        "This parameter is particularly useful when you want explicit control over how many options "
        "the model considers at each step of text generation."
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, top_k=40):\n'
        '    """Query Ollama with a specific top_k setting"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "top_k": top_k\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different top-k values affect the model's output. "
        "We'll use a creative task to demonstrate how limiting token selection impacts generation."
    ),
    nbf.v4.new_code_cell(
        'creative_prompt = "Describe a futuristic city in one sentence."\n\n'
        'print("Top-k = 1 (Most probable only)")\n'
        'print(query_ollama(creative_prompt, top_k=1))\n'
        'print("\\nTop-k = 10 (Limited diversity)")\n'
        'print(query_ollama(creative_prompt, top_k=10))\n'
        'print("\\nTop-k = 50 (More options)")\n'
        'print(query_ollama(creative_prompt, top_k=50))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose top-k based on your use case:\n\n"
        "1. **Low Top-k (1-5)**\n"
        "   - When you need very focused, deterministic outputs\n"
        "   - For tasks requiring high precision\n"
        "   - When consistency is crucial\n\n"
        "2. **Medium Top-k (10-20)**\n"
        "   - For balanced text generation\n"
        "   - When some variation is desired\n"
        "   - For general conversation\n\n"
        "3. **High Top-k (40-100)**\n"
        "   - For creative writing\n"
        "   - When exploring different possibilities\n"
        "   - For brainstorming sessions\n\n"
        "**Tips:**\n"
        "- Can be combined with temperature and top-p\n"
        "- Start with top-k = 40 for general use\n"
        "- Lower values create more focused but potentially repetitive text\n"
        "- Higher values allow for more diverse outputs but may include less relevant tokens"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/03_top_k.ipynb")
