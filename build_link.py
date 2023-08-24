from faker import Faker
import random
import requests
import json
import sys

class ObjectLinkGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_object_link(self, parent_type, child_type,parent_id, child_id,counter):
        object_link = {
            "object_link_src_object_type_name": parent_type,
            "object_link_src_doc_id": f"/{parent_type}/{parent_id}/",
            "object_link_dest_doc_id": f"/{child_type}/{child_id}/",
            "object_link_id": counter,
            "object_link_src_object_id": parent_id,
            "object_link_dest_object_type_name": child_type,
            "doc_type": "object_link",
            "doc_id": f"/object_link/{counter}/",            
            "object_link_dest_object_id": child_id,
            "rev":[{
                "object_link_src_object_type_name": child_type,
                "object_link_src_doc_id": f"/{child_type}/{child_id}/",
                "object_link_dest_doc_id": f"/{parent_type}/{parent_id}/",
                "object_link_id": counter+1,
                "object_link_src_object_id": parent_id,
                "object_link_dest_object_type_name": parent_type,
                "doc_type": "object_link",
                "doc_id": f"/object_link/{counter}/rev/",            
                "object_link_dest_object_id": child_id,                
                }
            ]
            
        }
        return object_link

multi = int(sys.argv[1])

indicator_index = 2000
adversary_index = 2000
event_index = 2000
object_link = 2000

solr_url = "http://localhost:8983/solr"  # Change this URL to match your Solr setup
collection = "link_collection"



def index_documents_in_batches(solr_url, collection, documents, batch_size=10000):
    solr_url = f"{solr_url}/{collection}"
    headers = {"Content-Type": "application/json"}
    
    num_documents = len(documents)
    num_batches = (num_documents + batch_size - 1) // batch_size

    print(f"childs ready to be posted {num_documents}")

    for batch_num in range(num_batches):
        start = batch_num * batch_size
        end = min((batch_num + 1) * batch_size, num_documents)
        batch = documents[start:end]

        json_data = json.dumps(batch)

        update_url = f"{solr_url}/update/"
        response = requests.post(update_url, headers=headers, data=json_data)

        print(f"Indexed batch {batch_num + 1} ({start + 1}-{end}): {response.status_code}")

        # Commit changes to make them visible immediately (optional)
    commit_url = f"{solr_url}/update?commit=true"
    commit_response = requests.get(commit_url)
    print(commit_response.text)


# Example usage
link_generator = ObjectLinkGenerator()
num_parents = 10000000


global_object_links = []

counter = num_parents * multi 

item_types = ['indicator', 'adversary', 'signature', 'attachment', 'event']

while counter < num_parents * (multi+7):

    parent_id = 0

    random_parent_type = random.choice(item_types[:3])
    
    if random_parent_type == "indicator":
        parent_id = random.randint(1, 25000000)
    else:
        parent_id = random.randint(1, 1000000)

    print("Randomly selected item:", random_parent_type)

    max_children = random.randint(20, 2000)
    print(f"{max_children} childs to be linked to {random_parent_type}/{parent_id}")

    for index in range(1,max_children):
        random_child_type = random.choice(item_types)
        if random_parent_type == "indicator":            
            child_index = random.randint(1, 25000000)
        else:
            child_index = random.randint(1, 1000000)
                        
        global_object_links.append(link_generator.generate_object_link(random_parent_type, random_child_type, parent_id, child_index,counter))
        counter += 2
        
    if len(global_object_links) >= 100000 or counter >= num_parents * (multi+7):
        #post
        index_documents_in_batches(solr_url, collection,global_object_links,50000)
        global_object_links = []