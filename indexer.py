import requests
import json
import sys
import pickle

import concurrent.futures

from adversary_generator import AdversaryGenerator
from attachments_generator import AttachmentGenerator
from event_generator import EventGenerator
from indicator_generator import IndicatorGenerator
from signature_generator import SignatureGenerator
from source_generator import SourceGenerator
from datetime import datetime

# Define your Solr server and collection information
solr_url = "http://localhost:8983/solr"  # Change this URL to match your Solr setup
collection = "threat_library"


super_index = 0
indicator_iterations = 10
iterations = 10

def index_documents(solr_url, documents):
    for document in documents:
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps([document])
        
        # Define the Solr update URL
        update_url = f"{solr_url}/update/json/docs"

        # Send the index request
        response = requests.post(update_url, headers=headers, data=json_data)
        
        # Print the response
        print(f"Indexing document: {document['doc_id']}")
        print(response.text)

        # Commit changes to make them visible immediately (optional)
        commit_url = f"{solr_url}/update?commit=true"
        commit_response = requests.get(commit_url)
        print(commit_response.text)


def index_documents_in_batches(solr_url, collection, documents, batch_size=5000):
    solr_url = f"{solr_url}/{collection}"
    headers = {"Content-Type": "application/json"}
    
    num_documents = len(documents)
    num_batches = (num_documents + batch_size - 1) // batch_size

    for batch_num in range(num_batches):
        start = batch_num * batch_size
        end = min((batch_num + 1) * batch_size, num_documents)
        batch = documents[start:end]

        json_data = json.dumps(batch)

        update_url = f"{solr_url}/update"
        response = requests.post(update_url, headers=headers, data=json_data)

        print(f"Indexed {documents[0]['doc_type']} batch {batch_num + 1} ({start + 1}-{end}): {response.status_code}")

        # Commit changes to make them visible immediately (optional)
        commit_url = f"{solr_url}/update?commit=true"
        commit_response = requests.get(commit_url)
        print(commit_response.text)


def signatures_worker():
    signatureGenerator = SignatureGenerator()
    start_index = super_index
    for i in range(iterations):        
        print(f"{num_documents} signature will be items generated")
        signature_documents = signatureGenerator.generate_objects(num_documents,start_index)
        
        print(f"indexin signature items generated")
        index_documents_in_batches(solr_url,collection, signature_documents)

        start_index += num_documents
    

def indicator_worker():
    indicatorGenerator = IndicatorGenerator()
    start_index = (iterator_num_documents * indicator_iterations) * multi
    for i in range(indicator_iterations):

        print(f"{iterator_num_documents} indicator items will be generated")        
        indicator_documents = indicatorGenerator.generate_objects(iterator_num_documents,start_index)        

        print(f"indexin indicator_documents generated")

       # Generate a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")        
        file_name = f"indicator_{timestamp}.pk1"
        # File path to write JSON data
        file_path = file_name

        with open(file_path, 'wb') as pickle_file:
            pickle.dump(indicator_documents, pickle_file)

        #index_documents_in_batches(solr_url,collection, indicator_documents)

        start_index += iterator_num_documents
    

def adversary_worker():
    adversaryGenerator = AdversaryGenerator()
    start_index = super_index
    for i in range(iterations):
        
        print(f"{num_documents} adversary_documents items will be generated")        
        adversary_documents = adversaryGenerator.generate_objects(num_documents,start_index)
        
        print(f"indexin adversary_documents generated")
        index_documents_in_batches(solr_url,collection, adversary_documents)

        start_index += num_documents
    

def event_worker():
    eventGenerator = EventGenerator()
    start_index = super_index
    for i in range(iterations):

        print(f"{num_documents} event_documents items will be generated")        
        event_documents = eventGenerator.generate_objects(num_documents,start_index)
        
        print(f"indexin events_documents generated")
        index_documents_in_batches(solr_url,collection, event_documents)

        start_index += num_documents
    

def att_worker():
    attachmentGenerator = AttachmentGenerator()    
    start_index = super_index    
    for i in range(10):
        
        print(f"{num_documents} att_documents items will be generated")        
        att_documents = attachmentGenerator.generate_objects(num_documents,start_index)        

        print(f"indexin adversary_documents generated")
        index_documents_in_batches(solr_url,collection, att_documents)

        start_index += num_documents


def load_indi():
    # Load data from pickle file
    pickle_filename = 'indicator_2023-08-23_15-00-27.pk1'
    with open(pickle_filename, 'rb') as pickle_file:
        loaded_data = pickle.load(pickle_file)

    index_documents_in_batches(solr_url,collection, loaded_data)


iterator_num_documents = 100000
num_documents = 1000000


# create a thread pool with 2 threads
#pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
 
# submit tasks to the pool
#pool.submit(signatures_worker)
#pool.submit(indicator_worker)
#pool.submit(adversary_worker)
#pool.submit(event_worker)
#pool.submit(att_worker)
 
# wait for all tasks to complete
#pool.shutdown(wait=True)
 
sys.argv.append("2")
sys.argv.append("0")


multi = int(sys.argv[2]) 


if sys.argv[1] == "1":
    signatures_worker()

if sys.argv[1] == "2":
    indicator_worker()

if sys.argv[1] == "3":
    adversary_worker()

if sys.argv[1] == "4":
    event_worker()

if sys.argv[1] == "5":
    att_worker()

if sys.argv[1] == "6":
    load_indi()



print("Main thread continuing to run")







    












# Call the function to index the documents









