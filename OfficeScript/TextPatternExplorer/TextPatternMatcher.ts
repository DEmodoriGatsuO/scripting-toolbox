/*
Script Name: TextPatternMatcher
Purpose: This Office Script function takes a workbook, text, a regular expression pattern, and flags as inputs. It searches for matches of the pattern within the text using the specified flags and returns an array of matching results.

@param workbook {ExcelScript.Workbook} - The workbook context.
@param text {string} - The text to search for matches.
@param pattern {string} - The regular expression pattern to match against the text.
@param flags {string} - The flags to be applied to the regular expression pattern.

@return {string[]} - An array containing the matching results found in the text.
*/

function main(workbook: ExcelScript.Workbook, text: string, pattern: string, flags: string): string[] {
    // Create a regular expression object with the provided pattern and flags
    const regexPattern = new RegExp(pattern, flags);

    // Use the match() function of the input text to find matches based on the pattern
    const matches = text.match(regexPattern) || [];

    return matches;
}