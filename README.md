(to get exe file) (pip install pyinstaller or pip install --upgrade pyinstaller) (pyinstaller --onefile --windowed --hidden-import=comtypes.stream _0_ClassEditor_Main.py)
Updated Win11 support so Name Surname is automaticly filled. -added 12-12-25
Theese are specific classes that are supportet in this program. "Teams", "(+", "Extern", "Kfm", "Lager", "Büro 25"
If new class is used it needs to be manualy added in code. like "Teams", "(+", "Extern", "Kfm", "Lager", "Büro 25", "Verkauf" 
Otherwise Themas might include time like 45min that already shows that something is wrong.
Could automaticly fix the problem if extracted themas has t?\b.*?\d*\s*mins? then hide lines.