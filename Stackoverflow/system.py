class System:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.tags = []

    def identify_frequent_tags(self, n):
        tag_count = {}
        for question in self.questions:
            for tag in question.tags:
                if tag.name in tag_count:
                    tag_count[tag.name] += 1
                else:
                    tag_count[tag.name] = 1

        frequent_tags = sorted(tag_count, key=tag_count.get, reverse=True)[:n]
        return frequent_tags
