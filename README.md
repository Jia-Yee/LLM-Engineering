# LLM Engineering - Learning by Doing

A practical guide to becoming a prompt engineer through hands-on learning with real recruitment scenarios. Perfect for learning LLM prompting over a weekend! This repository was created with help from [devin.ai](https://devin.ai/).

## Overview

This repository provides a hands-on approach to mastering prompt engineering through practical examples in recruitment scenarios. You'll learn by doing, working through interactive Jupyter notebooks that demonstrate how to:
- Analyze resumes and job descriptions
- Create targeted recruitment prompts
- Generate effective interview questions
- Evaluate candidate responses
- Assess cultural fit


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

## Repository Structure

The repository is organized into three main sections:

### 1. Introduction of Parameters
Core parameter notebooks for understanding LLM behavior:
- `01_temperature.ipynb`: Control randomness and creativity in responses
- `02_top_p.ipynb`: Nucleus sampling for balanced text generation
- `03_top_k.ipynb`: Token selection strategies for output control
- `04_max_tokens.ipynb`: Managing response length effectively
- `05_presence_penalty.ipynb`: Reducing repetition in outputs
- `06_frequency_penalty.ipynb`: Enhancing response diversity
- `07_stop_sequences.ipynb`: Controlling response termination
- `08_context_window.ipynb`: Managing input length and context
- `09_system_prompt.ipynb`: Defining model behavior and personality
- `10_seed.ipynb`: Ensuring reproducible outputs

### 2. Introduction of Prompting
Fundamental prompting concepts and techniques:
- `11_basic_parameters.ipynb`: Essential prompting parameters
- `12_advanced_parameters.ipynb`: Advanced parameter combinations
- `13_prompt_structure.ipynb`: Building effective prompt templates
- `14_prompt_tasks.ipynb`: Task-specific prompting strategies

### 3. Techniques
Advanced prompting methodologies:
- `15_zero_shot_prompting.ipynb`: Prompting without examples
- `16_few_shot_prompting.ipynb`: Learning from minimal examples
- `17_chain_of_thought_prompting.ipynb`: Step-by-step reasoning
- `18_automatic_reasoning_prompting.ipynb`: Self-guided problem solving
- `19_self_consistency_prompting.ipynb`: Maintaining consistent outputs
- `20_tree_of_thought_prompting.ipynb`: Exploring multiple reasoning paths

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
- [devin.ai](https://devin.ai/) for assistance in creating this repository
