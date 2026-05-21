# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None
base_dir = r'D:\MyAIProject\大乐透'

a = Analysis(
    [os.path.join(base_dir, 'launcher.py')],
    pathex=[base_dir],
    binaries=[],
    datas=[
        (os.path.join(base_dir, 'templates'), 'templates'),
        (os.path.join(base_dir, 'static'), 'static'),
        (os.path.join(base_dir, 'config.py'), '.'),
        (os.path.join(base_dir, 'models'), 'models'),
        (os.path.join(base_dir, 'crawler'), 'crawler'),
        (os.path.join(base_dir, 'analysis'), 'analysis'),
        (os.path.join(base_dir, 'api'), 'api'),
    ],
    hiddenimports=[
        'waitress',
        'flask',
        'requests',
        'bs4',
        'lxml',
        'models.database',
        'models',
        'crawler.dlt_crawler',
        'crawler.ssq_crawler',
        'crawler',
        'analysis.frequency',
        'analysis.missing',
        'analysis.segment',
        'analysis.parity',
        'analysis.sum_value',
        'analysis.consecutive',
        'analysis.repeat',
        'analysis.ac_value',
        'analysis.span',
        'analysis',
        'api.draw',
        'api.analysis',
        'api',
        'config',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='彩票分析系统',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='彩票分析系统',
)
