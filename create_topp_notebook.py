import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Top-p (Nucleus Sampling) Parameter in LLMs\n\n"
        "## Introduction\n"
        "Top-p, also known as nucleus sampling, is a text generation parameter that helps control the randomness "
        "of the model's output by considering only the most likely tokens whose cumulative probability exceeds "
        "the specified top-p value.\n\n"
        "- **Top-p = 0.1**: Very focused, considers only the most probable tokens\n"
        "- **Top-p = 0.5**: Balanced, considers moderately probable tokens\n"
        "- **Top-p = 1.0**: Considers all possible tokens\n\n"
        "Unlike temperature, which scales probabilities, top-p truncates the probability distribution to only "
        "include the most likely tokens up to the cumulative probability threshold."
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, top_p=0.9):\n'
        '    """Query Ollama with a specific top_p setting"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "top_p": top_p\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different top-p values affect the model's output. "
        "We'll use a creative writing prompt and observe the differences in token selection."
    ),
    nbf.v4.new_code_cell(
        'creative_prompt = "List three possible uses for a magical crystal ball."\n\n'
        'print("Top-p = 0.1 (Very focused)")\n'
        'print(query_ollama(creative_prompt, top_p=0.1))\n'
        'print("\\nTop-p = 0.5 (Balanced)")\n'
        'print(query_ollama(creative_prompt, top_p=0.5))\n'
        'print("\\nTop-p = 0.9 (More diverse)")\n'
        'print(query_ollama(creative_prompt, top_p=0.9))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose top-p based on your use case:\n\n"
        "1. **Low Top-p (0.1 - 0.3)**\n"
        "   - Technical writing\n"
        "   - Factual responses\n"
        "   - When precision is crucial\n\n"
        "2. **Medium Top-p (0.4 - 0.7)**\n"
        "   - General conversation\n"
        "   - Content generation\n"
        "   - Balanced creativity and coherence\n\n"
        "3. **High Top-p (0.8 - 1.0)**\n"
        "   - Creative writing\n"
        "   - Brainstorming\n"
        "   - When diversity is important\n\n"
        "**Tips:**\n"
        "- Top-p can be used alongside temperature for fine-tuned control\n"
        "- Start with top-p = 0.9 for general use cases\n"
        "- Lower values create more predictable but potentially repetitive text\n"
        "- Higher values allow for more creative but potentially less focused outputs"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/02_top_p.ipynb")
