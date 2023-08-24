import random
from faker import Faker
import uuid
from sentence_generator import SentenceGenerator

from source_generator import SourceGenerator



class AttributeGenerator:
    def __init__(self):
        self.faker = Faker()
        self.source_generator = SourceGenerator()
        # Create an instance of the SentenceGenerator class
        

#random_sentence = generator.generate_sentence(max_words=8)

    def generate_att(self, att_id):


        #source_generator = SourceGenerator()
        
        source = {
             
            "attribute_name":SentenceGenerator.get_next_sentence(),
            "attribute_value":SentenceGenerator.get_next_sentence(),
            "attribute_value_cs":SentenceGenerator.get_next_sentence(),
            "attribute_created_at":self.faker.iso8601() + "Z",
            "attribute_updated_at":self.faker.iso8601() + "Z",
            "attribute_indicator_id":random.randint(1, 100),
            "attribute_attribute_id":random.randint(1, 100),
            "doc_type":"attribute",
            "doc_id":f"/indicator/attribute/{uuid.uuid4()}/",            
            "attribute_id":att_id,
            "sources":self.source_generator.generate_sources(att_id,att_id, "indicator/Attribute",random.randint(1, 2))
        }
        return source
    
    def generate_atts(self,qty, att_index):
        atts = []
        for n in range(0, qty):
            atts.append(self.generate_att(att_index))
            att_index += 1
        return atts