import os
from autogen import ConversableAgent

os.environ["OPENAI_API_KEY"] = "dummy_key"  

llm_config_local = {
    "config_list": [{
        "model": "gemma-2-2b-it-GGUF/gemma-2-2b-it-Q4_K_M.gguf",  
        "base_url": "http://localhost:1234/v1/completions",  
        "price": [0, 0]  
    }]
}

general_agent = ConversableAgent(
    "weather_forecaster",
    llm_config=llm_config_local,
    code_execution_config=False,  
    function_map=None,  
    human_input_mode="NEVER"
)

async def get_general_response(query):
    try:
        response = await general_agent.a_initiate_chat(message=query, recipient=general_agent)
        return f"General Query Response: {response}"
    except Exception as e:
        return f"Error in processing the query: {e}"
