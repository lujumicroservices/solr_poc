from faker import Faker
import random
from datetime import datetime

class AttachmentGenerator:
    def __init__(self):
        self.faker = Faker()

    def generate_objects(self, num_objects,startindex):
        objects = []

        for j in range(1, num_objects + 1):
            obj = {
                "attachment_title": self.faker.sentence(),
                "attachment_name": self.faker.file_name(),
                "attachment_type_name": self.faker.word(),
                "attachment_path": self.faker.uuid4(),
                "attachment_file_size": str(random.randint(10000000, 99999999)),
                "attachment_placeholder": "0",
                "attachment_hash": self.faker.md5(),
                "attachment_malware_locked": "1",
                "attachment_content_type_name": self.faker.mime_type(),
                "attachment_type_id": random.randint(1, 10),
                "attachment_content_type_id": random.randint(1, 10),
                "attachment_id": startindex,
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
                "doc_type": "attachment",
                "related_asset_count": random.randint(0, 10),
                "related_identity_count": random.randint(0, 10),
                "attachment_updated_at": datetime.utcnow().isoformat() + "Z",
                "related_course_of_action_count": random.randint(0, 10),
                "attachment_published_at": datetime.utcnow().isoformat() + "Z",
                "doc_id": f"/attachment/{startindex}/",
                "related_intrusion_set_count": random.randint(0, 10),
                "attachment_created_at": datetime.utcnow().isoformat() + "Z",                
                "related_incident_count": random.randint(0, 10),
                "attachment_touched_at": datetime.utcnow().isoformat() + "Z"
            }
            startindex += 1
            objects.append(obj)

        return objects


