from .jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    listunique = []
    for job in jobs:
        if not job["job_type"] in listunique:
            listunique.append(job["job_type"])

    return listunique


def filter_by_job_type(jobs, job_type):
    # jobs = read(path)
    # print(jobs[5])
    listFilter = []
    for job in jobs:
        if (job["job_type"] == job_type):
            listFilter.append(job)
    return listFilter


def get_unique_industries(path):
    jobs = read(path)
    listunique = []
    for job in jobs:
        if not job["industry"] in listunique:
            if (job["industry"] != ""):
                listunique.append(job["industry"])
    return listunique


def filter_by_industry(jobs, industry):
    # jobs = read(path)
    # print(jobs[5])
    listFilter = []
    for job in jobs:
        if (job["industry"] == industry):
            listFilter.append(job)
    return listFilter


def get_max_salary(path):
    jobs = read(path)
    listunique = []
    for job in jobs:
        if not job["max_salary"] in listunique:
            if (job["max_salary"] != "" and job["max_salary"].isnumeric()):
                listunique.append(int(job["max_salary"]))
    maxValue = max(listunique)
    return maxValue


def get_min_salary(path):
    jobs = read(path)
    listunique = []
    for job in jobs:
        if not job["min_salary"] in listunique:
            if (job["min_salary"] != "" and job["min_salary"].isnumeric()):
                listunique.append(int(job["min_salary"]))
    maxValue = min(listunique)
    return maxValue


def matches_salary_range(job, salary):
    # jobs = read(path)
    # print(jobs[5])
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if (
            type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
           ):
        raise ValueError()
    if job["min_salary"] > job["max_salary"]:
        raise ValueError()
    if (type(salary) != int):
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def validação(job, salary):
    # jobs = read(path)
    # print(jobs[5])
    if "min_salary" not in job or "max_salary" not in job:
        return False
    if (
            type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
           ):
        return False
    if job["min_salary"] > job["max_salary"]:
        return False
    if (type(salary) != int):
        return False
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    listunique = []
    for job in jobs:
        if validação(job, salary) is True:
            if (job["min_salary"] <= salary <= job["max_salary"]):
                listunique.append(job)
    return listunique


# get_unique_industries('jobs.csv')
# print(get_max_salary('jobs.csv'))
# print(get_min_salary('jobs.csv'))
# filter_by_job_type('jobs.csv', 'FULL_TIME')
