from flask import Blueprint, jsonify, request
from models.database import (
    get_dlt_draws, get_latest_dlt, get_dlt_count,
    get_ssq_draws, get_latest_ssq, get_ssq_count,
)

draw_bp = Blueprint('draw', __name__)


@draw_bp.route('/api/dlt/draws')
def dlt_draws():
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    draws = get_dlt_draws(limit, offset)
    return jsonify({'data': draws, 'total': get_dlt_count()})


@draw_bp.route('/api/dlt/latest')
def dlt_latest():
    d = get_latest_dlt()
    return jsonify({'data': d})


@draw_bp.route('/api/ssq/draws')
def ssq_draws():
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    draws = get_ssq_draws(limit, offset)
    return jsonify({'data': draws, 'total': get_ssq_count()})


@draw_bp.route('/api/ssq/latest')
def ssq_latest():
    d = get_latest_ssq()
    return jsonify({'data': d})
