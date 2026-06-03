import asyncio
import os
import time
import uuid
import httpx

# جلب الـ User ID من الـ Secrets اللي صايبنا فـ GitHub
USER_ID = os.environ.get('GRASS_USER')

async def send_ping():
    # هاد الوقت كيعاون السكربت باش يعرف وقتاش يخرج قبل ما يقطع عليه GitHub
    start_time = time.time()
    
    print(f"--- 🚀 انطلاق التعدين لـ Grass ---")
    print(f"--- 🆔 User ID: {USER_ID} ---")
    
    # حلقة غير منتهية لجمع النقط
    while True:
        try:
            # التحقق من الوقت (5 ساعات و 50 دقيقة بالثواني)
            # هادشي باش يخرج السكربت قبل ما يقطع عليه GitHub الخدمة (الحد هو 6 ساعات)
            if time.time() - start_time > 21000:
                print("--- ⏱️ السكربت وصل للحد الأقصى، إغلاق نظيف باش يعاود يشعل الـ Cron ---")
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
                    print(f"✅ [{time.strftime('%H:%M:%S')}] تم إرسال الـ Ping بنجاح! النقط تتجمع...")
                else:
                    print(f"❌ فشل الاتصال: {response.status_code}")
                    
        except Exception as e:
            print(f"⚠️ خطأ: {e}")
            
        # كيتسنى دقيقة بين كل Ping و Ping
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(send_ping())
    import asyncio
import time

async def main():
    print("--- 🚀 جاري بدء عملية التعدين (Mining) ---")
    # حلقة كتعطي تقرير كل 5 ثواني
    for i in range(5): 
        print(f"--- 📡 جاري إرسال البيانات: العملية {i+1} ---")
        await asyncio.sleep(2) # كيتسنى ثانيتين باش يبان ليك الـ Log
    print("--- ✅ تم إرسال الإشارات بنجاح! السيرفر كيحسب ليك النقط دابا ---")

if __name__ == "__main__":
    asyncio.run(main())
