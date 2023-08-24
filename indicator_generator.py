from faker import Faker
import random
from datetime import datetime
import json
from attribute_generator import AttributeGenerator
from data_generator import DataGenerator
from source_generator import SourceGenerator
import time




class IndicatorGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_objects(self, num_objects,startindex):
        objects = []




        source_generator = SourceGenerator()
        att_generator = AttributeGenerator()

        start_time = time.time()

        for j in range(1, num_objects + 1):
            obj = {
                "indicator_value": self.faker.domain_name(),
                "indicator_type_name": DataGenerator.get_random_indicator_type(),
                "indicator_status_name": random.choice(["Review", "Active", "Inactive"]),
                "indicator_hash": self.faker.md5(),
                "indicator_score": round(random.uniform(0, 10), 2),
                "indicator_touched_at": datetime.utcnow().isoformat() + "Z",
                "indicator_generated_score": round(random.uniform(0, 10), 2),
                "related_exploit_target_count": random.randint(0, 10),
                "indicator_updated_at": datetime.utcnow().isoformat() + "Z",
                "indicator_published_at": datetime.utcnow().isoformat() + "Z",
                "related_task_count": random.randint(0, 10),
                "related_adversary_count": random.randint(0, 10),
                "related_investigation_count": random.randint(0, 10),
                "related_vulnerability_count": random.randint(0, 10),
                "indicator_created_at": datetime.utcnow().isoformat() + "Z",
                "related_tool_count": random.randint(0, 10),
                "related_signature_count": random.randint(0, 10),
                "related_indicator_count": random.randint(0, 10),
                "related_ttp_count": random.randint(0, 10),
                "related_campaign_count": random.randint(0, 10),
                "indicator_type_id": random.randint(1, 20),
                "indicator_id": random.randint(1, 100),
                "related_malware_count": random.randint(0, 10),
                "related_attack_pattern_count": random.randint(0, 10),
                "related_attachment_count": random.randint(0, 10),
                "related_event_count": random.randint(0, 10),
                "related_report_count": random.randint(0, 10),
                "doc_type": "indicator",
                "related_asset_count": random.randint(0, 10),
                "related_identity_count": random.randint(0, 10),
                "indicator_status_id": random.randint(1, 5),
                "related_course_of_action_count": random.randint(0, 10),
                "doc_id": f"/indicator/{startindex}/",
                "related_intrusion_set_count": random.randint(0, 10),                
                "related_incident_count": random.randint(0, 10),
                "sources":  source_generator.generate_sources(startindex,startindex, "indicator",random.randint(1, 2)),      
                "attributes": att_generator.generate_atts(random.randint(1, 2),startindex)
            }
            startindex+=1
            
            objects.append(obj)

            if len(objects) % 1000 == 0:
                elapsed_time = time.time() - start_time
                print(f"{j} indicator generated in {elapsed_time:.2f} seconds")
                start_time = time.time()


        return objects

