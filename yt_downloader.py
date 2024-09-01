import yt_dlp
from tqdm import tqdm


class YouTubeDownloader:
    def __init__(self, url, download_path=None):
        self.url = url
        self.download_path = download_path
        self.ydl_opts = {
            'format': 'best',
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook],
        }
        self.pbar = None
        self.total_bytes = None

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            if not self.pbar:
                self.total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
                self.pbar = tqdm(total=self.total_bytes, unit='B', unit_scale=True, desc="Downloading")
            self.pbar.update(d['downloaded_bytes'] - self.pbar.n)
        elif d['status'] == 'finished':
            self.pbar.close()
            print("Download complete!")

    def download_video(self):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
        except Exception as e:
            print(f'Error: {e}')


def main():
    url = input("Enter the YouTube video URL: ")
    download_path = "D:\\"
    downloader = YouTubeDownloader(url, download_path)
    downloader.download_video()


if __name__ == '__main__':
    main()
