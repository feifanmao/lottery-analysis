import sqlite3
import config


def get_conn():
    conn = sqlite3.connect(config.DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dlt_draws (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT UNIQUE NOT NULL,
        draw_date DATE,
        front_1 INTEGER, front_2 INTEGER, front_3 INTEGER,
        front_4 INTEGER, front_5 INTEGER,
        back_1 INTEGER, back_2 INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS ssq_draws (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue TEXT UNIQUE NOT NULL,
        draw_date DATE,
        red_1 INTEGER, red_2 INTEGER, red_3 INTEGER,
        red_4 INTEGER, red_5 INTEGER, red_6 INTEGER,
        blue INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()


# ---------- 大乐透 ----------

def insert_dlt_draw(issue, draw_date, front_nums, back_nums):
    """front_nums: list of 5 ints, back_nums: list of 2 ints"""
    conn = get_conn()
    try:
        conn.execute(
            'INSERT OR IGNORE INTO dlt_draws (issue, draw_date, front_1, front_2, front_3, front_4, front_5, back_1, back_2) VALUES (?,?,?,?,?,?,?,?,?)',
            (issue, draw_date, *front_nums, *back_nums)
        )
        conn.commit()
    finally:
        conn.close()


def get_dlt_draws(limit=100, offset=0):
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM dlt_draws ORDER BY issue DESC LIMIT ? OFFSET ?',
        (limit, offset)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_latest_dlt():
    conn = get_conn()
    row = conn.execute('SELECT * FROM dlt_draws ORDER BY issue DESC LIMIT 1').fetchone()
    conn.close()
    return dict(row) if row else None


def get_dlt_count():
    conn = get_conn()
    row = conn.execute('SELECT COUNT(*) as cnt FROM dlt_draws').fetchone()
    conn.close()
    return row['cnt']


def get_latest_dlt_issue():
    conn = get_conn()
    row = conn.execute('SELECT issue FROM dlt_draws ORDER BY issue DESC LIMIT 1').fetchone()
    conn.close()
    return row['issue'] if row else None


# ---------- 双色球 ----------

def insert_ssq_draw(issue, draw_date, red_nums, blue_num):
    """red_nums: list of 6 ints, blue_num: int"""
    conn = get_conn()
    try:
        conn.execute(
            'INSERT OR IGNORE INTO ssq_draws (issue, draw_date, red_1, red_2, red_3, red_4, red_5, red_6, blue) VALUES (?,?,?,?,?,?,?,?,?)',
            (issue, draw_date, *red_nums, blue_num)
        )
        conn.commit()
    finally:
        conn.close()


def get_ssq_draws(limit=100, offset=0):
    conn = get_conn()
    rows = conn.execute(
        'SELECT * FROM ssq_draws ORDER BY issue DESC LIMIT ? OFFSET ?',
        (limit, offset)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_latest_ssq():
    conn = get_conn()
    row = conn.execute('SELECT * FROM ssq_draws ORDER BY issue DESC LIMIT 1').fetchone()
    conn.close()
    return dict(row) if row else None


def get_ssq_count():
    conn = get_conn()
    row = conn.execute('SELECT COUNT(*) as cnt FROM ssq_draws').fetchone()
    conn.close()
    return row['cnt']


def get_latest_ssq_issue():
    conn = get_conn()
    row = conn.execute('SELECT issue FROM ssq_draws ORDER BY issue DESC LIMIT 1').fetchone()
    conn.close()
    return row['issue'] if row else None
