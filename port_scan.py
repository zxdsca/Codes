import os
import json
import subprocess
import socket
from collections import defaultdict

def is_host_alive(host):
    """
    Check if a host is alive by trying to resolve its A record.
    Returns True if an A record is found, False otherwise.
    """
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

def get_alive_subdomains(domain):
    """
    Reads the main JSON output file for the given domain,
    extracts all subdomains (from the grouped structure if present),
    and returns a deduplicated list of subdomains that have a valid A record.
    """
    output_dir = "outputs"
    json_file = os.path.join(output_dir, f"{domain}_scan.json")
    alive_hosts = set()
    
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
        
        # Expecting "subdomains" to be stored as:
        # "subdomains": { "data": [ { "root_domain": X, "data": [list of hosts], "total_results": Y }, ... ] }
        subdomains_groups = data.get("subdomains", {}).get("data", [])
        for group in subdomains_groups:
            hosts = group.get("data", [])
            for host in hosts:
                if is_host_alive(host):
                    alive_hosts.add(host)
    except Exception as e:
        print(f"Error reading or parsing {json_file}: {e}")
    
    return sorted(list(alive_hosts))

def save_alive_hosts_to_file(domain, alive_hosts):
    """
    Write the alive subdomains to a text file, one per line.
    """
    output_text_file = f"{domain}_alive_hosts.txt"
    try:
        with open(output_text_file, "w") as tf:
            for host in alive_hosts:
                tf.write(host + "\n")
        print(f"Saved {len(alive_hosts)} alive hosts to {output_text_file}")
    except Exception as e:
        print(f"Error writing alive hosts to file for {domain}: {e}")
    return output_text_file

def run_naabu(domain, hosts_file):
    """
    Runs naabu with the given hosts file.
    Uses -l flag for the list of hosts and -tp 10 to scan top 10 ports.
    Outputs the results in JSON lines format to a file.
    """
    output_json_file = f"{domain}_ports.json"
    command = [
        "naabu",
        "-l", hosts_file,
        "-Pn",
        "-c", "50",
        "-tp", "full",
        "-j", "-o", output_json_file  # JSON output
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Naabu error: {result.stderr}")
        return output_json_file, []
    return output_json_file, parse_naabu_output(output_json_file)

def parse_naabu_output(output_json_file):
    """
    Parse naabu JSON output file and group results by host.
    Expected output per line (example):
      {"host":"example.com","ip":"1.2.3.4","port":80,"protocol":"tcp",...}
    Returns a list of dicts grouped by host:
      [ { "host": "example.com", "ports": [80,443,...], "total_results": N }, ... ]
    """
    grouped = defaultdict(list)
    try:
        with open(output_json_file, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        obj = json.loads(line)
                        host = obj.get("host")
                        port = obj.get("port")
                        if host and port:
                            grouped[host].append(port)
                    except Exception as e:
                        print("Error parsing naabu JSON line:", e)
    except Exception as e:
        print(f"Error reading {output_json_file}: {e}")
        return []
    
    # Build the final grouped list
    final_ports = []
    for host, ports in grouped.items():
        unique_ports = sorted(list(set(ports)))
        final_ports.append({
            "host": host,
            "ports": unique_ports,
            "total_results": len(unique_ports)
        })
    return final_ports

def run_port_scan(domain):
    """
    Complete workflow for port scanning:
      1. Read the main JSON file for the domain and extract subdomains.
      2. Filter alive subdomains.
      3. Save alive hosts to a text file.
      4. Run naabu with that text file to scan top 10 ports.
      5. Parse and group the output.
      6. Merge the port scan results into the main JSON output file.
      7. Return the structured port scan data.
    """
    alive_hosts = get_alive_subdomains(domain)
    if not alive_hosts:
        print("No alive hosts found for port scanning.")
        return {"data": []}
    
    limited_hosts = alive_hosts[:5] + alive_hosts[-5:]
    
    # hosts_file = save_alive_hosts_to_file(domain, alive_hosts)
    hosts_file = save_alive_hosts_to_file(domain, limited_hosts)
    output_json_file, port_scan_data = run_naabu(domain, hosts_file)
    
    # Merge port scan results into the main JSON output file
    output_dir = "outputs"
    main_json_file = os.path.join(output_dir, f"{domain}_scan.json")
    try:
        if os.path.exists(main_json_file):
            with open(main_json_file, "r") as f:
                existing_data = json.load(f)
        else:
            existing_data = {}
        
        existing_data["port_scan"] = {"data": port_scan_data}
        
        with open(main_json_file, "w") as f:
            json.dump(existing_data, f, indent=4)
        
        print(f"Updated {main_json_file} with port scan data.")
    except Exception as e:
        print(f"Error merging port scan data into main JSON: {e}")
    
    return {"data": port_scan_data}
