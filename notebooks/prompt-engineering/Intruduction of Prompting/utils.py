import requests
import json
import psutil
from IPython.display import Markdown, display

def check_system_memory():
    """Check if system has enough memory for the model"""
    available_memory = psutil.virtual_memory().available / (1024 * 1024 * 1024)  # Convert to GB
    required_memory = 8.4  # Required GB for llama2
    return available_memory >= required_memory, available_memory

def query_model(prompt, system_prompt=None, **kwargs):
    """Query the Ollama API with the given prompt and parameters"""
    try:
        # Check system memory
        has_memory, available_memory = check_system_memory()
        if not has_memory:
            return f"⚠️ Insufficient system memory. Available: {available_memory:.1f}GB, Required: 8.4GB. Please free up memory or use a smaller model."

        url = "http://localhost:11434/api/generate"
        data = {
            "model": "llama2",
            "prompt": prompt,
            **kwargs
        }

        if system_prompt:
            data["system"] = system_prompt

        response = requests.post(url, json=data)

        # Check if request was successful
        response.raise_for_status()

        # Parse response
        try:
            result = response.json()
            if "error" in result:
                return f"⚠️ API Error: {result['error']}"
            return result.get("response", "No response received")
        except json.JSONDecodeError:
            return f"⚠️ Invalid JSON response: {response.text[:200]}..."

    except requests.exceptions.ConnectionError:
        return "⚠️ Could not connect to Ollama API. Is Ollama running?"
    except requests.exceptions.RequestException as e:
        return f"⚠️ API request failed: {str(e)}"
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"

def display_example(title, prompt, system_prompt=None):
    """Display an example prompt and its response"""
    display(Markdown(f"### {title}"))
    display(Markdown(f"**Prompt:**\n{prompt}"))
    if system_prompt:
        display(Markdown(f"**System Prompt:**\n{system_prompt}"))
    response = query_model(prompt, system_prompt)
    display(Markdown(f"**Response:**\n{response}"))
