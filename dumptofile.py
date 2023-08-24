import json
import urllib2

# Specify the Solr endpoint URL
solr_url = 'http://localhost:8983/solr/threat_library'

# Create a Solr client
solr = pysolr.Solr(solr_url)

# Set up the query to retrieve all documents
query = 'doc_type:object_link'
page_size = 1000

# Initialize variables
offset = 0
total_documents = 100000
all_documents = []

# Paginate through the documents
while True:

    print("pages " + page_size + " size " + offset )

    url = f"{solr_url}/select?q={query}&rows={page_size}&start={offset}&wt=json"
    response = urllib2.urlopen(url)
    data = json.load(response)
    
    num_results = data['response']['numFound']
    documents = data['response']['docs']
    
    if not documents:
        break
    
    total_documents += len(documents)
    all_documents.extend(documents)
    
    offset += page_size
    
    if offset >= num_results:
        break

# Specify the output file path
output_file = 'solr_documents.json'

# Write the documents to the output file
with open(output_file, 'w') as f:
    json.dump(all_documents, f, indent=2)


print("Saved " + total_documents + " documents to " + output_file)
