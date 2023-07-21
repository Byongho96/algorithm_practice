import re

# paragrpah를 찾아 프린트
def find_print_paragraph(html: str, start_idx: int) -> int:
    end_idx = html.find('</p>', start_idx)
    paragraph = html[start_idx:end_idx]

    paragraph = re.sub(r'<[a-zA-Z| |/]+>', '', paragraph)   # 태그 지우기
    paragraph = paragraph.strip()   # 양쪽 공백 지우기
    paragraph = re.sub(r' {2,}', ' ', paragraph)    # 연속 공백 제거

    print(paragraph)

    return end_idx

# title을 찾아 프린트
def find_print_title(html: str, start_idx: int) -> int:
    end_idx = html.find('"', start_idx)
    print('title : ' + html[start_idx:end_idx])

    return end_idx

if __name__ == '__main__':
    html = input()
    
    title_idx = html.find('title="', html.find('<div', 0))  # title 속성의 시작 인덱스
    paragraph_idx = html.find('<p>', 0)                     # p 태그의 시작 인덱스

    T = len('title="')
    P = len('<p>')

    # 더 이상 title이 없을 때까지
    while title_idx != -1: 
        title_start_idx = title_idx + T
        end_idx = find_print_title(html, title_start_idx)
        title_idx = html.find('title="', html.find('<div', end_idx)) # title 속성의 시작 인덱스 업데이트

        # 다음 title 전 까지의 p를 출력
        while (paragraph_idx < title_idx) or (title_idx == -1 and paragraph_idx != -1):
            paragraph_start_idx = paragraph_idx + P
            end_idx = find_print_paragraph(html, paragraph_start_idx)
            paragraph_idx = html.find('<p>', end_idx) # p 태그의 시작 인덱스 업데이트

# import re  
  
# if __name__ == '__main__':  
#     html = input()  
  
#     # <main>제거
#     html = html[len('<main>'): -len('</main>')]  
  
#     # title 출력
#     html = re.sub(r'<div +title="([\w ]*)">', r'title : \1\n', html)  
#     html = re.sub(r'</div>', '', html)  
  
#     # p 출력
#     html = re.sub(r'<p>', '', html)  
#     html = re.sub(r'</p>', '\n', html)  
  
#     # 기타 태그 제거
#     html = re.sub(r'</?[\w ]*>', '', html)  
#     # 연속 공백 제거
#     html = re.sub(r' {2,}', ' ', html)  
#     # 양쪽 공백 제거
#     html = re.sub(r' ?\n ?', '\n', html)  
  
#     print(html)