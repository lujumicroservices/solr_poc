import random
from faker import Faker
import uuid

class SourceGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_source(self, source_id,parent_id, parent):
        source = {
            "source_type": "other_sources",
            "source_creator_source_name": self.faker.user_name(),
            "source_creator_source_type": "other_sources",
            "source_name": self.faker.user_name(),
            "source_creator_source_id": random.randint(1, 1000000),
            "source_indicator_id": parent_id,
            "source_updated_at": self.faker.iso8601() + "Z",
            "source_source_id": random.randint(1, 1000000),
            "doc_type": "source",
            "source_created_at": self.faker.iso8601() + "Z",
            "source_published_at": self.faker.iso8601() + "Z",
            "doc_id": f"/indicator/{parent}/{uuid.uuid4()}/",           
            "source_id": source_id
        }
        return source
    
    def generate_sources(self, source_id,parent_id, parent,num_sources):
        sources = []
        for n in range(1, num_sources):
            sources.append(self.generate_source(source_id,parent_id, parent))
            source_id += 1
        return sources