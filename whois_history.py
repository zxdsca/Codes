import requests
import json, re
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

API_KEY = "AIzaSyB82zt_C7hsuKoBp-HNSoL4V4E5XOy_mSc"
MODEL = "models/gemini-2.0-flash"
llm = ChatGoogleGenerativeAI(api_key=API_KEY, model=MODEL, temperature=0)

def get_whois_history(domain):
    print(f"Fetching WHOIS history for {domain}")
    whois_url = f"https://api.whoxy.com/?key=e9ddbbd683d80d4xp03bcd61620bf20e&history={domain}&format=json"

    try:
        response = requests.get(whois_url)
        response.raise_for_status()
        whois_data = response.json()
    except requests.RequestException as e:
        print(f"HTTP request failed for {domain}: {e}")
        return {"domain": domain, "registrant_email": "", "Org_name": ""}
    except ValueError as e:
        print(f"Failed to parse JSON for {domain}: {e}")
        return {"domain": domain, "registrant_email": "", "Org_name": ""}
    
    response_schemas = [
        ResponseSchema(name="registrant_email", description="The registrant email from the WHOIS data"),
        ResponseSchema(name="Org_name", description="The company or organization name from the WHOIS data")
        ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    safe_format_instructions = format_instructions.replace("{", "{{").replace("}", "}}")

    template = (
        "Analyze the following WHOIS history JSON data and identify the registrant email and company name.\n"
        "Ignore privacy protection services like 'Domains By Proxy, LLC'. Only show official registration information.\n"
        "Return your answer strictly as valid JSON following the format below:\n"
        f"{safe_format_instructions}\n\n"
        "JSON data: {whois_data}"
        )
    prompt_template = PromptTemplate(template=template, input_variables=["whois_data"])
    chain = LLMChain(llm=llm, prompt=prompt_template)

    try:
        ai_response = chain.invoke({"whois_data": json.dumps(whois_data)})
    except Exception as e:
        print(f"LLM invocation failed for {domain}: {e}")
        return {"domain": domain, "registrant_email": "", "Org_name": ""}
    
    if isinstance(ai_response, dict) and "text" in ai_response:
        output_text = ai_response["text"]
    else:
        output_text = ai_response

    output_text = re.sub(r"```(?:json)?\n(.*?)\n```", r"\1", output_text, flags=re.DOTALL).strip()
    
    try:
        parsed_output = output_parser.parse(output_text)
    except Exception as e:
        print("Failed to parse AI response:", e)
        parsed_output = {"registrant_email": "", "Org_name": ""}
    
    return {
        "domain": domain,
        "registrant_email": parsed_output["registrant_email"],
        "Org_name": parsed_output["Org_name"]
        }
