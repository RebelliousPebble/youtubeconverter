# -*- mode: python -*-

block_cipher = None


a = Analysis(['converter.py'],
             pathex=['C:\\Users\\glenn\\PycharmProjects\\youtubeconverter', 'C:\Users\glenn\AppData\Local\conda\conda\envs\Py36\Lib\encodings'],
             binaries=['C:\ffmpeg-4.0-win64-static\bin\ffmpeg.exe'],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='converter',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
