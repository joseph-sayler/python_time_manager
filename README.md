# python_time_manager

## Goal

The goal of this project is to create a time entry system in Python.

## Documentation

[![mkdocs build](https://github.com/joseph-sayler/python_time_manager/actions/workflows/main.yml/badge.svg)](https://github.com/joseph-sayler/python_time_manager/actions/workflows/main.yml)
[![pages-build-deployment](https://github.com/joseph-sayler/python_time_manager/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://github.com/joseph-sayler/python_time_manager/actions/workflows/pages/pages-build-deployment)

Documentation available at [https://joseph-sayler.github.io/python_time_manager/](https://joseph-sayler.github.io/python_time_manager/)

## Inspiration

Currently for work, I manually manage a markdown file where I enter the date, current project, time spent on an activity, then a total at the end of the day of all time spent on all activities. I do this over and over and over... again, and thought it would be nice to have an automated way to do this!

## Plan

Right now this is very much WIP, but my thoughts are to create a core system that takes in all data and stores it in a database (sqlite for now). Once I have input figured out, then will tackle output. I will probably wrap this in a command line interface to start, but should probably make it flexible enough to use with any kind of program. The goal would be to make a web app or maybe a small desktop app to run the core components inside of.

First steps though are making the core data intake engine and saving data to a db. With that done, I can work on a simple CLI to test. Then move on to displaying data back, another front end (web app perhaps), add some extra bells and whistles, all until I have what I want!

There is a blog containing notes about my thoughts, progress I make,and ideas I have located under the documents folder.
