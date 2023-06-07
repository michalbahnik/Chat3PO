from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationEntityMemory

from chat3po.prompt_templates import C3PO_PROMPT_TEMPLATE


class Chat3PO:
    def __init__(self, llm: str = "openai", api_key: str = ""):
        if llm == "openai":
            self._llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
        else:
            raise ValueError(f"LLM '{llm}' model not supported.")

        self._memory = ConversationEntityMemory(llm=self._llm)

        self._conversation = ConversationChain(
            llm=self._llm,
            prompt=C3PO_PROMPT_TEMPLATE,
            memory=self._memory,
        )

    def run(self, input_: str):
        return self._conversation.run(input_)
