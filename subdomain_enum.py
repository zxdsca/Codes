import os
import json
import subprocess
from collections import defaultdict

def save_root_domains_to_file(domain):
    input_file = os.path.join("outputs", f"{domain}_scan.json")
    output_text_file = f"{domain}_root_domains.txt"
    
    try:
        with open(input_file, "r") as f:
            data = json.load(f)
        
        # Extract the list of domains from the reverse_whois section
        reverse_whois = data.get("reverse_whois", {})
        domains = reverse_whois.get("domains", [])

        top_domains = domains[:10]+domains[-10:]
        # top_domains = ["coupa.com","coupadev.com"]
        
        # Write each domain to the text file, one per line
        with open(output_text_file, "w") as tf:
            for d in top_domains: #later replace with this line with domains
                tf.write(d + "\n")
                
        print(f"Extracted {len(domains)} root domains from {input_file} and saved to {output_text_file}")
    except Exception as e:
        print(f"Error in save_root_domains_to_file for {domain}: {e}")

def run_subfinder(domain):
    """
    Runs subfinder in bulk mode using the text file of root domains for the given domain.
    Then, it parses the output and merges the subdomain results into the existing JSON file.
    """
    # Define file names based on the domain
    text_file = f"{domain}_root_domains.txt"  # Root domains text file
    output_json_file = f"{domain}_subdomains.json"  # Subfinder JSON output file
    output_dir = "outputs"
    json_file = os.path.join(output_dir, f"{domain}_scan.json")
    
    # Run subfinder with the -dL flag using the text file
    command = ["subfinder", "-dL", text_file, "-oJ", "-o", output_json_file]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Subfinder error: {result.stderr}")
        return {"data": []}
    
    # Parse the subfinder output file
    # grouped = defaultdict(list)
    grouped = {}

    try:
        with open(output_json_file, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        obj = json.loads(line)
                        host = obj.get("host")
                        input_domain = obj.get("input")
                        if host and input_domain:
                            if input_domain not in grouped:
                                grouped[input_domain] = set()
                            grouped[input_domain].add(host)
                    except Exception as e:
                        print("Error parsing JSON line:", e)
    except Exception as e:
        print(f"Error reading {output_json_file}: {e}")
        return {"data": []}
    
    final_subdomains = []
    for input_domain, hosts in grouped.items():
        unique_hosts = sorted(list(hosts))
        entry = {
            "root_domain": input_domain,
            "data": unique_hosts,
            "total_results": len(unique_hosts)
        }
        final_subdomains.append(entry)
    
    # Merge the subdomain results into the existing JSON file
    try:
        if os.path.exists(json_file):
            with open(json_file, "r") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}
        
        existing_data["subdomains"] = {"data": final_subdomains}
        
        with open(json_file, "w") as f:
            json.dump(existing_data, f, indent=4)
        
        print(f"Updated {json_file} with subdomain data.")
    except Exception as e:
        print(f"Error merging subdomain data: {e}")
    
    return {"data": final_subdomains}