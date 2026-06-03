import asyncio
import os
import time
import uuid
import httpx

# جلب المعلومات من الـ Secrets ديال GitHub
USER_ID = os.environ.get('GRASS_USER') # حط الـ ID ديالك فـ الـ Secret
# ملاحظة: Grass كيخدم بـ User ID ماشي الباسورد فـ السكريبتات
# إيلا كان عندك Token، بدلو فـ خانة الـ Authorization

async def send_ping():
    start_time = time.time()
    print(f"--- انطلاق التعدين لـ Grass ---")
    
    # الحلقة اللي ما كتسالاش
    while True:
        try:
            # التحقق من الوقت (5 ساعات و 50 دقيقة)
            if time.time() - start_time > 21000:
                print("--- السكربت وصل للحد الأقصى، إغلاق نظيف ---")
                break
            
            # محاكاة الاتصال
            url = "https://proxy2.getgrass.io/ping"
            payload = {
                "id": str(uuid.uuid4()),
                "user_id": USER_ID,
                "timestamp": time.time()
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload, timeout=10)
                if response.status_code == 200:
                    print(f"[{time.strftime('%H:%M:%S')}] تم إرسال الـ Ping بنجاح! النقط تتجمع...")
                else:
                    print(f"فشل الاتصال: {response.status_code}")
                    
        except Exception as e:
            print(f"خطأ: {e}")
            
        await asyncio.sleep(60) # يصيفط بينغ كل دقيقة

if __name__ == "__main__":
    asyncio.run(send_ping())
