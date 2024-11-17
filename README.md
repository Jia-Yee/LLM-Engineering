# LLM Engineering - Parameter Documentation

A comprehensive guide to LLM parameters using Jupyter notebooks, Ollama, and Llama2.

## Parameters Covered

1. Temperature (Randomness/Creativity)
2. Top-p (Nucleus Sampling)
3. Top-k (Token Selection)
4. Max Tokens (Output Length)
5. Presence Penalty (Repetition Control)
6. Frequency Penalty (Diversity)
7. Stop Sequences (Output Termination)
8. Context Window (Input Length)
9. System Prompt (Behavior Control)
10. Seed (Reproducibility)

## Setup

1. Install requirements:
```bash
pip install jupyter nbformat
```

2. Install Ollama and download Llama2:
```bash
# Follow Ollama installation instructions at https://ollama.ai
ollama pull llama2
```

3. Run Jupyter:
```bash
jupyter notebook
```

Navigate to `notebooks/prompt-engineering/parameters/` to explore the parameter documentation.

## Structure

- `notebooks/prompt-engineering/parameters/`: Jupyter notebooks documenting each parameter
- `create_*.py`: Python scripts for generating the notebooks

Each notebook includes:
- Parameter introduction
- Code examples
- Best practices
- Use cases

