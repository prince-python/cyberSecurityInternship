from django.shortcuts import render
import nmap

def index(request):
    return render(request, 'index.html')

def scan_result(request):
    if request.method == 'POST':
        target = request.POST.get('target')
        scanner = nmap.PortScanner()
        try:
            scanner.scan(hosts=target, arguments='-sV')

            scan_results = []
            for host in scanner.all_hosts():
                for proto in scanner[host].all_protocols():
                    ports = scanner[host][proto].keys()
                    for port in ports:
                        port_data = scanner[host][proto][port]
                        scan_results.append({
                            'port': port,
                            'state': port_data.get('state', ''),
                            'name': port_data.get('name', ''),
                            'product': port_data.get('product', ''),
                            'version': port_data.get('version', '')
                        })

            return render(request, 'result.html', {'scan_results': scan_results})
        except Exception as e:
            return render(request, 'result.html', {'error': str(e)})
    else:
        return render(request, 'index.html')
