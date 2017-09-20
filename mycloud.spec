# -*- mode: python -*-
a = Analysis(['mycloud.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\PyInstaller\\mycloud'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mycloud.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
