/**
 * Convert UNIX Timestamps
 * This Google Apps Script converts UNIX timestamps in a specified sheet to human-readable date and time.
 */

function convertUnixTimestamps() {
    // 1. Specify the sheet
    const sheetName = 'シート名を入れてね！'; // Replace with your sheet name
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  
    // 2. Get the range containing data
    const range = sheet.getDataRange();
  
    // 3. Store data from the range in an array
    let values = range.getValues();
  
    // Convert UNIX timestamps to human-readable dates
    for (let i = 1; i < values.length; i++) {
      if (Object.prototype.toString.call(values[i][0]) === '[object String]') {
        values[i][0] = convertUnixToDateTime(values[i][0]);
      }
    }
  
    // 4. Assign the updated array back to the range
    range.setValues(values);
}
  
  // Convert UNIX timestamp to human-readable date and time
  function convertUnixToDateTime(unixTimestamp) {
    const formattedDate = Utilities.formatDate(new Date(unixTimestamp), "Asia/Tokyo", "yyyy/MM/dd HH:mm:ss");
    return formattedDate;
}
  
