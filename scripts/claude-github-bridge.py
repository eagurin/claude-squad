#!/usr/bin/env python3
"""
Claude GitHub Bridge - использует локальный Claude для обработки GitHub запросов
Требует запущенный claude-code-bridge.py
"""

import os
import sys
import json
import requests
from pathlib import Path

# Конфигурация
CLAUDE_BRIDGE_URL = "http://localhost:5858/v1/chat/completions"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GITHUB_REPOSITORY")

def process_github_request(prompt: str, context: dict) -> str:
    """Обрабатывает запрос через локальный Claude bridge"""
    
    # Формируем контекст для Claude
    system_prompt = f"""You are a helpful coding assistant working on the {REPO} repository.
You are responding to a GitHub issue or PR comment.
Follow the project guidelines in CLAUDE.md if present.
Be concise and helpful. Format your response in GitHub-flavored markdown."""
    
    # Вызываем локальный Claude bridge
    response = requests.post(CLAUDE_BRIDGE_URL, json={
        "model": "claude-3-opus-20240229",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4000
    })
    
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error calling Claude bridge: {response.status_code}"

def main():
    # Читаем промпт из файла
    prompt_file = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-prompt.txt"
    with open(prompt_file, 'r') as f:
        prompt = f.read().strip()
    
    # Обрабатываем через Claude
    response = process_github_request(prompt, {
        "repo": REPO,
        "token": GITHUB_TOKEN
    })
    
    # Сохраняем ответ
    with open("/tmp/claude-response.txt", 'w') as f:
        f.write(response)
    
    print("Response generated successfully")

if __name__ == "__main__":
    main()