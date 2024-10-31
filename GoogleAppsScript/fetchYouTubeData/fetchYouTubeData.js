/**
 * YouTube Video Data Fetcher
 * This Google Apps Script fetches video information from a YouTube channel and populates it in a Google Sheet.
 */

function fetchYouTubeData() {
    // Get the active spreadsheet and target sheet by name
    const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    const sheetName = 'set sheet name'; // Replace with your sheet name
    const sheet = spreadsheet.getSheetByName(sheetName);
    
    // Clear existing content from the sheet
    sheet.clearContents();
    
    // Base URL for constructing video URLs
    const youtubeUrl = "https://www.youtube.com/watch?v=";
    
    // Replace with the YouTube channel ID you want to fetch data from
    const channelId = 'Please set channel ID';
    
    // Fetch channel information
    const channel = YouTube.Channels.list([
      'snippet',
      'contentDetails',
    ], {
      'id': channelId
    });
  
    // Prepare the header row for the sheet
    const headerRow = ["Thumbnail", "Title", "Published At", "ID", "Description", "URL"];
    
    // Initialize data array with the header row
    const data = [headerRow];
    
    // Iterate through channel's items (usually just one)
    for (const item of channel.items) {
      const contentDetails = item.contentDetails;
      const playlistId = contentDetails.relatedPlaylists.uploads;
      
      // Fetch video IDs from the channel's playlist
      const videoIds = getAllVideoIds(playlistId);
      
      // Fetch detailed video information using video IDs
      const videos = getVideoDetails(videoIds);
      
      // Populate data array with video information
      for (const video of videos) {
        const videoData = [
          video.snippet.thumbnails.default.url,
          video.snippet.title,
          Utilities.formatDate(new Date(video.snippet.publishedAt), "Asia/Tokyo", "yyyy/MM/dd HH:mm:ss"),
          video.id,
          video.snippet.description,
          youtubeUrl + video.id
        ];
        data.push(videoData);
      }
      
      // Write data array to the sheet
      sheet.getRange(1, 1, data.length, headerRow.length).setValues(data);
    }
  }
  
  // Recursively fetch all video IDs from a playlist
  function getAllVideoIds(playlistId, pageToken = null) {
    const playlistItemsInfo = YouTube.PlaylistItems.list(['contentDetails'], {
      'playlistId': playlistId,
      'maxResults': 50,
      pageToken,
    });
  
    const videoIds = playlistItemsInfo.items.map(item => item.contentDetails.videoId);
    const nextPageToken = playlistItemsInfo.nextPageToken;
  
    if (nextPageToken) {
      return [...videoIds, ...getAllVideoIds(playlistId, nextPageToken)];
    } else {
      return videoIds;
    }
  }
  
  // Fetch detailed video information using video IDs
  function getVideoDetails(videoIds) {
    const batchSize = 50; // Number of videos to fetch in one request
    let videos = [];
  
    for (let i = 0; i < videoIds.length; i += batchSize) {
      const batchVideoIds = videoIds.slice(i, i + batchSize).join(',');
      const videoInfo = YouTube.Videos.list(['snippet', 'statistics'], {
        'id': batchVideoIds,
      });
      videos.push(...videoInfo.items);
    }
  
    return videos;
  }
  