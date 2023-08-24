from faker import Faker
import random
from datetime import datetime

class AdversaryGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_objects(self, num_objects,startindex):
        objects = []

        for j in range(1, num_objects + 1):
            obj = {
                "adversary_name": self.faker.user_name(),
                "related_exploit_target_count": random.randint(0, 10),
                "related_task_count": random.randint(0, 10),
                "related_adversary_count": random.randint(0, 10),
                "related_investigation_count": random.randint(0, 10),
                "related_vulnerability_count": random.randint(0, 10),
                "related_tool_count": random.randint(0, 10),
                "related_signature_count": random.randint(0, 10),
                "related_indicator_count": random.randint(0, 10),
                "adversary_created_at": datetime.utcnow().isoformat() + "Z",
                "related_ttp_count": random.randint(0, 10),
                "related_campaign_count": random.randint(0, 10),
                "related_malware_count": random.randint(0, 10),
                "related_attack_pattern_count": random.randint(0, 10),
                "adversary_touched_at": datetime.utcnow().isoformat() + "Z",
                "related_attachment_count": random.randint(0, 10),
                "adversary_updated_at": datetime.utcnow().isoformat() + "Z",
                "related_event_count": random.randint(0, 10),
                "related_report_count": random.randint(0, 10),
                "adversary_published_at": datetime.utcnow().isoformat() + "Z",
                "doc_type": "adversary",
                "adversary_id": startindex,
                "related_asset_count": random.randint(0, 10),
                "related_identity_count": random.randint(0, 10),
                "related_course_of_action_count": random.randint(0, 10),
                "doc_id": f"/adversary/{startindex}/",
                "related_intrusion_set_count": random.randint(0, 10),                
                "related_incident_count": random.randint(0, 10)
            }
            startindex += 1
            objects.append(obj)

        return objects


