from django.shortcuts import render,HttpResponse
import subprocess
import whois



import requests

def index(request):
    return render(request, 'index.html')

def result(request):

   if request.method == 'POST':
        query = request.POST.get('query')
        result_data = {}


        # 1. theHarvester
        try:
            harvester_cmd = f"theHarvester -d {query} -b all -l 50"
            harvester_output = subprocess.getoutput(harvester_cmd)
            result_data['harvester'] = harvester_output
        except Exception as e:
            result_data['harvester'] = f"Error running theHarvester: {e}"


            
        
        # 1. WHOIS Lookup
        try:
            whois_data = whois.whois(query)
            result_data['whois'] = whois_data.text if hasattr(whois_data, 'text') else str(whois_data)
        except Exception as e:
            result_data['whois'] = f"WHOIS failed: {e}"

        return render(request, 'result.html', {
            'query': query,
            'results': result_data 

        })


         # 3. EmailRep (if email format)
        try:
            if '@' in query:
                rep_response = requests.get(f"https://emailrep.io/{query}")
                if rep_response.status_code == 200:
                    result_data['emailrep'] = rep_response.json()
                else:
                    result_data['emailrep'] = f"EmailRep Error: {rep_response.status_code}"
            else:
                result_data['emailrep'] = "Skipped - not an email."
        except Exception as e:
            result_data['emailrep'] = f"EmailRep Exception: {e}"

        return render(request, 'result.html', {
            'query': query,
            'results': result_data
        })

        return render(request, 'index.html')
