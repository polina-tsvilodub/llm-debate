"""
Boilerplate code for building an LLM bot debate.
"""
import argparse
from utils import init_model


class BotDebate():
    """
    Debate object for running a debate between two LLMs.
    Helps to keep track of configs and the conversation.
    Uses the LancgChain package in the background; therefore,
    accepts generation parameters for the LLM as supported
    by the package's API.
    For using OpenAI models, a secret key in the .env file
    is required.
    """
    def __init__(
            self, 
            model_name, 
            debate_question="Should open science practices be enforced by research institutions? ",
            **kwargs
        ):
        """
        Parameters
        ----------
        model_name: str 
            Name of the LLM to use for both agents, 
            as expected by the package.
        debate_question: str
            Question to be debated by the agents. 
            Prepended at the beginning of the conversation.
        **kwargs: generation parameters for the LLM,
                    as accepted by the API.    
        """

        self.model_name = model_name
        self.modelA = init_model(
            model_name,
            **kwargs,
        )
        self.modelB = init_model(
            model_name,
            **kwargs,
        )
        
        # for keeping track of the conversation
        self.conversation_history = debate_question 
        # nicely formatted conversation holder
        self.conversation_history_output = debate_question

    
    def run_debate(
            self, 
            n_turns=5, 
            init_prompt = "Answer this message in a short tweet in-character. ",
        ):
        """
        Main entry point for running the discussion. 
        
        Parameters
        ----------
        n_turns: int
            Number of turns of the conversation to run.
        init_prompt: str
            Instructions appended to the conversation history.
        """
        # seed persona which are used to cast the agents into character
        seed_personaA = "You are a grumpy scientist. "
        seed_personaB = "You are a kind scientist. "

        # initialize conversation turn counter
        t = 0

        while t < n_turns:
            # first agent turn
            sentenceA = self.modelA.predict(
                text=self.conversation_history + seed_personaA + init_prompt, 
            )
            print("sentence A: ", sentenceA)
            # reply by second agent
            sentenceB = self.modelB.predict(
                text=self.conversation_history + sentenceA + seed_personaB + init_prompt, 
            )
            print("sentence B ",sentenceB)
            # update conversation history
            self.conversation_history = self.conversation_history + sentenceA + sentenceB
            # update nicely formatted conversation history
            self.conversation_history_output = self.conversation_history_output + "\n\nModel A:" + sentenceA + "\n\nModel B:" + sentenceB
            # increment turn counter 
            t += 1

        return self.conversation_history, self.conversation_history_output


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--temperature",
        type=float,
        default=0.1,
        help="Temperature for pragmatic speaker",
    )

    parser.add_argument(
        "--n_turns",
        type=int,
        default=5,
        help=(
            "How many turns of the conversation "
            "to run."
        )
    )

    parser.add_argument(
        "--model_name",
        type=str,
        default="gpt-3.5-turbo",
        help="Name of LangChain supported model",
    )

    parser.add_argument(
        "--max_tokens",
        type=int,
        default=32,
        help="Maximal number of new tokens to generate per turn.",
    )
    args = parser.parse_args()

    # print values of all arguments
    print("Arguments:")
    for arg in vars(args):
        print(f"{arg}: {getattr(args, arg)}") 

    # instantiate the debate
    debate = BotDebate(
        model_name=args.model_name,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    raw_conversation, pretty_conversation = debate.run_debate(
        n_turns=args.n_turns,
    )

    print("End of conversation: \n\n", pretty_conversation) 
    print("raw history : \n\n", raw_conversation)



