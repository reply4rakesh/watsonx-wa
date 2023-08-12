from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.chains.question_answering import load_qa_chain
from genai.model import Credentials
from genai.schemas import GenerateParams
from genai.extensions.langchain.llm import LangChainInterface
from dotenv import load_dotenv
from os import environ



import os, getpass, json
from pandas import read_json
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes

from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods

from ibm_watson_machine_learning.foundation_models import Model

#from rouge_score import rouge_scorer
#from collections import defaultdict
import numpy as np



def getAnswer(query):
    credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": "SRQvmoaqVYVSrZL44eJc3J9jznJwcqsWym6exlrcRkSm"
    }
    project_id = "dd74a4f3-48ee-44df-b5f2-fa2bd13f4d69"


    model_id = ModelTypes.FLAN_UL2

    #instruction = f"""Summarize the Input text.\\n\\nInput:\\nif you choose to create an account then the minimum we ask is that you choose a unique username and password use a web browser that accepts session cookies and provide a verified email address.\\n\\nOutput:\\nthe service allows you to use pseudonyms.\\n\\nInput:\\nany other information requested such as your real name is optional unless you are accepting these terms on behalf of a legal entity in which case we need more information about the legal entity or if you opt for a paid account in which case additional information will be necessary for billing purposes.\\n\\nOutput:\\nyou agree to provide your full legal name when you register to the service. it does not prevent you from using a pseudonym.\\n\\nInput:\\nnpm services may provide information and software that is inaccurate incomplete misleading illegal offensive or otherwise harmful.\\n\\nOutput:\\nthe service does not guarantee accuracy or reliability of the information provided.\\n\\nInput:\\ndevice information. in addition to log data we may also collect information about the device you re using pinterest on including what type of device it is what operating system you re using device settings unique device identifiers and crash data. whether we collect some or all of this information often depends on what type of device you re using and its settings. for example different types of information are available depending on whether you re using a mac or a pc or an iphone or an android phone. to learn more about what information your device makes available to us please also check the policies of your device manufacturer or software provider.\\n\\nOutput:\\nthe service may use tracking pixels web beacons browser fingerprinting and or device fingerprinting on users.\\n\\nInput:\\nyou may optionally add other information to your account such as a profile name and profile picture. this information is end to end encrypted.\\n """

    

    parameters = {
        GenParams.MAX_NEW_TOKENS: 50,
        GenParams.MIN_NEW_TOKENS:10,
        GenParams.DECODING_METHOD: DecodingMethods.GREEDY,
        #GenParams.RANDOM_SEED:33,
        GenParams.REPETITION_PENALTY:2
    
    }


    model = Model(
        model_id=model_id,
        params=parameters,    credentials=credentials,
        project_id=project_id)
    loader = PyPDFDirectoryLoader('Dengue.pdf')

    documents = loader.load()

#instruction=documents[0]
    instruction=""
    for i in range(len(documents)):
        sample=str(documents[i])
        st=sample.index('page_content')+13
        end=sample.index('metadata')
        instruction+=str(sample[st:end])


    #results.append(model.generate_text(prompt="".join([instruction+few_shot_examples[0], input_text])))
    #input_text="list down the symptoms of dengue each seperated by ',' "
    #input_text="list down the types of diabetes each seperated by ',' "
    input_text=query

    results=(model.generate_text(prompt="".join([instruction,input_text])))



#results = []

   
    return results 


# if __name__ == '__main__':
#     getAnswer("What is the rating of IBM?")

