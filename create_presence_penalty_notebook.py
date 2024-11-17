import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Presence Penalty Parameter in LLMs\n\n"
        "## Introduction\n"
        "The presence_penalty parameter helps control repetition in model outputs by penalizing tokens "
        "that have already appeared in the text. This encourages the model to explore new topics and "
        "avoid getting stuck in repetitive patterns.\n\n"
        "Key aspects:\n"
        "- **Range**: Usually -2.0 to 2.0\n"
        "- **Positive values**: Encourage the model to talk about new topics\n"
        "- **Negative values**: Allow more repetition\n"
        "- **Zero**: No penalty applied\n\n"
        "Understanding presence_penalty is crucial for:\n"
        "- Reducing redundant information\n"
        "- Encouraging topic exploration\n"
        "- Maintaining natural conversation flow"
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, presence_penalty=0.0):\n'
        '    """Query Ollama with a specific presence_penalty setting"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "presence_penalty": presence_penalty\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different presence_penalty values affect the model's tendency to repeat information. "
        "We'll use a prompt that naturally invites repetition to demonstrate the impact."
    ),
    nbf.v4.new_code_cell(
        'repetitive_prompt = "List 5 benefits of exercise. For each benefit, provide a detailed explanation."\n\n'
        'print("Presence Penalty = -1.0 (More repetition allowed)")\n'
        'print(query_ollama(repetitive_prompt, presence_penalty=-1.0))\n'
        'print("\\nPresence Penalty = 0.0 (Neutral)")\n'
        'print(query_ollama(repetitive_prompt, presence_penalty=0.0))\n'
        'print("\\nPresence Penalty = 1.0 (Less repetition)")\n'
        'print(query_ollama(repetitive_prompt, presence_penalty=1.0))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose presence_penalty based on your use case:\n\n"
        "1. **High Penalty (0.7 to 2.0)**\n"
        "   - Creative writing\n"
        "   - Brainstorming sessions\n"
        "   - Exploring diverse topics\n\n"
        "2. **Medium Penalty (0.3 to 0.7)**\n"
        "   - General conversation\n"
        "   - Content generation\n"
        "   - Explanations\n\n"
        "3. **Low or Negative Penalty (-2.0 to 0.3)**\n"
        "   - Technical documentation\n"
        "   - When consistency is important\n"
        "   - Formal writing\n\n"
        "**Tips:**\n"
        "- Start with presence_penalty = 0.0 and adjust based on needs\n"
        "- Higher values can make outputs more diverse but potentially less focused\n"
        "- Lower values maintain consistency but might lead to repetition\n"
        "- Consider combining with frequency_penalty for fine-tuned control\n"
        "- Monitor output quality when using extreme values"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/05_presence_penalty.ipynb")
