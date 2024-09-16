import os
from autogen import ConversableAgent
os.environ["OPENAI_API_KEY"] = "dummy_key"


# Print the available methods for the class
agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": [{"model": "gemma-2-2b-it-GGUF/gemma-2-2b-it-Q4_K_M.gguf", "base_url": "http://localhost:1234/v1/completions"}]},
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER"
)

print(dir(agent))
