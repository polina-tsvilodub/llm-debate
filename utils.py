from dotenv import load_dotenv
import openai
import os

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import HuggingFaceHub


def init_model(model_name, **kwargs):
    """
    Helper for initializing different models as the LLM backbone.
    May require API credentials.
    
    Parameters:
    ----------
    model_name: str
        Model to be used. Has to be a model known to langchain.
    **kwargs: dict
        LLM configs for sampling. Depend on particular model.

    Returns:
    --------
    model: langchain.LLM
        Initialized model.
    """

    if model_name in ["gpt-3.5-turbo", "gpt-4"]:
        try:
            load_dotenv()
            openai.api_key = os.getenv("OPENAI_API_KEY")
        except:
            raise ValueError("OpenAI API key missing. Please add your API key to your env file with the key OPENAI_API_KEY")
        # load model
        model = ChatOpenAI(
            model_name=model_name,
            **kwargs
        )
    elif any([s in model_name for s in ["davinci", "ada", "babbage", "curie"]]):
        try:
            load_dotenv()
            openai.api_key = os.getenv("OPENAI_API_KEY")
        except:
            raise ValueError((
                "OpenAI API key missing. Please add your API "
                "key to your env file with the key OPENAI_API_KEY"
            ))
        
        model = OpenAI(
            model=model_name,
            **kwargs
        )
    elif "/" in model_name:
        load_dotenv()
        try:
            load_dotenv()
            assert os.environ["HUGGINGFACEHUB_API_TOKEN"] != "" 
        except:
            print((
                "Huggingface API token is missing! "
                "Add the token to your env file "
                "with they key HUGGINGFACEHUB_API_TOKEN"
            ))
        
        model = HuggingFaceHub(
            repo_id=model_name, 
            #model_kwargs=kwargs
        )

    else:
        raise ValueError((
            f"Unknown or incorrect model name {model_name}. "
             "See https://python.langchain.com/en/latest/modules"
             "/models/llms/integrations.html "
             "for a list of available models."
        ))
    return model