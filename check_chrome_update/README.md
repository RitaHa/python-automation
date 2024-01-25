# Chrome Update Checker

## Overview

This script provides a simple solution to fetch the latest version of Google Chrome stable tag from the [quay.io repository](https://quay.io/repository/browser/google-chrome-stable?tab=tags). It is designed to provide notifications when the tag is updated, helping you stay informed, particularly if tests become unstable. An example use case is setting up a daily cron job for script execution, with notifications to Slack in case a new version has been released. The script will fail for two days if an update is detected.

The script utilizes the `requests` library.