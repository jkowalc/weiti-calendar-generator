
def generate_topics_for_subject(subject):
    return_dict = {}
    for class_type in subject.classes_schedule:
        if len(subject.classes_schedule[class_type]) > 1:
            return_dict[class_type.name] = {}
            for group in subject.classes_schedule[class_type]:
                topic_count = len(subject.classes_schedule[class_type][group])
                return_dict[class_type.name][group] = [[""] * topic_count]
        else:
            key = list(subject.classes_schedule[class_type].keys())[0]
            topic_count = len(subject.classes_schedule[class_type][key])
            return_dict[class_type.name] = [[""] * topic_count]
    return return_dict


def generate_topics(semester, subjects):
    topics = {'semester': semester.code}
    for subject in subjects:
        topics[subject.full_code] = generate_topics_for_subject(subject)
    return topics
