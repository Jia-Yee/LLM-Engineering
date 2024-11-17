import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Frequency Penalty Parameter in LLMs\n\n"
        "## Introduction\n"
        "The frequency_penalty parameter helps control the diversity of the model's output by "
        "penalizing tokens based on their frequency in the generated text. Unlike presence_penalty "
        "which penalizes tokens that appear at all, frequency_penalty scales its penalty based on "
        "how often tokens have been used.\n\n"
        "Key aspects:\n"
        "- **Range**: Usually -2.0 to 2.0\n"
        "- **Positive values**: Decrease likelihood of frequent tokens\n"
        "- **Negative values**: Increase likelihood of frequent tokens\n"
        "- **Zero**: No frequency-based adjustments\n\n"
        "Understanding frequency_penalty is crucial for:\n"
        "- Controlling vocabulary diversity\n"
        "- Managing writing style consistency\n"
        "- Balancing repetition and variation"
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, frequency_penalty=0.0):\n'
        '    """Query Ollama with a specific frequency_penalty setting"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "frequency_penalty": frequency_penalty\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different frequency_penalty values affect the model's word choice "
        "and vocabulary diversity. We'll use a prompt that naturally invites using similar "
        "vocabulary to demonstrate the impact."
    ),
    nbf.v4.new_code_cell(
        'vocabulary_prompt = "Write a paragraph about artificial intelligence using technical terms."\n\n'
        'print("Frequency Penalty = -1.0 (More repetition of terms)")\n'
        'print(query_ollama(vocabulary_prompt, frequency_penalty=-1.0))\n'
        'print("\\nFrequency Penalty = 0.0 (Neutral)")\n'
        'print(query_ollama(vocabulary_prompt, frequency_penalty=0.0))\n'
        'print("\\nFrequency Penalty = 1.0 (More diverse vocabulary)")\n'
        'print(query_ollama(vocabulary_prompt, frequency_penalty=1.0))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose frequency_penalty based on your use case:\n\n"
        "1. **High Penalty (0.7 to 2.0)**\n"
        "   - Creative writing\n"
        "   - Diverse vocabulary needs\n"
        "   - Exploratory content\n\n"
        "2. **Medium Penalty (0.3 to 0.7)**\n"
        "   - General writing\n"
        "   - Balanced vocabulary\n"
        "   - Most conversational tasks\n\n"
        "3. **Low or Negative Penalty (-2.0 to 0.3)**\n"
        "   - Technical writing\n"
        "   - Consistent terminology\n"
        "   - Educational content\n\n"
        "**Tips:**\n"
        "- Start with frequency_penalty = 0.0 and adjust based on needs\n"
        "- Higher values increase vocabulary diversity but may reduce precision\n"
        "- Lower values maintain consistent terminology but might feel repetitive\n"
        "- Can be used with presence_penalty for fine-tuned control\n"
        "- Consider the domain-specific needs (technical vs creative)\n"
        "- Monitor coherence when using extreme values"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/06_frequency_penalty.ipynb")
