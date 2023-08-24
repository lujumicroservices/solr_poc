import pysolr
import json
from anytree import Node, RenderTree
import networkx as nx
import matplotlib.pyplot as plt


# Connect to your Solr instance
solr = pysolr.Solr('http://localhost:8983/solr/threat_library', timeout=1000)

def indexsearch():
    # Define your query
    query = {
        'q': 'doc_type:indicator AND ({!join from=object_link_src_doc_id to=doc_id method=crossCollection fromIndex=threat_library v=$pd18ffef97d score=none p87e1510a75=$p87e1510a75})',     # Query
        'fl': 'id:indicator_id,*,indicator_score,sources,id:indicator_id,type_id:indicator_type_id,status_id:indicator_status_id,hash:indicator_hash,value:indicator_value,last_detected_at:indicator_last_detected_at,expired_at:indicator_expired_at,created_at:indicator_created_at,updated_at:indicator_updated_at,description:indicator_description,expires_at:indicator_expires_at,manual_score:indicator_manual_score,generated_score:indicator_generated_score,score:indicator_score,touched_at:indicator_touched_at,published_at:indicator_published_at,type_name:indicator_type_name,status_name:indicator_status_name,import_ids:indicator_import_ids,id:source_id,source_id:source_source_id,name:source_name,type:source_type,creator_source_id:source_creator_source_id,creator_source_name:source_creator_source_name,creator_source_type:source_creator_source_type,tlp_id:source_tlp_id,tlp_name:source_tlp_name,tlp_none:source_tlp_none,created_at:source_created_at,updated_at:source_updated_at,published_at:source_published_at,[child childFilter=\"doc_type:source AND (/sources/*:*)\" fl=id:source_id,source_id:source_source_id,name:source_name,type:source_type,creator_source_id:source_creator_source_id,creator_source_name:source_creator_source_name,creator_source_type:source_creator_source_type,tlp_id:source_tlp_id,tlp_name:source_tlp_name,tlp_none:source_tlp_none,created_at:source_created_at,updated_at:source_updated_at,published_at:source_published_at limit=1000]',  # Fields to retrieve (id, title, text)
        'p87e1510a75': 'adversary_name:*juan*',
        'pd18ffef97d': '{!join from=doc_id to=object_link_dest_doc_id method=crossCollection fromIndex=threat_library v=$p87e1510a75 score=none}',
        'rows': 10             
    }


    """     query = {
    'q': '*:*',
    'fq': '{!parent which="isParent:true"}childDocType:child',
    'fl': '*',    
    } """


    # Execute the query
    results = solr.search(**query)

    # Print the results
    formatted_results = json.dumps(results.docs, indent=2)

    # Print the formatted JSON
    print(formatted_results)

def analize():
    # Define your query

    field_name = 'doc_type'

    params = {
    'q': '*:*',
    'facet': 'true',
    'facet.field': "doc_type",
    'facet.limit': -1,  # Retrieve all facet values
    'rows': 0  # We don't need actual search results, only facets
    }

    '''
    params = {
    'q': 'doc_type:"object_link" AND -doc_id:*rev/',
    'facet': 'true',
    'facet.field': "object_link_dest_object_type_name",
    'facet.limit': -1,  # Retrieve all facet values
    'rows': 0  # We don't need actual search results, only facets
    }
    '''


    

    # Execute the query
    results = solr.search(**params)

    print(json.dumps(results.facets, indent=2))



def tree():
    # Define your query
    query = {
        'q': 'doc_type:object_link AND -doc_id:*rev/',     # Query
        'rows': 1000,
        'sort': "object_link_id asc"            
    }

    # Execute the query
    results = solr.search(**query)
    # Create an undirected graph
    G = nx.Graph()
    
    node_dict = {}
    for obj in results.docs:
        parent_name = obj["object_link_src_doc_id"]
        child_name = obj["object_link_dest_doc_id"]

        #if "event" in parent_name or "event" in child_name:
        #    continue

        if parent_name not in node_dict:
            node_dict[parent_name] = parent_name        
            G.add_node(parent_name)

        if child_name not in node_dict:
            node_dict[child_name] = child_name
            G.add_node(child_name)

        G.add_edges_from([ (parent_name, child_name)])

    pos = nx.spring_layout(G)  # Spring layout
    nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_color='black')
    plt.show()



indexsearch()





