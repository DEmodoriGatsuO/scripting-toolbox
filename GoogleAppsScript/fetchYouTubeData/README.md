# YouTube Video Data Fetcher

The "YouTube Video Data Fetcher" is a Google Apps Script that fetches video information from a YouTube channel and populates it in a Google Sheet. This script uses the YouTube Data API to retrieve video data and formats it into a structured sheet.

## How to Use

1. Open your Google Sheets document where you want to populate the YouTube video data.

2. In the Google Sheets menu, go to Extensions > Apps Script. This will open the Google Apps Script editor.

3. Replace the placeholder values in the script with your specific values:
   - Replace `'シート名を入れてください！'` with the name of the sheet where you want to populate the data.
   - Replace `'取得したいchannelのIDをセットする箇所です'` with the actual YouTube channel ID you want to fetch data from.

4. Save the script by clicking on the floppy disk icon or pressing `Ctrl + S` (Windows) or `Command + S` (Mac).

5. Run the `fetchYouTubeData` function by clicking the play button (▶️) in the Google Apps Script editor.

6. The script will fetch the video data from the specified YouTube channel and populate it in the specified sheet.

## Note

- Ensure that you have enabled the YouTube Data API in your Google Cloud Console and obtained the necessary API credentials before using this script.

- The script uses the YouTube Data API to fetch video information. You might encounter limitations based on API quotas and request limits.

- The script includes comments to guide you through the code and help you customize it according to your needs.

## License

hogehoge