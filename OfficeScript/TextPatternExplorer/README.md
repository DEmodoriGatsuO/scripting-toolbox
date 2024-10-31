# Text Pattern Explorer

Text Pattern Explorer is a simple Office Script project that provides a function to search for and extract text patterns using regular expressions. This project aims to simplify the process of finding specific patterns within text data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Text Pattern Explorer is a tool built using Office Script that allows you to easily find and extract text patterns from a given input text. It utilizes regular expressions to perform pattern matching, providing users with a flexible way to search for specific text patterns.

## Features

- Search for text patterns using regular expressions.
- Specify custom flags for regular expression matching.
- Extract matching results from the input text.

## Usage

The `findPatternMatches` function accepts the following parameters:

- `workbook` (ExcelScript.Workbook): The workbook context.
- `text` (string): The text to search for matches.
- `pattern` (string): The regular expression pattern to match against the text.
- `flags` (string): The flags to be applied to the regular expression pattern.

The function returns an array of matching results found in the text.