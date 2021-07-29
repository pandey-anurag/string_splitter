import re

class TagManipulator():    
    def __parse_string(self, tags, regex=""):
        result_list = []

        tempResult = re.split( regex, tags )
        for result in tempResult:
            if len(result) > 0:
                result_list.append(result) 
        return result_list

    def parse_string(self, tags):
        if len(tags) > 0:
            results = []
            tags = tags.split(",")
            for tag in tags:
                if len(tag) > 0:
                    results.append(tag.strip())
            return results
        return list(tags)