## Project: AutoGen with PyAutoGen and Litellm

### Overview
This project utilizes PyAutoGen and Litellm, along with the AutoGen framework, to develop LLM applications enabling conversational interactions between multiple agents. AutoGen agents are customizable, conversable, and support human participation. The project focuses on task-solving abilities through the integration of various LLMs, human inputs, and tools.

### Installation
1. Install Ollama
    ```
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2. Install dependencies:
    ```
    pip install pyautogen litellm[proxy]
    ```

### Usage
1. Run Litellm with the desired model at 2 diferent shell prompt:
    ```
    litellm --model ollama/codellama
    litellm --model ollama/mistral
    ```
2. Rename the ports in the configuration file:
    - Open the configuration file (`config.json` or similar).
    - Find the `"base_url"` field.
    - Change the port number to your desired value: `"http://0.0.0.0:portnumber"`.

### Additional Resources
- [AutoGen Project](https://www.microsoft.com/en-us/research/project/autogen/)
- [AutoGen GitHub Repository](https://github.com/microsoft/autogen)
- [Ollama Website](https://ollama.com/)

For more detailed instructions and information, refer to the respective documentation provided by PyAutoGen, Litellm, and the AutoGen framework.

Feel free to contribute to the project or report any issues on the GitHub repository.