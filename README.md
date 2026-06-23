# YouTube Downloader Bot

A Telegram bot that allows users to download YouTube videos or extract audio from YouTube links with just a few clicks.

## Features

- Download YouTube videos
- Extract audio from YouTube videos
- Multiple video quality options (360p, 720p, 1080p)
- Support for YouTube Shorts
- Fast and user-friendly interface
- Automatic file cleanup after download
- Multi-user support
- Built with Python and pyTelegramBotAPI

## How It Works

### Video Download

1. Start the bot
2. Select **Download Video**
3. Send a YouTube link
4. Choose the desired quality
5. Receive the downloaded video

### Audio Extraction

1. Start the bot
2. Select **Extract Audio**
3. Send a YouTube link
4. Receive the audio file

## Supported Content

- YouTube Videos
- YouTube Shorts

## Technologies Used

- Python
- pyTelegramBotAPI
- yt-dlp

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd youtube-downloader-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=your_bot_token
```

Run the bot:

```bash
python main.py
```

## Project Structure

```text
.
├── handlers/
├── keyboards/
├── utils/
├── main.py
└── requirements.txt
```

## License

This project is licensed under the MIT License.
