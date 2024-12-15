from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# 読み込み用のPDFファイル
input_file = open('/home/nao/HackU/PDF2text/koyoukeiyaku.pdf', 'rb')
# 書き込み用のテキストファイル
output_file = open('/home/nao/HackU/PDF2text/output.txt', 'w')

# Layout Analysisのパラメーターを設定
laparams = LAParams()
laparams

# 共有リソースを格納するPDFリソースマネージャーオブジェクトを作成
resource_manager = PDFResourceManager()
resource_manager 

# テキストに変換
device = TextConverter(resource_manager, output_file, laparams=laparams)
device

# ページの内容を処理するためのPDFインタプリタオブジェクトを作成
interpreter = PDFPageInterpreter(resource_manager, device)
interpreter

# ドキュメントに含まれる各ページを処理
for page in PDFPage.get_pages(input_file):
    interpreter.process_page(page)

