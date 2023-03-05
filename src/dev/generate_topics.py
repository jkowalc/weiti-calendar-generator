
def generate_topics_for_subject(subject):
    return_dict = {}
    for class_type in subject.classes_schedule:
        if isinstance(subject.classes_schedule[class_type], dict):
            return_dict[class_type.value] = {}
            for group in subject.classes_schedule[class_type]:
                return_dict[class_type.value][group] = ["" * len(subject.classes_schedule[class_type][group])]
        else:
            return_dict[class_type.value] = ["" * len(subject.classes_schedule[class_type])]
    return return_dict


def generate_topics(semester, subjects):
    topics = {'semester': semester.code}
    for subject in subjects:
        topics[subject.full_code] = generate_topics_for_subject(subject)
    return topics
