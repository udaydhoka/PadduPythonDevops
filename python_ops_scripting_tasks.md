# Python Scripting Practice Tasks for Ops / DevOps Engineers

This document contains **20 practical Python scripting tasks** designed
to evaluate the skills of an Ops/DevOps engineer with \~1 year of
experience.\
The tasks test automation thinking, system interaction, log analysis,
API usage, and infrastructure scripting.

------------------------------------------------------------------------

# Section 1: Practical Automation Tasks

## 1. Server Health Monitoring Script

Write a Python script that: - Checks CPU usage - Checks memory usage -
Checks disk usage

If any metric exceeds a threshold (example: 80%), print an alert.

**Bonus** - Send alert to email or Slack.

**Skills Tested** - psutil - condition checks - automation logic

------------------------------------------------------------------------

## 2. Log File Error Analyzer

Given a large application log file, write a script that:

-   Extracts lines containing `ERROR` or `CRITICAL`
-   Counts occurrences of each error
-   Outputs a summary report

Example output:

    ERROR Database connection failed : 12
    ERROR Timeout occurred : 5

**Skills Tested** - File handling - Regex - Dictionary usage

------------------------------------------------------------------------

## 3. Bulk Command Executor

Write a script that:

-   Reads server IPs from a file
-   SSH into each server
-   Executes a command like:

```{=html}
<!-- -->
```
    df -h

Collect outputs into a single report.

**Skills Tested** - paramiko - loops - file parsing

------------------------------------------------------------------------

## 4. Disk Usage Cleanup Script

Write a script that:

-   Scans a directory
-   Finds files older than 30 days
-   Prints them
-   Optionally deletes them

**Bonus** - Show total disk space that will be freed

**Skills Tested** - os - datetime - filesystem traversal

------------------------------------------------------------------------

## 5. REST API Data Fetcher

Write a script that:

-   Calls a public API such as:

```{=html}
<!-- -->
```
    https://jsonplaceholder.typicode.com/posts

-   Extracts specific fields
-   Saves them to a CSV file

**Skills Tested** - requests - JSON parsing - CSV writing

------------------------------------------------------------------------

## 6. Simple CLI Tool

Create a CLI tool using argparse.

Example commands:

    python server_tool.py --disk
    python server_tool.py --cpu
    python server_tool.py --memory

Each option prints the respective system metric.

**Skills Tested** - CLI arguments - modular coding

------------------------------------------------------------------------

## 7. Log Rotation Script

Write a script that:

-   Checks log file size
-   If size \> 100MB
    -   rename log file
    -   compress it

Example:

    app.log → app_2026_03_05.log.gz

**Skills Tested** - file operations - compression - automation

------------------------------------------------------------------------

## 8. Configuration File Validator

Given a JSON or YAML config file, write a script that:

Validates required fields exist:

    host
    port
    username
    timeout

If missing → print error.

**Skills Tested** - JSON/YAML parsing - validation logic

------------------------------------------------------------------------

## 9. Deployment Status Checker

Write a script that:

Checks if a service is running.

Example command:

    systemctl status nginx

Return:

    Service Running
    Service Stopped

**Skills Tested** - subprocess - command execution - output parsing

------------------------------------------------------------------------

## 10. Simple Scheduler Script

Write a script that:

-   Runs a task every 10 minutes
-   Logs execution time to a file

Example log:

    Task executed at 2026-03-05 19:30

**Skills Tested** - scheduling - logging - loops

------------------------------------------------------------------------

# Section 2: Interview‑Style DevOps Problems

## 11. Log Monitoring & Alert Script

Write a Python script that:

-   Continuously monitors a log file
-   Detects if more than N errors occur in the last 1 minute
-   Prints an alert

Example log lines:

    2026-03-05 10:02:01 INFO Service started
    2026-03-05 10:02:10 ERROR DB connection failed

**Evaluation Focus** - File reading - Time window logic - Efficient log
scanning

------------------------------------------------------------------------

## 12. Multi‑Server Disk Usage Reporter

Input file:

servers.txt

    server1
    server2
    server3

Script should:

-   SSH into each server
-   Run:

```{=html}
<!-- -->
```
    df -h

-   Collect results
-   Generate a summarized report

**Evaluation Focus** - SSH automation - Error handling - Parsing output

------------------------------------------------------------------------

## 13. Deployment Automation Script

Create a script that:

-   Pulls latest code from Git
-   Builds the project
-   Restarts the service

Example steps:

    git pull
    dotnet build
    systemctl restart myservice

**Evaluation Focus** - subprocess - automation workflow - failure
handling

------------------------------------------------------------------------

## 14. API Health Checker

Given a list of API endpoints:

    https://service1/api/health
    https://service2/api/health

Script should:

-   Call each endpoint
-   Record response time
-   Mark service as Healthy / Unhealthy

Example output:

    Service1 : Healthy (120ms)
    Service2 : Unhealthy

**Evaluation Focus** - HTTP requests - Timeout handling - Reporting

------------------------------------------------------------------------

## 15. Large Log File Analyzer

Given a 5GB log file, create a script that:

-   Finds top 10 most frequent errors
-   Shows count

Example output:

    Database connection failed : 230
    Timeout occurred : 121

**Evaluation Focus** - Efficient file reading - Memory usage -
Dictionary counting

------------------------------------------------------------------------

## 16. File Integrity Checker

Write a script that:

-   Calculates hash (MD5/SHA256) of files
-   Stores them in a file
-   Later verifies if any file changed

Example output:

    config.yml → Modified
    app.log → Unchanged

**Evaluation Focus** - hashing - file verification

------------------------------------------------------------------------

## 17. Config Deployment Validator

Before deployment, validate configuration files.

Example JSON:

    {
     "host": "localhost",
     "port": 8080
    }

Required fields:

-   host
-   port
-   timeout
-   retries

If missing → fail deployment.

**Evaluation Focus** - JSON validation - error reporting

------------------------------------------------------------------------

## 18. Parallel Server Command Runner

Given 50 servers, run a command on all:

    uptime

Script should:

-   Execute commands in parallel
-   Collect results
-   Show failures

**Evaluation Focus** - threading / multiprocessing - SSH automation -
scalability

------------------------------------------------------------------------

## 19. Automatic Log Archiver

Script should:

-   Detect logs older than 7 days
-   Compress them
-   Move them to an archive folder

Example:

    app.log → archive/app_20260301.log.gz

**Evaluation Focus** - file operations - scheduling logic

------------------------------------------------------------------------

## 20. Mini Monitoring Tool

Create a script that prints system status:

    CPU Usage : 35%
    Memory : 4GB / 8GB
    Disk : 60%

**Bonus** - Save metrics to a log file every minute

**Evaluation Focus** - system metrics - periodic tasks

------------------------------------------------------------------------

# Suggested Evaluation Criteria

When reviewing solutions, evaluate candidates on:

-   Code structure and readability
-   Error handling
-   Logging
-   CLI usability
-   Documentation
-   Efficiency for large files or multiple servers
