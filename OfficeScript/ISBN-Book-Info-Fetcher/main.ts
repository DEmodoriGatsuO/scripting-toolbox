/**
 * Script Name: ISBN Lookup and Update
 * Purpose: This script fetches book information using ISBN codes from Google Books API
 *          and updates the specified worksheet with the retrieved data.
 */

// Main function to execute the script
async function main(workbook: ExcelScript.Workbook, sheetName: string = "Sheet1") {
    // Get the worksheet with the specified name
    const sheet = workbook.getWorksheet(sheetName);

    // Get the entire used data range
    const range = sheet.getUsedRange(true);

    // Check if there is any data in the used range
    if (!range) {
        console.log(`No data on this sheet.`);
        return;
    }

    // Log the address of the used range
    console.log(`Used range for the worksheet: ${range.getAddress()}`);

    // Get values from the range and process ISBN codes
    let values = range.getValues();
    range.clear();

    for (let i = 1; i < values.length; i++) {
        let isbnCode = values[i][0].toString().replace('-', '');
        let bookData: BookInfo = await fetchBookInfo(isbnCode);

        if (bookData) {
            values[i][1] = bookData.title;
            values[i][2] = bookData.imageLink;
            values[i][3] = bookData.publishedDate;
            values[i][4] = bookData.authors;
            values[i][5] = bookData.description;
            console.log(bookData);
        }
    }

    // Update the worksheet with the fetched book information
    range.setValues(values);
}

// Function to fetch book information from Google Books API
async function fetchBookInfo(isbn: string): Promise<BookInfo | null> {
    try {
        let fetchResult = await fetch('https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn);

        if (fetchResult.ok) {
            let jsonData: JSONData = await fetchResult.json();
            if (jsonData.totalItems > 0) {
                let volumeInfo = jsonData.items[0].volumeInfo;
                let bookInfo: BookInfo = {
                    title: volumeInfo.title || "",
                    imageLink: volumeInfo.imageLinks?.thumbnail || "",
                    publishedDate: volumeInfo.publishedDate || "",
                    authors: volumeInfo.authors?.join(", ") || "",
                    description: volumeInfo.description || ""
                };
                return bookInfo;
            }
        }
    } catch (error) {
        console.error(`Error fetching book info for ISBN ${isbn}: ${error}`);
    }

    return null;
}

// Interface for the fetched book information
interface BookInfo {
    title: string;
    imageLink: string;
    publishedDate: string;
    authors: string;
    description: string;
}

/**
 * An interface that matches the relevant part of the returned JSON structure from Google Books API.
 */
interface JSONData {
    totalItems: number;
    items: {
        volumeInfo: {
            title: string;
            imageLinks: {
                thumbnail: string;
            };
            publishedDate: string;
            authors: string[];
            description: string;
        };
    }[];
}
