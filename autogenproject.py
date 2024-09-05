import autogen

# CONFIGURATION
config_list_mistral = [
    {
        'base_url': "http://localhost:4000",
        'api_key': "NULL"
    }
]

config_list_codellama = [
    {
        'base_url': "http://localhost:24709",
        'api_key': "NULL"
    }
]
# LLM Configurations
llm_config_mistral = {
    "config_list": config_list_mistral,
    "model": "mistral-7b"  
}

llm_config_codellama = {
    "config_list": config_list_codellama,
    "model": "codellama-7b"  
}


user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=2,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "groupchat"},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)
coderllama = autogen.AssistantAgent(
    name="codellama",
    llm_config=llm_config_codellama,
    system_message="""You are a python expert. Write codes that user_proxy wanted from you""",
)

executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="""Executor. Execute the code written by the codellama and report the result.""",
    llm_config=llm_config_codellama,
    human_input_mode="NEVER",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "paper",
        "use_docker": True,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
)
groupchat = autogen.GroupChat(
    agents=[user_proxy, coderllama, executor], messages=[], max_round=10
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_mistral)

user_proxy.initiate_chat(
    manager,
    message="""Create an basic tic-tac-toe app using Python""",
)
