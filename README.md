# Autogen-Agents-with-Ollama-Models
## Dependencies
pyautogen
litellm

## Installation
conda create -n autogen python=3.11
conda activate autogen

pip install pyautogen
pip install litellm

### Ollama Models on local
ollama run codellama

ollama run mistral

### Using litellm to reach ollama models
litellm --model ollama/mistral

litellm --model ollama/codellama

![Ekran Görüntüsü (279)](https://github.com/user-attachments/assets/971095b2-6ee9-4fc4-8bed-8e7c26786a6d)
