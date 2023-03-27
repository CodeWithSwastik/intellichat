import openai
from aiohttp import ClientSession
from typing import Dict, List, Optional, Union

class ChatBotConfig:
    def __init__(self, *, system_prompt: Optional[str] = None, **details: str) -> None:
        self.details: Dict[str, str] = details
        self.system_prompt: str = system_prompt or self.generate_system_prompt()

    def generate_system_prompt(self) -> str:
        prompt = "You are an AI Chatbot."
        for key, value in self.details.items():
            prompt += f" Your {key} is {value}." 
        return prompt

class ChatBot:
    def __init__(
            self, 
            api_key: str, 
            model: str = "gpt-3.5-turbo", 
            config: Optional[ChatBotConfig] = None, 
            conversation_history: Optional[List[Dict[str, Union[str, int]]]] = None, 
            async_mode: bool = False,
            session: Optional[ClientSession] = None
        ) -> None:
        self.api_key: str = api_key
        openai.api_key: str = api_key

        self.model: str = model
        self.config: ChatBotConfig = config or ChatBotConfig()
        self.conversation_history: List[Dict[str, Union[str, int]]] = conversation_history or []

            
        if async_mode:
            self.session: ClientSession = session or ClientSession()
            openai.aiosession.set(self.session)
            self.get_response = self.get_async_response


    def get_response(self, message: str, user: str = "User", **kwargs) -> str:
        self.conversation_history.append({"author": user, "message": message})

        completion: openai.ChatCompletion = openai.ChatCompletion.create(model=self.model, messages=self._get_messages(), **kwargs)
        response: str = completion.choices[0].message.content
        self.conversation_history.append({"author": 'Bot', "message": response})
        return response

    async def get_async_response(self, message: str, user: str = "User", **kwargs) -> None:
        self.conversation_history.append({"author": user, "message": message})

        completion: openai.ChatCompletion = await openai.ChatCompletion.acreate(model=self.model, messages=self._get_messages(), **kwargs)
        response: str = completion.choices[0].message.content
        self.conversation_history.append({"author": 'Bot', "message": response})
        return response
        
    def _get_messages(self) -> List[Dict[str, str]]:
        conversation: List[Dict[str, str]] = [{"role": "system", "content": self.config.system_prompt}]
        for r in self.conversation_history:
            d: Dict[str, Union[str, int]] = {"role": "assistant" if r['author'] == 'Bot' else 'user', "content": r['message']}
            if r['author'] not in ('Bot', 'User'):
                d['content'] = f"{r['author']} said '{r['message']}'"
            conversation.append(d)

        chars = sum(len(d['content']) for d in conversation)   
        while chars > 4000 and len(conversation) > 1:
            conversation.pop(1)
            chars = sum(len(d['content']) for d in conversation)   

        return conversation