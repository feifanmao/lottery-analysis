from flask import Blueprint, jsonify, request
from models.database import get_dlt_draws, get_ssq_draws
from analysis.frequency import analyze_dlt_frequency, analyze_ssq_frequency
from analysis.missing import analyze_dlt_missing, analyze_ssq_missing
from analysis.segment import analyze_dlt_segment, analyze_ssq_segment
from analysis.parity import analyze_dlt_parity, analyze_ssq_parity
from analysis.sum_value import analyze_dlt_sum, analyze_ssq_sum
from analysis.consecutive import analyze_dlt_consecutive, analyze_ssq_consecutive
from analysis.repeat import analyze_dlt_repeat, analyze_ssq_repeat
from analysis.ac_value import analyze_dlt_ac, analyze_ssq_ac
from analysis.span import analyze_dlt_span, analyze_ssq_span

analysis_bp = Blueprint('analysis', __name__)


def _get_draws(lottery, limit=200):
    if lottery == 'dlt':
        return get_dlt_draws(limit)
    return get_ssq_draws(limit)


@analysis_bp.route('/api/analysis/frequency')
def frequency():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_frequency(draws))
    return jsonify(analyze_ssq_frequency(draws))


@analysis_bp.route('/api/analysis/missing')
def missing():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_missing(draws))
    return jsonify(analyze_ssq_missing(draws))


@analysis_bp.route('/api/analysis/segment')
def segment():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_segment(draws))
    return jsonify(analyze_ssq_segment(draws))


@analysis_bp.route('/api/analysis/parity')
def parity():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_parity(draws))
    return jsonify(analyze_ssq_parity(draws))


@analysis_bp.route('/api/analysis/sum')
def sum_value():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_sum(draws))
    return jsonify(analyze_ssq_sum(draws))


@analysis_bp.route('/api/analysis/consecutive')
def consecutive():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_consecutive(draws))
    return jsonify(analyze_ssq_consecutive(draws))


@analysis_bp.route('/api/analysis/repeat')
def repeat():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_repeat(draws))
    return jsonify(analyze_ssq_repeat(draws))


@analysis_bp.route('/api/analysis/ac')
def ac_value():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_ac(draws))
    return jsonify(analyze_ssq_ac(draws))


@analysis_bp.route('/api/analysis/span')
def span():
    lottery = request.args.get('lottery', 'dlt')
    draws = _get_draws(lottery)
    if lottery == 'dlt':
        return jsonify(analyze_dlt_span(draws))
    return jsonify(analyze_ssq_span(draws))
