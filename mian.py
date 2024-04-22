from eqq import eqq
from answer import answer_dict


def get_answer_result(di: dict):
    not_yet_list = []
    answer_list = []
    length = len(answer_dict)
    anaylse = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    for value, i in zip(di.values(), range(1, length + 1)):
        if value == -1:
            not_yet_list.append(i)
        elif value == 0 or value == 1:
            answer_list.append(i)
    for answer_title, answer_num in zip(answer_dict, di.values()):
        anaylse[list(answer_title[answer_num].values())[0]] += 1
    # print("未答题", not_yet_list)
    # print("已答题", answer_list)
    return anaylse


# 答案(不止这3题，具体题目请参考answer_dict)。均为单选题，-1表示未答题，0表示第一个选项，1表示第二个选项
di = {"第1题": 1, "第2题": 0, "第3题": -1}
anaylse = get_answer_result(di)
print("分值统计", anaylse)
# 再通过分值统计的结果，得出每个题目的得分，按照得分高低列举出前3个性格类型，根据eqq的内容对每个性格类型进行分析，展示给用户。
# 这部分请你自己完善。
