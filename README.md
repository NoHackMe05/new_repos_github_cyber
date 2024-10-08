# Script to Extract and Save New GitHub Repositories in Cybersecurity

This Python script is designed to query the GitHub API to retrieve and save new cybersecurity-related repositories created in the last 7 days. The results are saved in a JSON file.

## Features

- Search for cybersecurity-related GitHub repositories with more than 10 stars.
- Filter repositories created within the last 7 days.
- Save results in a JSON file.

## Prerequisites

- Python 3.x
- Requests library
- `json` library

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/NoHackMe05/new_repos_github_cyber.git
    cd new_repos_github_cyber
    ```

2. Install the necessary dependencies:

    ```
    pip install requests
    ```

## Usage

To run the script manually, use the following command:

```
python extract_new_repos.py
```
