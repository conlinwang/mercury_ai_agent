def get_response_time(url):
    if url == "learnwithhasan.com":
        return 0.5
    if url == "google.com":
        return 0.3
    if url == "openai.com":
        return 0.4
'''
from SimplerLLM.tools.rapid_api import RapidAPIClient
def get_seo_page_report(url :str):
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {
        'url': url,
    }
    api_client = RapidAPIClient() 
    response = api_client.call_api(api_url, method='GET', params=api_params)
    return response

url = 'learnwithhasan.com'
get_seo_page_report(url)
'''
