# Simple task distributor 

## Introduction

Simple task distributor utilizing the python3 concurrent.futures packages.

## usage

```
usage: task-mapper [-h] --files FILES [FILES ...] --command COMMAND
                   [--executors EXECUTORS] [--executor-type {process,thread}]

optional arguments:
  -h, --help            show this help message and exit
  --files FILES [FILES ...], -f FILES [FILES ...]
  --command COMMAND, -c COMMAND
                        Command applied to all files given.
  --executors EXECUTORS, -j EXECUTORS
                        Ammount of processes or threads allowed.
  --executor-type {process,thread}, -e {process,thread}
                        Type of Executor
```

### example:

compress all png files in a directory using optipng:
```
task-mapper --command "optipng -o2" --files *.png --executors 6
```

optional parameters: 

```
--executors/-j set number of worker threads/processes

--executor-type set type of worker, thread/process

```