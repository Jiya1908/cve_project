from flask import Blueprint, jsonify, request
from models import CVE

cve_blueprint = Blueprint('cve', __name__)

@cve_blueprint.route('/cves/list', methods=['GET'])
def get_cves():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    cves = CVE.query.paginate(page, per_page, error_out=False)

    return jsonify({
        "total_records": cves.total,
        "data": [cve.to_dict() for cve in cves.items]
    })

@cve_blueprint.route('/cves/<cve_id>', methods=['GET'])
def get_cve_details(cve_id):
    cve = CVE.query.filter_by(cve_id=cve_id).first()
    if not cve:
        return jsonify({"error": "CVE not found"}), 404

    return jsonify(cve.to_dict())
