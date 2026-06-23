import os
import time
import imageio_ffmpeg
import yt_dlp

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# یه کلاس لاگر ساده برای اینکه جزییات yt_dlp رو مستقیم بیاره تو ترمینال شما
class MyLogger:
    def debug(self, msg):
        # برای اینکه ترمینال خیلی شلوغ نشه فقط لاگ‌های مهم رو نشون میدیم
        if "debug" in msg.lower() or "download" in msg.lower():
            print(f"⚙️ [yt-dlp DEBUG]: {msg}")

    def info(self, msg):
        print(f"ℹ️ [yt-dlp INFO]: {msg}")

    def warning(self, msg):
        print(f"⚠️ [yt-dlp WARNING]: {msg}")

    def error(self, msg):
        print(f"❌ [yt-dlp ERROR]: {msg}")


def download_video(link, quality, max_retries=3):
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    outtmpl = os.path.join(DOWNLOAD_DIR, '%(title)s_%(id)s.%(ext)s')
    
    for attempt in range(max_retries):
        try:
            ydl_opts = {
                'format': f'bestvideo[height<={quality}]+bestaudio/best',
                'outtmpl': outtmpl,
                'merge_output_format': 'mp4',
                'ffmpeg_location': ffmpeg_path,
                
                # --- 🔍 تنظیمات مانیتورینگ و لاگ شدید ---
                'quiet': False,             # خاموش کردن حالت سکوت
                'verbose': True,            # فعال کردن پرحرفی برای دیدن جزییات اتصال
                'logger': MyLogger(),       # وصل کردن به لاگر بالا
            }
            
            print(f"\n🚀 Starting video download attempt {attempt + 1}...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=True)
                filename = ydl.prepare_filename(info)
                
                if os.path.exists(filename):
                    return filename
                
                base = os.path.splitext(filename)[0]
                mp4_file = base + ".mp4"
                if os.path.exists(mp4_file):
                    return mp4_file
                
                raise Exception(f"File not found: {filename}")
        
        except Exception as e:
            print(f"💥 Attempt {attempt + 1} failed with Python Exception: {e}")
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"⏳ Waiting {wait}s before next retry...")
                time.sleep(wait)
            else:
                raise

def download_audio(link, max_retries=3):
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
    outtmpl = os.path.join(DOWNLOAD_DIR, '%(title)s_%(id)s.%(ext)s')
    
    for attempt in range(max_retries):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': outtmpl,
                'ffmpeg_location': ffmpeg_path,
                'quiet': False,
                'verbose': True,
                'logger': MyLogger(),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            
            print(f"\n🚀 Starting audio download attempt {attempt + 1}...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=True)
                base = os.path.splitext(ydl.prepare_filename(info))[0]
                mp3_file = base + ".mp3"
                
                if os.path.exists(mp3_file):
                    return mp3_file
                
                raise Exception(f"MP3 file not found")
        
        except Exception as e:
            print(f"💥 Attempt {attempt + 1} failed with Python Exception: {e}")
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                time.sleep(wait)
            else:
                raise