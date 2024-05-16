import os
from langchain_core.runnables.base import RunnableSequence
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short Summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=os.environ.get("OPENAI_API_KEY"))

    sequence  = RunnableSequence(summary_prompt_template | llm)
    mock = True
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/manoj-kumar-thangaraj-1b7b2054/', mock=mock)
    res = sequence.invoke({"information":linkedin_data})
    print(res)
    