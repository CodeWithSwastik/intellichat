# IntelliChat

A convenient wrapper for OpenAI's Chat Completion API.

## Example

Simplest Use Case
```python
from intellichat import ChatBot

bot = ChatBot(api_key="sk-...")

response = bot.get_response("Hi!")

print(response)
```
