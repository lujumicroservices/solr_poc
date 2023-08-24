from faker import Faker
import random
from datetime import datetime

from source_generator import SourceGenerator

class SignatureGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_objects(self, num_objects, startindex):
        objects = []

        source_generator = SourceGenerator()

        for i in range(1, num_objects + 1):
            obj = {
                "signature_value": self.faker.uuid4(),
                "signature_name": self.faker.uuid4(),
                "signature_type_name": "OpenIOC",
                "signature_hash": self.faker.md5(),
                "signature_description": self.faker.sentence(),
                "signature_status_name": "Active",
                "signature_created_at": datetime.utcnow().isoformat() + "Z",
                "signature_updated_at": datetime.utcnow().isoformat() + "Z",
                "related_exploit_target_count": random.randint(0, 10),
                "related_task_count": random.randint(0, 10),
                "related_adversary_count": random.randint(0, 10),
                "related_investigation_count": random.randint(0, 10),
                "related_vulnerability_count": random.randint(0, 10),
                "related_tool_count": random.randint(0, 10),
                "related_signature_count": random.randint(0, 10),
                "related_indicator_count": random.randint(0, 10),
                "related_ttp_count": random.randint(0, 10),
                "related_campaign_count": random.randint(0, 10),
                "related_malware_count": random.randint(0, 10),
                "related_attack_pattern_count": random.randint(0, 10),
                "related_attachment_count": random.randint(0, 10),
                "related_event_count": random.randint(0, 10),
                "related_report_count": random.randint(0, 10),
                "signature_last_detected_at": datetime.utcnow().isoformat() + "Z",
                "doc_type": "signature",
                "signature_published_at": datetime.utcnow().isoformat() + "Z",
                "signature_id": startindex,
                "related_asset_count": random.randint(0, 10),
                "related_identity_count": random.randint(0, 10),
                "signature_status_id": 1,
                "related_course_of_action_count": random.randint(0, 10),
                "signature_touched_at": datetime.utcnow().isoformat() + "Z",
                "doc_id": f"/signature/{startindex}/",
                "related_intrusion_set_count": random.randint(0, 10),
                "signature_type_id": 4,                
                "related_incident_count": random.randint(0, 10)                       
            }
            startindex+=1
            objects.append(obj)

        return objects

