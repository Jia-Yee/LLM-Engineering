import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Max Tokens Parameter in LLMs\n\n"
        "## Introduction\n"
        "The max_tokens parameter controls the maximum length of the model's output in tokens. "
        "It acts as a safety limit to prevent unnecessarily long responses and helps manage "
        "computational resources.\n\n"
        "Key aspects:\n"
        "- **Token**: A piece of text (usually 3-4 characters in English)\n"
        "- **Default**: Usually model-specific (e.g., 2048 for many models)\n"
        "- **Range**: From 1 to model's context window size\n\n"
        "Understanding max_tokens is crucial for:\n"
        "- Controlling response length\n"
        "- Managing API costs\n"
        "- Ensuring consistent output sizes"
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, max_tokens=100):\n'
        '    """Query Ollama with a specific max_tokens setting"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "num_predict": max_tokens  # Ollama uses num_predict for max_tokens\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different max_tokens values affect the model's output length. "
        "We'll use the same prompt with different token limits to demonstrate the impact."
    ),
    nbf.v4.new_code_cell(
        'summary_prompt = "Explain how neural networks work."\n\n'
        'print("Max Tokens = 20 (Very brief)")\n'
        'print(query_ollama(summary_prompt, max_tokens=20))\n'
        'print("\\nMax Tokens = 50 (Concise)")\n'
        'print(query_ollama(summary_prompt, max_tokens=50))\n'
        'print("\\nMax Tokens = 200 (Detailed)")\n'
        'print(query_ollama(summary_prompt, max_tokens=200))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose max_tokens based on your use case:\n\n"
        "1. **Short Responses (10-30 tokens)**\n"
        "   - Quick answers\n"
        "   - Single-sentence responses\n"
        "   - Command generation\n\n"
        "2. **Medium Responses (50-100 tokens)**\n"
        "   - Paragraphs\n"
        "   - Brief explanations\n"
        "   - Summaries\n\n"
        "3. **Long Responses (200+ tokens)**\n"
        "   - Detailed explanations\n"
        "   - Content generation\n"
        "   - Complex analysis\n\n"
        "**Tips:**\n"
        "- Always set max_tokens to prevent runaway generation\n"
        "- Consider token costs in production environments\n"
        "- Remember that max_tokens is an upper limit, not a target\n"
        "- Balance between completeness and conciseness\n"
        "- Account for different languages (some use more tokens per word)"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/04_max_tokens.ipynb")
