from faker import Faker
import random
from datetime import datetime

class EventGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_objects(self, num_objects,startindex):
        objects = []

        for j in range(1, num_objects + 1):
            obj = {
                "event_description": self.faker.paragraph(),
                "event_title": f"Incident - IA{startindex}",
                "event_type_name": "Incident",
                "event_hash": self.faker.md5(),
                "event_type_id": random.randint(1, 20),
                "related_exploit_target_count": random.randint(0, 10),
                "related_task_count": random.randint(0, 10),
                "related_adversary_count": random.randint(0, 10),
                "related_investigation_count": random.randint(0, 10),
                "related_vulnerability_count": random.randint(0, 10),
                "related_tool_count": random.randint(0, 10),
                "event_published_at": datetime.utcnow().isoformat() + "Z",
                "related_signature_count": random.randint(0, 10),
                "event_happened_at": datetime.utcnow().isoformat() + "Z",
                "related_indicator_count": random.randint(0, 10),
                "related_ttp_count": random.randint(0, 10),
                "related_campaign_count": random.randint(0, 10),
                "related_malware_count": random.randint(0, 10),
                "event_updated_at": datetime.utcnow().isoformat() + "Z",
                "related_attack_pattern_count": random.randint(0, 10),
                "related_attachment_count": random.randint(0, 10),
                "related_event_count": random.randint(0, 10),
                "related_report_count": random.randint(0, 10),
                "doc_type": "event",
                "event_touched_at": datetime.utcnow().isoformat() + "Z",
                "event_created_at": datetime.utcnow().isoformat() + "Z",
                "related_asset_count": random.randint(0, 10),
                "related_identity_count": random.randint(0, 10),
                "related_course_of_action_count": random.randint(0, 10),
                "doc_id": f"/event/{startindex}/",
                "related_intrusion_set_count": random.randint(0, 10),
                "event_id": startindex,           
                "related_incident_count": random.randint(0, 10)
            }
            startindex += 1    
            objects.append(obj)

        return objects


