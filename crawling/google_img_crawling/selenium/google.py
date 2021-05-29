# 설치한 selenium 라이브러리를 불러온다.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # 시간 지연 코드
import urllib.request # 이미지 다운로드
import ssl # SSL 인증 모듈

chromedrive = "/Users/byeonsam-yeong/Desktop/library/Python/crawling/selenium/chromedriver"

# webdriver를 이용해 다운받아놓은 chromedrive를 변수 driver에 넣는다.
driver = webdriver.Chrome(chromedrive)
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl") # 구글 이미지 주소
elem = driver.find_element_by_name("q") # 구글 검색 name="q"
elem.send_keys("조코딩") # 키보드 입력 값을 전송
elem.send_keys(Keys.RETURN)


# 이미지가 50장밖에 저장이 안된다. -> 1. 구글 스크롤 시 이미지가 생성 -> 2. 더보기 버튼 생성

# 마우스 스크롤
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

# 이미지 검색 -> 우측 큰 이미지 -> 우 클릭 후 다운로드
# elements는 여러개를 한번에 선택해서 리스트에 담는다.
# 이미지의 클래스등 동일하게 선택할 수 있는 요소 사용
# 클릭하거나 이동할때 시간이 필요    
imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1

for img in imgs:
    try:
        img.click() # 선택, 클릭
        time.sleep(2)
        # 우측 큰 이미지의 태그를 찾고 이미지 src 가져온다 -> class는 여러개의 값을 선택할 수 있으므로, 구체적으로 full xpath로 가져온다.
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src") 
        ssl._create_default_https_context = ssl._create_unverified_context # SSL 인증
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") # 이미지 다운로드, 이미지 Url, 저장하고자하는 이름
        count += 1
    except:
        pass

driver.close()