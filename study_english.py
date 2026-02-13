import time
import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def format_time(seconds):
    if not seconds: return "00:00"
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def run_english_study_fix():
    print("="*60)
    print("🇺🇸 Your World in English (키 충돌 해결판)")
    print("="*60)
    print("✅ 스페이스바 충돌 문제를 해결했습니다.")
    print("✅ 이제 'a' 키를 눌러서 반복하세요! (훨씬 빠릅니다)")
    print("="*60)

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("detach", True)

    # Your World in English 동영상 목록
    target_url = "https://www.youtube.com/@yourworldinenglish/videos"

    print("\n[시스템] 채널 접속 중...")
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(target_url)

        saved_start_time = 0.0

        print("\n" + "="*50)
        print("✅ 접속 완료! 보고 싶은 영상을 클릭하세요.")
        print("--------------------------------------------------")
        print("👉 [s] 키      : '여기 저장' (Set 🚩)")
        print("👉 [a] 키      : '다시 듣기' (Again 🔄) <--- 강력 추천!")
        print("👉 [n] 키      : '다음 영상' (Next ⏭️)")
        print("👉 [q] 키      : 종료")
        print("--------------------------------------------------")
        print("💡 팁: 's' 누르고 'a' 누르면 손이 아주 편합니다.")

        while True:
            # 1. 시작점 저장 (s)
            if keyboard.is_pressed('s'):
                try:
                    current_time = driver.execute_script("return document.querySelector('video').currentTime;")
                    saved_start_time = current_time
                    print(f"\r🚩 시작점 저장: {format_time(saved_start_time)}          ", end="")
                    time.sleep(0.5)
                except:
                    pass

            # 2. 구간 반복 (a) - 스페이스바 대체
            elif keyboard.is_pressed('a'):
                try:
                    driver.execute_script(f"""
                        var v = document.querySelector('video');
                        if (v) {{ 
                            v.currentTime = {saved_start_time}; 
                            v.play(); 
                        }}
                    """)
                    print(f"\r🔄 다시 듣기: {format_time(saved_start_time)}           ", end="")
                    time.sleep(0.3) # 반응 속도 더 빠르게 조정
                except:
                    pass
            
            # 3. 다음 영상 (n)
            elif keyboard.is_pressed('n'):
                try:
                    keyboard.send('shift+n')
                    print("\n⏭️ 다음 영상으로...")
                    saved_start_time = 0.0
                    time.sleep(1.0)
                except:
                    pass

            # 4. 종료 (q)
            elif keyboard.is_pressed('q'):
                print("\n👋 종료합니다.")
                break
            
            time.sleep(0.05)

    except Exception as e:
        print(f"\n❌ 오류: {e}")
        input("엔터 키를 누르면 종료합니다...")

if __name__ == "__main__":
    run_english_study_fix()
