import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# System Prompt Parameter in LLMs\n\n"
        "## Introduction\n"
        "The system prompt is a special instruction set that defines the model's behavior, "
        "personality, and operational constraints. It acts as a foundation for how the model "
        "should interpret and respond to subsequent user prompts.\n\n"
        "Key aspects:\n"
        "- **Persistence**: Affects all following interactions\n"
        "- **Scope**: Can define roles, constraints, and behaviors\n"
        "- **Priority**: Usually takes precedence over user prompts\n"
        "- **Format**: Natural language instructions\n\n"
        "Understanding system prompts is crucial for:\n"
        "- Controlling model behavior\n"
        "- Ensuring consistent responses\n"
        "- Implementing safety guardrails\n"
        "- Defining specialized roles"
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, system=""):\n'
        '    """Query Ollama with a specific system prompt"""\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps({\n'
        '            "model": "llama2",\n'
        '            "prompt": prompt,\n'
        '            "system": system\n'
        '        })\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how different system prompts affect the model's behavior and responses. "
        "We'll use the same user prompt with different system prompts to demonstrate the impact."
    ),
    nbf.v4.new_code_cell(
        'question = "What do you think about artificial intelligence?"\n\n'
        '# Default behavior\n'
        'print("Default (No system prompt):")\n'
        'print(query_ollama(question))\n\n'
        '# Technical expert\n'
        'technical_system = "You are a technical expert in AI. Provide detailed, technical responses."\n'
        'print("\\nTechnical Expert:")\n'
        'print(query_ollama(question, technical_system))\n\n'
        '# Simplified explainer\n'
        'simple_system = "You are an educator explaining concepts to beginners. Use simple language and analogies."\n'
        'print("\\nSimplified Explainer:")\n'
        'print(query_ollama(question, simple_system))\n\n'
        '# Critical perspective\n'
        'critical_system = "You are a technology ethicist. Consider both benefits and potential risks."\n'
        'print("\\nCritical Perspective:")\n'
        'print(query_ollama(question, critical_system))'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "Design system prompts based on your use case:\n\n"
        "1. **Role Definition**\n"
        "   - Be specific about expertise\n"
        "   - Define communication style\n"
        "   - Set knowledge boundaries\n\n"
        "2. **Behavioral Control**\n"
        "   - Establish response format\n"
        "   - Define tone and personality\n"
        "   - Set ethical guidelines\n\n"
        "3. **Safety and Constraints**\n"
        "   - Implement content filters\n"
        "   - Define forbidden topics\n"
        "   - Set output limitations\n\n"
        "**Tips:**\n"
        "- Keep system prompts clear and concise\n"
        "- Test with various user inputs\n"
        "- Layer instructions logically\n"
        "- Include error handling guidance\n"
        "- Document system prompts\n"
        "- Regular validation and updates"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/09_system_prompt.ipynb")
