# Simple task distributor 

## Introduction

Simple task distributor utilizing the python3 concurrent.futures packages.

## usage

```
usage: task-mapper [-h] --files FILES [FILES ...] --command COMMAND
                   [--executors EXECUTORS] [--executor-type {process,thread}]
task-mapper: error: the following arguments are required: --files/-f, --command/-c
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