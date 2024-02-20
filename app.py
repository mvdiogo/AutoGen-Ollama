import autogen
import socket

task = """
Write a python script to output numbers 1 to a randon number and then the user_proxy agent should run the script
"""

config_list_mistral = [
    {
        'base_url': 'http://0.0.0.0:8000',
        'api_key': 'NULL',
        'model': 'ollama/mistral',
    }
]

config_list_codellama = [
    {
        'base_url': 'http://0.0.0.0:34655',
        'api_key': 'NULL',
        'model': 'ollama/codellama',
    }
]

llm_config_mistral = {
    'config_list': config_list_mistral,
}

llm_config_codellama = {
    'config_list': config_list_codellama,
}

coder = autogen.AssistantAgent(name='Coder', llm_config=llm_config_codellama)

user_proxy = autogen.UserProxyAgent(
    name='user_proxy',
    human_input_mode='NEVER',
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get('content', '')
    .rstrip()
    .endswith('TERMINATE'),
    code_execution_config={'work_dir': 'web'},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)


def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', port))
            return True  # Port is available
        except OSError:
            return False  # Port is already in use


def main():
    blocked_ports = [8000, 34655]

    for port in blocked_ports:
        if is_port_open(port):
            print(f'Port {port} was not detected.')
            print(
                f"""  
            Please follow the 3 steps:
            1. Install the dependency (pip install pyautogen litellm[proxy]),
            2. rum litellm
                litellm --model ollama/codellama
                litellm --model ollama/mistral 
            3. rename the ports on 'base_url': 'http://0.0.0.0:portnumber',
            """
            )
            print('Finished checking ports.')
        else:
            user_proxy.initiate_chat(coder, message=task)


if __name__ == '__main__':
    main()
