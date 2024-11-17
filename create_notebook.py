import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Temperature Parameter in LLMs\n\n"
        "## Introduction\n"
        "Temperature is a crucial parameter in Large Language Models that controls the randomness and creativity of the model's outputs. "
        "It is typically set between 0 and 1, where:\n\n"
        "- **Temperature = 0**: The model becomes deterministic, always choosing the most likely next token\n"
        "- **Temperature = 1**: The model maintains the original probability distribution\n"
        "- **Temperature > 1**: The model increases randomness, making all token probabilities more uniform\n\n"
        'Think of temperature as a "creativity knob" - lower values make the model more focused and consistent, '
        "while higher values make it more creative and diverse."
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, temperature=0.7):\n'
        '    """Query Ollama with a specific temperature setting"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "temperature": temperature\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different temperature values affect the model's output. "
        "We'll use a creative writing prompt and observe the differences."
    ),
    nbf.v4.new_code_cell(
        'creative_prompt = "Write a one-sentence story about a mysterious door in the forest."\n\n'
        'print("Temperature = 0.0 (Very focused)")\n'
        'print(query_ollama(creative_prompt, temperature=0.0))\n'
        'print("\\nTemperature = 0.7 (Balanced)")\n'
        'print(query_ollama(creative_prompt, temperature=0.7))\n'
        'print("\\nTemperature = 1.5 (Very creative)")\n'
        'print(query_ollama(creative_prompt, temperature=1.5))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Choose temperature based on your use case:\n\n"
        "1. **Low Temperature (0.0 - 0.3)**\n"
        "   - Fact-based QA\n"
        "   - Code generation\n"
        "   - Logic problems\n"
        "   - When consistency is crucial\n\n"
        "2. **Medium Temperature (0.4 - 0.7)**\n"
        "   - General conversation\n"
        "   - Text summarization\n"
        "   - Most default use cases\n\n"
        "3. **High Temperature (0.8 - 1.5)**\n"
        "   - Creative writing\n"
        "   - Brainstorming\n"
        "   - Generating diverse ideas\n"
        "   - When uniqueness is valued\n\n"
        "Remember: Higher temperature values increase diversity but may also increase the likelihood of errors or hallucinations."
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/01_temperature.ipynb")
