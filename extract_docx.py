from docx import Document
import sys

# 设置默认编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')

# 打开Word文档
doc = Document('青少年关系建造训练营.docx')

# 提取文本内容
content = []
for paragraph in doc.paragraphs:
    if paragraph.text.strip():
        content.append({
            'text': paragraph.text,
            'style': paragraph.style.name
        })

# 提取标题和正文
for item in content:
    print(f"Style: {item['style']}")
    print(f"Text: {item['text']}")
    print("-" * 50)