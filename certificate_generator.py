import hashlib
import json

def generate_certificate(name, course, date):
    certificate = {
        "name": name,
        "course": course,
        "date": date
    }

    cert_str = json.dumps(certificate, sort_keys=True)
    cert_hash = hashlib.sha256(cert_str.encode()).hexdigest()

    print("✅ Certificate Created!")
    print("Data:", certificate)
    print("Hash:", cert_hash)

    return cert_hash

if __name__ == "__main__":
    generate_certificate("Gungun", "Blockchain Fundamentals", "2025-10-29")
