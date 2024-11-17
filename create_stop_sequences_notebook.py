import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Stop Sequences Parameter in LLMs\n\n"
        "## Introduction\n"
        "Stop sequences are specific strings that tell the model when to stop generating text. "
        "They act as termination signals, allowing fine-grained control over where the model's "
        "output should end.\n\n"
        "Key aspects:\n"
        "- **Format**: Can be single characters, words, or phrases\n"
        "- **Multiple stops**: Can specify multiple stop sequences\n"
        "- **Case sensitivity**: Usually case-sensitive\n"
        "- **Whitespace**: Handling depends on implementation\n\n"
        "Understanding stop sequences is crucial for:\n"
        "- Controlling output boundaries\n"
        "- Maintaining format consistency\n"
        "- Implementing structured outputs"
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, stop=None):\n'
        '    """Query Ollama with specific stop sequences"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "stop": stop if stop else []\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different stop sequences affect the model's output. "
        "We'll use various prompts and stop sequences to demonstrate their impact."
    ),
    nbf.v4.new_code_cell(
        'list_prompt = "List the first 5 planets from the sun:\\n1. Mercury\\n2. Venus\\n3."\n\n'
        'print("No stop sequence:")\n'
        'print(query_ollama(list_prompt))\n'
        'print("\\nStop at newline (\'\\n\'):")\n'
        'print(query_ollama(list_prompt, stop=["\\n"]))\n'
        'print("\\nStop at number (\'4.\'):")\n'
        'print(query_ollama(list_prompt, stop=["4."]))'
    ),
    nbf.v4.new_code_cell(
        'qa_prompt = "Q: What is machine learning?\\nA: "\n\n'
        'print("Stop at next question (\'Q:\'):")\n'
        'print(query_ollama(qa_prompt, stop=["Q:"]))\n'
        'print("\\nStop at multiple sequences (\'Q:\' or \'\\n\'):")\n'
        'print(query_ollama(qa_prompt, stop=["Q:", "\\n"]))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose stop sequences based on your use case:\n\n"
        "1. **Structured Output**\n"
        "   - Use delimiters like `###` or `===`\n"
        "   - Consider using unique tokens\n"
        "   - Match start/end patterns\n\n"
        "2. **Conversational**\n"
        "   - Use turn indicators (`User:`, `Assistant:`)\n"
        "   - Consider newlines as stops\n"
        "   - Use clear dialogue markers\n\n"
        "3. **List Generation**\n"
        "   - Use numbering patterns\n"
        "   - Consider item separators\n"
        "   - Use consistent formatting\n\n"
        "**Tips:**\n"
        "- Keep stop sequences unique and unambiguous\n"
        "- Test stop sequences with sample outputs\n"
        "- Consider case sensitivity\n"
        "- Use multiple stop sequences when needed\n"
        "- Be careful with common words as stops\n"
        "- Document stop sequences for reproducibility"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/07_stop_sequences.ipynb")
