import nbformat as nbf

nb = nbf.v4.new_notebook()

# Create cells
cells = [
    nbf.v4.new_markdown_cell(
        "# Seed Parameter in LLMs\n\n"
        "## Introduction\n"
        "The seed parameter is a crucial tool for achieving reproducibility in LLM outputs. "
        "It controls the randomness in the model's generation process, allowing you to get "
        "consistent results across multiple runs with the same input.\n\n"
        "Key aspects:\n"
        "- **Determinism**: Same seed + same prompt = same output\n"
        "- **Testing**: Essential for debugging and validation\n"
        "- **Experimentation**: Enables controlled comparisons\n"
        "- **Quality Assurance**: Helps in maintaining output consistency\n\n"
        "Understanding seed management is important for:\n"
        "- Debugging model behavior\n"
        "- Scientific experiments\n"
        "- Quality assurance testing\n"
        "- Production deployments requiring consistency"
    ),
    nbf.v4.new_code_cell(
        'import json\n'
        'from subprocess import Popen, PIPE\n\n'
        'def query_ollama(prompt, seed=None):\n'
        '    """Query Ollama with a specific seed"""\n'
        '    payload = {\n'
        '        "model": "llama2",\n'
        '        "prompt": prompt\n'
        '    }\n'
        '    if seed is not None:\n'
        '        payload["seed"] = seed\n\n'
        '    cmd = [\n'
        '        "curl",\n'
        '        "http://localhost:11434/api/generate",\n'
        '        "-d",\n'
        '        json.dumps(payload)\n'
        '    ]\n\n'
        '    process = Popen(cmd, stdout=PIPE, stderr=PIPE)\n'
        '    output, _ = process.communicate()\n\n'
        '    responses = [json.loads(line) for line in output.decode().strip().split("\\n")]\n'
        '    return "".join(r.get("response", "") for r in responses)'
    ),
    nbf.v4.new_markdown_cell(
        "## Examples\n\n"
        "Let's explore how seeds affect model outputs by running the same prompt multiple times "
        "with different seed configurations."
    ),
    nbf.v4.new_code_cell(
        'prompt = "Write a short story about a robot learning to paint."\n\n'
        '# No seed (random outputs)\n'
        'print("Without seed (Run 1):")\n'
        'print(query_ollama(prompt))\n'
        'print("\\nWithout seed (Run 2):")\n'
        'print(query_ollama(prompt))\n\n'
        '# Fixed seed (consistent outputs)\n'
        'seed_value = 42\n'
        'print(f"\\nWith seed {seed_value} (Run 1):")\n'
        'print(query_ollama(prompt, seed_value))\n'
        'print(f"\\nWith seed {seed_value} (Run 2):")\n'
        'print(query_ollama(prompt, seed_value))\n\n'
        '# Different seed value\n'
        'different_seed = 123\n'
        'print(f"\\nWith different seed {different_seed}:")\n'
        'print(query_ollama(prompt, different_seed))'
    ),
    nbf.v4.new_markdown_cell(
        "## Testing Reproducibility\n\n"
        "Let's demonstrate how seeds can be used for testing and debugging by comparing "
        "outputs across different prompts and configurations."
    ),
    nbf.v4.new_code_cell(
        '# Test different prompts with same seed\n'
        'test_seed = 42\n'
        'prompts = [\n'
        '    "Explain quantum computing",\n'
        '    "Write a haiku about spring",\n'
        '    "Describe a sunset"\n'
        ']\n\n'
        'for prompt in prompts:\n'
        '    print(f"Prompt: {prompt}")\n'
        '    print("First run:")\n'
        '    print(query_ollama(prompt, test_seed))\n'
        '    print("\\nSecond run (should be identical):")\n'
        '    print(query_ollama(prompt, test_seed))\n'
        '    print("\\n" + "-"*50 + "\\n")'
    ),
    nbf.v4.new_markdown_cell(
        "## Best Practices\n\n"
        "1. **Development and Testing**\n"
        "   - Use fixed seeds during development\n"
        "   - Document seed values in test cases\n"
        "   - Verify reproducibility across environments\n\n"
        "2. **Production Deployment**\n"
        "   - Consider when to use fixed seeds\n"
        "   - Balance consistency vs. diversity\n"
        "   - Implement seed management strategy\n\n"
        "3. **Experimentation**\n"
        "   - Use seeds for A/B testing\n"
        "   - Control for randomness in experiments\n"
        "   - Document seed values for reproducibility\n\n"
        "**Tips:**\n"
        "- Always log seed values used in production\n"
        "- Use different seeds for different use cases\n"
        "- Consider seed ranges for controlled variation\n"
        "- Document seed-dependent behaviors\n"
        "- Test with multiple seed values\n"
        "- Include seed management in monitoring"
    )
]

nb.cells = cells

# Create the directories if they don't exist
import os
os.makedirs("notebooks/prompt-engineering/parameters", exist_ok=True)

# Write the notebook
nbf.write(nb, "notebooks/prompt-engineering/parameters/10_seed.ipynb")
