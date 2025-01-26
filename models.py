from database import db

class CVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    severity = db.Column(db.String(10), nullable=True)
    published_date = db.Column(db.String(20), nullable=True)
    last_modified_date = db.Column(db.String(20), nullable=True)

    def to_dict(self):
        """Convert the CVE object to a dictionary."""
        return {
            "cve_id": self.cve_id,
            "description": self.description,
            "severity": self.severity,
            "published_date": self.published_date,
            "last_modified_date": self.last_modified_date,
        }
