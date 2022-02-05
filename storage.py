import json
# Useful links for later:
# https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
# https://www.geeksforgeeks.org/writing-to-file-in-python/#with

# 1.new class named Storage 2.in class make object x ={"departments":[]} 3. make function for object dump in json 4. field or function for object x?

class StoragePool(object):
    def __init__(self, departments = []):
        self.departments = departments
        
    def add_department(self, department):
        self.departments.append(department)
    
    def save(self):
        json_string = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        with open('storage.json', 'w') as file_output:
            file_output.write(json_string)
    
    @staticmethod
    def load():
        with open("storage.json","r") as file_input:
            penis = json.loads(file_input.read())
            return StoragePool(**penis)

class Department(object):
    def __init__(self, name, href, years = []):
        self.name = name
        self.href = href
        self.years = years
    
    def get_name(self):
        return self.name
    
    def get_href(self):
        return self.href
    
    def set_years(self, years):
        self.years = years
        
class Year(object):
    def __init__(self, year, href,semesters = []):
        self.year = year
        self.href = href
        self.semesters = semesters
    
    def get_year(self):
        return self.year
    
    def get_href(self):
        return self.href
    
    def set_semesters(self, semesters):
        self.semesters = semesters
        
class Semester(object):
    def __init__(self, semester, href,subjects = []):
        self.semester = semester
        self.href = href
        self.subjects = subjects
    
    def get_semester(self):
        return self.semester
    
    def get_href(self):
        return self.href
    
    def set_subjects(self, subjects):
        self.subjects = subjects
        
class Subject(object):
    def __init__(self, name, href,categories = [], id = ""):
        self.name = name
        self.href = href
        self.id = id # TODO: Extract ID from href
        self.categories = categories
    
    def get_name(self):
        return self.name
    
    def get_href(self):
        return self.href
    
    def get_id(self):
        return self.id
    
    def set_categories(self, categories):
        self.categories = categories

class Category(object):
    def __init__(self, name, href, description, lecturers, lectures = []):
        self.name = name
        self.href = href
        self.description = description
        self.lecturers = lecturers
        self.lectures = lectures
    
    def get_name(self):
        return self.name
    
    def get_href(self):
        return self.href
    
    def add_lecture(self, lecture):
        self.lectures.append(lecture)

class Lecture(object):
    def __init__(self, date, length, page_href = '', links = []):
        self.date = date
        self.length = length
        if len(links) == 0:
            self.links = [ Link(page_href, 'page') ]
        else:
            self.links = links
    
    def get_date(self):
        return self.date
    
    def get_length(self):
        return self.length
    
    def get_links(self):
        return self.links
    
    def add_link(self, link):
        self.links.append(link)
        
class Link(object):
    def __init__(self, href, type):
        self.href = href
        self.type = type
    
    def get_href(self):
        return self.href
    
    def get_type(self):
        return self.type
