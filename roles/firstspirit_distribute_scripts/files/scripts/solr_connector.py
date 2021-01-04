import re
import json
import urllib.request

def extract_indexing_data(log_file):
    """Reads the rsync log_file, extract information on added/updated/deleted files
    and returns map containing a list of "changes" and a list of "deletions" """
    changes = []
    deletions = []

    with open(log_file) as f:
        for line in f:
            # relevant lines contain the part (including the single quotes):
            # '#del. path/to/file'  -> for deleted files
            # '#send path/to/file'  -> for new/updated files
            m = re.search(".*'#(.*)'", line)
            if m is not None:
                action, _, filePath = m.group(1).partition(" ")
                if action == 'del.':
                    deletions.append(filePath)
                else:
                    changes.append(filePath)

    return {"changes": changes, "deletions": deletions}

def trigger_indexer_with_post(data, indexer_url):
    """Issues a POST Request with the supplied data to the solr-indexer"""

    body = json.dumps(data).encode('utf-8')
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    req = urllib.request.Request(indexer_url, data=body, headers=headers, method='POST')
    with urllib.request.urlopen(req) as response:
        pass
    if response.status != 200:
        raise Exception(response)

def trigger_indexer_with_get(indexer_url, fair_identifier):
    """Issues a GET Request to the solr-indexer url with the fair_identifier as request parameter"""

    req = urllib.request.Request(indexer_url + '?fairIdentifier=' + fair_identifier, method='GET')
    with urllib.request.urlopen(req) as response:
        pass
    if response.status != 200:
        raise Exception(response)
