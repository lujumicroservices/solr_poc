import random

class DataGenerator:
    
    @staticmethod
    def get_random_indicator_type():
        indicator_types = [
            "ASN",
            "Binary String",
            "CIDR Block",
            "CVE",
            "Email Address",
            "Email Attachment",
            "Email Subject",
            "FQDN",
            "File Mapping",
            "File Path",
            "Filename",
            "Fuzzy Hash",
            "GOST Hash",
            "Hash ION",
            "IP Address",
            "IPv6 Address",
            "MAC Address",
            "MD5",
            "Mutex",
            "Password",
            "Registry Key",
            "SHA-1",
            "SHA-256",
            "SHA-384",
            "SHA-512",
            "Service Name",
            "String",
            "URL",
            "URL Path",
            "User-agent",
            "Username",
            "X-Mailer",
            "x509 Serial",
            "x509 Subject"
        ]
        return random.choice(indicator_types)
