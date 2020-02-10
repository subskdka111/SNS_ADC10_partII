# SNS_ADC10

## Project Title: Classroom assignment system

### Team Members:
1. Subash Khadka
2. Nitesh Manandhar
3. Shuva Shrestha
---

## Installation Guide

1. Clone Repo
2. In Command prompt `cd` to SNS_Classroom folder where _manage.py_ is located
3. Migrate all models `python manage.py migrate`
4. Create admin user `python manage.py createadmin`
5. _(Optional)_ Create modules `python manage.py createmodules`
6. Runserver `python manage.py runserver`
7. Login with admin user created in 4

## User Authorization

| Roles | Admin | Teacher | Student | Without authentication |
| ----- | ----- | ----- | ----- | ----- |
| Create User | :heavy_check_mark: | :x: | :x: | :x: |
| Create Post | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| Comment on Post | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :x: |
| Create Module | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| Enroll for Module | :x: | :x: | :heavy_check_mark: | :x: |
| Create Assignment | :heavy_check_mark: | :heavy_check_mark: | :x: | :x: |
| Post Assignment | :x: | :x: | :heavy_check_mark: | :x: |