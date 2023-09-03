# Simulating a debate of LLM bots

This repository offers a minimal boilerplate code for participating in the IICCSSS 2023 hackathon **topic C "Simulating a debate of bots about open science"**. Below, you can find instructions and hints for the code, as well as general information about the hackthon topic. The contact person for this topic is Polina.

## Code

### Installation
To get started, first, clone the repository: 
```
git clone https://github.com/polina-tsvilodub/llm-debate.git
cd llm-debate
```

If you develop locally, we strongly recommend to create a virtual environment before installing any packages. You will need to use Python >= 3.8; you can install the requirements by running: 
```
pip install -r requirements.txt
```

However, instead of developing locally, you can also run the code on [Google Colab](https://colab.google/). Execute the same steps described above to get started on Colab.
langchain (older version). 

### Running the starter code

To run the current version of the code, execute `python debate.py`. You can optionally pass various configurations, which you can inspect by executing `python debate.py --help`. 

There are two files in the repository:
* `debate.py`: entrypoint file for simulating a debate. Implements a simple class instantiating a debate object which can save meta information about the conversation and instantiates two agents.
* `utils.py`: utilities file containing a helper function for configuring OpenAI der HuggingFace models available through the API of the package LangChain (for more information on the package, see [here](https://python.langchain.com/docs/get_started/introduction.html)).
  * LLMs supported by this code are OpenAI models and models available through the Huggingface Hub. For full information about models available through the Huggingface Hub, see [here](https://huggingface.co/docs/api-inference/quicktour). For getting started, the following models might be good candidates (model names that can be passed to initialize the debate are listed): 
    * OpenAI: gpt-3.5-turbo
    * Huggigface Hub: google/flan-t5-xxl, facebook/opt-1.3b 
    * To use OpenAI models, you need to add a .env file to the directory in which you have this code. Make sure to NOT push your .env file to publich GitHub repositories. The env file should contain the variable "OPENAI_API_KEY" with the respective key. The same file should contain "HUGGINGFACEHUB_API_TOKEN" with the respective key for accessing the Huggingface Hub models.

## Additional materials 

Below, you can find links to some papers and blogposts that might help you get started.
* [Bommasani et al. 2021. On the opportunities and risks of foundation models.](https://arxiv.org/abs/2108.07258)
* [Perez et al. 2022. Discovering language model behaviors with model-written evaluations.](https://arxiv.org/pdf/2212.09251)
* [Park et al. 2023. Generative agents: interactive simulacra of human behavior.](https://arxiv.org/abs/2304.03442)