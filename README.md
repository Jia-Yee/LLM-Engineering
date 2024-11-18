# LLM Engineering - Parameter Documentation

A comprehensive guide to LLM parameters using Jupyter notebooks, Ollama, and llama3.

## Overview

This repository provides detailed documentation and practical examples for understanding and effectively using various LLM (Large Language Model) parameters. Through interactive Jupyter notebooks, you'll learn how each parameter affects model behavior and performance.

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

## Prerequisites

- Python 3.8 or higher
- Jupyter Notebook
- Ollama
- Basic understanding of LLMs

## Setup

1. Install requirements:
```bash
pip install jupyter nbformat
```

2. Install Ollama and download Llama3:
```bash
# Follow Ollama installation instructions at https://ollama.ai
ollama pull llama3
```

3. Run Jupyter:
```bash
jupyter notebook
```

Navigate to `notebooks/prompt-engineering/parameters/` to explore the parameter documentation.

## Repository Structure

- `notebooks/prompt-engineering/parameters/`: Jupyter notebooks documenting each parameter

Each notebook includes:
- Parameter introduction
- Code examples
- Best practices
- Use cases

## Usage Examples

Here's a quick example of how to use the notebooks:

1. Open the desired parameter notebook (e.g., `temperature.ipynb`)
2. Follow the interactive examples
3. Experiment with different parameter values
4. Observe the effects on model outputs

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your PR description clearly describes the changes and links to any relevant issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Ollama team for providing the LLM infrastructure
- Contributors who have helped improve the documentation
